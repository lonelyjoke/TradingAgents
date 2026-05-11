from __future__ import annotations

from datetime import datetime, timedelta
from urllib.parse import urlparse

import pandas as pd
import requests
from parsel import Selector

from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)
from .tushare_research import _date_window, _query_optional_api


ALLOWED_DOMAINS = {
    "www.baiinfo.com",
    "baiinfo.com",
    "www.100ppi.com",
    "100ppi.com",
}


EXCHANGE_ALIASES = {
    "SHFE": ["SHFE", "SHF", ""],
    "SHF": ["SHF", "SHFE", ""],
    "DCE": ["DCE", ""],
    "CZCE": ["CZCE", "CZC", ""],
    "CZC": ["CZC", "CZCE", ""],
    "CFFEX": ["CFFEX", "CFE", ""],
    "CFE": ["CFE", "CFFEX", ""],
    "GFEX": ["GFEX", "GFE", ""],
    "GFE": ["GFE", "GFEX", ""],
    "INE": ["INE", ""],
}


COMPANY_COMMODITY_MAP = {
    "600160.SH": {
        "name": "Juhua Group",
        "products": [
            {
                "name": "R32",
                "type": "web_spot",
                "role": "main product",
                "urls": ["https://www.baiinfo.com/fuhuagong/r32"],
            },
            {
                "name": "R125",
                "type": "web_spot",
                "role": "main product",
                "urls": ["https://www.baiinfo.com/fuhuagong/r125"],
            },
            {
                "name": "R134a",
                "type": "web_spot",
                "role": "main product",
                "urls": ["https://www.baiinfo.com/fuhuagong/r134a"],
            },
            {
                "name": "PVDF",
                "type": "web_spot",
                "role": "secondary product",
                "urls": ["https://www.baiinfo.com/fuhuagong/pvdf"],
            },
            {
                "name": "Fluorite",
                "type": "web_spot",
                "role": "raw material proxy",
                "urls": ["https://www.baiinfo.com/fuhuagong/fluorite"],
            },
            {
                "name": "Hydrofluoric acid",
                "type": "web_spot",
                "role": "raw material proxy",
                "urls": ["https://www.baiinfo.com/fuhuagong/hydrofluoric-acid"],
            },
        ],
        "spread_note": "Watch refrigerant selling prices against fluorite and hydrofluoric acid cost proxies.",
    },
    "601899.SH": {
        "name": "Zijin Mining",
        "products": [
            {"name": "Copper", "type": "futures", "role": "main product", "prefix": "CU", "exchange": "SHFE"},
            {"name": "Gold", "type": "futures", "role": "main product", "prefix": "AU", "exchange": "SHFE"},
        ],
        "spread_note": "Use metal futures as price proxies; mine cost curves still require external research.",
    },
    "002460.SZ": {
        "name": "Ganfeng Lithium",
        "products": [
            {"name": "Lithium carbonate", "type": "futures", "role": "main product", "prefix": "LC", "exchange": "GFEX"},
        ],
        "spread_note": "Lithium carbonate futures proxy product price; lithium concentrate costs require external data.",
    },
    "300750.SZ": {
        "name": "CATL",
        "products": [
            {"name": "Lithium carbonate", "type": "futures", "role": "raw material proxy", "prefix": "LC", "exchange": "GFEX"},
        ],
        "spread_note": "For battery makers, lithium carbonate is a cost proxy rather than a direct revenue product.",
    },
}


INDUSTRY_PRODUCT_HINTS = {
    "铜": [{"name": "Copper", "type": "futures", "role": "industry proxy", "prefix": "CU", "exchange": "SHFE"}],
    "黄金": [{"name": "Gold", "type": "futures", "role": "industry proxy", "prefix": "AU", "exchange": "SHFE"}],
    "锂": [{"name": "Lithium carbonate", "type": "futures", "role": "industry proxy", "prefix": "LC", "exchange": "GFEX"}],
    "煤": [{"name": "Coking coal", "type": "futures", "role": "industry proxy", "prefix": "JM", "exchange": "DCE"}],
    "钢": [{"name": "Rebar", "type": "futures", "role": "industry proxy", "prefix": "RB", "exchange": "SHFE"}],
    "铝": [{"name": "Aluminum", "type": "futures", "role": "industry proxy", "prefix": "AL", "exchange": "SHFE"}],
}


def _is_allowed_url(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host in ALLOWED_DOMAINS


def _clean_text(text: str) -> str:
    return " ".join(str(text or "").split())


def _fetch_whitelisted_page(url: str) -> tuple[str, str]:
    if not _is_allowed_url(url):
        raise TushareDataError(f"URL is not in the commodity whitelist: {url}")
    response = requests.get(
        url,
        timeout=12,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
            )
        },
    )
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    selector = Selector(text=response.text)
    title = _clean_text(selector.xpath("//title/text()").get(""))
    body = _clean_text(" ".join(selector.xpath("//body//text()").getall()))
    return title, body


