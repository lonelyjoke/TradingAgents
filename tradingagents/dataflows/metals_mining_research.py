"""Metals-and-mining-specific verification context for A-share companies."""

from __future__ import annotations

import re
from dataclasses import dataclass

import pandas as pd

from .commodity_research import (
    METAL_FUTURES_SOURCE_REGISTRY,
    _infer_products,
    get_commodity_context,
)
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


METALS_MINING_COMPANIES = {
    "600547.SH": {
        "name": "Shandong Gold",
        "metals": ("Gold",),
        "business_model": "gold mining with smelting/trading exposure",
        "watchlist": (
            "equity gold output, grade, recovery rate, and mine-by-mine ramp",
            "cash cost / AISC per gram and sustaining capex",
            "gold-price sensitivity, hedging, and inventory mark-to-market",
            "mine life, reserves, goodwill, leverage, and acquisition returns",
        ),
    },
    "000975.SZ": {
        "name": "Shanjin International Gold",
        "metals": ("Gold",),
        "business_model": "gold miner with domestic and overseas assets",
        "watchlist": (
            "equity production growth and mine-grade durability",
            "AISC per gram, overseas jurisdiction risk, and FX exposure",
            "project ramp, reserves replacement, and acquisition discipline",
        ),
    },
    "600489.SH": {
        "name": "Zhongjin Gold",
        "metals": ("Gold",),
        "business_model": "gold mining plus smelting / refining platform",
        "watchlist": (
            "mining output versus smelting/refining contribution",
            "unit cost, grade, reserve life, and project ramp",
            "inventory, hedging, and working-capital volatility",
        ),
    },
    "601899.SH": {
        "name": "Zijin Mining",
        "metals": ("Copper", "Gold"),
        "business_model": "global copper-gold mining platform",
        "watchlist": (
            "equity copper/gold output and major-project ramp schedule",
            "mine-by-mine cost curve, grade, recovery, and capex intensity",
            "jurisdiction risk, leverage, FX, and acquisition integration",
        ),
    },
    "600362.SH": {
        "name": "Jiangxi Copper",
        "metals": ("Copper",),
        "business_model": "copper mining, smelting, and trading platform",
        "watchlist": (
            "mine output versus smelting / trading mix",
            "TC/RC, cathode copper spread, inventory, and working capital",
            "copper-price beta versus smelting-margin compression",
        ),
    },
    "000878.SZ": {
        "name": "Yunnan Copper",
        "metals": ("Copper",),
        "business_model": "copper smelting with upstream resource exposure",
        "watchlist": (
            "self-owned mine contribution and concentrate sourcing",
            "TC/RC, energy cost, inventory, and cash conversion",
            "copper-price pass-through versus smelting margin",
        ),
    },
    "000630.SZ": {
        "name": "Tongling Nonferrous",
        "metals": ("Copper",),
        "business_model": "copper mining / smelting / processing company",
        "watchlist": (
            "mining share, smelting utilization, and processing margin",
            "TC/RC, inventory, derivatives, and leverage",
            "capex returns and cash-flow conversion",
        ),
    },
    "601600.SH": {
        "name": "Chalco",
        "metals": ("Aluminum",),
        "business_model": "integrated aluminum and alumina producer",
        "watchlist": (
            "aluminum supply ceiling, domestic-overseas price gap, and import/export arbitrage",
            "aluminum price, alumina cost, power cost, and smelting capacity utilization",
            "downstream demand bridge across property, grid/PV, EV lightweighting, exports, and general manufacturing",
            "alumina self-sufficiency, power-cost position, integrated-margin resilience, and inventory",
            "capex, leverage, dividend coverage, and cash-flow sensitivity to aluminum/alumina spreads",
        ),
    },
    "000807.SZ": {
        "name": "Yunnan Aluminium",
        "metals": ("Aluminum",),
        "business_model": "hydropower-linked aluminum producer",
        "watchlist": (
            "aluminum price, alumina cost, hydro availability, and power tariff",
            "capacity utilization, carbon policy, and smelting margin",
            "cash conversion and dividend durability through downcycles",
        ),
    },
    "002460.SZ": {
        "name": "Ganfeng Lithium",
        "metals": ("Lithium carbonate",),
        "business_model": "lithium resource, processing, and battery-materials platform",
        "watchlist": (
            "lithium carbonate price, spodumene cost, inventory, and impairment",
            "mine ramp, processing utilization, and downstream demand",
            "equity-accounted assets, capex, and cycle-trough survival",
        ),
    },
    "002466.SZ": {
        "name": "Tianqi Lithium",
        "metals": ("Lithium carbonate",),
        "business_model": "lithium resource and processing company",
        "watchlist": (
            "lithium price sensitivity and spodumene / carbonate spread",
            "asset leverage, dividend capacity, and equity-accounted earnings",
            "project ramp, inventory, and impairment risk",
        ),
    },
}


