"""Derived forward forecast-model scaffold context."""

from __future__ import annotations

from datetime import datetime
import re
from typing import Any, Mapping

from .industry_identity import (
    is_automotive_components_text,
    consumer_staples_subsector_hints,
    has_lithium_battery_symbol_hint,
    is_hog_breeding_text,
    is_insurance_text,
    is_lithium_battery_text,
    is_telecom_operator_text,
)
from .research_evidence import extract_evidence_records, infer_model_variable
from .underwriting_packet import compact_underwriting_packet


def _compact_lines(text: str, patterns: tuple[str, ...], *, limit: int = 8) -> list[str]:
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    rows: list[str] = []
    for raw in (text or "").splitlines():
        line = re.sub(r"\s+", " ", raw.strip())
        if not line or line.startswith("#") or line.startswith("| ---"):
            continue
        if any(pattern.search(line) for pattern in compiled):
            if len(line) > 280:
                line = line[:277] + "..."
            rows.append(line.replace("|", "/"))
        if len(rows) >= limit:
            break
    return rows


def _is_battery_context(symbol: str, text: str) -> bool:
    return is_lithium_battery_text(symbol, text)


def _battery_forecast_drivers() -> list[tuple[str, str, str]]:
    return [
        ("Power battery revenue", "GWh shipments x ASP", "installation demand, share, customer mix, price clauses"),
        ("Energy-storage revenue", "GWh shipments x ASP", "storage tenders, overseas demand, project delivery"),
        ("Materials / recycling / other", "volume x realized spread or service revenue", "vertical integration and utilization"),
        ("Gross profit", "segment revenue x segment gross margin", "lithium/material cost, yield, depreciation, warranty"),
        ("Operating profit", "gross profit - R&D - SG&A", "R&D capitalization/expense, scale leverage"),
        ("net profit/EPS / FCF", "operating profit - tax/minority + working-capital/capex bridge", "cash conversion and capex cycle"),
    ]


_MODEL_VARIABLE_LABELS = {
    "segment_volume": "segment volume / utilization / backlog",
    "market_share": "market share / segment volume",
    "asp_or_price": "realized ASP / price pass-through",
    "unit_cost": "unit cost / gross margin",
    "utilization_or_backlog": "segment volume / utilization / backlog",
    "segment_margin": "segment gross margin",
    "revenue": "segment revenue",
    "operating_expense": "operating expense ratio",
    "profit_or_eps": "net profit / EPS",
    "cash_conversion": "OCF / FCF conversion",
    "capex_or_roic": "capex / ROIC / scenario probability",
    "balance_sheet": "working capital / balance-sheet risk",
    "valuation": "valuation multiple / risk premium",
    "scenario_probability": "scenario probability",
    "unmapped": "working hypothesis / verification calendar",
}


def _knowledge_planet_assumption_rows(text: str, *, limit: int = 8) -> list[tuple[str, str, str, str, str]]:
    """Translate KPE ledger rows into model variables for downstream LLM judgment.

    This deliberately stops short of changing a forecast.  It makes the model
    state the affected variable, allowed use, and public verification gate.
    """
    rows: list[tuple[str, str, str, str, str]] = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not re.match(r"^\|\s*KPE\d+\s*\|", line, re.I):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 8:
            continue
        evidence_id = cells[0]
        evidence = cells[6]
        verification = cells[7]
        raw_variable = cells[8] if len(cells) >= 9 and cells[8] else infer_model_variable(evidence)
        variable = _MODEL_VARIABLE_LABELS.get(raw_variable, raw_variable)
        outcome = (
            cells[9]
            if len(cells) >= 10 and cells[9]
            else "numeric delta / probability before-after / rejection reason"
        )
        rows.append(
            (
                evidence_id,
                variable,
                "private/proxy prior; quantify delta or reject, never use as a hard fact",
                verification or "public filing, announcement, market or operating KPI cross-check",
                outcome,
            )
        )
        if len(rows) >= limit:
            break
    return rows


def _forecast_years(curr_date: str) -> tuple[str, str, str]:
    try:
        year = datetime.fromisoformat(str(curr_date)[:10]).year
    except ValueError:
        year = datetime.now().year
    return tuple(f"{year + offset}E" for offset in range(3))  # type: ignore[return-value]


def _expectation_excerpt(text: str, patterns: tuple[str, ...]) -> str:
    rows = _compact_lines(text, patterns, limit=2)
    return " / ".join(rows) if rows else "missing; do not invent"


def _sell_side_expectation_excerpt(text: str) -> str:
    categories = ("earnings_forecast", "valuation_method", "rating_target_change")
    for raw in (text or "").splitlines():
        line = re.sub(r"\s+", " ", raw.strip())
        if not line.startswith("|") or not any(f"| {category} |" in line for category in categories):
            continue
        return line.replace("|", "/")[:520]
    return "missing; no company-specific external forecast supplied"


