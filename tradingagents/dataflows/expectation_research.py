from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta

from .tushare_a_stock import (
    TushareDataError,
    _fetch_daily_basic_latest,
    _fetch_income_statement_data,
    _fetch_stock_basic,
    _format_value,
    _format_yyyymmdd,
    _markdown_table,
    _to_tushare_date,
    is_a_share_symbol,
)
from .tushare_research import _query_optional_api
from .earnings_modeling import _snapshot_from_income_row, _latest_rows


@dataclass(frozen=True)
class ImpliedExpectationSnapshot:
    market_cap_cny: float | None
    pe_ttm: float | None
    ps_ttm: float | None
    implied_ttm_earnings_cny: float | None
    implied_ttm_sales_cny: float | None


def _safe_div(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator is None or denominator == 0:
        return None
    return numerator / denominator


def _implied_snapshot(daily_basic: pd.Series | None) -> ImpliedExpectationSnapshot:
    if daily_basic is None:
        return ImpliedExpectationSnapshot(None, None, None, None, None)
    total_mv = pd.to_numeric(pd.Series([daily_basic.get("total_mv")]), errors="coerce").iloc[0]
    pe_ttm = pd.to_numeric(pd.Series([daily_basic.get("pe_ttm")]), errors="coerce").iloc[0]
    ps_ttm = pd.to_numeric(pd.Series([daily_basic.get("ps_ttm")]), errors="coerce").iloc[0]
    market_cap_cny = None if pd.isna(total_mv) else float(total_mv) * 10_000
    pe_v = None if pd.isna(pe_ttm) else float(pe_ttm)
    ps_v = None if pd.isna(ps_ttm) else float(ps_ttm)
    return ImpliedExpectationSnapshot(
        market_cap_cny=market_cap_cny,
        pe_ttm=pe_v,
        ps_ttm=ps_v,
        implied_ttm_earnings_cny=_safe_div(market_cap_cny, pe_v),
        implied_ttm_sales_cny=_safe_div(market_cap_cny, ps_v),
    )


def _metric_percentile(data: pd.DataFrame, metric: str) -> float | None:
    if data is None or data.empty or metric not in data.columns:
        return None
    numeric = pd.to_numeric(data[metric], errors="coerce").dropna()
    if numeric.empty:
        return None
    latest = numeric.iloc[-1]
    return float((numeric <= latest).mean() * 100)


def _valuation_history(symbol: str, curr_date: str, years: int = 5) -> pd.DataFrame:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    data = _query_optional_api(
        "daily_basic",
        ts_code=symbol,
        start_date=_to_tushare_date(start_dt.strftime("%Y-%m-%d")),
        end_date=_to_tushare_date(end_dt.strftime("%Y-%m-%d")),
        fields="ts_code,trade_date,pe_ttm,pb,ps_ttm,dv_ttm,total_mv",
    )
    if data is None or data.empty:
        return pd.DataFrame()
    return data.sort_values("trade_date")


def _rounded_percentile_or_none(data: pd.DataFrame, metric: str) -> float | None:
    value = _metric_percentile(data, metric)
    return None if value is None else round(value, 1)


def get_market_expectation_context(ticker: str, curr_date: str, years: int = 5) -> str:
    """Reverse the current quote into the expectations the market is approximately carrying."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Market-expectation context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
    income = _fetch_income_statement_data(symbol, curr_date, freq="quarterly", limit=8)
    latest_any_row, latest_annual_row = _latest_rows(income)
    latest_any = _snapshot_from_income_row(latest_any_row)
    latest_annual = _snapshot_from_income_row(latest_annual_row)
    implied = _implied_snapshot(daily_basic)
    history = _valuation_history(symbol, curr_date, years=years)

    rows = [
        {
            "metric": "Market cap (CNY)",
            "value": implied.market_cap_cny,
            "interpretation": "current equity value",
        },
        {
            "metric": "PE TTM",
            "value": implied.pe_ttm,
            "interpretation": "earnings multiple the market is paying now",
        },
        {
            "metric": "PS TTM",
            "value": implied.ps_ttm,
            "interpretation": "sales multiple the market is paying now",
        },
        {
            "metric": "Implied TTM earnings (CNY)",
            "value": implied.implied_ttm_earnings_cny,
            "interpretation": "market cap divided by PE TTM",
        },
        {
            "metric": "Implied TTM sales (CNY)",
            "value": implied.implied_ttm_sales_cny,
            "interpretation": "market cap divided by PS TTM",
        },
        {
            "metric": "PE percentile",
            "value": None if history.empty else _rounded_percentile_or_none(history, "pe_ttm"),
            "interpretation": f"{years}-year valuation position",
        },
        {
            "metric": "PB percentile",
            "value": None if history.empty else _rounded_percentile_or_none(history, "pb"),
            "interpretation": f"{years}-year valuation position",
        },
        {
            "metric": "PS percentile",
            "value": None if history.empty else _rounded_percentile_or_none(history, "ps_ttm"),
            "interpretation": f"{years}-year valuation position",
        },
    ]

    comparison_rows = []
    if latest_annual is not None:
        comparison_rows.append(
            {
                "benchmark": "latest annual parent profit",
                "value": latest_annual.net_profit_parent,
                "vs_implied_ttm_earnings": _safe_div(
                    latest_annual.net_profit_parent,
                    implied.implied_ttm_earnings_cny,
                ),
            }
        )
    if latest_any is not None:
        comparison_rows.append(
            {
                "benchmark": f"latest reported annualized parent profit ({latest_any.period})",
                "value": latest_any.annualized_net_profit_parent,
                "vs_implied_ttm_earnings": _safe_div(
                    latest_any.annualized_net_profit_parent,
                    implied.implied_ttm_earnings_cny,
                ),
            }
        )

    lines = [
        f"# Market-expectation context for {symbol} as of {curr_date}",
        "",
        f"- Company: {_format_value(None if basic is None else basic.get('name'))}",
        f"- Valuation trade date: {_format_yyyymmdd(None if daily_basic is None else daily_basic.get('trade_date'))}",
        "- Purpose: separate a good company from a good investment by asking what the current price already implies.",
        "",
        "## Implied Valuation Snapshot",
        _markdown_table(pd.DataFrame(rows)),
        "",
        "## Earnings Benchmarks Versus Implied TTM Earnings",
        _markdown_table(pd.DataFrame(comparison_rows)),
        "",
        "## Analyst Instructions",
        "- Do not call a stock cheap or expensive from PE/PB alone. State what earnings power, sales scale, or durability the current quote appears to require.",
        "- Compare the implied TTM earnings with latest annual and latest annualized reported earnings before claiming an expectation gap.",
        "- If current valuation already assumes recovery, say so; if it still prices in deterioration despite improving drivers, say so.",
        "- Translate every rating into a view on mispricing: which assumption in the market quote is too optimistic or too pessimistic?",
    ]
    return "\n".join(lines)
