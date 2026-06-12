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
    )
