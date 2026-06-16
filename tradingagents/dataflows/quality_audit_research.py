"""Derived sell-side depth and key-number audit context."""

from __future__ import annotations

from typing import Mapping


def _status(text: str, *, fail_markers: tuple[str, ...] = ()) -> str:
    cleaned = (text or "").strip()
    if len(cleaned) < 120:
        return "missing"
    lower = cleaned.lower()
    if any(marker in lower for marker in fail_markers):
        return "partial"
    return "ready"


def _commodity_driver_has_usable_evidence(commodity_lower: str, *names: str) -> bool:
    for line in commodity_lower.splitlines():
        if not any(name in line for name in names):
            continue
        if "unavailable" in line or "missing;" in line or "n/a" in line:
            continue
        if "verified" in line or "proxy" in line:
            return True
    return False


def _commodity_driver_is_listed_missing(commodity_lower: str, *names: str) -> bool:
    for line in commodity_lower.splitlines():
        if any(name in line for name in names) and (
            "unavailable" in line or "missing;" in line or "n/a" in line
        ):
            return True
    return False


def _metals_quality_rows(
    *,
    metals_mining_context: str,
    industry_kpi_context: str,
    forecast_model_context: str,
    commodity_context: str,
) -> list[tuple[str, str, str]]:
    metals_lower = (metals_mining_context or "").lower()
    if "status: triggered" not in metals_lower:
        return []

    rows: list[tuple[str, str, str]] = []
    kpi_lower = (industry_kpi_context or "").lower()
    forecast_lower = (forecast_model_context or "").lower()
    commodity_lower = (commodity_context or "").lower()

    if "battery / energy-storage chain" in kpi_lower or "cathode" in kpi_lower:
        rows.append(
            (
                "Metals/mining KPI routing",
                "partial",
                "metals/mining target is using a battery-chain KPI map; reroute to nonferrous cycle, resource, cost curve, segment mix, project, and cash-risk KPIs",
            )
        )
    if "cathode / material revenue" in forecast_lower or "lithium carbonate" in forecast_lower:
        rows.append(
            (
                "Metals/mining forecast bridge",
                "partial",
                "forecast bridge is using battery-material formulas; use realized metal price, equity output, AISC/unit cost, smelting spread, trading value, NAV/SOTP, and FCF",
            )
        )

    if "metals covered: aluminum" in metals_lower:
        has_aluminum_proxy = _commodity_driver_has_usable_evidence(commodity_lower, "aluminum", "閾?")
        has_alumina_proxy = _commodity_driver_has_usable_evidence(commodity_lower, "alumina", "姘у寲閾?")
        has_power_evidence = _commodity_driver_has_usable_evidence(commodity_lower, "power cost", "鐢靛姏鎴愭湰")
        has_anode_evidence = _commodity_driver_has_usable_evidence(
            commodity_lower,
            "anode",
            "carbon anode",
        )
        listed_missing = []
        if _commodity_driver_is_listed_missing(commodity_lower, "power cost", "鐢靛姏鎴愭湰"):
            listed_missing.append("power cost")
        if _commodity_driver_is_listed_missing(commodity_lower, "anode", "carbon anode"):
            listed_missing.append("anode cost")
        if has_aluminum_proxy and not (has_alumina_proxy and has_power_evidence and has_anode_evidence):
            missing = []
            if not has_alumina_proxy:
                missing.append("alumina")
            if not has_power_evidence:
                missing.append("power cost")
            if not has_anode_evidence:
                missing.append("anode cost")
            missing_text = ", ".join(list(dict.fromkeys(missing + listed_missing)))
            rows.append(
                (
                    "Aluminum spread driver coverage",
                    "partial",
                    f"SHFE aluminum proxy is present, but usable cost evidence is missing for {missing_text}; treat missing cost data as neutral for direction and only as a confidence cap. Margin-collapse or margin-resilience claims require independent verified cost, spread, inventory, cash-flow, or segment-margin evidence",
                )
            )

    return rows


