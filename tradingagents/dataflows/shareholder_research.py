from __future__ import annotations

from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta

from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    _to_tushare_date,
    is_a_share_symbol,
)
from .tushare_research import _safe_optional_query


def _recent_quarter_ends(curr_date: str, count: int = 4) -> list[str]:
    current = datetime.strptime(curr_date, "%Y-%m-%d")
    quarter_ends = []
    year = current.year
    candidates = [f"{year}0331", f"{year}0630", f"{year}0930", f"{year}1231"]
    for text in candidates:
        dt = datetime.strptime(text, "%Y%m%d")
        if dt <= current:
            quarter_ends.append(text)
    prev_year = year - 1
    while len(quarter_ends) < count:
        quarter_ends = [f"{prev_year}0331", f"{prev_year}0630", f"{prev_year}0930", f"{prev_year}1231"] + quarter_ends
        prev_year -= 1
    return quarter_ends[-count:]


def _holder_query(api_name: str, symbol: str, periods: list[str]) -> pd.DataFrame:
    frames = []
    for period in periods:
        result = _safe_optional_query(api_name, ts_code=symbol, period=period)
        if isinstance(result, TushareDataError) or result is None or result.empty:
            continue
        result = result.copy()
        if "period" not in result.columns and "end_date" in result.columns:
            result["period"] = result["end_date"].astype(str)
        frames.append(result)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def _holder_concentration(data: pd.DataFrame) -> pd.DataFrame:
    if data is None or data.empty:
        return pd.DataFrame()
    working = data.copy()
    keep = [col for col in ["period", "holder_name", "hold_amount", "hold_ratio"] if col in working.columns]
    working = working[keep]
    if "period" not in working.columns or "hold_ratio" not in working.columns:
        return working
    working["hold_ratio"] = pd.to_numeric(working["hold_ratio"], errors="coerce")
    grouped = (
        working.groupby("period", dropna=False)["hold_ratio"]
        .sum(min_count=1)
        .reset_index(name="top10_hold_ratio_sum")
        .sort_values("period", ascending=False)
    )
    return grouped


def _holder_display(data: pd.DataFrame) -> pd.DataFrame:
    if data is None or data.empty:
        return pd.DataFrame()
    display = data[[col for col in ["period", "holder_name", "hold_amount", "hold_ratio"] if col in data.columns]].copy()
    sort_cols = [col for col in ["period", "hold_ratio"] if col in display.columns]
    if "period" in display.columns:
        latest_period = display["period"].astype(str).max()
        display = display[display["period"].astype(str) == latest_period]
    if sort_cols:
        display = display.sort_values(sort_cols, ascending=[False] * len(sort_cols))
    return display.head(10)


def _safe_sort_desc(data: pd.DataFrame, preferred_cols: list[str]) -> pd.DataFrame:
    sort_cols = [col for col in preferred_cols if col in data.columns]
    if not sort_cols:
        return data
    return data.sort_values(sort_cols, ascending=[False] * len(sort_cols))


def _holder_number(symbol: str, curr_date: str, years: int = 3) -> pd.DataFrame | TushareDataError:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    result = _safe_optional_query(
        "stk_holdernumber",
        ts_code=symbol,
        start_date=_to_tushare_date(start_dt.strftime("%Y-%m-%d")),
        end_date=_to_tushare_date(curr_date),
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [col for col in ["ann_date", "end_date", "holder_num"] if col in result.columns]
    return _safe_sort_desc(result[keep], ["end_date", "ann_date"])


def _holder_trades(symbol: str, curr_date: str, years: int = 3) -> pd.DataFrame | TushareDataError:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    result = _safe_optional_query(
        "stk_holdertrade",
        ts_code=symbol,
        start_date=_to_tushare_date(start_dt.strftime("%Y-%m-%d")),
        end_date=_to_tushare_date(curr_date),
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        "ann_date",
        "holder_name",
        "holder_type",
        "in_de",
        "change_vol",
        "change_ratio",
        "after_share",
        "after_ratio",
        "avg_price",
    ]
    return _safe_sort_desc(result[[col for col in keep if col in result.columns]], ["ann_date"])


def _holder_trade_lifecycle(data: pd.DataFrame, curr_date: str) -> pd.DataFrame:
    """Summarize whether large holder reductions are historical or still current.

    Tushare's trade feed records executed changes, not necessarily the remaining
    intent of the holder. This bridge therefore avoids treating every historical
    reduction as a live overhang. Analysts still need separate evidence before
    claiming future selling pressure.
    """
    columns = [
        "holder_name",
        "latest_trade_date",
        "latest_direction",
        "latest_after_ratio",
        "days_since_latest_trade",
        "lifecycle_read",
    ]
    if data is None or data.empty:
        return pd.DataFrame(columns=columns)
    required = {"holder_name", "ann_date", "in_de"}
    if not required.issubset(data.columns):
        return pd.DataFrame(columns=columns)

    working = data.copy()
    working["ann_date"] = pd.to_datetime(working["ann_date"].astype(str), format="%Y%m%d", errors="coerce")
    working = working.dropna(subset=["ann_date"])
    if working.empty:
        return pd.DataFrame(columns=columns)

    current = datetime.strptime(curr_date, "%Y-%m-%d")
    rows = []
    for holder_name, group in working.groupby("holder_name", dropna=False):
        latest = group.sort_values("ann_date", ascending=False).iloc[0]
        latest_date = latest["ann_date"]
        days_since = (current - latest_date.to_pydatetime()).days
        latest_direction = str(latest.get("in_de") or "")
        if latest_direction == "DE":
            if days_since > 45:
                lifecycle = "executed historical reduction; future selling needs separate evidence"
            else:
                lifecycle = "recent executed reduction; monitor follow-through before calling it persistent"
        elif latest_direction == "IN":
            lifecycle = "latest disclosed action was an increase"
        else:
            lifecycle = "latest direction unclear; do not infer live pressure"
        rows.append(
            {
                "holder_name": holder_name,
                "latest_trade_date": latest_date.strftime("%Y%m%d"),
                "latest_direction": latest_direction,
                "latest_after_ratio": latest.get("after_ratio"),
                "days_since_latest_trade": days_since,
                "lifecycle_read": lifecycle,
            }
        )
    return pd.DataFrame(rows).sort_values("days_since_latest_trade")


def _pledge_stats(symbol: str) -> pd.DataFrame | TushareDataError:
    result = _safe_optional_query("pledge_stat", ts_code=symbol)
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        "end_date",
        "pledge_count",
        "unrest_pledge",
        "rest_pledge",
        "total_share",
        "pledge_ratio",
    ]
    return _safe_sort_desc(result[[col for col in keep if col in result.columns]], ["end_date"])


