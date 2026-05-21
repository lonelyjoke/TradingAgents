from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta

from .tushare_a_stock import (
    TushareDataError,
    _fetch_balance_sheet_data,
    _fetch_cashflow_data,
    _fetch_daily_basic_latest,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    _to_tushare_date,
    is_a_share_symbol,
)
from .tushare_research import (
    _fetch_announcements,
    _safe_optional_query,
)


_CAPITAL_ALLOCATION_PATTERNS: dict[str, tuple[str, ...]] = {
    "dividend": ("分红", "利润分配", "现金红利"),
    "repurchase": ("回购",),
    "financing": ("定增", "增发", "配股", "可转债", "中期票据", "公司债", "融资", "发行股票"),
    "mna": ("收购", "并购", "重大资产重组", "股权转让"),
    "capex": ("扩产", "募投项目", "项目投资", "在建工程"),
    "equity_incentive": ("股权激励", "员工持股"),
}


def _date_window(curr_date: str, years: int = 3) -> tuple[str, str]:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    return _to_tushare_date(start_dt.strftime("%Y-%m-%d")), _to_tushare_date(curr_date)


def _announcement_category(title: str) -> str:
    text = str(title or "")
    for category, patterns in _CAPITAL_ALLOCATION_PATTERNS.items():
        if any(pattern in text for pattern in patterns):
            return category
    return "other"


def _management_snapshot(symbol: str) -> pd.DataFrame | TushareDataError:
    result = _safe_optional_query("stock_company", ts_code=symbol)
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        "ts_code",
        "chairman",
        "manager",
        "secretary",
        "reg_capital",
        "setup_date",
        "province",
        "main_business",
    ]
    return result[[col for col in keep if col in result.columns]].copy()


