from __future__ import annotations

from dataclasses import dataclass
from html import unescape
import re
from typing import Any

import pandas as pd
import requests

from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _markdown_table,
    is_a_share_symbol,
)


@dataclass(frozen=True)
class PolicySource:
    title: str
    issuer: str
    publish_date: str
    policy_level: str
    url: str


OFFICIAL_POLICY_SOURCES: tuple[PolicySource, ...] = (
    PolicySource(
        title="中共中央关于制定国民经济和社会发展第十五个五年规划的建议",
        issuer="中国政府网",
        publish_date="2025-10-28",
        policy_level="national-plan",
        url="https://www.gov.cn/gongbao/2025/issue_12386/202511/content_7047415.html",
    ),
    PolicySource(
        title="中共中央 国务院关于加快经济社会发展全面绿色转型的意见",
        issuer="中国政府网",
        publish_date="2024-08-11",
        policy_level="national-direction",
        url="https://www.gov.cn/zhengce/202408/content_6967663.htm",
    ),
)

INDUSTRY_POLICY_SOURCES: dict[str, tuple[PolicySource, ...]] = {
    "renewable-energy": (
        PolicySource(
            title="“十四五”可再生能源发展规划",
            issuer="国家发展改革委、国家能源局等",
            publish_date="2022-06-01",
            policy_level="industry-plan",
            url="https://www.ndrc.gov.cn/xxgk/zcfb/ghwb/202206/t20220601_1326719_ext.html",
        ),
    ),
    "digital-economy": (
        PolicySource(
            title="数字中国建设整体布局规划",
            issuer="中国政府网",
            publish_date="2023-02-27",
            policy_level="industry-plan",
            url="https://www.gov.cn/zhengce/2023-02/27/content_5743484.htm",
        ),
    ),
    "future-industries": (
        PolicySource(
            title="工业和信息化部等七部门关于推动未来产业创新发展的实施意见",
            issuer="中国政府网",
            publish_date="2024-01-29",
            policy_level="industry-plan",
            url="https://www.gov.cn/zhengce/zhengceku/202401/content_6929021.htm",
        ),
    ),
    "hydrogen": (
        PolicySource(
            title="氢能产业发展中长期规划（2021—2035年）",
            issuer="国家发展改革委、国家能源局",
            publish_date="2022-03-23",
            policy_level="industry-plan",
            url="https://www.ndrc.gov.cn/xxgk/zcfb/ghwb/202203/t20220323_1320038_ext.html",
        ),
    ),
    "livestock-hog": (
        PolicySource(
            title="生猪产能调控实施方案（2024年修订）",
            issuer="农业农村部",
            publish_date="2024-03-01",
            policy_level="industry-plan",
            url="https://www.moa.gov.cn/govpublic/xmsyj/202403/t20240304_6450572.htm",
        ),
    ),
}

INDUSTRY_MATCH_RULES: dict[str, tuple[str, ...]] = {
    "renewable-energy": ("风电", "光伏", "电气设备", "新能源", "发电设备"),
    "digital-economy": ("软件服务", "互联网", "通信设备", "计算机", "数据中心"),
    "future-industries": ("商业航天", "低空经济", "机器人", "人工智能", "高端装备"),
    "hydrogen": ("氢能", "绿色甲醇", "绿醇", "甲醇", "燃料电池"),
    "livestock-hog": ("生猪", "猪肉", "畜牧", "养殖", "饲料"),
}


