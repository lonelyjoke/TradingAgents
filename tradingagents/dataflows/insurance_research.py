"""Insurance-specific verification context for A-share insurers."""

from __future__ import annotations

import re
from dataclasses import dataclass

import pandas as pd

from .filing_research import _load_financial_report_texts
from .industry_identity import is_insurance_text
from .tushare_a_stock import (
    _fetch_daily_basic_latest,
    _fetch_fina_indicator,
    _fetch_stock_basic,
    _fetch_stock_basic_universe,
    _format_value,
    _markdown_table,
)


INSURANCE_SYMBOL_HINTS = frozenset(
    {
        "601318.SH",  # Ping An
        "601601.SH",  # CPIC
        "601336.SH",  # New China Life
        "601628.SH",  # China Life
        "601319.SH",  # PICC
    }
)

INSURANCE_TERMS = (
    "\u4fdd\u9669",
    "\u5bff\u9669",
    "\u8d22\u9669",
    "\u4ea7\u9669",
    "\u5065\u5eb7\u9669",
    "\u5185\u542b\u4ef7\u503c",
    "\u65b0\u4e1a\u52a1\u4ef7\u503c",
    "NBV",
    "EV",
)

INSURANCE_EVIDENCE_TERMS = (
    "\u65b0\u4e1a\u52a1\u4ef7\u503c",
    "\u65b0\u4e1a\u52a1\u4ef7\u503c\u7387",
    "NBV",
    "\u5185\u542b\u4ef7\u503c",
    "\u8425\u8fd0\u5229\u6da6",
    "\u5269\u4f59\u8fb9\u9645",
    "CSM",
    "NCSM",
    "\u4ee3\u7406\u4eba",
    "\u94f6\u4fdd",
    "\u7eed\u671f",
    "\u9000\u4fdd",
    "\u7efc\u5408\u6210\u672c\u7387",
    "\u8d54\u4ed8\u7387",
    "\u8d39\u7528\u7387",
    "\u51c0\u6295\u8d44\u6536\u76ca\u7387",
    "\u603b\u6295\u8d44\u6536\u76ca\u7387",
    "\u7efc\u5408\u6295\u8d44\u6536\u76ca\u7387",
    "\u507f\u4ed8\u80fd\u529b",
    "\u8d44\u4ea7\u914d\u7f6e",
)

MISSING_INSURANCE_ITEMS = (
    "P/EV and embedded-value growth",
    "NBV growth and NBV margin by channel",
    "agent count, agent productivity, bancassurance contribution, persistency and surrender",
    "solvency adequacy and payout constraint",
    "net / total / comprehensive investment yield and duration mismatch",
    "P&C COR split into loss ratio and expense ratio",
    "CSM/NCSM movement and insurance-service-result bridge",
)


@dataclass(frozen=True)
class InsuranceProfile:
    status: str
    reason: str
    company_name: str
    industry: str


def _safe_text(value: object) -> str:
    return str(value or "").strip()


def _is_insurance_profile(symbol: str, basic: pd.Series | None) -> InsuranceProfile:
    company_name = _format_value(basic.get("name")) if basic is not None else ""
    industry = _format_value(basic.get("industry")) if basic is not None else ""
    text = f"{symbol} {company_name} {industry}"
    if is_insurance_text(symbol):
        return InsuranceProfile("triggered", "curated A-share insurer ticker", company_name, industry)
    if is_insurance_text("", text):
        return InsuranceProfile(
            "triggered",
            "company name or Tushare industry contains insurance terms",
            company_name,
            industry,
        )
    return InsuranceProfile("not_applicable", "no insurance ticker, name, or industry trigger", company_name, industry)


def _numeric(value: object) -> float | None:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return None if pd.isna(parsed) else float(parsed)


def _latest_indicator_row(indicators: pd.DataFrame) -> pd.Series | None:
    if indicators is None or indicators.empty:
        return None
    rows = indicators.copy()
    if "end_date" in rows.columns:
        rows = rows.sort_values("end_date", ascending=False)
    return rows.iloc[0]


