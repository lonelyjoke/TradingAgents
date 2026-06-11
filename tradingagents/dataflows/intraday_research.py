"""A-share historical minute-line behavior context."""

from __future__ import annotations

from datetime import datetime, timedelta

import pandas as pd

from .tushare_a_stock import TushareDataError, is_a_share_symbol, resolve_a_share_symbol
from .tushare_client import TushareClientError, get_tushare_pro_bar


def _markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join("" if item is None else str(item) for item in row) + " |")
    return "\n".join(lines)


def _fmt_pct(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{value:+.2f}%"


def _fmt_num(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{value:,.2f}"


def _pct(current: float | None, base: float | None) -> float | None:
    if current is None or base in (None, 0) or pd.isna(current) or pd.isna(base):
        return None
    return (float(current) / float(base) - 1.0) * 100.0


def _fetch_intraday_bars(
    ts_code: str,
    curr_date: str,
    look_back_days: int,
    freq: str = "1min",
) -> pd.DataFrame:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - timedelta(days=max(look_back_days, 1))
    return get_tushare_pro_bar(
        ts_code=ts_code,
        freq=freq,
        asset="E",
        start_date=start_dt.strftime("%Y-%m-%d 09:30:00"),
        end_date=end_dt.strftime("%Y-%m-%d 15:30:00"),
    )


def _normalize_bars(raw: pd.DataFrame) -> pd.DataFrame:
    if raw is None or raw.empty:
        return pd.DataFrame()
    frame = raw.copy()
    frame.columns = [str(col).lower() for col in frame.columns]

    time_col = next(
        (
            col
            for col in [
                "trade_time",
                "datetime",
                "trade_date",
                "date",
                "time",
            ]
            if col in frame.columns
        ),
        None,
    )
    if time_col is not None:
        frame["dt"] = pd.to_datetime(frame[time_col], errors="coerce")
    else:
        frame["dt"] = pd.to_datetime(frame.index, errors="coerce")

    for col in ["open", "high", "low", "close", "vol", "volume", "amount"]:
        if col in frame.columns:
            frame[col] = pd.to_numeric(frame[col], errors="coerce")
    if "vol" not in frame.columns and "volume" in frame.columns:
        frame["vol"] = frame["volume"]
    if "vol" not in frame.columns:
        frame["vol"] = 0.0

    required = {"dt", "open", "high", "low", "close"}
    if not required.issubset(frame.columns):
        return pd.DataFrame()
    frame = frame.dropna(subset=["dt", "open", "high", "low", "close"])
    if frame.empty:
        return frame
    frame["trade_day"] = frame["dt"].dt.strftime("%Y-%m-%d")
    return frame.sort_values("dt")


def _day_metrics(day: pd.DataFrame) -> dict[str, object]:
    first_open = float(day["open"].iloc[0])
    first_close = float(day["close"].iloc[0])
    last_close = float(day["close"].iloc[-1])
    high = float(day["high"].max())
    low = float(day["low"].min())
    total_vol = float(day["vol"].sum()) if "vol" in day.columns else 0.0
    first_30 = day.head(30)
    last_30 = day.tail(30)
    first_30_vol = float(first_30["vol"].sum()) if "vol" in day.columns else 0.0
    last_30_vol = float(last_30["vol"].sum()) if "vol" in day.columns else 0.0
    minute_returns = day["close"].pct_change() * 100.0
    largest_swing = minute_returns.abs().max()
    return {
        "bars": len(day),
        "open": first_open,
        "close": last_close,
        "intraday_return": _pct(last_close, first_open),
        "high_low_range": _pct(high, low),
        "drawdown_from_high": _pct(last_close, high),
        "rebound_from_low": _pct(last_close, low),
        "first_30min_return": _pct(float(first_30["close"].iloc[-1]), first_open)
        if not first_30.empty
        else None,
        "last_30min_return": _pct(last_close, float(last_30["open"].iloc[0]))
        if not last_30.empty
        else None,
        "first_30min_volume_share": (first_30_vol / total_vol * 100.0)
        if total_vol
        else None,
        "last_30min_volume_share": (last_30_vol / total_vol * 100.0)
        if total_vol
        else None,
        "largest_minute_close_move": float(largest_swing)
        if not pd.isna(largest_swing)
        else None,
        "volume": total_vol,
        "first_close": first_close,
    }


def get_intraday_behavior_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 10,
    freq: str = "1min",
) -> str:
    """Return minute-line behavior context for A-share PM validation."""
    try:
        ts_code = resolve_a_share_symbol(ticker)
    except TushareDataError as exc:
        return f"## Intraday Minute-Line Behavior Context\nStatus: failed\nReason: {exc}"
    if not is_a_share_symbol(ts_code):
        return (
            "## Intraday Minute-Line Behavior Context\n"
            "Status: not_applicable\n"
            "Reason: minute-line Tushare context is only enabled for A-share symbols."
        )

    try:
        raw = _fetch_intraday_bars(ts_code, curr_date, look_back_days, freq=freq)
    except (TushareClientError, TushareDataError, Exception) as exc:
        return (
            "## Intraday Minute-Line Behavior Context\n"
            "Status: failed\n"
            f"Reason: {exc}"
        )

    bars = _normalize_bars(raw)
    if bars.empty:
        return (
            "## Intraday Minute-Line Behavior Context\n"
            "Status: partial\n"
            f"Reason: no usable {freq} bars were returned for {ts_code} near {curr_date}."
        )

    target_dt = datetime.strptime(curr_date, "%Y-%m-%d").date()
    days = [
        day
        for day in sorted(bars["trade_day"].unique())
        if datetime.strptime(day, "%Y-%m-%d").date() <= target_dt
    ]
    if not days:
        return (
            "## Intraday Minute-Line Behavior Context\n"
            "Status: partial\n"
            f"Reason: bars are present but none are on or before {curr_date}."
        )
    latest_day = days[-1]
    day = bars[bars["trade_day"] == latest_day]
    metrics = _day_metrics(day)

    rows = [
        ["Trade day", latest_day],
        ["Minute bars", metrics["bars"]],
        ["Open / Close", f"{_fmt_num(metrics['open'])} / {_fmt_num(metrics['close'])}"],
        ["Intraday return", _fmt_pct(metrics["intraday_return"])],
        ["High-low range", _fmt_pct(metrics["high_low_range"])],
        ["Close vs high / low", f"{_fmt_pct(metrics['drawdown_from_high'])} / {_fmt_pct(metrics['rebound_from_low'])}"],
        ["First 30min return", _fmt_pct(metrics["first_30min_return"])],
        ["Last 30min return", _fmt_pct(metrics["last_30min_return"])],
        ["First / last 30min volume share", f"{_fmt_pct(metrics['first_30min_volume_share'])} / {_fmt_pct(metrics['last_30min_volume_share'])}"],
        ["Largest minute close move", _fmt_pct(metrics["largest_minute_close_move"])],
    ]
    interpretation = []
    if metrics["drawdown_from_high"] is not None and metrics["drawdown_from_high"] < -3:
        interpretation.append("intraday close materially below the high, signaling possible profit-taking or failed breakout")
    if metrics["last_30min_return"] is not None and metrics["last_30min_return"] > 1:
        interpretation.append("late-session confirmation was positive")
    if metrics["last_30min_return"] is not None and metrics["last_30min_return"] < -1:
        interpretation.append("late-session pressure was negative")
    if metrics["first_30min_volume_share"] is not None and metrics["first_30min_volume_share"] > 35:
        interpretation.append("volume was concentrated in the opening phase, so opening noise may dominate the day")
    if not interpretation:
        interpretation.append("no single intraday pattern should dominate the fundamental thesis")

    return "\n\n".join(
        [
            "## Intraday Minute-Line Behavior Context",
            "Status: ready",
            f"Symbol: {ts_code}",
            _markdown_table(["Metric", "Value"], rows),
            "**PM usage rule:** Treat minute K-line evidence as market-behavior validation for timing, liquidity, and sizing. Do not use it as a substitute for company research, segment economics, earnings forecasts, or valuation work.",
            "**Behavior read-through:** " + "; ".join(interpretation) + ".",
        ]
    )
