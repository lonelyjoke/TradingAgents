from __future__ import annotations

from datetime import datetime, timedelta
import re
from urllib.parse import urlparse

import pandas as pd
import requests

try:
    from parsel import Selector
except ModuleNotFoundError:  # pragma: no cover - exercised when optional dep is absent.
    Selector = None

from .industry_classifier import banking_profile_hint, is_banking_entity
from .industry_identity import is_telecom_operator_text
from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)
from .tushare_research import _date_window, _fetch_announcements, _query_optional_api


ALLOWED_DOMAINS = {
    "www.baiinfo.com",
    "baiinfo.com",
    "www.100ppi.com",
    "100ppi.com",
    "www.moa.gov.cn",
    "moa.gov.cn",
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


METAL_FUTURES_SOURCE_REGISTRY = {
    "Gold": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "AU",
        "contract_example": "AU.SHF",
        "overseas_cross_checks": "COMEX GC futures; LBMA gold benchmark",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Silver": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "AG",
        "contract_example": "AG.SHF",
        "overseas_cross_checks": "COMEX SI futures; LBMA silver benchmark",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Copper": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "CU",
        "contract_example": "CU.SHF",
        "overseas_cross_checks": "COMEX HG futures; LME copper",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Aluminum": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "AL",
        "contract_example": "AL.SHF",
        "overseas_cross_checks": "LME aluminum",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Alumina": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "AO",
        "contract_example": "AO.SHF",
        "overseas_cross_checks": "domestic alumina spot assessments from SMM / Baiinfo / Mysteel when licensed",
        "coverage": "live domestic futures via Tushare as an alumina cost/spread proxy; spot assessments require separate licensed data",
    },
    "Zinc": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "ZN",
        "contract_example": "ZN.SHF",
        "overseas_cross_checks": "LME zinc",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Lead": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "PB",
        "contract_example": "PB.SHF",
        "overseas_cross_checks": "LME lead",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Nickel": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "NI",
        "contract_example": "NI.SHF",
        "overseas_cross_checks": "LME nickel",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Tin": {
        "domestic_exchange": "SHFE",
        "tushare_prefix": "SN",
        "contract_example": "SN.SHF",
        "overseas_cross_checks": "LME tin",
        "coverage": "live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module",
    },
    "Lithium carbonate": {
        "domestic_exchange": "GFEX",
        "tushare_prefix": "LC",
        "contract_example": "LC.GFE",
        "overseas_cross_checks": "Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments",
        "coverage": "live GFEX futures via Tushare; global spot assessment sources require separate licensed data",
    },
    "Industrial silicon": {
        "domestic_exchange": "GFEX",
        "tushare_prefix": "SI",
        "contract_example": "SI.GFE",
        "overseas_cross_checks": "SMM / Asian Metal silicon spot assessments",
        "coverage": "live GFEX futures via Tushare; spot assessments require separate licensed data",
    },
}


def _metal_product(name: str, role: str = "main product") -> dict:
    source = METAL_FUTURES_SOURCE_REGISTRY[name]
    return {
        "name": name,
        "type": "futures",
        "role": role,
        "prefix": source["tushare_prefix"],
        "exchange": source["domestic_exchange"],
        "overseas_cross_checks": source["overseas_cross_checks"],
    }


def _unavailable_key_driver(name: str, role: str, source_hint: str) -> dict:
    return {
        "name": name,
        "type": "unavailable_key_driver",
        "role": role,
        "source_hint": source_hint,
    }


