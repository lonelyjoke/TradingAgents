import threading
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Any, Callable, Dict, List, Union
from zoneinfo import ZoneInfo

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult
from langchain_core.messages import AIMessage


# DeepSeek mainland pricing effective 2026-08-17, CNY per 1M tokens.
# Kept beside the emitted estimate so historical run artifacts remain auditable
# if provider pricing changes later.
_DEEPSEEK_PRICING_CNY_PER_MILLION = {
    "legacy_before_2026_08_17": {
        "deepseek-v4-flash": {"cache_hit": 0.02, "cache_miss": 1.0, "output": 2.0},
        "deepseek-v4-pro": {"cache_hit": 0.025, "cache_miss": 3.0, "output": 6.0},
    },
    "off_peak": {
        "deepseek-v4-flash": {"cache_hit": 0.05, "cache_miss": 1.5, "output": 4.5},
        "deepseek-v4-pro": {"cache_hit": 0.15, "cache_miss": 4.5, "output": 13.5},
    },
    "peak": {
        "deepseek-v4-flash": {"cache_hit": 0.10, "cache_miss": 3.0, "output": 9.0},
        "deepseek-v4-pro": {"cache_hit": 0.30, "cache_miss": 9.0, "output": 27.0},
    },
}

_BEIJING_TZ = ZoneInfo("Asia/Shanghai")


def _deepseek_pricing_tier(at: datetime) -> str:
    local = at.astimezone(_BEIJING_TZ)
    if local.date().isoformat() < "2026-08-17":
        return "legacy_before_2026_08_17"
    minute = local.hour * 60 + local.minute
    if 9 * 60 <= minute < 12 * 60 or 14 * 60 <= minute < 18 * 60:
        return "peak"
    return "off_peak"


