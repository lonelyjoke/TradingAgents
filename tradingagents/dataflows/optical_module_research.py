from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .thematic_research import _compact_text, _load_financial_report_texts
from .tushare_a_stock import (
    TushareDataError,
    _fetch_balance_sheet_data,
    _fetch_cashflow_data,
    _fetch_fina_indicator,
    _fetch_income_statement_data,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)


OPTICAL_MODULE_SYMBOLS = {
    "300308.SZ": {"name": "Zhongji Innolight", "role": "high-speed optical module"},
    "300502.SZ": {"name": "Eoptolink", "role": "high-speed optical module"},
    "300394.SZ": {"name": "TFC Communication", "role": "optical component / connector"},
    "002281.SZ": {"name": "Accelink", "role": "optical module and optical device"},
    "603083.SH": {"name": "Cambridge Technology", "role": "optical module / telecom equipment"},
    "688498.SH": {"name": "Yuanjie Semiconductor", "role": "optical chip"},
    "300548.SZ": {"name": "Broadex Technologies", "role": "optical module / device"},
    "688205.SH": {"name": "Dk Photonics", "role": "optical transmission device"},
    "300570.SZ": {"name": "Taichenguang", "role": "optical component / connector"},
    "688313.SH": {"name": "Sicc", "role": "optical communication device"},
}

OPTICAL_MODULE_TERMS = (
    "optical module",
    "optical communication",
    "transceiver",
    "datacom",
    "800g",
    "1.6t",
    "400g",
    "cpo",
    "lpo",
    "silicon photonics",
    "coherent",
    "ai server",
    "cloud capex",
    "\u5149\u6a21\u5757",
    "\u5149\u901a\u4fe1",
    "\u5149\u5668\u4ef6",
    "\u5149\u82af\u7247",
    "\u9ad8\u901f\u7387",
    "\u6570\u901a",
    "\u7845\u5149",
    "\u76f8\u5e72",
    "\u4e91\u5382\u5546",
    "\u7b97\u529b",
    "\u4eba\u5de5\u667a\u80fd",
)

SUBCHAIN_ROWS = (
    {
        "position": "Downstream demand",
        "evidence_needed": "hyperscaler AI capex, GPU/ASIC cluster deployment, switch upgrade cycle, 800G/1.6T adoption",
        "listed_examples": "Nvidia/ASIC supply chain; Arista/Cisco switches; A-share module and component makers",
    },
    {
        "position": "Optical module integrator",
        "evidence_needed": "800G/1.6T shipment mix, overseas customer certification, pricing pressure, capacity and yield",
        "listed_examples": "300308.SZ, 300502.SZ, 002281.SZ, 603083.SH, 300548.SZ",
    },
    {
        "position": "Optical component / connector",
        "evidence_needed": "customer share, unit content per module, high-speed upgrade pull-through, margin sustainability",
        "listed_examples": "300394.SZ, 300570.SZ",
    },
    {
        "position": "Optical chip / device",
        "evidence_needed": "domestic substitution, qualification status, ASP, yield, telecom versus datacom exposure",
        "listed_examples": "688498.SH, 688205.SH",
    },
    {
        "position": "Technology route",
        "evidence_needed": "CPO, LPO, silicon photonics and coherent optics roadmaps; replacement versus content uplift risk",
        "listed_examples": "module makers, optical-chip makers, switch ecosystem",
    },
)


@dataclass(frozen=True)
class OpticalModuleProfile:
    symbol: str
    company_name: str
    industry: str
    role: str
    trigger_reason: str
    report_texts: list[tuple[str, str]]


