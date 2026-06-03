"""Prompt-side context compaction helpers.

These helpers reduce repeated LLM input tokens without changing the raw data
kept in state or saved report artifacts. The compactor is deliberately local
and deterministic: it preserves headings, verdict-like lines, failure markers,
and evidence-sensitive rows before trimming long table tails.
"""

from __future__ import annotations

import re
from collections.abc import Mapping

from tradingagents.dataflows.config import get_config


_IMPORTANT_RE = re.compile(
    "|".join(
        [
            r"^#{1,6}\s+",
            r"^\*\*[^*]+:\*\*",
            r"\b(rating|recommendation|verdict|conclusion|summary|take-?away)\b",
            r"\b(core bet|expectation gap|probability|payoff|valuation|catalyst)\b",
            r"\b(safety price|defensive build anchor|margin of safety|mean[- ]revert|slow accumulation)\b",
            r"\b(key data check|unit[- ]economics|verification calendar|project ramp)\b",
            r"\b(internal filing quality|filing internal quality|accounting reconciliation|footnote radar|disclosure quality)\b",
            r"\b(non[- ]recurring|balance[- ]sheet forward|cash[- ]flow quality|capex|CIP|MD&A)\b",
            r"\b(financing|listing|dilution|take rate|breakeven|occupancy|utilization)\b",
            r"\b(falsification|risk|research gap|unverified|assumption|audit)\b",
            r"\b(failed|failure|unavailable|missing|partial|thin|error|reason)\b",
            r"\b(revenue|profit|margin|cash flow|eps|pe|pb|roe|roic|debt)\b",
            r"\b(dividend|yield|payout|defensive|cash cow|free cash flow|FCF)\b",
            r"\b(building materials|cement|clinker|waterproof|gypsum|fiberglass|glass|coating|ceramic|pipe)\b",
            r"\b(order|backlog|inventory|capacity|utilization|price|spread)\b",
            r"\b(shipping|freight|tanker|VLCC|TCE|TD3C|BDTI|BCTI|BDI|BCI|BPI|CTFI|Hormuz)\b",
            r"\b(compute|GPU|IDC|data center|lease|leasing|rack|power|PUE)\b",
            r"\b(wholesale|source|published|corroborated|conflicting)\b",
            r"\b(supply|demand|policy|peer|shareholder|pledge|repurchase)\b",
            r"(评级|建议|结论|摘要|核心|下注|预期差|赔率|估值|催化)",
            r"(证伪|风险|缺口|未验证|假设|审计|失败|缺失|不可用|部分)",
            r"(收入|利润|毛利|现金流|负债|订单|库存|产能|价格|价差)",
            r"(建材|水泥|熟料|防水|石膏板|玻纤|玻璃|涂料|瓷砖|管材|竣工)",
            r"(供给|需求|政策|同业|股东|质押|回购|分红|管理层)",
            r"(航运|油运|油轮|运价|霍尔木兹|补库|吨海里|干散货|集运)",
        ]
    ),
    re.IGNORECASE,
)


_CONTEXT_KEYS = {
    "thematic_catalyst_context",
    "commodity_context",
    "shipping_context",
    "filing_intelligence_context",
    "peer_comparison_context",
    "supply_chain_comparison_context",
    "earnings_model_context",
    "market_expectation_context",
    "price_earnings_decomposition_context",
    "management_capital_allocation_context",
    "shareholder_structure_context",
    "investor_interaction_context",
    "policy_planning_context",
    "web_fact_check_context",
    "baijiu_context",
    "compute_leasing_context",
    "dividend_defensive_context",
    "building_materials_context",
    "data_coverage_context",
}


_BASE_LIMITS = {
    "default": 5000,
    "analyst_report": 4500,
    "debate_history": 12000,
    "risk_history": 9000,
    "investment_plan": 7000,
    "trader_plan": 4500,
    "past_context": 3500,
    "recent_decision_context": 2500,
    "data_coverage_context": 3500,
    "commodity_context": 3500,
    "shipping_context": 4500,
    "peer_comparison_context": 3500,
    "supply_chain_comparison_context": 3000,
    "earnings_model_context": 3500,
    "market_expectation_context": 3000,
    "price_earnings_decomposition_context": 3500,
    "investor_interaction_context": 3500,
    "policy_planning_context": 3000,
    "web_fact_check_context": 3500,
    "baijiu_context": 5500,
    "compute_leasing_context": 4500,
    "dividend_defensive_context": 5000,
    "building_materials_context": 5500,
    "management_capital_allocation_context": 5000,
    "filing_intelligence_context": 8000,
    "shareholder_structure_context": 5500,
    "thematic_catalyst_context": 6500,
}