def build_quality_audit_context(
    symbol: str,
    curr_date: str,
    *,
    industry_cycle_context: str = "",
    company_business_model_context: str = "",
    industry_kpi_context: str = "",
    forecast_model_context: str = "",
    peer_comparison_context: str = "",
    price_earnings_decomposition_context: str = "",
    earnings_model_context: str = "",
    filing_intelligence_context: str = "",
    metals_mining_context: str = "",
    commodity_context: str = "",
) -> str:
    rows = [
        ("Industry cycle stage", _status(industry_cycle_context, fail_markers=("cycle evidence insufficient",)), "cycle verdict must precede valuation language"),
        ("Business model / segment economics", _status(company_business_model_context, fail_markers=("no clean business-model",)), "reader must understand how the company earns money"),
        ("Industry KPI checklist", _status(industry_kpi_context), "sector-native KPIs must be verified or listed as gaps"),
        ("Three-year forecast bridge", _status(forecast_model_context), "valuation must connect to revenue/profit/cash-flow assumptions"),
        ("True peer and valuation cross-check", _status(peer_comparison_context), "peer set should match business buckets, not just exchange industry label"),
        ("PE/PB/EPS decomposition", _status(price_earnings_decomposition_context), "multiple changes must be separated from earnings changes"),
        ("Financial-statement extraction", _status(earnings_model_context), "base numbers and latest snapshots must be traceable"),
        ("Filing intelligence", _status(filing_intelligence_context), "MD&A, segment, risk, and business description evidence"),
    ]
    rows.extend(
        _metals_quality_rows(
            metals_mining_context=metals_mining_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            commodity_context=commodity_context,
        )
    )
    weak = [name for name, status, _ in rows if status != "ready"]
    return "\n".join(
        [
            f"# Sell-Side Depth And Key-Number Audit for {symbol} as of {curr_date}",
            "",
            "- Purpose: make the final report auditable. Strong wording needs source, formula, period, and driver bridge.",
            "",
            "## Depth Checklist",
            "| section | status | required treatment |",
            "| --- | --- | --- |",
            *[f"| {name} | {status} | {treatment} |" for name, status, treatment in rows],
            "",
            "## Key Number Audit Rules",
            "- Every decisive PE/PB/EV multiple must state numerator, denominator, period, and whether it is TTM, run-rate, forward, or normalized.",
            "- Every dividend yield, payout ratio, safety price, target price, or entry band must show formula and source period.",
            "- Every margin, ASP, shipment, utilization, inventory, backlog, and contract-liability claim must name its evidence status: verified, proxy, stale, or missing.",
            "- If a number comes from one quarter, label it as quarterly/run-rate evidence and reconcile seasonality before annualizing.",
            "- If the report uses SOTP, separate core value, scenario value, and optionality; do not bury speculative second curves inside the base multiple.",
            "",
            "## Deep Sell-Side Bridge Requirements",
            "- Order/project companies: include an order bridge: opening backlog + new orders - delivered/revenue-recognized orders = ending backlog; reconcile contract liabilities, receivables, inventory/goods shipped, and cash collection.",
            "- Peer work: split true operating peers from broad industry screens; name substitute expressions and explain why the target is better or worse than alternatives.",
            "- Forecast/valuation: provide bull/base/bear or sensitivity assumptions for revenue, margin, expense ratio, net profit/EPS, FCF, and valuation multiple. Do not jump from one profit number to a safety price without showing assumptions.",
            "- Filing quality: discuss receivables, notes, inventory components, contract assets/liabilities, cash conversion, capex/CIP, depreciation, FX, impairments, and disclosure quality when material.",
            "- Second curves: treat new business, ships, mines, capacity, platforms, data centers, or investee holdings as scenario/optionality value unless unit economics, customer evidence, utilization, capex, cash conversion, and control rights are disclosed.",
            "- Evidence grading: mark each decisive claim as reported, calculated, estimated, proxy, stale, missing, or unverified, and carry missing thesis-critical items into the verification calendar.",
            "- Objectivity guardrail: missing thesis-critical evidence is neutral for direction but material for confidence. It can reduce conviction, sizing, and valuation credit, but it cannot be the decisive reason for Buy/Sell, Underweight/Sell, or 'perfect scenario priced' language.",
            "- Objectivity guardrail: if a decisive industry-native driver is partial or missing on both sides of the debate, cap conviction and prefer Hold/watch or smaller sizing unless verified evidence independently proves a strong probability/payoff skew.",
            "- For aluminum names, if alumina, power, or anode cost evidence is missing, do not call margin deterioration proven. Underweight/Sell needs independent verified evidence such as cost squeeze, segment-margin compression, inventory/cash deterioration, superior peer opportunity cost, or valuation stress.",
            "- For metals/mining, do not permit strong Buy/Sell language from PE/PB, technicals, one-quarter working capital, or one exchange futures proxy when the key spread/cost driver is missing.",
            "",
            "## Report Quality Verdict",
            f"- Weak or incomplete modules: {', '.join(weak) if weak else 'none detected from supplied contexts'}",
            "- Manager instruction: if any weak module is thesis-critical, cap rating conviction or make the missing data a dated verification item.",
        ]
    )


def get_quality_audit_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
) -> str:
    supplied = dict(contexts or {})
    return build_quality_audit_context(
        ticker,
        curr_date,
        industry_cycle_context=supplied.get("industry_cycle_context", ""),
        company_business_model_context=supplied.get("company_business_model_context", ""),
        industry_kpi_context=supplied.get("industry_kpi_context", ""),
        forecast_model_context=supplied.get("forecast_model_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        price_earnings_decomposition_context=supplied.get("price_earnings_decomposition_context", ""),
        earnings_model_context=supplied.get("earnings_model_context", ""),
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        metals_mining_context=supplied.get("metals_mining_context", ""),
        commodity_context=supplied.get("commodity_context", ""),
    )