def _safe_fetch(label: str, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        return TushareDataError(f"{label} unavailable: {exc}")


def _data_gap_note(label: str, data) -> str | None:
    if isinstance(data, TushareDataError):
        return f"{label}: {data}"
    if data is None or data.empty:
        return f"{label}: no rows returned"
    return None


def _contains_terms(terms: tuple[str, ...], *parts: object) -> bool:
    text = " ".join(str(part or "") for part in parts).lower()
    return any(term.lower() in text for term in terms)


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> OpticalModuleProfile | None:
    basic = _safe_fetch("stock_basic", _fetch_stock_basic, symbol)
    company_name = OPTICAL_MODULE_SYMBOLS.get(symbol, {}).get("name", symbol)
    industry = ""
    if not isinstance(basic, TushareDataError) and basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    _, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:3000] for _, text in report_texts[:4])

    if symbol in OPTICAL_MODULE_SYMBOLS:
        reason = "curated A-share AI optical-module supply-chain ticker list"
        role = OPTICAL_MODULE_SYMBOLS[symbol]["role"]
    elif _contains_terms(OPTICAL_MODULE_TERMS, company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains optical-module or AI datacom terms"
        role = "optical communication / AI datacom candidate"
    else:
        return None

    return OpticalModuleProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        role=role,
        trigger_reason=reason,
        report_texts=list(report_texts),
    )


def _latest_rows(data, columns: list[str], limit: int = 8) -> pd.DataFrame:
    if isinstance(data, TushareDataError) or data is None or data.empty:
        return pd.DataFrame()
    cols = [col for col in columns if col in data.columns]
    if not cols:
        return pd.DataFrame()
    rows = data[cols].copy()
    if "end_date" in rows.columns:
        rows["end_date"] = rows["end_date"].astype(str)
        rows = rows.sort_values("end_date", ascending=False)
    return rows.head(limit)


def _financial_signal_table(income, indicators) -> pd.DataFrame:
    rows = _latest_rows(
        income,
        ["end_date", "total_revenue", "revenue", "n_income_attr_p", "n_income"],
    )
    if rows.empty:
        return rows
    indicator_rows = _latest_rows(
        indicators,
        ["end_date", "grossprofit_margin", "netprofit_margin", "roe", "q_gr_yoy", "q_profit_yoy"],
    )
    if not indicator_rows.empty and "end_date" in rows.columns:
        rows = rows.merge(indicator_rows, on="end_date", how="left")
    for col in rows.columns:
        if col != "end_date":
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
    return rows


def _delivery_quality_table(balance, cashflow, income) -> pd.DataFrame:
    rows = _latest_rows(
        balance,
        [
            "end_date",
            "inventories",
            "accounts_receiv",
            "notes_receiv",
            "contract_liab",
            "adv_receipts",
            "money_cap",
            "total_liab",
            "total_assets",
        ],
    )
    if rows.empty:
        return rows
    cash = _latest_rows(cashflow, ["end_date", "n_cashflow_act", "c_fr_sale_sg"], limit=8)
    if not cash.empty:
        rows = rows.merge(cash, on="end_date", how="left")
    rev = _latest_rows(income, ["end_date", "total_revenue", "revenue", "n_income_attr_p"], limit=8)
    if not rev.empty:
        rows = rows.merge(rev, on="end_date", how="left")
    for col in rows.columns:
        if col != "end_date":
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
    revenue_col = "total_revenue" if "total_revenue" in rows.columns else "revenue" if "revenue" in rows.columns else None
    if revenue_col:
        for col in ["inventories", "accounts_receiv", "contract_liab", "adv_receipts"]:
            if col in rows.columns:
                rows[f"{col}_to_revenue"] = (rows[col] / rows[revenue_col].abs()).round(4)
    if {"n_cashflow_act", "n_income_attr_p"} <= set(rows.columns):
        rows["ocf_to_profit"] = (rows["n_cashflow_act"] / rows["n_income_attr_p"].abs()).round(4)
    if {"total_liab", "total_assets"} <= set(rows.columns):
        rows["liability_to_assets"] = (rows["total_liab"] / rows["total_assets"].abs()).round(4)
    keep = [
        "end_date",
        "inventories_to_revenue",
        "accounts_receiv_to_revenue",
        "contract_liab_to_revenue",
        "adv_receipts_to_revenue",
        "ocf_to_profit",
        "liability_to_assets",
        "money_cap",
    ]
    return rows[[col for col in keep if col in rows.columns]]


