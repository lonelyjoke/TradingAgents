from __future__ import annotations

import os
from pathlib import Path
import hashlib
import sys
import time


def _fingerprint(value: str) -> str:
    if not value:
        return "<empty>"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def _load_env() -> tuple[str, dict[str, str]]:
    dotenv_path = ""
    dotenv_values: dict[str, str] = {}
    try:
        from dotenv import dotenv_values as read_dotenv_values
        from dotenv import find_dotenv, load_dotenv

        dotenv_path = find_dotenv(usecwd=True)
        if dotenv_path:
            dotenv_values = {
                key: str(value or "")
                for key, value in read_dotenv_values(dotenv_path).items()
                if key
            }
        load_dotenv(dotenv_path or None, override=True)
    except ImportError:
        dotenv_path = "<python-dotenv not installed>"
    return dotenv_path, dotenv_values


def _print_result(label: str, func) -> None:
    started = time.time()
    try:
        data = func()
        rows = 0 if data is None else len(data)
        cols = list(getattr(data, "columns", []))
        print(f"{label}: OK rows={rows} cols={cols[:8]} elapsed={time.time() - started:.2f}s")
        if rows:
            print(data.head(2).to_string(index=False))
    except Exception as exc:
        print(f"{label}: ERR {type(exc).__name__}: {str(exc)[:280]} elapsed={time.time() - started:.2f}s")


def main() -> None:
    raw_process_token = os.getenv("TUSHARE_TOKEN") or ""
    dotenv_path, dotenv_values = _load_env()
    token = os.getenv("TUSHARE_TOKEN") or ""
    http_url = os.getenv("TUSHARE_HTTP_URL") or ""
    disable_official_fallback = (os.getenv("TUSHARE_DISABLE_OFFICIAL_FALLBACK") or "").lower() in {
        "1",
        "true",
        "yes",
    }
    dotenv_token = dotenv_values.get("TUSHARE_TOKEN", "")
    dotenv_http_url = dotenv_values.get("TUSHARE_HTTP_URL", "")
    print(f"python: {sys.executable}")
    print(f"cwd: {Path.cwd()}")
    print(f"dotenv: {dotenv_path or '<not found>'}")
    print(
        "process TUSHARE_TOKEN before .env load: "
        f"{'set' if raw_process_token else 'missing'} "
        f"length={len(raw_process_token)} fp={_fingerprint(raw_process_token)}"
    )
    print(
        "project .env TUSHARE_TOKEN: "
        f"{'set' if dotenv_token else 'missing'} "
        f"length={len(dotenv_token)} fp={_fingerprint(dotenv_token)}"
    )
    print(f"TUSHARE_TOKEN: {'set' if token else 'missing'} length={len(token)}")
    print(f"TUSHARE_TOKEN fingerprint after load: {_fingerprint(token)}")
    if dotenv_token:
        print(f"TUSHARE_TOKEN matches project .env: {token == dotenv_token}")
    print(f"TUSHARE_HTTP_URL after load: {http_url or '<unset>'}")
    print(f"TUSHARE_DISABLE_OFFICIAL_FALLBACK: {disable_official_fallback}")
    if dotenv_http_url:
        print(f"project .env TUSHARE_HTTP_URL: {dotenv_http_url}")

    try:
        import tushare as ts
    except Exception as exc:
        print(f"tushare import failed: {type(exc).__name__}: {exc}")
        return

    print(f"tushare: {getattr(ts, '__version__', '<unknown>')} {getattr(ts, '__file__', '<unknown>')}")
    if not token:
        return

    clients = []
    if http_url:
        configured = ts.pro_api(token)
        configured._DataApi__http_url = http_url.rstrip("/") + "/"
        clients.append(("configured_http_url", configured))
    if not disable_official_fallback:
        clients.append(("official", ts.pro_api(token)))
    elif not http_url:
        print("official client skipped, but no TUSHARE_HTTP_URL is configured.")
    else:
        print("official client skipped because TUSHARE_DISABLE_OFFICIAL_FALLBACK=true")

    for name, pro in clients:
        print(f"\nCLIENT {name}")
        client_results: list[tuple[str, str, int]] = []

        def check(label: str, func) -> None:
            started = time.time()
            try:
                data = func()
                rows = 0 if data is None else len(data)
                cols = list(getattr(data, "columns", []))
                client_results.append((label, "ok", rows))
                print(
                    f"{label}: OK rows={rows} cols={cols[:8]} "
                    f"elapsed={time.time() - started:.2f}s"
                )
                if rows:
                    print(data.head(2).to_string(index=False))
            except Exception as exc:
                client_results.append((label, "err", 0))
                print(
                    f"{label}: ERR {type(exc).__name__}: {str(exc)[:280]} "
                    f"elapsed={time.time() - started:.2f}s"
                )

        check(
            "stock_basic_one",
            lambda pro=pro: pro.stock_basic(
                ts_code="600519.SH",
                fields="ts_code,symbol,name,industry,list_date",
            ),
        )
        check(
            "stock_basic_universe",
            lambda pro=pro: pro.stock_basic(
                list_status="L",
                fields="ts_code,symbol,name,industry,list_date",
            ),
        )
        check(
            "daily_basic",
            lambda pro=pro: pro.daily_basic(
                ts_code="600519.SH",
                start_date="20260501",
                end_date="20260527",
                fields="ts_code,trade_date,close,pe_ttm,pb,dv_ttm,total_mv",
            ),
        )
        check(
            "daily",
            lambda pro=pro: pro.daily(
                ts_code="600519.SH",
                start_date="20260501",
                end_date="20260527",
            ),
        )
        if client_results and all(status == "ok" and rows == 0 for _, status, rows in client_results):
            print(
                "SUMMARY: reachable but returned zero rows for every checked endpoint; "
                "treat this client as unavailable for A-share market/valuation/peer data."
            )
        elif any(status == "err" for _, status, _ in client_results):
            print(
                "SUMMARY: at least one checked endpoint errored; inspect the message above "
                "for token, permission, proxy, or gateway issues."
            )


if __name__ == "__main__":
    main()
