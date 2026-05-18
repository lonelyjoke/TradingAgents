from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .tushare_a_stock import (
    TushareDataError,
    _derive_financial_metrics,
    _fetch_balance_sheet_data,
    _fetch_cashflow_data,
    _fetch_fina_indicator,
    _fetch_income_statement_data,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)


@dataclass(frozen=True)
class EarningsSnapshot:
    end_date: str
    period: str
    revenue: float | None
    net_profit_parent: float | None
    annualized_revenue: float | None
    annualized_net_profit_parent: float | None


def _period_label(end_date: str) -> str:
    text = str(end_date or "")
    if text.endswith("0331"):
        return "Q1"
    if text.endswith("0630"):
        return "H1"
    if text.endswith("0930"):
        return "Q3"
    if text.endswith("1231"):
        return "FY"
    return "Unknown"


def _annualization_factor(end_date: str) -> float | None:
    text = str(end_date or "")
    if text.endswith("0331"):
        return 4.0
    if text.endswith("0630"):
        return 2.0
    if text.endswith("0930"):
        return 4.0 / 3.0
    if text.endswith("1231"):
        return 1.0
    return None


def _annualize_cumulative(value: float | None, end_date: str) -> float | None:
    if value is None:
        return None
    factor = _annualization_factor(end_date)
    return None if factor is None else value * factor


def _snapshot_from_income_row(row: pd.Series | None) -> EarningsSnapshot | None:
    if row is None:
        return None
    end_date = str(row.get("end_date") or "")
    revenue = pd.to_numeric(
        pd.Series([row.get("revenue", row.get("total_revenue"))]),
        errors="coerce",
    ).iloc[0]
    net_profit_parent = pd.to_numeric(
        pd.Series([row.get("n_income_attr_p", row.get("n_income"))]),
        errors="coerce",
    ).iloc[0]
    revenue_v = None if pd.isna(revenue) else float(revenue)
    profit_v = None if pd.isna(net_profit_parent) else float(net_profit_parent)
    return EarningsSnapshot(
        end_date=end_date,
        period=_period_label(end_date),
        revenue=revenue_v,
        net_profit_parent=profit_v,
        annualized_revenue=_annualize_cumulative(revenue_v, end_date),
        annualized_net_profit_parent=_annualize_cumulative(profit_v, end_date),
    )


def _latest_rows(income: pd.DataFrame) -> tuple[pd.Series | None, pd.Series | None]:
    if income is None or income.empty:
        return None, None
    ordered = income.copy()
    ordered["end_date"] = ordered["end_date"].astype(str)
    ordered = ordered.sort_values("end_date", ascending=False)
    latest_any = ordered.iloc[0]
    annual = ordered[ordered["end_date"].str.endswith("1231")]
    latest_annual = None if annual.empty else annual.iloc[0]
    return latest_any, latest_annual


