from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .industry_classifier import is_banking_entity
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
    seasonality_adjusted_revenue: float | None
    seasonality_adjusted_net_profit_parent: float | None
    seasonality_method: str


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


def _seasonality_share(
    income: pd.DataFrame,
    *,
    end_date: str,
    value_col: str,
) -> float | None:
    """Estimate the historical cumulative-period share of full-year results."""
    if income is None or income.empty:
        return None
    if value_col not in income.columns:
        return None
    text = str(end_date or "")
    if len(text) < 8 or text.endswith("1231"):
        return 1.0 if text.endswith("1231") else None
    period_suffix = text[-4:]
    current_year = text[:4]
    data = income.copy()
    data["end_date"] = data["end_date"].astype(str)
    data[value_col] = pd.to_numeric(data.get(value_col), errors="coerce")
    data["year"] = data["end_date"].str[:4]
    shares: list[float] = []
    for year, group in data.groupby("year"):
        if year >= current_year:
            continue
        period_rows = group[group["end_date"].str.endswith(period_suffix)]
        annual_rows = group[group["end_date"].str.endswith("1231")]
        if period_rows.empty or annual_rows.empty:
            continue
        period_v = period_rows.sort_values("end_date").iloc[-1][value_col]
        annual_v = annual_rows.sort_values("end_date").iloc[-1][value_col]
        if pd.isna(period_v) or pd.isna(annual_v) or annual_v == 0:
            continue
        share = float(period_v) / float(annual_v)
        if 0 < share < 1.5:
            shares.append(share)
    if not shares:
        return None
    return float(pd.Series(shares).median())


def _seasonality_adjusted_value(
    value: float | None,
    *,
    end_date: str,
    income: pd.DataFrame | None,
    value_col: str,
) -> tuple[float | None, str]:
    if value is None:
        return None, "missing reported value"
    if str(end_date or "").endswith("1231"):
        return value, "FY actual"
    share = _seasonality_share(income if income is not None else pd.DataFrame(), end_date=end_date, value_col=value_col)
    if share:
        return value / share, f"historical median {str(end_date)[-4:]} share {share:.1%}"
    fallback = _annualize_cumulative(value, end_date)
    return fallback, "simple run-rate fallback; no historical seasonal share available"