def _structured_kpe_quantification_section(
    bundle: Mapping[str, Any] | None,
) -> list[str]:
    impacts = list((bundle or {}).get("kpe_impacts", []))
    if not impacts:
        return []
    lines = [
        "",
        "## Structured KPE Physical And Financial Quantification",
        "| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for impact in impacts[:12]:
        probability = (
            f"bull {impact.get('bull_probability_before_pct')}->{impact.get('bull_probability_after_pct')}; "
            f"base {impact.get('base_probability_before_pct')}->{impact.get('base_probability_after_pct')}; "
            f"bear {impact.get('bear_probability_before_pct')}->{impact.get('bear_probability_after_pct')}"
        )
        missing = ", ".join(str(item) for item in impact.get("missing_inputs", [])) or "none"
        lines.append(
            f"| {impact.get('evidence_id', '')} | {impact.get('segment', '')} | "
            f"{impact.get('variable', '')} | {impact.get('assumption_delta')} {impact.get('unit', '')} | "
            f"{impact.get('revenue_delta_cny_mn')} | {impact.get('parent_profit_delta_cny_mn')} | "
            f"{impact.get('eps_delta_cny')} | {impact.get('fcf_delta_cny_mn')} | {probability} | "
            f"{impact.get('quantification_status', '')} | "
            f"{str(impact.get('decision_outcome', '')).replace('|', '/')} | {missing.replace('|', '/')} |"
        )
    lines.append(
        "- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied."
    )
    return lines


def _structured_sell_side_expectation_section(
    bundle: Mapping[str, Any] | None,
) -> list[str]:
    observations = list((bundle or {}).get("sell_side_intelligence", []))
    if not observations:
        return []
    lines = [
        "",
        "## Sell-Side Forecast, Valuation And Revision Observations",
        "| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in observations[:12]:
        values = [
            row.get("intelligence_id", ""),
            f"{row.get('institution', '')}/{row.get('published_at', '')}",
            row.get("freshness", ""),
            row.get("rating_signal", ""),
            row.get("forecast_facts", ""),
            row.get("valuation_facts", ""),
            row.get("normalized_points", ""),
            row.get("revision_signal", ""),
            "single observation; compare period/variable/magnitude with the independent model",
        ]
        lines.append("| " + " | ".join(str(value).replace("|", "/") for value in values) + " |")
    lines.extend(
        [
            "- Do not average incompatible forecast years, valuation dates or methods.",
            "- A range or median may be called consensus only when a named multi-broker sample and statistical basis are supplied.",
        ]
    )
    return lines


def _shared_underwriting_section(
    bundle: Mapping[str, Any] | None,
) -> list[str]:
    packet = compact_underwriting_packet(
        (bundle or {}).get("underwriting_packet", {})
    )
    if not packet:
        return []
    lines = [
        "",
        "## Shared Company Underwriting Packet",
        f"- Research readiness: {packet.get('research_readiness', 'missing')}",
        f"- Readiness reasons: {'; '.join(str(item) for item in packet.get('readiness_reasons', [])) or 'none supplied'}",
        f"- Forecast years: {', '.join(str(item) for item in packet.get('forecast_years', []))}",
        "- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.",
    ]
    company = packet.get("company_model", {})
    if company:
        lines.extend(
            [
                "",
                "### Company Operating Equations",
                f"- Revenue: {company.get('revenue_equation', 'missing')}",
                f"- Profit: {company.get('profit_equation', 'missing')}",
                f"- Cash flow: {company.get('cash_flow_equation', 'missing')}",
                f"- Reinvestment: {company.get('capital_intensity_and_reinvestment', 'missing')}",
            ]
        )
    questions = list(packet.get("underwriting_questions", []))
    if questions:
        lines.extend(
            [
                "",
                "### Company-Specific Underwriting Questions",
                "| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in questions[:8]:
            lines.append(
                f"| {row.get('question_id', '')} | {str(row.get('question', '')).replace('|', '/')} | "
                f"{str(row.get('current_answer', '')).replace('|', '/')} | "
                f"{', '.join(str(item) for item in row.get('decisive_model_variables', []))} | "
                f"{', '.join(str(item) for item in row.get('affected_financial_lines', []))} | "
                f"{', '.join(str(item) for item in row.get('missing_evidence', []))}; "
                f"{str(row.get('next_verification', '')).replace('|', '/')} |"
            )
    forecast = list(packet.get("forecast_lines", []))
    if forecast:
        years = list(packet.get("forecast_years", [])) + ["Y1", "Y2", "Y3"]
        lines.extend(
            [
                "",
                "### Shared Three-Year Model Lines",
                f"| segment | metric | unit | base | {years[0]} | {years[1]} | {years[2]} | formula | status | sensitivity / missing |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in forecast[:36]:
            lines.append(
                f"| {row.get('segment', '')} | {row.get('metric', '')} | {row.get('unit', '')} | "
                f"{row.get('base_value')} | {row.get('year_1_value')} | {row.get('year_2_value')} | "
                f"{row.get('year_3_value')} | {str(row.get('formula', '')).replace('|', '/')} | "
                f"{row.get('assumption_status', '')} | {str(row.get('key_sensitivity', '')).replace('|', '/')}; "
                f"{', '.join(str(item) for item in row.get('missing_inputs', []))} |"
            )
    return lines


def _is_battery_material_context(symbol: str, text: str) -> bool:
    lower = f"{symbol}\n{text}".lower()
    # Cell/system makers discuss cathodes and LFP extensively; those upstream
    # mentions must not reroute their full-company model to a material spread.
    if str(symbol or "").strip().upper() == "300750.SZ":
        return False
    return any(
        token in text
        for token in ("正极材料", "磷酸铁锂", "三元材料", "前驱体", "锂电材料", "电池材料")
    ) or any(token in lower for token in ("cathode", "precursor", "lfp"))


def _is_wind_power_context(symbol: str, text: str) -> bool:
    lower = f"{symbol}\n{text}".lower()
    wind_hits = sum(
        token in text
        for token in ("风电", "海上风电", "海风", "塔筒", "管桩", "导管架", "海工", "风电装备", "风机")
    ) + sum(token in lower for token in ("wind power", "offshore wind", "monopile", "jacket foundation", "tower"))
    battery_hits = sum(
        token in text
        for token in ("动力电池", "储能电池", "锂离子电池", "正极材料", "磷酸铁锂", "三元材料", "电芯")
    ) + sum(token in lower for token in ("battery", "cathode", "precursor", "lfp"))
    return wind_hits >= 2 and battery_hits == 0


def _is_metals_mining_context(symbol: str, text: str) -> bool:
    lower = f"{symbol}\n{text}".lower()
    if "status: triggered" in lower and "metals-mining" in lower:
        return True
    metals_hits = sum(
        token in text
        for token in (
            "有色金属",
            "铜",
            "铝",
            "锌",
            "铅",
            "锡",
            "黄金",
            "白银",
            "矿山",
            "矿业",
            "采矿",
            "采选",
            "冶炼",
            "矿石",
            "品位",
            "储量",
            "权益产量",
            "现金成本",
            "完全成本",
            "加工费",
            "套期保值",
        )
    ) + sum(
        token in lower
        for token in (
            "601168",
            "601899",
            "600362",
            "000630",
            "000878",
            "600547",
            "nonferrous metals / mining",
            "metals-mining",
            "copper",
            "aluminum",
            "zinc",
            "lead",
            "gold",
            "silver",
            "mining",
            "smelting",
            "aisc",
            "tc/rc",
            "nav/sotp",
        )
    )
    battery_hits = sum(
        token in text
        for token in ("动力电池", "储能电池", "锂离子电池", "正极材料", "磷酸铁锂", "三元材料", "电芯")
    ) + sum(token in lower for token in ("battery", "cathode", "precursor", "lfp"))
    return metals_hits >= 2 and battery_hits == 0


def _insurance_context_triggered(text: str) -> bool:
    lower = (text or "").lower()
    return "status: triggered" in lower and "insurance verification context" in lower


def _metals_covered(text: str) -> str:
    match = re.search(r"metals covered:\s*([^\n]+)", text or "", re.I)
    return match.group(1).strip().lower() if match else ""


def _metals_forecast_drivers(symbol: str, text: str) -> list[tuple[str, str, str]]:
    lower = f"{symbol}\n{text}".lower()
    covered = _metals_covered(text)
    if "aluminum" in covered or "601600" in lower or "000807" in lower or "铝" in text:
        return [
            ("Primary aluminum revenue", "primary aluminum output x realized aluminum price", "SHFE/LME price, premium/discount, capacity utilization, sales mix"),
            ("Alumina / upstream spread", "alumina output or self-supply x alumina spread", "alumina price, bauxite cost, self-sufficiency, import cost, inventory lag"),
            ("Smelting margin", "aluminum ASP - alumina - power - anode/carbon - other cash cost", "power tariff/self-generation, coal/energy cost, anode price, carbon policy"),
            ("Segment SOTP value", "alumina value + primary aluminum earnings value + trading/energy value + overseas/project optionality", "segment margin, capex, project timetable, jurisdiction and execution haircut"),
            ("net profit/EPS / FCF", "operating profit - tax/minority/finance cost + working-capital/capex bridge", "minority interest, debt cost, OCF/NI, inventory, receivables, dividend coverage"),
        ]
    if "copper" in covered or any(code in lower for code in ("601899", "600362", "000630", "000878", "601168")):
        return [
            ("Mining revenue", "equity copper/by-product output x realized selling price", "reserve grade, recovery, mine life, ramp schedule, realized price versus SHFE/LME/COMEX proxy"),
            ("Smelting / refining spread", "processed volume x TC/RC or processing margin", "concentrate supply, treatment/refining charges, utilization, power and energy cost"),
            ("Trading / pass-through revenue", "traded volume x thin gross spread", "inventory exposure, customer credit, working-capital intensity; do not value like scarce resources"),
            ("Gross profit", "mining gross profit + smelting spread + by-product credits - unit cash/AISC cost", "cash cost, AISC/unit cost, sustaining capex, FX, energy/labor, product mix"),
            ("NAV / SOTP value", "mine-by-mine NAV + smelting/trading earnings value + project optionality", "capex, construction-in-progress, commissioning, permitting, jurisdiction risk, discount/haircut"),
            ("net profit/EPS / FCF", "operating profit - tax/minority/finance cost + working-capital/capex bridge", "minority interest, debt maturity, OCF/NI, hedging/derivatives, inventory marks"),
        ]
    if "gold" in covered or "黄金" in text:
        return [
            ("Gold / silver revenue", "equity precious-metal output x realized selling price", "SHFE/COMEX/LBMA proxy, real-rate/USD sensitivity, grade, recovery, sales mix"),
            ("Mine margin", "realized price - cash cost/AISC per gram or ounce", "AISC, sustaining capex, labor/energy, FX, tax/royalty"),
            ("Project / acquisition value", "mine-by-mine NAV + ramp/acquisition optionality", "reserve life, capex, commissioning, jurisdiction and integration risk"),
            ("FCF / dividend capacity", "mine operating cash flow - sustaining/growth capex - tax/minority/finance cost", "OCF/NI, debt maturity, hedging, inventory, dividend policy"),
            ("P/NAV / PE value", "NAV per share or normalized EPS x multiple", "gold-price deck, cost curve, reserve replacement, peer P/NAV"),
        ]
    if "lithium" in covered or "锂" in text:
        return [
            ("Lithium revenue", "lithium carbonate/hydroxide shipment x realized ASP", "futures/spot price, customer mix, pass-through, export/import"),
            ("Resource / processing spread", "realized ASP - spodumene/brine/salt-lake cost - conversion cost", "ore cost, brine yield, utilization, inventory lag"),
            ("Project ramp value", "equity resource output x ramp probability x margin", "grade, recovery, capex, commissioning, permits, impairment risk"),
            ("Inventory / impairment bridge", "inventory quantity x price change + impairment reversals/charges", "cycle stage, cost layers, downstream restocking"),
            ("net profit/EPS / FCF", "operating profit - tax/minority/finance cost + working-capital/capex bridge", "OCF/NI, leverage, capex, equity-accounted earnings"),
        ]
    return [
        ("Mining revenue", "equity output by metal x realized selling price", "reserve grade, recovery rate, mine life, ramp schedule, realized price versus SHFE/LME/COMEX proxy"),
        ("Smelting / refining spread", "processed volume x TC/RC or processing margin", "concentrate supply, treatment/refining charges, utilization, power and energy cost"),
        ("Trading / pass-through revenue", "traded volume x thin gross spread", "inventory exposure, customer credit, working-capital intensity; do not value like scarce resources"),
        ("Gross profit", "mining gross profit + smelting spread + by-product credits - unit cash/AISC cost", "cash cost, AISC/unit cost, sustaining capex, FX, energy/labor, product mix"),
        ("NAV / SOTP value", "mine-by-mine NAV + smelting/trading earnings value + project optionality", "capex, construction-in-progress, commissioning, permitting, jurisdiction risk, discount/haircut"),
        ("net profit/EPS / FCF", "operating profit - tax/minority/finance cost + working-capital/capex bridge", "minority interest, debt maturity, OCF/NI, hedging/derivatives, inventory marks"),
    ]


def _hog_breeding_forecast_drivers() -> list[tuple[str, str, str]]:
    return [
        ("Hog sales kilograms", "commodity-hog output x average sale weight", "monthly company output, slaughter weight, piglet/breeding-hog mix, capacity utilization"),
        ("Realized hog revenue", "sales kg x company commodity-hog ASP + piglet/breeding-hog revenue treated separately", "company ASP versus national spot and DCE live-hog curve; product mix and seasonality"),
        ("Unit spread", "realized hog ASP - complete hog-breeding cost", "feed cost, PSY/FCR, mortality/disease control, finance cost, scale efficiency"),
        ("Core breeding profit", "sales kg x unit spread", "hog-price sensitivity, cost sensitivity, output elasticity, inventory/biological-asset marks"),
        ("Cash profit / FCF", "core breeding profit + depreciation - working capital - capex - interest - tax/minority", "OCF/NI, inventory build, capex cuts or restarts, debt maturity"),
        ("Valuation bridge", "scenario profit x normalized cyclical PE with PB-floor cross-check", "implied hog price from current market cap, cycle stage, balance-sheet survival and dilution risk"),
    ]


def _insurance_forecast_drivers() -> list[tuple[str, str, str]]:
    return [
        ("Life NBV", "new business value = new premium x NBV margin by channel", "agent productivity, agent count, bancassurance mix, product margin, persistency/surrender"),
        ("Embedded value / CSM", "opening EV + expected return + operating variance + NBV contribution +/- market variance", "EV growth, CSM/NCSM movement, insurance-service result, assumption changes"),
        ("P&C underwriting profit", "earned premium x (1 - COR)", "premium growth, loss ratio, expense ratio, catastrophe losses, auto-pricing discipline"),
        ("Investment income", "investment assets x net/total/comprehensive yield - liability cost pressure", "bond yield, equity-market beta, impairment, duration mismatch, accounting classification"),
        ("OPAT / net profit / EPS", "insurance service result + investment spread + bank/subsidiary contribution - tax/minority/non-recurring", "core operating profit, Ping An Bank contribution, one-offs, share count"),
        ("Dividend / SOTP value", "capital generation and solvency-supported payout + insurance core P/EV + bank/asset-management/tech value", "solvency ratio, payout policy, holding-company discount, double-counting checks"),
    ]


def _automotive_components_forecast_drivers() -> list[tuple[str, str, str]]:
    return [
        ("Core product revenue", "sum(customer vehicle volume x platform share x content per vehicle), cross-checked with segment units x ASP", "customer/model exposure, SOP cadence, annual price reductions and product mix"),
        ("Segment gross profit", "sum(segment revenue x segment gross margin)", "ASP, material pass-through, utilization, launch/ramp cost and mix"),
        ("Operating profit", "segment gross profit - R&D - selling/admin - impairment", "R&D conversion, scale leverage, depreciation and credit risk"),
        ("Parent net profit / EPS", "operating profit +/- finance and FX - tax - minority; divided by diluted shares", "interest versus FX decomposition, subsidies/one-offs and share count"),
        ("OCF / capex / FCF / incremental ROIC", "net profit + D&A - working capital - capex; incremental EBIT after tax / incremental invested capital", "receivables, inventory, new-plant ramp, capex discipline and cash conversion"),
        ("Second-curve scenario value", "qualified delivered units x ASP x margin, valued separately until unit economics and cash conversion are verified", "customer nomination, order-to-revenue schedule, capex, utilization and probability"),
    ]


def _consumer_staples_forecast_drivers(symbol: str, text: str) -> list[tuple[str, str, str]] | None:
    subsectors = consumer_staples_subsector_hints(symbol, text)
    if not subsectors:
        return None
    if "functional_beverage" in subsectors:
        return [
            ("Core energy-drink revenue", "Dongpeng Special Drink volume x realized ASP x channel mix", "category growth, weather, terminal coverage, regional penetration, terminal price and same-store productivity"),
            ("Second-curve revenue", "new-product volume x ASP x repeat-purchase/channel penetration", "electrolyte water, juice tea, coffee/tea shelf penetration, repeat purchase, cannibalization versus incrementality"),
            ("Gross profit", "revenue x gross margin by product/channel", "sugar, PET/can/packaging, logistics, product mix, price discipline and promotion intensity"),
            ("Operating profit", "gross profit - selling expense - admin/R&D", "advertising, rebate/lottery policy, salesforce expansion, scale leverage"),
            ("Cash profit / FCF", "net profit + D&A - working capital - capex", "contract liabilities/prepayments, distributor inventory, receivables, inventory and buyback/dividend execution"),
            ("Valuation bridge", "normalized EPS/FCF x consumer-growth multiple with ROE/payout cross-check", "H1/H2 revenue growth, margin stability, second-curve proof, channel health and downside entry band"),
        ]
    return [
        ("Core revenue", "category volume x ASP x product/channel mix", "category growth, traffic/weather/catering recovery, regional penetration and product mix"),
        ("Gross profit", "revenue x gross margin", "raw-material and packaging costs, price/mix, promotion intensity and logistics"),
        ("Operating profit", "gross profit - selling/admin/R&D expense", "sales expense, channel rebates, scale leverage and brand investment"),
        ("Cash profit / FCF", "net profit + D&A - working capital - capex", "contract liabilities/prepayments, inventory, receivables, OCF/NI and capex"),
        ("Valuation bridge", "normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check", "growth durability, channel health, margin stability and shareholder return"),
    ]


def build_forecast_model_context(
    symbol: str,
    curr_date: str,
    *,
    earnings_model_context: str = "",
    company_business_model_context: str = "",
    filing_intelligence_context: str = "",
    peer_comparison_context: str = "",
    industry_kpi_context: str = "",
    metals_mining_context: str = "",
    insurance_context: str = "",
    knowledge_planet_context: str = "",
    market_expectation_context: str = "",
    structured_research_context: Mapping[str, Any] | None = None,
) -> str:
    gated_insurance_context = (
        insurance_context if _insurance_context_triggered(insurance_context) else ""
    )
    combined = "\n".join(
        [
            earnings_model_context,
            company_business_model_context,
            filing_intelligence_context,
            peer_comparison_context,
            gated_insurance_context,
            industry_kpi_context,
            metals_mining_context,
            knowledge_planet_context,
            market_expectation_context,
        ]
    )
    is_hog_breeder = is_hog_breeding_text(symbol, combined)
    is_battery_company = _is_battery_context(symbol, combined)
    evidence = _compact_lines(
        combined,
        (
            r"revenue|gross margin|net profit|EPS|OCF|FCF|capex|ROE",
            r"segment|business model|profit pool|valuation",
            r"NBV|embedded value|P/EV|solvency|COR|loss ratio|expense ratio|investment yield|bancassurance|agent productivity|CSM|NCSM|OPAT",
            r"hog|pig|piglet|sow|live hog|slaughter|complete cost|breeding sow|pork|DCE|LH\d+|ASP",
            r"\u751f\u732a|\u5546\u54c1\u732a|\u4ed4\u732a|\u80fd\u7e41\u6bcd\u732a|\u6bcd\u732a\u5b58\u680f|\u732a\u4ef7|\u732a\u5468\u671f|\u51fa\u680f|\u5b8c\u5168\u6210\u672c|\u732a\u8089",
            r"收入|毛利|净利润|归母|现金流|资本开支|分部|业务",
        ),
        limit=10,
    )
    if has_lithium_battery_symbol_hint(symbol):
        drivers = _battery_forecast_drivers()
    elif is_automotive_components_text(symbol, combined):
        drivers = _automotive_components_forecast_drivers()
    elif is_telecom_operator_text(symbol, combined):
        drivers = [
            ("Mobile service revenue", "mobile subscribers x mobile ARPU", "5G penetration, package mix, churn, DOU, pricing discipline"),
            ("Broadband / home revenue", "broadband subscribers x household ARPU", "gigabit penetration, smart-home attach, bundling"),
            ("Enterprise / cloud / AI revenue", "customer count x cloud/IDC/AI ARPU or project revenue", "cloud growth, AI paid adoption, IDC utilization, contract liabilities"),
            ("EBITDA / operating profit", "service revenue x margin - depreciation - SG&A/R&D", "network scale, cloud gross margin, depreciation, personnel and maintenance cost"),
            ("net profit/EPS / dividend capacity", "operating profit - tax/minority + FCF after capex", "capex-to-revenue, OCF/NI, payout ratio, net cash/debt"),
        ]
    elif is_insurance_text(symbol, combined):
        drivers = _insurance_forecast_drivers()
    elif is_hog_breeder:
        drivers = _hog_breeding_forecast_drivers()
    elif (consumer_drivers := _consumer_staples_forecast_drivers(symbol, combined)) is not None:
        drivers = consumer_drivers
    elif _is_metals_mining_context(symbol, combined):
        drivers = _metals_forecast_drivers(symbol, combined)
    elif _is_wind_power_context(symbol, combined):
        drivers = [
            ("Wind-equipment revenue", "opening backlog + new orders - delivered orders", "offshore wind tenders, overseas customer awards, delivery schedule"),
            ("Project ASP / mix", "delivered tonnage or MW-equivalent x project ASP", "monopile/jacket/tower mix, export share, FX clauses"),
            ("Gross profit", "project revenue x project gross margin", "steel plate cost, fabrication yield, port/logistics cost, utilization, FX"),
            ("Operating profit", "gross profit - R&D - SG&A - finance cost - impairment", "scale leverage, capex depreciation, receivables, credit risk"),
            ("net profit/EPS / FCF", "operating profit - tax/minority + working-capital/capex bridge", "contract liabilities, prepayments, inventory, OCF/NI, capex cycle"),
        ]
    elif _is_battery_material_context(symbol, combined):
        drivers = [
            ("Cathode / material revenue", "shipment volume x cathode ASP", "LFP/ternary demand, customer order cadence, pass-through clauses"),
            ("Manufacturing spread", "cathode ASP - lithium carbonate / precursor / energy / processing cost", "raw-material price, inventory-cost lag, processing fee"),
            ("Gross profit", "shipment volume x unit spread", "capacity utilization, yield, depreciation, product mix"),
            ("Operating profit", "gross profit - R&D - SG&A - credit impairment", "customer concentration, receivables, scale leverage"),
            ("net profit/EPS / FCF", "operating profit - tax/minority + working-capital/capex bridge", "OCF/NI, inventory, capex, expansion cycle"),
        ]
    elif is_battery_company:
        drivers = _battery_forecast_drivers()
    else:
        drivers = [
            ("Core revenue", "volume x ASP x mix", "demand, price, market share"),
            ("Gross profit", "revenue x gross margin", "cost curve, utilization, product mix"),
            ("Operating profit", "gross profit - R&D - SG&A", "expense discipline and scale leverage"),
            ("net profit/EPS", "operating profit - tax/minority/financial items", "non-recurring and minority interest"),
            ("Free cash flow", "net profit + D&A - working capital - capex", "cash conversion and reinvestment"),
        ]

    hog_sensitivity_section = []
    if is_hog_breeder:
        hog_sensitivity_section = [
            "",
            "## Hog-Breeding Sensitivity Requirement",
            "| item | Formula / requirement |",
            "| --- | --- |",
            "| Sales kg | commodity-hog output x average sale weight |",
            "| Unit spread | realized commodity-hog ASP - complete hog-breeding cost |",
            "| Breeding profit | sales kg x unit spread |",
            "| Sensitivity | show at least bear/base/bull hog ASP cases and each 1 CNY/kg move where data permits |",
            "| Implied cycle | reverse-engineer the hog ASP implied by current market cap under normalized PE/PB bands |",
            "| Valuation floor | stress-case book value / NAV after losses and impairment, cross-checked with trough PB |",
            "- No Buy/Overweight or Underweight/Sell conclusion is complete without linking rating triggers to hog ASP, complete cost, breeding-sow inventory, OCF, leverage, and current-market-cap implied hog price.",
            "- The scenario table must be monotonic in economic logic: a positive-spread recovery case cannot have a selected fair-value range below a worse loss-making stress case unless the report explicitly explains why PB support disappears.",
            "- Use PE only on normalized cycle earnings. Do not use TTM PE or a one-year trough/peak EPS as the primary hog-breeder valuation anchor.",
        ]

    battery_model_section = []
    if is_battery_company:
        battery_model_section = [
            "",
            "## Battery Forecast And Valuation Controls",
            "| control | Mandatory treatment |",
            "| --- | --- |",
            "| Segment model | model power battery, energy storage, materials/recycling, and other businesses separately |",
            "| Revenue bridge | GWh shipments x realized ASP by segment; reconcile mix and consolidation eliminations |",
            "| Margin bridge | ASP/pass-through - lithium/material cost - manufacturing/depreciation/warranty; show utilization sensitivity |",
            "| Earnings bridge | segment gross profit - R&D/SG&A/finance - tax/minority/non-recurring = parent net profit/EPS |",
            "| Cash bridge | net profit + D&A - working capital - capex = FCF; reconcile OCF/NI and capacity expansion |",
            "| Scenario discipline | show bear/base/bull shipment, ASP, utilization, gross margin, EPS, FCF, and valuation multiple |",
            "| Valuation monotonicity | a deterioration case must not receive a higher multiple than base without an explicit, evidence-backed reason |",
            "| Probability audit | record scenario probabilities before and after each private/proxy clue; unexplained probability changes are invalid |",
            "- Missing shipment, ASP, utilization, or segment-margin evidence must remain a neutral explicit model gap; narrative strength cannot fill a numeric cell, and the gap must not mechanically alter the rating.",
        ]

    kp_assumption_rows = _knowledge_planet_assumption_rows(knowledge_planet_context)
    kp_assumption_section = []
    if kp_assumption_rows:
        kp_assumption_section = [
            "",
            "## Alternative-Intelligence Assumption Bridge",
            "| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |",
            "| --- | --- | --- | --- | --- |",
            *[
                f"| {evidence_id} | {variable} | {use} | {verification} | {outcome} |"
                for evidence_id, variable, use, verification, outcome in kp_assumption_rows
            ],
            "- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.",
        ]

    evidence_records = [
        record
        for record in extract_evidence_records(
            {
                "earnings_model": earnings_model_context,
                "financial_report_intelligence": filing_intelligence_context,
                "industry_kpi": industry_kpi_context,
                "market_expectation": market_expectation_context,
                "knowledge_planet": knowledge_planet_context,
            },
            max_records=100,
        )
        if record.model_variable != "unmapped"
    ]
    evidence_records.sort(
        key=lambda row: {
            "reported": 0,
            "calculated": 1,
            "private_proxy": 2,
            "estimated": 3,
            "missing": 4,
        }.get(row.status, 5)
    )
    evidence_records = evidence_records[:16]
    evidence_ledger_section = [
        "",
        "## Model-Ready Evidence Ledger",
        "| evidence_id | source | tier | status | model variable | source period | evidence |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    if evidence_records:
        evidence_ledger_section.extend(
            f"| {row.evidence_id} | {row.source_module} | {row.source_tier} | {row.status} | "
            f"{row.model_variable} | {row.period} | {row.text} |"
            for row in evidence_records
        )
    else:
        evidence_ledger_section.append(
            "| - | - | - | missing | - | - | No model-ready numeric evidence extracted; keep forecasts explicitly assumption-led. |"
        )

    year_1, year_2, year_3 = _forecast_years(curr_date)
    structured_segments = list((structured_research_context or {}).get("segments", []))
    structured_segment_rows = [
        (
            f"| {segment.get('segment', 'unmapped')} | segment revenue = volume/units x ASP/mix | "
            "to be estimated | to be estimated | to be estimated | "
            f"base period={segment.get('period', 'unspecified')}; reported revenue={segment.get('revenue_reported_value')} "
            f"({segment.get('revenue_reported_unit', 'unit missing')}); revenue weight={segment.get('revenue_weight_pct')}%; "
            f"growth={segment.get('revenue_growth_pct')}%; gross margin={segment.get('gross_margin_pct')}%; "
            f"margin change={segment.get('gross_margin_change_pp')}pp; source={segment.get('source_module', '')}; "
            f"mode={segment.get('extraction_mode', '')} |"
        )
        for segment in structured_segments[:10]
        if segment.get("segment")
    ]
    segment_matrix_section = [
        "",
        "## Segment / Business-Bucket Three-Year Operating Matrix",
        f"| business bucket / driver | formula | {year_1} | {year_2} | {year_3} | evidence ids / assumption status |",
        "| --- | --- | --- | --- | --- | --- |",
        *(
            structured_segment_rows
            if structured_segment_rows
            else [
                f"| {name} | {formula} | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |"
                for name, formula, _ in drivers
            ]
        ),
        "- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.",
    ]

    expectation_section = [
        "",
        "## Consensus And Market-Implied Expectation Gap",
        "| comparison layer | supplied evidence | required model treatment |",
        "| --- | --- | --- |",
        f"| Current market-implied expectation | {_expectation_excerpt(market_expectation_context, (r'implied|PE TTM|market cap|隐含|市值',))} | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |",
        f"| External sell-side / consensus proxy | {_sell_side_expectation_excerpt(knowledge_planet_context)} | label broker/date/count; use range or median only when the source is company-specific |",
        "| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |",
        "- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.",
        "- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.",
    ]

    assumption_change_section = [
        "",
        "## Assumption Change And Valuation Transmission Ledger",
        "| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
        "| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |",
        "- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.",
        "- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.",
    ]
    structured_kpe_section = _structured_kpe_quantification_section(
        structured_research_context
    )
    sell_side_expectation_section = _structured_sell_side_expectation_section(
        structured_research_context
    )
    shared_underwriting_section = _shared_underwriting_section(
        structured_research_context
    )
    underwriting_packet = (structured_research_context or {}).get(
        "underwriting_packet", {}
    )
    model_profile = str(
        underwriting_packet.get("company_model", {}).get(
            "model_profile", "corporate"
        )
    )
    mandatory_rows_by_profile = {
        "bank": [
            ("Earning assets / NIM", "asset mix, loan/deposit pricing and funding cost"),
            ("Net interest / fee income", "volume x spread plus fee/AUM drivers"),
            ("Pre-provision profit / credit cost", "cost efficiency, NPL migration and provisions"),
            ("Parent profit / EPS / ROE", "tax, shares, capital consumption and payout"),
            ("NPL / provision coverage / CET1", "asset quality and regulatory capital"),
        ],
        "insurance": [
            ("Premium / APE / NBV", "channel volume, margin, persistency and product mix"),
            ("EV / CSM / investment spread", "liability growth and investment return versus cost"),
            ("P&C COR where applicable", "loss ratio and expense ratio"),
            ("OPAT / parent profit / EPS", "operating and market-sensitive profit bridge"),
            ("Solvency / payout", "capital consumption and distributable capacity"),
        ],
        "securities": [
            ("Brokerage / investment banking", "turnover, fee rate and issuance pipeline"),
            ("Asset management", "AUM, fee rate and product mix"),
            ("Trading / investment income", "market exposure, leverage and risk budget"),
            ("Parent profit / EPS / ROE", "business mix, tax and share count"),
            ("Net capital / capital adequacy", "regulatory and balance-sheet constraint"),
        ],
        "reit": [
            ("Occupancy / rent per unit", "lease renewal, supply and tenant quality"),
            ("NOI", "rental revenue less property operating cost"),
            ("Distributable cash flow", "NOI, interest, maintenance capex and working cash"),
            ("Payout / per-unit distribution", "distribution policy and unit count"),
            ("NAV / cap rate", "asset valuation and financing sensitivity"),
        ],
        "corporate": [
            ("Revenue", "reconcile segment volume, ASP, mix, and eliminations"),
            ("Gross margin", "tie to price/spread, cost, utilization, and mix"),
            ("Operating expense ratio", "tie to R&D, sales, admin, and scale leverage"),
            ("Net profit / EPS", "tie to tax, minority, non-recurring, and share count"),
            ("Operating cash flow / capex / FCF", "tie to working capital and reinvestment"),
        ],
    }
    mandatory_rows = mandatory_rows_by_profile.get(
        model_profile,
        mandatory_rows_by_profile["corporate"],
    )

    return "\n".join(
        [
            f"# Forward Forecast Model Scaffold for {symbol} as of {curr_date}",
            "",
            "- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.",
            "",
            "## Evidence Base Already Present",
            *([f"- {line}" for line in evidence] if evidence else ["- No compact earnings/model evidence was extracted; the forecast must be explicitly evidence-limited."]),
            "",
            "## Driver Bridge",
            "| Forecast line | Formula / bridge | Required assumptions |",
            "| --- | --- | --- |",
            *[f"| {name} | {formula} | {assumption} |" for name, formula, assumption in drivers],
            *hog_sensitivity_section,
            *battery_model_section,
            *kp_assumption_section,
            *evidence_ledger_section,
            *segment_matrix_section,
            *expectation_section,
            *assumption_change_section,
            *shared_underwriting_section,
            *structured_kpe_section,
            *sell_side_expectation_section,
            "",
            "## Mandatory Three-Year Table",
            f"| item | {year_1} | {year_2} | {year_3} | evidence / assumption status |",
            "| --- | --- | --- | --- | --- |",
            *[
                f"| {item} | to be estimated | to be estimated | to be estimated | {requirement} |"
                for item, requirement in mandatory_rows
            ],
            "",
            "## Analyst Instructions",
            "- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.",
            "- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.",
            "- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.",
            "- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.",
            "- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.",
        ]
    )


def get_forecast_model_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, Any] | None = None,
) -> str:
    supplied = dict(contexts or {})
    return build_forecast_model_context(
        ticker,
        curr_date,
        earnings_model_context=supplied.get("earnings_model_context", ""),
        company_business_model_context=supplied.get("company_business_model_context", ""),
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        industry_kpi_context=supplied.get("industry_kpi_context", ""),
        metals_mining_context=supplied.get("metals_mining_context", ""),
        insurance_context=supplied.get("insurance_context", ""),
        knowledge_planet_context=supplied.get("knowledge_planet_context", ""),
        market_expectation_context=supplied.get("market_expectation_context", ""),
        structured_research_context=supplied.get("structured_research_context", {}),
    )