COMPANY_COMMODITY_MAP = {
    "600547.SH": {
        "name": "Shandong Gold",
        "products": [_metal_product("Gold")],
        "spread_note": "Use SHFE gold futures as the timely domestic proxy; realized mine price, output, grade, and unit cost still require filings and production disclosures.",
    },
    "000975.SZ": {
        "name": "Shanjin International Gold",
        "products": [_metal_product("Gold")],
        "spread_note": "Use SHFE gold futures as the timely domestic proxy; validate equity output, mine cost, and overseas asset exposure from filings.",
    },
    "600489.SH": {
        "name": "Zhongjin Gold",
        "products": [_metal_product("Gold")],
        "spread_note": "Use SHFE gold futures as the timely domestic proxy; separate mining profit from smelting/trading contribution.",
    },
    "600988.SH": {
        "name": "Chifeng Gold",
        "products": [_metal_product("Gold")],
        "spread_note": "Use SHFE gold futures as the timely domestic proxy; overseas mine jurisdiction, grade, and unit cost are separate diligence items.",
    },
    "002155.SZ": {
        "name": "Hunan Gold",
        "products": [_metal_product("Gold"), _metal_product("Silver")],
        "spread_note": "Use SHFE gold/silver futures as proxies; antimony and other by-products need separate spot or filing evidence before quantification.",
    },
    "002237.SZ": {
        "name": "Hengbang",
        "products": [_metal_product("Gold"), _metal_product("Silver")],
        "spread_note": "Use SHFE precious-metal futures as proxies; split mining, smelting, and processing/trading economics.",
    },
    "601899.SH": {
        "name": "Zijin Mining",
        "products": [_metal_product("Copper"), _metal_product("Gold")],
        "spread_note": "Use metal futures as price proxies; mine cost curves still require external research.",
    },
    "603993.SH": {
        "name": "CMOC",
        "products": [_metal_product("Copper"), _metal_product("Nickel", "secondary product")],
        "spread_note": "Use SHFE copper/nickel as domestic proxies; cobalt and molybdenum need separate spot benchmarks and company disclosures.",
    },
    "600362.SH": {
        "name": "Jiangxi Copper",
        "products": [_metal_product("Copper")],
        "spread_note": "Use SHFE copper as the timely proxy; separate mining, smelting TC/RC, inventory, and trading exposure.",
    },
    "000878.SZ": {
        "name": "Yunnan Copper",
        "products": [_metal_product("Copper")],
        "spread_note": "Use SHFE copper as the timely proxy; smelting margins and TC/RC can offset copper-price beta.",
    },
    "000630.SZ": {
        "name": "Tongling Nonferrous",
        "products": [_metal_product("Copper")],
        "spread_note": "Use SHFE copper as the timely proxy; validate mine share versus smelting/trading share before extrapolating margins.",
    },
    "601600.SH": {
        "name": "Chalco",
        "products": [
            _metal_product("Aluminum"),
            _metal_product("Alumina", "raw-material / upstream spread proxy"),
            _unavailable_key_driver(
                "Power cost",
                "electricity input cost driver",
                "company filings, regional tariff/self-generation disclosures, or licensed power-cost datasets",
            ),
            _unavailable_key_driver(
                "Carbon anode cost",
                "carbon/anode input cost driver",
                "company filings or licensed petroleum-coke / prebaked-anode spot datasets",
            ),
        ],
        "spread_note": "Use SHFE aluminum as the timely selling-price proxy and SHFE alumina as a cost/spread proxy; power cost, anode cost, and capacity utilization still require company disclosures or licensed datasets. Missing cost data is a neutral evidence gap, not bearish evidence.",
    },
    "000807.SZ": {
        "name": "Yunnan Aluminium",
        "products": [
            _metal_product("Aluminum"),
            _metal_product("Alumina", "raw-material / upstream spread proxy"),
            _unavailable_key_driver(
                "Power cost",
                "hydro/power-tariff input cost driver",
                "company filings, regional hydropower/tariff disclosures, or licensed power-cost datasets",
            ),
        ],
        "spread_note": "Use SHFE aluminum as the timely selling-price proxy and SHFE alumina as a cost/spread proxy; power cost, hydro availability, and capacity utilization determine margin pass-through. Missing cost data is a neutral evidence gap, not bearish evidence.",
    },
    "000426.SZ": {
        "name": "Xingye Silver & Tin",
        "products": [
            _metal_product("Silver"),
            _metal_product("Tin"),
            _metal_product("Lead", "secondary product"),
            _metal_product("Zinc", "secondary product"),
        ],
        "spread_note": "Use SHFE silver, tin, lead, and zinc futures as timely product-price proxies; reserve grade, equity output, AISC/unit cost, and mine ramp still require filing or production disclosure before extrapolating margins.",
    },
    "603345.SH": {
        "name": "Anjoy Foods",
        "products": [
            {"name": "Live hog futures", "type": "futures", "role": "meat raw-material cost proxy", "prefix": "LH", "exchange": "DCE", "selection": "near_month_with_main_reference"},
            {"name": "Soybean meal futures", "type": "futures", "role": "feed and protein-chain cost proxy", "prefix": "M", "exchange": "DCE", "selection": "near_month_with_main_reference"},
            {"name": "Corn futures", "type": "futures", "role": "feed and starch/flour-chain cost proxy", "prefix": "C", "exchange": "DCE", "selection": "near_month_with_main_reference"},
            {"name": "Palm oil futures", "type": "futures", "role": "edible-oil cost proxy for prepared dishes", "prefix": "P", "exchange": "DCE", "selection": "near_month_with_main_reference"},
        ],
        "spread_note": "For frozen-food processors, these are cost proxies rather than realized input prices. Fish paste/surimi, poultry, flour, packaging, cold-chain and channel promotion still require filings, official data, or reputable industry checks before quantification.",
    },
    "002460.SZ": {
        "name": "Ganfeng Lithium",
        "products": [_metal_product("Lithium carbonate")],
        "spread_note": "Lithium carbonate futures proxy product price; lithium concentrate costs require external data.",
    },
    "002466.SZ": {
        "name": "Tianqi Lithium",
        "products": [_metal_product("Lithium carbonate")],
        "spread_note": "GFEX lithium carbonate futures proxy downstream product price; upstream spodumene and equity-accounted assets require separate checks.",
    },
    "600111.SH": {
        "name": "China Northern Rare Earth",
        "products": [],
        "spread_note": "Rare-earth oxide prices are not covered by the Tushare futures chain here; use official/licensed spot benchmarks before making price claims.",
    },
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
    "300750.SZ": {
        "name": "CATL",
        "products": [
            {"name": "Lithium carbonate", "type": "futures", "role": "raw material proxy", "prefix": "LC", "exchange": "GFEX"},
        ],
        "spread_note": "For battery makers, lithium carbonate is a cost proxy rather than a direct revenue product.",
    },
    "301358.SZ": {
        "name": "Hunan Yuneng",
        "products": [
            {"name": "Lithium carbonate", "type": "futures", "role": "LFP cathode raw-material cost proxy", "prefix": "LC", "exchange": "GFEX"},
        ],
        "spread_note": "For LFP cathode producers, lithium carbonate is a critical raw-material cost proxy, not the realized cathode selling price. Margin work still needs LFP cathode ASP, iron phosphate cost, processing fee, capacity utilization, customer mix, and inventory-cost lag evidence.",
    },
    "002714.SZ": {
        "name": "Muyuan Foods",
        "products": [
            {"name": "Breeding sow inventory", "type": "moa_livestock", "role": "capacity leading signal", "keywords": ["能繁母猪", "存栏"]},
            {"name": "Live hog", "type": "moa_livestock", "role": "main product", "keywords": ["活猪", "生猪"]},
            {"name": "Live hog futures", "type": "futures", "role": "timely market-implied price signal", "prefix": "LH", "exchange": "DCE", "selection": "near_month_with_main_reference"},
            {"name": "Piglet", "type": "moa_livestock", "role": "leading supply signal", "keywords": ["仔猪"]},
            {"name": "Pork", "type": "moa_livestock", "role": "downstream price", "keywords": ["猪肉"]},
            {"name": "Feed", "type": "moa_livestock", "role": "cost proxy", "keywords": ["活猪配合饲料", "饲料"]},
            {"name": "Hog-grain ratio", "type": "moa_livestock", "role": "cycle spread", "keywords": ["猪粮比价", "猪粮比"]},
        ],
        "spread_note": "For hog breeders, read realized hog price together with piglet price, feed cost, and hog-grain spread before extrapolating earnings.",
    },
}


