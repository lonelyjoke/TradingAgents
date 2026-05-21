from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha1
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Iterable

import pandas as pd
import requests

from .config import get_config
from .investor_interaction_research import fetch_investor_interaction_history
from .tushare_a_stock import (
    TushareDataError,
    _fetch_daily_basic_latest,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)
from .tushare_research import (
    _fetch_announcements,
    _fetch_major_news,
    _fetch_news_feed,
    _safe_optional_query,
)


_FINANCIAL_REPORT_TEXT_CACHE: dict[
    tuple[str, str, int], tuple[pd.DataFrame | TushareDataError, list[tuple[str, str]]]
] = {}


_FINANCIAL_REPORT_TITLE_RE = re.compile(
    r"(年度报告|半年度报告|季度报告|一季度报告|三季度报告|年报|半年报|季报|中期报告)(?!摘要)"
)
_FINANCIAL_REPORT_TITLE_RE = re.compile(
    "|".join(
        [
            r"\u5e74\u5ea6\u62a5\u544a",
            r"\u5e74\u62a5",
            r"\u534a\u5e74\u5ea6\u62a5\u544a",
            r"\u534a\u5e74\u62a5",
            r"\u4e2d\u671f\u62a5\u544a",
            r"\u4e00\u5b63\u5ea6\u62a5\u544a",
            r"\u7b2c\u4e00\u5b63\u5ea6\u62a5\u544a",
            r"\u4e09\u5b63\u5ea6\u62a5\u544a",
            r"\u7b2c\u4e09\u5b63\u5ea6\u62a5\u544a",
            r"\u5b63\u5ea6\u62a5\u544a",
            r"\u5b63\u62a5",
            r"éªžæ‘å®³éŽ¶ãƒ¥æ†¡",
            r"é—å©‚å‹¾æ´ï¸½å§¤é›å¦¡ç€›ï½…å®³éŽ¶ãƒ¥æ†¡",
            r"æ¶“â‚¬ç€›ï½…å®³éŽ¶ãƒ¥æ†¡",
            r"æ¶“å¤Šî„œæ´ï¸½å§¤é›å¦¡éªžå­˜å§¤",
            r"é—å©‚å‹¾éŽ¶îš‚ç€›ï½†å§¤",
            r"æ¶“î…Ÿæ¹¡éŽ¶ãƒ¥æ†¡",
        ]
    )
)
_FINANCIAL_REPORT_EXCLUDE_RE = re.compile(
    r"(?:\u6458\u8981|\u53d6\u6d88|\u66f4\u6b63|\u4fee\u8ba2|\u82f1\u6587|"
    r"\u5ba1\u8ba1\u62a5\u544a|\u5185\u90e8\u63a7\u5236|\u793e\u4f1a\u8d23\u4efb|ESG)"
)
_COMPANY_NAME_RE = re.compile(
    r"[\u4e00-\u9fffA-Za-z0-9（）()·]{2,40}"
    r"(?:有限责任公司|股份有限公司|有限公司|有限合伙|合伙企业)"
)
_INVESTMENT_MARKERS = (
    "参股",
    "持股",
    "投资",
    "长期股权投资",
    "其他权益工具投资",
    "其他非流动金融资产",
    "非上市权益工具投资",
)
_INVESTMENT_SECTION_HINTS = (
    "其他非流动金融资产",
    "其他权益工具投资",
    "长期股权投资",
    "非上市权益工具投资",
)
_SHORT_INVESTEE_ROW_RE = re.compile(
    r"^\s*([\u4e00-\u9fffA-Za-z0-9·（）()]{2,30})\s+"
)
_SHORT_INVESTEE_EXCLUSIONS = {
    "??????",
    "??????",
    "??????",
    "????????????",
    "????????????",
    "????????????",
    "????????????",
    "????????????",
    "????????????",
    # Generic accounting rows are not investees. Treating them as entities
    # pollutes the thematic candidate pool with balance-sheet vocabulary.
    "\u6536\u76ca",
    "\u56fa\u5b9a\u8d44\u4ea7",
    "\u5728\u5efa\u5de5\u7a0b",
    "\u65e0\u5f62\u8d44\u4ea7",
    "\u5f00\u53d1\u652f\u51fa",
    "\u957f\u671f\u80a1\u6743\u6295\u8d44",
    "\u5176\u4ed6\u975e\u6d41\u52a8\u91d1\u878d\u8d44\u4ea7",
    "\u6d3b\u52a8\u73b0\u91d1\u6d41\u5165\u5c0f\u8ba1",
    "\u6d3b\u52a8\u73b0\u91d1\u6d41\u51fa\u5c0f\u8ba1",
    "\u6d3b\u52a8\u4ea7\u751f\u7684\u73b0\u91d1\u6d41\u91cf\u51c0\u989d",
    "\u6536\u56de\u6295\u8d44\u6536\u5230\u7684\u73b0\u91d1",
    "\u53d6\u5f97\u6295\u8d44\u6536\u76ca\u6536\u5230\u7684\u73b0\u91d1",
    "\u652f\u4ed8\u7684\u73b0\u91d1",
    "\u5546\u8a89",
    "\u4f7f\u7528\u6743\u8d44\u4ea7",
    "\u6295\u8d44\u6027\u623f\u5730\u4ea7",
    "\u503a\u6743\u6295\u8d44",
    "\u5176\u4ed6\u6743\u76ca\u5de5\u5177\u6295\u8d44",
}
_BUSINESS_THEME_KEYWORDS = {
    "算力租赁": ("算力租赁", "算力服务", "智算中心", "算力中心", "GPU租赁"),
    "商业航天": ("商业航天", "火箭", "卫星互联网", "运载火箭"),
    "低空经济": ("低空经济", "无人机", "eVTOL"),
    "机器人": ("机器人", "人形机器人"),
    "储能": ("储能",),
    "氢能": ("氢能", "制氢"),
    "半导体": ("半导体", "晶圆", "芯片"),
    "数据中心": ("数据中心", "IDC"),
}
_NEWS_CATALYST_KEYWORDS = (
    "IPO",
    "上市",
    "受理",
    "招股说明书",
    "商业化",
    "投产",
    "订单",
    "签约",
    "并购",
    "挂牌",
    "获得批文",
)
_COMPANY_NAME_PREFIXES = (
    "公司持有",
    "公司参股",
    "公司投资",
    "市场关注",
    "市场热议",
    "关注",
    "持有",
    "参股",
    "投资于",
    "投资",
)
_AMOUNT_RE = re.compile(
    r"(?<!\d)(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(?:\s*(亿元|万元|元))?"
)
_BUSINESS_QUANTIFICATION_MARKERS = (
    "收入",
    "利润",
    "订单",
    "合同",
    "客户",
    "营业收入",
    "业务收入",
    "毛利",
    "现金流",
)
_RELIABLE_FILING_THEME_RULES: dict[str, dict[str, tuple[str, ...]]] = {
    "order-ramp": {
        "aliases": ("\u5728\u624b\u8ba2\u5355", "\u65b0\u589e\u8ba2\u5355", "\u8ba2\u5355\u50a8\u5907", "\u4e2d\u6807", "\u5408\u540c\u8d1f\u503a"),
        "proof": ("\u8ba2\u5355", "\u5408\u540c", "\u8425\u6536", "\u6536\u5165", "\u4ea4\u4ed8"),
    },
    "new-product-commercialization": {
        "aliases": ("\u65b0\u4ea7\u54c1", "\u65b0\u4e1a\u52a1", "\u91cf\u4ea7", "\u5546\u4e1a\u5316", "\u8ba4\u8bc1"),
        "proof": ("\u8ba2\u5355", "\u6536\u5165", "\u8425\u6536", "\u5ba2\u6237", "\u91cf\u4ea7", "\u4ea4\u4ed8"),
    },
    "overseas-expansion": {
        "aliases": ("\u6d77\u5916", "\u5883\u5916", "\u56fd\u9645\u5e02\u573a", "\u51fa\u53e3"),
        "proof": ("\u8ba2\u5355", "\u6536\u5165", "\u8425\u6536", "\u5ba2\u6237", "\u4ea4\u4ed8"),
    },
    "capacity-release": {
        "aliases": ("\u6295\u4ea7", "\u8fbe\u4ea7", "\u4ea7\u80fd", "\u4ea7\u7ebf"),
        "proof": ("\u6536\u5165", "\u8425\u6536", "\u8ba2\u5355", "\u4ea4\u4ed8", "\u5229\u6da6"),
    },
}
_NEGATIVE_MONETIZATION_MARKERS = (
    "\u5c1a\u672a\u5f62\u6210",
    "\u672a\u5f62\u6210",
    "\u5c1a\u672a",
    "\u6682\u65e0",
    "\u5c1a\u65e0",
)
_FILING_THEME_READS = {
    "order-ramp": {
        "story_read": "demand visibility is improving",
        "proof_needed": "watch conversion into delivery, revenue, and cash collection",
    },
    "new-product-commercialization": {
        "story_read": "new product may be moving from R&D into monetization",
        "proof_needed": "watch customer adoption, orders, and gross margin",
    },
    "overseas-expansion": {
        "story_read": "geographic expansion can widen the earnings runway",
        "proof_needed": "watch order quality, localization, and profitability",
    },
    "capacity-release": {
        "story_read": "supply capability may be unlocking future revenue",
        "proof_needed": "watch utilization, sell-through, and return on capital",
    },
}
_CROSS_SOURCE_THEME_ALIASES = {
    "commercial-space": ("\u5546\u4e1a\u822a\u5929", "\u822a\u5929\u519b\u5de5", "\u84dd\u7bad\u822a\u5929"),
    "compute-power": ("\u7b97\u529b", "\u7b97\u7535\u534f\u540c", "\u6570\u636e\u4e2d\u5fc3", "\u80fd\u6e90\u4e92\u8054\u7f51"),
    "ai-meteorology": ("AI\u6c14\u8c61", "\u6c14\u8c61\u5927\u6a21\u578b", "\u5929\u6c14\u9884\u62a5"),
    "green-methanol": ("\u7eff\u8272\u7532\u9187", "\u7eff\u9187", "\u7532\u9187"),
    "buyback-shareholder-return": ("\u56de\u8d2d", "\u6ce8\u9500", "\u5e02\u503c\u7ba1\u7406"),
    "capital-allocation": ("\u957f\u671f\u80a1\u6743\u6295\u8d44", "\u4ef7\u503c\u6295\u8d44", "\u6295\u8d44\u6536\u76ca"),
}


