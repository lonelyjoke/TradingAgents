from __future__ import annotations

from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta

from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _format_yyyymmdd,
    _markdown_table,
    _to_tushare_date,
    is_a_share_symbol,
)
from .tushare_research import _query_optional_api


def _safe_pct(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "N/A"
    return f"{value * 100:.1f}%"


def _safe_float(value) -> float | None:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(parsed):
        return None
    return float(parsed)


def _fetch_price_history(symbol: str, curr_date: str, years: int = 5) -> pd.DataFrame:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    data = _query_optional_api(
        "daily",
        ts_code=symbol,
        start_date=_to_tushare_date(start_dt.strftime("%Y-%m-%d")),
        end_date=_to_tushare_date(end_dt.strftime("%Y-%m-%d")),
        fields="ts_code,trade_date,close",
    )
    if data is None or data.empty:
        return pd.DataFrame()
    return data.sort_values("trade_date")


def _fetch_valuation_history(symbol: str, curr_date: str, years: int = 5) -> pd.DataFrame:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    data = _query_optional_api(
        "daily_basic",
        ts_code=symbol,
        start_date=_to_tushare_date(start_dt.strftime("%Y-%m-%d")),
        end_date=_to_tushare_date(end_dt.strftime("%Y-%m-%d")),
        fields="ts_code,trade_date,pe_ttm,pb,ps_ttm,total_mv",
    )
    if data is None or data.empty:
        return pd.DataFrame()
    return data.sort_values("trade_date")


def _build_price_eps_pe_history(
    price_history: pd.DataFrame,
    valuation_history: pd.DataFrame,
) -> pd.DataFrame:
    """Join price and PE history, then infer a consistent TTM EPS proxy.

    Tushare's daily PE TTM is calculated from the contemporaneous market price.
    Therefore close / PE TTM is not a replacement for reported EPS, but it is a
    useful internally consistent proxy for asking whether price changes were
    driven more by EPS movement or by multiple movement.
    """
    if price_history is None or price_history.empty:
        return pd.DataFrame()
    if valuation_history is None or valuation_history.empty:
        return pd.DataFrame()

    prices = price_history.copy()
    values = valuation_history.copy()
    for frame, columns in [
        (prices, ["close"]),
        (values, ["pe_ttm", "pb", "ps_ttm", "total_mv"]),
    ]:
        for col in columns:
            if col in frame.columns:
                frame[col] = pd.to_numeric(frame[col], errors="coerce")

    history = pd.merge(
        prices[["ts_code", "trade_date", "close"]],
        values[["ts_code", "trade_date", "pe_ttm", "pb", "ps_ttm", "total_mv"]],
        on=["ts_code", "trade_date"],
        how="inner",
    ).sort_values("trade_date")
    if history.empty:
        return history

    history = history[(history["close"] > 0) & (history["pe_ttm"] > 0)].copy()
    if history.empty:
        return history
    history["eps_ttm_proxy"] = history["close"] / history["pe_ttm"]
    history["market_cap_cny"] = history["total_mv"] * 10_000
    history["trade_dt"] = pd.to_datetime(history["trade_date"], format="%Y%m%d", errors="coerce")
    return history.dropna(subset=["trade_dt", "eps_ttm_proxy"])


def _nearest_row_on_or_after(history: pd.DataFrame, target_dt: pd.Timestamp) -> pd.Series | None:
    if history.empty:
        return None
    candidates = history[history["trade_dt"] >= target_dt]
    if candidates.empty:
        candidates = history
    return candidates.iloc[0]


def _classify_driver(price_change: float, eps_change: float, pe_change: float) -> str:
    """Classify what mainly explains the price move."""
    if abs(price_change) < 0.03:
        return "price broadly flat; focus on whether EPS and PE offset each other"
    if price_change > 0:
        if eps_change > 0.05 and pe_change > 0.05:
            return "double engine: EPS growth plus multiple expansion"
        if eps_change > 0.05 and pe_change <= 0.05:
            return "earnings-led rerating: price mostly follows EPS improvement"
        if eps_change <= 0.05 and pe_change > 0.05:
            return "multiple-led rerating: price relies more on valuation expansion"
        return "fragile rise: price up despite weak EPS and weak multiple support"
    if eps_change > 0.05 and pe_change < -0.05:
        return "derating despite EPS growth: market paid a lower multiple"
    if eps_change < -0.05 and pe_change < -0.05:
        return "double drag: EPS decline plus multiple contraction"
    if eps_change < -0.05 and pe_change >= -0.05:
        return "earnings-led drawdown: price mainly reflects EPS deterioration"
    return "valuation-led drawdown or mixed signal"


def _checkpoint_rows(history: pd.DataFrame, curr_date: str) -> list[dict]:
    if history.empty:
        return []
    latest = history.iloc[-1]
    latest_dt = latest["trade_dt"]
    anchors = [
        ("6M", latest_dt - relativedelta(months=6)),
        ("1Y", latest_dt - relativedelta(years=1)),
        ("3Y", latest_dt - relativedelta(years=3)),
        ("5Y", latest_dt - relativedelta(years=5)),
    ]

    rows: list[dict] = []
    for label, target_dt in anchors:
        anchor = _nearest_row_on_or_after(history, pd.Timestamp(target_dt))
        if anchor is None or anchor["trade_date"] == latest["trade_date"]:
            continue
        price_ratio = _safe_float(latest["close"]) / _safe_float(anchor["close"])
        eps_ratio = _safe_float(latest["eps_ttm_proxy"]) / _safe_float(anchor["eps_ttm_proxy"])
        pe_ratio = _safe_float(latest["pe_ttm"]) / _safe_float(anchor["pe_ttm"])
        price_change = price_ratio - 1
        eps_change = eps_ratio - 1
        pe_change = pe_ratio - 1
        rows.append(
            {
                "window": label,
                "anchor_date": _format_yyyymmdd(anchor["trade_date"]),
                "anchor_close": round(float(anchor["close"]), 3),
                "anchor_pe_ttm": round(float(anchor["pe_ttm"]), 2),
                "anchor_eps_proxy": round(float(anchor["eps_ttm_proxy"]), 3),
                "price_change": _safe_pct(price_change),
                "eps_proxy_change": _safe_pct(eps_change),
                "pe_change": _safe_pct(pe_change),
                "primary_read": _classify_driver(price_change, eps_change, pe_change),
            }
        )
    return rows


def _same_price_summary(
    history: pd.DataFrame,
    band: float = 0.05,
    min_age_days: int = 60,
) -> dict:
    if history.empty:
        return {}
    latest = history.iloc[-1]
    latest_close = float(latest["close"])
    latest_dt = latest["trade_dt"]
    older = history[history["trade_dt"] <= latest_dt - pd.Timedelta(days=min_age_days)]
    similar = older[
        (older["close"] >= latest_close * (1 - band))
        & (older["close"] <= latest_close * (1 + band))
    ]
    if similar.empty:
        return {
            "similar_price_days": 0,
            "interpretation": "No sufficiently old same-price observations in the look-back window.",
        }

    median_pe = float(similar["pe_ttm"].median())
    median_eps = float(similar["eps_ttm_proxy"].median())
    latest_pe = float(latest["pe_ttm"])
    latest_eps = float(latest["eps_ttm_proxy"])
    eps_gap = latest_eps / median_eps - 1 if median_eps else None
    pe_gap = latest_pe / median_pe - 1 if median_pe else None
    if eps_gap is not None and eps_gap > 0.1:
        read = "At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes."
    elif eps_gap is not None and eps_gap < -0.1:
        read = "At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes."
    elif pe_gap is not None and pe_gap > 0.1:
        read = "At similar historical prices, today's multiple is higher; check whether the business quality or cycle outlook justifies the premium."
    else:
        read = "At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence."
    return {
        "similar_price_days": int(len(similar)),
        "first_similar_date": _format_yyyymmdd(similar.iloc[0]["trade_date"]),
        "last_similar_date": _format_yyyymmdd(similar.iloc[-1]["trade_date"]),
        "median_pe_ttm_at_similar_price": round(median_pe, 2),
        "latest_pe_ttm": round(latest_pe, 2),
        "median_eps_proxy_at_similar_price": round(median_eps, 3),
        "latest_eps_proxy": round(latest_eps, 3),
        "latest_eps_vs_same_price_history": _safe_pct(eps_gap),
        "latest_pe_vs_same_price_history": _safe_pct(pe_gap),
        "interpretation": read,
    }


def _metric_percentile(history: pd.DataFrame, metric: str) -> float | None:
    if history.empty or metric not in history.columns:
        return None
    values = pd.to_numeric(history[metric], errors="coerce").dropna()
    if values.empty:
        return None
    latest = values.iloc[-1]
    return float((values <= latest).mean() * 100)


def _latest_snapshot_rows(history: pd.DataFrame) -> list[dict]:
    if history.empty:
        return []
    latest = history.iloc[-1]
    pe_percentile = _metric_percentile(history, "pe_ttm")
    eps_percentile = _metric_percentile(history, "eps_ttm_proxy")
    return [
        {"metric": "latest trade date", "value": _format_yyyymmdd(latest["trade_date"])},
        {"metric": "close", "value": round(float(latest["close"]), 3)},
        {"metric": "PE TTM", "value": round(float(latest["pe_ttm"]), 2)},
        {"metric": "EPS TTM proxy = close / PE TTM", "value": round(float(latest["eps_ttm_proxy"]), 3)},
        {"metric": "PE percentile in window", "value": _safe_pct(None if pe_percentile is None else pe_percentile / 100)},
        {
            "metric": "EPS proxy percentile in window",
            "value": _safe_pct(None if eps_percentile is None else eps_percentile / 100),
        },
    ]


def get_price_earnings_decomposition_context(
    ticker: str,
    curr_date: str,
    years: int = 5,
) -> str:
    """Explain whether historical price moves were driven by EPS or by PE multiple."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Price-EPS-PE decomposition expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    price_history = _fetch_price_history(symbol, curr_date, years=years)
    valuation_history = _fetch_valuation_history(symbol, curr_date, years=years)
    history = _build_price_eps_pe_history(price_history, valuation_history)
    if history.empty:
        return "\n".join(
            [
                f"# Historical price-EPS-PE decomposition for {symbol} as of {curr_date}",
                "",
                "- Retrieval status: no usable positive-PE price/valuation history returned.",
                "- Analyst instruction: do not infer whether the current price is EPS-driven or multiple-driven from this module.",
            ]
        )

    checkpoint_df = pd.DataFrame(_checkpoint_rows(history, curr_date))
    same_price = _same_price_summary(history)
    same_price_df = pd.DataFrame([same_price]) if same_price else pd.DataFrame()

    lines = [
        f"# Historical price-EPS-PE decomposition for {symbol} as of {curr_date}",
        "",
        f"- Company: {_format_value(None if basic is None else basic.get('name'))}",
        f"- Look-back window: {years} years",
        "- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.",
        "- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.",
        "",
        "## Latest Snapshot",
        _markdown_table(pd.DataFrame(_latest_snapshot_rows(history))),
        "",
        "## Price Move Decomposition",
        _markdown_table(checkpoint_df),
        "",
        "## Same-Price History Check",
        _markdown_table(same_price_df),
        "",
        "## Analyst Instructions",
        "- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.",
        "- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.",
        "- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.",
        "- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.",
        "- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.",
    ]
    return "\n".join(lines)
