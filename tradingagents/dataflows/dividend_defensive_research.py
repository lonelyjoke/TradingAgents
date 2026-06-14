from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta

from .config import get_config
from .industry_classifier import is_banking_entity
from .tushare_a_stock import (
    TushareDataError,
    _fetch_cashflow_data,
    _fetch_daily_basic_latest,
    _fetch_fina_indicator,
    _fetch_income_statement_data,
    _fetch_stock_basic,
    _fetch_stock_basic_universe,
    _format_value,
    _get_pro_client,
    _markdown_table,
    _to_tushare_date,
    is_a_share_symbol,
)
from .tushare_research import _latest_daily_basic_market


DEFENSIVE_INDUSTRY_TERMS = (
    "\u94f6\u884c",
    "\u767d\u9152",
    "\u5bb6\u7535",
    "\u7535\u529b",
    "\u6c34\u7535",
    "\u9ad8\u901f",
    "\u94c1\u8def",
    "\u6e2f\u53e3",
    "\u516c\u7528",
    "\u71c3\u6c14",
    "\u6c34\u52a1",
    "\u7535\u4fe1\u8fd0\u8425",
    "\u901a\u4fe1\u8fd0\u8425",
    "\u8fd0\u8425\u5546",
    "\u901a\u4fe1\u670d\u52a1",
    "\u592e\u4f01",
    "\u5e7f\u544a",
    "\u4f20\u5a92",
    "\u98df\u54c1",
    "\u996e\u6599",
)


@dataclass(frozen=True)
class DefensiveDividendAssessment:
    status: str
    rating: str
    dividend_stability: str
    coverage: str
    industry_durability: str
    valuation_buffer: str
    trap_risk: str


def _date_window(curr_date: str, years: int) -> tuple[str, str]:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    return _to_tushare_date(start_dt.strftime("%Y-%m-%d")), _to_tushare_date(curr_date)


def _numeric(value) -> float | None:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return None if pd.isna(parsed) else float(parsed)


def _fetch_dividends(symbol: str, curr_date: str, years: int) -> pd.DataFrame:
    start, end = _date_window(curr_date, years)
    pro = _get_pro_client()
    data = pro.dividend(
        ts_code=symbol,
        ann_date_start=start,
        ann_date_end=end,
    )
    if data is None or data.empty:
        return pd.DataFrame()
    keep = [
        "ts_code",
        "ann_date",
        "end_date",
        "div_proc",
        "cash_div_tax",
        "stk_div",
        "record_date",
        "ex_date",
        "pay_date",
    ]
    cols = [col for col in keep if col in data.columns]
    return data[cols].sort_values(["end_date", "ann_date"], ascending=False)


def _annual_dividend_summary(dividends: pd.DataFrame) -> pd.DataFrame:
    if dividends is None or dividends.empty or "end_date" not in dividends.columns:
        return pd.DataFrame(columns=["end_date", "cash_div_tax_sum", "events"])
    data = dividends.copy()
    data["cash_div_tax"] = pd.to_numeric(data.get("cash_div_tax"), errors="coerce")
    grouped = (
        data.dropna(subset=["cash_div_tax"])
        .groupby("end_date", dropna=False)
        .agg(cash_div_tax_sum=("cash_div_tax", "sum"), events=("cash_div_tax", "count"))
        .reset_index()
        .sort_values("end_date", ascending=False)
    )
    return grouped


def _annual_rows(data: pd.DataFrame, limit: int = 5) -> pd.DataFrame:
    if data is None or data.empty or "end_date" not in data.columns:
        return pd.DataFrame()
    rows = data.copy()
    rows["end_date"] = rows["end_date"].astype(str)
    annual = rows[rows["end_date"].str.endswith("1231")]
    return annual.sort_values("end_date", ascending=False).head(limit)


def _pct_change(first: float | None, last: float | None) -> float | None:
    if first in (None, 0) or last is None:
        return None
    return (last / first - 1.0) * 100


