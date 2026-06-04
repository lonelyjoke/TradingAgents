"""Medical-device-specific verification context for A-share companies."""

from __future__ import annotations

import re
from dataclasses import dataclass

import pandas as pd

from .filing_research import _load_financial_report_texts
from .tushare_a_stock import (
    _fetch_daily_basic_latest,
    _fetch_fina_indicator,
    _fetch_stock_basic,
    _fetch_stock_basic_universe,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)


MEDICAL_DEVICE_COMPANIES = {
    "300760.SZ": {
        "name": "\u8fc8\u745e\u533b\u7597",
        "business_model": "medical equipment + IVD + consumables global platform",
        "watchlist": (
            "patient monitoring, anesthesia, ventilator, ultrasound, and IVD installed-base cycle",
            "reagent / consumable pull-through from analyzers and lab automation",
            "domestic equipment renewal, procurement cadence, and anti-corruption drag",
            "overseas registration, channel inventory, localization, and FX sensitivity",
        ),
    },
    "688271.SH": {
        "name": "\u8054\u5f71\u533b\u7597",
        "business_model": "high-end imaging equipment company",
        "watchlist": (
            "CT/MRI/PET-CT/DR installed-base growth and replacement cycle",
            "large-equipment procurement, tender timing, and service revenue",
            "domestic substitution in tertiary hospitals",
            "overseas certification, channel buildout, and service network",
        ),
    },
    "002223.SZ": {
        "name": "\u9c7c\u8dc3\u533b\u7597",
        "business_model": "home-care medical devices and consumables",
        "watchlist": (
            "oxygen concentrator, respiratory, glucose monitoring, and home-care demand",
            "channel inventory and online/offline sell-through",
            "product mix, consumable repeat purchase, and pricing pressure",
        ),
    },
    "300832.SZ": {
        "name": "\u65b0\u4ea7\u4e1a",
        "business_model": "IVD analyzer + reagent closed-loop company",
        "watchlist": (
            "analyzer installed base and testing volume",
            "reagent revenue pull-through, menu expansion, and gross margin",
            "lab automation penetration and overseas distributor quality",
        ),
    },
    "603658.SH": {
        "name": "\u5b89\u56fe\u751f\u7269",
        "business_model": "IVD analyzer + reagent company",
        "watchlist": (
            "chemiluminescence installed base and reagent throughput",
            "testing menu breadth and hospital penetration",
            "collection/payment cycle and reagent price pressure",
        ),
    },
    "300633.SZ": {
        "name": "\u5f00\u7acb\u533b\u7597",
        "business_model": "ultrasound and endoscopy equipment company",
        "watchlist": (
            "ultrasound replacement cycle and endoscopy penetration",
            "domestic procurement cadence and overseas certification",
            "high-end product mix and service/consumable attach rate",
        ),
    },
    "688029.SH": {
        "name": "\u5357\u5fae\u533b\u5b66",
        "business_model": "endoscopic diagnosis/treatment consumables company",
        "watchlist": (
            "procedure volume, product mix, and hospital access",
            "consumable price pressure and collection risk",
            "overseas direct-sales and distributor quality",
        ),
    },
    "300003.SZ": {
        "name": "\u4e50\u666e\u533b\u7597",
        "business_model": "cardiovascular devices + consumables + pharma hybrid",
        "watchlist": (
            "stent / structural-heart / EP product mix",
            "volume-based procurement reset and new-product offset",
            "cash conversion across device and pharma segments",
        ),
    },
    "688016.SH": {
        "name": "\u5fc3\u8109\u533b\u7597",
        "business_model": "vascular intervention device company",
        "watchlist": (
            "procedure growth, product approval, and hospital penetration",
            "VBP and price-pressure offset by volume and new products",
            "gross margin, R&D pipeline, and international registration",
        ),
    },
    "688617.SH": {
        "name": "\u60e0\u6cf0\u533b\u7597",
        "business_model": "electrophysiology and vascular intervention device company",
        "watchlist": (
            "EP procedure growth and catheter penetration",
            "VBP exposure, new product approvals, and hospital coverage",
            "overseas registration and channel expansion",
        ),
    },
}


