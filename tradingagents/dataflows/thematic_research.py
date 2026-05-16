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
)


_FINANCIAL_REPORT_TITLE_RE = re.compile(
    r"(年度报告|半年度报告|季度报告|一季度报告|三季度报告|年报|半年报|季报|中期报告)(?!摘要)"
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
    "项目",
    "合计",
    "小计",
    "期初余额",
    "期末余额",
    "本期增加",
    "本期减少",
    "账面价值",
    "公允价值",
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
    reports = result[titles.str.contains(_FINANCIAL_REPORT_TITLE_RE, regex=True)].copy()
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
    reports = _financial_report_announcements(symbol, curr_date, look_back_days)
    if isinstance(reports, TushareDataError) or reports is None or reports.empty:
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
                    if not normalized:
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


def _extract_short_investee_name(line: str) -> str | None:
    """Extract short investee names from row-like filing lines."""
    if _extract_reported_amount_cny(line) is None:
        return None
    match = _SHORT_INVESTEE_ROW_RE.search(line)
    if not match:
        return None
    candidate = _normalize_company_name(match.group(1))
    if candidate in _SHORT_INVESTEE_EXCLUSIONS or len(candidate) < 2:
        return None
    return candidate


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
            if not normalized:
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
                "reported_value": _format_cny(reported_amount_cny),
                "vs_listed_mkt_cap": f"{ratio:.1%}" if ratio is not None else "N/A",
                "valuation_treatment": treatment,
                "bull_angle": bull_angle,
                "bear_check": bear_check,
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
    investee_terms = sorted(
        {
            candidate.name
            for candidate in financial_candidates
            if candidate.kind == "asset-revaluation"
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
    news_candidates = _extract_news_candidates(combined_major_news, combined_news_feed)

    financial_rows = []
    for candidate in financial_candidates:
        matches = _candidate_news_matches(candidate, [combined_major_news, combined_news_feed])
        financial_rows.append(
            {
                "candidate": candidate.name,
                "kind": candidate.kind,
                "financial_report_evidence": _compact_text(candidate.evidence, 120),
                "recent_news_match": "yes" if matches else "no",
                "catalyst_signal": "yes" if _news_has_catalyst(matches) else "no",
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
        combined_major_news,
        combined_news_feed,
        market_cap_cny,
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
        "## News-Origin Candidates -> Filing Validation",
        _build_candidate_table(news_rows),
        "",
        "## Thematic Valuation Bridge",
        _build_candidate_table(valuation_rows),
        "",
        "## Analyst Instructions",
        "- Treat filing-origin candidates as the first-pass candidate pool for investee IPOs, asset listings, and verified new-business lines.",
        "- Treat news-origin candidates as unverified until annual or half-year report text supports the same investee, asset, or business line.",
        "- A candidate may influence valuation only after filing verification plus a clear economic transmission path, timetable, and materiality check.",
        "- Asset-revaluation themes may enter SOTP/NAV only when ownership value is disclosed, material versus listed-company market cap, and realizability is discussed.",
        "- Business-realization themes may enter core valuation only when filings disclose monetization evidence such as revenue, profit, orders, or cash-flow contribution; otherwise keep them as qualitative optionality.",
        "- If report text extraction is unavailable, say so explicitly and do not pretend that news-only themes were verified.",
    ]
    return "\n".join(lines)
