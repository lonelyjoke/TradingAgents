"""Derived industry-cycle verdict context.

This module does not invent fresh market data. It summarizes already-fetched
sector-native contexts into a single cycle-stage read so downstream agents do
not jump from company ratios straight to phrases such as "cycle bottom".
"""

from __future__ import annotations

import re
from typing import Mapping


_NEGATIVE_CONTEXT_MARKERS = (
    "not_applicable",
    "no commodity mapping found",
    "no shipping mapping found",
    "no curated",
    "unavailable",
    "failed",
)


def _has_usable_context(text: str) -> bool:
    cleaned = (text or "").strip()
    if len(cleaned) < 120:
        return False
    lower = cleaned.lower()
    return not any(marker in lower for marker in _NEGATIVE_CONTEXT_MARKERS)


def _first_matching_lines(text: str, patterns: tuple[str, ...], *, limit: int = 4) -> list[str]:
    rows: list[str] = []
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("| ---"):
            continue
        if any(pattern.search(line) for pattern in compiled):
            compact = re.sub(r"\s+", " ", line)
            rows.append(compact[:320])
        if len(rows) >= limit:
            break
    return rows


def _extract_percent(text: str, label_patterns: tuple[str, ...]) -> float | None:
    for pattern in label_patterns:
        match = re.search(pattern, text or "", re.I)
        if not match:
            continue
        try:
            return float(match.group(1))
        except ValueError:
            continue
    return None


def _commodity_stage(commodity_context: str) -> tuple[str, str]:
    change = _extract_percent(
        commodity_context,
        (
            r"change_over_window\s*\|\s*([-+]?\d+(?:\.\d+)?)%",
            r"\|\s*[-+]?\d+(?:\.\d+)?\s*\|\s*\d{8}\s*\|\s*([-+]?\d+(?:\.\d+)?)%",
        ),
    )
    lower = commodity_context.lower()
    has_curve = "curve=" in lower or "远期" in commodity_context or "futures" in lower
    if change is None:
        if has_curve:
            return (
                "evidence-limited price-stabilization check",
                "Futures/price proxy is present, but the module could not derive a clean price-change percentage.",
            )
        return (
            "evidence-limited cycle read",
            "Commodity context is available but lacks a clean direction signal; keep exact stage provisional.",
        )
    if change >= 25:
        return (
            "right-side recovery / early upcycle candidate",
            f"Mapped product proxy rose {change:.1f}% over the look-back window; this supports margin repair but may also include restocking or inventory gains.",
        )
    if change >= 8:
        return (
            "bottom-right validation stage",
            f"Mapped product proxy rose {change:.1f}% over the look-back window; this supports bottoming language only if inventory, demand, and company cash conversion confirm.",
        )
    if change > -8:
        return (
            "range-bound / bottom-testing stage",
            f"Mapped product proxy moved {change:.1f}% over the look-back window; price evidence alone does not prove a new upcycle.",
        )
    return (
        "downcycle / failed-rebound risk",
        f"Mapped product proxy fell {abs(change):.1f}% over the look-back window; margin and inventory assumptions require stress-case treatment.",
    )