def _financial_snapshot(
    daily_basic: pd.Series | None,
    indicators: pd.DataFrame,
) -> pd.DataFrame:
    row = _latest_indicator_row(indicators)
    payload = {
        "pe_ttm": None if daily_basic is None else _numeric(daily_basic.get("pe_ttm")),
        "pb": None if daily_basic is None else _numeric(daily_basic.get("pb")),
        "dv_ttm": None if daily_basic is None else _numeric(daily_basic.get("dv_ttm")),
        "roe_annual": None if row is None else _numeric(row.get("roe_annual")),
        "roe_latest": None if row is None else _numeric(row.get("roe")),
        "netprofit_yoy": None if row is None else _numeric(row.get("netprofit_yoy")),
        "debt_to_assets": None if row is None else _numeric(row.get("debt_to_assets")),
    }
    return pd.DataFrame([payload])


def _extract_insurance_filing_evidence(
    report_texts: list[tuple[str, str]],
    *,
    max_rows: int = 14,
) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for title, text in report_texts:
        compact = re.sub(r"\s+", " ", _safe_text(text))
        if not compact:
            continue
        for term in INSURANCE_EVIDENCE_TERMS:
            for match in re.finditer(re.escape(term), compact, flags=re.IGNORECASE):
                start = max(0, match.start() - 90)
                end = min(len(compact), match.end() + 160)
                excerpt = compact[start:end].strip()
                key = (term.lower(), excerpt[:100])
                if key in seen:
                    continue
                seen.add(key)
                rows.append(
                    {
                        "lens": _lens_for_term(term),
                        "term": term,
                        "source": title,
                        "evidence": excerpt,
                    }
                )
                if len(rows) >= max_rows:
                    return pd.DataFrame(rows)
    return pd.DataFrame(rows)


def _lens_for_term(term: str) -> str:
    if term in {"NBV", "\u65b0\u4e1a\u52a1\u4ef7\u503c", "\u65b0\u4e1a\u52a1\u4ef7\u503c\u7387"}:
        return "life_franchise"
    if term in {"\u5185\u542b\u4ef7\u503c", "EV", "CSM", "NCSM", "\u5269\u4f59\u8fb9\u9645"}:
        return "embedded_value"
    if term in {"\u4ee3\u7406\u4eba", "\u94f6\u4fdd", "\u7eed\u671f", "\u9000\u4fdd"}:
        return "distribution_quality"
    if term in {"\u7efc\u5408\u6210\u672c\u7387", "\u8d54\u4ed8\u7387", "\u8d39\u7528\u7387"}:
        return "pnc_underwriting"
    if term in {
        "\u51c0\u6295\u8d44\u6536\u76ca\u7387",
        "\u603b\u6295\u8d44\u6536\u76ca\u7387",
        "\u7efc\u5408\u6295\u8d44\u6536\u76ca\u7387",
        "\u8d44\u4ea7\u914d\u7f6e",
    }:
        return "investment_spread"
    if term == "\u507f\u4ed8\u80fd\u529b":
        return "solvency"
    return "insurance_core"


def _peer_screen(symbol: str, curr_date: str, limit: int = 8) -> pd.DataFrame:
    basic = _fetch_stock_basic(symbol)
    if basic is None:
        return pd.DataFrame()
    universe = _fetch_stock_basic_universe()
    if universe is None or universe.empty or "industry" not in universe.columns:
        return pd.DataFrame()
    industry = _format_value(basic.get("industry"))
    peers = universe[universe["industry"].fillna("").astype(str) == industry].copy()
    if peers.empty:
        return pd.DataFrame()
    rows = []
    for _, peer in peers.head(limit).iterrows():
        ts_code = _format_value(peer.get("ts_code"))
        if not ts_code:
            continue
        daily = _fetch_daily_basic_latest(ts_code, curr_date)
        indicators = _fetch_fina_indicator(ts_code, curr_date)
        latest = _latest_indicator_row(indicators)
        rows.append(
            {
                "ts_code": ts_code,
                "name": _format_value(peer.get("name")),
                "pe_ttm": None if daily is None else _numeric(daily.get("pe_ttm")),
                "pb": None if daily is None else _numeric(daily.get("pb")),
                "dv_ttm": None if daily is None else _numeric(daily.get("dv_ttm")),
                "roe_annual": None if latest is None else _numeric(latest.get("roe_annual")),
                "netprofit_yoy": None if latest is None else _numeric(latest.get("netprofit_yoy")),
            }
        )
    return pd.DataFrame(rows)


def _render_missing_items() -> str:
    return "\n".join(f"- {item}" for item in MISSING_INSURANCE_ITEMS)