class StatsCallbackHandler(BaseCallbackHandler):
    """Callback handler that tracks LLM calls, tool calls, and token usage."""

    def __init__(
        self,
        *,
        now_provider: Callable[[], datetime] | None = None,
    ) -> None:
        super().__init__()
        self._lock = threading.Lock()
        self.llm_calls = 0
        self.tool_calls = 0
        self.tokens_in = 0
        self.tokens_out = 0
        self.cached_tokens_in = 0
        self.llm_errors = 0
        self._run_labels: Dict[str, str] = {}
        self._run_models: Dict[str, str] = {}
        self._run_pricing_tiers: Dict[str, str] = {}
        self._counted_runs: set[str] = set()
        self._breakdown: Dict[str, Dict[str, int]] = {}
        self._model_breakdown: Dict[str, Dict[str, int]] = {}
        self._estimated_model_costs: Dict[str, Decimal] = {}
        self._pricing_tier_tokens: Dict[str, int] = {
            "legacy_before_2026_08_17": 0,
            "off_peak": 0,
            "peak": 0,
        }
        self._now_provider = now_provider or (lambda: datetime.now(_BEIJING_TZ))

    @staticmethod
    def _label(serialized: Dict[str, Any], kwargs: Dict[str, Any]) -> str:
        metadata = kwargs.get("metadata") or {}
        for candidate in (
            metadata.get("langgraph_node"),
            metadata.get("agent_name"),
            kwargs.get("name"),
            serialized.get("name"),
        ):
            if candidate:
                return str(candidate)
        identifier = serialized.get("id")
        if isinstance(identifier, list) and identifier:
            return str(identifier[-1])
        return "unattributed"

    def _row(self, label: str) -> Dict[str, int]:
        return self._breakdown.setdefault(
            label,
            {
                "llm_calls": 0,
                "tool_calls": 0,
                "tokens_in": 0,
                "tokens_out": 0,
                "cached_tokens_in": 0,
                "llm_errors": 0,
            },
        )

    @staticmethod
    def _model_name(serialized: Dict[str, Any], kwargs: Dict[str, Any]) -> str:
        invocation = kwargs.get("invocation_params") or {}
        metadata = kwargs.get("metadata") or {}
        serialized_kwargs = serialized.get("kwargs") or {}
        for candidate in (
            invocation.get("model"),
            invocation.get("model_name"),
            metadata.get("ls_model_name"),
            serialized_kwargs.get("model"),
            serialized_kwargs.get("model_name"),
        ):
            if candidate:
                return str(candidate)
        return "unattributed"

    def _model_row(self, model: str) -> Dict[str, int]:
        return self._model_breakdown.setdefault(
            model,
            {
                "llm_calls": 0,
                "tokens_in": 0,
                "tokens_out": 0,
                "cached_tokens_in": 0,
                "llm_errors": 0,
            },
        )

    def _model_start(self, serialized: Dict[str, Any], kwargs: Dict[str, Any]) -> None:
        run_key = str(kwargs.get("run_id") or "")
        label = self._label(serialized, kwargs)
        model = self._model_name(serialized, kwargs)
        with self._lock:
            if run_key:
                if run_key in self._counted_runs:
                    return
                self._run_labels[run_key] = label
                self._run_models[run_key] = model
                self._run_pricing_tiers[run_key] = _deepseek_pricing_tier(
                    self._now_provider()
                )
                self._counted_runs.add(run_key)
            self.llm_calls += 1
            self._row(label)["llm_calls"] += 1
            self._model_row(model)["llm_calls"] += 1

    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        **kwargs: Any,
    ) -> None:
        """Increment LLM call counter when an LLM starts."""
        self._model_start(serialized, kwargs)

    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[Any]],
        **kwargs: Any,
    ) -> None:
        """Increment LLM call counter when a chat model starts."""
        self._model_start(serialized, kwargs)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Extract token usage from LLM response."""
        try:
            generation = response.generations[0][0]
        except (IndexError, TypeError):
            return

        usage_metadata = None
        if hasattr(generation, "message"):
            message = generation.message
            if isinstance(message, AIMessage) and hasattr(message, "usage_metadata"):
                usage_metadata = message.usage_metadata

        if usage_metadata:
            with self._lock:
                tokens_in = usage_metadata.get("input_tokens", 0)
                tokens_out = usage_metadata.get("output_tokens", 0)
                input_details = usage_metadata.get("input_token_details", {}) or {}
                cached_tokens = input_details.get(
                    "cache_read", input_details.get("cached_tokens", 0)
                )
                self.tokens_in += tokens_in
                self.tokens_out += tokens_out
                self.cached_tokens_in += cached_tokens
                run_key = str(kwargs.get("run_id") or "")
                label = self._run_labels.pop(run_key, "unattributed")
                model = self._run_models.pop(run_key, "unattributed")
                pricing_tier = self._run_pricing_tiers.pop(run_key, "off_peak")
                row = self._row(label)
                row["tokens_in"] += tokens_in
                row["tokens_out"] += tokens_out
                row["cached_tokens_in"] += cached_tokens
                model_row = self._model_row(model)
                model_row["tokens_in"] += tokens_in
                model_row["tokens_out"] += tokens_out
                model_row["cached_tokens_in"] += cached_tokens
                rates = _DEEPSEEK_PRICING_CNY_PER_MILLION.get(
                    pricing_tier, {}
                ).get(model.lower())
                if rates:
                    cache_hit = min(cached_tokens, tokens_in)
                    cache_miss = max(tokens_in - cache_hit, 0)
                    cost = (
                        Decimal(cache_hit) * Decimal(str(rates["cache_hit"]))
                        + Decimal(cache_miss) * Decimal(str(rates["cache_miss"]))
                        + Decimal(tokens_out) * Decimal(str(rates["output"]))
                    ) / Decimal(1_000_000)
                    self._estimated_model_costs[model] = (
                        self._estimated_model_costs.get(model, Decimal("0")) + cost
                    )
                    self._pricing_tier_tokens[pricing_tier] += tokens_in + tokens_out

    def on_llm_error(self, error: BaseException, **kwargs: Any) -> None:
        """Track provider failures/retries separately from successful calls."""
        with self._lock:
            self.llm_errors += 1
            run_key = str(kwargs.get("run_id") or "")
            label = self._run_labels.pop(run_key, "unattributed")
            model = self._run_models.pop(run_key, "unattributed")
            self._run_pricing_tiers.pop(run_key, None)
            self._row(label)["llm_errors"] += 1
            self._model_row(model)["llm_errors"] += 1

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        **kwargs: Any,
    ) -> None:
        """Increment tool call counter when a tool starts."""
        with self._lock:
            self.tool_calls += 1
            self._row(self._label(serialized, kwargs))["tool_calls"] += 1

    def get_stats(self) -> Dict[str, Any]:
        """Return current statistics."""
        with self._lock:
            uncached_tokens = max(self.tokens_in - self.cached_tokens_in, 0)
            breakdown = {
                label: dict(row)
                for label, row in sorted(
                    self._breakdown.items(),
                    key=lambda item: (
                        item[1]["tokens_in"],
                        item[1]["tokens_out"],
                        item[1]["llm_calls"],
                    ),
                    reverse=True,
                )
            }
            model_breakdown = {
                model: dict(row)
                for model, row in sorted(
                    self._model_breakdown.items(),
                    key=lambda item: (
                        item[1]["tokens_in"],
                        item[1]["tokens_out"],
                        item[1]["llm_calls"],
                    ),
                    reverse=True,
                )
            }
            model_costs: Dict[str, float] = {}
            estimated_cost = Decimal("0")
            priced_tokens = 0
            for model, cost in self._estimated_model_costs.items():
                model_costs[model] = float(
                    cost.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
                )
                estimated_cost += cost
            priced_tokens = sum(self._pricing_tier_tokens.values())
            return {
                "llm_calls": self.llm_calls,
                "tool_calls": self.tool_calls,
                "tokens_in": self.tokens_in,
                "tokens_out": self.tokens_out,
                "cached_tokens_in": self.cached_tokens_in,
                "uncached_tokens_in": uncached_tokens,
                "cache_hit_ratio": round(
                    self.cached_tokens_in / self.tokens_in, 4
                ) if self.tokens_in else 0.0,
                "llm_errors": self.llm_errors,
                "node_breakdown": breakdown,
                "model_breakdown": model_breakdown,
                "estimated_llm_cost_cny": float(
                    estimated_cost.quantize(
                        Decimal("0.0001"), rounding=ROUND_HALF_UP
                    )
                ),
                "estimated_model_costs_cny": model_costs,
                "cost_estimate_priced_tokens": priced_tokens,
                "cost_pricing_snapshot": {
                    "as_of": "2026-08-17",
                    "effective_at_beijing": "2026-08-17 00:00",
                    "unit": "CNY per 1M tokens",
                    "peak_hours_beijing": ["09:00-12:00", "14:00-18:00"],
                    "deepseek": _DEEPSEEK_PRICING_CNY_PER_MILLION,
                },
                "cost_pricing_tier_tokens": dict(self._pricing_tier_tokens),
            }