def _filing_snippets(report_texts: list[tuple[str, str]]) -> str:
    snippets = []
    for title, text in report_texts[:4]:
        snippet = _compact_text(text, 700)
        if snippet:
            snippets.append(f"- {title}: {snippet}")
    return "\n".join(snippets) if snippets else "No readable filing snippets found; treat customer mix, product generation, capacity, and overseas exposure as research gaps."


def get_optical_module_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Return a gated AI optical-module / datacom hardware research layer."""
    if not is_a_share_symbol(ticker):
        return f"# AI optical-module context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    symbol = ticker.upper()
    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# AI optical-module context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: no curated optical-module mapping and no optical communication / AI datacom terms found in company name, industry, or recent filing text."
        )

    income = _safe_fetch("income statement", _fetch_income_statement_data, symbol, curr_date)
    balance = _safe_fetch("balance sheet", _fetch_balance_sheet_data, symbol, curr_date)
    cashflow = _safe_fetch("cash flow", _fetch_cashflow_data, symbol, curr_date)
    indicators = _safe_fetch("financial indicators", _fetch_fina_indicator, symbol, curr_date)
    data_gaps = [
        note
        for note in [
            _data_gap_note("income statement", income),
            _data_gap_note("balance sheet", balance),
            _data_gap_note("cash flow", cashflow),
            _data_gap_note("financial indicators", indicators),
        ]
        if note
    ]

    lines = [
        f"# AI optical-module context for {symbol} as of {curr_date}",
        "",
        "- Status: triggered",
        f"- Company: {profile.company_name}",
        f"- Tushare industry: {profile.industry or 'N/A'}",
        f"- Supply-chain role: {profile.role}",
        f"- Trigger reason: {profile.trigger_reason}",
        "",
        "## AI Optical Supply-Chain Map",
        _markdown_table(pd.DataFrame(SUBCHAIN_ROWS)),
        "",
        "## Company Financial Signals",
        _markdown_table(_financial_signal_table(income, indicators)),
        "",
        "## Delivery / Working-Capital Verification",
        _markdown_table(_delivery_quality_table(balance, cashflow, income)),
        "",
        "## Filing Snippets",
        _filing_snippets(profile.report_texts),
    ]
    if data_gaps:
        lines.extend(
            [
                "",
                "## Data Gaps",
                *[f"- {gap}; do not make unsupported claims based on this dataset." for gap in data_gaps],
            ]
        )
    lines.extend(
        [
            "",
            "## Analyst Instructions",
            "- Do not treat the stock as a generic high-growth technology name. Start from its supply-chain role: module integrator, optical component, optical chip, connector, or telecom/device supplier.",
            "- The core AI thesis must bridge downstream AI capex into company revenue: hyperscaler GPU/ASIC cluster buildout, switch-speed upgrade, 400G/800G/1.6T migration, customer qualification, capacity, yield, and shipment mix.",
            "- High revenue growth is investable only when gross margin, inventory/revenue, receivables/revenue, operating cash flow, customer concentration, and overseas exposure form a coherent delivery story.",
            "- For Zhongji Innolight and Eoptolink, explicitly test whether growth is driven by 800G share gain, 1.6T ramp, overseas cloud customer orders, price/mix, exchange-rate effects, or temporary supply shortage.",
            "- Treat CPO, LPO, silicon photonics, coherent optics, export restrictions, tariff/geopolitical exposure, and customer concentration as thesis-critical risks, not boilerplate.",
            "- If exact customer, order, ASP, shipment, capacity, or 1.6T qualification data is missing, mark it as a research gap and use financial-statement proxies conditionally.",
            "- Valuation work must separate base-case earnings already implied by the current multiple from scenario value tied to future AI capex and technology-route optionality.",
        ]
    )
    return "\n".join(lines)
