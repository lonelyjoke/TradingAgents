from __future__ import annotations

from dataclasses import dataclass
import re

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


BAIJIU_SYMBOLS = {
    "600519.SH": "贵州茅台",
    "000858.SZ": "五粮液",
    "000568.SZ": "泸州老窖",
    "600809.SH": "山西汾酒",
    "002304.SZ": "洋河股份",
    "000596.SZ": "古井贡酒",
    "603369.SH": "今世缘",
    "600779.SH": "水井坊",
    "600702.SH": "舍得酒业",
    "603198.SH": "迎驾贡酒",
    "603589.SH": "口子窖",
    "600559.SH": "老白干酒",
    "000799.SZ": "酒鬼酒",
    "600197.SH": "伊力特",
    "000995.SZ": "皇台酒业",
}

BAIJIU_TERMS = (
    "白酒",
    "茅台",
    "五粮液",
    "泸州老窖",
    "汾酒",
    "洋河",
    "古井贡",
    "今世缘",
    "舍得",
    "水井坊",
    "口子窖",
    "老白干",
    "酒鬼酒",
    "酱香",
    "浓香",
    "清香",
    "飞天",
    "经销商",
)


@dataclass(frozen=True)
class BaijiuProfile:
    symbol: str
    company_name: str
    industry: str
    trigger_reason: str
    report_texts: list[tuple[str, str]]


