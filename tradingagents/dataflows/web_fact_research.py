from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import html
import re
import time
import xml.etree.ElementTree as ET

import requests

from .config import get_config
from .industry_classifier import banking_profile_hint, is_banking_entity
from .tushare_a_stock import _fetch_stock_basic, _format_value, is_a_share_symbol


@dataclass(frozen=True)
class WebFactItem:
    query: str
    title: str
    source: str
    published: str
    link: str
    snippet: str
    extracted_values: str
    evidence_grade: str


_PRICE_RE = re.compile(
    r"(?:(?:[0-9]{1,3}(?:,[0-9]{3})+)|(?:[0-9]{1,6}))(?:\.\d+)?\s*"
    r"(?:\u5143/\u74f6|\u5143|\u4e07\u5143|\u4ebf\u5143|%|bp)",
    re.IGNORECASE,
)

_RSS_DATE_FORMATS = (
    "%a, %d %b %Y %H:%M:%S %Z",
    "%a, %d %b %Y %H:%M:%S GMT",
)

_MAOTAI = "\u8305\u53f0"
_FEITIAN_MAOTAI = "\u98de\u5929\u8305\u53f0"
_BAIJIU = "\u767d\u9152"
_WHOLESALE_PRICE = "\u4e00\u6279\u4ef7"
_TODAY_WINE_PRICE = "\u4eca\u65e5\u9152\u4ef7"
_ORIGINAL_CARTON = "\u539f\u7bb1"
_LOOSE_BOTTLE = "\u6563\u74f6"
_CHANNEL_INVENTORY = "\u6e20\u9053\u5e93\u5b58"
_DEALER = "\u7ecf\u9500\u5546"
_AUTO = "\u6c7d\u8f66"
_NEW_ENERGY = "\u65b0\u80fd\u6e90"
_TERMINAL_DISCOUNT = "\u7ec8\u7aef\u4f18\u60e0"
_PRICE_WAR = "\u4ef7\u683c\u6218"
_MONTHLY_SALES = "\u6708\u9500\u91cf"
_EXPORT_SALES = "\u51fa\u53e3\u9500\u91cf"
_MODEL_PRICE = "\u8f66\u578b\u4ef7\u683c"
_PRODUCT_PRICE = "\u4ea7\u54c1\u4ef7\u683c"
_ORDER_SALES_MARGIN = "\u8ba2\u5355 \u9500\u91cf \u6bdb\u5229\u7387"
_NIM = "\u51c0\u606f\u5dee"
_DEPOSIT_COST = "\u5b58\u6b3e\u6210\u672c\u7387"
_MORTGAGE_REPRICING = "\u5b58\u91cf\u623f\u8d37\u91cd\u5b9a\u4ef7"
_ASSET_QUALITY = "\u4e0d\u826f\u7387"
_PROVISION_COVERAGE = "\u62e8\u5907\u8986\u76d6\u7387"
_CET1 = "\u6838\u5fc3\u4e00\u7ea7\u8d44\u672c\u5145\u8db3\u7387"
_WEALTH_MANAGEMENT = "\u8d22\u5bcc\u7ba1\u7406"
_COPPER = "\u94dc"
_GOLD = "\u9ec4\u91d1"
_INVENTORY = "\u5e93\u5b58"
_OUTPUT = "\u4ea7\u91cf"
_UNIT_COST = "\u6210\u672c"
_MINE_PROJECT = "\u77ff\u5c71 \u9879\u76ee\u8fdb\u5c55"
_ACQUISITION = "\u5e76\u8d2d"
_SHIPPING = "\u6c34\u8fd0"
_MARINE_SHIPPING = "\u822a\u8fd0"
_FREIGHT_RATE = "\u8fd0\u4ef7"
_OIL_TANKER = "\u6cb9\u8fd0"
_TANKER = "\u6cb9\u8f6e"
_DRY_BULK = "\u5e72\u6563\u8d27"
_HORMUZ = "\u970d\u5c14\u6728\u5179"
_RESTOCKING = "\u8865\u5e93"
_BIOPHARMA = "\u751f\u7269\u533b\u836f"
_INNOVATIVE_DRUG = "\u521b\u65b0\u836f"
_CLINICAL_TRIAL = "\u4e34\u5e8a"
_PIPELINE = "\u7ba1\u7ebf"
_INDICATION = "\u9002\u5e94\u75c7"
_NMPA = "NMPA"
_FDA = "FDA"
_CDE = "CDE"
_MEDICAL_INSURANCE = "\u533b\u4fdd"
_APPROVAL = "\u83b7\u6279"
_COMMERCIALIZATION = "\u5546\u4e1a\u5316"
_CASH_FLOW = "\u73b0\u91d1\u6d41"
_CRO = "CRO"
_CDMO = "CDMO"
_GEOPOLITICAL_RISK = "\u5730\u7f18\u98ce\u9669"
_ORDER_BACKLOG = "\u8ba2\u5355"
_SOFTWARE = "\u8f6f\u4ef6"
_SAAS = "SaaS"
_SUBSCRIPTION = "\u8ba2\u9605"
_PAID_USERS = "\u4ed8\u8d39\u7528\u6237"
_ARPU = "ARPU"
_MAU = "MAU"
_CONTRACT_LIABILITY = "\u5408\u540c\u8d1f\u503a"
_RENEWAL = "\u7eed\u8d39"
_XINCHUANG = "\u4fe1\u521b"
_TENDER = "\u62db\u6807"
_AI_PAID = "AI \u4ed8\u8d39"
_WPS = "WPS"
_MEDICAL_DEVICE = "\u533b\u7597\u5668\u68b0"
_MEDICAL_EQUIPMENT = "\u533b\u7597\u8bbe\u5907"
_IVD = "IVD"
_REAGENT = "\u8bd5\u5242"
_CONSUMABLE = "\u8017\u6750"
_INSTALLED_BASE = "\u88c5\u673a"
_EQUIPMENT_RENEWAL = "\u8bbe\u5907\u66f4\u65b0"
_VBP = "\u96c6\u91c7"
_REGISTRATION_CERT = "\u6ce8\u518c\u8bc1"
_OVERSEAS_CHANNEL = "\u6d77\u5916\u6e20\u9053"
_ULTRASOUND = "\u8d85\u58f0"
_ENDOSCOPY = "\u5185\u7aa5\u955c"