def _snapshot_from_income_row(
    row: pd.Series | None,
    income: pd.DataFrame | None = None,
) -> EarningsSnapshot | None:
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
    adjusted_revenue, revenue_method = _seasonality_adjusted_value(
        revenue_v,
        end_date=end_date,
        income=income,
        value_col="revenue",
    )
    adjusted_profit, profit_method = _seasonality_adjusted_value(
        profit_v,
        end_date=end_date,
        income=income,
        value_col="n_income_attr_p",
    )
    method = profit_method if profit_v is not None else revenue_method
    return EarningsSnapshot(
        end_date=end_date,
        period=_period_label(end_date),
        revenue=revenue_v,
        net_profit_parent=profit_v,
        annualized_revenue=_annualize_cumulative(revenue_v, end_date),
        annualized_net_profit_parent=_annualize_cumulative(profit_v, end_date),
        seasonality_adjusted_revenue=adjusted_revenue,
        seasonality_adjusted_net_profit_parent=adjusted_profit,
        seasonality_method=method,
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
    latest_end_date = str(latest.get("end_date") or "")
    comparable = ordered[
        (ordered["end_date"].str[-4:] == latest_end_date[-4:])
        & (ordered["end_date"] < latest_end_date)
    ]
    # Same-period year-on-year comparison is the only clean basis for an
    # interim margin delta.  Fall back to the immediately prior report only
    # when the history does not contain a comparable period, and label it.
    if not comparable.empty:
        previous = comparable.iloc[0]
        comparison_basis = f"YoY: {latest_end_date} vs {previous.get('end_date')}"
    else:
        previous = ordered.iloc[1] if len(ordered) > 1 else None
        comparison_basis = (
            f"sequential-report fallback: {latest_end_date} vs {previous.get('end_date')}"
            if previous is not None
            else "N/A"
        )

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
            "comparison_basis": comparison_basis,
            "model_role": "top-line starting point for volume × price × mix",
        },
        {
            "driver": "Gross margin",
            "latest_signal": _format_value(latest.get("reported_gross_margin"), "%"),
            "change_vs_prior_report": _delta("reported_gross_margin"),
            "comparison_basis": comparison_basis,
            "model_role": "main bridge from demand to gross profit",
        },
        {
            "driver": "Operating margin",
            "latest_signal": _format_value(latest.get("derived_operating_margin"), "%"),
            "change_vs_prior_report": _delta("derived_operating_margin"),
            "comparison_basis": comparison_basis,
            "model_role": "tests pricing, mix, and cost absorption",
        },
        {
            "driver": "Net margin",
            "latest_signal": _format_value(latest.get("derived_net_margin"), "%"),
            "change_vs_prior_report": _delta("derived_net_margin"),
            "comparison_basis": comparison_basis,
            "model_role": "captures final earnings conversion",
        },
        {
            "driver": "Finance-expense ratio",
            "latest_signal": _format_value(latest.get("finance_expense_ratio"), "%"),
            "change_vs_prior_report": _delta("finance_expense_ratio"),
            "comparison_basis": comparison_basis,
            "model_role": "captures leverage drag or relief",
        },
        {
            "driver": "OCF / net profit",
            "latest_signal": _format_value(latest.get("ocf_to_net_profit")),
            "change_vs_prior_report": "N/A",
            "comparison_basis": comparison_basis,
            "model_role": "tests earnings quality and cash realization",
        },
        {
            "driver": "Receivables / revenue",
            "latest_signal": _format_value(latest.get("receivables_to_revenue"), "%"),
            "change_vs_prior_report": _delta("receivables_to_revenue"),
            "comparison_basis": comparison_basis,
            "model_role": "tests working-capital drag; interim periods use annualized revenue",
        },
        {
            "driver": "Inventory / revenue",
            "latest_signal": _format_value(latest.get("inventory_to_revenue"), "%"),
            "change_vs_prior_report": _delta("inventory_to_revenue"),
            "comparison_basis": comparison_basis,
            "model_role": "tests inventory build and demand quality; interim periods use annualized revenue",
        },
    ]


def _is_banking_stock(symbol: str, basic: pd.Series | None) -> bool:
    return is_banking_entity(symbol, basic=basic)


