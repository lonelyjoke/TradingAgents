from __future__ import annotations

from dataclasses import dataclass
import re

import pandas as pd

from .industry_identity import has_lithium_battery_symbol_hint
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


BUILDING_MATERIAL_SYMBOLS = {
    "600585.SH": "海螺水泥",
    "000401.SZ": "冀东水泥",
    "600801.SH": "华新水泥",
    "000672.SZ": "上峰水泥",
    "002233.SZ": "塔牌集团",
    "601992.SH": "金隅集团",
    "002271.SZ": "东方雨虹",
    "300737.SZ": "科顺股份",
    "603737.SH": "三棵树",
    "000786.SZ": "北新建材",
    "002372.SZ": "伟星新材",
    "600176.SH": "中国巨石",
    "601636.SH": "旗滨集团",
    "002918.SZ": "蒙娜丽莎",
    "002791.SZ": "坚朗五金",
    "605006.SH": "山东玻纤",
    "002043.SZ": "兔宝宝",
    "603378.SH": "亚士创能",
}

SUBSECTOR_TERMS = {
    "cement": ("水泥", "熟料", "骨料", "矿粉", "混凝土", "商混"),
    "waterproof": ("防水", "卷材", "涂料", "砂浆", "建筑修缮"),
    "gypsum_board": ("石膏板", "龙骨", "轻钢龙骨", "北新"),
    "fiberglass_glass": ("玻纤", "玻璃纤维", "电子布", "玻璃", "浮法", "光伏玻璃"),
    "pipe": ("管材", "管件", "PPR", "PVC", "PE管", "给排水"),
    "coating": ("涂料", "乳胶漆", "保温", "装饰"),
    "ceramic": ("瓷砖", "陶瓷", "岩板", "卫浴"),
    "hardware": ("五金", "门窗", "幕墙", "紧固件"),
    "wood_panel": ("板材", "人造板", "胶合板", "生态板"),
}

BUILDING_MATERIAL_PRODUCT_TERMS = tuple(
    sorted({term for terms in SUBSECTOR_TERMS.values() for term in terms})
) + (
    "建材",
    "建筑材料",
)

BUILDING_MATERIAL_DEMAND_TERMS = (
    "地产",
    "基建",
    "竣工",
    "旧改",
    "城中村",
)

BUILDING_MATERIAL_TERMS = BUILDING_MATERIAL_PRODUCT_TERMS + BUILDING_MATERIAL_DEMAND_TERMS

SUBSECTOR_DRIVER_ROWS = {
    "cement": (
        ("Demand", "real-estate new starts/completion, infrastructure construction, regional shipment rate"),
        ("Supply", "capacity replacement, staggered production, clinker utilization, regional discipline"),
        ("Price/Cost", "cement/clinker ASP, coal/power cost, unit cost, inventory"),
        ("Forward signals", "contract liabilities are weaker than price/shipment data for spot sales; use cautiously"),
    ),
    "waterproof": (
        ("Demand", "property completion, repair/renovation, infrastructure waterproofing, channel mix"),
        ("Supply", "industry clean-up after credit stress, low-price competition, dealer inventory"),
        ("Price/Cost", "asphalt, emulsion, polyester tire-base cloth, gross margin by product/channel"),
        ("Forward signals", "receivables, notes, impairment, cash collected from customers, distributor quality"),
    ),
    "gypsum_board": (
        ("Demand", "completion/renovation, commercial fit-out, hospital/school/public buildings"),
        ("Supply", "regional capacity, brand/channel density, product mix upgrade"),
        ("Price/Cost", "waste paper/gypsum/energy, unit manufacturing cost, premium board share"),
        ("Forward signals", "segment margin and channel inventory matter more than headline revenue"),
    ),
    "fiberglass_glass": (
        ("Demand", "wind power, electronics, auto lightweighting, PV/architectural glass demand"),
        ("Supply", "new capacity ignition/cold repair, inventory, export mix"),
        ("Price/Cost", "roving/electronic yarn/electronic cloth/glass ASP, soda ash/gas/electricity"),
        ("Forward signals", "inventory and ASP inflection decide earnings beta"),
    ),
    "pipe": (
        ("Demand", "retail renovation, municipal water/gas, old-community renovation"),
        ("Supply", "brand/channel share, dealer health, project-versus-retail mix"),
        ("Price/Cost", "PVC/PE/PPR resin, copper/brass accessories, gross margin by product"),
        ("Forward signals", "retail channel cash conversion and receivables separate quality from scale"),
    ),
    "coating": (
        ("Demand", "new-home completion, renovation, engineering channel, retail repaint"),
        ("Supply", "channel inventory, dealer rebates, brand concentration"),
        ("Price/Cost", "titanium dioxide, emulsion, solvents, packaging, product mix"),
        ("Forward signals", "receivables and impairment decide whether revenue quality is investable"),
    ),
    "ceramic": (
        ("Demand", "property completion, renovation, export, distributor/store traffic"),
        ("Supply", "kiln utilization, regional capacity exits, energy constraints"),
        ("Price/Cost", "gas/coal/electricity, tile ASP, inventory markdown"),
        ("Forward signals", "inventory, receivables, and dealer health usually lead earnings risk"),
    ),
    "hardware": (
        ("Demand", "curtain wall/door-window projects, completion cycle, export projects"),
        ("Supply", "SKU breadth, service network, project-bidding discipline"),
        ("Price/Cost", "steel/aluminium/zinc alloy, product mix and project margin"),
        ("Forward signals", "receivables aging and credit impairment are core risk variables"),
    ),
    "wood_panel": (
        ("Demand", "home furnishing, renovation, channel/store traffic"),
        ("Supply", "brand channel, upstream board capacity, certification barriers"),
        ("Price/Cost", "wood pulp/logs/resin, product mix, retail pricing"),
        ("Forward signals", "retail order quality and dealer inventory matter more than broad property beta"),
    ),
}