@dataclass(frozen=True)
class ThemeCandidate:
    name: str
    kind: str
    origin: str
    evidence: str


def _compact_text(value: str, limit: int = 180) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text[:limit] + ("..." if len(text) > limit else "")


def _normalize_company_name(value: str) -> str:
    name = str(value or "").strip()
    for prefix in _COMPANY_NAME_PREFIXES:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    return name.strip()


def _financial_report_announcements(
    symbol: str, curr_date: str, look_back_days: int
) -> pd.DataFrame | TushareDataError:
    result = _fetch_announcements(symbol, curr_date, look_back_days)
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    if "title" not in result.columns:
        return pd.DataFrame()
    titles = result["title"].fillna("").astype(str)
    is_report = titles.str.contains(_FINANCIAL_REPORT_TITLE_RE, regex=True)
    is_excluded = titles.str.contains(_FINANCIAL_REPORT_EXCLUDE_RE, regex=True)
    reports = result[is_report & ~is_excluded].copy()
    return reports.sort_values("ann_date", ascending=False).head(4)


def _cache_dir() -> Path:
    root = Path(get_config()["data_cache_dir"]).expanduser()
    path = root / "disclosures"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _download_disclosure(url: str) -> Path | None:
    if not url:
        return None
    digest = sha1(url.encode("utf-8")).hexdigest()
    pdf_path = _cache_dir() / f"{digest}.pdf"
    if pdf_path.exists():
        return pdf_path
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 TradingAgents thematic-research"},
            timeout=20,
        )
        response.raise_for_status()
        pdf_path.write_bytes(response.content)
        return pdf_path
    except Exception:
        return None