INDUSTRY_PRODUCT_HINTS = {
    "铜": [_metal_product("Copper", "industry proxy")],
    "黄金": [_metal_product("Gold", "industry proxy")],
    "银": [_metal_product("Silver", "industry proxy")],
    "锡": [_metal_product("Tin", "industry proxy")],
    "铅": [_metal_product("Lead", "industry proxy")],
    "锌": [_metal_product("Zinc", "industry proxy")],
    "锂": [_metal_product("Lithium carbonate", "industry proxy")],
    "煤": [{"name": "Coking coal", "type": "futures", "role": "industry proxy", "prefix": "JM", "exchange": "DCE"}],
    "钢": [{"name": "Rebar", "type": "futures", "role": "industry proxy", "prefix": "RB", "exchange": "SHFE"}],
    "铝": [_metal_product("Aluminum", "industry proxy")],
    "养殖": [
        {"name": "Breeding sow inventory", "type": "moa_livestock", "role": "capacity leading signal", "keywords": ["能繁母猪", "存栏"]},
        {"name": "Live hog", "type": "moa_livestock", "role": "main product", "keywords": ["活猪", "生猪"]},
        {"name": "Live hog futures", "type": "futures", "role": "timely market-implied price signal", "prefix": "LH", "exchange": "DCE", "selection": "near_month_with_main_reference"},
        {"name": "Piglet", "type": "moa_livestock", "role": "leading supply signal", "keywords": ["仔猪"]},
        {"name": "Feed", "type": "moa_livestock", "role": "cost proxy", "keywords": ["活猪配合饲料", "饲料"]},
        {"name": "Hog-grain ratio", "type": "moa_livestock", "role": "cycle spread", "keywords": ["猪粮比价", "猪粮比"]},
    ],
    "畜牧": [
        {"name": "Breeding sow inventory", "type": "moa_livestock", "role": "capacity leading signal", "keywords": ["能繁母猪", "存栏"]},
        {"name": "Live hog", "type": "moa_livestock", "role": "main product", "keywords": ["活猪", "生猪"]},
        {"name": "Live hog futures", "type": "futures", "role": "timely market-implied price signal", "prefix": "LH", "exchange": "DCE", "selection": "near_month_with_main_reference"},
        {"name": "Piglet", "type": "moa_livestock", "role": "leading supply signal", "keywords": ["仔猪"]},
        {"name": "Feed", "type": "moa_livestock", "role": "cost proxy", "keywords": ["活猪配合饲料", "饲料"]},
        {"name": "Hog-grain ratio", "type": "moa_livestock", "role": "cycle spread", "keywords": ["猪粮比价", "猪粮比"]},
    ],
}