def _trend_summary(income: pd.DataFrame, cashflow: pd.DataFrame) -> pd.DataFrame:
    annual_income = _annual_rows(income)
    annual_cashflow = _annual_rows(cashflow)
    if annual_income.empty:
        return pd.DataFrame()
    cols = [col for col in ["end_date", "total_revenue", "n_income_attr_p"] if col in annual_income.columns]
    summary = annual_income[cols].copy()
    if not annual_cashflow.empty:
        keep = [col for col in ["end_date", "n_cashflow_act", "c_pay_acq_const_fiolta", "c_pay_dist_dpcp_int_exp"] if col in annual_cashflow.columns]
        summary = summary.merge(annual_cashflow[keep], on="end_date", how="left")
    for col in summary.columns:
        if col != "end_date":
            summary[col] = pd.to_numeric(summary[col], errors="coerce")
    if {"n_cashflow_act", "c_pay_acq_const_fiolta"} <= set(summary.columns):
        summary["free_cash_flow_proxy"] = summary["n_cashflow_act"] - summary["c_pay_acq_const_fiolta"].abs()
    if {"c_pay_dist_dpcp_int_exp", "n_income_attr_p"} <= set(summary.columns):
        summary["cash_distribution_to_profit"] = summary["c_pay_dist_dpcp_int_exp"].abs() / summary["n_income_attr_p"].abs()
    return summary


def _defensive_industry_hint(basic: pd.Series | None) -> bool:
    if basic is None:
        return False
    text = f"{basic.get('name', '')} {basic.get('industry', '')}"
    return any(term in text for term in DEFENSIVE_INDUSTRY_TERMS)


def _dividend_stats(annual_dividends: pd.DataFrame, daily_basic: pd.Series | None) -> dict[str, object]:
    values = pd.to_numeric(annual_dividends.get("cash_div_tax_sum", pd.Series(dtype=float)), errors="coerce").dropna()
    years = int(len(values))
    latest = float(values.iloc[0]) if years else None
    previous = float(values.iloc[1]) if years > 1 else None
    mean = float(values.mean()) if years else None
    cv = float(values.std(ddof=0) / mean) if years > 1 and mean not in (None, 0) else None
    cut = previous is not None and latest is not None and latest < previous * 0.75
    dv_ttm = None if daily_basic is None else _numeric(daily_basic.get("dv_ttm"))
    dv_ratio = None if daily_basic is None else _numeric(daily_basic.get("dv_ratio"))
    return {
        "dividend_years": years,
        "latest_cash_div_tax_sum": latest,
        "dividend_cv": cv,
        "recent_cut": cut,
        "dv_ttm": dv_ttm,
        "dv_ratio": dv_ratio,
    }