def _safe_fetch(label: str, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        return TushareDataError(f"{label} unavailable: {exc}")


def _contains_baijiu_terms(*parts: object) -> bool:
    text = " ".join(str(part or "") for part in parts)
    return any(term in text for term in BAIJIU_TERMS)


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> BaijiuProfile | None:
    basic = _safe_fetch("stock_basic", _fetch_stock_basic, symbol)
    company_name = BAIJIU_SYMBOLS.get(symbol, symbol)
    industry = ""
    if not isinstance(basic, TushareDataError) and basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    reports, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:2000] for _, text in report_texts[:3])
    if symbol in BAIJIU_SYMBOLS:
        reason = "curated A-share baijiu ticker list"
    elif _contains_baijiu_terms(company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains baijiu terms"
    else:
        return None

    return BaijiuProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
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
    if "end_date" in rows.columns:
        rows["end_date"] = rows["end_date"].astype(str)
        rows = rows.sort_values("end_date", ascending=False)
    return rows.head(limit)


def _growth_table(income: pd.DataFrame | TushareDataError) -> pd.DataFrame:
    rows = _latest_rows(
        income,
        ["end_date", "total_revenue", "revenue", "n_income_attr_p", "n_income"],
        limit=8,
    )
    if rows.empty or "end_date" not in rows.columns:
        return rows
    for col in ["total_revenue", "revenue", "n_income_attr_p", "n_income"]:
        if col in rows.columns:
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
    annual = rows[rows["end_date"].astype(str).str.endswith("1231")].copy()
    base = annual if not annual.empty else rows.copy()
    value_cols = [col for col in ["total_revenue", "revenue", "n_income_attr_p", "n_income"] if col in base.columns]
    for col in value_cols:
        base[f"{col}_yoy"] = base[col].pct_change(-1).mul(100).round(2)
    return base.head(6)


def _contract_liability_table(balance: pd.DataFrame | TushareDataError) -> pd.DataFrame:
    rows = _latest_rows(
        balance,
        ["end_date", "contract_liab", "adv_receipts", "inventories", "money_cap", "accounts_receiv"],
        limit=8,
    )
    if rows.empty:
        return rows
    for col in ["contract_liab", "adv_receipts", "inventories", "money_cap", "accounts_receiv"]:
        if col in rows.columns:
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
            rows[f"{col}_qoq"] = rows[col].pct_change(-1).mul(100).round(2)
    return rows


def _cash_quality_table(cashflow: pd.DataFrame | TushareDataError, income: pd.DataFrame | TushareDataError) -> pd.DataFrame:
    cash_rows = _latest_rows(cashflow, ["end_date", "n_cashflow_act", "c_fr_sale_sg"], limit=8)
    inc_rows = _latest_rows(income, ["end_date", "n_income_attr_p", "n_income"], limit=8)
    if cash_rows.empty:
        return pd.DataFrame()
    merged = cash_rows.merge(inc_rows, on="end_date", how="left")
    for col in ["n_cashflow_act", "c_fr_sale_sg", "n_income_attr_p", "n_income"]:
        if col in merged.columns:
            merged[col] = pd.to_numeric(merged[col], errors="coerce")
    profit_col = "n_income_attr_p" if "n_income_attr_p" in merged.columns else "n_income"
    if profit_col in merged.columns:
        merged["ocf_to_profit"] = (merged["n_cashflow_act"] / merged[profit_col]).round(2)
    return merged.head(6)


def _valuation_row(indicators: pd.DataFrame | TushareDataError) -> pd.DataFrame:
    if isinstance(indicators, TushareDataError) or indicators is None or indicators.empty:
        return pd.DataFrame()
    data = indicators.copy()
    if "end_date" in data.columns:
        data["end_date"] = data["end_date"].astype(str)
        data = data.sort_values("end_date", ascending=False)
    cols = [
        "end_date",
        "roe",
        "roe_waa",
        "grossprofit_margin",
        "netprofit_margin",
        "netprofit_yoy",
        "or_yoy",
        "debt_to_assets",
    ]
    return _latest_rows(data, cols, limit=6)


def _snippets(report_texts: list[tuple[str, str]], terms: tuple[str, ...], limit: int = 10) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for title, text in report_texts[:5]:
        for raw in str(text or "").splitlines():
            line = _compact_text(raw, limit=260)
            if not line:
                continue
            if any(term in line for term in terms):
                rows.append({"report": title[:40], "evidence": line})
                if len(rows) >= limit:
                    return pd.DataFrame(rows)
    return pd.DataFrame(rows)


def get_baijiu_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Return a gated baijiu verification layer for A-share liquor companies."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Baijiu verification context for {ticker}\n\nStatus: not_applicable\n\n- Reason: not an A-share ticker."
    if not curr_date:
        from datetime import datetime

        curr_date = datetime.now().strftime("%Y-%m-%d")

    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Baijiu verification context for {symbol} as of {curr_date}\n\n"
            "Status: not_applicable\n\n"
            "- Reason: no baijiu company-name, industry, curated ticker, or filing-text trigger was found."
        )

    income = _safe_fetch("income", _fetch_income_statement_data, symbol, curr_date, "quarterly", 10)
    balance = _safe_fetch("balancesheet", _fetch_balance_sheet_data, symbol, curr_date, "quarterly", 10)
    cashflow = _safe_fetch("cashflow", _fetch_cashflow_data, symbol, curr_date, "quarterly", 10)
    indicators = _safe_fetch("fina_indicator", _fetch_fina_indicator, symbol, curr_date)

    channel_terms = ("批价", "一批价", "原箱", "散瓶", "渠道库存", "经销商", "回款", "合同负债", "预收款")
    product_terms = ("飞天", "茅台1935", "普五", "国窖", "青花", "年份酒", "系列酒", "直营", "i茅台")
    policy_terms = ("消费税", "禁酒", "反腐", "三公", "商标许可", "关联交易")

    lines = [
        f"# Baijiu verification context for {symbol} as of {curr_date}",
        "",
        "Status: triggered",
        f"- Company: {profile.company_name}",
        f"- Industry: {profile.industry or 'N/A'}",
        f"- Trigger: {profile.trigger_reason}",
        "",
        "## How This Layer Should Be Used",
        "- This layer is only for baijiu/liquor targets. Do not apply its channel-price logic to unrelated consumer names.",
        "- Treat wholesale price, channel inventory, and dealer payment evidence as thesis-critical. If unavailable, keep them as neutral retrieval tasks; do not substitute generic PE/technicals or mechanically alter the rating.",
        "- Contract liabilities must be read with seasonality: compare same-quarter YoY and multi-year seasonal baselines before calling a Q4-to-Q1 move demand deterioration.",
        "- For Maotai specifically, separate Feitian loose-bottle, original-carton, retail price, wholesale/reference price, ex-factory price, and company guided price.",
        "",
        "## Revenue and Profit Trend",
        _markdown_table(_growth_table(income)),
        "",
        "## Channel Payment and Inventory Signals",
        _markdown_table(_contract_liability_table(balance)),
        "",
        "## Cash Conversion Quality",
        _markdown_table(_cash_quality_table(cashflow, income)),
        "",
        "## Profitability and Balance-Sheet Quality",
        _markdown_table(_valuation_row(indicators)),
        "",
        "## Filing Evidence: Channel and Payments",
        _markdown_table(_snippets(profile.report_texts, channel_terms)),
        "",
        "## Filing Evidence: Product Mix and Direct Sales",
        _markdown_table(_snippets(profile.report_texts, product_terms)),
        "",
        "## Filing Evidence: Policy and Governance",
        _markdown_table(_snippets(profile.report_texts, policy_terms, limit=6)),
        "",
        "## Required Peer Basket",
        _markdown_table(
            pd.DataFrame(
                [{"symbol": code, "company": name} for code, name in BAIJIU_SYMBOLS.items()]
            )
        ),
        "",
        "## Analyst Checklist",
        "- Verify latest Feitian / core product wholesale prices from dated and reputable channel-price sources; if unavailable, state that price evidence is missing.",
        "- Compare contract liabilities against prior Q1/Q2/Q3/Q4 observations, not just the previous quarter.",
        "- Compare target against high-end and regional baijiu peers on growth, ROE, cash conversion, dividend/buyback yield, PE/PB, and channel health.",
        "- Separate bull/bear cases into volume, price, mix, channel inventory, and valuation-multiple assumptions.",
        "- If peer comparison or high-frequency price evidence fails, final rating should carry an explicit low-confidence tag.",
    ]
    return "\n".join(lines)
