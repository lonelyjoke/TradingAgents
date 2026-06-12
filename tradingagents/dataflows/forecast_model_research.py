"""Derived forward forecast-model scaffold context."""

from __future__ import annotations

import re
from typing import Mapping


def _compact_lines(text: str, patterns: tuple[str, ...], *, limit: int = 8) -> list[str]:
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    rows: list[str] = []
    for raw in (text or "").splitlines():
        line = re.sub(r"\s+", " ", raw.strip())
        if not line or line.startswith("| ---"):
            continue
        if any(pattern.search(line) for pattern in compiled):
            if len(line) > 280:
                line = line[:277] + "..."
            rows.append(line.replace("|", "/"))
        if len(rows) >= limit:
            break
    return rows


def _is_battery_context(symbol: str, text: str) -> bool:
    lower = f"{symbol}\n{text}".lower()
    return (
        "300750" in lower
        or "battery" in lower
        or "动力电池" in text
        or "储能电池" in text
        or "锂离子电池" in text
    )


def build_forecast_model_context(
    symbol: str,
    curr_date: str,
    *,
    earnings_model_context: str = "",
    company_business_model_context: str = "",
    filing_intelligence_context: str = "",
    peer_comparison_context: str = "",
    industry_kpi_context: str = "",
) -> str:
    combined = "\n".join(
        [
            earnings_model_context,
            company_business_model_context,
            filing_intelligence_context,
            peer_comparison_context,
            industry_kpi_context,
        ]
    )
    evidence = _compact_lines(
        combined,
        (
            r"revenue|gross margin|net profit|EPS|OCF|FCF|capex|ROE",
            r"segment|business model|profit pool|valuation",
            r"收入|毛利|净利润|归母|现金流|资本开支|分部|业务",
        ),
        limit=10,
    )
    if _is_battery_context(symbol, combined):
        drivers = [
            ("Power battery revenue", "GWh shipments x ASP", "installation demand, share, customer mix, price clauses"),
            ("Energy-storage revenue", "GWh shipments x ASP", "storage tenders, overseas demand, project delivery"),
            ("Materials / recycling / other", "volume x realized spread or service revenue", "vertical integration and utilization"),
            ("Gross profit", "segment revenue x segment gross margin", "lithium/material cost, yield, depreciation, warranty"),
            ("Operating profit", "gross profit - R&D - SG&A", "R&D capitalization/expense, scale leverage"),
            ("net profit/EPS / FCF", "operating profit - tax/minority + working-capital/capex bridge", "cash conversion and capex cycle"),
        ]
    else:
        drivers = [
            ("Core revenue", "volume x ASP x mix", "demand, price, market share"),
            ("Gross profit", "revenue x gross margin", "cost curve, utilization, product mix"),
            ("Operating profit", "gross profit - R&D - SG&A", "expense discipline and scale leverage"),
            ("net profit/EPS", "operating profit - tax/minority/financial items", "non-recurring and minority interest"),
            ("Free cash flow", "net profit + D&A - working capital - capex", "cash conversion and reinvestment"),
        ]

    return "\n".join(
        [
            f"# Forward Forecast Model Scaffold for {symbol} as of {curr_date}",
            "",
            "- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.",
            "",
            "## Evidence Base Already Present",
            *([f"- {line}" for line in evidence] if evidence else ["- No compact earnings/model evidence was extracted; the forecast must be explicitly evidence-limited."]),
            "",
            "## Driver Bridge",
            "| Forecast line | Formula / bridge | Required assumptions |",
            "| --- | --- | --- |",
            *[f"| {name} | {formula} | {assumption} |" for name, formula, assumption in drivers],
            "",
            "## Mandatory Three-Year Table",
            "| item | 2026E | 2027E | 2028E | evidence / assumption status |",
            "| --- | --- | --- | --- | --- |",
            "| Revenue | to be estimated | to be estimated | to be estimated | tie to segment volume, ASP, and mix |",
            "| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |",
            "| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |",
            "| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |",
            "| Operating cash flow / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and capex |",
            "",
            "## Analyst Instructions",
            "- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.",
            "- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.",
            "- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.",
        ]
    )


def get_forecast_model_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
) -> str:
    supplied = dict(contexts or {})
    return build_forecast_model_context(
        ticker,
        curr_date,
        earnings_model_context=supplied.get("earnings_model_context", ""),
        company_business_model_context=supplied.get("company_business_model_context", ""),
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        industry_kpi_context=supplied.get("industry_kpi_context", ""),
    )