_SHIPPING_NAME_HINTS = (
    "\u8f6e\u8239",
    "\u822a\u8fd0",
    "\u6d77\u80fd",
    "\u5357\u6cb9",
    "\u6d77\u63a7",
)

_BIOPHARMA_NAME_HINTS = (
    "\u767e\u6d4e",
    "\u6052\u745e",
    "\u4fe1\u8fbe",
    "\u5eb7\u65b9",
    "\u541b\u5b9e",
    "\u836f\u660e\u5eb7\u5fb7",
    "\u836f\u660e",
    "\u751f\u7269",
    "\u533b\u836f",
)

_SOFTWARE_NAME_HINTS = (
    "\u91d1\u5c71\u529e\u516c",
    "\u7528\u53cb",
    "\u6052\u751f\u7535\u5b50",
    "\u5b9d\u4fe1\u8f6f\u4ef6",
    "\u5e7f\u8054\u8fbe",
    "\u540c\u82b1\u987a",
    "\u6df1\u4fe1\u670d",
    "\u79d1\u5927\u8baf\u98de",
    "\u9053\u901a\u79d1\u6280",
)

_MEDICAL_DEVICE_NAME_HINTS = (
    "\u8fc8\u745e\u533b\u7597",
    "\u8054\u5f71\u533b\u7597",
    "\u9c7c\u8dc3\u533b\u7597",
    "\u65b0\u4ea7\u4e1a",
    "\u5b89\u56fe\u751f\u7269",
    "\u5f00\u7acb\u533b\u7597",
    "\u5357\u5fae\u533b\u5b66",
    "\u5fc3\u8109\u533b\u7597",
    "\u60e0\u6cf0\u533b\u7597",
)