def _assess(
    *,
    basic: pd.Series | None,
    daily_basic: pd.Series | None,
    dividend_stats: dict[str, object],
    trend: pd.DataFrame,
    indicators: pd.DataFrame,
) -> DefensiveDividendAssessment:
    is_bank = is_banking_entity(basic=basic)
    defensive_industry = _defensive_industry_hint(basic)
    dv_ttm = dividend_stats.get("dv_ttm")
    dividend_years = int(dividend_stats.get("dividend_years") or 0)
    cv = dividend_stats.get("dividend_cv")
    recent_cut = bool(dividend_stats.get("recent_cut"))

    candidate = bool(
        (dv_ttm is not None and dv_ttm >= 2.0)
        or (dividend_years >= 4 and dv_ttm is not None and dv_ttm >= 1.0)
        or is_bank
        or defensive_industry
    )
    if not candidate:
        return DefensiveDividendAssessment(
            status="not_applicable",
            rating="not_applicable",
            dividend_stability="not_applicable",
            coverage="not_applicable",
            industry_durability="not_applicable",
            valuation_buffer="not_applicable",
            trap_risk="not_applicable",
        )

    stable = dividend_years >= 4 and not recent_cut and (cv is None or cv <= 0.35)
    dividend_stability = "pass" if stable else "watch" if dividend_years >= 2 and not recent_cut else "fail"

    latest_profit = None
    latest_ocf = None
    latest_fcf = None
    latest_dist_ratio = None
    if not trend.empty:
        latest = trend.iloc[0]
        latest_profit = _numeric(latest.get("n_income_attr_p"))
        latest_ocf = _numeric(latest.get("n_cashflow_act"))
        latest_fcf = _numeric(latest.get("free_cash_flow_proxy"))
        latest_dist_ratio = _numeric(latest.get("cash_distribution_to_profit"))
    coverage_pass = latest_profit is not None and latest_profit > 0
    if not is_bank:
        coverage_pass = coverage_pass and latest_ocf is not None and latest_ocf > 0
        if latest_dist_ratio is not None:
            coverage_pass = coverage_pass and latest_dist_ratio <= 0.85
    coverage = "pass" if coverage_pass else "watch" if latest_profit and latest_profit > 0 else "fail"

    revenue_change = None
    profit_change = None
    if not trend.empty and len(trend) >= 2:
        ordered = trend.sort_values("end_date")
        revenue_change = _pct_change(
            _numeric(ordered.iloc[0].get("total_revenue")),
            _numeric(ordered.iloc[-1].get("total_revenue")),
        )
        profit_change = _pct_change(
            _numeric(ordered.iloc[0].get("n_income_attr_p")),
            _numeric(ordered.iloc[-1].get("n_income_attr_p")),
        )
    durable = is_bank or defensive_industry or (
        (revenue_change is None or revenue_change > -15)
        and (profit_change is None or profit_change > -20)
    )
    industry_durability = "pass" if durable else "fail"

    pb = None if daily_basic is None else _numeric(daily_basic.get("pb"))
    pe_ttm = None if daily_basic is None else _numeric(daily_basic.get("pe_ttm"))
    valuation_buffer = "pass" if dv_ttm is not None and dv_ttm >= 3.0 else "watch"
    if pe_ttm is not None and pe_ttm > 35 and (dv_ttm is None or dv_ttm < 2.5):
        valuation_buffer = "fail"
    if pb is not None and pb > 5 and (dv_ttm is None or dv_ttm < 2.5):
        valuation_buffer = "fail"

    fail_count = [dividend_stability, coverage, industry_durability, valuation_buffer].count("fail")
    watch_count = [dividend_stability, coverage, industry_durability, valuation_buffer].count("watch")
    if fail_count >= 2 or (recent_cut and coverage == "fail"):
        rating = "weak"
        trap_risk = "high"
    elif fail_count == 1 or watch_count >= 2:
        rating = "medium"
        trap_risk = "medium"
    else:
        rating = "strong"
        trap_risk = "low"

    return DefensiveDividendAssessment(
        status="triggered",
        rating=rating,
        dividend_stability=dividend_stability,
        coverage=coverage,
        industry_durability=industry_durability,
        valuation_buffer=valuation_buffer,
        trap_risk=trap_risk,
    )


def _enrich_peer_financials(data: pd.DataFrame, curr_date: str, limit: int) -> pd.DataFrame:
    rows = []
    for _, row in data.head(limit).iterrows():
        symbol = str(row.get("ts_code") or "").strip()
        if not symbol:
            rows.append({})
            continue
        try:
            indicators = _fetch_fina_indicator(symbol, curr_date)
        except Exception:
            indicators = pd.DataFrame()
        if indicators is None or indicators.empty:
            rows.append({})
            continue
        ordered = indicators.copy()
        if "end_date" in ordered.columns:
            ordered["end_date"] = ordered["end_date"].astype(str)
            ordered = ordered.sort_values("end_date", ascending=False)
        latest = ordered.iloc[0]
        rows.append(
            {
                "roe": latest.get("roe"),
                "roa": latest.get("roa"),
                "netprofit_yoy": latest.get("netprofit_yoy"),
                "debt_to_assets": latest.get("debt_to_assets"),
            }
        )
    financials = pd.DataFrame(rows)
    return pd.concat([data.head(limit).reset_index(drop=True), financials], axis=1)


def _score_defensive_candidates(data: pd.DataFrame) -> pd.DataFrame:
    if data is None or data.empty:
        return pd.DataFrame()
    scored = data.copy()
    for col in ["dv_ttm", "pb", "pe_ttm", "roe", "roa", "netprofit_yoy", "debt_to_assets", "total_mv"]:
        if col in scored.columns:
            scored[col] = pd.to_numeric(scored[col], errors="coerce")
    scored["defensive_score"] = (
        scored.get("dv_ttm", pd.Series(dtype=float)).rank(pct=True).fillna(0.5) * 25
        + scored.get("roe", scored.get("roa", pd.Series(dtype=float))).rank(pct=True).fillna(0.5) * 20
        + (1 - scored.get("pb", pd.Series(dtype=float)).rank(pct=True)).fillna(0.5) * 15
        + (1 - scored.get("debt_to_assets", pd.Series(dtype=float)).rank(pct=True)).fillna(0.5) * 15
        + scored.get("netprofit_yoy", pd.Series(dtype=float)).rank(pct=True).fillna(0.5) * 15
        + scored.get("total_mv", pd.Series(dtype=float)).rank(pct=True).fillna(0.5) * 10
    )
    scored["defensive_score"] = scored["defensive_score"].round(1)
    return scored.sort_values("defensive_score", ascending=False)


