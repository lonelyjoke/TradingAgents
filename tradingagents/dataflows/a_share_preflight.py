from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

import pandas as pd

from .tushare_a_stock import (
    TushareDataError,
    _fetch_balance_sheet_data,
    _fetch_cashflow_data,
    _fetch_daily_basic_latest,
    _fetch_daily_with_backfill,
    _fetch_fina_indicator,
    _fetch_income_statement_data,
    _fetch_stock_basic,
    _format_yyyymmdd,
    is_a_share_symbol,
)
from .thematic_research import (
    _financial_report_text_audit_markdown,
    _load_financial_report_texts,
)


class AShareDataPreflightError(RuntimeError):
    """Raised before LLM generation when required A-share data is unavailable."""


@dataclass(frozen=True)
class PreflightCheck:
    name: str
    status: str
    detail: str


CURATED_STOCK_BASIC_FALLBACKS = {
    "601600.SH": {"name": "中国铝业", "industry": "铝"},
    "600547.SH": {"name": "山东黄金", "industry": "黄金"},
    "601318.SH": {"name": "中国平安", "industry": "保险"},
    "300760.SZ": {"name": "迈瑞医疗", "industry": "医疗器械"},
}


def _require(condition: bool, name: str, detail: str) -> PreflightCheck:
    return PreflightCheck(name, "ready" if condition else "failed", detail)


def _curated_stock_basic_check(symbol: str, reason: str) -> PreflightCheck | None:
    fallback = CURATED_STOCK_BASIC_FALLBACKS.get(symbol)
    if not fallback:
        return None
    return PreflightCheck(
        "stock_basic",
        "ready",
        f"{fallback['name']} / {fallback['industry']} (curated fallback; stock_basic unavailable: {reason})",
    )


def _check_stock_basic(symbol: str) -> PreflightCheck:
    try:
        basic = _fetch_stock_basic(symbol)
    except Exception as exc:
        fallback = _curated_stock_basic_check(symbol, str(exc))
        return fallback or PreflightCheck("stock_basic", "warning", str(exc))
    if basic is None:
        fallback = _curated_stock_basic_check(symbol, "no stock_basic row returned")
        return fallback or PreflightCheck("stock_basic", "warning", "no stock_basic row returned")
    name = basic.get("name") if hasattr(basic, "get") else ""
    industry = basic.get("industry") if hasattr(basic, "get") else ""
    return PreflightCheck("stock_basic", "ready", f"{name or symbol} / {industry or 'N/A'}")


def _parse_trade_date(value: object) -> datetime | None:
    text = _format_yyyymmdd(value)
    try:
        return datetime.strptime(text, "%Y-%m-%d")
    except ValueError:
        return None


def _staleness_ok(latest: datetime | None, curr_date: str, max_staleness_days: int) -> bool:
    if latest is None:
        return False
    current = datetime.strptime(curr_date, "%Y-%m-%d")
    return latest <= current and (current - latest).days <= max_staleness_days


def _check_daily(symbol: str, curr_date: str, max_staleness_days: int) -> PreflightCheck:
    end = datetime.strptime(curr_date, "%Y-%m-%d")
    lookback_days = max(45, max_staleness_days * 2)
    start = (end - timedelta(days=lookback_days)).strftime("%Y-%m-%d")
    try:
        data, notice = _fetch_daily_with_backfill(symbol, start, curr_date)
    except Exception as exc:
        return PreflightCheck("daily", "failed", str(exc))
    if data is None or data.empty or "Date" not in data.columns:
        return PreflightCheck("daily", "failed", "no daily OHLCV rows returned")
    latest = pd.to_datetime(data["Date"], errors="coerce").max()
    latest_dt = latest.to_pydatetime() if pd.notna(latest) else None
    if not _staleness_ok(latest_dt, curr_date, max_staleness_days):
        rendered = latest_dt.strftime("%Y-%m-%d") if latest_dt else "N/A"
        return PreflightCheck(
            "daily",
            "failed",
            f"latest daily row {rendered} is stale versus {curr_date}",
        )
    note = f"latest {latest_dt.strftime('%Y-%m-%d')}"
    if notice:
        note += f"; {notice}"
    return PreflightCheck("daily", "ready", note)


def _check_daily_basic(symbol: str, curr_date: str, max_staleness_days: int) -> PreflightCheck:
    try:
        row = _fetch_daily_basic_latest(symbol, curr_date)
    except Exception as exc:
        return PreflightCheck("daily_basic", "failed", str(exc))
    if row is None:
        return PreflightCheck("daily_basic", "failed", "no daily_basic valuation row returned")
    latest = _parse_trade_date(row.get("trade_date") if hasattr(row, "get") else None)
    if not _staleness_ok(latest, curr_date, max_staleness_days):
        rendered = latest.strftime("%Y-%m-%d") if latest else "N/A"
        return PreflightCheck(
            "daily_basic",
            "failed",
            f"latest daily_basic row {rendered} is stale versus {curr_date}",
        )
    return PreflightCheck("daily_basic", "ready", f"latest {latest.strftime('%Y-%m-%d')}")