def _report_titles(reports: object, limit: int = 4) -> list[str]:
    if isinstance(reports, pd.DataFrame):
        if reports.empty:
            return []
        rows = reports.head(limit).to_dict("records")
    elif isinstance(reports, list):
        rows = reports[:limit]
    else:
        return []
    titles: list[str] = []
    for row in rows:
        if isinstance(row, dict):
            title = _format_value(row.get("title"))
        else:
            title = _format_value(row)
        if title:
            titles.append(title)
    return titles


def get_insurance_context(
    symbol: str,
    curr_date: str,
    look_back_days: int = 900,
    peer_limit: int = 8,
) -> str:
    """Return an insurance-native research layer for A-share insurers."""
    symbol = str(symbol or "").strip().upper()
    basic = _fetch_stock_basic(symbol)
    profile = _is_insurance_profile(symbol, basic)

    lines = [
        f"# Insurance verification context for {symbol} as of {curr_date}",
        "",
        f"- Status: {profile.status}",
        f"- Reason: {profile.reason}",
        f"- Company: {profile.company_name or symbol}",
        f"- Tushare industry: {profile.industry or 'N/A'}",
    ]
    if profile.status != "triggered":
        lines.extend(
            [
                "",
                "## Analyst Instructions",
                "- Reason: no insurance ticker, company-name, or industry trigger was found.",
                "- Do not force NBV, EV, solvency, or COR analysis into this stock unless primary evidence proves insurance exposure.",
            ]
        )
        return "\n".join(lines)

    daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
    indicators = _fetch_fina_indicator(symbol, curr_date)
    snapshot = _financial_snapshot(daily_basic, indicators)
    reports, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    evidence = _extract_insurance_filing_evidence(report_texts)
    peer_screen = _peer_screen(symbol, curr_date, limit=peer_limit)

    lines.extend(
        [
            "",
            "## Insurance-Native KPI Screen",
            _markdown_table(snapshot),
            "",
            "## Insurance Filing Evidence",
            _markdown_table(evidence) if not evidence.empty else "No insurance-native filing excerpts found.",
            "",
            "## Insurance Peer Screen",
            _markdown_table(peer_screen) if not peer_screen.empty else "Insurance peer screen unavailable.",
            "",
            "## Required Insurance Valuation Bridge",
            "- Life/health: start from NBV growth, NBV margin, agent and bancassurance productivity, persistency/surrender, CSM/NCSM movement, and EV growth.",
            "- P&C: separate premium growth from underwriting quality; require COR, loss ratio, expense ratio, and catastrophe / auto-pricing context.",
            "- Investment book: test net, total, and comprehensive investment yield against liability cost, duration, equity-market beta, and impairment risk.",
            "- Solvency and payout: dividends and buybacks are investable only when solvency adequacy, capital generation, and regulatory constraints support them.",
            "- Valuation: use P/EV, NBV multiple, PB/ROE, dividend yield, and SOTP together; PE is a cross-check, not the primary insurance anchor.",
            "- Defensive-rating calibration: Q1 net profit, non-recurring profit, or operating cash flow deterioration is a warning signal, not standalone proof that a high-dividend insurer has lost defensive value.",
            "- Allocation language: distinguish absolute downside from insurance-sector relative low-weighting and defensive-basket suitability; use Hold or relative Underweight/watch when NBV/OPAT evidence is still missing or mixed.",
            "",
            "## Research Gaps To Close Before High Conviction",
            _render_missing_items(),
            "",
            "## Analyst Instructions",
            "- Treat this as the specialist insurance layer. It should override generic manufacturing, commodity, shipping, or pure-bank framing when the target is an insurer.",
            "- For integrated insurers with banking subsidiaries, split the thesis into insurance core, bank subsidiary, asset-management / technology optionality, and capital-return policy.",
            "- Do not call hidden investee holdings a core valuation driver unless ownership, fair value, exit path, lock-up, and tax/double-counting checks are available.",
            "- If the report lacks NBV, EV, solvency, investment-yield, or COR evidence, cap conviction and keep the conclusion as evidence-limited.",
        ]
    )
    report_titles = _report_titles(reports)
    if report_titles:
        lines.insert(7, f"- Reports considered: {', '.join(report_titles)}")
    return "\n".join(lines)
