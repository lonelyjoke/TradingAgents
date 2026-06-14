from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

import pandas as pd

from .config import get_config
from .industry_identity import is_telecom_operator_text
from .investor_interaction_research import fetch_investor_interaction_history
from .thematic_research import _load_financial_report_texts
from .tushare_a_stock import TushareDataError, _fetch_stock_basic, _format_value, is_a_share_symbol
from .tushare_research import _fetch_announcements, _fetch_major_news, _fetch_news_feed


@dataclass(frozen=True)
class ComputeEvidenceHit:
    source: str
    date: str
    title: str
    excerpt: str
    matched_terms: tuple[str, ...]
    evidence_grade: str


_HARD_LEASING_TERMS = (
    "\u7b97\u529b\u79df\u8d41",
    "\u7b97\u529b\u79df\u7528",
    "\u7b97\u529b\u51fa\u79df",
    "\u7b97\u529b\u670d\u52a1\u6536\u5165",
    "\u7b97\u529b\u4e1a\u52a1\u6536\u5165",
    "\u7b97\u529b\u8fd0\u8425",
    "\u667a\u7b97\u4e2d\u5fc3\u8fd0\u8425",
    "\u7b97\u529b\u4e2d\u5fc3\u8fd0\u8425",
    "GPU\u79df\u8d41",
    "GPU\u79df\u7528",
    "GPU\u51fa\u79df",
    "\u673a\u67dc\u79df\u8d41",
)
_COMPUTE_ASSET_TERMS = (
    "\u7b97\u529b\u670d\u52a1",
    "\u667a\u7b97\u4e2d\u5fc3",
    "\u7b97\u529b\u4e2d\u5fc3",
    "\u667a\u80fd\u7b97\u529b\u4e2d\u5fc3",
    "AI\u7b97\u529b",
    "\u9ad8\u6027\u80fd\u7b97\u529b",
    "\u8bad\u7ec3\u7b97\u529b",
    "\u63a8\u7406\u7b97\u529b",
)
_STRONG_TERMS = _HARD_LEASING_TERMS + _COMPUTE_ASSET_TERMS
_WEAK_TERMS = (
    "\u7b97\u529b",
    "\u667a\u7b97",
    "\u6570\u636e\u4e2d\u5fc3",
    "GPU",
    "NVIDIA",
    "\u82f1\u4f1f\u8fbe",
    "H100",
    "H800",
    "A100",
    "A800",
    "AI\u670d\u52a1\u5668",
    "\u670d\u52a1\u5668",
    "\u673a\u67dc",
    "\u6db2\u51b7",
    "IDC",
)
_MONETIZATION_TERMS = (
    "\u79df\u8d41",
    "\u79df\u7528",
    "\u51fa\u79df",
    "\u670d\u52a1\u6536\u5165",
    "\u4e1a\u52a1\u6536\u5165",
    "\u8fd0\u8425\u6536\u5165",
    "\u6708\u79df",
    "\u79df\u91d1",
    "\u4e0a\u67b6",
    "\u6295\u8fd0",
    "\u878d\u8d44\u79df\u8d41",
)
_NON_COMMITTAL_TERMS = (
    "\u4ee5\u516c\u53f8\u516c\u544a\u4e3a\u51c6",
    "\u6682\u65e0\u5e94\u62ab\u9732",
    "\u8bf7\u5173\u6ce8\u540e\u7eed\u516c\u544a",
    "\u4e0d\u4fbf\u900f\u9732",
)


def _dedupe_terms(terms: Iterable[str]) -> list[str]:
    result: list[str] = []
    for term in terms:
        clean = str(term or "").strip()
        if clean and clean not in result:
            result.append(clean)
    return result


def _terms_in_text(text: str, terms: Iterable[str]) -> list[str]:
    haystack = str(text or "")
    upper = haystack.upper()
    matched = []
    for term in terms:
        needle = term.upper()
        if needle and needle in upper:
            matched.append(term)
    return _dedupe_terms(matched)


def _clean_text(text: object) -> str:
    cleaned = re.sub(r"\s+", " ", str(text or "")).strip()
    return cleaned


def _excerpt_around_terms(text: str, terms: Iterable[str], *, radius: int = 120) -> str:
    cleaned = _clean_text(text)
    upper = cleaned.upper()
    indexes = [upper.find(term.upper()) for term in terms if term and upper.find(term.upper()) >= 0]
    if not indexes:
        return cleaned[:240]
    start = max(0, min(indexes) - radius)
    end = min(len(cleaned), min(indexes) + radius)
    excerpt = cleaned[start:end]
    if start > 0:
        excerpt = "..." + excerpt
    if end < len(cleaned):
        excerpt += "..."
    return excerpt


