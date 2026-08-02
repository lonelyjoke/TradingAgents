"""Shared helpers for invoking an agent with structured output and a graceful fallback.

The Portfolio Manager, Trader, and Research Manager all follow the same
canonical pattern:

1. At agent creation, wrap the LLM with ``with_structured_output(Schema)``
   so the model returns a typed Pydantic instance. If the provider does
   not support structured output (rare; mostly older Ollama models), the
   wrap is skipped and the agent uses free-text generation instead.
2. At invocation, run the structured call and render the result back to
   markdown. If the structured call itself fails for any reason
   (malformed JSON from a weak model, transient provider issue), fall
   back to a plain ``llm.invoke`` so the pipeline never blocks.

Centralising the pattern here keeps the agent factories small and ensures
all three agents log the same warnings when fallback fires.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable, Optional, TypeVar

from pydantic import BaseModel

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


def _configured_language_repair_instruction() -> str:
    """Keep schema-repair retries in the configured reader-facing language."""

    try:
        from tradingagents.dataflows.config import get_config

        language = str(get_config().get("output_language", "English") or "English")
    except Exception:
        language = "English"
    if language.strip().lower() == "english":
        return ""
    return (
        f" Every reader-facing prose field must be written in {language}. "
        "Translate upstream prose by meaning; preserve ticker symbols, source IDs, "
        "metric abbreviations and units, but do not preserve full English sentences."
    )


def _response_text(response: Any) -> str:
    content = getattr(response, "content", response)
    if isinstance(content, list):
        return "\n".join(
            str(item.get("text", ""))
            if isinstance(item, dict) and item.get("type") == "text"
            else str(item)
            if isinstance(item, str)
            else ""
            for item in content
        )
    if isinstance(content, dict):
        return json.dumps(content, ensure_ascii=False)
    return str(content or "")


def _json_object(text: str) -> dict[str, Any]:
    cleaned = str(text or "").strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.I).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    try:
        value = json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.S)
        if not match:
            raise
        value = json.loads(match.group(0))
    if not isinstance(value, dict):
        raise ValueError("structured fallback must return one JSON object")
    return value


def _compact_validation_error(exc: Exception, limit: int = 24) -> str:
    """Return only the actionable schema paths for a follow-up repair."""

    errors = getattr(exc, "errors", None)
    if not callable(errors):
        return str(exc)[:6000]
    rows: list[str] = []
    try:
        details = errors(include_url=False, include_context=False)
    except TypeError:
        details = errors()
    for row in details[:limit]:
        location = ".".join(str(part) for part in row.get("loc", ())) or "<root>"
        rows.append(f"- {location}: {row.get('msg', row.get('type', 'invalid'))}")
    remaining = max(len(details) - limit, 0)
    if remaining:
        rows.append(f"- ... {remaining} additional validation issues")
    return "\n".join(rows)


def _schema_prompt(prompt: Any, schema: type[T]) -> Any:
    instruction = f"""

STRUCTURED OUTPUT CONTRACT
Return exactly one JSON object and no Markdown fences or commentary. The object
must validate against this JSON Schema. Keep narrative fields in the requested
report language. Do not omit required fields and do not invent facts to satisfy
the schema.
{json.dumps(schema.model_json_schema(), ensure_ascii=False, separators=(',', ':'))}
"""
    if isinstance(prompt, str):
        return prompt + instruction
    if isinstance(prompt, list):
        return [*prompt, {"role": "user", "content": instruction}]
    if hasattr(prompt, "to_messages"):
        return [*prompt.to_messages(), {"role": "user", "content": instruction}]
    return f"{prompt}{instruction}"


class SchemaPromptValidationError(ValueError):
    """Keep the model's invalid JSON so repair does not repeat the full prompt."""

    def __init__(self, message: str, raw_response: str, cause: Exception):
        super().__init__(message)
        self.raw_response = raw_response
        self.cause = cause