def build_industry_cycle_context(
    symbol: str,
    curr_date: str,
    *,
    commodity_context: str = "",
    shipping_context: str = "",
    baijiu_context: str = "",
    building_materials_context: str = "",
    consumer_staples_context: str = "",
    metals_mining_context: str = "",
    policy_planning_context: str = "",
    investor_interaction_context: str = "",
    filing_intelligence_context: str = "",
    knowledge_planet_context: str = "",
) -> str:
    """Build a compact industry-cycle verdict from existing evidence contexts."""

    # Context producers normally return strings, but optional/non-A-share
    # paths and mocked integrations may supply None or proxy objects.  Treat
    # those as unavailable rather than letting one optional layer crash the
    # entire research graph.
    def _context_text(value: object) -> str:
        return value if isinstance(value, str) else ""

    commodity_context = _context_text(commodity_context)
    shipping_context = _context_text(shipping_context)
    baijiu_context = _context_text(baijiu_context)
    building_materials_context = _context_text(building_materials_context)
    consumer_staples_context = _context_text(consumer_staples_context)
    metals_mining_context = _context_text(metals_mining_context)
    policy_planning_context = _context_text(policy_planning_context)
    investor_interaction_context = _context_text(investor_interaction_context)
    filing_intelligence_context = _context_text(filing_intelligence_context)
    knowledge_planet_context = _context_text(knowledge_planet_context)

    active_layers: list[tuple[str, str, str]] = []
    if _has_usable_context(commodity_context):
        stage, reason = _commodity_stage(commodity_context)
        active_layers.append(("commodity/product price", stage, reason))
    if _has_usable_context(shipping_context):
        active_layers.append(
            (
                "shipping/freight",
                "freight-cycle evidence required",
                "Shipping context is available; route-level freight and broad-index evidence should govern cycle language.",
            )
        )
    if _has_usable_context(baijiu_context):
        active_layers.append(
            (
                "baijiu/channel",
                "channel-cycle verification required",
                "Baijiu context is available; wholesale price, channel inventory, contract liabilities, and payment quality should govern cycle language.",
            )
        )
    if _has_usable_context(building_materials_context):
        active_layers.append(
            (
                "building materials",
                "construction-chain cycle verification required",
                "Building-materials context is available; ASP, regional demand, capacity discipline, inventory, receivables, and cash collection should govern cycle language.",
            )
        )
    if _has_usable_context(consumer_staples_context):
        active_layers.append(
            (
                "consumer staples/channel",
                "demand-and-channel cycle verification required",
                "Consumer context is available; sell-through, distributor inventory, promotion, raw-material costs, and contract liabilities should govern cycle language.",
            )
        )
    if _has_usable_context(metals_mining_context):
        active_layers.append(
            (
                "metals/mining",
                "metal-price and mine-economics verification required",
                "Metals/mining context is available; realized prices, reserves, grade, AISC/unit cost, project ramp, hedging, and NAV/SOTP should govern cycle language.",
            )
        )
    if _has_usable_context(knowledge_planet_context):
        active_layers.append(
            (
                "Knowledge Planet private/proxy intelligence",
                "private cycle clues require objective bridge",
                "Knowledge Planet context is available; industry weekly data, channel checks, and PDF research may improve cycle timing, but sell-side pushes must be converted into price/spread/inventory/cost evidence before valuation.",
            )
        )

    if not active_layers:
        active_layers.append(
            (
                "general industry",
                "cycle evidence insufficient",
                "No usable sector-native cycle module was available. Do not claim a cycle bottom/top from company PE, PB, or one-quarter financials alone.",
            )
        )

    primary_stage = active_layers[0][1]
    if primary_stage in {"cycle evidence insufficient", "evidence-limited cycle read"}:
        confidence = "low"
    elif "evidence-limited" in primary_stage or "verification required" in primary_stage:
        confidence = "medium-low"
    else:
        confidence = "medium"

    evidence_lines = _first_matching_lines(
        "\n".join(
            [
                commodity_context,
                shipping_context,
                baijiu_context,
                building_materials_context,
                consumer_staples_context,
                metals_mining_context,
                policy_planning_context,
                investor_interaction_context,
                filing_intelligence_context,
                knowledge_planet_context,
            ]
        ),
        (
            r"latest_price|change_over_window|curve=|库存|inventory|开工|utilization|合同负债|订单|批价|wholesale|freight|TCE|BDI|BDTI|BCTI|AISC|grade|毛利率|OCF",
        ),
        limit=8,
    )

    layer_rows = [
        f"| {layer} | {stage} | {reason.replace('|', '/')} |"
        for layer, stage, reason in active_layers
    ]
    evidence_rows = [f"- {line}" for line in evidence_lines] or [
        "- No compact evidence lines could be extracted; keep the cycle verdict provisional."
    ]

    return "\n".join(
        [
            f"# Industry Cycle Scan for {symbol} as of {curr_date}",
            "",
            f"- Cycle verdict: {primary_stage}",
            f"- Confidence: {confidence}",
            "- Use: this is a pre-valuation gate. Company earnings and valuation should be read after this cycle stage is stated.",
            "",
            "## Cycle Evidence Matrix",
            "| layer | stage read | evidence read |",
            "| --- | --- | --- |",
            *layer_rows,
            "",
            "## Extracted Evidence Lines",
            *evidence_rows,
            "",
            "## Segment-Level Cycle And Prosperity Bridge",
            "| analytical layer | required question | acceptable evidence |",
            "| --- | --- | --- |",
            "| Demand | Is end demand accelerating, stable, slowing, or contracting for this segment? | orders, tenders, sell-through, installation, traffic, AUM/premium, route volume, policy-backed demand |",
            "| Supply | Is industry/company supply disciplined or expanding faster than demand? | capacity, utilization, inventory, competitor entry/exit, sow/reserve/fleet/store/installed-base data |",
            "| Price and mix | Does pricing power or product/customer mix support prosperity? | ASP, product price, discount, spread, freight rate, NIM, NBV margin, COR, mix |",
            "| Volume and share | Is the company gaining profitable volume or merely following the market? | shipment/output, market share, backlog conversion, customer/geography mix |",
            "| Profit and cash | Does prosperity reach segment margin, working capital, OCF and FCF? | segment gross margin/profit, receivables, inventory, contract liabilities, capex, cash conversion |",
            "| Cycle classification | What are the segment's current level and marginal direction? | high / medium-high / neutral / weakening / low / bottom-testing / recovery plus improving/stable/deteriorating |",
            "- Complete this bridge for each material business segment. The consolidated cycle verdict is a profit-weighted synthesis, not the first available commodity or industry signal.",
            "- A segment can be high-prosperity but decelerating, or low-prosperity but recovering. Report both level and direction, with dates and confidence.",
            "- If company filings show strong segment growth while product/industry data weaken, surface the conflict and test market-share gain, mix, lag, or accounting timing instead of averaging the signals.",
            "",
            "## Analyst Instructions",
            "- Do not write `cycle bottom`, `周期底部`, or `cycle reversal` as a fact unless this scan and company financials both support it.",
            "- If cycle evidence says bottom-testing or evidence-limited, use language such as `bottom-right validation stage`, `右侧待验证`, or `needs confirmation`.",
            "- Tie the cycle verdict to the earnings bridge: ASP/price, spread, volume, utilization, inventory, cash conversion, and valuation multiple.",
            "- Do not transfer the cycle stage of one segment to all company businesses. Explain which segment drives revenue, gross profit, EPS, cash flow, and valuation.",
            "- State falsification signals: price/spread breakdown, inventory rebuild, order/contract-liability deterioration, cash-conversion failure, or peer-relative evidence that contradicts the cycle read.",
        ]
    )


def get_industry_cycle_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
) -> str:
    """Public helper for tests and fallback callers.

    Runtime graph code normally passes already-fetched contexts to avoid duplicate
    vendor calls. Direct callers may supply a context mapping; without one this
    returns a conservative empty-evidence verdict.
    """

    supplied = dict(contexts or {})
    return build_industry_cycle_context(
        ticker,
        curr_date,
        commodity_context=supplied.get("commodity_context", ""),
        shipping_context=supplied.get("shipping_context", ""),
        baijiu_context=supplied.get("baijiu_context", ""),
        building_materials_context=supplied.get("building_materials_context", ""),
        consumer_staples_context=supplied.get("consumer_staples_context", ""),
        metals_mining_context=supplied.get("metals_mining_context", ""),
        policy_planning_context=supplied.get("policy_planning_context", ""),
        investor_interaction_context=supplied.get("investor_interaction_context", ""),
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        knowledge_planet_context=supplied.get("knowledge_planet_context", ""),
    )
