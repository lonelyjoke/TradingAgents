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


class SchemaPromptStructured:
    """Schema-validated JSON generation without provider tool_choice."""

    structured_mode = "schema_prompt_structured"

    def __init__(self, llm: Any, schema: type[T]):
        self.llm = llm
        self.schema = schema

    def invoke(self, prompt: Any) -> T:
        response = self.llm.invoke(_schema_prompt(prompt, self.schema))
        return self.schema.model_validate(_json_object(_response_text(response)))


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
            logger.warning(
                "%s: structured-output invocation failed (%s); retrying once as free text",
                agent_name, exc,
            )
    else:
        structured_error = "structured output binding unavailable"

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
            repair_prompt = f"""Your previous response did not validate against the required schema.

Return exactly one valid JSON object with no Markdown fences or commentary. Preserve the analysis and values already present. Do not add unsupported facts. Required JSON Schema:
{json.dumps(fallback_schema.model_json_schema(), ensure_ascii=False, separators=(',', ':'))}

Previous response:
{content[:50000]}
"""
            try:
                repaired_response = plain_llm.invoke(repair_prompt)
                repaired_text = _response_text(repaired_response)
                repaired_result = fallback_schema.model_validate(
                    _json_object(repaired_text)
                )
                rendered = render(repaired_result)
                metadata = {
                    "mode": "schema_repaired_fallback",
                    "agent": agent_name,
                    "structured_error": structured_error,
                    "validated_payload": repaired_result.model_dump(mode="json"),
                }
                return (rendered, metadata) if return_metadata else rendered
            except Exception as second_repair_error:
                repair_error = (
                    f"; fallback validation={first_repair_error}; "
                    f"repair validation={second_repair_error}"
                )
    metadata = {
        "mode": "free_text_fallback",
        "agent": agent_name,
        "structured_error": structured_error + repair_error,
    }
    return (content, metadata) if return_metadata else content
