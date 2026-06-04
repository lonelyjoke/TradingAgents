from __future__ import annotations

from dataclasses import dataclass

import re

import pandas as pd

from .thematic_research import _compact_text, _load_financial_report_texts
from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)


BIOPHARMA_COMPANIES = {
    "688235.SH": {
        "name": "百济神州",
        "business_model": "global innovative-drug company",
        "watchlist": (
            "BRUKINSA/zanubrutinib",
            "TEVIMBRA/tislelizumab",
            "sonrotoclax/BCL2",
            "global commercialization",
        ),
    },
    "600276.SH": {
        "name": "恒瑞医药",
        "business_model": "China innovative-drug and legacy pharma company",
        "watchlist": (
            "PD-1 and oncology portfolio",
            "ADC and differentiated pipelines",
            "GLP-1/metabolic optionality",
            "innovative-drug export/BD evidence",
        ),
    },
    "688180.SH": {
        "name": "君实生物",
        "business_model": "commercializing biotech company",
        "watchlist": (
            "toripalimab commercialization",
            "US label and partner economics",
            "pipeline breadth versus cash runway",
            "sales efficiency",
        ),
    },
    "603259.SH": {
        "name": "药明康德",
        "business_model": "CRO/CDMO pharma-services company",
        "watchlist": (
            "order backlog and customer funding cycle",
            "CRO/CDMO capacity utilization",
            "geopolitical and customer-concentration risk",
            "free cash flow and capex discipline",
        ),
    },
}


BIOPHARMA_TERMS = (
    "创新药",
    "生物医药",
    "医药",
    "药品",
    "制药",
    "临床",
    "适应症",
    "管线",
    "上市申请",
    "新药",
    "抗体",
    "肿瘤",
    "研发",
    "CDE",
    "NMPA",
    "FDA",
    "EMA",
    "ClinicalTrials.gov",
    "Phase",
)

SERVICES_TERMS = ("CRO", "CDMO", "药明康德", "药明生物", "临床前", "药物发现")


@dataclass(frozen=True)
class BiopharmaProfile:
    symbol: str
    company_name: str
    industry: str
    business_model: str
    watchlist: tuple[str, ...]
    trigger_reason: str
    report_texts: list[tuple[str, str]]


def _safe_fetch(label: str, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        return TushareDataError(f"{label} unavailable: {exc}")


def _contains_terms(terms: tuple[str, ...], *parts: object) -> bool:
    text = " ".join(str(part or "") for part in parts)
    return any(term.lower() in text.lower() for term in terms)


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> BiopharmaProfile | None:
    basic = _safe_fetch("stock_basic", _fetch_stock_basic, symbol)
    curated = BIOPHARMA_COMPANIES.get(symbol, {})
    company_name = str(curated.get("name") or symbol)
    industry = ""
    if not isinstance(basic, TushareDataError) and basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    _, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:3500] for _, text in report_texts[:4])
    if symbol in BIOPHARMA_COMPANIES:
        reason = "curated A-share biopharma / pharma-services ticker list"
    elif _contains_terms(BIOPHARMA_TERMS + SERVICES_TERMS, company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains biopharma terms"
    else:
        return None

    is_services = _contains_terms(SERVICES_TERMS, company_name, industry, text_probe)
    business_model = str(
        curated.get(
            "business_model",
            "CRO/CDMO pharma-services company" if is_services else "innovative-drug company",
        )
    )
    watchlist = tuple(curated.get("watchlist", ()))
    if not watchlist:
        watchlist = (
            "approved products and commercial ramp",
            "late-stage pipeline and label expansion",
            "regulatory review and reimbursement milestones",
            "R&D spend, cash runway, and dilution risk",
        )

    return BiopharmaProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        business_model=business_model,
        watchlist=watchlist,
        trigger_reason=reason,
        report_texts=list(report_texts),
    )


