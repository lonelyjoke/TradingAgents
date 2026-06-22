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
from .tushare_research import _query_optional_api
from .industry_identity import (
    CONSUMER_STAPLES_SYMBOL_HINTS,
    consumer_staples_subsector_hints,
)


CONSUMER_STAPLES_SYMBOLS = {
    "603345.SH": "Anjoy Foods",
    "002216.SZ": "Sanquan Food",
    "000895.SZ": "Shuanghui Development",
    "600887.SH": "Yili",
    "603288.SH": "Haitian Flavouring",
    "600872.SH": "Jonjee Hi-Tech",
    "603517.SH": "Juewei Food",
    "002557.SZ": "Qiaqia Food",
    "605089.SH": "Weizhixiang",
    "605499.SH": "Eastroc Beverage",
}

CONSUMER_PRODUCT_TERMS = (
    "food",
    "beverage",
    "dairy",
    "meat",
    "snack",
    "condiment",
    "frozen",
    "prepared dish",
    "食品",
    "饮料",
    "乳制品",
    "肉制品",
    "调味",
    "休闲食品",
    "速冻",
    "预制菜",
    "冻品",
    "鱼糜",
    "火锅料",
    "米面",
    "烘焙",
    "卤味",
)

SUBSECTOR_TERMS = {
    "frozen_prepared_food": ("速冻", "冻品", "预制菜", "鱼糜", "火锅料", "米面", "prepared dish", "frozen"),
    "meat_processing": ("肉制品", "屠宰", "猪肉", "肉食", "ham", "sausage"),
    "dairy": ("乳制品", "奶粉", "液态奶", "酸奶", "dairy"),
    "condiment": ("调味", "酱油", "醋", "复合调味料", "condiment"),
    "snack_food": ("休闲食品", "坚果", "瓜子", "零食", "snack"),
    "beverage": ("饮料", "茶饮", "果汁", "beverage"),
}

SUBSECTOR_TERMS["functional_beverage"] = (
    "\u4e1c\u9e4f\u7279\u996e",
    "\u529f\u80fd\u996e\u6599",
    "\u80fd\u91cf\u996e\u6599",
    "\u7535\u89e3\u8d28\u6c34",
    "\u679c\u6c41\u8336",
    "functional beverage",
    "energy drink",
)

SUBSECTOR_DRIVER_ROWS = {
    "frozen_prepared_food": (
        ("Demand", "restaurant chain penetration, hotpot/quick-service traffic, family convenience demand, distributor restocking"),
        ("Price/mix", "core hotpot products versus prepared dishes, new SKU velocity, promotion intensity, ASP and mix"),
        ("Cost", "surimi, poultry/pork, flour, edible oil, cold-chain energy and logistics"),
        ("Forward signals", "inventory/revenue, contract liabilities, distributor feedback, Q2/Q3 margin after Spring Festival seasonality"),
    ),
    "meat_processing": (
        ("Demand", "household protein consumption, catering recovery, channel mix and product premiumization"),
        ("Price/mix", "processed-meat ASP, fresh/frozen split, packaged food mix"),
        ("Cost", "hog price, pork spread, slaughter utilization, cold-chain logistics"),
        ("Forward signals", "inventory, receivables, hog-cost pass-through, dividend safety"),
    ),
    "dairy": (
        ("Demand", "birth cohort pressure, liquid milk volume, premium mix, channel inventory"),
        ("Price/mix", "basic milk versus premium/cheese/milk powder, promotion pressure"),
        ("Cost", "raw milk price, feed cost, packaging, cold-chain"),
        ("Forward signals", "dealer inventory, receivables, ad spend, raw-milk cycle"),
    ),
    "condiment": (
        ("Demand", "restaurant traffic, household cooking, distributor sell-through, catering-channel recovery"),
        ("Price/mix", "base condiment versus high-end/compound products, price hikes, promotion intensity"),
        ("Cost", "soybean meal, wheat, sugar, packaging, energy"),
        ("Forward signals", "contract liabilities, distributor inventory, channel rebate and gross margin"),
    ),
    "snack_food": (
        ("Demand", "offline traffic, e-commerce mix, gifting seasonality, new channel penetration"),
        ("Price/mix", "premium SKU mix, discounting, channel take rate"),
        ("Cost", "nuts/seeds, oils, sugar, packaging"),
        ("Forward signals", "inventory freshness, sell-through, receivables and cash collection"),
    ),
    "beverage": (
        ("Demand", "temperature/weather, channel traffic, convenience-store penetration, category growth"),
        ("Price/mix", "premiumization, new-product repeat purchase, promotion and channel mix"),
        ("Cost", "sugar, PET, packaging, logistics"),
        ("Forward signals", "inventory, distributor prepayment, marketing spend and gross margin"),
    ),
}