def _extract_pdf_text(pdf_path: Path) -> str:
    txt_path = pdf_path.with_suffix(".txt")
    if txt_path.exists():
        return txt_path.read_text(encoding="utf-8", errors="ignore")

    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        return ""

    try:
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        subprocess.run(
            [pdftotext, "-layout", str(pdf_path), str(tmp_path)],
            check=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
        text = tmp_path.read_text(encoding="utf-8", errors="ignore")
        txt_path.write_text(text, encoding="utf-8")
        tmp_path.unlink(missing_ok=True)
        return text
    except Exception:
        return ""


def _load_financial_report_texts(
    symbol: str, curr_date: str, look_back_days: int = 900
) -> tuple[pd.DataFrame | TushareDataError, list[tuple[str, str]]]:
    cache_key = (symbol, curr_date, look_back_days)
    cached = _FINANCIAL_REPORT_TEXT_CACHE.get(cache_key)
    if cached is not None:
        cached_reports, cached_texts = cached
        reports_copy = (
            cached_reports.copy()
            if isinstance(cached_reports, pd.DataFrame)
            else cached_reports
        )
        return reports_copy, list(cached_texts)

    reports = _financial_report_announcements(symbol, curr_date, look_back_days)
    if isinstance(reports, TushareDataError) or reports is None or reports.empty:
        _FINANCIAL_REPORT_TEXT_CACHE[cache_key] = (
            reports.copy() if isinstance(reports, pd.DataFrame) else reports,
            [],
        )
        return reports, []

    texts: list[tuple[str, str]] = []
    for _, row in reports.iterrows():
        pdf_path = _download_disclosure(str(row.get("url") or ""))
        if pdf_path is None:
            continue
        text = _extract_pdf_text(pdf_path)
        if text:
            title = str(row.get("title") or row.get("ann_date") or "financial report")
            texts.append((title, text))
    _FINANCIAL_REPORT_TEXT_CACHE[cache_key] = (reports.copy(), list(texts))
    return reports, texts


def _extract_financial_candidates(report_texts: Iterable[tuple[str, str]]) -> list[ThemeCandidate]:
    candidates: dict[tuple[str, str], ThemeCandidate] = {}
    for title, text in report_texts:
        investment_section_window = 0
        for raw_line in str(text or "").splitlines():
            line = _compact_text(raw_line, limit=240)
            if not line:
                continue

            has_investment_marker = any(marker in line for marker in _INVESTMENT_MARKERS)
            if any(marker in line for marker in _INVESTMENT_SECTION_HINTS):
                investment_section_window = 12
            if has_investment_marker:
                for match in _COMPANY_NAME_RE.findall(line):
                    normalized = _normalize_company_name(match)
                    if not _is_valid_asset_revaluation_candidate(normalized, line):
                        continue
                    key = (normalized, "asset-revaluation")
                    candidates[key] = ThemeCandidate(
                        name=normalized,
                        kind="asset-revaluation",
                        origin="financial report",
                        evidence=f"{title}: {line}",
                    )

            if has_investment_marker or investment_section_window > 0:
                short_name = _extract_short_investee_name(line)
                if short_name:
                    key = (short_name, "asset-revaluation")
                    candidates.setdefault(
                        key,
                        ThemeCandidate(
                            name=short_name,
                            kind="asset-revaluation",
                            origin="financial report",
                            evidence=f"{title}: {line}",
                        ),
                    )

            for theme_name, aliases in _BUSINESS_THEME_KEYWORDS.items():
                if any(alias in line for alias in aliases):
                    key = (theme_name, "business-realization")
                    candidates.setdefault(
                        key,
                        ThemeCandidate(
                            name=theme_name,
                            kind="business-realization",
                            origin="financial report",
                            evidence=f"{title}: {line}",
                        ),
                    )
            investment_section_window = max(0, investment_section_window - 1)
    return list(candidates.values())


def _extract_reliable_filing_theme_candidates(
    report_texts: Iterable[tuple[str, str]],
) -> list[ThemeCandidate]:
    """Extract filing-backed bull themes only when monetization evidence exists."""
    candidates: dict[tuple[str, str], ThemeCandidate] = {}
    for title, text in report_texts:
        for raw_line in str(text or "").splitlines():
            line = _compact_text(raw_line, limit=240)
            if not line:
                continue
            if any(marker in line for marker in _NEGATIVE_MONETIZATION_MARKERS):
                continue
            has_quantification = (
                _extract_reported_amount_cny(line) is not None
                or bool(re.search(r"\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?%", line))
                or any(marker in line for marker in _BUSINESS_QUANTIFICATION_MARKERS)
            )
            if not has_quantification:
                continue
            for theme_name, rule in _RELIABLE_FILING_THEME_RULES.items():
                aliases = rule["aliases"]
                proof_markers = rule["proof"]
                if any(alias in line for alias in aliases) and any(
                    marker in line for marker in proof_markers
                ):
                    key = (theme_name, "business-realization")
                    candidates.setdefault(
                        key,
                        ThemeCandidate(
                            name=theme_name,
                            kind="business-realization",
                            origin="financial report",
                            evidence=f"{title}: {line}",
                        ),
                    )
    return list(candidates.values())


def _filing_theme_read(candidate: ThemeCandidate) -> dict[str, str]:
    return _FILING_THEME_READS.get(
        candidate.name,
        {
            "story_read": "filing-backed operating theme",
            "proof_needed": "watch monetization, timing, and materiality",
        },
    )


def _canonical_theme_name(value: str | None) -> str | None:
    text = str(value or "").strip()
    if not text:
        return None
    if text in _CROSS_SOURCE_THEME_ALIASES:
        return text
    for theme_name, aliases in _CROSS_SOURCE_THEME_ALIASES.items():
        if any(alias in text for alias in aliases):
            return theme_name
    return text


def _build_cross_source_validation_rows(
    reliable_filing_themes: Iterable[ThemeCandidate],
    news_candidates: Iterable[ThemeCandidate],
    concept_memberships: pd.DataFrame | TushareDataError,
    interaction_records: pd.DataFrame | TushareDataError,
) -> list[dict[str, str]]:
    """Corroborate themes across filing, news, concept, and interaction sources."""
    source_map: dict[str, set[str]] = {}
    hard_evidence: dict[str, bool] = {}

    for candidate in reliable_filing_themes:
        theme = _canonical_theme_name(candidate.name)
        if not theme:
            continue
        source_map.setdefault(theme, set()).add("filing")
        hard_evidence[theme] = True

    for candidate in news_candidates:
        theme = _canonical_theme_name(candidate.name)
        if theme:
            source_map.setdefault(theme, set()).add("news")

    if not isinstance(concept_memberships, TushareDataError) and concept_memberships is not None:
        for _, row in concept_memberships.iterrows():
            theme = _canonical_theme_name(str(row.get("concept_name") or ""))
            if theme:
                source_map.setdefault(theme, set()).add("concept")

    if not isinstance(interaction_records, TushareDataError) and interaction_records is not None:
        for _, row in interaction_records.iterrows():
            theme = _canonical_theme_name(str(row.get("theme") or ""))
            answer_class = str(row.get("answer_class") or "")
            if theme and theme != "unclassified":
                source_map.setdefault(theme, set()).add("interaction")
                if answer_class == "substantive":
                    hard_evidence.setdefault(theme, False)

    rows: list[dict[str, str]] = []
    for theme, sources in sorted(source_map.items()):
        source_count = len(sources)
        has_filing = "filing" in sources
        has_hard_evidence = hard_evidence.get(theme, False)
        if has_hard_evidence and source_count >= 2:
            cross_read = "hard catalyst with cross-source corroboration"
            suggested_tier = "tier-1 hard catalyst"
            upgrade_path = "eligible for core review if materiality is sufficient"
        elif has_hard_evidence:
            cross_read = "latent hard catalyst; economic bridge exists but fetched corroboration is thin"
            suggested_tier = "tier-1 pending diligence"
            upgrade_path = "seek a second independent source or direct milestone"
        elif source_count >= 2:
            cross_read = "corroborated narrative; multiple sources agree but economics remain unproven"
            suggested_tier = "tier-2 corroborated narrative"
            upgrade_path = "seek filing monetization evidence before core valuation"
        else:
            cross_read = "single-source narrative"
            suggested_tier = "tier-3 narrative option"
            upgrade_path = "collect independent corroboration"
        rows.append(
            {
                "theme": theme,
                "source_families": ", ".join(sorted(sources)),
                "source_count": str(source_count),
                "hard_evidence": "yes" if has_hard_evidence else "no",
                "cross_source_read": cross_read,
                "suggested_tier": suggested_tier,
                "upgrade_path": upgrade_path,
            }
        )
    return rows


def _extract_short_investee_name(line: str) -> str | None:
    """Extract short investee names from row-like filing lines."""
    if _extract_reported_amount_cny(line) is None:
        return None
    match = _SHORT_INVESTEE_ROW_RE.search(line)
    if not match:
        return None
    candidate = _normalize_company_name(match.group(1))
    if not _is_valid_asset_revaluation_candidate(candidate, line):
        return None
    return candidate


def _looks_like_accounting_row_name(value: str) -> bool:
    text = str(value or "")
    accounting_tokens = (
        "\u8d44\u4ea7",
        "\u8d1f\u503a",
        "\u73b0\u91d1",
        "\u6536\u76ca",
        "\u635f\u5931",
        "\u5e94\u6536",
        "\u5e94\u4ed8",
        "\u6298\u65e7",
        "\u51cf\u503c",
        "\u516c\u5141\u4ef7\u503c",
        "\u7efc\u5408\u6536\u76ca",
        "\u501f\u6b3e",
        "\u5408\u540c\u8d1f\u503a",
        "\u9884\u4ed8\u6b3e",
        "\u5e94\u6536\u6b3e\u9879",
        "\u5b58\u8d27",
        "\u6295\u8d44\u6027\u623f\u5730\u4ea7",
        "\u957f\u671f\u80a1\u6743\u6295\u8d44",
        "\u5176\u4ed6\u6743\u76ca\u5de5\u5177\u6295\u8d44",
        "\u5408\u8ba1",
        "\u5ba2\u6237",
        "\u4f9b\u5e94\u5546",
        "\u6301\u80a1",
        "\u81ea\u7136\u4eba",
        "\u80a1\u672c",
        "\u8d44\u672c\u516c\u79ef",
        "\u672a\u5206\u914d\u5229\u6da6",
        "\u5c11\u6570\u80a1\u4e1c\u6743\u76ca",
    )
    return any(token in text for token in accounting_tokens)


_ASSET_CANDIDATE_EXCLUSION_TOKENS = (
    "\u77ed\u671f\u501f\u6b3e",
    "\u957f\u671f\u501f\u6b3e",
    "\u501f\u6b3e",
    "\u5408\u8ba1",
    "\u5ba2\u6237",
    "\u4f9b\u5e94\u5546",
    "\u6301\u80a1",
    "\u81ea\u7136\u4eba",
    "\u9884\u7b97\u62e8\u6b3e",
    "\u6295\u8d44\u6027\u623f\u5730\u4ea7",
    "\u6027\u623f\u5730\u4ea7",
    "\u6743\u76ca\u5de5\u5177",
    "\u503a\u6743\u6295\u8d44",
    "\u5bf9\u5b50\u516c\u53f8\u6295\u8d44",
    "\u5bf9\u8054\u8425\u4f01\u4e1a",
    "\u8d26\u9762\u4ef7\u503c",
    "\u53d7\u8ba9\u65b9",
    "\u4e3b\u627f\u9500\u5546",
    "\u4fdd\u8350\u4eba",
    "\u672c\u6b21\u53d1\u884c",
    "\u8bc9\u8bbc\u516c\u544a",
    "\u8fd8\u9700\u83b7\u5f97",
    "\u8d44\u4ea7",
    "\u8d1f\u503a",
    "\u73b0\u91d1\u6d41",
    "\u6536\u5165",
    "\u6210\u672c",
    "\u8d39\u7528",
)


def _is_valid_asset_revaluation_candidate(candidate: str, evidence: str = "") -> bool:
    text = str(candidate or "").strip()
    if not text or len(text) < 2 or len(text) > 40:
        return False
    if text in _SHORT_INVESTEE_EXCLUSIONS:
        return False
    if _looks_like_accounting_row_name(text):
        return False
    if any(token in text for token in _ASSET_CANDIDATE_EXCLUSION_TOKENS):
        return False
    if re.fullmatch(r"[\d.,%\uff08\uff09()\-\s]+", text):
        return False
    return True


def _iter_news_texts(*frames: pd.DataFrame | TushareDataError) -> Iterable[str]:
    for frame in frames:
        if isinstance(frame, TushareDataError) or frame is None or frame.empty:
            continue
        for _, row in frame.iterrows():
            parts = [row.get("title"), row.get("content")]
            text = " ".join(str(part or "") for part in parts)
            if text.strip():
                yield text


def _extract_news_candidates(*frames: pd.DataFrame | TushareDataError) -> list[ThemeCandidate]:
    candidates: dict[tuple[str, str], ThemeCandidate] = {}
    for text in _iter_news_texts(*frames):
        snippet = _compact_text(text)
        for theme_name, aliases in _BUSINESS_THEME_KEYWORDS.items():
            if any(alias in text for alias in aliases):
                key = (theme_name, "business-realization")
                candidates.setdefault(
                    key,
                    ThemeCandidate(
                        name=theme_name,
                        kind="business-realization",
                        origin="news",
                        evidence=snippet,
                    ),
                )
        for match in _COMPANY_NAME_RE.findall(text):
            normalized = _normalize_company_name(match)
            if not _is_valid_asset_revaluation_candidate(normalized, text):
                continue
            key = (normalized, "asset-revaluation")
            candidates.setdefault(
                key,
                ThemeCandidate(
                    name=normalized,
                    kind="asset-revaluation",
                    origin="news",
                    evidence=snippet,
                ),
            )
    return list(candidates.values())


def _candidate_aliases(candidate: ThemeCandidate) -> tuple[str, ...]:
    if candidate.name in _BUSINESS_THEME_KEYWORDS:
        return _BUSINESS_THEME_KEYWORDS[candidate.name]
    if candidate.name in _RELIABLE_FILING_THEME_RULES:
        return _RELIABLE_FILING_THEME_RULES[candidate.name]["aliases"]
    return (candidate.name,)


def _candidate_in_reports(candidate: ThemeCandidate, report_texts: Iterable[tuple[str, str]]) -> bool:
    aliases = _candidate_aliases(candidate)
    texts = list(report_texts)
    if any(any(alias in text for alias in aliases) for _, text in texts):
        return True

    if candidate.kind != "asset-revaluation":
        return False

    report_company_names = {
        _normalize_company_name(match)
        for _, text in texts
        for match in _COMPANY_NAME_RE.findall(text)
    }
    return any(
        candidate.name.endswith(report_name) or report_name.endswith(candidate.name)
        for report_name in report_company_names
        if report_name
    )


def _candidate_news_matches(
    candidate: ThemeCandidate,
    news_frames: Iterable[pd.DataFrame | TushareDataError],
) -> list[str]:
    aliases = _candidate_aliases(candidate)
    matches = []
    for text in _iter_news_texts(*news_frames):
        if any(alias in text for alias in aliases):
            matches.append(_compact_text(text))
    return matches[:3]


def _news_has_catalyst(texts: Iterable[str]) -> bool:
    return any(any(keyword in text for keyword in _NEWS_CATALYST_KEYWORDS) for text in texts)


def _build_candidate_table(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "No candidates found."
    return _markdown_table(pd.DataFrame(rows))


def _portfolio_pattern_summary(
    financial_candidates: Iterable[ThemeCandidate],
    report_texts: Iterable[tuple[str, str]],
) -> dict[str, str]:
    """Detect when investees are part of a repeatable capital-allocation pattern.

    A single investee can be an isolated optionality item. Multiple verified
    investees plus filing evidence of realized exits or investment income deserve
    a different analyst question: is management demonstrating repeatable capital
    allocation skill that the market may be underpricing?
    """
    candidates = [
        candidate
        for candidate in financial_candidates
        if candidate.kind == "asset-revaluation"
    ]
    joined_text = "\n".join(text for _, text in report_texts)
    realization_markers = (
        "\u6295\u8d44\u6536\u76ca",  # investment income
        "\u5904\u7f6e\u957f\u671f\u80a1\u6743\u6295\u8d44",  # disposal of LT equity investment
        "\u5904\u7f6e\u91d1\u878d\u8d44\u4ea7",  # disposal of financial assets
        "\u51fa\u552e\u80a1\u6743",  # sale of equity
        "\u516c\u5141\u4ef7\u503c\u53d8\u52a8\u6536\u76ca",  # FV gains
    )
    realized_signal = any(marker in joined_text for marker in realization_markers)
    if len(candidates) >= 2 and realized_signal:
        read = (
            "repeat-investor pattern worth explicit review: filings show multiple "
            "verified investees plus realized-investment language"
        )
    elif len(candidates) >= 2:
        read = (
            "portfolio optionality exists, but realized track record is not yet "
            "verified from the filing text"
        )
    elif candidates:
        read = "single-investee optionality; do not infer broad investing skill from one asset"
    else:
        read = "no verified investee pattern found"
    return {
        "verified_investee_count": str(len(candidates)),
        "realized_investment_signal": "yes" if realized_signal else "no",
        "pattern_read": read,
    }


def _combine_news_frames(*frames: pd.DataFrame | TushareDataError) -> pd.DataFrame | TushareDataError:
    data_frames = [
        frame
        for frame in frames
        if isinstance(frame, pd.DataFrame) and frame is not None and not frame.empty
    ]
    if not data_frames:
        first_error = next(
            (frame for frame in frames if isinstance(frame, TushareDataError)),
            None,
        )
        return first_error if first_error is not None else pd.DataFrame()
    combined = pd.concat(data_frames, ignore_index=True)
    if "title" in combined.columns:
        combined = combined.drop_duplicates(subset=["title"], keep="first")
    return combined


def _filter_news_by_entity_terms(
    frame: pd.DataFrame | TushareDataError,
    entity_terms: Iterable[str],
) -> pd.DataFrame | TushareDataError:
    """Keep only news that actually mentions the target company or verified investees."""
    if isinstance(frame, TushareDataError) or frame is None or frame.empty:
        return frame
    terms = [str(term).strip() for term in entity_terms if str(term).strip()]
    if not terms:
        return frame.iloc[0:0].copy()

    def row_matches(row: pd.Series) -> bool:
        text = " ".join(str(row.get(col) or "") for col in ("title", "content"))
        return any(term in text for term in terms)

    return frame[frame.apply(row_matches, axis=1)].reset_index(drop=True)


def _extract_reported_amount_cny(text: str) -> float | None:
    """Best-effort amount parser for filing evidence lines.

    Financial-report tables often collapse into a single text line after PDF
    extraction. Prefer explicitly unit-tagged figures, but also accept large
    comma-separated bare numbers because A-share reports commonly print raw CNY
    values in tables without repeating the unit on every row.
    """
    values: list[float] = []
    for raw_value, unit in _AMOUNT_RE.findall(str(text or "")):
        numeric = float(raw_value.replace(",", ""))
        if unit == "亿元":
            numeric *= 100_000_000
        elif unit == "万元":
            numeric *= 10_000
        elif unit == "元":
            numeric *= 1
        elif "," not in raw_value and numeric < 10_000:
            # Avoid treating years, percentages, or small row numbers as money.
            continue
        values.append(numeric)
    return max(values) if values else None


def _format_cny(value: float | None) -> str:
    if value is None:
        return "not separately disclosed"
    if abs(value) >= 100_000_000:
        return f"{value / 100_000_000:.2f} 亿元"
    if abs(value) >= 10_000:
        return f"{value / 10_000:.2f} 万元"
    return f"{value:.0f} 元"


def _safe_market_cap_cny(symbol: str, curr_date: str) -> float | None:
    try:
        daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
    except Exception:
        return None
    if daily_basic is None:
        return None
    total_mv = daily_basic.get("total_mv")
    try:
        return float(total_mv) * 10_000
    except (TypeError, ValueError):
        return None


def _has_business_quantification(candidate: ThemeCandidate) -> bool:
    return any(marker in candidate.evidence for marker in _BUSINESS_QUANTIFICATION_MARKERS)


def _valuation_treatment(
    candidate: ThemeCandidate,
    reported_amount_cny: float | None,
    market_cap_cny: float | None,
    has_news_catalyst: bool,
) -> tuple[str, str, str]:
    """Return treatment, bull angle, and bear check for valuation debate."""
    if candidate.kind == "asset-revaluation":
        ratio = (
            reported_amount_cny / market_cap_cny
            if reported_amount_cny is not None and market_cap_cny
            else None
        )
        if reported_amount_cny is None:
            return (
                "verified asset; do not quantify until holding value is disclosed",
                "Could add optionality once a realizable asset value becomes observable.",
                "Challenge ownership value, liquidity, dilution, lock-up, and whether any uplift is actually realizable.",
            )
        if ratio is None:
            return (
                "quantifiable asset; compare against market cap before using in valuation",
                "Potential SOTP/NAV uplift exists if the investee reprices.",
                "Do not let an absolute number sound large without testing listed-company materiality.",
            )
        if ratio >= 0.01 and has_news_catalyst:
            return (
                "eligible for SOTP/NAV review",
                "A verified, material asset with a live catalyst can support upside beyond core operations.",
                "Stress realizability, haircut assumptions, timing, and double-counting versus current book value.",
            )
        if ratio >= 0.01:
            return (
                "material asset; keep in valuation watchlist pending catalyst",
                "Material verified ownership may become an upside lever if a catalyst emerges.",
                "Without a catalyst, current carrying value may already be the cleanest anchor.",
            )
        return (
            "verified but immaterial to core valuation",
            "Useful as optionality, not as the spine of the thesis.",
            "Argue that even full revaluation would not move listed-company value enough to matter.",
        )

    if _has_business_quantification(candidate):
        return (
            "eligible for scenario valuation, not automatic core valuation",
            "Verified commercialization evidence can justify upside scenarios if revenue/profit contribution scales.",
            "Test whether disclosed contribution is recurring, profitable, and large enough versus the existing business.",
        )
    return (
        "real theme, not yet separately quantifiable",
        "Shows strategic direction and may deserve qualitative optionality.",
        "Keep it out of core valuation until revenue, profit, orders, or cash-flow contribution is separately evidenced.",
    )


def _catalyst_tier(
    candidate: ThemeCandidate,
    reported_amount_cny: float | None,
    market_cap_cny: float | None,
    has_news_catalyst: bool,
) -> tuple[str, str]:
    """Classify verified themes into hard vs soft catalysts."""
    if candidate.kind == "asset-revaluation":
        ratio = (
            reported_amount_cny / market_cap_cny
            if reported_amount_cny is not None and market_cap_cny
            else None
        )
        if ratio is not None and ratio >= 0.01 and has_news_catalyst:
            return ("tier-1 hard catalyst", "core/SOTP valuation eligible")
        if ratio is not None and ratio >= 0.01:
            return ("tier-2 soft catalyst", "scenario valuation / watchlist")
        return ("tier-2 soft catalyst", "qualitative optionality only")
    if _has_business_quantification(candidate):
        return ("tier-1 hard catalyst", "scenario-to-core bridge eligible")
    return ("tier-2 soft catalyst", "scenario support only")


def _build_valuation_rows(
    financial_candidates: Iterable[ThemeCandidate],
    news_candidates: Iterable[ThemeCandidate],
    report_texts: Iterable[tuple[str, str]],
    major_news: pd.DataFrame | TushareDataError,
    news_feed: pd.DataFrame | TushareDataError,
    market_cap_cny: float | None,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    verified_candidates = list(financial_candidates)
    for candidate in news_candidates:
        if _candidate_in_reports(candidate, report_texts):
            verified_candidates.append(candidate)

    for candidate in verified_candidates:
        key = (candidate.name, candidate.kind)
        if key in seen:
            continue
        seen.add(key)
        news_matches = _candidate_news_matches(candidate, [major_news, news_feed])
        reported_amount_cny = _extract_reported_amount_cny(candidate.evidence)
        treatment, bull_angle, bear_check = _valuation_treatment(
            candidate,
            reported_amount_cny,
            market_cap_cny,
            _news_has_catalyst(news_matches),
        )
        ratio = (
            reported_amount_cny / market_cap_cny
            if reported_amount_cny is not None and market_cap_cny
            else None
        )
        rows.append(
            {
                "candidate": candidate.name,
                "kind": candidate.kind,
                "catalyst_tier": _catalyst_tier(
                    candidate,
                    reported_amount_cny,
                    market_cap_cny,
                    _news_has_catalyst(news_matches),
                )[0],
                "valuation_weight": _catalyst_tier(
                    candidate,
                    reported_amount_cny,
                    market_cap_cny,
                    _news_has_catalyst(news_matches),
                )[1],
                "reported_value": _format_cny(reported_amount_cny),
                "vs_listed_mkt_cap": f"{ratio:.1%}" if ratio is not None else "N/A",
                "valuation_treatment": treatment,
                "bull_angle": bull_angle,
                "bear_check": bear_check,
            }
        )
    return rows


def _build_narrative_option_rows(
    news_candidates: Iterable[ThemeCandidate],
    report_texts: Iterable[tuple[str, str]],
    major_news: pd.DataFrame | TushareDataError,
    news_feed: pd.DataFrame | TushareDataError,
) -> list[dict[str, str]]:
    """Keep unverified themes visible as low-weight A-share narrative optionality."""
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for candidate in news_candidates:
        key = (candidate.name, candidate.kind)
        if key in seen or _candidate_in_reports(candidate, report_texts):
            continue
        seen.add(key)
        matches = _candidate_news_matches(candidate, [major_news, news_feed])
        rows.append(
            {
                "candidate": candidate.name,
                "kind": candidate.kind,
                "catalyst_tier": "tier-3 narrative option",
                "valuation_weight": "small imagination premium only",
                "news_mentions": str(len(matches) or 1),
                "evidence": _compact_text(candidate.evidence, 120),
                "discipline": "do not enter core valuation before filing verification",
            }
        )
    return rows


def _fetch_legacy_concept_memberships(symbol: str) -> pd.DataFrame | TushareDataError:
    """Fetch Tushare's 5000-point legacy concept memberships for one stock."""
    result = _safe_optional_query(
        "concept_detail",
        ts_code=symbol,
        fields="id,concept_name,ts_code,name,in_date,out_date",
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return result
    keep = [
        col
        for col in ["id", "concept_name", "ts_code", "name", "in_date", "out_date"]
        if col in result.columns
    ]
    data = result[keep].copy()
    if "out_date" in data.columns:
        active = data["out_date"].isna() | (data["out_date"].astype(str).str.strip() == "")
        if active.any():
            data = data[active]
    return data.drop_duplicates().sort_values(
        [col for col in ["concept_name", "in_date"] if col in data.columns]
    )


def _build_concept_membership_rows(
    concept_memberships: pd.DataFrame | TushareDataError,
) -> list[dict[str, str]]:
    """Render concept memberships as low-weight narrative options."""
    if (
        isinstance(concept_memberships, TushareDataError)
        or concept_memberships is None
        or concept_memberships.empty
    ):
        return []
    rows = []
    for _, row in concept_memberships.iterrows():
        rows.append(
            {
                "candidate": str(row.get("concept_name") or "").strip(),
                "kind": "concept-membership",
                "catalyst_tier": "tier-3 narrative option",
                "valuation_weight": "small imagination premium only",
                "source": "tushare concept_detail",
                "evidence": f"concept_id={row.get('id', 'N/A')}; in_date={row.get('in_date', 'N/A')}",
            }
        )
    return rows


def _interaction_candidate_label(row: pd.Series) -> str:
    text = f"{row.get('question') or ''} {row.get('answer') or ''}"
    theme = str(row.get("theme") or "official-interaction")
    if "\u7b97\u529b" in text and "\u79df\u8d41" in text:
        return "\u7b97\u529b\u79df\u8d41/\u667a\u4e91\u8ba1\u7b97"
    if "\u667a\u4e91\u8ba1\u7b97" in text:
        return "\u667a\u4e91\u8ba1\u7b97"
    if "\u7b97\u529b" in text or "\u6570\u636e\u4e2d\u5fc3" in text:
        return "\u7b97\u529b/\u6570\u636e\u4e2d\u5fc3"
    if "\u7f51\u7edc\u5de5\u7a0b" in text:
        return "\u7f51\u7edc\u5de5\u7a0b\u5efa\u8bbe"
    return theme


def _interaction_evidence(row: pd.Series) -> str:
    question = str(row.get("question") or "").strip()
    answer = str(row.get("answer") or "").strip()
    if question and answer:
        return _compact_text(f"Q: {question} / A: {answer}", 220)
    return _compact_text(answer or question, 220)


def _build_interaction_option_rows(
    interaction_records: pd.DataFrame | TushareDataError,
) -> list[dict[str, str]]:
    """Render official interaction answers as low-weight narrative options."""
    if (
        isinstance(interaction_records, TushareDataError)
        or interaction_records is None
        or interaction_records.empty
    ):
        return []

    rows: list[dict[str, str]] = []
    for _, row in interaction_records.iterrows():
        answer_class = str(row.get("answer_class") or "").strip()
        answer = str(row.get("answer") or "").strip()
        theme = str(row.get("theme") or "unclassified")
        if answer_class in {"", "unanswered", "unavailable"} or not answer:
            continue
        if answer_class == "non-committal" and theme == "unclassified":
            continue
        if answer_class == "non-committal":
            catalyst_tier = "tier-3 investor concern / unverified narrative"
            valuation_weight = "no valuation credit; diligence red flag until filings clarify economics"
        else:
            catalyst_tier = "tier-3 narrative option"
            valuation_weight = "small imagination premium only"
        rows.append(
            {
                "candidate": _interaction_candidate_label(row),
                "kind": "investor-interaction",
                "catalyst_tier": catalyst_tier,
                "valuation_weight": valuation_weight,
                "source": str(row.get("source_type") or "official interaction"),
                "evidence": _interaction_evidence(row),
                "story_read": str(row.get("story_read") or ""),
                "proof_needed": str(row.get("proof_needed") or ""),
                "credibility": str(row.get("credibility") or ""),
            }
        )
    return rows


def get_thematic_catalyst_context(
    ticker: str,
    curr_date: str,
    financial_look_back_days: int = 900,
    news_look_back_days: int = 180,
) -> str:
    """Cross-check A-share thematic candidates between filings and news.

    The system intentionally uses two directions:
    1) financial-report candidates that are then checked for recent news catalysts;
    2) news-discovered candidates that must be validated against financial reports
       before they may influence valuation.
    """
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Thematic catalyst research expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    company_name = _format_value(basic.get("name")) if basic is not None else symbol
    reports, report_texts = _load_financial_report_texts(
        symbol, curr_date, financial_look_back_days
    )
    news_terms = [symbol, symbol.split(".")[0], company_name]
    major_news = _fetch_major_news(news_terms, curr_date, news_look_back_days)
    news_feed = _fetch_news_feed(news_terms, curr_date, news_look_back_days)
    market_cap_cny = _safe_market_cap_cny(symbol, curr_date)

    financial_candidates = _extract_financial_candidates(report_texts)
    reliable_filing_themes = _extract_reliable_filing_theme_candidates(report_texts)
    financial_candidates = financial_candidates + reliable_filing_themes
    investee_terms = sorted(
        {
            candidate.name
            for candidate in financial_candidates
            if candidate.kind == "asset-revaluation"
            and _is_valid_asset_revaluation_candidate(candidate.name, candidate.evidence)
        }
    )
    investee_major_news = (
        _fetch_major_news(investee_terms, curr_date, news_look_back_days)
        if investee_terms
        else pd.DataFrame()
    )
    investee_news_feed = (
        _fetch_news_feed(investee_terms, curr_date, news_look_back_days)
        if investee_terms
        else pd.DataFrame()
    )
    combined_major_news = _combine_news_frames(major_news, investee_major_news)
    combined_news_feed = _combine_news_frames(news_feed, investee_news_feed)
    entity_terms = [*news_terms, *investee_terms]
    filtered_major_news = _filter_news_by_entity_terms(combined_major_news, entity_terms)
    filtered_news_feed = _filter_news_by_entity_terms(combined_news_feed, entity_terms)
    news_candidates = _extract_news_candidates(filtered_major_news, filtered_news_feed)
    concept_memberships = _fetch_legacy_concept_memberships(symbol)
    try:
        interaction_records = fetch_investor_interaction_history(
            symbol,
            end_date=curr_date,
            lookback_days=news_look_back_days,
            max_pages=10,
        )
    except Exception as exc:
        interaction_records = TushareDataError(str(exc))

    financial_rows = []
    for candidate in financial_candidates:
        matches = _candidate_news_matches(candidate, [filtered_major_news, filtered_news_feed])
        financial_rows.append(
            {
                "candidate": candidate.name,
                "kind": candidate.kind,
                "financial_report_evidence": _compact_text(candidate.evidence, 120),
                "recent_news_match": "yes" if matches else "no",
                "catalyst_signal": "yes" if _news_has_catalyst(matches) else "no",
            }
        )

    reliable_theme_rows = []
    for candidate in reliable_filing_themes:
        theme_read = _filing_theme_read(candidate)
        reliable_theme_rows.append(
            {
                "candidate": candidate.name,
                "kind": candidate.kind,
                "financial_report_evidence": _compact_text(candidate.evidence, 120),
                "reliability_gate": "filing-backed + monetization evidence",
                "story_read": theme_read["story_read"],
                "proof_needed": theme_read["proof_needed"],
            }
        )

    news_rows = []
    for candidate in news_candidates:
        verified = _candidate_in_reports(candidate, report_texts)
        news_rows.append(
            {
                "candidate": candidate.name,
                "kind": candidate.kind,
                "news_evidence": _compact_text(candidate.evidence, 120),
                "financial_report_validation": "verified" if verified else "not verified",
                "valuation_status": "eligible for review" if verified else "reject pending filing evidence",
            }
        )

    valuation_rows = _build_valuation_rows(
        financial_candidates,
        news_candidates,
        report_texts,
        filtered_major_news,
        filtered_news_feed,
        market_cap_cny,
    )
    portfolio_pattern = _portfolio_pattern_summary(financial_candidates, report_texts)
    narrative_option_rows = _build_narrative_option_rows(
        news_candidates,
        report_texts,
        filtered_major_news,
        filtered_news_feed,
    )
    concept_membership_rows = _build_concept_membership_rows(concept_memberships)
    interaction_option_rows = _build_interaction_option_rows(interaction_records)
    cross_source_rows = _build_cross_source_validation_rows(
        reliable_filing_themes,
        news_candidates,
        concept_memberships,
        interaction_records,
    )

    report_titles = []
    if isinstance(reports, TushareDataError):
        report_titles.append(f"Financial report lookup unavailable: {reports}")
    elif reports is None or reports.empty:
        report_titles.append("No recent annual/half-year report announcements found.")
    else:
        for _, row in reports.iterrows():
            report_titles.append(
                f"- {row.get('ann_date', 'N/A')}: {row.get('title', 'N/A')}"
            )

    extraction_note = (
        "Financial-report text extraction succeeded."
        if report_texts
        else "Financial-report text extraction unavailable or no readable report text was retrieved."
    )

    lines = [
        f"# Thematic catalyst cross-check for {symbol} as of {curr_date}",
        "",
        f"- Company: {company_name}",
        f"- Financial-report look-back: {financial_look_back_days} days",
        f"- News look-back: {news_look_back_days} days",
        f"- Investee news terms: {', '.join(investee_terms) if investee_terms else 'none'}",
        f"- Extraction status: {extraction_note}",
        "",
        "## Financial Reports Considered",
        *report_titles,
        "",
        "## Filing-Origin Candidates -> News Catalyst Check",
        _build_candidate_table(financial_rows),
        "",
        "## Reliable Filing-Origin Bull Themes",
        _build_candidate_table(reliable_theme_rows),
        "",
        "## News-Origin Candidates -> Filing Validation",
        _build_candidate_table(news_rows),
        "",
        "## Thematic Valuation Bridge",
        _build_candidate_table(valuation_rows),
        "",
        "## Narrative Optionality Watchlist",
        _build_candidate_table(
            narrative_option_rows + concept_membership_rows + interaction_option_rows
        ),
        "",
        "## Cross-Source Theme Validation",
        _build_candidate_table(cross_source_rows),
        "",
        "## Portfolio Pattern Check",
        _build_candidate_table([portfolio_pattern]),
        "",
        "## Analyst Instructions",
        "- Treat filing-origin candidates as the first-pass candidate pool for investee IPOs, asset listings, and verified new-business lines.",
        "- Treat filing-origin operating themes as bull support only when the filing itself contains a believable economic bridge such as orders, revenue, delivery, customers, commercialization, or capacity release; reject bare buzzwords without monetization evidence.",
        "- Treat news-origin candidates as unverified until annual or half-year report text supports the same investee, asset, or business line.",
        "- A candidate may influence valuation only after filing verification plus a clear economic transmission path, timetable, and materiality check.",
        "- Use a three-tier ladder: tier-1 hard catalysts can enter core/SOTP valuation; tier-2 soft catalysts can support scenario upside or probability; tier-3 narrative options from news, interaction, concept linkage, or media association may justify only a small imagination premium until filings verify them.",
        "- Keep economic hardness separate from evidence completeness. If a filing-backed theme has a real monetization bridge but the fetched corroboration is thin, mark it as tier-1 pending diligence / latent hard catalyst instead of demoting it to pure narrative or pretending proof is complete.",
        "- Asset-revaluation themes may enter SOTP/NAV only when ownership value is disclosed, material versus listed-company market cap, and realizability is discussed.",
        "- After reviewing single investees, ask a second-level question: is there a repeatable capital-allocation pattern? If filings show multiple verified investees plus realized exits, investment income, or fair-value gains over time, discuss whether management's first-level investing capability itself is a durable bull factor rather than treating each asset as an isolated anecdote.",
        "- Business-realization themes may enter core valuation only when filings disclose monetization evidence such as revenue, profit, orders, or cash-flow contribution; otherwise keep them as qualitative optionality.",
        "- If report text extraction is unavailable, say so explicitly and do not pretend that news-only themes were verified.",
    ]
    return "\n".join(lines)