METALS_MINING_TERMS = (
    "\u6709\u8272\u91d1\u5c5e",
    "\u9ec4\u91d1",
    "\u767d\u94f6",
    "\u94dc",
    "\u94dd",
    "\u950c",
    "\u94c5",
    "\u954d",
    "\u9521",
    "\u9502",
    "\u7a00\u571f",
    "\u77ff\u5c71",
    "\u77ff\u4e1a",
    "\u91c7\u77ff",
    "\u51b6\u70bc",
    "\u77ff\u77f3",
    "\u54c1\u4f4d",
    "\u50a8\u91cf",
    "\u6743\u76ca\u4ea7\u91cf",
    "\u8fbe\u4ea7",
    "AISC",
    "LME",
    "COMEX",
)

METALS_EVIDENCE_TERMS = (
    "\u8d44\u6e90\u50a8\u91cf",
    "\u50a8\u91cf",
    "\u54c1\u4f4d",
    "\u6743\u76ca\u4ea7\u91cf",
    "\u4ea7\u91cf",
    "\u5355\u4f4d\u6210\u672c",
    "\u5b8c\u5168\u6210\u672c",
    "\u73b0\u91d1\u6210\u672c",
    "\u91d1\u4ef7",
    "\u94dc\u4ef7",
    "\u94dd\u4ef7",
    "\u9502\u4ef7",
    "\u5957\u671f\u4fdd\u503c",
    "\u884d\u751f\u91d1\u878d\u5de5\u5177",
    "\u5b58\u8d27",
    "\u5728\u5efa\u5de5\u7a0b",
    "\u8d44\u672c\u5f00\u652f",
    "\u77ff\u5c71",
    "\u51b6\u70bc",
    "\u52a0\u5de5\u8d39",
    "AISC",
    "TC",
    "RC",
)

MISSING_METALS_ITEMS = (
    "resource / reserve tonnage, grade, recovery rate, and mine life",
    "equity output by mine, ramp schedule, and production guidance",
    "cash cost, AISC, sustaining capex, and unit cost in RMB and USD terms",
    "mining versus smelting / refining / trading split and segment margins",
    "commodity-price sensitivity table across metal price, FX, volume, and cost",
    "inventory, hedging / derivatives, working-capital, and impairment exposure",
    "project capex, construction-in-progress, jurisdiction risk, and NAV / SOTP bridge",
)

NONFERROUS_CYCLE_GATE_ROWS = (
    {
        "layer": "Industry Cycle View",
        "question": "Is the metal in structural tightness, ordinary restocking, or a fading price cycle?",
        "evidence_rule": "Test supply ceiling/capacity policy, inventories, operating rates, LME/SHFE spreads, imports/exports, and downstream demand before judging prosperity.",
    },
    {
        "layer": "Company Expression View",
        "question": "Does this company express the cycle through scarce resources, low-cost smelting, or pass-through processing?",
        "evidence_rule": "Separate resource ownership, alumina/self-supply, power cost, equity output, segment margin, capex, and working-capital conversion.",
    },
    {
        "layer": "Valuation/Odds View",
        "question": "Is low PE a peak-earnings trap or an ROE re-rating path despite high PB?",
        "evidence_rule": "Compare TTM and forward/normalized PE, PB-ROE, dividend coverage, trough valuation, and peer opportunity cost rather than using PB alone.",
    },
    {
        "layer": "Tactical Attribution View",
        "question": "Was the recent move caused by metal price, sector beta, company residual, news/rumor, or liquidity/positioning?",
        "evidence_rule": "Use same-metal equities, cross-metal equities, futures, announcements, news/rumor probe, turnover, and trend state before calling emotion-kill or fundamental repricing.",
    },
)