class SchemaPromptStructured:
    """Schema-validated JSON generation without provider tool_choice."""

    structured_mode = "schema_prompt_structured"

    def __init__(self, llm: Any, schema: type[T]):
        self.llm = llm
        self.schema = schema

    def invoke(self, prompt: Any) -> T:
        response = self.llm.invoke(_schema_prompt(prompt, self.schema))
        raw_response = _response_text(response)
        try:
            return self.schema.model_validate(_json_object(raw_response))
        except Exception as exc:
            raise SchemaPromptValidationError(
                "schema-prompt response failed validation:\n"
                + _compact_validation_error(exc),
                raw_response,
                exc,
            ) from exc


def _schema_repair_contract(schema: type[T], exc: Exception) -> dict[str, Any]:
    """Return the smallest useful schema fragment for a validation repair."""

    full_schema = schema.model_json_schema()
    errors = getattr(exc, "errors", None)
    if not callable(errors):
        return full_schema
    try:
        details = errors(include_url=False, include_context=False)
    except TypeError:
        details = errors()
    fields = {
        str(row.get("loc", ())[0])
        for row in details
        if row.get("loc") and isinstance(row.get("loc", ())[0], str)
    }
    properties = full_schema.get("properties", {})
    if not fields or len(fields) > 10 or not fields.issubset(properties):
        return full_schema

    selected = {name: properties[name] for name in properties if name in fields}
    contract: dict[str, Any] = {
        "type": full_schema.get("type", "object"),
        "properties": selected,
        "required": [
            name for name in full_schema.get("required", []) if name in fields
        ],
    }
    if "additionalProperties" in full_schema:
        contract["additionalProperties"] = full_schema["additionalProperties"]

    definitions = full_schema.get("$defs", {})
    referenced: set[str] = set()

    def collect_refs(value: Any) -> None:
        if isinstance(value, dict):
            ref = value.get("$ref")
            if isinstance(ref, str) and ref.startswith("#/$defs/"):
                name = ref.rsplit("/", 1)[-1]
                if name not in referenced:
                    referenced.add(name)
                    collect_refs(definitions.get(name, {}))
            for child in value.values():
                collect_refs(child)
        elif isinstance(value, list):
            for child in value:
                collect_refs(child)

    collect_refs(selected)
    if referenced:
        contract["$defs"] = {
            name: definitions[name] for name in definitions if name in referenced
        }
    return contract


def _validation_cause(exc: Exception) -> Exception:
    return exc.cause if isinstance(exc, SchemaPromptValidationError) else exc


def _is_thinking_tool_choice_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return "tool_choice" in message and any(
        token in message for token in ("thinking", "reason", "not support")
    )


def bind_structured(llm: Any, schema: type[T], agent_name: str) -> Optional[Any]:
    """Return ``llm.with_structured_output(schema)`` or ``None`` if unsupported.

    Logs a warning when the binding fails so the user understands the agent
    will use free-text generation for every call instead of one-shot fallback.
    """
    try:
        return llm.with_structured_output(schema)
    except (NotImplementedError, AttributeError) as exc:
        if not _is_thinking_tool_choice_error(exc):
            logger.warning(
                "%s: provider does not support with_structured_output (%s); "
                "falling back to free-text generation",
                agent_name,
                exc,
            )
            return None
        logger.warning(
            "%s: provider does not support with_structured_output (%s); "
            "using schema-prompt JSON validation without tool_choice",
            agent_name, exc,
        )
        return SchemaPromptStructured(llm, schema)


