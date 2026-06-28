from __future__ import annotations

from dataclasses import dataclass
import re

import pandas as pd

from .thematic_research import _compact_text, _load_financial_report_texts
from .industry_identity import has_lithium_battery_symbol_hint, is_telecom_operator_text
from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)


SOFTWARE_COMPANIES = {
    "688111.SH": {
        "name": "\u91d1\u5c71\u529e\u516c",
        "business_model": "office productivity subscription / enterprise SaaS",
        "watchlist": (
            "WPS Office MAU and paid-user conversion",
            "personal subscription revenue, ARPU, renewal, and paid penetration",
            "institutional subscription versus license/authorization split",
            "WPS AI pricing, paid penetration, ARPU uplift, and cloud cost",
            "contract liabilities by duration and conversion into revenue",
            "Xinchuang / government and enterprise procurement cadence",
        ),
    },
    "600588.SH": {
        "name": "\u7528\u53cb\u7f51\u7edc",
        "business_model": "enterprise software / SaaS transition with implementation risk",
        "watchlist": (
            "ARR, cloud subscription revenue, renewal, and NRR",
            "project implementation revenue versus high-margin SaaS subscription",
            "contract liabilities mix and cash collection quality",
            "large-customer churn, sales efficiency, and implementation cycle",
            "AI product revenue evidence rather than feature announcements",
        ),
    },
    "600570.SH": {
        "name": "\u6052\u751f\u7535\u5b50",
        "business_model": "financial IT project software and recurring maintenance",
        "watchlist": (
            "financial-institution IT budget cycle",
            "order backlog, project acceptance, and receivables collection",
            "recurring maintenance / platform revenue versus project delivery",
            "AI and data-product monetization evidence",
        ),
    },
    "600845.SH": {
        "name": "\u5b9d\u4fe1\u8f6f\u4ef6",
        "business_model": "industrial software / automation / cloud-data-center hybrid",
        "watchlist": (
            "industrial software order visibility",
            "IDC/cloud utilization versus software margin",
            "project delivery, receivables, and cash conversion",
            "steel-sector capex and digitalization budget",
        ),
    },
    "002410.SZ": {
        "name": "\u5e7f\u8054\u8fbe",
        "business_model": "construction software / SaaS transition",
        "watchlist": (
            "costing software paid seats and renewal",
            "construction-cycle exposure and customer budget",
            "SaaS conversion, ARR, ARPU, and churn",
            "cash collection and contract-liability conversion",
        ),
    },
    "300033.SZ": {
        "name": "\u540c\u82b1\u987a",
        "business_model": "financial information subscription / traffic monetization",
        "watchlist": (
            "paid terminal users, ARPU, renewal, and market-activity beta",
            "ad / fund-sales / traffic monetization sensitivity",
            "AI investment-advisory product monetization and compliance risk",
        ),
    },
    "300454.SZ": {
        "name": "\u6df1\u4fe1\u670d",
        "business_model": "cybersecurity appliance plus subscription / cloud service",
        "watchlist": (
            "security subscription renewal and product attach rate",
            "hardware-appliance versus software/service gross margin",
            "government/enterprise budget cycle and receivables",
            "cloud and AI-security product monetization",
        ),
    },
    "002230.SZ": {
        "name": "\u79d1\u5927\u8baf\u98de",
        "business_model": "AI platform / education / enterprise software hybrid",
        "watchlist": (
            "AI model monetization by product line",
            "education and government project acceptance",
            "gross margin by hardware, project, and software/service",
            "R&D intensity, cash conversion, and subsidy dependence",
        ),
    },
    "688208.SH": {
        "name": "\u9053\u901a\u79d1\u6280",
        "business_model": "automotive diagnostics hardware plus software subscription",
        "watchlist": (
            "diagnostic-device shipments versus subscription/service revenue",
            "overseas channel inventory and tariffs",
            "software renewal, cloud diagnostics, and charging-pile service revenue",
            "gross margin by hardware and software/service",
        ),
    },
}


SOFTWARE_TERMS = (
    "\u8f6f\u4ef6",
    "\u4fe1\u606f\u6280\u672f",
    "\u529e\u516c\u8f6f\u4ef6",
    "\u4f01\u4e1a\u8f6f\u4ef6",
    "\u91d1\u878dIT",
    "\u5de5\u4e1a\u8f6f\u4ef6",
    "SaaS",
    "ARR",
    "ARPU",
    "MAU",
    "\u8ba2\u9605",
    "\u7eed\u8d39",
    "\u5408\u540c\u8d1f\u503a",
    "\u6388\u6743",
    "\u4fe1\u521b",
    "WPS",
    "AI",
)