LITHIUM_MATERIAL_HINTS = (
    "正极",
    "负极",
    "磷酸铁锂",
    "三元材料",
    "前驱体",
    "锂电材料",
    "电池材料",
    "LFP",
    "cathode",
    "precursor",
)


def _lithium_material_products() -> list[dict]:
    return [
        {
            "name": "Lithium carbonate",
            "type": "futures",
            "role": "lithium-battery-material raw-material cost proxy",
            "prefix": "LC",
            "exchange": "GFEX",
        }
    ]

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
    if Selector is not None:
        selector = Selector(text=response.text)
        title = _clean_text(selector.xpath("//title/text()").get(""))
        body = _clean_text(" ".join(selector.xpath("//body//text()").getall()))
    else:
        title_match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.I | re.S)
        title = _clean_text(title_match.group(1) if title_match else "")
        body = _clean_text(re.sub(r"<[^>]+>", " ", response.text))
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


def _moa_monthly_archive_urls(curr_date: str, months_back: int = 6) -> list[str]:
    anchor = datetime.strptime(curr_date, "%Y-%m-%d")
    urls = []
    for offset in range(months_back):
        year = anchor.year
        month = anchor.month - offset
        while month <= 0:
            month += 12
            year -= 1
        urls.append(f"https://www.moa.gov.cn/ztzl/szcpxx/jdsj/{year}/{year}{month:02d}/")
    return urls


