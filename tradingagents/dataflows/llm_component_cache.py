"""Content-addressed cache for expensive, deterministic LLM components.

Only schema-validated model objects are stored.  Cache keys include the exact
prompt, model identity, schema and an explicit component version, so a hit is
semantically equivalent to replaying the same request.  Deterministic
validation still runs after a cached object is loaded.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


def llm_identity(llm: Any) -> str:
    parts = [f"{type(llm).__module__}.{type(llm).__qualname__}"]
    for attribute in ("model_name", "model", "model_id", "deployment_name"):
        value = getattr(llm, attribute, None)
        if value:
            parts.append(f"{attribute}={value}")
    extra_body = getattr(llm, "extra_body", None)
    if extra_body:
        parts.append(
            "extra_body="
            + json.dumps(extra_body, ensure_ascii=False, sort_keys=True, default=str)
        )
    reasoning_effort = getattr(llm, "reasoning_effort", None)
    if reasoning_effort:
        parts.append(f"reasoning_effort={reasoning_effort}")
    return "|".join(parts)


def _cache_path(
    cache_dir: str | Path,
    *,
    component: str,
    version: str,
    prompt: str,
    llm: Any,
    schema: type[BaseModel],
) -> Path:
    schema_json = json.dumps(
        schema.model_json_schema(),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    key_payload = {
        "component": component,
        "version": version,
        "model": llm_identity(llm),
        "schema_sha256": hashlib.sha256(schema_json.encode("utf-8")).hexdigest(),
        "prompt_sha256": hashlib.sha256(str(prompt).encode("utf-8")).hexdigest(),
    }
    digest = hashlib.sha256(
        json.dumps(
            key_payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    return Path(cache_dir) / component / f"{digest}.json"


def load_cached_model(
    cache_dir: str | Path | None,
    *,
    component: str,
    version: str,
    prompt: str,
    llm: Any,
    schema: type[T],
) -> T | None:
    if not cache_dir:
        return None
    path = _cache_path(
        cache_dir,
        component=component,
        version=version,
        prompt=prompt,
        llm=llm,
        schema=schema,
    )
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
        return schema.model_validate(envelope["payload"])
    except (OSError, ValueError, TypeError, KeyError):
        return None


def store_cached_model(
    cache_dir: str | Path | None,
    *,
    component: str,
    version: str,
    prompt: str,
    llm: Any,
    value: T,
) -> None:
    if not cache_dir:
        return
    path = _cache_path(
        cache_dir,
        component=component,
        version=version,
        prompt=prompt,
        llm=llm,
        schema=type(value),
    )
    envelope = {
        "component": component,
        "version": version,
        "model": llm_identity(llm),
        "payload": value.model_dump(mode="json"),
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(envelope, ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )
        os.replace(temporary, path)
    except OSError:
        # Cache writes are always best-effort and must never break a report run.
        return
