from __future__ import annotations

from datetime import datetime
from urllib.parse import urlparse

import pandas as pd
import requests
from parsel import Selector

from .tushare_a_stock import TushareDataError, _markdown_table, is_a_share_symbol


SHIPPING_ALLOWED_DOMAINS = {
    "en.stockq.org",
    "stockq.org",
    "www.balticexchange.com",
    "balticexchange.com",
}


STOCKQ_INDICES = {
    "BDTI": {
        "name": "Baltic Dirty Tanker Index",
        "url": "https://en.stockq.org/index/BDTI.php",
        "segment": "crude/product tanker",
        "meaning": "Dirty tanker market proxy, relevant to crude oil tanker earnings.",
    },
    "BCTI": {
        "name": "Baltic Clean Tanker Index",
        "url": "https://en.stockq.org/index/BCTI.php",
        "segment": "product tanker",
        "meaning": "Clean tanker market proxy, relevant to refined oil/product tanker earnings.",
    },
    "BDI": {
        "name": "Baltic Dry Index",
        "url": "https://en.stockq.org/index/BDI.php",
        "segment": "dry bulk",
        "meaning": "Dry bulk composite proxy, relevant to iron ore, coal, grain shipping demand.",
    },
    "BCI": {
        "name": "Baltic Capesize Index",
        "url": "https://en.stockq.org/index/BCI.php",
        "segment": "dry bulk capesize",
        "meaning": "Capesize proxy, relevant to iron ore and coal routes.",
    },
    "BPI": {
        "name": "Baltic Panamax Index",
        "url": "https://en.stockq.org/index/BPI.php",
        "segment": "dry bulk panamax",
        "meaning": "Panamax proxy, relevant to coal, grain, and mid-size bulk trades.",
    },
    "BSI": {
        "name": "Baltic Supramax Index",
        "url": "https://en.stockq.org/index/BSI.php",
        "segment": "dry bulk supramax",
        "meaning": "Supramax proxy, relevant to smaller bulk trades.",
    },
}


SHIPPING_COMPANY_MAP = {
    "601872.SH": {
        "name": "招商轮船",
        "segments": ["crude_tanker", "dry_bulk", "lng"],
        "indices": ["BDTI", "BDI", "BCI", "BPI"],
        "note": "Oil tanker exposure needs VLCC route/TCE validation; dry bulk and LNG are additional cycle drivers.",
    },
    "600026.SH": {
        "name": "中远海能",
        "segments": ["crude_tanker", "product_tanker"],
        "indices": ["BDTI", "BCTI"],
        "note": "Crude/product tanker spot earnings are key drivers.",
    },
    "601975.SH": {
        "name": "招商南油",
        "segments": ["product_tanker"],
        "indices": ["BCTI", "BDTI"],
        "note": "Product tanker rates are more relevant than VLCC crude tanker rates.",
    },
    "601919.SH": {
        "name": "中远海控",
        "segments": ["container"],
        "indices": [],
        "note": "Container freight indices such as SCFI/CCFI need a dedicated source; do not infer from tanker indices.",
    },
}


ROUTE_TAXONOMY = {
    "crude_tanker": [
        {
            "route": "VLCC Middle East Gulf -> China",
            "common_code": "TD3C / CTFI China-import VLCC proxy",
            "driver": "China crude imports, OPEC supply, ton-mile demand, sanctions/fleet availability.",
            "data_status": "Route-level TCE/rate not yet parsed; use BDTI and public CTFI news as proxy only.",
        },
        {
            "route": "VLCC West Africa -> China",
            "common_code": "WAF-China VLCC proxy",
            "driver": "Atlantic crude exports, China buying, ballast distance.",
            "data_status": "Unverified route-level data source required.",
        },
        {
            "route": "Suezmax West Africa -> Europe/US",
            "common_code": "Suezmax proxy",
            "driver": "Atlantic basin crude flows and fleet tightness.",
            "data_status": "Unverified route-level data source required.",
        },
        {
            "route": "Aframax regional crude trades",
            "common_code": "Aframax proxy",
            "driver": "Regional crude arbitrage and port constraints.",
            "data_status": "Unverified route-level data source required.",
        },
    ],
    "product_tanker": [
        {
            "route": "MR product tanker East/West routes",
            "common_code": "BCTI / MR proxy",
            "driver": "Refined product exports, refinery margins, regional inventory gaps.",
            "data_status": "Use BCTI as broad proxy; route-level MR TCE requires dedicated source.",
        },
        {
            "route": "LR2 naphtha/product tanker routes",
            "common_code": "LR2 proxy",
            "driver": "Asia naphtha demand and clean product arbitrage.",
            "data_status": "Unverified route-level data source required.",
        },
    ],
    "dry_bulk": [
        {
            "route": "Brazil -> China iron ore",
            "common_code": "C3 / Capesize proxy",
            "driver": "Iron ore imports, Brazil-China ton-mile demand.",
            "data_status": "Use BCI/BDI as broad proxy; route-level C3 requires dedicated source.",
        },
        {
            "route": "West Australia -> China iron ore",
            "common_code": "C5 / Capesize proxy",
            "driver": "China steel demand and Australian iron ore shipments.",
            "data_status": "Use BCI/BDI as broad proxy; route-level C5 requires dedicated source.",
        },
        {
            "route": "Panamax coal/grain trades",
            "common_code": "P-route proxy",
            "driver": "Coal imports, grain seasonality, port congestion.",
            "data_status": "Use BPI as broad proxy.",
        },
    ],
    "container": [
        {
            "route": "Asia -> Europe container",
            "common_code": "SCFI/CCFI route proxy",
            "driver": "Retail demand, blank sailings, Red Sea detours, vessel supply.",
            "data_status": "Dedicated SCFI/CCFI source not yet integrated.",
        },
        {
            "route": "Transpacific container",
            "common_code": "SCFI/FBX proxy",
            "driver": "US import demand, tariff timing, inventory cycle.",
            "data_status": "Dedicated SCFI/CCFI/FBX source not yet integrated.",
        },
    ],
    "lng": [
        {
            "route": "LNG carrier spot market",
            "common_code": "BLNG proxy",
            "driver": "Winter demand, European gas storage, Asian LNG spot demand.",
            "data_status": "Baltic LNG route data not yet integrated.",
        }
    ],
}