def _peer_tables(symbol: str, basic: pd.Series | None, curr_date: str, trade_date: str | None, peer_limit: int) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    notes: list[str] = []
    try:
        universe = _fetch_stock_basic_universe()
    except Exception as exc:
        return pd.DataFrame(), pd.DataFrame(), [f"stock_basic universe unavailable: {exc}"]
    if universe is None or universe.empty or "ts_code" not in universe.columns:
        return pd.DataFrame(), pd.DataFrame(), ["stock_basic universe unavailable or missing ts_code."]

    try:
        market = _latest_daily_basic_market(trade_date) if trade_date else pd.DataFrame()
    except Exception as exc:
        market = pd.DataFrame()
        notes.append(f"daily_basic market snapshot unavailable: {exc}")
    if market is None or market.empty or "ts_code" not in market.columns:
        return pd.DataFrame(), pd.DataFrame(), notes + ["peer tables need daily_basic market snapshot."]

    merged = universe.merge(market, on="ts_code", how="inner")
    if "industry" not in merged.columns:
        merged["industry"] = ""
    industry = "" if basic is None else str(basic.get("industry") or "")
    same = merged[merged["industry"].astype(str) == industry].copy() if industry else pd.DataFrame()
    defensive_mask = merged.apply(
        lambda row: any(term in f"{row.get('name', '')} {row.get('industry', '')}" for term in DEFENSIVE_INDUSTRY_TERMS),
        axis=1,
    )
    high_yield_mask = pd.to_numeric(merged.get("dv_ttm"), errors="coerce") >= 2.5
    cross = merged[(defensive_mask | high_yield_mask) & (merged["ts_code"] != symbol)].copy()

    if not same.empty:
        same = _enrich_peer_financials(same.sort_values("total_mv", ascending=False), curr_date, peer_limit)
        same = _score_defensive_candidates(same)
    if not cross.empty:
        cross = _enrich_peer_financials(cross.sort_values("total_mv", ascending=False), curr_date, max(peer_limit, 16))
        cross = _score_defensive_candidates(cross).head(peer_limit)
    return same.head(peer_limit), cross.head(peer_limit), notes