SUBSECTOR_DRIVER_ROWS["functional_beverage"] = (
    ("Demand", "energy-drink category growth, weather/temperature, outdoor and blue-collar traffic, convenience-store and traditional-channel sell-through"),
    ("Core SKU", "Dongpeng Special Drink volume, ASP, terminal price discipline, regional penetration and same-store productivity"),
    ("Second curve", "electrolyte water, juice tea, coffee/tea SKU repeat purchase, shelf penetration, and cannibalization versus incremental demand"),
    ("Cost", "sugar, PET, cans/packaging, logistics, advertising/rebate intensity and lottery/promotion policy"),
    ("Forward signals", "distributor prepayment, contract liabilities, channel inventory, terminal promotion, gross margin and selling-expense ratio"),
)


@dataclass(frozen=True)
class ConsumerStaplesProfile:
    symbol: str
    company_name: str
    industry: str
    subsectors: tuple[str, ...]
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


def _detect_subsectors(*parts: object) -> tuple[str, ...]:
    text = " ".join(str(part or "") for part in parts).lower()
    matches = [
        name
        for name, terms in SUBSECTOR_TERMS.items()
        if any(term.lower() in text for term in terms)
    ]
    return tuple(matches or ["general_consumer_staples"])


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> ConsumerStaplesProfile | None:
    basic = _safe_fetch("stock_basic", _fetch_stock_basic, symbol)
    company_name = CONSUMER_STAPLES_SYMBOLS.get(symbol, symbol)
    industry = ""
    if not isinstance(basic, TushareDataError) and basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    _, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:3000] for _, text in report_texts[:4])

    subsector_hints = consumer_staples_subsector_hints(symbol, company_name, industry, text_probe)

    if symbol in CONSUMER_STAPLES_SYMBOLS or symbol in CONSUMER_STAPLES_SYMBOL_HINTS:
        reason = "curated A-share consumer-staples ticker list"
    elif _contains_terms(CONSUMER_PRODUCT_TERMS, company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains consumer-staples terms"
    else:
        return None
    subsectors = tuple(
        dict.fromkeys(subsector_hints or _detect_subsectors(company_name, industry, text_probe))
    )

    return ConsumerStaplesProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        subsectors=subsectors,
        trigger_reason=reason,
        report_texts=list(report_texts),
    )


def _latest_rows(data, columns: list[str], limit: int = 6) -> pd.DataFrame:
    if isinstance(data, TushareDataError) or data is None or data.empty:
        return pd.DataFrame()
    cols = [col for col in columns if col in data.columns]
    if not cols:
        return pd.DataFrame()
    rows = data[cols].copy()
    rows = rows.loc[:, ~rows.columns.duplicated()].copy()
    if "end_date" in rows.columns:
        rows["end_date"] = rows["end_date"].astype(str)
        rows = rows.sort_values("end_date", ascending=False)
    return rows.head(limit)


def _financial_signal_table(income, indicators) -> pd.DataFrame:
    rows = _latest_rows(
        income,
        ["end_date", "total_revenue", "revenue", "n_income_attr_p", "n_income"],
        limit=8,
    )
    if rows.empty:
        return rows
    indicator_rows = _latest_rows(
        indicators,
        ["end_date", "grossprofit_margin", "netprofit_margin", "roe", "q_gr_yoy", "q_profit_yoy"],
        limit=8,
    )
    if not indicator_rows.empty and "end_date" in rows.columns:
        rows = rows.merge(indicator_rows, on="end_date", how="left")
    for col in rows.columns:
        if col != "end_date":
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
    return rows


def _working_capital_table(balance, cashflow, income) -> pd.DataFrame:
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
        limit=8,
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
        rows["debt_to_assets"] = (rows["total_liab"] / rows["total_assets"].abs()).round(4)
    keep = [
        "end_date",
        "inventories_to_revenue",
        "accounts_receiv_to_revenue",
        "contract_liab_to_revenue",
        "adv_receipts_to_revenue",
        "ocf_to_profit",
        "debt_to_assets",
        "money_cap",
    ]
    return rows[[col for col in keep if col in rows.columns]]