def _evidence_source_rows(profile: BiopharmaProfile) -> pd.DataFrame:
    rows = [
        {
            "data_bucket": "Company filings / IR",
            "source": "annual/interim reports, exchange announcements, investor presentations, official pipeline pages",
            "use": "segment revenue, R&D spend, cash runway, product sales, disclosed milestones, management wording",
            "valuation_treatment": "filing-grade base evidence; still separate disclosed fact from forward assumption",
        },
        {
            "data_bucket": "Clinical trials",
            "source": "ClinicalTrials.gov, CDE trial registration, company trial registry when official",
            "use": "NCT/registration ID, phase, enrollment, status, primary completion, endpoint, comparator",
            "valuation_treatment": "pipeline risk-adjusted NPV input; Phase I/II normally optionality, not base earnings",
        },
        {
            "data_bucket": "Regulatory",
            "source": "CDE/NMPA, FDA, EMA, labels, review decisions, approved indications",
            "use": "NDA/BLA/MAA acceptance, approval, label breadth, safety warnings, review timing",
            "valuation_treatment": "official catalyst evidence; do not treat media speculation as approval proof",
        },
        {
            "data_bucket": "Reimbursement / pricing",
            "source": "医保目录/NRDL, national and provincial procurement, official tender/platform prices",
            "use": "access, negotiated price, volume trade-off, margin pressure, competitive intensity",
            "valuation_treatment": "commercial ramp and margin input; missing price data caps conviction",
        },
        {
            "data_bucket": "Clinical readouts",
            "source": "ASCO/ESMO/ASH/AACR abstracts, peer-reviewed papers, conference presentations",
            "use": "ORR, PFS, OS, DOR, AE/SAE, discontinuation, subgroup, line of therapy",
            "valuation_treatment": "evidence quality depends on trial design, maturity, sample size, and comparator",
        },
    ]
    if "services" in profile.business_model.lower() or "CRO" in " ".join(profile.watchlist):
        rows.append(
            {
                "data_bucket": "CRO/CDMO demand",
                "source": "company filings, customer concentration disclosure, order/backlog commentary, capex/utilization evidence",
                "use": "customer funding cycle, backlog visibility, project conversion, geopolitical restrictions",
                "valuation_treatment": "service-cycle and FCF evidence; do not value like a drug-owner pipeline",
            }
        )
    return pd.DataFrame(rows)


def _asset_gate_rows(profile: BiopharmaProfile) -> pd.DataFrame:
    if "services" in profile.business_model.lower() or "CRO" in " ".join(profile.watchlist):
        return pd.DataFrame(
            [
                {
                    "bucket": "Drug discovery / CRO",
                    "must_verify": "customer demand, new project flow, pricing, cancellation, client concentration",
                    "source": "filings, IR, customer funding trend, official order/backlog commentary",
                    "valuation_rule": "service revenue/FCF multiple; no pipeline rNPV unless the company owns the asset economics",
                },
                {
                    "bucket": "CDMO capacity",
                    "must_verify": "capacity utilization, ramp schedule, capex returns, large-project conversion",
                    "source": "filings, capex/CIP, segment margin, management commentary",
                    "valuation_rule": "cycle and utilization sensitivity; capex without utilization is not growth proof",
                },
                {
                    "bucket": "Geopolitical risk",
                    "must_verify": "affected revenue/customer mix, legal status, mitigation plan, order behavior",
                    "source": "official filings, risk disclosures, customer/geography segment data",
                    "valuation_rule": "scenario haircut to revenue visibility, multiple, and cash-flow durability",
                },
            ]
        )
    return pd.DataFrame(
        [
            {
                "bucket": "Approved commercial assets",
                "must_verify": "approved indication, label breadth, sales ramp, reimbursement, gross margin, competition",
                "source": "filings, CDE/NMPA/FDA/EMA labels, NRDL/procurement, product sales disclosure",
                "valuation_rule": "base valuation can use revenue/profit contribution when sales evidence exists",
            },
            {
                "bucket": "Label expansion / late-stage trials",
                "must_verify": "phase, endpoint, comparator, enrollment, primary completion, regulatory path",
                "source": "ClinicalTrials.gov/CDE, official pipeline, conference abstract",
                "valuation_rule": "risk-adjusted NPV; catalyst timing is a watch item until official",
            },
            {
                "bucket": "Early pipeline",
                "must_verify": "mechanism, differentiation, safety signal, sample size, competitive landscape",
                "source": "trial registry, abstracts, company R&D disclosure",
                "valuation_rule": "scenario optionality; do not let Phase I/II drive base-case valuation",
            },
            {
                "bucket": "BD / licensing",
                "must_verify": "upfront/milestone/royalty terms, territory, economics retained, partner quality",
                "source": "official announcement and filing treatment",
                "valuation_rule": "SOTP/rNPV only for retained economics; avoid double-counting product sales and royalties",
            },
        ]
    )


