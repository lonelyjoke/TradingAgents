"""Derived forward forecast-model scaffold context."""

from __future__ import annotations

import re
from typing import Mapping

from .industry_identity import (
    consumer_staples_subsector_hints,
    is_hog_breeding_text,
    is_insurance_text,
    is_telecom_operator_text,
)


def _compact_lines(text: str, patterns: tuple[str, ...], *, limit: int = 8) -> list[str]:
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    rows: list[str] = []
    for raw in (text or "").splitlines():
        line = re.sub(r"\s+", " ", raw.strip())
        if not line or line.startswith("| ---"):
            continue
        if any(pattern.search(line) for pattern in compiled):
            if len(line) > 280:
                line = line[:277] + "..."
            rows.append(line.replace("|", "/"))
        if len(rows) >= limit:
            break
    return rows


def _is_battery_context(symbol: str, text: str) -> bool:
    lower = f"{symbol}\n{text}".lower()
    return (
        "300750" in lower
        or "battery" in lower
        or "动力电池" in text
        or "储能电池" in text
        or "锂离子电池" in text
    )


def _is_battery_material_context(symbol: str, text: str) -> bool:
    lower = f"{symbol}\n{text}".lower()
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
        ]
    )
    is_hog_breeder = is_hog_breeding_text(symbol, combined)
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
    if is_telecom_operator_text(symbol, combined):
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
    elif _is_battery_context(symbol, combined):
        drivers = [
            ("Power battery revenue", "GWh shipments x ASP", "installation demand, share, customer mix, price clauses"),
            ("Energy-storage revenue", "GWh shipments x ASP", "storage tenders, overseas demand, project delivery"),
            ("Materials / recycling / other", "volume x realized spread or service revenue", "vertical integration and utilization"),
            ("Gross profit", "segment revenue x segment gross margin", "lithium/material cost, yield, depreciation, warranty"),
            ("Operating profit", "gross profit - R&D - SG&A", "R&D capitalization/expense, scale leverage"),
            ("net profit/EPS / FCF", "operating profit - tax/minority + working-capital/capex bridge", "cash conversion and capex cycle"),
        ]
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
            "",
            "## Mandatory Three-Year Table",
            "| item | 2026E | 2027E | 2028E | evidence / assumption status |",
            "| --- | --- | --- | --- | --- |",
            "| Revenue | to be estimated | to be estimated | to be estimated | tie to segment volume, ASP, and mix |",
            "| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |",
            "| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |",
            "| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |",
            "| Operating cash flow / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and capex |",
            "",
            "## Analyst Instructions",
            "- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.",
            "- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.",
            "- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.",
            "- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.",
        ]
    )


def get_forecast_model_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
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
    )
