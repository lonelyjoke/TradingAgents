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


def _print_frame(label: str, data) -> bool:
    rows = 0 if data is None else len(data)
    cols = list(getattr(data, "columns", []))
    print(f"{label}: OK rows={rows} cols={cols[:10]}")
    if rows:
        print(data.head(5).to_string(index=False))
    return rows > 0


def _run_check(label: str, func) -> bool:
    started = time.time()
    try:
        ok = _print_frame(label, func())
        print(f"{label}: elapsed={time.time() - started:.2f}s")
        return ok
    except Exception as exc:
        print(
            f"{label}: ERR {type(exc).__name__}: {str(exc)[:500]} "
            f"elapsed={time.time() - started:.2f}s"
        )
        return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test TradingAgents shared Tushare gateway configuration."
    )
    parser.add_argument("--ts-code", default="000001.SZ", help="A-share ts_code for pro_bar.")
    parser.add_argument("--limit", type=int, default=3, help="Rows to request per check.")
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
    if http_url != "https://tt.dailyfetch.top/":
        print("CONFIG WARNING: pro is not using https://tt.dailyfetch.top/")

    checks = [
        (
            "pro.index_basic",
            lambda: pro.index_basic(limit=args.limit),
        ),
        (
            "get_tushare_pro_bar",
            lambda: get_tushare_pro_bar(ts_code=args.ts_code, limit=args.limit),
        ),
    ]

    results = [_run_check(label, func) for label, func in checks]
    if all(results):
        print("SUMMARY: SUCCESS - new Tushare API returned rows for both checks.")
        return 0
    print("SUMMARY: FAILED - inspect ERR messages or zero-row checks above.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