_KNOWN_COMPANIES = {
    "600519.SH": ("\u8d35\u5dde\u8305\u53f0", _BAIJIU),
    "002594.SZ": ("\u6bd4\u4e9a\u8fea", _AUTO),
    "601872.SH": ("\u62db\u5546\u8f6e\u8239", _SHIPPING),
    "600026.SH": ("\u4e2d\u8fdc\u6d77\u80fd", _SHIPPING),
    "601975.SH": ("\u62db\u5546\u5357\u6cb9", _SHIPPING),
    "601919.SH": ("\u4e2d\u8fdc\u6d77\u63a7", _SHIPPING),
    "688235.SH": ("\u767e\u6d4e\u795e\u5dde", _BIOPHARMA),
    "600276.SH": ("\u6052\u745e\u533b\u836f", _INNOVATIVE_DRUG),
    "688180.SH": ("\u541b\u5b9e\u751f\u7269", _BIOPHARMA),
    "603259.SH": ("\u836f\u660e\u5eb7\u5fb7", "\u533b\u836f\u670d\u52a1"),
    "688111.SH": ("\u91d1\u5c71\u529e\u516c", _SOFTWARE),
    "600588.SH": ("\u7528\u53cb\u7f51\u7edc", _SOFTWARE),
    "600570.SH": ("\u6052\u751f\u7535\u5b50", "\u91d1\u878dIT"),
    "600845.SH": ("\u5b9d\u4fe1\u8f6f\u4ef6", "\u5de5\u4e1a\u8f6f\u4ef6"),
    "002410.SZ": ("\u5e7f\u8054\u8fbe", _SOFTWARE),
    "300033.SZ": ("\u540c\u82b1\u987a", "\u91d1\u878d\u4fe1\u606f\u670d\u52a1"),
    "300454.SZ": ("\u6df1\u4fe1\u670d", "\u7f51\u7edc\u5b89\u5168"),
    "002230.SZ": ("\u79d1\u5927\u8baf\u98de", "AI \u8f6f\u4ef6"),
    "688208.SH": ("\u9053\u901a\u79d1\u6280", "\u6c7d\u8f66\u8bca\u65ad\u8f6f\u4ef6"),
    "300760.SZ": ("\u8fc8\u745e\u533b\u7597", _MEDICAL_DEVICE),
    "688271.SH": ("\u8054\u5f71\u533b\u7597", _MEDICAL_EQUIPMENT),
    "002223.SZ": ("\u9c7c\u8dc3\u533b\u7597", _MEDICAL_DEVICE),
    "300832.SZ": ("\u65b0\u4ea7\u4e1a", "\u4f53\u5916\u8bca\u65ad"),
    "603658.SH": ("\u5b89\u56fe\u751f\u7269", "\u4f53\u5916\u8bca\u65ad"),
}


def _clean_html(text: str) -> str:
    cleaned = re.sub(r"<[^>]+>", " ", str(text or ""))
    cleaned = html.unescape(cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _safe_date(text: str) -> str:
    value = str(text or "").strip()
    for fmt in _RSS_DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return value[:10] if value else ""


def _extract_values(text: str) -> str:
    values = []
    for match in _PRICE_RE.finditer(text):
        value = match.group(0).replace(" ", "")
        if value not in values:
            values.append(value)
    return ", ".join(values[:8])


def _find_child_text(item: ET.Element, local_name: str) -> str:
    for child in item:
        if child.tag.rsplit("}", 1)[-1] == local_name:
            return child.text or ""
    return ""


def _parse_rss_response(response: requests.Response) -> ET.Element:
    response.raise_for_status()
    text = (response.text or "").lstrip()
    if not text.startswith(("<", "\ufeff<")):
        raise ValueError("search provider returned a non-RSS response")
    try:
        return ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"search provider returned unreadable RSS: {exc}") from exc