ALUMINUM_DEMAND_BRIDGE_ROWS = (
    {
        "channel": "Property / construction",
        "analyst_rule": "Treat as a cyclical drag or stabilizer; do not let it erase other demand channels without quantified evidence.",
    },
    {
        "channel": "Grid, PV, EV, lightweighting",
        "analyst_rule": "Use as core demand support only when volume, utilization, order, or policy evidence is supplied; otherwise mark as positive assumption.",
    },
    {
        "channel": "Exports and domestic-overseas arbitrage",
        "analyst_rule": "Check LME/SHFE spread, import/export incentives, tariffs, and inventory movement before claiming price-gap upside.",
    },
    {
        "channel": "AI / robotics / new manufacturing",
        "analyst_rule": "Keep as indirect optionality unless aluminum volume linkage is quantified; it can lift sentiment but should not dominate the base case.",
    },
    {
        "channel": "Monetary / inflation beta",
        "analyst_rule": "Separate broad liquidity beta from physical tightness; commodity inflation can help but does not replace supply-demand proof.",
    },
)


@dataclass(frozen=True)
class MetalsMiningProfile:
    symbol: str
    company_name: str
    industry: str
    business_model: str
    metals: tuple[str, ...]
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


def _inferred_metals(symbol: str) -> tuple[str, ...]:
    mapping = _infer_products(symbol)
    metals = []
    for product in mapping.get("products", []):
        name = str(product.get("name", ""))
        if name in METAL_FUTURES_SOURCE_REGISTRY and name not in metals:
            metals.append(name)
    return tuple(metals)