def _management_rewards(symbol: str, curr_date: str, years: int = 3) -> pd.DataFrame | TushareDataError:
    start, end = _date_window(curr_date, years)
    result = _safe_optional_query(
        "stk_rewards",
        ts_code=symbol,
        start_date=start,
        end_date=end,
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    if "ts_code" in result.columns:
        result = result[result["ts_code"].astype(str) == symbol].copy()
        if result.empty:
            return result
    keep = [
        "ann_date",
        "end_date",
        "name",
        "title",
        "reward",
        "hold_vol",
    ]
    data = result[[col for col in keep if col in result.columns]].copy()
    for col in ["reward", "hold_vol"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    return data.sort_values(["end_date", "ann_date"], ascending=False)


def _dividends(symbol: str, curr_date: str, years: int = 5) -> pd.DataFrame | TushareDataError:
    start, end = _date_window(curr_date, years)
    result = _safe_optional_query(
        "dividend",
        ts_code=symbol,
        ann_date_start=start,
        ann_date_end=end,
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        "ann_date",
        "end_date",
        "div_proc",
        "cash_div_tax",
        "stk_div",
        "record_date",
        "ex_date",
        "pay_date",
    ]
    return result[[col for col in keep if col in result.columns]].sort_values(
        ["end_date", "ann_date"], ascending=False
    )


def _repurchases(symbol: str, curr_date: str, years: int = 3) -> pd.DataFrame | TushareDataError:
    start, end = _date_window(curr_date, years)
    result = _safe_optional_query(
        "repurchase",
        ts_code=symbol,
        start_date=start,
        end_date=end,
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    if "ts_code" in result.columns:
        result = result[result["ts_code"].astype(str) == symbol].copy()
        if result.empty:
            return result
    keep = [
        "ann_date",
        "end_date",
        "proc",
        "exp_date",
        "vol",
        "amount",
        "high_limit",
        "low_limit",
    ]
    cleaned = result[[col for col in keep if col in result.columns]].drop_duplicates()
    return cleaned.sort_values(
        ["ann_date"], ascending=False
    )


def _capital_allocation_announcements(symbol: str, curr_date: str, years: int = 3) -> pd.DataFrame:
    announcements = _fetch_announcements(symbol, curr_date, look_back_days=years * 366)
    if isinstance(announcements, TushareDataError) or announcements is None or announcements.empty:
        return pd.DataFrame()
    data = announcements.copy()
    data["category"] = data.get("title", "").map(_announcement_category)
    data = data[data["category"] != "other"]
    cols = [col for col in ["ann_date", "category", "title"] if col in data.columns]
    return data[cols].head(20)


def _capital_flow_table(symbol: str, curr_date: str) -> pd.DataFrame:
    cashflow = _fetch_cashflow_data(symbol, curr_date, freq="annual", limit=5)
    balance = _fetch_balance_sheet_data(symbol, curr_date, freq="annual", limit=5)
    if cashflow is None or cashflow.empty:
        return pd.DataFrame()
    merged = cashflow.copy()
    if balance is not None and not balance.empty:
        keep = [col for col in ["end_date", "money_cap", "goodwill", "total_assets", "total_liab"] if col in balance.columns]
        merged = merged.merge(balance[keep], on="end_date", how="left")
    cols = [
        "end_date",
        "n_cashflow_act",
        "c_pay_acq_const_fiolta",
        "c_recp_disp_fiolta",
        "c_pay_dist_dpcp_int_exp",
        "n_cashflow_inv_act",
        "n_cashflow_fin_act",
        "money_cap",
        "goodwill",
        "total_assets",
        "total_liab",
    ]
    return merged[[col for col in cols if col in merged.columns]].copy()


def _dividend_yield_cross_check(
    dividends: pd.DataFrame | TushareDataError,
    daily_basic: pd.Series | None,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    close = None
    dv_ttm = None
    if daily_basic is not None:
        close_v = pd.to_numeric(pd.Series([daily_basic.get("close")]), errors="coerce").iloc[0]
        dv_ttm_v = pd.to_numeric(pd.Series([daily_basic.get("dv_ttm")]), errors="coerce").iloc[0]
        close = None if pd.isna(close_v) else float(close_v)
        dv_ttm = None if pd.isna(dv_ttm_v) else float(dv_ttm_v)
    if dv_ttm is not None:
        rows.append(
            {
                "basis": "Tushare daily_basic dv_ttm",
                "cash_div_per_share": None,
                "reference_price": close,
                "yield_pct": dv_ttm,
                "note": "Use as the primary trailing dividend-yield reference when present.",
            }
        )
    if isinstance(dividends, pd.DataFrame) and not dividends.empty and "end_date" in dividends.columns:
        data = dividends.copy()
        if "cash_div_tax" in data.columns:
            data["cash_div_tax"] = pd.to_numeric(data["cash_div_tax"], errors="coerce")
            grouped = (
                data.dropna(subset=["cash_div_tax"])
                .groupby("end_date", dropna=False)["cash_div_tax"]
                .sum()
                .reset_index()
                .sort_values("end_date", ascending=False)
                .head(5)
            )
            for _, row in grouped.iterrows():
                cash_div = float(row["cash_div_tax"])
                rows.append(
                    {
                        "basis": f"sum of announced dividends for end_date {row['end_date']}",
                        "cash_div_per_share": cash_div,
                        "reference_price": close,
                        "yield_pct": None if close in (None, 0) else cash_div / close * 100,
                        "note": "Check whether this includes annual, interim, and special dividends before citing shareholder yield.",
                    }
                )
    return pd.DataFrame(rows)


def get_management_capital_allocation_context(
    ticker: str,
    curr_date: str,
    look_back_years: int = 3,
) -> str:
    """Assess management hard signals and capital allocation behavior."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Management/capital-allocation context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    snapshot = _management_snapshot(symbol)
    rewards = _management_rewards(symbol, curr_date, years=look_back_years)
    dividends = _dividends(symbol, curr_date, years=max(look_back_years, 5))
    repurchases = _repurchases(symbol, curr_date, years=look_back_years)
    capflows = _capital_flow_table(symbol, curr_date)
    announcements = _capital_allocation_announcements(symbol, curr_date, years=look_back_years)
    daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
    dividend_yield_check = _dividend_yield_cross_check(dividends, daily_basic)

    lines = [
        f"# Management and capital-allocation context for {symbol} as of {curr_date}",
        "",
        f"- Company: {_format_value(None if basic is None else basic.get('name'))}",
        "- Scope: use hard evidence to assess stewardship; do not pretend management quality is fully quantifiable from one snapshot.",
        "",
        "## Management Snapshot",
        _markdown_table(snapshot if isinstance(snapshot, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Management Compensation And Holdings",
        _markdown_table(rewards if isinstance(rewards, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Capital Allocation Cash Flows",
        _markdown_table(capflows),
        "",
        "## Dividend History",
        _markdown_table(dividends if isinstance(dividends, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Dividend Yield Cross-Check",
        _markdown_table(dividend_yield_check),
        "",
        "## Repurchase History",
        _markdown_table(repurchases if isinstance(repurchases, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Capital Allocation Announcements",
        _markdown_table(announcements),
        "",
        "## Analyst Instructions",
        "- Separate stewardship from narration: reward managers for durable ROIC, cash generation, sensible leverage, disciplined capex, and shareholder returns, not for grand plans alone.",
        "- Read investing cash outflow together with future revenue, margin, and ROIC evidence; capex is good only when later returns justify it.",
        "- Use goodwill, acquisitions, financing, dividends, and buybacks to judge whether capital is being compounded, hoarded, or diluted away.",
        "- When citing dividend yield, prefer `dv_ttm` or a summed trailing dividend basis; do not mix a single annual proposal with full-year shareholder-return language unless you label it as annual-only.",
        "- Management quality is a synthesis variable: combine these hard signals with long-run delivery against prior promises in filings and announcements.",
    ]
    return "\n".join(lines)