def _bing_news_rss(query: str, *, timeout: float, max_results: int) -> list[WebFactItem]:
    headers = {
        "Accept": "application/rss+xml, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.5",
        "User-Agent": "Mozilla/5.0 TradingAgents fact-check; evidence-only",
    }
    endpoints = [
        (
            "https://www.bing.com/news/search",
            {"q": query, "format": "rss", "cc": "cn", "setlang": "zh-CN"},
        ),
        (
            "https://www.bing.com/search",
            {"q": query, "format": "rss", "cc": "cn", "setlang": "zh-CN"},
        ),
    ]
    last_error: Exception | None = None
    root: ET.Element | None = None
    for url, params in endpoints:
        try:
            response = requests.get(
                url,
                params=params,
                timeout=timeout,
                headers=headers,
            )
            root = _parse_rss_response(response)
            break
        except Exception as exc:
            last_error = exc
    if root is None:
        raise RuntimeError(f"Bing RSS unavailable: {last_error}")

    rows: list[WebFactItem] = []
    for item in root.findall("./channel/item")[:max_results]:
        title = _clean_html(item.findtext("title"))
        snippet = _clean_html(item.findtext("description"))
        source = _clean_html(item.findtext("source") or _find_child_text(item, "source"))
        published = _safe_date(item.findtext("pubDate") or "")
        link = _clean_html(item.findtext("link"))
        combined = f"{title} {snippet}"
        rows.append(
            WebFactItem(
                query=query,
                title=title,
                source=source or "Bing News",
                published=published,
                link=link,
                snippet=snippet[:260],
                extracted_values=_extract_values(combined),
                evidence_grade="web-news reference; not filing/announcement-grade evidence",
            )
        )
    return rows


def _company_profile(symbol: str) -> tuple[str, str]:
    try:
        basic = _fetch_stock_basic(symbol)
    except Exception:
        basic = None
    if basic is None:
        hint = banking_profile_hint(symbol)
        return hint or _KNOWN_COMPANIES.get(symbol, (symbol, ""))
    return _format_value(basic.get("name")), _format_value(basic.get("industry"))


def _is_shipping_profile(company_name: str, industry: str) -> bool:
    return any(keyword in industry for keyword in (_SHIPPING, _MARINE_SHIPPING)) or any(
        keyword in company_name for keyword in _SHIPPING_NAME_HINTS
    )


def _is_biopharma_profile(company_name: str, industry: str) -> bool:
    return any(
        keyword in industry
        for keyword in (_BIOPHARMA, _INNOVATIVE_DRUG, "\u533b\u836f", "\u5236\u836f")
    ) or any(keyword in company_name for keyword in _BIOPHARMA_NAME_HINTS)


def _is_medical_device_profile(company_name: str, industry: str) -> bool:
    return any(
        keyword in industry
        for keyword in (
            _MEDICAL_DEVICE,
            _MEDICAL_EQUIPMENT,
            "\u533b\u7528\u8017\u6750",
            "\u4f53\u5916\u8bca\u65ad",
        )
    ) or any(keyword in company_name for keyword in _MEDICAL_DEVICE_NAME_HINTS)


def _is_software_profile(company_name: str, industry: str) -> bool:
    return any(
        keyword in industry
        for keyword in (_SOFTWARE, "\u91d1\u878dIT", "\u5de5\u4e1a\u8f6f\u4ef6", "\u7f51\u7edc\u5b89\u5168", "AI")
    ) or any(keyword in company_name for keyword in _SOFTWARE_NAME_HINTS)