_PROFILE_MULTIPLIER = {
    "analyst": 1.25,
    "research": 1.0,
    "trader": 0.75,
    "risk": 0.55,
    "portfolio": 0.75,
}


def _enabled() -> bool:
    return bool(get_config().get("prompt_context_compaction_enabled", True))


def _line_is_important(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if any(
        token in stripped
        for token in [
            "\u7b97\u529b",
            "\u79df\u8d41",
            "\u667a\u4e91\u8ba1\u7b97",
            "\u6570\u636e\u4e2d\u5fc3",
            "\u7f51\u7edc\u5de5\u7a0b",
            "\u5e7f\u4e1c\u76c8\u5cf0",
            "\u6db2\u51b7",
            "\u5149\u6a21\u5757",
            "\u6307\u5b9a\u4fe1\u606f\u62ab\u9732\u5a92\u4f53",
            "\u975e\u627f\u8bfa",
        ]
    ):
        return True
    if _IMPORTANT_RE.search(stripped):
        return True
    if stripped.startswith("|") and any(
        token in stripped.lower()
        for token in [
            "rating",
            "verdict",
            "failed",
            "missing",
            "partial",
            "revenue",
            "profit",
            "margin",
            "现金",
            "利润",
            "缺失",
            "失败",
        ]
    ):
        return True
    return False


def _truncate_line(line: str, limit: int = 360) -> str:
    if len(line) <= limit:
        return line
    return line[: limit - 24].rstrip() + " ... [line trimmed]"


def prompt_limit(label: str, profile: str = "research") -> int:
    """Return the character budget for a prompt field under a usage profile."""
    base = _BASE_LIMITS.get(label, _BASE_LIMITS["default"])
    multiplier = _PROFILE_MULTIPLIER.get(profile, 1.0)
    return max(1200, int(base * multiplier))


def compact_for_prompt(
    text: str | None,
    *,
    label: str = "context",
    profile: str = "research",
    max_chars: int | None = None,
) -> str:
    """Compact long markdown/text before injecting it into an LLM prompt.

    The compactor favors high-signal lines and keeps both the opening and ending
    slices, because many contexts put status/metadata at the top and analyst
    guidance or caveats at the bottom.
    """
    if not text:
        return ""
    if not _enabled():
        return text

    budget = max_chars if max_chars is not None else prompt_limit(label, profile)
    if len(text) <= budget:
        return text

    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    important_budget = int(budget * 0.55)
    important_lines: list[str] = []
    important_chars = 0
    seen: set[str] = set()

    for line in lines:
        if not _line_is_important(line):
            continue
        compact_line = _truncate_line(line)
        key = compact_line.strip()
        if key in seen:
            continue
        seen.add(key)
        important_lines.append(compact_line)
        important_chars += len(compact_line) + 1
        if important_chars >= important_budget:
            break

    head_budget = max(500, int(budget * 0.28))
    tail_budget = max(350, budget - important_chars - head_budget - 260)
    head = text[:head_budget].rstrip()
    tail = text[-tail_budget:].lstrip() if tail_budget > 0 else ""

    parts = [
        f"[Compacted {label}: original {len(text)} chars, budget {budget} chars. "
        "Preserved high-signal lines plus head/tail slices.]",
        "",
        "[High-signal extracted lines]",
        "\n".join(important_lines) if important_lines else "(none detected)",
        "",
        "[Opening slice]",
        head,
    ]
    if tail:
        parts.extend(["", "[Ending slice]", tail])

    compacted = "\n".join(parts)
    return compacted[: budget + 300]


def compact_state_fields(
    state: Mapping[str, object],
    *,
    profile: str,
    keys: set[str] | None = None,
) -> dict[str, str]:
    """Return compacted copies of selected state text fields."""
    selected = keys or _CONTEXT_KEYS
    return {
        key: compact_for_prompt(str(state.get(key, "") or ""), label=key, profile=profile)
        for key in selected
    }


def compact_analyst_report(text: str, *, profile: str = "research") -> str:
    return compact_for_prompt(text, label="analyst_report", profile=profile)


def compact_debate_history(text: str, *, profile: str = "research") -> str:
    return compact_for_prompt(text, label="debate_history", profile=profile)


def compact_risk_history(text: str, *, profile: str = "portfolio") -> str:
    return compact_for_prompt(text, label="risk_history", profile=profile)
