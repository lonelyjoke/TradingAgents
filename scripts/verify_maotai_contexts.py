"""Verify Maotai-specific research contexts under the current Tushare gateway.

This script is intentionally narrow: it does not run the full multi-agent
research workflow. It validates the data contexts that caused the latest
600519.SH report to be evidence-limited.
"""

from __future__ import annotations

import hashlib
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv


def _fingerprint(value: str | None) -> str:
    if not value:
        return "unset"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def _status(text: str) -> str:
    lowered = text.lower()
    failure_markers = [
        "unavailable",
        "no daily_basic valuation snapshot",
        "no data returned",
        "failed",
        "error",
        "traceback",
    ]
    if any(marker in lowered for marker in failure_markers):
        return "CHECK"
    return "OK"


def _preview(title: str, text: str, max_chars: int = 1200) -> None:
    print(f"\n## {title}")
    print(f"status={_status(text)} length={len(text)}")
    print(text[:max_chars].rstrip())
    if len(text) > max_chars:
        print("... <truncated>")


def _fetch_daily_basic_latest_with_retry(fetch_func, symbol: str, curr_date: str, attempts: int = 3):
    last = None
    for attempt in range(attempts):
        latest = fetch_func(symbol, curr_date)
        if latest is not None:
            return latest
        last = latest
        if attempt < attempts - 1:
            time.sleep(0.5)
    return last


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(project_root))
    env_path = project_root / ".env"
    load_dotenv(env_path, override=True)

    token = os.getenv("TUSHARE_TOKEN")
    print(f"cwd: {project_root}")
    print(f"dotenv: {env_path}")
    print(
        "TUSHARE_TOKEN: "
        f"{'set' if token else 'unset'} length={len(token) if token else 0} "
        f"fp={_fingerprint(token)}"
    )
    print(f"TUSHARE_HTTP_URL: {os.getenv('TUSHARE_HTTP_URL')}")
    print(
        "TUSHARE_DISABLE_OFFICIAL_FALLBACK: "
        f"{os.getenv('TUSHARE_DISABLE_OFFICIAL_FALLBACK')}"
    )

    from tradingagents.dataflows.baijiu_research import get_baijiu_context
    from tradingagents.dataflows.dividend_defensive_research import (
        get_dividend_defensive_context,
    )
    from tradingagents.dataflows.tushare_a_stock import _fetch_daily_basic_latest
    from tradingagents.dataflows.tushare_research import get_peer_comparison

    symbol = "600519.SH"
    curr_date = "2026-05-27"

    print("\n## daily_basic latest")
    try:
        latest = _fetch_daily_basic_latest_with_retry(
            _fetch_daily_basic_latest,
            symbol,
            curr_date,
        )
        if latest is None:
            print("status=CHECK latest=None")
        else:
            fields = [
                "ts_code",
                "trade_date",
                "close",
                "pe_ttm",
                "pb",
                "dv_ttm",
                "total_mv",
            ]
            print("status=OK")
            print(latest[[field for field in fields if field in latest.index]].to_string())
    except Exception as exc:
        print(f"status=CHECK error={type(exc).__name__}: {exc}")

    checks = [
        ("peer_comparison", lambda: get_peer_comparison(symbol, curr_date)),
        ("baijiu_context", lambda: get_baijiu_context(symbol, curr_date)),
        (
            "dividend_defensive_context",
            lambda: get_dividend_defensive_context(symbol, curr_date),
        ),
    ]
    for title, func in checks:
        try:
            _preview(title, func(), max_chars=2000)
        except Exception as exc:
            print(f"\n## {title}")
            print(f"status=CHECK error={type(exc).__name__}: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