def _report_snippets(profile: BiopharmaProfile) -> pd.DataFrame:
    rows = []
    terms = BIOPHARMA_TERMS + SERVICES_TERMS + tuple(profile.watchlist)
    for title, text in profile.report_texts[:8]:
        if not _contains_terms(terms, title, text[:5000]):
            continue
        snippet = _snippet_around_terms(text, terms)
        if snippet:
            rows.append({"report": title[:80], "snippet": snippet})
        if len(rows) >= 5:
            break
    return pd.DataFrame(rows)


def _snippet_around_terms(text: str, terms: tuple[str, ...], window: int = 220) -> str:
    cleaned = re.sub(r"\s+", " ", str(text or "")).strip()
    lower = cleaned.lower()
    positions = [
        lower.find(str(term).lower())
        for term in terms
        if str(term or "").strip() and lower.find(str(term).lower()) >= 0
    ]
    if not positions:
        return _compact_text(cleaned, limit=520)
    pos = min(positions)
    start = max(0, pos - window)
    end = min(len(cleaned), pos + window)
    prefix = "..." if start else ""
    suffix = "..." if end < len(cleaned) else ""
    return prefix + cleaned[start:end] + suffix


def get_biopharma_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Return a gated biopharma/pharma-services research discipline layer."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Biopharma verification context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Biopharma verification context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: no curated biopharma mapping and no biopharma terms found in company name, industry, or recent filing text."
        )

    watchlist = "\n".join(f"- {item}" for item in profile.watchlist)
    snippets = _report_snippets(profile)
    snippet_block = (
        _markdown_table(snippets)
        if not snippets.empty
        else "No readable filing snippets found around biopharma terms; treat report-body evidence as a data gap, not as negative evidence."
    )
    lines = [
        f"# Biopharma verification context for {symbol} as of {curr_date}",
        "",
        "- Status: triggered",
        f"- Company: {profile.company_name}",
        f"- Tushare industry: {profile.industry or 'N/A'}",
        f"- Business model: {profile.business_model}",
        f"- Trigger reason: {profile.trigger_reason}",
        "",
        "## Company Watchlist",
        watchlist,
        "",
        "## Source Priority And Data Acquisition",
        _markdown_table(_evidence_source_rows(profile)),
        "",
        "## Asset / Evidence Gate",
        _markdown_table(_asset_gate_rows(profile)),
        "",
        "## Filing Text Evidence Snippets",
        snippet_block,
        "",
        "## Manager Treatment",
        "- Separate commercialized products, label-expansion catalysts, clinical pipeline, BD economics, and cash runway before valuing the company.",
        "- Commercial assets can enter base valuation only when sales/reimbursement/label evidence is present; clinical assets should use risk-adjusted NPV or scenario optionality.",
        "- Do not treat Phase I/II, conference abstracts, or management pipeline wording as base-case earnings without trial quality, regulatory path, and competitive context.",
        "- For CRO/CDMO/pharma-services names, analyze order visibility, customer funding, capacity utilization, geopolitical risk, and FCF; do not value them like drug-owner pipelines.",
        "- Missing clinical-trial IDs, regulatory status, reimbursement/price data, or product sales is a research gap that caps conviction rather than a reason to invent numbers.",
    ]
    return "\n".join(lines)