def _pledge_details(symbol: str) -> pd.DataFrame | TushareDataError:
    result = _safe_optional_query("pledge_detail", ts_code=symbol)
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        "ann_date",
        "holder_name",
        "pledge_amount",
        "start_date",
        "end_date",
        "is_release",
    ]
    return _safe_sort_desc(result[[col for col in keep if col in result.columns]], ["ann_date"]).head(20)


def _share_float(symbol: str, curr_date: str, years: int = 2) -> pd.DataFrame | TushareDataError:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    result = _safe_optional_query(
        "share_float",
        ts_code=symbol,
        start_date=_to_tushare_date(start_dt.strftime("%Y-%m-%d")),
        end_date=_to_tushare_date(curr_date),
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        "ann_date",
        "float_date",
        "float_share",
        "float_ratio",
        "holder_name",
        "share_type",
    ]
    return _safe_sort_desc(result[[col for col in keep if col in result.columns]], ["float_date"])


def get_shareholder_structure_context(
    ticker: str,
    curr_date: str,
    look_back_years: int = 3,
) -> str:
    """Assess ownership structure, chip concentration, and supply-overhang signals."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Shareholder-structure context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    periods = _recent_quarter_ends(curr_date, count=4)
    top10 = _holder_query("top10_holders", symbol, periods)
    float_top10 = _holder_query("top10_floatholders", symbol, periods)
    holder_num = _holder_number(symbol, curr_date, years=look_back_years)
    holder_trade = _holder_trades(symbol, curr_date, years=look_back_years)
    pledge_stat = _pledge_stats(symbol)
    pledge_detail = _pledge_details(symbol)
    share_float = _share_float(symbol, curr_date, years=2)

    top10_display = _holder_display(top10)
    float_display = _holder_display(float_top10)

    lines = [
        f"# Shareholder-structure context for {symbol} as of {curr_date}",
        "",
        f"- Company: {_format_value(None if basic is None else basic.get('name'))}",
        f"- Quarter-ends sampled: {', '.join(periods)}",
        "",
        "## Top-10 Holder Concentration",
        _markdown_table(_holder_concentration(top10)),
        "",
        "## Top-10 Holders",
        _markdown_table(top10_display),
        "",
        "## Top-10 Float Holder Concentration",
        _markdown_table(_holder_concentration(float_top10)),
        "",
        "## Top-10 Float Holders",
        _markdown_table(float_display),
        "",
        "## Holder Count",
        _markdown_table(holder_num if isinstance(holder_num, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Holder Increase / Decrease",
        _markdown_table(holder_trade if isinstance(holder_trade, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Holder Trade Lifecycle",
        _markdown_table(
            _holder_trade_lifecycle(holder_trade, curr_date)
            if isinstance(holder_trade, pd.DataFrame)
            else pd.DataFrame()
        ),
        "",
        "## Pledge Statistics",
        _markdown_table(pledge_stat if isinstance(pledge_stat, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Pledge Details",
        _markdown_table(pledge_detail if isinstance(pledge_detail, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Unlock / Float Supply",
        _markdown_table(share_float if isinstance(share_float, pd.DataFrame) else pd.DataFrame()),
        "",
        "## Analyst Instructions",
        "- Distinguish ownership quality from short-term flow: concentrated strategic ownership can be stabilizing, while crowded float ownership can also amplify exits.",
        "- Read holder-count changes together with price action and float-holder changes before claiming retail crowding or institutional accumulation.",
        "- Distinguish executed historical selling from live future supply. Once a disclosed reduction has already happened, do not keep calling it a current headwind unless later filings, unlock schedules, or new holder data support a separate future-overhang thesis.",
        "- Treat insider reductions, high pledge ratios, and near-term unlocks as potential supply overhangs, but connect them to size, timing, lifecycle stage, and separately verified future tradability before changing the thesis.",
        "- Use this layer to refine current odds and relative allocation; it should rarely override core business quality by itself.",
    ]
    return "\n".join(lines)