@dataclass(frozen=True)
class BuildingMaterialsProfile:
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


def _contains_terms(terms: tuple[str, ...], *parts: object) -> bool:
    text = " ".join(str(part or "") for part in parts)
    return any(term in text for term in terms)


def _term_hit_count(terms: tuple[str, ...], text: str) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def _filing_has_building_material_business(text: str) -> bool:
    """Require product-to-business economics, not downstream-use mentions."""
    if any(
        phrase in text
        for phrase in ("并非建材", "不属于建材", "非建材业务", "not a building-material")
    ):
        return False
    identity_prefix = r"(?:主营业务(?:为|包括|涵盖)|主要产品(?:为|包括)|核心产品(?:为|包括)|分产品)"
    economic_suffix = r"(?:营业收入|销售收入|产销量|销量|产能|生产销售|毛利率)"
    product_pattern = "(?:" + "|".join(
        re.escape(term) for term in BUILDING_MATERIAL_PRODUCT_TERMS
    ) + ")"
    return bool(
        re.search(identity_prefix + r".{0,80}" + product_pattern, text, re.I)
        or re.search(product_pattern + r".{0,35}" + economic_suffix, text, re.I)
    )


def _detect_subsectors(*parts: object) -> tuple[str, ...]:
    text = " ".join(str(part or "") for part in parts)
    matches = [
        name
        for name, terms in SUBSECTOR_TERMS.items()
        if any(term.lower() in text.lower() for term in terms)
    ]
    return tuple(matches or ["general_building_materials"])