def _bank_driver_rows(
    income: pd.DataFrame,
    balance: pd.DataFrame,
    indicators: pd.DataFrame,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def latest_row(frame: pd.DataFrame) -> pd.Series:
        if frame is None or frame.empty or "end_date" not in frame.columns:
            return pd.Series(dtype="object")
        ordered = frame.copy()
        ordered["end_date"] = ordered["end_date"].astype(str)
        return ordered.sort_values("end_date", ascending=False).iloc[0]

    latest_income = latest_row(income)
    latest_balance = latest_row(balance)
    latest_indicator = latest_row(indicators)

    rows.append(
        {
            "driver": "Net profit run-rate",
            "latest_signal": _format_value(latest_income.get("n_income_attr_p")),
            "change_vs_prior_report": _format_value(latest_indicator.get("netprofit_yoy"), "%"),
            "model_role": "starting point for bank EPS; use seasonality-adjusted profit, not generic sales-volume logic",
        }
    )
    rows.append(
        {
            "driver": "ROE / ROA",
            "latest_signal": f"ROE {_format_value(latest_indicator.get('roe'), '%')} / ROA {_format_value(latest_indicator.get('roa'), '%')}",
            "change_vs_prior_report": "N/A",
            "model_role": "connect PB valuation to sustainable profitability and cost of equity",
        }
    )
    rows.append(
        {
            "driver": "Balance-sheet scale",
            "latest_signal": f"assets {_format_value(latest_balance.get('total_assets'))} / liabilities {_format_value(latest_balance.get('total_liab'))}",
            "change_vs_prior_report": "N/A",
            "model_role": "loan/deposit and RWA growth must be checked in filings before treating expansion as positive",
        }
    )
    rows.append(
        {
            "driver": "Required bank filing metrics",
            "latest_signal": "NIM, loan yield, deposit cost, NPL, special-mention, overdue, provision coverage, CET1",
            "change_vs_prior_report": "read from Banking KPI Pack",
            "model_role": "core bank earnings bridge; do not substitute gross margin, inventory, receivables, or OCF ratios",
        }
    )
    return rows


def get_earnings_model_context(ticker: str, curr_date: str) -> str:
    """Build an evidence-led earnings bridge for A-share research workflows."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Earnings-model context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    income = _fetch_income_statement_data(symbol, curr_date, freq="quarterly", limit=20)
    balance = _fetch_balance_sheet_data(symbol, curr_date, freq="quarterly", limit=8)
    cashflow = _fetch_cashflow_data(symbol, curr_date, freq="quarterly", limit=8)
    indicators = _fetch_fina_indicator(symbol, curr_date)
    derived = _derive_financial_metrics(income, balance, cashflow, indicators)
    is_banking = _is_banking_stock(symbol, basic)
    latest_any_row, latest_annual_row = _latest_rows(income)
    latest_any = _snapshot_from_income_row(latest_any_row, income)
    latest_annual = _snapshot_from_income_row(latest_annual_row, income)

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
                "seasonality_adjusted_revenue": snap.seasonality_adjusted_revenue,
                "seasonality_adjusted_net_profit_parent": snap.seasonality_adjusted_net_profit_parent,
                "seasonality_method": snap.seasonality_method,
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
        _markdown_table(pd.DataFrame(_bank_driver_rows(income, balance, indicators) if is_banking else _build_driver_rows(derived))),
        "",
        "## Research Hygiene Notes",
        *(
            [
                "- Banking earnings must be bridged through NIM, balance-sheet mix, fee income, credit cost, asset quality, capital adequacy, and payout capacity.",
                "- Do not use manufacturing-style revenue = volume × price × mix, gross margin, inventory, receivables, or OCF conversion as primary bank drivers.",
                "- Treat simple annualized interim earnings as a run-rate stress test, not a forward forecast.",
                "- Prefer the seasonality-adjusted estimate when judging full-year earnings power, and verify bank-specific KPIs in the financial-report intelligence context.",
            ]
            if is_banking
            else [
                "- Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.",
                "- Treat simple annualized interim earnings as a run-rate stress test, not a forward forecast.",
                "- Prefer the seasonality-adjusted estimate when judging full-year earnings power, and state the historical share used.",
                "- Treat one-quarter margin inflections as provisional until they recur or are explained by filing evidence.",
            ]
        ),
        "",
        "## Scenario-Building Instructions",
        *(
            [
                "- Build every bank case through earning assets × NIM, fee income, credit cost, operating efficiency, tax/minority items, capital needs, and payout.",
                "- Use three cases only: bull, base, bear. For each case, state which bank driver changes, not merely the target price.",
                "- Tie every catalyst to one bank lever: NIM, deposit cost, retail/wholesale loan mix, fee take-rate, NPL/special-mention trend, provision coverage, CET1, or dividend.",
                "- When a thesis depends on a missing bank driver, keep the case conditional and state the exact future filing datum that would update the model.",
                "- Do not upgrade a rating because PB/PE is low; upgrade only when the bank-specific earnings or valuation bridge improves.",
            ]
            if is_banking
            else [
                "- Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.",
                "- Use three cases only: bull, base, bear. For each case, state which operating driver changes, not merely the target price.",
                "- Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.",
                "- When a thesis depends on a missing driver, keep the case conditional and state the exact future filing or industry datum that would update the model.",
                "- Do not upgrade a rating because a story is attractive; upgrade only when the earnings bridge or valuation bridge improves.",
            ]
        ),
    ]
    return "\n".join(lines)