def _company_profile(symbol: str, curr_date: str, look_back_days: int) -> MetalsMiningProfile | None:
    basic = _fetch_stock_basic(symbol)
    curated = METALS_MINING_COMPANIES.get(symbol, {})
    company_name = str(curated.get("name") or symbol)
    industry = ""
    if basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    _, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:4000] for _, text in report_texts[:4])
    inferred_metals = _inferred_metals(symbol)
    if symbol in METALS_MINING_COMPANIES:
        reason = "curated A-share metals / mining ticker list"
    elif inferred_metals:
        reason = "commodity map contains exchange-traded metal products"
    elif _contains_terms(METALS_MINING_TERMS, company_name, industry, text_probe):
        reason = "company name / Tushare industry / filing text contains metals-mining terms"
    else:
        return None

    metals = tuple(curated.get("metals") or inferred_metals)
    return MetalsMiningProfile(
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        business_model=str(curated.get("business_model", "metals / mining / smelting company")),
        metals=metals,
        watchlist=tuple(
            curated.get(
                "watchlist",
                (
                    "resource / reserve quality, grade, and equity production",
                    "unit cost, AISC, sustaining capex, and project ramp",
                    "commodity price, FX, inventory, hedging, and impairment sensitivity",
                    "mining / smelting / trading split, leverage, and NAV / SOTP bridge",
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
        "netprofit_yoy": None if latest is None else _numeric(latest.get("netprofit_yoy")),
        "debt_to_assets": None if latest is None else _numeric(latest.get("debt_to_assets")),
        "ocf_yoy": None if latest is None else _numeric(latest.get("ocf_yoy")),
    }
    return pd.DataFrame([payload])


def _price_source_rows(profile: MetalsMiningProfile) -> pd.DataFrame:
    rows = []
    for metal in profile.metals:
        source = METAL_FUTURES_SOURCE_REGISTRY.get(metal)
        if source is None:
            rows.append(
                {
                    "metal": metal,
                    "domestic_chain": "not mapped in Tushare futures registry",
                    "overseas_cross_check": "use official/licensed spot benchmark before quantifying",
                    "analyst_rule": "treat price as unverified until a source/date/unit is shown",
                }
            )
            continue
        rows.append(
            {
                "metal": metal,
                "domestic_chain": (
                    f"Tushare fut_daily -> {source['domestic_exchange']} "
                    f"{source['tushare_prefix']} contracts ({source['contract_example']})"
                ),
                "overseas_cross_check": source["overseas_cross_checks"],
                "analyst_rule": source["coverage"],
            }
        )
    if not rows:
        rows.append(
            {
                "metal": "N/A",
                "domestic_chain": "no exchange-traded metal product inferred",
                "overseas_cross_check": "N/A",
                "analyst_rule": "do not force commodity-price claims without a mapped source",
            }
        )
    return pd.DataFrame(rows)


def _business_model_gate() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "bucket": "Mining asset quality",
                "must_verify": "reserve / resource tonnage, grade, recovery rate, equity output, mine life",
                "valuation_rule": "higher multiple only when reserve quality and low-cost output are evidenced",
            },
            {
                "bucket": "Unit economics",
                "must_verify": "cash cost, AISC, sustaining capex, energy/labor/input cost, FX",
                "valuation_rule": "cycle upside needs cost-curve resilience, not only rising metal prices",
            },
            {
                "bucket": "Smelting / trading split",
                "must_verify": "TC/RC, processing margin, inventory exposure, realized price versus exchange proxy",
                "valuation_rule": "do not value smelting/trading earnings like scarce mining NAV",
            },
            {
                "bucket": "Project ramp / capex",
                "must_verify": "construction progress, capex budget, commissioning, permitting, jurisdiction risk",
                "valuation_rule": "NAV/SOTP should haircut delayed, over-budget, or high-risk projects",
            },
            {
                "bucket": "Risk management",
                "must_verify": "hedging, derivatives, inventory marks, debt maturity, FX, impairment",
                "valuation_rule": "earnings quality haircut when commodity beta is amplified by leverage or MTM risk",
            },
        ]
    )


def _nonferrous_cycle_gate() -> pd.DataFrame:
    return pd.DataFrame(list(NONFERROUS_CYCLE_GATE_ROWS))


def _aluminum_demand_bridge(profile: MetalsMiningProfile) -> pd.DataFrame:
    if not any(str(metal).lower() == "aluminum" for metal in profile.metals):
        return pd.DataFrame()
    return pd.DataFrame(list(ALUMINUM_DEMAND_BRIDGE_ROWS))


def _report_snippets(profile: MetalsMiningProfile) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    terms = METALS_EVIDENCE_TERMS + profile.metals + tuple(profile.watchlist)
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
                "debt_to_assets": None if latest is None else _numeric(latest.get("debt_to_assets")),
                "netprofit_yoy": None if latest is None else _numeric(latest.get("netprofit_yoy")),
            }
        )
    return pd.DataFrame(rows)


def _render_missing_items() -> str:
    return "\n".join(f"- {item}" for item in MISSING_METALS_ITEMS)