@dataclass(frozen=True)
class SoftwareProfile:
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


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> SoftwareProfile | None:
    basic = _safe_fetch("stock_basic", _fetch_stock_basic, symbol)
    curated = SOFTWARE_COMPANIES.get(symbol, {})
    company_name = str(curated.get("name") or symbol)
    industry = ""
    if not isinstance(basic, TushareDataError) and basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    _, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:3500] for _, text in report_texts[:4])
    if symbol not in SOFTWARE_COMPANIES and is_telecom_operator_text(company_name, industry, text_probe):
        return None
    if symbol in SOFTWARE_COMPANIES:
        reason = "curated A-share software / SaaS ticker list"
    elif _contains_terms(SOFTWARE_TERMS, company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains software terms"
    else:
        return None

    return SoftwareProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        business_model=str(curated.get("business_model", "software / IT-services company")),
        watchlist=tuple(
            curated.get(
                "watchlist",
                (
                    "recurring revenue and renewal evidence",
                    "contract liabilities and cash collection quality",
                    "project implementation versus subscription mix",
                    "AI monetization evidence rather than feature announcements",
                ),
            )
        ),
        trigger_reason=reason,
        report_texts=list(report_texts),
    )


def _source_rows() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "data_bucket": "Filings / annual and quarterly reports",
                "use": "segment revenue, gross margin, contract liabilities, deferred revenue, R&D, cash conversion",
                "rule": "base evidence; separate disclosed facts from management narrative",
            },
            {
                "data_bucket": "Official IR / exchange Q&A",
                "use": "MAU, paid users, ARPU, renewal, AI commercialization wording, customer budget signals",
                "rule": "semi-official evidence; usable when dated and attributable",
            },
            {
                "data_bucket": "Product and pricing pages",
                "use": "subscription tiers, seat pricing, AI add-on pricing, enterprise packages",
                "rule": "pricing evidence only; not proof of uptake without user/revenue data",
            },
            {
                "data_bucket": "Tender / procurement / Xinchuang",
                "use": "government and enterprise orders, project scope, customer type, delivery cadence",
                "rule": "order signal; must still test acceptance, margin, and collection",
            },
            {
                "data_bucket": "Peer and global comps",
                "use": "SaaS, project software, financial IT, cybersecurity, and software-hardware model comparison",
                "rule": "match business model before comparing PE/PS/PB or Rule of 40",
            },
        ]
    )


def _taxonomy_rows() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model": "Product-led subscription",
                "examples": "office productivity, financial information terminals, developer tools",
                "core_question": "Can a large free/low-price user base convert into paid users and higher ARPU without churn?",
                "native_metrics": "MAU, paid users, conversion, ARPU, renewal/churn, billing duration, cloud cost",
            },
            {
                "model": "Enterprise-seat SaaS",
                "examples": "ERP/CRM/collaboration/security subscriptions",
                "core_question": "Are seats expanding inside customers and renewing at attractive gross margin?",
                "native_metrics": "ARR/MRR, NRR/GRR, seats, logo retention, S&M efficiency, deferred revenue",
            },
            {
                "model": "Project implementation software",
                "examples": "financial IT, government IT, industrial software delivery",
                "core_question": "Are orders accepted, collected, and converted into recurring revenue rather than low-margin delivery?",
                "native_metrics": "backlog, acceptance, receivables, cash collection, project margin, maintenance mix",
            },
            {
                "model": "Software-hardware hybrid",
                "examples": "cybersecurity appliances, auto diagnostics, AI education devices",
                "core_question": "How much profit comes from repeatable software/service versus cyclical hardware shipments?",
                "native_metrics": "hardware units, attach rate, service renewal, channel inventory, mix gross margin",
            },
            {
                "model": "Cloud/IDC hybrid",
                "examples": "industrial cloud, IDC plus software platform",
                "core_question": "Is growth driven by high-margin software or capital-intensive utilization?",
                "native_metrics": "utilization, capex, depreciation, power cost, software revenue, ROIC",
            },
        ]
    )