def _fact_queries(symbol: str, company_name: str, industry: str) -> list[str]:
    name = company_name if company_name and company_name != "N/A" else symbol
    queries: list[str]
    if symbol == "600519.SH" or _MAOTAI in name or _BAIJIU in industry:
        queries = [
            f"{name} {_FEITIAN_MAOTAI} {_WHOLESALE_PRICE} {_TODAY_WINE_PRICE}",
            f"{name} {_FEITIAN_MAOTAI} {_ORIGINAL_CARTON} {_LOOSE_BOTTLE} {_WHOLESALE_PRICE}",
            f"{name} {_CHANNEL_INVENTORY} {_WHOLESALE_PRICE} {_DEALER}",
        ]
    elif is_banking_entity(symbol, company_name=name, industry=industry):
        queries = [
            f"{name} {_NIM} {_DEPOSIT_COST}",
            f"{name} {_ASSET_QUALITY} {_PROVISION_COVERAGE} {_CET1}",
            f"{name} {_MORTGAGE_REPRICING} {_WEALTH_MANAGEMENT}",
        ]
    elif _AUTO in industry or _NEW_ENERGY in industry or "\u6bd4\u4e9a\u8fea" in name:
        queries = [
            f"{name} {_TERMINAL_DISCOUNT} {_PRICE_WAR}",
            f"{name} {_MONTHLY_SALES} {_EXPORT_SALES}",
            f"{name} {_MODEL_PRICE} {_TERMINAL_DISCOUNT}",
        ]
    elif any(keyword in industry for keyword in (_COPPER, _GOLD, "\u77ff", "\u6709\u8272")):
        queries = [
            f"{name} {_COPPER} {_GOLD} {_PRODUCT_PRICE} {_INVENTORY}",
            f"{name} {_OUTPUT} {_UNIT_COST} {_ORDER_SALES_MARGIN}",
            f"{name} {_MINE_PROJECT} {_ACQUISITION}",
        ]
    elif _is_shipping_profile(name, industry):
        queries = [
            f"{name} VLCC TD3C TCE {_FREIGHT_RATE} {_OIL_TANKER}",
            f"{name} BDTI CTFI {_TANKER} {_FREIGHT_RATE}",
            f"{name} {_HORMUZ} {_RESTOCKING} {_OIL_TANKER}",
            f"{name} BDI BCI BPI {_DRY_BULK} {_FREIGHT_RATE}",
        ]
    elif _is_medical_device_profile(name, industry):
        queries = [
            f"{name} {_MEDICAL_DEVICE} {_EQUIPMENT_RENEWAL} {_TENDER}",
            f"{name} {_IVD} {_INSTALLED_BASE} {_REAGENT} {_CONSUMABLE}",
            f"{name} {_VBP} {_MEDICAL_DEVICE} {_PRODUCT_PRICE}",
            f"{name} {_REGISTRATION_CERT} {_FDA} CE {_OVERSEAS_CHANNEL}",
            f"{name} {_ULTRASOUND} {_ENDOSCOPY} {_MEDICAL_EQUIPMENT}",
        ]
    elif _is_biopharma_profile(name, industry):
        if "\u836f\u660e\u5eb7\u5fb7" in name or _CRO in industry or _CDMO in industry:
            queries = [
                f"{name} {_CRO} {_CDMO} {_ORDER_BACKLOG} {_GEOPOLITICAL_RISK}",
                f"{name} {_ORDER_BACKLOG} {_CASH_FLOW} {_COMMERCIALIZATION}",
                f"{name} BIOSECURE {_GEOPOLITICAL_RISK} {_CRO} {_CDMO}",
            ]
        else:
            queries = [
                f"{name} {_CLINICAL_TRIAL} {_PIPELINE} {_INDICATION} {_NMPA} {_FDA}",
                f"{name} {_CDE} {_NMPA} {_FDA} {_APPROVAL}",
                f"{name} {_MEDICAL_INSURANCE} {_COMMERCIALIZATION} {_CASH_FLOW}",
                f"{name} {_PIPELINE} {_CLINICAL_TRIAL} ORR PFS OS",
            ]
    elif _is_software_profile(name, industry):
        if "\u91d1\u5c71\u529e\u516c" in name or _WPS in name:
            queries = [
                f"{name} {_WPS} {_AI_PAID} {_ARPU} {_PAID_USERS} {_SUBSCRIPTION}",
                f"{name} {_CONTRACT_LIABILITY} {_SUBSCRIPTION} \u673a\u6784\u8ba2\u9605 \u6388\u6743",
                f"{name} {_XINCHUANG} {_TENDER} WPS 365",
                f"{name} {_WPS} AI \u4ef7\u683c {_SUBSCRIPTION} Copilot",
            ]
        else:
            queries = [
                f"{name} {_SAAS} ARR {_ARPU} {_RENEWAL} {_CONTRACT_LIABILITY}",
                f"{name} {_SUBSCRIPTION} {_PAID_USERS} {_MAU} {_AI_PAID}",
                f"{name} {_ORDER_BACKLOG} \u9879\u76ee \u9a8c\u6536 \u56de\u6b3e",
                f"{name} {_XINCHUANG} {_TENDER} {_SOFTWARE}",
            ]
    else:
        queries = [
            f"{name} {_PRODUCT_PRICE} {_CHANNEL_INVENTORY}",
            f"{name} {_ORDER_SALES_MARGIN}",
        ]

    deduped: list[str] = []
    for query in queries:
        if query not in deduped:
            deduped.append(query)
    return deduped