MEDICAL_DEVICE_TERMS = (
    "\u533b\u7597\u5668\u68b0",
    "\u533b\u7597\u8bbe\u5907",
    "\u533b\u7597\u4eea\u5668",
    "\u533b\u7528\u8017\u6750",
    "\u9ad8\u503c\u8017\u6750",
    "\u4f53\u5916\u8bca\u65ad",
    "\u8bca\u65ad\u8bd5\u5242",
    "\u8bd5\u5242",
    "\u8017\u6750",
    "\u68c0\u9a8c\u8bbe\u5907",
    "\u76d1\u62a4\u4eea",
    "\u9ebb\u9189\u673a",
    "\u547c\u5438\u673a",
    "\u8d85\u58f0",
    "\u5f71\u50cf\u8bbe\u5907",
    "\u5185\u7aa5\u955c",
    "\u6ce8\u518c\u8bc1",
    "\u88c5\u673a",
    "\u96c6\u91c7",
    "\u8bbe\u5907\u66f4\u65b0",
    "\u8d34\u606f\u8d37\u6b3e",
    "\u62db\u6295\u6807",
    "\u56fd\u4ea7\u66ff\u4ee3",
    "\u51fa\u6d77",
    "\u6d77\u5916\u6e20\u9053",
    "IVD",
    "FDA",
    "CE",
    "NMPA",
    "CT",
    "MRI",
)

MEDICAL_DEVICE_EVIDENCE_TERMS = (
    "\u88c5\u673a",
    "\u8bbe\u5907\u66f4\u65b0",
    "\u62db\u6295\u6807",
    "\u8bd5\u5242",
    "\u8017\u6750",
    "\u4f53\u5916\u8bca\u65ad",
    "IVD",
    "\u6d41\u6c34\u7ebf",
    "\u96c6\u91c7",
    "\u56fd\u4ea7\u66ff\u4ee3",
    "\u6ce8\u518c\u8bc1",
    "\u6d77\u5916",
    "\u51fa\u6d77",
    "\u6e20\u9053",
    "\u5e94\u6536\u8d26\u6b3e",
    "\u7ecf\u8425\u6027\u73b0\u91d1\u6d41",
    "\u7814\u53d1",
    "\u6bdb\u5229\u7387",
    "\u8d34\u606f",
    "\u533b\u7597\u65b0\u57fa\u5efa",
    "FDA",
    "CE",
    "NMPA",
)

MISSING_MEDICAL_DEVICE_ITEMS = (
    "installed base, replacement cycle, and tender / procurement cadence",
    "equipment revenue versus reagent / consumable pull-through",
    "VBP / procurement price pressure and volume-offset evidence",
    "NMPA/FDA/CE registration status and overseas channel quality",
    "segment gross margin, service revenue, and product-mix upgrade",
    "receivables, collection, distributor inventory, and operating cash-flow quality",
    "R&D pipeline, product approval calendar, and domestic-substitution proof",
)


@dataclass(frozen=True)
class MedicalDeviceProfile:
    symbol: str
    company_name: str
    industry: str
    business_model: str
    watchlist: tuple[str, ...]
    trigger_reason: str
    report_texts: list[tuple[str, str]]


def _safe_text(value: object) -> str:
    return str(value or "").strip()


def _contains_terms(terms: tuple[str, ...], *parts: object) -> bool:
    text = " ".join(str(part or "") for part in parts).lower()
    return any(str(term).lower() in text for term in terms if str(term or "").strip())


def _snippet_around_terms(text: str, terms: tuple[str, ...], window: int = 220) -> str:
    cleaned = re.sub(r"\s+", " ", _safe_text(text))
    lower = cleaned.lower()
    positions = [
        lower.find(str(term).lower())
        for term in terms
        if str(term or "").strip() and lower.find(str(term).lower()) >= 0
    ]
    if not positions:
        return cleaned[:520]
    pos = min(positions)
    start = max(0, pos - window)
    end = min(len(cleaned), pos + window)
    prefix = "..." if start else ""
    suffix = "..." if end < len(cleaned) else ""
    return prefix + cleaned[start:end] + suffix


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> MedicalDeviceProfile | None:
    basic = _fetch_stock_basic(symbol)
    curated = MEDICAL_DEVICE_COMPANIES.get(symbol, {})
    company_name = str(curated.get("name") or symbol)
    industry = ""
    if basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    _, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:4000] for _, text in report_texts[:4])
    if symbol in MEDICAL_DEVICE_COMPANIES:
        reason = "curated A-share medical-device ticker list"
    elif _contains_terms(MEDICAL_DEVICE_TERMS, company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains medical-device terms"
    else:
        return None

    return MedicalDeviceProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        business_model=str(curated.get("business_model", "medical-device / IVD / consumables company")),
        watchlist=tuple(
            curated.get(
                "watchlist",
                (
                    "installed base, tender cadence, and replacement cycle",
                    "reagent / consumable pull-through and product mix",
                    "VBP / procurement price pressure and domestic substitution",
                    "overseas registration, channel quality, and cash collection",
                ),
            )
        ),
        trigger_reason=reason,
        report_texts=list(report_texts),
    )


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