def _hit_grade(source: str, text: str, strong_terms: list[str], weak_terms: list[str]) -> str:
    hard_terms = [term for term in strong_terms if term in _HARD_LEASING_TERMS]
    asset_terms = [term for term in strong_terms if term in _COMPUTE_ASSET_TERMS]
    if source in {"filing", "announcement"} and hard_terms:
        return "official hard compute-leasing signal; still needs economics verification"
    if source in {"filing", "announcement"} and asset_terms:
        return "official compute/AI-infrastructure adjacency; needs leasing or operating economics"
    if source == "interaction" and strong_terms:
        if any(term in text for term in _NON_COMMITTAL_TERMS):
            return "official Q&A but non-committal; watch item only"
        return "official Q&A signal; lower than filing/announcement proof"
    if source == "news" and strong_terms:
        return "media/search corroboration; cannot trigger valuation alone"
    if weak_terms:
        return "weak adjacency signal; requires stronger official evidence"
    return "unclassified"


def _record_hit(
    *,
    source: str,
    date: object,
    title: object,
    text: object,
) -> ComputeEvidenceHit | None:
    combined = f"{title or ''}\n{text or ''}"
    strong = _terms_in_text(combined, _STRONG_TERMS)
    weak = _terms_in_text(combined, _WEAK_TERMS)
    if not strong and not weak:
        return None
    return ComputeEvidenceHit(
        source=source,
        date=_clean_text(date)[:20],
        title=_clean_text(title)[:100],
        excerpt=_excerpt_around_terms(combined, strong or weak),
        matched_terms=tuple(_dedupe_terms([*strong, *weak])),
        evidence_grade=_hit_grade(source, combined, strong, weak),
    )


def _scan_report_texts(report_texts: list[tuple[str, str]], limit: int = 12) -> list[ComputeEvidenceHit]:
    hits: list[ComputeEvidenceHit] = []
    for title, text in report_texts:
        hit = _record_hit(source="filing", date="", title=title, text=text)
        if hit:
            hits.append(hit)
    return hits[:limit]


def _scan_table_rows(
    data: pd.DataFrame | TushareDataError | None,
    *,
    source: str,
    date_cols: tuple[str, ...],
    title_cols: tuple[str, ...],
    text_cols: tuple[str, ...],
    limit: int = 12,
) -> tuple[list[ComputeEvidenceHit], str | None]:
    if isinstance(data, TushareDataError):
        return [], str(data)
    if data is None or data.empty:
        return [], None
    hits: list[ComputeEvidenceHit] = []
    for _, row in data.head(80).iterrows():
        date = next((row.get(col) for col in date_cols if col in data.columns), "")
        title = next((row.get(col) for col in title_cols if col in data.columns), "")
        text_parts = [str(row.get(col) or "") for col in text_cols if col in data.columns]
        hit = _record_hit(source=source, date=date, title=title, text=" ".join(text_parts))
        if hit:
            hits.append(hit)
    return hits[:limit], None


def _trigger_verdict(hits: list[ComputeEvidenceHit]) -> tuple[bool, str]:
    official_hits = [hit for hit in hits if hit.source in {"filing", "announcement", "interaction"}]
    official_hard = [
        hit for hit in official_hits if any(term in hit.matched_terms for term in _HARD_LEASING_TERMS)
    ]
    filing_or_announcement_hard = [
        hit for hit in official_hard if hit.source in {"filing", "announcement"}
    ]
    official_asset = [
        hit for hit in official_hits if any(term in hit.matched_terms for term in _COMPUTE_ASSET_TERMS)
    ]
    official_weak = [
        hit for hit in official_hits if any(term in hit.matched_terms for term in _WEAK_TERMS)
    ]
    monetization_hits = [
        hit
        for hit in official_hits
        if any(term in hit.excerpt for term in _MONETIZATION_TERMS)
    ]

    if filing_or_announcement_hard:
        return True, "triggered by official filing/announcement strong compute-leasing signal"
    if official_hard and monetization_hits:
        return True, "triggered by official Q&A hard compute-leasing signal plus monetization wording"
    if len(official_weak) >= 2 and monetization_hits:
        return True, "triggered by multiple official weak compute signals plus monetization wording"
    return False, "no sufficient official compute-leasing trigger"