def _macro_table(curr_date: str) -> tuple[pd.DataFrame, list[str]]:
    notes: list[str] = []
    frames: list[pd.DataFrame] = []
    for api_name, fields, label in [
        ("cn_cpi", "month,nt_val,nt_yoy,town_yoy,cnt_yoy", "CPI"),
        ("cn_ppi", "month,ppi_yoy,ppi_mp_yoy", "PPI"),
    ]:
        try:
            data = _query_optional_api(api_name, fields=fields)
            if data is not None and not data.empty:
                data = data.loc[:, ~data.columns.duplicated()].copy()
                data["macro_source"] = label
                frames.append(data.head(6))
            else:
                notes.append(f"{api_name} returned no rows")
        except Exception as exc:
            notes.append(f"{api_name} unavailable: {exc}")
    if not frames:
        return pd.DataFrame(), notes
    combined = pd.concat(frames, ignore_index=True, sort=False)
    combined = combined.loc[:, ~combined.columns.duplicated()].copy()
    cols = [col for col in ["macro_source", "month", "nt_yoy", "town_yoy", "cnt_yoy", "ppi_yoy", "ppi_mp_yoy"] if col in combined.columns]
    return combined[cols].head(12), notes


def _driver_rows(profile: ConsumerStaplesProfile) -> pd.DataFrame:
    rows = []
    for subsector in profile.subsectors:
        for driver, must_read in SUBSECTOR_DRIVER_ROWS.get(
            subsector, SUBSECTOR_DRIVER_ROWS["frozen_prepared_food"]
        ):
            rows.append({"subsector": subsector, "driver": driver, "must_read": must_read})
    return pd.DataFrame(rows)


def get_consumer_staples_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Return a gated consumer-staples / food-beverage research discipline layer."""
    if not is_a_share_symbol(ticker):
        return f"# Consumer-staples verification context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    symbol = ticker.upper()
    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Consumer-staples verification context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: no curated consumer-staples mapping and no food/beverage terms found in company name, industry, or recent filing text."
        )

    income = _safe_fetch("income statement", _fetch_income_statement_data, symbol, curr_date)
    balance = _safe_fetch("balance sheet", _fetch_balance_sheet_data, symbol, curr_date)
    cashflow = _safe_fetch("cash flow", _fetch_cashflow_data, symbol, curr_date)
    indicators = _safe_fetch("financial indicators", _fetch_fina_indicator, symbol, curr_date)
    macro, macro_notes = _macro_table(curr_date)
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

    filing_snippets = []
    for title, text in profile.report_texts[:4]:
        snippet = _compact_text(text, 700)
        if snippet:
            filing_snippets.append(f"- {title}: {snippet}")

    lines = [
        f"# Consumer-staples verification context for {symbol} as of {curr_date}",
        "",
        "- Status: triggered",
        f"- Company: {profile.company_name}",
        f"- Tushare industry: {profile.industry or 'N/A'}",
        f"- Trigger reason: {profile.trigger_reason}",
        f"- Detected subsectors: {', '.join(profile.subsectors)}",
        "",
        "## Consumer-Native Driver Map",
        _markdown_table(_driver_rows(profile)),
        "",
        "## Company Financial Signals",
        _markdown_table(_financial_signal_table(income, indicators)),
        "",
        "## Channel / Inventory / Cash-Conversion Signals",
        _markdown_table(_working_capital_table(balance, cashflow, income)),
        "",
        "## Macro And Industry Demand Proxies",
        _markdown_table(macro) if not macro.empty else "No CPI/PPI macro rows were retrieved from Tushare optional APIs.",
    ]
    if data_gaps:
        lines.extend(
            [
                "",
                "## Data Gaps",
                *[f"- {gap}; do not make unsupported claims based on this dataset." for gap in data_gaps],
            ]
        )
    if macro_notes:
        lines.extend(["", "Macro data notes:"] + [f"- {note}" for note in macro_notes[:4]])
    lines.extend(
        [
            "",
            "## Filing Snippets",
            "\n".join(filing_snippets) if filing_snippets else "No readable filing snippets found; treat segment mix, channel inventory, and management discussion as research gaps.",
            "",
            "## Analyst Instructions",
            "- For food and beverage names, do not stop at PE/PB, dividend yield, or generic consumption recovery.",
            "- Start from category identity: frozen prepared food, meat processing, dairy, condiment, snacks, or beverage; each category has different seasonality, channel economics, and cost pass-through.",
            "- For Anjoy/frozen-food names, explicitly test whether Q1 strength is Spring Festival restocking, channel destocking completion, product mix improvement, or durable end-demand acceleration.",
            "- Revenue growth is investable only when gross margin, inventory/revenue, contract liabilities or advance receipts, receivables, and operating cash flow tell a coherent story.",
            "- Treat raw-material prices, restaurant traffic, retail sales, channel inventory, and prepared-dish penetration as critical industry variables. If exact data is missing, mark it as a research gap and use financial-statement proxies conditionally.",
            "- Product innovation or prepared-dish optionality belongs in scenario value until segment revenue, margin, repeat purchase, channel sell-through, or management disclosure verifies it.",
            "- Food-safety events, promotion intensity, cold-chain cost, and distributor health are thesis-critical risks, not generic risk boilerplate.",
        ]
    )
    return "\n".join(lines)