def invoke_structured_or_freetext(
    structured_llm: Optional[Any],
    plain_llm: Any,
    prompt: Any,
    render: Callable[[T], str],
    agent_name: str,
    *,
    return_metadata: bool = False,
    fallback_schema: type[T] | None = None,
) -> str | tuple[str, dict[str, Any]]:
    """Run the structured call and render to markdown; fall back to free-text on any failure.

    ``prompt`` is whatever the underlying LLM accepts (a string for chat
    invocations, a list of message dicts for chat models that take that
    shape). The same value is forwarded to the free-text path so the
    fallback sees the same input the structured call did.
    """
    retained_invalid_response = ""
    retained_validation_error: Exception | None = None
    if structured_llm is not None:
        try:
            result = structured_llm.invoke(prompt)
            rendered = render(result)
            metadata = {
                "mode": getattr(structured_llm, "structured_mode", "structured"),
                "agent": agent_name,
                "structured_error": "",
                "validated_payload": result.model_dump(mode="json"),
            }
            return (rendered, metadata) if return_metadata else rendered
        except Exception as exc:
            structured_error = str(exc)
            if isinstance(exc, SchemaPromptValidationError):
                retained_invalid_response = exc.raw_response
                retained_validation_error = exc.cause
            if fallback_schema is not None and _is_thinking_tool_choice_error(exc):
                try:
                    runner = SchemaPromptStructured(plain_llm, fallback_schema)
                    result = runner.invoke(prompt)
                    rendered = render(result)
                    metadata = {
                        "mode": runner.structured_mode,
                        "agent": agent_name,
                        "structured_error": structured_error,
                        "validated_payload": result.model_dump(mode="json"),
                    }
                    return (rendered, metadata) if return_metadata else rendered
                except Exception as schema_prompt_error:
                    structured_error += f"; schema prompt={schema_prompt_error}"
                    if isinstance(schema_prompt_error, SchemaPromptValidationError):
                        retained_invalid_response = schema_prompt_error.raw_response
                        retained_validation_error = schema_prompt_error.cause
            logger.warning(
                "%s: structured-output invocation failed (%s); retrying once as free text",
                agent_name, exc,
            )
    else:
        structured_error = "structured output binding unavailable"

    if retained_invalid_response:
        content = retained_invalid_response
    else:
        response = plain_llm.invoke(prompt)
        content = _response_text(response)
    repair_error = ""
    if fallback_schema is not None:
        try:
            repaired_result = fallback_schema.model_validate(_json_object(content))
            rendered = render(repaired_result)
            metadata = {
                "mode": "schema_repaired_fallback",
                "agent": agent_name,
                "structured_error": structured_error,
                "validated_payload": repaired_result.model_dump(mode="json"),
            }
            return (rendered, metadata) if return_metadata else rendered
        except Exception as first_repair_error:
            latest_text = content
            latest_error: Exception = retained_validation_error or first_repair_error
            repair_failures = [f"fallback validation={first_repair_error}"]
            # A first repair often leaves only one or two enum/missing-field
            # errors. Feed those exact paths back once more instead of throwing
            # away an otherwise schema-complete response and publishing raw JSON.
            for attempt in range(1, 3):
                repair_contract = _schema_repair_contract(
                    fallback_schema, _validation_cause(latest_error)
                )
                repair_prompt = f"""Your previous response did not validate against the required schema.

Return exactly one valid JSON object with no Markdown fences or commentary. Preserve the analysis and values already present. Do not add unsupported facts. Correct every listed validation issue. Required JSON Schema:
{json.dumps(repair_contract, ensure_ascii=False, separators=(',', ':'))}
{_configured_language_repair_instruction()}

Validation issues from the previous response:
{_compact_validation_error(latest_error)}

Previous response:
{latest_text[:50000]}
"""
                try:
                    repaired_response = plain_llm.invoke(repair_prompt)
                    latest_text = _response_text(repaired_response)
                    repaired_result = fallback_schema.model_validate(
                        _json_object(latest_text)
                    )
                    rendered = render(repaired_result)
                    metadata = {
                        "mode": "schema_repaired_fallback",
                        "agent": agent_name,
                        "structured_error": structured_error,
                        "validated_payload": repaired_result.model_dump(mode="json"),
                        "schema_repair_attempts": attempt,
                    }
                    return (rendered, metadata) if return_metadata else rendered
                except Exception as next_error:
                    latest_error = next_error
                    repair_failures.append(
                        f"repair attempt {attempt} validation={next_error}"
                    )
            content = latest_text
            repair_error = "; " + "; ".join(repair_failures)
    metadata = {
        "mode": "free_text_fallback",
        "agent": agent_name,
        "structured_error": structured_error + repair_error,
    }
    return (content, metadata) if return_metadata else content