def _extract_evidence_snippets(product: str, title: str, body: str, max_snippets: int = 4) -> list[str]:
    keywords = [product.lower(), "价格", "报价", "参考价", "市场价", "出厂", "元/吨", "涨跌"]
    pieces = []
    window = 120
    lower_body = body.lower()
    for keyword in keywords:
        start = 0
        needle = keyword.lower()
        while True:
            idx = lower_body.find(needle, start)
            if idx == -1:
                break
            snippet = body[max(0, idx - window) : min(len(body), idx + window)]
            snippet = _clean_text(snippet)
            if snippet and snippet not in pieces:
                pieces.append(snippet)
            start = idx + len(needle)
            if len(pieces) >= max_snippets:
                return pieces
    if title:
        pieces.append(title)
    return pieces[:max_snippets]


def _fetch_web_spot(product: dict) -> dict:
    name = product["name"]
    errors = []
    for url in product.get("urls", []):
        try:
            title, body = _fetch_whitelisted_page(url)
            snippets = _extract_evidence_snippets(name, title, body)
            return {
                "product": name,
                "role": product.get("role", ""),
                "data_type": "web spot evidence",
                "latest_contract_or_source": url,
                "latest_price": "Not parsed",
                "latest_date": "See source",
                "change_over_window": "Not computed",
                "inventory_or_receipt": "N/A",
                "evidence_status": "Fetched whitelist page; verify exact price from snippets/source.",
                "evidence": " | ".join(snippets)[:800] if snippets else title,
            }
        except Exception as exc:
            errors.append(f"{url}: {exc}")
    return {
        "product": name,
        "role": product.get("role", ""),
        "data_type": "web spot evidence",
        "latest_contract_or_source": ", ".join(product.get("urls", [])),
        "latest_price": "N/A",
        "latest_date": "N/A",
        "change_over_window": "N/A",
        "inventory_or_receipt": "N/A",
        "evidence_status": "Unavailable; do not state price or change as fact.",
        "evidence": "; ".join(errors)[:800],
    }


def _latest_futures_trade_date(curr_date: str, exchange: str) -> pd.DataFrame:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    fields = "ts_code,trade_date,open,high,low,close,vol,amount,oi"
    last_error = None
    exchanges = EXCHANGE_ALIASES.get(exchange.upper(), [exchange, ""])
    for offset in range(60):
        date = (end_dt - timedelta(days=offset)).strftime("%Y%m%d")
        for exch in exchanges:
            try:
                kwargs = {"trade_date": date, "fields": fields}
                if exch:
                    kwargs["exchange"] = exch
                data = _query_optional_api("fut_daily", **kwargs)
                if data is not None and not data.empty:
                    data = data.copy()
                    data["query_exchange"] = exch or "ALL"
                    return data
            except Exception as exc:
                last_error = exc
    raise TushareDataError(
        f"No futures daily data found for {exchange} using aliases {exchanges}: {last_error}"
    )


def _fetch_futures_product(product: dict, curr_date: str, look_back_days: int) -> dict:
    name = product["name"]
    prefix = product["prefix"].upper()
    exchange = product["exchange"]
    try:
        latest_board = _latest_futures_trade_date(curr_date, exchange)
        candidates = latest_board[
            latest_board["ts_code"].fillna("").astype(str).str.upper().str.startswith(prefix)
        ].copy()
        if candidates.empty:
            raise TushareDataError(f"No {prefix} futures contract found on latest trade date.")

        candidates["oi_numeric"] = pd.to_numeric(candidates.get("oi"), errors="coerce")
        candidates["vol_numeric"] = pd.to_numeric(candidates.get("vol"), errors="coerce")
        candidates = candidates.sort_values(["oi_numeric", "vol_numeric"], ascending=False)
        latest = candidates.iloc[0]
        ts_code = latest["ts_code"]

        _, _, start, end = _date_window(curr_date, look_back_days)
        history = _query_futures_history(ts_code, exchange, start, end)
        history = history.sort_values("trade_date") if history is not None else pd.DataFrame()
        close = pd.to_numeric(history.get("close", pd.Series(dtype=float)), errors="coerce").dropna()
        if len(close) >= 2 and close.iloc[0] != 0:
            pct = f"{(close.iloc[-1] / close.iloc[0] - 1) * 100:.2f}%"
        else:
            pct = "N/A"

        receipt = _fetch_futures_receipt(ts_code, exchange, str(latest.get("trade_date")))
        return {
            "product": name,
            "role": product.get("role", ""),
            "data_type": "Tushare futures proxy",
            "latest_contract_or_source": ts_code,
            "latest_price": _format_value(latest.get("close")),
            "latest_date": str(latest.get("trade_date")),
            "change_over_window": pct,
            "inventory_or_receipt": receipt,
            "evidence_status": "Verified by Tushare futures daily data.",
            "evidence": (
                f"exchange={exchange}, query_exchange={latest.get('query_exchange', 'N/A')}, "
                f"prefix={prefix}, selected by open interest/volume"
            ),
        }
    except Exception as exc:
        return {
            "product": name,
            "role": product.get("role", ""),
            "data_type": "Tushare futures proxy",
            "latest_contract_or_source": f"{prefix}.{exchange}",
            "latest_price": "N/A",
            "latest_date": "N/A",
            "change_over_window": "N/A",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Unavailable; do not state price or change as fact.",
            "evidence": str(exc)[:800],
        }