POLICY_THEME_RULES: dict[str, dict[str, Any]] = {
    "renewable-energy": {
        "aliases": (
            "风电",
            "海上风电",
            "分散式风电",
            "光伏",
            "新能源",
            "可再生能源",
            "非化石能源",
            "清洁能源",
            "新型能源体系",
            "绿色转型",
            "绿色低碳",
        ),
        "market_read": "supports multi-year demand visibility for clean-energy equipment and infrastructure",
        "bull_use": "argue the company sits inside a policy-backed demand pool",
        "bear_use": "test whether support expands volume but not necessarily margin or returns",
    },
    "commercial-space": {
        "aliases": ("商业航天", "航天"),
        "market_read": "signals strategic support for a future-industry lane",
        "bull_use": "treat as policy-backed optionality when the company has real exposure",
        "bear_use": "keep valuation weight low unless monetization or ownership is verified",
    },
    "ai-and-digital": {
        "aliases": ("人工智能", "数字经济", "算力", "数据要素"),
        "market_read": "supports expansion of digital infrastructure and AI-related demand",
        "bull_use": "support adjacency themes linked to compute, data-center, or AI demand",
        "bear_use": "distinguish ecosystem demand from company-specific monetization",
    },
    "advanced-manufacturing": {
        "aliases": ("高端装备", "先进制造业", "智能制造", "新质生产力"),
        "market_read": "supports industrial upgrading and premium manufacturing lanes",
        "bull_use": "reinforce durability for firms with real product leadership",
        "bear_use": "challenge whether the company is a beneficiary or only adjacent",
    },
    "green-fuels": {
        "aliases": ("氢能", "绿色燃料", "绿色甲醇", "可再生能源制氢", "绿色低碳"),
        "market_read": "supports decarbonization pathways beyond electricity",
        "bull_use": "support new-business TAM expansion when commercialization exists",
        "bear_use": "require offtake, utilization, and revenue before valuation uplift",
    },
    "livestock-capacity": {
        "aliases": ("生猪产能", "能繁母猪", "产能调控", "基础产能", "绿色区域"),
        "market_read": "supports disciplined capacity management in the hog industry",
        "bull_use": "argue that sector supply discipline can improve cycle visibility for efficient producers",
        "bear_use": "test whether policy merely stabilizes supply without guaranteeing company-specific margin",
    },
    "food-security": {
        "aliases": ("粮食安全", "重要农产品", "畜产品", "稳产保供", "农产品供给"),
        "market_read": "signals strategic support for domestic agricultural supply resilience",
        "bull_use": "frame efficient leaders as beneficiaries of long-run strategic relevance",
        "bear_use": "separate policy importance from shareholder returns and pricing power",
    },
}


def _clean_policy_html(html: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", html or "", flags=re.I | re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", unescape(text)).strip()


def _fetch_policy_documents(
    sources: tuple[PolicySource, ...] = OFFICIAL_POLICY_SOURCES,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    client = session or requests.Session()
    rows = []
    for source in sources:
        text = ""
        retrieval_status = "ok"
        fetch_error = ""
        try:
            response = client.get(
                source.url,
                timeout=20,
                headers={"User-Agent": "Mozilla/5.0 TradingAgents policy-research"},
            )
            response.raise_for_status()
            text = _clean_policy_html(response.text)
        except Exception as exc:
            retrieval_status = "failed"
            fetch_error = str(exc)
        rows.append(
            {
                "title": source.title,
                "issuer": source.issuer,
                "publish_date": source.publish_date,
                "policy_level": source.policy_level,
                "url": source.url,
                "retrieval_status": retrieval_status,
                "fetch_error": fetch_error,
                "text": text,
            }
        )
    return pd.DataFrame(rows)


def _company_terms(symbol: str) -> list[str]:
    basic = _fetch_stock_basic(symbol)
    terms = [symbol, symbol.split(".")[0]]
    if basic is not None:
        for col in ("name", "industry"):
            value = basic.get(col)
            if value is not None and not pd.isna(value):
                terms.append(str(value))
    return [term for i, term in enumerate(terms) if term and term not in terms[:i]]


def _select_industry_policy_sources(company_terms: list[str]) -> tuple[PolicySource, ...]:
    selected: list[PolicySource] = []
    joined = " ".join(company_terms)
    for policy_bucket, keywords in INDUSTRY_MATCH_RULES.items():
        if any(keyword in joined for keyword in keywords):
            selected.extend(INDUSTRY_POLICY_SOURCES.get(policy_bucket, ()))
    return tuple(selected)


def _policy_source_frame(sources: tuple[PolicySource, ...]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "title": source.title,
                "issuer": source.issuer,
                "publish_date": source.publish_date,
                "policy_level": source.policy_level,
                "url": source.url,
            }
            for source in sources
        ]
    )