def _financial_snapshot(symbol: str, curr_date: str) -> pd.DataFrame:
    daily = _fetch_daily_basic_latest(symbol, curr_date)
    indicators = _fetch_fina_indicator(symbol, curr_date)
    latest = _latest_indicator_row(indicators)
    payload = {
        "pe_ttm": None if daily is None else _numeric(daily.get("pe_ttm")),
        "pb": None if daily is None else _numeric(daily.get("pb")),
        "dv_ttm": None if daily is None else _numeric(daily.get("dv_ttm")),
        "roe_annual": None if latest is None else _numeric(latest.get("roe_annual")),
        "grossprofit_margin": None if latest is None else _numeric(latest.get("grossprofit_margin")),
        "netprofit_margin": None if latest is None else _numeric(latest.get("netprofit_margin")),
        "netprofit_yoy": None if latest is None else _numeric(latest.get("netprofit_yoy")),
        "or_yoy": None if latest is None else _numeric(latest.get("or_yoy")),
    }
    return pd.DataFrame([payload])


def _source_rows() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "data_bucket": "Filings / annual and quarterly reports",
                "use": "segment revenue, gross margin, installed-base wording, R&D, overseas mix, receivables, cash conversion",
                "rule": "base evidence; separate disclosed facts from management narrative",
            },
            {
                "data_bucket": "NMPA / FDA / CE / product registration",
                "use": "new product approval, overseas market access, product category upgrade",
                "rule": "official catalyst evidence; registration is not revenue without channel and tender proof",
            },
            {
                "data_bucket": "Tender / procurement / equipment renewal policy",
                "use": "hospital capex cadence, equipment replacement cycle, order visibility, domestic substitution",
                "rule": "order signal; still test delivery, acceptance, margin, and payment",
            },
            {
                "data_bucket": "VBP / centralized procurement",
                "use": "price cuts, volume offset, hospital access, competitor reshuffle",
                "rule": "separate device price reset from procedure/testing-volume recovery",
            },
            {
                "data_bucket": "Distributor / overseas channel checks",
                "use": "channel inventory, sell-through, localization, FX, service network",
                "rule": "caps conviction when unavailable; do not turn shipment into terminal demand without support",
            },
        ]
    )


def _business_model_gate(profile: MedicalDeviceProfile) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "bucket": "Capital equipment",
                "must_verify": "installed base, replacement cycle, tender cadence, delivery/acceptance, service attach rate",
                "valuation_rule": "cycle-sensitive equipment revenue plus service option; PE alone can overstate replacement-cycle durability",
            },
            {
                "bucket": "IVD closed loop",
                "must_verify": "analyzer installed base, tests per machine, reagent menu breadth, reagent gross margin, lab automation penetration",
                "valuation_rule": "higher-quality recurring revenue only when reagent pull-through and testing volume are evidenced",
            },
            {
                "bucket": "Consumables / high-value devices",
                "must_verify": "procedure volume, product approval, hospital access, VBP exposure, price-volume offset",
                "valuation_rule": "volume and product-mix bridge after procurement resets; do not ignore price cuts",
            },
            {
                "bucket": "Overseas expansion",
                "must_verify": "FDA/CE/NMPA equivalents, distributor quality, localization, channel inventory, FX and tariffs",
                "valuation_rule": "growth optionality becomes base only when region mix, registration, and sell-through evidence exist",
            },
            {
                "bucket": "Cash conversion",
                "must_verify": "receivables, inventory, distributor credit, operating cash flow, warranty/service obligations",
                "valuation_rule": "quality haircut when profit growth outruns cash collection or channel inventory builds",
            },
        ]
    )