def _company_profile(
    symbol: str, curr_date: str, look_back_days: int
) -> BuildingMaterialsProfile | None:
    basic = _safe_fetch("stock_basic", _fetch_stock_basic, symbol)
    company_name = BUILDING_MATERIAL_SYMBOLS.get(symbol, symbol)
    industry = ""
    if not isinstance(basic, TushareDataError) and basic is not None:
        company_name = _format_value(basic.get("name")) or company_name
        industry = _format_value(basic.get("industry"))

    reports, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    text_probe = " ".join(text[:3000] for _, text in report_texts[:4])

    if symbol in BUILDING_MATERIAL_SYMBOLS:
        reason = "curated A-share building-materials ticker list"
    elif _contains_terms(BUILDING_MATERIAL_PRODUCT_TERMS, company_name, industry):
        reason = "company name or Tushare industry identifies a building-material business"
    elif (
        _term_hit_count(BUILDING_MATERIAL_PRODUCT_TERMS, text_probe) >= 2
        and _filing_has_building_material_business(text_probe)
    ):
        reason = "filing text contains repeated building-material products plus revenue/business evidence"
    else:
        return None

    subsectors = _detect_subsectors(company_name, industry, text_probe)
    return BuildingMaterialsProfile(
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
    if "end_date" in rows.columns:
        rows["end_date"] = rows["end_date"].astype(str)
        rows = rows.sort_values("end_date", ascending=False)
    return rows.head(limit)


def _growth_margin_table(
    income: pd.DataFrame | TushareDataError,
    indicators: pd.DataFrame | TushareDataError,
) -> pd.DataFrame:
    rows = _latest_rows(
        income,
        ["end_date", "total_revenue", "revenue", "n_income_attr_p", "n_income"],
        limit=8,
    )
    if rows.empty:
        return rows
    for col in ["total_revenue", "revenue", "n_income_attr_p", "n_income"]:
        if col in rows.columns:
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
            rows[f"{col}_yoy"] = rows[col].pct_change(-1).mul(100).round(2)

    indicator_rows = _latest_rows(
        indicators,
        ["end_date", "grossprofit_margin", "netprofit_margin", "roe", "debt_to_assets"],
        limit=8,
    )
    if not indicator_rows.empty:
        rows = rows.merge(indicator_rows, on="end_date", how="left")
    return rows.head(6)


def _working_capital_table(balance: pd.DataFrame | TushareDataError) -> pd.DataFrame:
    rows = _latest_rows(
        balance,
        [
            "end_date",
            "accounts_receiv",
            "notes_receiv",
            "contract_asset",
            "inventories",
            "contract_liab",
            "adv_receipts",
            "money_cap",
        ],
        limit=8,
    )
    if rows.empty:
        return rows
    for col in rows.columns:
        if col != "end_date":
            rows[col] = pd.to_numeric(rows[col], errors="coerce")
            rows[f"{col}_qoq"] = rows[col].pct_change(-1).mul(100).round(2)
    return rows.head(6)


def _cash_quality_table(
    cashflow: pd.DataFrame | TushareDataError,
    income: pd.DataFrame | TushareDataError,
) -> pd.DataFrame:
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


def _segment_snippets(profile: BuildingMaterialsProfile) -> list[str]:
    snippets: list[str] = []
    terms = BUILDING_MATERIAL_TERMS + ("毛利率", "销量", "单价", "成本", "应收", "存货")
    for title, text in profile.report_texts[:5]:
        lowered = text.lower()
        for term in terms:
            idx = lowered.find(str(term).lower())
            if idx < 0:
                continue
            start = max(0, idx - 220)
            end = min(len(text), idx + 520)
            compact = _compact_text(text[start:end], limit=620)
            if compact and compact not in snippets:
                snippets.append(f"- {title}: {compact}")
            break
        if len(snippets) >= 6:
            break
    return snippets


def _driver_table(subsectors: tuple[str, ...]) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    used = [item for item in subsectors if item in SUBSECTOR_DRIVER_ROWS]
    if not used:
        used = ["cement", "waterproof", "fiberglass_glass"]
    for subsector in used[:4]:
        for driver, checkpoint in SUBSECTOR_DRIVER_ROWS[subsector]:
            rows.append(
                {
                    "subsector": subsector,
                    "driver": driver,
                    "buy_side_checkpoint": checkpoint,
                }
            )
    return pd.DataFrame(rows)


def get_building_materials_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Return a gated building-materials research pack for A-share companies."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        return (
            "# Building-materials verification context unavailable\n\n"
            f"- Reason: expected A-share symbol; got {ticker!r}."
        )

    if has_lithium_battery_symbol_hint(symbol):
        return (
            f"# Building-materials verification context for {symbol} as of {curr_date}\n\n"
            "- Status: not_applicable\n"
            "- Trigger: structured battery-cell/system identity overrides incidental construction-material terms in filings or thematic context."
        )

    profile = _company_profile(symbol, curr_date, look_back_days)
    if profile is None:
        return (
            f"# Building-materials verification context for {symbol} as of {curr_date}\n\n"
            "- Status: not_applicable\n"
            "- Trigger: no curated ticker, company-name, industry, or filing-text match for building-materials analysis.\n"
            "- Instruction: do not inject cement, waterproofing, glass, gypsum-board, pipe, coating, ceramic-tile, or property-completion logic unless other primary evidence proves relevance."
        )

    income = _safe_fetch("income statement", _fetch_income_statement_data, symbol, "quarterly", curr_date)
    balance = _safe_fetch("balance sheet", _fetch_balance_sheet_data, symbol, "quarterly", curr_date)
    cashflow = _safe_fetch("cashflow", _fetch_cashflow_data, symbol, "quarterly", curr_date)
    indicators = _safe_fetch("financial indicators", _fetch_fina_indicator, symbol, curr_date)

    lines = [
        f"# Building-materials verification context for {symbol} as of {curr_date}",
        "",
        "- Status: triggered",
        f"- Company: {profile.company_name}",
        f"- Tushare industry: {profile.industry or 'N/A'}",
        f"- Trigger: {profile.trigger_reason}",
        f"- Detected subsectors: {', '.join(profile.subsectors)}",
        "",
        "## Buy-Side Industry Driver Map",
        _markdown_table(_driver_table(profile.subsectors)),
        "",
        "## Financial Cycle Checkpoints",
        "- Start with company filings and management wording as first-order evidence: segment revenue, volume/price/cost, gross margin, working capital, cash flow, capex, impairment, and capital-return language.",
        "- Use industry stage as the second layer that explains those filings: demand contraction / inventory digestion / price stabilization / profit repair / replacement-cycle recovery.",
        "- For cement, the base-cycle question is whether company filings confirm volume-price pressure, cost relief, inventory digestion, or disciplined supply and price repair. Buybacks and dividends matter as shareholder-return and safety-margin verification after the operating evidence is read.",
        "- Revenue growth without cash collection is weak evidence for building-material names exposed to property and engineering channels.",
        "- Low PB is a hypothesis, not a buy signal. It becomes investable only when asset value is credible, utilization/price/cash signals stop deteriorating, and capital allocation is aligned with shareholders.",
        "- High dividend yield is a starting point, not defense. Test payout against profit trough, operating cash flow, maintenance capex, working-capital drag, and buyback/dividend priority.",
        "- Cement/glass/fiberglass require product-price, inventory, cost, and utilization evidence; waterproof/coating/pipe/hardware require channel, receivable, impairment, and cash-collection evidence.",
        "",
        "## Growth, Margin, ROE, Leverage Snapshot",
        _markdown_table(_growth_margin_table(income, indicators)) or "No data returned.",
        "",
        "## Working-Capital And Demand-Visibility Snapshot",
        _markdown_table(_working_capital_table(balance)) or "No data returned.",
        "",
        "## Cash-Quality Snapshot",
        _markdown_table(_cash_quality_table(cashflow, income)) or "No data returned.",
        "",
        "## Filing Segment / Product Evidence Snippets",
    ]
    snippets = _segment_snippets(profile)
    lines.extend(snippets or ["No building-material segment snippets returned."])
    lines.extend(
        [
            "",
            "## Required Manager Treatment",
            "- Include a concise Building Materials Operating Cycle Verdict when it changes the rating, valuation, or action plan; otherwise integrate the key points into the main business/valuation discussion instead of adding a decorative section.",
            "- Anchor first on company filings and management wording, then classify the industry stage and likely evolution path: demand still contracting, supply discipline repairing price, inventory digestion, margin trough, or confirmed recovery. Capital allocation, dividends, and buybacks should then be used as shareholder-return, safety-margin, and controlling-shareholder-attitude evidence.",
            "- Explain where the company sits in the building-material cycle: cement/glass price beta, property-completion chain, renovation retail chain, infrastructure chain, or export/new-material optionality.",
            "- If product price, regional shipment rate, kiln/grinding utilization, glass/fiberglass inventory, asphalt/resin/titanium-dioxide cost, or channel inventory is missing, label it as a neutral research gap with an exact retrieval task; do not mechanically alter the rating.",
            "- For low-PB/high-dividend names, explicitly explain why cheap book value or dividend yield is or is not enough: asset impairment risk, earnings trough depth, cash conversion, payout safety, and capital-allocation proof.",
            "- Do not let any single lens dominate. Financial-report evidence is the anchor; industry cycle explains the anchor; repurchase/dividend analysis tests shareholder alignment, safety margin, and capital-allocation quality.",
            "- Do not use a metals/mining playbook for cement or other building-material companies. Use sector-native variables before generic PE/PB/technical analysis.",
        ]
    )
    return "\n".join(lines)