def _infer_policy_relevance(
    policy_docs: pd.DataFrame,
    extra_terms: list[str] | None = None,
) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    if policy_docs is None or policy_docs.empty:
        return pd.DataFrame()
    extra_terms = extra_terms or []
    for _, doc in policy_docs.iterrows():
        text = " ".join(
            part
            for part in [
                str(doc.get("title") or ""),
                str(doc.get("text") or ""),
            ]
            if part
        )
        for theme, rule in POLICY_THEME_RULES.items():
            matched = [alias for alias in rule["aliases"] if alias in text]
            if not matched:
                continue
            rows.append(
                {
                    "policy_theme": theme,
                    "matched_terms": "、".join(matched),
                    "source_title": str(doc["title"]),
                    "issuer": str(doc["issuer"]),
                    "publish_date": str(doc["publish_date"]),
                    "policy_level": str(doc["policy_level"]),
                    "company_term_overlap": "、".join(
                        term for term in extra_terms if term and term in text
                    ),
                    "market_read": str(rule["market_read"]),
                    "bull_use": str(rule["bull_use"]),
                    "bear_use": str(rule["bear_use"]),
                }
            )
    return pd.DataFrame(rows)


def get_policy_planning_context(ticker: str, curr_date: str) -> str:
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Policy-planning context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    company_terms = _company_terms(symbol)
    try:
        national_docs = _fetch_policy_documents()
        industry_sources = _select_industry_policy_sources(company_terms)
        industry_docs = (
            _fetch_policy_documents(industry_sources)
            if industry_sources
            else pd.DataFrame()
        )
        docs = pd.concat([national_docs, industry_docs], ignore_index=True)
        matches = _infer_policy_relevance(docs, company_terms)
    except Exception as exc:
        docs = pd.DataFrame(
            [
                {
                    "title": "policy retrieval unavailable",
                    "issuer": "official-source fetch failed",
                    "publish_date": curr_date,
                    "policy_level": "unavailable",
                    "url": "",
                    "text": str(exc),
                }
            ]
        )
        matches = pd.DataFrame()

    lines = [
        f"# Policy-planning context for {symbol} as of {curr_date}",
        "",
        "## Official Policy Sources",
        _markdown_table(
            docs[
                [
                    col
                    for col in [
                        "title",
                        "issuer",
                        "publish_date",
                        "policy_level",
                        "retrieval_status",
                        "url",
                    ]
                    if col in docs.columns
                ]
            ]
        ),
        "",
        "## Routed Industry Policy Sources",
        _markdown_table(_policy_source_frame(industry_sources)),
        "",
        "## Policy Theme Mapping",
        _markdown_table(matches),
        "",
        "## Industry Policy Coverage",
        "- National-plan documents judge strategic direction; industry-plan documents judge whether the company's own lane has more concrete policy support.",
        "- A matched industry file is higher-confidence evidence for sector demand slope than a generic market narrative, but it still does not prove company-specific orders or profitability.",
        "",
        "## Analyst Instructions",
        "- Use national plans and official policy files to judge long-run demand slope, priority support, and strategic direction; do not confuse policy support with immediate earnings.",
        "- Bulls should explain whether the company has a real transmission path from policy to orders, pricing, capacity, or valuation.",
        "- Bears should ask whether policy expands industry volume without improving company economics, whether competition captures the benefit, and whether the company is only adjacent rather than a true beneficiary.",
        "- Treat policy files as strong evidence for direction and TAM, weaker evidence for company-specific monetization until filings or contracts confirm the bridge.",
    ]
    return "\n".join(lines)