def _fetch_moa_livestock_market(product: dict, curr_date: str) -> dict:
    name = product["name"]
    keywords = list(product.get("keywords", []))
    errors = []
    for url in _moa_monthly_archive_urls(curr_date):
        try:
            title, body = _fetch_whitelisted_page(url)
            if not any(keyword in body for keyword in keywords):
                continue
            snippets = []
            for keyword in keywords:
                snippets.extend(_extract_evidence_snippets(keyword, title, body, max_snippets=2))
            snippets = list(dict.fromkeys(snippets))
            return {
                "product": name,
                "role": product.get("role", ""),
                "data_type": "official livestock market evidence",
                "latest_contract_or_source": url,
                "latest_price": "See official source",
                "latest_date": "See official source",
                "change_over_window": "Not computed",
                "inventory_or_receipt": "N/A",
                "evidence_status": "Fetched official MOA livestock archive page; use as verified cycle evidence, parse exact series before quantifying.",
                "evidence": " | ".join(snippets)[:800] if snippets else title,
            }
        except Exception as exc:
            errors.append(f"{url}: {exc}")
    return {
        "product": name,
        "role": product.get("role", ""),
        "data_type": "official livestock market evidence",
        "latest_contract_or_source": "MOA monthly livestock archive",
        "latest_price": "N/A",
        "latest_date": "N/A",
        "change_over_window": "N/A",
        "inventory_or_receipt": "N/A",
        "evidence_status": "Unavailable; do not state hog-cycle data as fact.",
        "evidence": "; ".join(errors)[:800],
    }


