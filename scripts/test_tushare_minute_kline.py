from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys
import time


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _fingerprint(value: str) -> str:
    if not value:
        return "<empty>"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test minute-level A-share K-line data through TradingAgents Tushare gateway."
    )
    parser.add_argument("--ts-code", default="000001.SZ", help="A-share ts_code.")
    parser.add_argument(
        "--freq",
        default="1min",
        choices=["1min", "5min", "15min", "30min", "60min"],
        help="Minute K-line frequency.",
    )
    parser.add_argument(
        "--start-date",
        default="2024-01-02 09:30:00",
        help="Start datetime, e.g. 2024-01-02 09:30:00.",
    )
    parser.add_argument(
        "--end-date",
        default="2024-01-02 10:30:00",
        help="End datetime, e.g. 2024-01-02 10:30:00.",
    )
    parser.add_argument("--limit", type=int, default=20, help="Rows to print.")
    args = parser.parse_args()

    from tradingagents.dataflows.tushare_client import (
        get_tushare_pro_bar,
        get_tushare_pro_client,
        get_tushare_token,
    )

    print(f"repo: {REPO_ROOT}")
    print(f"python: {sys.executable}")

    try:
        token = get_tushare_token()
        pro = get_tushare_pro_client()
    except Exception as exc:
        print(f"INIT: ERR {type(exc).__name__}: {exc}")
        return 1

    http_url = getattr(pro, "_DataApi__http_url", "<missing>")
    print(f"TUSHARE_TOKEN: set length={len(token)} fp={_fingerprint(token)}")
    print(f"TUSHARE_HTTP_URL used by pro: {http_url}")

    started = time.time()
    try:
        df = get_tushare_pro_bar(
            ts_code=args.ts_code,
            freq=args.freq,
            start_date=args.start_date,
            end_date=args.end_date,
        )
    except Exception as exc:
        print(
            f"MINUTE_KLINE: ERR {type(exc).__name__}: {str(exc)[:800]} "
            f"elapsed={time.time() - started:.2f}s"
        )
        return 2

    rows = 0 if df is None else len(df)
    cols = list(getattr(df, "columns", []))
    print(
        f"MINUTE_KLINE: OK rows={rows} cols={cols} "
        f"elapsed={time.time() - started:.2f}s"
    )
    if rows:
        print(df.head(args.limit).to_string(index=False))
        print("SUMMARY: SUCCESS - minute-level K-line data returned rows.")
        return 0

    print(
        "SUMMARY: ZERO ROWS - the gateway responded, but this symbol/date/frequency "
        "returned no minute data. Try another trading day or frequency."
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
