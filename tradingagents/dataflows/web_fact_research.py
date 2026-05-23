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

_KNOWN_COMPANIES = {
    "600519.SH": ("\u8d35\u5dde\u8305\u53f0", _BAIJIU),
    "002594.SZ": ("\u6bd4\u4e9a\u8fea", _AUTO),
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
        "- Purpose: fill small but thesis-critical high-frequency facts that filings and Tushare may not cover, such as baijiu wholesale prices, channel inventory, terminal discounts, bank NIM/deposit-cost commentary, asset-quality updates, and recent sales clues.",
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
    lines.extend(
        [
            "## Analyst Instructions",
            "- Use this context to decide what must be verified next; do not treat a single web result as filing-grade evidence.",
            "- A hard trading trigger based on a web-searched price needs either multiple recent independent sources or an official/company source. Otherwise mark it as a watch item.",
            "- When sources conflict, report the range and downgrade conviction rather than choosing the most convenient number.",
            "- For Maotai, distinguish Feitian loose-bottle, original-carton, wholesale/reference price, retail price, and company ex-factory/guided price before using any number.",
            "- For banks, do not search or reason from orders, sales volume, gross margin, channel inventory, or product-price terms. Use web facts only to corroborate NIM/deposit cost, asset quality, provision coverage, capital adequacy, fee/wealth-management, and policy-rate transmission.",
        ]
    )
    return "\n".join(lines)