def _markdown_table(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "No web fact rows found."
    headers = list(rows[0].keys())
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        cells = [
            str(row.get(header, "")).replace("\n", " ").replace("|", "\\|")
            for header in headers
        ]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def _purpose_for_profile(symbol: str, company_name: str, industry: str) -> str:
    if symbol == "600519.SH" or _MAOTAI in company_name or _BAIJIU in industry:
        return (
            "fill small but thesis-critical high-frequency facts that filings and Tushare may not cover, "
            "such as baijiu wholesale prices, channel inventory, terminal discounts, and dealer commentary."
        )
    if is_banking_entity(symbol, company_name=company_name, industry=industry):
        return (
            "corroborate bank-specific high-frequency facts that filings and Tushare may lag, such as "
            "NIM/deposit-cost commentary, asset-quality updates, provision coverage, capital adequacy, "
            "fee income, and policy-rate transmission."
        )
    if _AUTO in industry or _NEW_ENERGY in industry or "\u6bd4\u4e9a\u8fea" in company_name:
        return (
            "fill high-frequency auto or new-energy facts that filings and Tushare may lag, such as "
            "terminal discounts, price-war signals, monthly sales, exports, and model-price changes."
        )
    if any(keyword in industry for keyword in (_COPPER, _GOLD, "\u77ff", "\u6709\u8272")):
        return (
            "corroborate resource-company facts that filings and Tushare may lag, such as commodity-price "
            "moves, exchange inventories, production/cost updates, mine-project progress, and M&A milestones."
        )
    if _is_shipping_profile(company_name, industry):
        return (
            "corroborate shipping-cycle facts that filings and Tushare may lag, such as VLCC TD3C/TCE, "
            "BDTI/BCTI/BDI proxies, CTFI China-import crude freight, Hormuz disruptions/reopening, "
            "restocking demand, ton-mile changes, and route-specific freight-rate commentary."
        )
    if _is_medical_device_profile(company_name, industry):
        return (
            "corroborate medical-device facts that filings and Tushare may lag, such as equipment "
            "renewal and tender cadence, installed base, IVD reagent pull-through, VBP price pressure, "
            "NMPA/FDA/CE registration, overseas channel quality, service network, and channel inventory."
        )
    if _is_biopharma_profile(company_name, industry):
        return (
            "corroborate biopharma facts that filings and Tushare may lag, such as clinical-trial "
            "status, CDE/NMPA/FDA/EMA regulatory updates, approved labels, reimbursement/pricing, "
            "commercialization, cash-runway commentary, and for CRO/CDMO names order-cycle or "
            "geopolitical-risk signals."
        )
    if _is_software_profile(company_name, industry):
        return (
            "corroborate software/SaaS facts that filings and Tushare may lag, such as ARR/ARPU, "
            "paid users, MAU conversion, renewal/churn, contract-liability structure, AI paid "
            "adoption, pricing tiers, Xinchuang tenders, project acceptance, and cash collection."
        )
    return (
        "fill small but thesis-critical high-frequency facts that filings and Tushare may not cover, "
        "such as product prices, channel inventory, sales clues, orders, and gross-margin commentary."
    )


def get_web_fact_check_context(
    ticker: str,
    curr_date: str,
    max_queries: int | None = None,
    max_results_per_query: int | None = None,
) -> str:
    """Search for simple high-frequency facts that filings/Tushare may miss."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Web fact-check context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    config = get_config()
    if not config.get("web_fact_check_enabled", True):
        return "# Web fact-check context disabled\n\n- Reason: `web_fact_check_enabled` is false."

    timeout = float(config.get("web_fact_check_timeout_sec", 6))
    max_queries = int(max_queries or config.get("web_fact_check_max_queries", 3))
    max_results_per_query = int(
        max_results_per_query or config.get("web_fact_check_max_results_per_query", 4)
    )

    company_name, industry = _company_profile(symbol)
    queries = _fact_queries(symbol, company_name, industry)[:max_queries]
    items: list[WebFactItem] = []
    errors: list[str] = []
    for query in queries:
        try:
            items.extend(
                _bing_news_rss(query, timeout=timeout, max_results=max_results_per_query)
            )
            time.sleep(0.2)
        except Exception as exc:
            errors.append(f"- {query}: {exc}")

    rows = [
        {
            "query": item.query,
            "published": item.published,
            "source": item.source,
            "title": item.title[:90],
            "values_found": item.extracted_values,
            "grade": item.evidence_grade,
            "link": item.link,
        }
        for item in items
    ]

    lines = [
        f"# Web fact-check context for {symbol} as of {curr_date}",
        "",
        f"- Company: {company_name}",
        f"- Industry: {industry or 'N/A'}",
        f"- Purpose: {_purpose_for_profile(symbol, company_name, industry)}",
        "- Evidence hierarchy: official filings/announcements > exchange Q&A > reputable news/search corroboration > market rumor. This context is search corroboration unless the source itself is official.",
        "",
        "## Search Queries",
        "\n".join(f"- {query}" for query in queries) if queries else "No configured queries.",
        "",
        "## Search Evidence",
        _markdown_table(rows),
        "",
    ]
    if errors:
        lines.extend(
            [
                "## Search Errors",
                f"- Search provider errors on {len(errors)} query path(s); treat this context as unavailable rather than evidence.",
                "",
            ]
        )
    instructions = [
        "## Analyst Instructions",
        "- Use this context to decide what must be verified next; do not treat a single web result as filing-grade evidence.",
        "- A hard trading trigger based on a web-searched price needs either multiple recent independent sources or an official/company source. Otherwise mark it as a watch item.",
        "- When sources conflict, report the range and downgrade conviction rather than choosing the most convenient number.",
    ]
    if symbol == "600519.SH" or _MAOTAI in company_name or _BAIJIU in industry:
        instructions.append(
            "- For Maotai, distinguish Feitian loose-bottle, original-carton, wholesale/reference price, retail price, and company ex-factory/guided price before using any number."
        )
    if is_banking_entity(symbol, company_name=company_name, industry=industry):
        instructions.append(
            "- For banks, do not search or reason from orders, sales volume, gross margin, channel inventory, or product-price terms. Use web facts only to corroborate NIM/deposit cost, asset quality, provision coverage, capital adequacy, fee/wealth-management, and policy-rate transmission."
        )
    if any(keyword in industry for keyword in (_COPPER, _GOLD, "\u77ff", "\u6709\u8272")):
        instructions.append(
            "- For resource companies, separate exchange commodity prices and inventories from company realized selling prices, unit costs, mine grades, and project execution evidence."
        )
    if _is_shipping_profile(company_name, industry):
        instructions.extend(
            [
                "- For shipping names, separate route-level rates (VLCC TD3C/TCE, CTFI) from broad proxies (BDTI/BCTI/BDI). Do not treat broad indices as exact voyage economics.",
                "- Treat Hormuz reopening as a two-sided mechanism: lower risk premium and faster vessel turnover can pressure rates, while restocking, queue normalization, and renewed cargo flows can support near-term demand. Require freight-rate or cargo-flow evidence before calling it bullish or bearish.",
            ]
        )
    if _is_biopharma_profile(company_name, industry):
        instructions.extend(
            [
                "- For biopharma names, separate official clinical/regulatory sources from news repetition. Use trial phase, endpoint, comparator, enrollment, and label status before turning a web result into a catalyst.",
                "- For CRO/CDMO/pharma-services names, search evidence should support order visibility, customer funding, utilization, geopolitical risk, or FCF durability; do not apply drug-owner pipeline valuation unless the company owns product economics.",
            ]
        )
    if _is_software_profile(company_name, industry):
        instructions.extend(
            [
                "- For software/SaaS names, do not use channel-inventory or generic product-price searches as thesis evidence unless the company sells hardware through channels. Route web checks to ARR/ARPU, paid users, renewal/churn, contract-liability structure, AI paid adoption, pricing tiers, tenders, project acceptance, and cash collection.",
                "- For WPS/office software, separate MAU from paid users, paid users from ARPU, AI feature launches from AI paid revenue, and contract liabilities from verified subscription renewal.",
                "- For project-heavy software, web evidence should support order backlog, implementation/acceptance timing, receivables, and collection rather than SaaS valuation shortcuts.",
            ]
        )
    lines.extend(instructions)
    return "\n".join(lines)