def _report_snippets(profile: MedicalDeviceProfile) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    terms = MEDICAL_DEVICE_EVIDENCE_TERMS + tuple(profile.watchlist)
    for title, text in profile.report_texts[:8]:
        if not _contains_terms(terms, title, text[:6000]):
            continue
        snippet = _snippet_around_terms(text, terms)
        if snippet:
            rows.append({"report": title[:80], "snippet": snippet})
        if len(rows) >= 8:
            break
    return pd.DataFrame(rows)


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
        latest = _latest_indicator_row(_fetch_fina_indicator(ts_code, curr_date))
        rows.append(
            {
                "ts_code": ts_code,
                "name": _format_value(peer.get("name")),
                "pe_ttm": None if daily is None else _numeric(daily.get("pe_ttm")),
                "pb": None if daily is None else _numeric(daily.get("pb")),
                "roe_annual": None if latest is None else _numeric(latest.get("roe_annual")),
                "grossprofit_margin": None if latest is None else _numeric(latest.get("grossprofit_margin")),
                "netprofit_yoy": None if latest is None else _numeric(latest.get("netprofit_yoy")),
            }
        )
    return pd.DataFrame(rows)


def _render_missing_items() -> str:
    return "\n".join(f"- {item}" for item in MISSING_MEDICAL_DEVICE_ITEMS)


def get_medical_device_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
    peer_limit: int = 8,
) -> str:
    """Return a gated medical-device research layer for A-share companies."""
    symbol = str(ticker or "").strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Medical-device verification context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Medical-device verification context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: no curated medical-device mapping and no device / IVD / consumables terms found in company name, industry, or recent filing text.\n"
            "- Do not force installed-base, VBP, reagent pull-through, or registration logic into this stock unless primary evidence proves medical-device exposure."
        )

    watchlist = "\n".join(f"- {item}" for item in profile.watchlist)
    snapshot = _financial_snapshot(symbol, curr_date)
    snippets = _report_snippets(profile)
    peer_screen = _peer_screen(symbol, curr_date, limit=peer_limit)
    snippet_block = (
        _markdown_table(snippets)
        if not snippets.empty
        else "No readable filing snippets found around medical-device terms; treat report-body evidence as a data gap, not as negative evidence."
    )

    lines = [
        f"# Medical-device verification context for {symbol} as of {curr_date}",
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
        "## Medical-Device KPI Screen",
        _markdown_table(snapshot),
        "",
        "## Source Priority And Data Acquisition",
        _markdown_table(_source_rows()),
        "",
        "## Business Model / Evidence Gate",
        _markdown_table(_business_model_gate(profile)),
        "",
        "## Filing Text Evidence Snippets",
        snippet_block,
        "",
        "## Medical-Device Peer Screen",
        _markdown_table(peer_screen) if not peer_screen.empty else "Medical-device peer screen unavailable.",
        "",
        "## Required Medical-Device Valuation Bridge",
        "- Equipment: installed base, replacement cycle, tender cadence, delivery / acceptance, service attach rate, and hospital capex cycle.",
        "- IVD: analyzer installed base, tests per machine, reagent menu expansion, reagent gross margin, and lab automation pull-through.",
        "- Consumables: procedure / testing volume, VBP price reset, product mix, hospital access, and volume-offset evidence.",
        "- Overseas: FDA/CE or local registration, distributor quality, localization, channel inventory, service network, FX and tariff exposure.",
        "- Valuation: combine PE/PEG, gross-margin durability, recurring consumable/service mix, overseas growth, and cash-conversion haircut; do not use a generic pharma pipeline frame.",
        "",
        "## Research Gaps To Close Before High Conviction",
        _render_missing_items(),
        "",
        "## Analyst Instructions",
        "- Treat this as the specialist medical-device layer. It should override generic pharma, pure manufacturing, or software framing when the target is a device / IVD / consumables company.",
        "- Separate capital equipment, reagent / consumable recurrence, service revenue, overseas expansion, and policy-procurement impact before valuation.",
        "- Missing installed-base, tender, VBP, registration, overseas channel, receivable, or reagent pull-through evidence caps conviction and belongs in research gaps.",
    ]
    return "\n".join(lines)