def get_metals_mining_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
    peer_limit: int = 8,
) -> str:
    """Return a gated metals/mining research layer for A-share companies."""
    symbol = str(ticker or "").strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Metals-mining verification context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Metals-mining verification context for {symbol}\n\n"
            "- Status: not_applicable\n"
            "- Reason: no curated metals/mining mapping, no exchange-traded metal product mapping, and no mining / smelting / metal terms found in company name, industry, or recent filing text.\n"
            "- Do not force reserve, grade, AISC, mine NAV, or commodity-price sensitivity logic into this stock unless primary evidence proves metals/mining exposure."
        )

    watchlist = "\n".join(f"- {item}" for item in profile.watchlist)
    snapshot = _financial_snapshot(symbol, curr_date)
    snippets = _report_snippets(profile)
    peer_screen = _peer_screen(symbol, curr_date, limit=peer_limit)
    price_context = get_commodity_context(symbol, curr_date, look_back_days=min(180, max(30, look_back_days)))
    aluminum_bridge = _aluminum_demand_bridge(profile)
    snippet_block = (
        _markdown_table(snippets)
        if not snippets.empty
        else "No readable filing snippets found around mining / metal terms; treat reserve, grade, unit-cost, and project-ramp evidence as a data gap, not as negative evidence."
    )

    lines = [
        f"# Metals-mining verification context for {symbol} as of {curr_date}",
        "",
        "- Status: triggered",
        f"- Company: {profile.company_name}",
        f"- Tushare industry: {profile.industry or 'N/A'}",
        f"- Business model: {profile.business_model}",
        f"- Metals covered: {', '.join(profile.metals) if profile.metals else 'N/A'}",
        f"- Trigger reason: {profile.trigger_reason}",
        "",
        "## Company Watchlist",
        watchlist,
        "",
        "## Metals / Mining KPI Screen",
        _markdown_table(snapshot),
        "",
        "## Metal Price Source Chain Audit",
        _markdown_table(_price_source_rows(profile)),
        "",
        "## Commodity Price Evidence Handoff",
        price_context,
        "",
        "## Business Model / Evidence Gate",
        _markdown_table(_business_model_gate()),
        "",
        "## Nonferrous Cycle Rating Gate",
        _markdown_table(_nonferrous_cycle_gate()),
        "",
        "## Aluminum Demand Bridge",
        _markdown_table(aluminum_bridge)
        if not aluminum_bridge.empty
        else "Not an aluminum-focused profile; use the broader nonferrous cycle gate instead.",
        "",
        "## Filing Text Evidence Snippets",
        snippet_block,
        "",
        "## Metals / Mining Peer Screen",
        _markdown_table(peer_screen) if not peer_screen.empty else "Metals / mining peer screen unavailable.",
        "",
        "## Required Metals Valuation Bridge",
        "- Build bull/base/bear cases from metal price, equity output, unit cost/AISC, FX, sustaining capex, and tax / minority interest.",
        "- Separate mining NAV from smelting, refining, processing, trading, and investment income. Do not assign scarce-resource multiples to pass-through volume.",
        "- Use mine-by-mine or segment SOTP when material assets have different metals, grades, jurisdictions, ramp status, or cost curves.",
        "- Treat domestic exchange futures as timely proxies. Overseas COMEX/LME/LBMA or licensed spot sources are cross-checks unless explicitly fetched and dated.",
        "- Safety-price work must use cycle-trough metal prices, survivable balance sheet, maintenance capex, and historical/peer trough valuation floors.",
        "- For nonferrous names, split the rating into Industry Cycle View, Company Expression View, Valuation/Odds View, and Tactical Attribution View before issuing the final action.",
        "- A low PE / high PB setup must be tested as either peak-earnings trap or ROE re-rating; PB alone is not enough for Underweight when earnings, cash flow, and dividends are being released.",
        "- One-quarter receivables, contract liabilities, inventory, or impairment direction can cap conviction, but should not decide the rating without seasonality, aging, peer comparison, and cash-conversion evidence.",
        "",
        "## Research Gaps To Close Before High Conviction",
        _render_missing_items(),
        "",
        "## Analyst Instructions",
        "- Treat this as the specialist metals / mining layer. It should override generic manufacturing or broad commodity framing when the target is a miner, smelter, or metal resource company.",
        "- Price beta is not enough: connect exchange prices to realized selling price, volume, cost curve, inventory, hedging, capex, and balance-sheet survival.",
        "- Missing reserve, grade, equity output, AISC, project-ramp, hedging, or NAV/SOTP evidence caps conviction and belongs in research gaps.",
        "- If the final action is Underweight/Sell despite structural supply constraints, low PE, dividend support, or visible profit release, explicitly prove the profit-center downshift, cash-cycle deterioration, superior peer alternative, or over-pricing path.",
    ]
    return "\n".join(lines)