def _is_allowed_url(url: str) -> bool:
    return urlparse(url).netloc.lower() in SHIPPING_ALLOWED_DOMAINS


def _clean_text(text: str) -> str:
    return " ".join(str(text or "").split())


def _fetch_page(url: str) -> str:
    if not _is_allowed_url(url):
        raise TushareDataError(f"URL is not in the shipping whitelist: {url}")
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
    return response.text


def _parse_stockq_index(code: str) -> dict:
    meta = STOCKQ_INDICES[code]
    try:
        html = _fetch_page(meta["url"])
        selector = Selector(text=html)
        text = _clean_text(" ".join(selector.xpath("//body//text()").getall()))
        tokens = text.split()
        idx = tokens.index("local")
        latest_value = tokens[idx + 1]
        change = tokens[idx + 2]
        change_pct = tokens[idx + 3]
        local_date = tokens[idx + 8] if len(tokens) > idx + 8 else "N/A"

        latest_rows = []
        for pos, token in enumerate(tokens):
            if "/" in token and len(token) == 10 and pos + 2 < len(tokens):
                latest_rows.append(f"{token} {tokens[pos + 1]} {tokens[pos + 2]}")
            if len(latest_rows) >= 8:
                break

        return {
            "index": code,
            "name": meta["name"],
            "segment": meta["segment"],
            "latest_value": latest_value,
            "change": change,
            "change_pct": change_pct,
            "local_date": local_date,
            "source": meta["url"],
            "evidence_status": "Fetched from StockQ public Baltic index page.",
            "evidence": "; ".join(latest_rows)[:500],
            "meaning": meta["meaning"],
        }
    except Exception as exc:
        return {
            "index": code,
            "name": meta["name"],
            "segment": meta["segment"],
            "latest_value": "N/A",
            "change": "N/A",
            "change_pct": "N/A",
            "local_date": "N/A",
            "source": meta["url"],
            "evidence_status": "Unavailable; do not state freight index level or change as fact.",
            "evidence": str(exc)[:500],
            "meaning": meta["meaning"],
        }


def _infer_shipping_mapping(symbol: str) -> dict:
    mapped = SHIPPING_COMPANY_MAP.get(symbol)
    if mapped:
        return mapped
    return {
        "name": symbol,
        "segments": [],
        "indices": [],
        "note": "No shipping mapping found. Add the ticker to SHIPPING_COMPANY_MAP before making shipping-rate claims.",
    }


def _route_table(segments: list[str]) -> pd.DataFrame:
    rows = []
    for segment in segments:
        rows.extend(ROUTE_TAXONOMY.get(segment, []))
    return pd.DataFrame(rows)


def get_shipping_context(ticker: str, curr_date: str, look_back_days: int = 90) -> str:
    """Return evidence-backed shipping cycle context for A-share shipping companies."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Shipping context expects A-share symbols like 601872.SH or 600026.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    mapping = _infer_shipping_mapping(symbol)
    index_rows = [_parse_stockq_index(code) for code in mapping.get("indices", [])]
    route_rows = _route_table(mapping.get("segments", []))

    lines = [
        f"# Shipping cycle context for {symbol} as of {curr_date}",
        "",
        f"- Company/segment map: {mapping.get('name', symbol)}",
        f"- Segments: {', '.join(mapping.get('segments', [])) or 'N/A'}",
        f"- Note: {mapping.get('note', 'N/A')}",
        "",
        "## Freight Index Evidence",
    ]
    if index_rows:
        lines.append(_markdown_table(pd.DataFrame(index_rows)))
    else:
        lines.append("No mapped public shipping index is available for this ticker.")

    lines.extend(["", "## Route Coverage And Missing Data"])
    if not route_rows.empty:
        lines.append(_markdown_table(route_rows))
    else:
        lines.append("No route taxonomy is mapped for this ticker.")

    lines.extend(
        [
            "",
            "## Analyst Instructions",
            "- Use BDTI as a broad crude/dirty tanker proxy, not a specific VLCC TD3C TCE quote.",
            "- Use BCTI as a broad clean/product tanker proxy, not a specific MR/LR route quote.",
            "- Use BDI/BCI/BPI/BSI as broad dry bulk proxies, not exact voyage rates.",
            "- If VLCC TD3C, TCE, SCFI/CCFI, LNG, or route-level rates are not in the evidence table, list them as unverified key variables.",
            "- Shipping equities are cyclical: connect freight indices to fleet supply, commodity demand, oil prices, sanctions, congestion, and contract/spot exposure.",
        ]
    )
    return "\n".join(lines)