def _fetch_livestock_sales_announcements(symbol: str, curr_date: str, look_back_days: int) -> dict:
    """Use company sales briefs as stable, ticker-specific hog-cycle evidence."""
    try:
        announcements = _fetch_announcements(symbol, curr_date, look_back_days)
        if isinstance(announcements, TushareDataError):
            raise announcements
        if announcements is None or announcements.empty:
            raise TushareDataError("No recent company announcement rows returned.")

        data = announcements.copy()
        title = data.get("title", pd.Series(dtype=str)).fillna("").astype(str)
        mask = title.str.contains("销售简报|销售情况|商品猪|生猪销售|活猪销售", regex=True)
        matches = data[mask].copy()
        if matches.empty:
            raise TushareDataError("No recent livestock sales brief announcement found.")

        sort_cols = [col for col in ("ann_date", "rec_time") if col in matches.columns]
        if sort_cols:
            matches = matches.sort_values(sort_cols, ascending=False)
        latest = matches.iloc[0]
        snippets = []
        for _, row in matches.head(3).iterrows():
            date = _format_value(row.get("ann_date") or row.get("rec_time"))
            snippets.append(f"{date}: {_clean_text(row.get('title', ''))}")
        return {
            "product": "Company monthly hog sales brief",
            "role": "ticker-specific realized volume/price evidence",
            "data_type": "company announcement",
            "latest_contract_or_source": _format_value(latest.get("url") or "Tushare/CNINFO announcements"),
            "latest_price": "Not parsed",
            "latest_date": _format_value(latest.get("ann_date") or latest.get("rec_time")),
            "change_over_window": "Not computed",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Fetched stable company announcement titles; parse the PDF/text before quantifying realized price or volume.",
            "evidence": " | ".join(snippets)[:800],
        }
    except Exception as exc:
        return {
            "product": "Company monthly hog sales brief",
            "role": "ticker-specific realized volume/price evidence",
            "data_type": "company announcement",
            "latest_contract_or_source": "Tushare/CNINFO announcements",
            "latest_price": "N/A",
            "latest_date": "N/A",
            "change_over_window": "N/A",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Unavailable; do not state company realized hog price or sales volume as fact.",
            "evidence": str(exc)[:800],
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


def _contract_month_key(ts_code: object) -> int | None:
    match = re.match(r"^[A-Za-z]+(\d{4})", str(ts_code or "").split(".")[0])
    if not match:
        return None
    yy = int(match.group(1)[:2])
    mm = int(match.group(1)[2:])
    if mm < 1 or mm > 12:
        return None
    return (2000 + yy) * 100 + mm


def _futures_root(ts_code: object) -> str:
    code = str(ts_code or "").split(".")[0].upper()
    match = re.match(r"^([A-Z]+)(?:\d{4})?$", code)
    return match.group(1) if match else ""


def _trade_month_key(trade_date: object, curr_date: str) -> int:
    raw = re.sub(r"\D", "", str(trade_date or ""))
    if len(raw) >= 6:
        return int(raw[:6])
    return int(datetime.strptime(curr_date, "%Y-%m-%d").strftime("%Y%m"))


def _futures_curve_summary(candidates: pd.DataFrame, limit: int = 6) -> str:
    if candidates is None or candidates.empty:
        return "N/A"
    curve = candidates.copy()
    if "contract_month_key" not in curve.columns:
        curve["contract_month_key"] = curve.get("ts_code", pd.Series(dtype=str)).map(_contract_month_key)
    if "oi_numeric" not in curve.columns:
        curve["oi_numeric"] = pd.to_numeric(curve.get("oi"), errors="coerce").fillna(0)
    if "vol_numeric" not in curve.columns:
        curve["vol_numeric"] = pd.to_numeric(curve.get("vol"), errors="coerce").fillna(0)
    curve = curve.dropna(subset=["contract_month_key"]).copy()
    if curve.empty:
        return "N/A"
    curve = curve.sort_values(["contract_month_key", "oi_numeric", "vol_numeric"], ascending=[True, False, False])
    parts = []
    for _, row in curve.head(limit).iterrows():
        parts.append(
            f"{row.get('ts_code')} close={_format_value(row.get('close'))}, "
            f"oi={_format_value(row.get('oi'))}, vol={_format_value(row.get('vol'))}"
        )
    return " | ".join(parts)


def _select_futures_contracts(candidates: pd.DataFrame, curr_date: str, selection: str) -> tuple[pd.Series, pd.Series, str]:
    candidates = candidates.copy()
    candidates["oi_numeric"] = pd.to_numeric(candidates.get("oi"), errors="coerce").fillna(0)
    candidates["vol_numeric"] = pd.to_numeric(candidates.get("vol"), errors="coerce").fillna(0)
    candidates["close_numeric"] = pd.to_numeric(candidates.get("close"), errors="coerce")
    candidates["contract_month_key"] = candidates.get("ts_code", pd.Series(dtype=str)).map(_contract_month_key)

    main_board = candidates.sort_values(["oi_numeric", "vol_numeric"], ascending=False)
    main = main_board.iloc[0]

    if selection != "near_month_with_main_reference":
        return main, main, "selected by open interest/volume"

    trade_month = _trade_month_key(main.get("trade_date"), curr_date)
    liquid = candidates[candidates["close_numeric"].notna() & (candidates["close_numeric"] > 0)].copy()
    if liquid.empty:
        return main, main, "selected by open interest/volume; no liquid near-month candidate"

    forward = liquid[liquid["contract_month_key"].fillna(0) >= trade_month].copy()
    if forward.empty:
        forward = liquid.copy()
    forward = forward.sort_values(
        ["contract_month_key", "oi_numeric", "vol_numeric"],
        ascending=[True, False, False],
    )
    near = forward.iloc[0]
    reason = "selected nearest active contract; main/open-interest contract kept as reference"
    return near, main, reason


def _fetch_futures_product(product: dict, curr_date: str, look_back_days: int) -> dict:
    name = product["name"]
    prefix = product["prefix"].upper()
    exchange = product["exchange"]
    try:
        latest_board = _latest_futures_trade_date(curr_date, exchange)
        candidates = latest_board[
            latest_board["ts_code"].fillna("").astype(str).map(_futures_root) == prefix
        ].copy()
        if candidates.empty:
            raise TushareDataError(f"No {prefix} futures contract found on latest trade date.")

        latest, main_contract, selection_reason = _select_futures_contracts(
            candidates,
            curr_date,
            str(product.get("selection", "")),
        )
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
        main_note = ""
        if str(main_contract.get("ts_code")) != str(ts_code):
            main_note = (
                f"; main_contract={main_contract.get('ts_code')} "
                f"close={_format_value(main_contract.get('close'))}, "
                f"oi={_format_value(main_contract.get('oi'))}"
            )
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
                f"prefix={prefix}, {selection_reason}{main_note}; "
                f"curve={_futures_curve_summary(candidates)}"
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


def _missing_key_driver_row(product: dict) -> dict:
    return {
        "product": product.get("name", ""),
        "role": product.get("role", ""),
        "data_type": "unavailable key driver",
        "latest_contract_or_source": product.get("source_hint", "No reliable mapped source"),
        "latest_price": "N/A",
        "latest_date": "N/A",
        "change_over_window": "N/A",
        "inventory_or_receipt": "N/A",
        "evidence_status": "Missing; neutral for direction, confidence cap only.",
        "evidence": "Do not treat this unavailable cost driver as margin deterioration or margin resilience without independent verified evidence.",
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
        symbol = _futures_root(ts_code)
        matches = receipt[receipt["symbol"].fillna("").astype(str).map(_futures_root) == symbol]
        if matches.empty or "vol" not in matches.columns:
            return "N/A"
        total = pd.to_numeric(matches["vol"], errors="coerce").sum()
        return _format_value(total)
    except Exception:
        return "N/A"


def _filing_text_probe(symbol: str, curr_date: str | None, look_back_days: int) -> str:
    if not curr_date:
        return ""
    try:
        from .filing_research import _load_financial_report_texts

        _, reports = _load_financial_report_texts(symbol, curr_date, look_back_days)
    except Exception:
        return ""
    return " ".join(text[:6000] for _, text in reports[:4])


def _infer_products(symbol: str, curr_date: str | None = None, look_back_days: int = 900) -> dict:
    symbol = str(symbol or "").strip().upper()
    bank_hint = banking_profile_hint(symbol)
    if bank_hint is not None:
        return {
            "name": bank_hint[0],
            "products": [],
            "spread_note": "Not applicable: financial institutions do not have a primary commodity/product-price spread driver. Use bank/financial KPIs instead.",
        }
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
    filing_probe = _filing_text_probe(symbol, curr_date, look_back_days)
    evidence_haystack = f"{haystack} {filing_probe}"
    if is_banking_entity(symbol, basic=basic) or any(token in haystack for token in ("银行", "保险", "证券", "信托", "多元金融")):
        return {
            "name": _format_value(basic.get("name")),
            "products": [],
            "spread_note": "Not applicable: financial institutions do not have a primary commodity/product-price spread driver. Use bank/financial KPIs instead.",
        }
    if is_telecom_operator_text(symbol, haystack, filing_probe):
        return {
            "name": _format_value(basic.get("name")),
            "products": [],
            "spread_note": "Not applicable: telecom operators do not have a primary commodity/product-price spread driver. Use telecom ARPU, subscribers, cloud/AI, capex, FCF, and dividend KPIs instead.",
        }
    products = []
    wind_equipment = any(
        token in evidence_haystack
        for token in ("风电", "海上风电", "海风", "塔筒", "管桩", "导管架", "海工", "风电装备")
    )
    if wind_equipment:
        products.append({"name": "Rebar", "type": "futures", "role": "steel cost proxy", "prefix": "RB", "exchange": "SHFE"})
    if any(token in evidence_haystack for token in LITHIUM_MATERIAL_HINTS) and not wind_equipment:
        products.extend(_lithium_material_products())
    for keyword, hints in INDUSTRY_PRODUCT_HINTS.items():
        if wind_equipment and keyword in {"银", "黄金", "铜", "锂"}:
            continue
        if keyword in evidence_haystack:
            products.extend(hints)
    deduped = []
    seen = set()
    for product in products:
        key = (product.get("name"), product.get("type"), product.get("prefix"), product.get("exchange"))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(product)
    products = deduped

    return {
        "name": _format_value(basic.get("name")),
        "products": products,
        "spread_note": (
            "Products inferred from stock name/industry and recent filing text. Verify whether these proxies match the company's actual revenue mix."
            if products
            else "No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims."
        ),
    }


def _source_priority_rows(products: list[dict]) -> list[dict[str, str]]:
    has_livestock = any(product.get("type") == "moa_livestock" for product in products)
    has_futures = any(product.get("type") == "futures" for product in products)
    has_web_spot = any(product.get("type") == "web_spot" for product in products)
    if has_livestock:
        return [
            {
                "priority": "1 - stable hard evidence",
                "source": "official MOA monthly data + company sales announcements",
                "use": "capacity direction, realized company price/volume after parsing",
                "limitation": "monthly and usually delayed",
            },
            {
                "priority": "2 - timely proxy",
                "source": "DCE live-hog futures via Tushare",
                "use": "market-implied cycle/timing signal",
                "limitation": "proxy, not company realized spot price",
            },
            {
                "priority": "3 - optional high-frequency spot",
                "source": "authorized third-party spot datasets",
                "use": "daily regional hog price, piglet price, slaughter weight, secondary fattening",
                "limitation": "requires source permission and口径 validation before hard triggers",
            },
        ]
    rows = [
        {
            "priority": "1 - company hard evidence",
            "source": "official filings, production reports, and sales announcements",
            "use": "realized product mix, output, unit cost, and cash-flow conversion",
            "limitation": "usually delayed and may not include daily spot prices",
        }
    ]
    if has_futures:
        rows.append(
            {
                "priority": "2 - exchange market proxy",
                "source": "Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts",
                "use": "timely product-price direction, curve shape, and scenario stress",
                "limitation": "proxy, not the company's realized selling price or mine cost curve",
            }
        )
    if has_web_spot:
        rows.append(
            {
                "priority": "3 - optional authorized spot",
                "source": "whitelisted industry spot-price pages",
                "use": "cross-check product and input spreads when exact price/date/unit is parsed",
                "limitation": "source permission and口径 validation required before hard triggers",
            }
        )
    return rows


def _metal_price_source_audit_rows(products: list[dict]) -> list[dict[str, str]]:
    rows = []
    for product in products:
        name = str(product.get("name", ""))
        source = METAL_FUTURES_SOURCE_REGISTRY.get(name)
        if not source:
            continue
        rows.append(
            {
                "metal": name,
                "domestic_price_chain": (
                    f"Tushare fut_daily -> {source['domestic_exchange']} "
                    f"{source['tushare_prefix']} contracts"
                ),
                "contract_example": source["contract_example"],
                "overseas_cross_check": source["overseas_cross_checks"],
                "coverage_status": source["coverage"],
            }
        )
    return rows


def get_commodity_context(ticker: str, curr_date: str, look_back_days: int = 90) -> str:
    """Return evidence-backed commodity price context for A-share companies."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Commodity context expects A-share symbols like 000001.SZ or 600160.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    mapping = _infer_products(symbol, curr_date, look_back_days)
    products = mapping.get("products", [])
    rows = []
    has_livestock_products = any(product.get("type") == "moa_livestock" for product in products)
    if has_livestock_products:
        rows.append(_fetch_livestock_sales_announcements(symbol, curr_date, max(look_back_days, 90)))
    for product in products:
        if product.get("type") == "futures":
            rows.append(_fetch_futures_product(product, curr_date, look_back_days))
        elif product.get("type") == "web_spot":
            rows.append(_fetch_web_spot(product))
        elif product.get("type") == "moa_livestock":
            rows.append(_fetch_moa_livestock_market(product, curr_date))
        elif product.get("type") == "unavailable_key_driver":
            rows.append(_missing_key_driver_row(product))

    lines = [
        f"# Commodity and product price context for {symbol} as of {curr_date}",
        "",
        f"- Company/product map: {mapping.get('name', symbol)}",
        f"- Look-back window for futures proxies: {look_back_days} days",
        f"- Spread note: {mapping.get('spread_note', 'N/A')}",
        "",
        "## Source Priority",
        _markdown_table(pd.DataFrame(_source_priority_rows(products))),
        "",
        "## Metal Price Source Audit",
    ]
    metal_rows = _metal_price_source_audit_rows(products)
    if metal_rows:
        lines.append(_markdown_table(pd.DataFrame(metal_rows)))
    else:
        lines.append("No exchange-traded metal source audit applies to the mapped products.")
    lines.extend(
        [
            "",
            "## Evidence Table",
        ]
    )

    if rows:
        lines.append(_markdown_table(pd.DataFrame(rows)))
    else:
        lines.append("No commodity mapping is available for this ticker.")

    instructions = [
        "",
        "## Analyst Instructions",
        "- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.",
        "- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.",
        "- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.",
        "- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.",
        "- If a thesis-critical input is marked missing, treat it as neutral for direction and only as a confidence cap; it cannot prove margin deterioration or margin resilience by itself.",
    ]
    if has_livestock_products:
        instructions[3:3] = [
            "- For livestock companies, prioritize stable official/company evidence first, then use timely futures or authorized spot feeds to monitor the turn.",
            "- Treat official MOA market pages as high-confidence cycle evidence, but do not quantify the cycle unless the exact monthly/weekly series is parsed from the source.",
            "- If the current-month breeding-sow inventory has not yet been officially released, state the latest available month and keep the current month as a verification item.",
        ]
    lines.extend(instructions)
    return "\n".join(lines)