def _markdown_table(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "No rows."
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


def _company_profile(symbol: str) -> tuple[str, str]:
    try:
        basic = _fetch_stock_basic(symbol)
    except Exception:
        basic = None
    if basic is None:
        return symbol, ""
    return _format_value(basic.get("name")), _format_value(basic.get("industry"))


def _fetch_sources(
    symbol: str,
    curr_date: str,
    *,
    financial_look_back_days: int,
    event_look_back_days: int,
    interaction_look_back_days: int,
    news_look_back_days: int,
) -> tuple[list[ComputeEvidenceHit], list[str]]:
    errors: list[str] = []
    hits: list[ComputeEvidenceHit] = []

    try:
        _, report_texts = _load_financial_report_texts(
            symbol,
            curr_date,
            look_back_days=financial_look_back_days,
        )
        hits.extend(_scan_report_texts(report_texts))
    except Exception as exc:
        errors.append(f"filing text unavailable: {exc}")

    try:
        announcements = _fetch_announcements(symbol, curr_date, event_look_back_days)
        ann_hits, ann_error = _scan_table_rows(
            announcements,
            source="announcement",
            date_cols=("ann_date", "rec_time"),
            title_cols=("title",),
            text_cols=("title",),
        )
        hits.extend(ann_hits)
        if ann_error:
            errors.append(f"announcement feed unavailable: {ann_error}")
    except Exception as exc:
        errors.append(f"announcement feed unavailable: {exc}")

    try:
        interactions = fetch_investor_interaction_history(
            symbol,
            end_date=curr_date,
            lookback_days=interaction_look_back_days,
            page_size=20,
            max_pages=3,
        )
        interaction_hits, _ = _scan_table_rows(
            interactions,
            source="interaction",
            date_cols=("answer_time", "question_time"),
            title_cols=("question",),
            text_cols=("question", "answer", "answer_class"),
        )
        hits.extend(interaction_hits)
    except Exception as exc:
        errors.append(f"investor interaction unavailable: {exc}")

    company_name, industry = _company_profile(symbol)
    terms = _dedupe_terms([symbol, symbol.split(".")[0], company_name])
    for news_source, fetcher in (
        ("major news", _fetch_major_news),
        ("news feed", _fetch_news_feed),
    ):
        try:
            data = fetcher(terms, curr_date, news_look_back_days, limit=20)
            news_hits, news_error = _scan_table_rows(
                data,
                source="news",
                date_cols=("pub_time", "datetime"),
                title_cols=("title",),
                text_cols=("title", "content", "src", "channels"),
            )
            hits.extend(news_hits)
            if news_error:
                errors.append(f"{news_source} unavailable: {news_error}")
        except Exception as exc:
            errors.append(f"{news_source} unavailable: {exc}")

    deduped: list[ComputeEvidenceHit] = []
    seen: set[tuple[str, str, str]] = set()
    for hit in hits:
        key = (hit.source, hit.date, hit.title)
        if key not in seen:
            deduped.append(hit)
            seen.add(key)
    return deduped, errors


def _render_not_applicable(symbol: str, curr_date: str, reason: str, hits: list[ComputeEvidenceHit], errors: list[str]) -> str:
    lines = [
        f"# Compute-leasing verification layer for {symbol} as of {curr_date}",
        "",
        "- Status: not_applicable",
        f"- Trigger verdict: {reason}.",
        "- Routing rule: do not inject compute-leasing analysis, valuation optionality, GPU economics, or IDC-style assumptions into this stock unless later official evidence triggers this layer.",
    ]
    if hits:
        rows = [
            {
                "source": hit.source,
                "date": hit.date,
                "title": hit.title,
                "terms": ", ".join(hit.matched_terms),
                "grade": hit.evidence_grade,
            }
            for hit in hits[:6]
        ]
        lines.extend(["", "## Weak/Non-triggering Mentions", _markdown_table(rows)])
    if errors:
        lines.extend(
            [
                "",
                "## Coverage Notes",
                "- Some A-share compute-leasing information is difficult to obtain from public feeds. Retrieval errors below are not negative evidence.",
                *[f"- {error}" for error in errors[:6]],
            ]
        )
    return "\n".join(lines)


def _render_triggered(symbol: str, curr_date: str, reason: str, hits: list[ComputeEvidenceHit], errors: list[str]) -> str:
    official_hits = [hit for hit in hits if hit.source in {"filing", "announcement", "interaction"}]
    news_hits = [hit for hit in hits if hit.source == "news"]
    rows = [
        {
            "source": hit.source,
            "date": hit.date,
            "title": hit.title,
            "terms": ", ".join(hit.matched_terms),
            "grade": hit.evidence_grade,
            "excerpt": hit.excerpt[:260],
        }
        for hit in [*official_hits[:10], *news_hits[:4]]
    ]
    lines = [
        f"# Compute-leasing verification layer for {symbol} as of {curr_date}",
        "",
        "- Status: triggered",
        f"- Trigger verdict: {reason}.",
        "- Scope: use this layer only for the compute-leasing / AI-compute business. Do not let it override evidence on the legacy core business.",
        "- Evidence hierarchy: official filings and announcements > official investor interaction > reputable media/search corroboration > market rumor. News-only mentions cannot support valuation uplift.",
        "- A-share limitation: GPU models, customer identity, lease price, utilization, power cost, and financing terms are often not fully disclosed. Missing data is a research gap, not neutral or negative proof.",
        "",
        "## Evidence Hits",
        _markdown_table(rows),
        "",
        "## Required Verification Gates",
        "- Asset gate: verify GPU/server model, quantity, delivery, ownership versus financing lease, data-center location, rack/IDC capacity, power access, PUE, network, O&M responsibility, and whether assets are actually online.",
        "- Contract gate: verify signed customer contracts, customer quality, related-party status, contract duration, minimum usage or take-or-pay clauses, pricing formula, renewal risk, receivables, prepayments, and cash collection.",
        "- Unit-economics gate: build revenue per card/rack/month, utilization, electricity, rack, bandwidth, O&M, depreciation, financing cost, gross margin, EBITDA, ROIC, and payback-period sensitivity. Do not treat revenue scale alone as value creation.",
        "- Capex/funding gate: compare procurement commitments, fixed assets, construction in progress, financing lease liabilities, guarantees, debt maturity, cash balance, and possible impairment if compute rental prices fall.",
        "- Transition-credibility gate: test whether the legacy business has real synergy with compute leasing, whether management has IDC/cloud/GPU operation experience, and whether the move looks like disciplined capital allocation or theme chasing.",
        "- SOTP gate: value legacy business, verified compute-leasing business, and unverified compute option separately. Unverified compute claims belong in scenario value or narrative option value, not base-case earnings.",
        "",
        "## Falsification Signals",
        "- Two reporting periods pass without compute-leasing revenue, order, asset-online, or cash-collection proof.",
        "- Announced assets do not arrive, are delayed, or cannot be tied to productive customer contracts.",
        "- Utilization or rental price is below the unit-economics assumption, while electricity, rack, bandwidth, depreciation, or financing costs are higher.",
        "- Receivables rise faster than compute revenue, or operating cash flow fails to follow reported growth.",
        "- The company relies on framework agreements, non-binding cooperation, or investor-interaction wording without hard contract/financial disclosure.",
        "- Shareholder reduction, pledge pressure, related-party transactions, guarantees, or refinancing pressure intensifies during the transition.",
        "",
        "## Analyst Instructions",
        "- Keep the compute-leasing thesis conditional unless the asset, contract, unit-economics, and funding gates are all supported by official evidence.",
        "- If only one or two gates are verified, cap conviction and present the compute business as evidence-limited optionality.",
        "- When external information is hard to obtain, list the exact missing fields instead of inventing GPU counts, prices, utilization, customers, or margins.",
    ]
    if errors:
        lines.extend(
            [
                "",
                "## Coverage Notes",
                "- Retrieval errors below are coverage gaps. They must not be treated as evidence against the compute-leasing thesis.",
                *[f"- {error}" for error in errors[:8]],
            ]
        )
    return "\n".join(lines)


def get_compute_leasing_context(
    ticker: str,
    curr_date: str,
    financial_look_back_days: int = 900,
    event_look_back_days: int = 365,
    interaction_look_back_days: int = 365,
    news_look_back_days: int = 180,
) -> str:
    """Return a gated A-share compute-leasing verification context.

    The module is intentionally narrow: it stays dormant unless official or
    semi-official evidence indicates a compute-leasing / AI-compute business.
    """
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return (
            "# Compute-leasing verification layer unavailable\n\n"
            f"- Reason: expected A-share symbol; got {ticker!r}."
        )

    config = get_config()
    if not config.get("compute_leasing_context_enabled", True):
        return "# Compute-leasing verification layer disabled\n\n- Status: not_applicable"

    company_name, industry = _company_profile(symbol)
    if is_telecom_operator_text(company_name, industry):
        return _render_not_applicable(
            symbol,
            curr_date,
            "telecom operator / cloud-network company; route AI/cloud compute into telecom-operator playbook unless a separately disclosed third-party compute-leasing business is proven",
            [],
            [],
        )

    hits, errors = _fetch_sources(
        symbol,
        curr_date,
        financial_look_back_days=financial_look_back_days,
        event_look_back_days=event_look_back_days,
        interaction_look_back_days=interaction_look_back_days,
        news_look_back_days=news_look_back_days,
    )
    triggered, reason = _trigger_verdict(hits)
    if not triggered:
        return _render_not_applicable(symbol, curr_date, reason, hits, errors)
    return _render_triggered(symbol, curr_date, reason, hits, errors)