def _peer_model_rows(profile: SoftwareProfile) -> pd.DataFrame:
    rows = [
        {
            "ticker": "688111.SH",
            "company": "\u91d1\u5c71\u529e\u516c",
            "model_label": "office productivity subscription / enterprise SaaS",
            "compare_with_target": "target" if profile.symbol == "688111.SH" else "use only if office/SaaS economics are relevant",
        },
        {
            "ticker": "600588.SH",
            "company": "\u7528\u53cb\u7f51\u7edc",
            "model_label": "enterprise software / SaaS transition",
            "compare_with_target": "compare on SaaS transition quality, not consolidated PE alone",
        },
        {
            "ticker": "600570.SH",
            "company": "\u6052\u751f\u7535\u5b50",
            "model_label": "financial IT project software",
            "compare_with_target": "project-cycle peer; lower PS may reflect different revenue recognition and margin durability",
        },
        {
            "ticker": "600845.SH",
            "company": "\u5b9d\u4fe1\u8f6f\u4ef6",
            "model_label": "industrial software / automation / cloud hybrid",
            "compare_with_target": "industrial capex and IDC exposure make valuation bridge different",
        },
        {
            "ticker": "300033.SZ",
            "company": "\u540c\u82b1\u987a",
            "model_label": "financial information subscription / traffic monetization",
            "compare_with_target": "better for paid-user/ARPU comparison than project-software names, but market beta differs",
        },
        {
            "ticker": "300454.SZ",
            "company": "\u6df1\u4fe1\u670d",
            "model_label": "cybersecurity appliance plus subscription",
            "compare_with_target": "requires hardware/software mix split before using PS or gross margin",
        },
        {
            "ticker": "002230.SZ",
            "company": "\u79d1\u5927\u8baf\u98de",
            "model_label": "AI software / education / project hybrid",
            "compare_with_target": "AI narrative peer, but government/project/hardware mix differs materially",
        },
    ]
    return pd.DataFrame(rows)


def _deep_dive_rows(profile: SoftwareProfile) -> pd.DataFrame:
    if profile.symbol == "688111.SH":
        return pd.DataFrame(
            [
                {
                    "question": "Free MAU to paid conversion",
                    "must_find": "global/China MAU, paid personal users, conversion rate, ARPU, renewal/churn",
                    "why_it_matters": "decides whether WPS is still user-scale story or becoming pricing-power story",
                },
                {
                    "question": "Personal subscription versus institutional revenue",
                    "must_find": "personal subscription, institutional subscription, institutional authorization/licensing, each growth and margin",
                    "why_it_matters": "AI ARPU uplift is more credible in subscription buckets than one-off authorization",
                },
                {
                    "question": "WPS AI monetization",
                    "must_find": "AI paid tier price, AI paid users, attach rate, ARPU uplift, incremental cloud/compute cost",
                    "why_it_matters": "feature launch does not prove earnings uplift; paid usage and margin determine base-case value",
                },
                {
                    "question": "Contract-liability quality",
                    "must_find": "QoQ/YoY balance, current/non-current split, billing duration, conversion to revenue, refund/churn clues",
                    "why_it_matters": "high contract liabilities can be healthy visibility or a stale prepaid base; direction and conversion decide",
                },
                {
                    "question": "Enterprise / Xinchuang demand",
                    "must_find": "government and enterprise tenders, WPS 365 deployment, customer quality, acceptance and collection",
                    "why_it_matters": "separates policy-driven order flow from durable enterprise SaaS expansion",
                },
                {
                    "question": "Competitive pressure",
                    "must_find": "Microsoft 365/Copilot, Feishu, DingTalk, Tencent Docs, Baidu Wenku pricing and bundling behavior",
                    "why_it_matters": "AI office may increase willingness to pay or trigger free-bundling pressure",
                },
            ]
        )
    return pd.DataFrame(
        [
            {
                "question": "Revenue mix",
                "must_find": "subscription/service/project/hardware split, growth, and gross margin",
                "why_it_matters": "determines whether the company deserves SaaS, project-software, or hybrid valuation",
            },
            {
                "question": "Recurring quality",
                "must_find": "ARR/MRR if disclosed, paid users/seats, renewal/churn, NRR/GRR, deferred revenue",
                "why_it_matters": "recurring evidence is the bridge from revenue growth to durable multiple",
            },
            {
                "question": "Cash conversion",
                "must_find": "receivables, contract assets, cash received from customers, OCF, bad-debt/impairment",
                "why_it_matters": "project growth without collection can destroy value despite reported revenue",
            },
            {
                "question": "AI monetization",
                "must_find": "paid AI customers, pricing, attach rate, incremental revenue, compute/cloud cost",
                "why_it_matters": "AI narrative belongs in optionality until it shows paid adoption and margin path",
            },
        ]
    )


