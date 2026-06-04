from __future__ import annotations

import argparse
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


DEFAULT_ENDPOINTS = (
    "stock_basic_symbol",
    "stock_basic_universe",
    "daily",
    "daily_basic",
    "fina_indicator",
    "income",
    "balancesheet",
    "cashflow",
)


def load_env_file(path: Path, *, override: bool = True) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if override or key not in os.environ:
            os.environ[key] = value.strip().strip('"').strip("'")


def tushare_date(value: str) -> str:
    value = value.strip()
    if len(value) == 8 and value.isdigit():
        return value
    return datetime.strptime(value, "%Y-%m-%d").strftime("%Y%m%d")


def gateway_client(token: str, gateway: str | None):
    try:
        import tushare as ts
    except ImportError as exc:
        raise RuntimeError(
            "tushare is not installed in this Python environment. "
            "Use the quant env or install tushare."
        ) from exc

    pro = ts.pro_api(token)
    if gateway:
        pro._DataApi__http_url = gateway.rstrip("/") + "/"
    return pro


def call_tushare(pro: Any, api_name: str, **kwargs):
    func = getattr(pro, api_name, None)
    if callable(func):
        return func(**kwargs)
    return pro.query(api_name, **kwargs)


def endpoint_params(name: str, symbol: str, curr_date: str) -> tuple[str, dict[str, Any]]:
    end = tushare_date(curr_date)
    start = (datetime.strptime(end, "%Y%m%d") - timedelta(days=900)).strftime("%Y%m%d")
    short_start = (datetime.strptime(end, "%Y%m%d") - timedelta(days=30)).strftime("%Y%m%d")
    if name == "stock_basic_symbol":
        return (
            "stock_basic",
            {
                "ts_code": symbol,
                "fields": "ts_code,symbol,name,area,industry,market,exchange,list_date",
            },
        )
    if name == "stock_basic_universe":
        return (
            "stock_basic",
            {
                "list_status": "L",
                "fields": "ts_code,symbol,name,area,industry,market,exchange,list_date",
            },
        )
    if name == "daily":
        return ("daily", {"ts_code": symbol, "start_date": short_start, "end_date": end})
    if name == "daily_basic":
        return (
            "daily_basic",
            {
                "ts_code": symbol,
                "start_date": short_start,
                "end_date": end,
                "fields": "ts_code,trade_date,close,pe_ttm,pb,total_mv,circ_mv",
            },
        )
    if name in {"fina_indicator", "income", "balancesheet", "cashflow"}:
        return (name, {"ts_code": symbol, "start_date": start, "end_date": end})
    raise ValueError(f"Unknown endpoint check: {name}")


def run_check(pro: Any, name: str, symbol: str, curr_date: str) -> dict[str, str]:
    api_name, params = endpoint_params(name, symbol, curr_date)
    try:
        data = call_tushare(pro, api_name, **params)
    except Exception as exc:
        return {"check": name, "api": api_name, "status": "ERROR", "detail": str(exc)}

    rows = len(data) if data is not None and hasattr(data, "__len__") else 0
    cols = list(getattr(data, "columns", [])[:8]) if data is not None else []
    if rows == 0:
        return {"check": name, "api": api_name, "status": "EMPTY", "detail": "0 rows"}
    return {
        "check": name,
        "api": api_name,
        "status": "OK",
        "detail": f"{rows} rows; columns={cols}",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a Tushare-compatible gateway.")
    parser.add_argument("--gateway", default=None, help="Gateway URL, e.g. http://a.sszhixia.cn/")
    parser.add_argument("--symbol", default="601318.SH", help="A-share ts_code to test")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="Current date yyyy-mm-dd")
    parser.add_argument(
        "--endpoints",
        nargs="*",
        default=list(DEFAULT_ENDPOINTS),
        choices=list(DEFAULT_ENDPOINTS),
        help="Endpoint checks to run",
    )
    parser.add_argument(
        "--env",
        default=".env",
        help="Env file containing TUSHARE_TOKEN and optional TUSHARE_HTTP_URL",
    )
    parser.add_argument(
        "--use-shell-env",
        action="store_true",
        help="Do not let --env override already-set shell environment variables.",
    )
    args = parser.parse_args()

    load_env_file(Path(args.env), override=not args.use_shell_env)
    token = os.getenv("TUSHARE_TOKEN", "").strip()
    gateway = args.gateway or os.getenv("TUSHARE_HTTP_URL", "").strip() or None

    print(f"TUSHARE_TOKEN: {'set' if token else 'missing'} length={len(token)}")
    print(f"Gateway under test: {gateway or 'official Tushare endpoint'}")
    print(f"Symbol/date: {args.symbol.upper()} / {args.date}")
    print("")

    if not token:
        print("ERROR: TUSHARE_TOKEN is missing. Set it in .env or environment.")
        return 2

    pro = gateway_client(token, gateway)
    results = [run_check(pro, name, args.symbol.upper(), args.date) for name in args.endpoints]
    by_name = {row["check"]: row for row in results}
    symbol_basic = by_name.get("stock_basic_symbol")
    universe_basic = by_name.get("stock_basic_universe")
    if (
        symbol_basic
        and universe_basic
        and symbol_basic["status"] == "EMPTY"
        and universe_basic["status"] == "OK"
    ):
        symbol_basic["status"] = "WARN"
        symbol_basic["detail"] = (
            "0 rows for ts_code filter, but stock_basic universe returned rows; "
            "the main system can fall back to universe lookup."
        )

    width = max(len(row["check"]) for row in results + [{"check": "check"}])
    print(f"{'check'.ljust(width)}  status  api             detail")
    print(f"{'-' * width}  ------  --------------  ------")
    for row in results:
        print(
            f"{row['check'].ljust(width)}  "
            f"{row['status'].ljust(6)}  "
            f"{row['api'].ljust(14)}  "
            f"{row['detail']}"
        )

    failed = [row for row in results if row["status"] not in {"OK", "WARN"}]
    warned = [row for row in results if row["status"] == "WARN"]
    if failed:
        print("")
        print("Result: FAILED. Send this table to the gateway provider/customer service.")
        return 1
    if warned:
        print("")
        print("Result: OK_WITH_WARNINGS. Required data is available, but some direct filters are unsupported.")
        return 0
    print("")
    print("Result: OK. The tested gateway returned rows for all required endpoints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