def get_dividend_defensive_context(
    ticker: str,
    curr_date: str,
    look_back_years: int = 6,
    peer_limit: int = 10,
) -> str:
    """Assess whether an A-share target is a true defensive dividend candidate."""
    config = get_config()
    if not config.get("dividend_defensive_context_enabled", True):
        return "# Dividend defensive verification layer\n\nStatus: disabled"

    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Dividend defensive context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    notes: list[str] = []
    try:
        basic = _fetch_stock_basic(symbol)
    except Exception as exc:
        basic = None
        notes.append(f"stock_basic unavailable: {exc}")
    try:
        daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
    except Exception as exc:
        daily_basic = None
        notes.append(f"daily_basic unavailable: {exc}")
    try:
        dividends = _fetch_dividends(symbol, curr_date, look_back_years)
    except Exception as exc:
        dividends = pd.DataFrame()
        notes.append(f"dividend history unavailable: {exc}")
    annual_dividends = _annual_dividend_summary(dividends)
    try:
        income = _fetch_income_statement_data(symbol, curr_date, freq="annual", limit=max(look_back_years, 5))
    except Exception as exc:
        income = pd.DataFrame()
        notes.append(f"income statement unavailable: {exc}")
    try:
        cashflow = _fetch_cashflow_data(symbol, curr_date, freq="annual", limit=max(look_back_years, 5))
    except Exception as exc:
        cashflow = pd.DataFrame()
        notes.append(f"cash-flow statement unavailable: {exc}")
    try:
        indicators = _fetch_fina_indicator(symbol, curr_date)
    except Exception as exc:
        indicators = pd.DataFrame()
        notes.append(f"financial indicators unavailable: {exc}")

    trend = _trend_summary(income, cashflow)
    dividend_stats = _dividend_stats(annual_dividends, daily_basic)
    assessment = _assess(
        basic=basic,
        daily_basic=daily_basic,
        dividend_stats=dividend_stats,
        trend=trend,
        indicators=indicators,
    )
    trade_date = None if daily_basic is None else str(daily_basic.get("trade_date") or "")
    same_peers, cross_peers, peer_notes = _peer_tables(symbol, basic, curr_date, trade_date, peer_limit)
    notes.extend(peer_notes)

    snapshot = pd.DataFrame(
        [
            {
                "metric": "dv_ttm",
                "value": dividend_stats.get("dv_ttm"),
                "interpretation": "Trailing dividend yield from daily_basic; high yield alone is not enough.",
            },
            {
                "metric": "dividend_years",
                "value": dividend_stats.get("dividend_years"),
                "interpretation": "Count of recent end_dates with cash_div_tax records.",
            },
            {
                "metric": "dividend_cv",
                "value": dividend_stats.get("dividend_cv"),
                "interpretation": "Lower variation implies more predictable dividends.",
            },
            {
                "metric": "recent_cut",
                "value": dividend_stats.get("recent_cut"),
                "interpretation": "A material recent cut is a dividend-trap warning.",
            },
        ]
    )
    valuation = pd.DataFrame(
        [
            {
                "trade_date": trade_date,
                "close": None if daily_basic is None else daily_basic.get("close"),
                "pe_ttm": None if daily_basic is None else daily_basic.get("pe_ttm"),
                "pb": None if daily_basic is None else daily_basic.get("pb"),
                "dv_ttm": dividend_stats.get("dv_ttm"),
                "total_mv": None if daily_basic is None else daily_basic.get("total_mv"),
            }
        ]
    )
    peer_cols = [
        "ts_code",
        "name",
        "industry",
        "total_mv",
        "pe_ttm",
        "pb",
        "dv_ttm",
        "roe",
        "roa",
        "netprofit_yoy",
        "debt_to_assets",
        "defensive_score",
    ]

    lines = [
        f"# Dividend defensive verification context for {symbol} as of {curr_date}",
        "",
        f"Status: {assessment.status}",
        f"Defensive Dividend Rating: {assessment.rating}",
        f"- Company: {_format_value(None if basic is None else basic.get('name'))}",
        f"- Industry: {_format_value(None if basic is None else basic.get('industry'))}",
        f"- Dividend stability: {assessment.dividend_stability}",
        f"- Dividend coverage: {assessment.coverage}",
        f"- Industry durability: {assessment.industry_durability}",
        f"- Valuation buffer: {assessment.valuation_buffer}",
        f"- Dividend trap risk: {assessment.trap_risk}",
        "",
        "## Routing Instruction",
    ]
    if assessment.status == "not_applicable":
        lines.extend(
            [
                "- This layer did not find enough dividend/defensive evidence to treat the target as a defensive dividend asset.",
                "- Do not force a high-dividend or cash-cow thesis unless another supplied context provides direct evidence.",
            ]
        )
    else:
        lines.extend(
            [
                "- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.",
                "- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.",
                "- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.",
            ]
        )
    lines.extend(
        [
            "",
            "## Dividend And Valuation Snapshot",
            _markdown_table(snapshot),
            "",
            "## Current Valuation Reference",
            _markdown_table(valuation),
            "",
            "## Annual Dividend History",
            _markdown_table(annual_dividends.head(look_back_years)),
            "",
            "## Profit And Cash-Flow Coverage",
            _markdown_table(trend.head(look_back_years)),
            "",
            "## Same-Industry Defensive Alternatives",
            _markdown_table(same_peers[[col for col in peer_cols if col in same_peers.columns]] if not same_peers.empty else pd.DataFrame()),
            "",
            "## Cross-Industry Defensive Alternatives",
            _markdown_table(cross_peers[[col for col in peer_cols if col in cross_peers.columns]] if not cross_peers.empty else pd.DataFrame()),
            "",
            "## Analyst Instructions",
            "- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.",
            "- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.",
            "- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.",
            "- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.",
            "- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.",
            "",
            "## Coverage Notes",
        ]
    )
    lines.extend([f"- {note}" for note in notes] if notes else ["- No retrieval errors recorded."])
    return "\n".join(lines)