def _gate_rows(profile: SoftwareProfile) -> pd.DataFrame:
    model = profile.business_model.lower()
    if "project" in model or "financial it" in model or "implementation" in model:
        rows = [
            {
                "gate": "Project software economics",
                "must_verify": "order backlog, implementation cycle, acceptance timing, receivables, collection, project gross margin",
                "valuation_rule": "earnings and cash-flow multiple; contract liabilities are not ARR unless subscription mix is proven",
            },
            {
                "gate": "Recurring layer",
                "must_verify": "maintenance/subscription revenue, renewal, customer retention, deferred revenue conversion",
                "valuation_rule": "can receive SaaS-like multiple only for verified recurring revenue",
            },
        ]
    elif "hardware" in model or "appliance" in model:
        rows = [
            {
                "gate": "Hardware versus software mix",
                "must_verify": "device/appliance revenue, software/service revenue, attach rate, renewal, channel inventory",
                "valuation_rule": "split valuation; hardware gross margin and inventory risk cannot be valued like pure SaaS",
            },
            {
                "gate": "Subscription durability",
                "must_verify": "service renewal, ARPU, churn, cloud costs, customer cohort evidence",
                "valuation_rule": "subscription optionality only after paid renewal evidence",
            },
        ]
    else:
        rows = [
            {
                "gate": "Subscription quality",
                "must_verify": "ARR/MRR if disclosed, paid users, ARPU, conversion, renewal, churn, NRR/GRR, billing duration",
                "valuation_rule": "SaaS valuation requires recurring-revenue and retention evidence, not just contract liabilities",
            },
            {
                "gate": "AI monetization",
                "must_verify": "AI paid users, AI attach rate, AI ARPU uplift, separate pricing, compute/cloud cost, margin impact",
                "valuation_rule": "feature launch is optionality; paid usage and revenue are needed for base-case uplift",
            },
        ]

    rows.extend(
        [
            {
                "gate": "Contract liabilities",
                "must_verify": "opening/closing balance, YoY and QoQ trend, current/non-current split, billing duration, conversion to revenue",
                "valuation_rule": "rising balance improves visibility only when renewal and conversion quality are verified",
            },
            {
                "gate": "Peer basket",
                "must_verify": "same sales motion and revenue recognition: product-led SaaS, project IT, industrial software, cyber, cloud/IDC, or hardware-plus-service",
                "valuation_rule": "do not compare broad 'software service' peers without model labels",
            },
        ]
    )
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
    return ("..." if start else "") + cleaned[start:end] + ("..." if end < len(cleaned) else "")


def _report_snippets(profile: SoftwareProfile) -> pd.DataFrame:
    rows = []
    terms = SOFTWARE_TERMS + tuple(profile.watchlist)
    for title, text in profile.report_texts[:8]:
        if not _contains_terms(terms, title, text[:5000]):
            continue
        snippet = _snippet_around_terms(text, terms)
        if snippet:
            rows.append({"report": title[:80], "snippet": snippet})
        if len(rows) >= 5:
            break
    return pd.DataFrame(rows)


def get_software_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Return a gated software/SaaS research discipline layer."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Software verification context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    if has_lithium_battery_symbol_hint(symbol):
        return (
            f"# Software verification context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: structured battery-cell/system identity overrides incidental software/AI wording; software is not a separately disclosed profit pool."
        )

    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Software verification context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: no curated software mapping and no software/SaaS terms found in company name, industry, or recent filing text."
        )

    snippets = _report_snippets(profile)
    snippet_block = (
        _markdown_table(snippets)
        if not snippets.empty
        else "No readable filing snippets found around software/SaaS terms; treat this as a data gap, not negative evidence."
    )
    return "\n".join(
        [
            f"# Software verification context for {symbol} as of {curr_date}",
            "",
            "- Status: triggered",
            f"- Company: {profile.company_name}",
            f"- Tushare industry: {profile.industry or 'N/A'}",
            f"- Business model: {profile.business_model}",
            f"- Trigger reason: {profile.trigger_reason}",
            "",
            "## Company Watchlist",
            "\n".join(f"- {item}" for item in profile.watchlist),
            "",
            "## Source Priority And Data Acquisition",
            _markdown_table(_source_rows()),
            "",
            "## Software Business-Model Taxonomy",
            _markdown_table(_taxonomy_rows()),
            "",
            "## Model-Labeled Peer Map",
            _markdown_table(_peer_model_rows(profile)),
            "",
            "## Company-Specific Deep-Dive Questions",
            _markdown_table(_deep_dive_rows(profile)),
            "",
            "## Software Evidence Gate",
            _markdown_table(_gate_rows(profile)),
            "",
            "## Filing Text Evidence Snippets",
            snippet_block,
            "",
            "## Manager Treatment",
            "- First classify the revenue model before applying valuation: product-led subscription, enterprise-seat SaaS, project implementation, cybersecurity appliance, cloud/IDC hybrid, or hardware-plus-service.",
            "- Do not use broad 'software service' peer rankings as relative-value proof until the peers are model-labeled.",
            "- Contract liabilities are visibility evidence only after checking billing duration, renewal, and conversion into revenue; flat or falling balances may be deceleration.",
            "- AI features are not AI revenue. Require paid users, attach rate, ARPU uplift, pricing, and compute/cloud cost before putting AI into base-case earnings.",
            "- Missing ARR, ARPU, paid users, renewal, NRR/GRR, churn, segment gross margin, or contract-liability structure caps conviction and must appear as a research gap.",
        ]
    )