def _check_frame(name: str, func, symbol: str, curr_date: str) -> PreflightCheck:
    try:
        data = func(symbol, curr_date)
    except Exception as exc:
        return PreflightCheck(name, "failed", str(exc))
    if isinstance(data, TushareDataError):
        return PreflightCheck(name, "failed", str(data))
    if data is None or data.empty:
        return PreflightCheck(name, "failed", "no rows returned")
    detail = f"{len(data)} rows"
    if "end_date" in data.columns:
        detail += f"; latest end_date {data['end_date'].astype(str).max()}"
    return PreflightCheck(name, "ready", detail)


def _check_filing_text(
    symbol: str,
    curr_date: str,
    *,
    look_back_days: int,
    min_total_chars: int,
) -> PreflightCheck:
    try:
        reports, texts = _load_financial_report_texts(
            symbol, curr_date, look_back_days=look_back_days
        )
    except Exception as exc:
        return PreflightCheck("filing_text", "failed", str(exc))

    if isinstance(reports, TushareDataError):
        audit = _financial_report_text_audit_markdown(symbol, curr_date, look_back_days)
        return PreflightCheck("filing_text", "failed", f"{reports}; {audit}")

    total_chars = sum(len(text or "") for _, text in texts)
    report_count = 0 if reports is None or reports.empty else len(reports)
    if not texts:
        audit = _financial_report_text_audit_markdown(symbol, curr_date, look_back_days)
        return PreflightCheck(
            "filing_text",
            "failed",
            (
                f"no readable annual/semiannual/quarterly report text returned; "
                f"candidate reports={report_count}; {audit}"
            ),
        )
    if total_chars < min_total_chars:
        audit = _financial_report_text_audit_markdown(symbol, curr_date, look_back_days)
        return PreflightCheck(
            "filing_text",
            "failed",
            (
                f"readable report text too thin: {total_chars} chars "
                f"< required {min_total_chars}; reports={report_count}; {audit}"
            ),
        )
    titles = ", ".join(title for title, _ in texts[:3])
    return PreflightCheck(
        "filing_text",
        "ready",
        (
            f"{len(texts)} readable report text(s), {total_chars} chars; "
            f"reports={report_count}; warmed cache for filing intelligence; {titles}"
        ),
    )


def _render_checks(symbol: str, curr_date: str, checks: list[PreflightCheck]) -> str:
    lines = [
        f"# A-share Data Preflight for {symbol} as of {curr_date}",
        "",
        "| check | status | detail |",
        "| --- | --- | --- |",
    ]
    for check in checks:
        detail = check.detail.replace("\n", " ").replace("|", "\\|")
        lines.append(f"| {check.name} | {check.status} | {detail} |")
    return "\n".join(lines)


def run_a_share_data_preflight(
    ticker: str,
    curr_date: str,
    *,
    selected_analysts: list[str] | tuple[str, ...] | None = None,
    max_staleness_days: int = 21,
    require_filing_text: bool = True,
    filing_text_look_back_days: int = 900,
    min_filing_text_chars: int = 500,
) -> str:
    """Verify core A-share data before spending LLM tokens."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# A-share Data Preflight\n\n- Status: skipped\n- Reason: {ticker!r} is not an A-share symbol."

    selected = {str(item).lower() for item in (selected_analysts or [])}
    checks = [_check_stock_basic(symbol)]
    if not selected or "market" in selected:
        checks.append(_check_daily(symbol, curr_date, max_staleness_days))
    if not selected or "fundamentals" in selected:
        checks.extend(
            [
                _check_daily_basic(symbol, curr_date, max_staleness_days),
                _check_frame("fina_indicator", _fetch_fina_indicator, symbol, curr_date),
                _check_frame("income", _fetch_income_statement_data, symbol, curr_date),
                _check_frame("balancesheet", _fetch_balance_sheet_data, symbol, curr_date),
                _check_frame("cashflow", _fetch_cashflow_data, symbol, curr_date),
            ]
        )
    if require_filing_text:
        checks.append(
            _check_filing_text(
                symbol,
                curr_date,
                look_back_days=filing_text_look_back_days,
                min_total_chars=min_filing_text_chars,
            )
        )

    failed = [check for check in checks if check.status == "failed"]
    rendered = _render_checks(symbol, curr_date, checks)
    if failed:
        failed_names = ", ".join(check.name for check in failed)
        raise AShareDataPreflightError(
            f"A-share data preflight failed for {symbol}: {failed_names}\n\n{rendered}"
        )
    return rendered