def _build_driver_rows(derived: pd.DataFrame) -> list[dict[str, str]]:
    if derived is None or derived.empty:
        return []
    ordered = derived.copy()
    ordered["end_date"] = ordered["end_date"].astype(str)
    ordered = ordered.sort_values("end_date", ascending=False)
    latest = ordered.iloc[0]
    previous = ordered.iloc[1] if len(ordered) > 1 else None

    def _delta(col: str) -> str:
        if previous is None:
            return "N/A"
        latest_v = pd.to_numeric(pd.Series([latest.get(col)]), errors="coerce").iloc[0]
        prev_v = pd.to_numeric(pd.Series([previous.get(col)]), errors="coerce").iloc[0]
        if pd.isna(latest_v) or pd.isna(prev_v):
            return "N/A"
        return f"{latest_v - prev_v:+.2f}pp"

    return [
        {
            "driver": "Revenue base",
            "latest_signal": _format_value(latest.get("revenue_base")),
            "change_vs_prior_report": "N/A",
            "model_role": "top-line starting point for volume × price × mix",
        },
        {
            "driver": "Gross margin",
            "latest_signal": _format_value(latest.get("reported_gross_margin"), "%"),
            "change_vs_prior_report": _delta("reported_gross_margin"),
            "model_role": "main bridge from demand to gross profit",
        },
        {
            "driver": "Operating margin",
            "latest_signal": _format_value(latest.get("derived_operating_margin"), "%"),
            "change_vs_prior_report": _delta("derived_operating_margin"),
            "model_role": "tests pricing, mix, and cost absorption",
        },
        {
            "driver": "Net margin",
            "latest_signal": _format_value(latest.get("derived_net_margin"), "%"),
            "change_vs_prior_report": _delta("derived_net_margin"),
            "model_role": "captures final earnings conversion",
        },
        {
            "driver": "Finance-expense ratio",
            "latest_signal": _format_value(latest.get("finance_expense_ratio"), "%"),
            "change_vs_prior_report": _delta("finance_expense_ratio"),
            "model_role": "captures leverage drag or relief",
        },
        {
            "driver": "OCF / net profit",
            "latest_signal": _format_value(latest.get("ocf_to_net_profit")),
            "change_vs_prior_report": "N/A",
            "model_role": "tests earnings quality and cash realization",
        },
        {
            "driver": "Receivables / revenue",
            "latest_signal": _format_value(latest.get("receivables_to_revenue"), "%"),
            "change_vs_prior_report": _delta("receivables_to_revenue"),
            "model_role": "tests working-capital drag; interim periods use annualized revenue",
        },
        {
            "driver": "Inventory / revenue",
            "latest_signal": _format_value(latest.get("inventory_to_revenue"), "%"),
            "change_vs_prior_report": _delta("inventory_to_revenue"),
            "model_role": "tests inventory build and demand quality; interim periods use annualized revenue",
        },
    ]


def get_earnings_model_context(ticker: str, curr_date: str) -> str:
    """Build an evidence-led earnings bridge for A-share research workflows."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Earnings-model context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    income = _fetch_income_statement_data(symbol, curr_date, freq="quarterly", limit=8)
    balance = _fetch_balance_sheet_data(symbol, curr_date, freq="quarterly", limit=8)
    cashflow = _fetch_cashflow_data(symbol, curr_date, freq="quarterly", limit=8)
    indicators = _fetch_fina_indicator(symbol, curr_date)
    derived = _derive_financial_metrics(income, balance, cashflow, indicators)
    latest_any_row, latest_annual_row = _latest_rows(income)
    latest_any = _snapshot_from_income_row(latest_any_row)
    latest_annual = _snapshot_from_income_row(latest_annual_row)

    snapshot_rows = []
    for label, snap in (("latest reported", latest_any), ("latest annual", latest_annual)):
        if snap is None:
            continue
        snapshot_rows.append(
            {
                "snapshot": label,
                "period": snap.period,
                "end_date": snap.end_date,
                "revenue": snap.revenue,
                "net_profit_parent": snap.net_profit_parent,
                "annualized_revenue": snap.annualized_revenue,
                "annualized_net_profit_parent": snap.annualized_net_profit_parent,
            }
        )

    lines = [
        f"# Earnings-model context for {symbol} as of {curr_date}",
        "",
        f"- Company: {_format_value(None if basic is None else basic.get('name'))}",
        "- Purpose: convert the thesis into a disciplined earnings bridge instead of a free-floating narrative.",
        "",
        "## Earnings Snapshots",
        _markdown_table(pd.DataFrame(snapshot_rows)),
        "",
        "## Operating Driver Bridge",
        _markdown_table(pd.DataFrame(_build_driver_rows(derived))),
        "",
        "## Research Hygiene Notes",
        "- Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.",
        "- Treat one-quarter margin inflections as provisional until they recur or are explained by filing evidence.",
        "",
        "## Scenario-Building Instructions",
        "- Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.",
        "- Use three cases only: bull, base, bear. For each case, state which operating driver changes, not merely the target price.",
        "- Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.",
        "- When a thesis depends on a missing driver, keep the case conditional and state the exact future filing or industry datum that would update the model.",
        "- Do not upgrade a rating because a story is attractive; upgrade only when the earnings bridge or valuation bridge improves.",
    ]
    return "\n".join(lines)