def _query_futures_history(ts_code: str, exchange: str, start: str, end: str) -> pd.DataFrame:
    fields = "ts_code,trade_date,close,vol,oi"
    exchanges = EXCHANGE_ALIASES.get(exchange.upper(), [exchange, ""])
    last_error = None
    for exch in exchanges:
        try:
            kwargs = {
                "ts_code": ts_code,
                "start_date": start,
                "end_date": end,
                "fields": fields,
            }
            if exch:
                kwargs["exchange"] = exch
            data = _query_optional_api("fut_daily", **kwargs)
            if data is not None and not data.empty:
                return data
        except Exception as exc:
            last_error = exc
    raise TushareDataError(f"No futures history found for {ts_code}: {last_error}")


def _fetch_futures_receipt(ts_code: str, exchange: str, trade_date: str) -> str:
    try:
        receipt = pd.DataFrame()
        for exch in EXCHANGE_ALIASES.get(exchange.upper(), [exchange, ""]):
            kwargs = {
                "trade_date": trade_date,
                "fields": "trade_date,symbol,product,warehouse,vol",
            }
            if exch:
                kwargs["exchange"] = exch
            receipt = _query_optional_api("fut_wsr", **kwargs)
            if receipt is not None and not receipt.empty:
                break
        if receipt is None or receipt.empty:
            return "N/A"
        symbol = "".join([char for char in str(ts_code).split(".")[0] if char.isalpha()])
        matches = receipt[
            receipt["symbol"].fillna("").astype(str).str.upper().str.startswith(symbol.upper())
        ]
        if matches.empty or "vol" not in matches.columns:
            return "N/A"
        total = pd.to_numeric(matches["vol"], errors="coerce").sum()
        return _format_value(total)
    except Exception:
        return "N/A"


def _infer_products(symbol: str) -> dict:
    mapped = COMPANY_COMMODITY_MAP.get(symbol)
    if mapped:
        return mapped

    try:
        basic = _fetch_stock_basic(symbol)
    except Exception as exc:
        return {
            "name": symbol,
            "products": [],
            "spread_note": f"stock_basic lookup unavailable; commodity mapping unavailable: {exc}",
        }
    if basic is None:
        return {
            "name": symbol,
            "products": [],
            "spread_note": "No stock_basic data found; commodity mapping unavailable.",
        }

    haystack = f"{basic.get('name', '')} {basic.get('industry', '')}"
    products = []
    for keyword, hints in INDUSTRY_PRODUCT_HINTS.items():
        if keyword in haystack:
            products.extend(hints)

    return {
        "name": _format_value(basic.get("name")),
        "products": products,
        "spread_note": (
            "Products inferred from stock name/industry. Verify whether these proxies match the company's actual revenue mix."
            if products
            else "No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims."
        ),
    }


def get_commodity_context(ticker: str, curr_date: str, look_back_days: int = 90) -> str:
    """Return evidence-backed commodity price context for A-share companies."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Commodity context expects A-share symbols like 000001.SZ or 600160.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    mapping = _infer_products(symbol)
    products = mapping.get("products", [])
    rows = []
    for product in products:
        if product.get("type") == "futures":
            rows.append(_fetch_futures_product(product, curr_date, look_back_days))
        elif product.get("type") == "web_spot":
            rows.append(_fetch_web_spot(product))

    lines = [
        f"# Commodity and product price context for {symbol} as of {curr_date}",
        "",
        f"- Company/product map: {mapping.get('name', symbol)}",
        f"- Look-back window for futures proxies: {look_back_days} days",
        f"- Spread note: {mapping.get('spread_note', 'N/A')}",
        "",
        "## Evidence Table",
    ]

    if rows:
        lines.append(_markdown_table(pd.DataFrame(rows)))
    else:
        lines.append("No commodity mapping is available for this ticker.")

    lines.extend(
        [
            "",
            "## Analyst Instructions",
            "- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.",
            "- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.",
            "- Do not state R32, R125, lithium, copper, inventory, or spread changes as facts unless they appear in the evidence table.",
            "- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.",
        ]
    )
    return "\n".join(lines)
