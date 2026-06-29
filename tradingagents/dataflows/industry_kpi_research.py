"""Derived industry-specific KPI checklist context.

This module turns already-fetched report/industry contexts into an evidence
checklist. It does not fetch or invent data; missing rows remain research gaps.
"""

from __future__ import annotations

import re
from typing import Mapping

from .industry_identity import (
    consumer_staples_subsector_hints,
    has_lithium_battery_symbol_hint,
    is_automotive_components_text,
    is_consumer_staples_text,
    is_hog_breeding_text,
    is_insurance_text,
    is_lithium_battery_text,
    is_telecom_operator_text,
)


def _compact_line(line: str, *, max_len: int = 260) -> str:
    line = re.sub(r"\s+", " ", (line or "").strip())
    if len(line) > max_len:
        return line[: max_len - 3] + "..."
    return line


def _matching_lines(text: str, patterns: tuple[str, ...], *, limit: int = 6) -> list[str]:
    rows: list[str] = []
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("| ---"):
            continue
        if any(pattern.search(line) for pattern in compiled):
            rows.append(_compact_line(line).replace("|", "/"))
        if len(rows) >= limit:
            break
    return rows


def _metals_context_triggered(text: str) -> bool:
    return "status: triggered" in (text or "").lower() and "metals-mining" in (text or "").lower()


def _insurance_context_triggered(text: str) -> bool:
    lower = (text or "").lower()
    return "status: triggered" in lower and "insurance verification context" in lower


def _metals_covered(text: str) -> str:
    match = re.search(r"metals covered:\s*([^\n]+)", text or "", re.I)
    return match.group(1).strip().lower() if match else ""


def _metals_playbook(symbol: str, combined_text: str) -> tuple[str, list[tuple[str, str, str]]] | None:
    covered = _metals_covered(combined_text)
    lower = f"{symbol}\n{combined_text}".lower()
    if "aluminum" in covered or "601600" in lower or "000807" in lower or "铝" in combined_text:
        return (
            "nonferrous metals / aluminum chain",
            [
                ("Cycle/Price", "SHFE/LME aluminum price, curve, inventory, LME-SHFE spread, import/export arbitrage", "realized ASP and cycle stage"),
                ("Cost Spread", "alumina price, bauxite cost/self-supply, power tariff/self-generation, anode/carbon cost", "smelting margin and gross margin"),
                ("Supply Discipline", "domestic capacity ceiling, operating rate, curtailments/restarts, policy and energy constraints", "supply elasticity and margin durability"),
                ("Demand Mix", "property/construction, grid, PV, EV lightweighting, packaging, exports, general manufacturing", "volume, mix, and pricing resilience"),
                ("Segment Economics", "alumina, primary aluminum, trading, energy and overseas segment revenue/margin split", "valuation bucket and SOTP treatment"),
                ("Cash/Balance Sheet", "inventory, receivables, contract liabilities, OCF/NI, capex, debt maturity, dividend coverage", "cycle survival and payout capacity"),
            ],
        )
    if "copper" in covered or any(code in lower for code in ("601899", "600362", "000630", "000878", "601168")):
        return (
            "nonferrous metals / copper-mining-smelting",
            [
                ("Cycle/Price", "SHFE/LME/COMEX copper price, curve, warehouse inventory, premiums/discounts, import arbitrage", "realized ASP and cycle stage"),
                ("Mine Assets", "reserve/resource tonnage, grade, recovery rate, mine life, equity copper output and ramp", "resource quality and volume runway"),
                ("Cost Curve", "cash cost, AISC/unit cost, sustaining capex, by-product credits, FX and energy/labor sensitivity", "margin resilience and downside"),
                ("Smelting Spread", "TC/RC, concentrate sourcing, cathode premium, utilization, inventory and derivative exposure", "smelting/refining profit pool"),
                ("Segment/SOTP", "mining, smelting/refining, processing, trading and new-project NAV split", "valuation bucket and multiple/NAV treatment"),
                ("Cash/Risk", "working capital, hedging, impairment, leverage, jurisdiction risk, project capex", "earnings quality and balance-sheet survival"),
            ],
        )
    if "gold" in covered or "黄金" in combined_text:
        return (
            "nonferrous metals / precious metals",
            [
                ("Macro Price", "SHFE/COMEX gold/silver, real rates, USD, central-bank buying, risk premium", "realized ASP and multiple support"),
                ("Mine Assets", "reserve/resource tonnage, grade, recovery, mine life, equity gold/silver output", "asset quality and production runway"),
                ("Cost Curve", "cash cost, AISC per gram/ounce, sustaining capex, labor/energy/FX", "margin resilience and downside"),
                ("Growth Projects", "mine ramp, acquisition integration, capex, permitting, jurisdiction risk", "NAV optionality and execution risk"),
                ("Risk Management", "hedging, inventory, impairment, taxes/royalties, minority interest, debt maturity", "earnings quality and FCF"),
                ("Valuation", "NAV/P-NAV, EV/resource, PE/FCF cross-check, dividend coverage", "probability/payoff and peer allocation"),
            ],
        )
    if "lithium" in covered or "锂" in combined_text:
        return (
            "lithium / metals cycle",
            [
                ("Price", "lithium carbonate/hydroxide price, futures curve, realized ASP", "revenue and inventory gains/losses"),
                ("Spread", "ore/salt-lake/brine cost, processing spread, by-product credits", "cash margin"),
                ("Inventory", "industry and company inventory, downstream restocking/destocking", "cycle stage"),
                ("Output", "equity resource output, conversion capacity, ramp schedule", "volume"),
                ("Demand", "battery installation, ESS, cathode output, export/import", "end demand"),
                ("Cost Curve", "peer cost curve, project grade, AISC/cash cost, impairment risk", "moat and downside"),
            ],
        )
    return None


def _insurance_playbook() -> tuple[str, list[tuple[str, str, str]]]:
    return (
        "insurance / integrated financial services",
        [
            ("Life NBV", "new business value, NBV margin, agent count/productivity, bancassurance contribution", "life franchise growth and P/EV repair"),
            ("Embedded Value", "EV growth, operating experience variance, CSM/NCSM movement, insurance service result", "capital generation and valuation anchor"),
            ("P&C Underwriting", "premium growth, COR, loss ratio, expense ratio, catastrophe/auto-pricing context", "underwriting profit quality"),
            ("Investment Spread", "net, total, and comprehensive investment yield versus liability cost and duration", "earnings volatility and book-value risk"),
            ("Solvency / Capital", "core/comprehensive solvency ratio, capital generation, payout ratio, dividend and buyback constraints", "dividend durability and downside"),
            ("SOTP / Subsidiaries", "insurance core, bank subsidiary, asset management, technology, and holding-company discount", "valuation bucket and double-counting control"),
        ],
    )


def _automotive_components_playbook() -> tuple[str, list[tuple[str, str, str]]]:
    return (
        "automotive components / platform supplier",
        [
            ("Customer / Vehicle Exposure", "top-customer revenue, customer vehicle sales, supplied platforms/models, content per vehicle, nomination and SOP schedule", "volume, concentration and revenue visibility"),
            ("Product Profit Pools", "filing-reported product revenue, volume, ASP/mix, gross margin, gross-profit contribution and lifecycle stage", "segment growth and consolidated margin mix"),
            ("Pricing / Annual Reduction", "OEM annual price-down clauses, raw-material pass-through, rebates, FX clauses and launch pricing", "realized ASP and pricing power"),
            ("Capacity / Utilization", "effective capacity, utilization, new-plant ramp, PPAP/SOP timing, depreciation and overseas localization", "operating leverage and ramp losses"),
            ("Cost / Margin Bridge", "aluminum/steel/rubber/plastics/electronics exposure as applicable, labor, freight, yield and product mix", "gross-margin attribution rather than proxy correlation"),
            ("Working Capital / Cash", "receivables and notes, inventory, contract assets/liabilities, OCF/NI, capex, depreciation and FCF", "cash conversion and customer bargaining power"),
            ("Reinvestment / ROIC", "incremental fixed assets/CIP/capex versus incremental revenue, EBIT and invested capital", "whether expansion creates value"),
            ("Second Curves", "customer nomination, order amount, delivery period, unit economics, required capex and revenue recognition for robotics/liquid cooling or other adjacencies", "optionality separated from core value"),
        ],
    )


def _consumer_staples_playbook(symbol: str, combined_text: str) -> tuple[str, list[tuple[str, str, str]]] | None:
    subsectors = consumer_staples_subsector_hints(symbol, combined_text)
    if not subsectors:
        return None
    if "functional_beverage" in subsectors:
        return (
            "consumer staples / functional beverage",
            [
                ("Category Demand", "energy-drink category growth, temperature/weather, outdoor/blue-collar traffic, convenience-store and traditional-channel sell-through", "volume runway and seasonality"),
                ("Core SKU", "Dongpeng Special Drink volume, ASP, terminal price, regional penetration, same-store terminal productivity", "core revenue durability and valuation multiple"),
                ("Second Curve", "electrolyte water, juice tea, coffee/tea SKU shelf penetration, repeat purchase, cannibalization versus incremental demand", "revenue growth quality and optionality"),
                ("Channel Health", "distributor inventory, contract liabilities/prepayments, rebate/lottery policy, terminal promotion intensity", "forward revenue visibility and channel stuffing risk"),
                ("Cost / Margin", "sugar, PET/can/packaging, logistics, product mix, advertising and selling-expense ratio", "gross margin and operating leverage"),
                ("Cash / Capital Return", "OCF/NI, receivables, inventory turnover, dividend/buyback execution, ROE sustainability", "earnings quality and downside support"),
            ],
        )
    if "baijiu" in subsectors:
        return (
            "baijiu / consumer channel",
            [
                ("Price", "wholesale price, retail price, promotion intensity", "brand power"),
                ("Channel", "channel inventory, distributor payment, contract liabilities", "cycle pressure"),
                ("Demand", "banquet/business demand, sell-through, regional traffic", "volume"),
                ("Mix", "high-end/sub-high-end mix, product upgrade/downgrade", "margin"),
                ("Cash", "receivables, advance receipts, cash conversion", "quality"),
            ],
        )
    return (
        "consumer staples / food-beverage channel",
        [
            ("Demand", "category growth, weather/traffic, retail/catering channel sell-through, regional penetration", "volume and mix"),
            ("Price / Mix", "ASP, premiumization, discounting, product mix, new-product repeat purchase", "revenue and gross margin"),
            ("Channel", "contract liabilities/prepayments, distributor inventory, receivables, rebate and promotion policy", "revenue visibility and channel health"),
            ("Cost", "sugar, raw milk/meat/grain/oil/PET/packaging/logistics depending on subsector", "gross margin"),
            ("Cash / Quality", "OCF/NI, inventory freshness, receivables, dividend/buyback, ROE sustainability", "earnings quality and downside"),
        ],
    )


def _battery_playbook() -> tuple[str, list[tuple[str, str, str]]]:
    return (
        "battery / energy-storage chain",
        [
            ("Demand", "NEV sales/penetration, power-battery installation GWh, storage tenders/shipments GWh", "volume and mix"),
            ("Share", "domestic/global battery-install share, key customer mix, overseas certification", "competitive position"),
            ("Price", "battery ASP, lithium/material pass-through, pricing clauses", "revenue and gross margin"),
            ("Cost", "lithium carbonate, cathode/anode/electrolyte, manufacturing yield, warranty", "unit margin"),
            ("Capacity", "effective capacity, utilization, new bases, capex and depreciation", "operating leverage"),
            ("Backlog", "contract liabilities, orders, storage pipeline, customer concentration", "visibility"),
            ("Cash / Return", "OCF/NI, working capital, capex, FCF and ROIC", "earnings quality and reinvestment return"),
        ],
    )


def _detect_playbook(symbol: str, combined_text: str) -> tuple[str, list[tuple[str, str, str]]]:
    lower = f"{symbol}\n{combined_text}".lower()
    # Structured company identity outranks incidental keywords from generic
    # metals, software, telecom, or thematic contexts.
    if has_lithium_battery_symbol_hint(symbol):
        return _battery_playbook()
    if is_automotive_components_text(symbol, combined_text):
        return _automotive_components_playbook()
    if is_telecom_operator_text(symbol, combined_text):
        return (
            "telecom operator / high-dividend SOE",
            [
                ("Mobile", "mobile subscribers, 5G penetration, mobile ARPU, DOU, churn, package mix", "service revenue and margin durability"),
                ("Broadband/Home", "broadband subscribers, household ARPU, gigabit penetration, smart-home attach", "cash-cow stability"),
                ("Enterprise/Cloud", "IDC, cloud revenue, cloud gross margin, AI/industry-digital revenue, contract liabilities", "second-curve growth and margin mix"),
                ("Capex", "5G/cloud/AI capex, depreciation, network utilization, capex-to-revenue", "FCF and ROIC"),
                ("Cash/Dividend", "OCF, FCF after capex, payout ratio, net cash/debt, dividend yield", "defensive yield and downside protection"),
                ("Peer Allocation", "China Mobile / China Unicom comparison, ARPU, ROE, FCF, dividend, cloud growth", "relative allocation"),
            ],
        )
    if is_insurance_text(symbol, combined_text):
        return _insurance_playbook()
    if is_hog_breeding_text(symbol, combined_text):
        return (
            "hog breeding / live-hog cycle",
            [
                ("Realized Hog Price", "company monthly commodity-hog ASP, national live-hog spot price, DCE live-hog futures curve", "revenue and cycle stage"),
                ("Cost Curve", "monthly complete hog-breeding cost, feed cost, PSY/FCR, mortality/disease spend, finance cost", "unit spread and downside resilience"),
                ("Volume / Weight", "commodity-hog output, average slaughter weight, piglet/breeding-hog mix, capacity utilization", "sales kilograms and operating leverage"),
                ("Supply Cycle", "national breeding-sow inventory, company sow herd, piglet price, slaughter volume, frozen pork inventory", "timing and amplitude of hog-price reversal"),
                ("Cash / Balance Sheet", "OCF, inventory and biological assets, impairment, capex, debt maturity, financing access", "bottom-cycle survival and dilution risk"),
                ("Valuation / Sensitivity", "hog-price sensitivity table, implied hog price from current market cap, PB floor cross-check", "rating, position size, and falsification trigger"),
            ],
        )
    consumer_playbook = _consumer_staples_playbook(symbol, combined_text)
    if consumer_playbook is not None:
        return consumer_playbook
    metals_playbook = _metals_playbook(symbol, combined_text)
    if _metals_context_triggered(combined_text) and metals_playbook is not None:
        return metals_playbook
    metals_hits = sum(
        token in combined_text
        for token in (
            "有色金属",
            "铜",
            "铝",
            "锌",
            "铅",
            "锡",
            "金",
            "银",
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
    battery_chain_hits = sum(
        token in combined_text
        for token in ("动力电池", "储能电池", "锂离子电池", "正极材料", "磷酸铁锂", "三元材料", "前驱体", "电池材料")
    ) + sum(token in lower for token in ("300750", "battery", "cathode", "precursor", "lfp"))
    if metals_hits >= 2 and battery_chain_hits == 0:
        if metals_playbook is not None:
            return metals_playbook
        return (
            "nonferrous metals / mining",
            [
                ("Cycle", "SHFE/LME/COMEX price, futures curve, inventory, import/export, TC/RC or processing spread", "cycle stage and realized price"),
                ("Resource", "reserve/resource tonnage, grade, recovery rate, mine life, equity output by mine", "asset quality and volume runway"),
                ("Cost Curve", "cash cost, AISC/unit cost, sustaining capex, energy/labor/FX sensitivity", "margin resilience and downside"),
                ("Segment Mix", "mining, smelting/refining, processing, trading revenue and margin split", "valuation bucket and multiple/NAV treatment"),
                ("Projects", "capex budget, construction-in-progress, commissioning, permitting, jurisdiction risk", "NAV/SOTP optionality and execution risk"),
                ("Risk/Cash", "hedging, derivatives, inventory marks, working capital, OCF/NI, leverage, debt maturity", "earnings quality and cycle survival"),
            ],
        )
    wind_hits = sum(
        token in combined_text
        for token in ("风电", "海上风电", "海风", "塔筒", "管桩", "导管架", "海工", "风电装备", "风机")
    ) + sum(token in lower for token in ("wind power", "offshore wind", "monopile", "jacket foundation", "tower"))
    battery_material_hits = sum(
        token in combined_text
        for token in ("正极材料", "磷酸铁锂", "三元材料", "前驱体", "锂电材料", "电池材料")
    ) + sum(token in lower for token in ("cathode", "precursor", "lfp"))
    battery_hits = sum(
        token in combined_text
        for token in ("动力电池", "储能电池", "锂离子电池", "电芯")
    ) + sum(token in lower for token in ("300750", "battery cell", "power battery"))
    if wind_hits >= 2 and battery_material_hits == 0 and battery_hits == 0:
        return (
            "wind power / offshore foundation equipment",
            [
                ("Demand", "offshore wind tenders, project approvals, grid-connection schedule, overseas capex cycle", "order intake and delivery volume"),
                ("Backlog", "new orders, order backlog, contract liabilities, order-to-revenue ratio", "revenue visibility"),
                ("Price", "tower/monopile/jacket ASP, project mix, export pricing, FX clauses", "revenue and gross margin"),
                ("Cost", "steel plate, welding/processing, logistics, port cost, FX, warranty", "project gross margin"),
                ("Capacity", "base capacity, dock/port resources, utilization, capex and depreciation", "operating leverage"),
                ("Cash", "prepayments, receivables, inventory, OCF/NI, capex, debt maturity", "cash conversion and balance-sheet risk"),
            ],
        )
    if "300750" not in lower and (
        any(
            token in combined_text
            for token in ("正极材料", "磷酸铁锂", "三元材料", "前驱体", "锂电材料", "电池材料")
        )
        or any(token in lower for token in ("cathode", "precursor", "lfp"))
    ):
        return (
            "lithium battery materials / cathode chain",
            [
                ("Demand", "LFP / ternary cathode output, downstream battery installation, ESS demand, customer order cadence", "shipment volume"),
                ("Price", "cathode ASP, lithium carbonate pass-through, processing fee / spread, contract pricing clauses", "revenue and gross margin"),
                ("Cost", "lithium carbonate, iron phosphate / precursor, energy, depreciation, inventory-cost lag", "unit margin"),
                ("Capacity", "effective capacity, utilization, new-line ramp, maintenance shutdowns", "operating leverage"),
                ("Customers", "CATL/BYD/major customer mix, concentration, credit terms, contract liabilities", "visibility and bargaining power"),
                ("Cash", "receivables, notes, inventory, OCF/NI, credit impairment", "earnings quality"),
            ],
        )
    if is_lithium_battery_text(symbol, combined_text):
        return _battery_playbook()
    if any(token in lower for token in ["002460", "赣锋", "锂", "lithium"]):
        return (
            "lithium / metals cycle",
            [
                ("Price", "lithium carbonate/hydroxide price, futures curve, realized ASP", "revenue and inventory gains/losses"),
                ("Spread", "ore/salt-lake/brine cost, processing spread, by-product credits", "cash margin"),
                ("Inventory", "industry and company inventory, downstream restocking/destocking", "cycle stage"),
                ("Output", "equity resource output, conversion capacity, ramp schedule", "volume"),
                ("Demand", "battery installation, ESS, cathode output, export/import", "end demand"),
                ("Cost Curve", "peer cost curve, project grade, AISC/cash cost, impairment risk", "moat and downside"),
            ],
        )
    if any(token in combined_text for token in ["白酒", "经销商", "批价", "动销"]):
        return (
            "baijiu / consumer channel",
            [
                ("Price", "wholesale price, retail price, promotion intensity", "brand power"),
                ("Channel", "channel inventory, distributor payment, contract liabilities", "cycle pressure"),
                ("Demand", "banquet/business demand, sell-through, regional traffic", "volume"),
                ("Mix", "high-end/sub-high-end mix, product upgrade/downgrade", "margin"),
                ("Cash", "receivables, advance receipts, cash conversion", "quality"),
            ],
        )
    if any(token in combined_text for token in ["水泥", "熟料", "防水", "玻璃", "建材"]):
        return (
            "building materials",
            [
                ("Demand", "property completion, infrastructure, regional construction starts", "volume"),
                ("Price", "cement/clinker/glass/waterproof ASP and regional spread", "revenue"),
                ("Capacity", "kiln utilization, capacity discipline, inventory days", "cycle stage"),
                ("Cost", "coal, soda ash, asphalt, energy and logistics", "gross margin"),
                ("Cash", "receivables, bills, credit impairment, operating cash flow", "balance-sheet quality"),
            ],
        )
    return (
        "generic company / sector",
        [
            ("Demand", "end-market volume, order/backlog, customer budget, channel sell-through", "revenue"),
            ("Price", "ASP, discount, mix, contract terms", "margin"),
            ("Cost", "raw material, labor, depreciation, logistics, warranty", "unit economics"),
            ("Capacity", "utilization, capex, bottleneck, operating leverage", "profit elasticity"),
            ("Competition", "market share, peer price behavior, substitution", "moat"),
            ("Cash", "working capital, receivables, inventory, free cash flow", "earnings quality"),
        ],
    )


def build_industry_kpi_context(
    symbol: str,
    curr_date: str,
    *,
    filing_intelligence_context: str = "",
    industry_cycle_context: str = "",
    company_business_model_context: str = "",
    commodity_context: str = "",
    metals_mining_context: str = "",
    peer_comparison_context: str = "",
    investor_interaction_context: str = "",
    policy_planning_context: str = "",
    web_fact_check_context: str = "",
    insurance_context: str = "",
    knowledge_planet_context: str = "",
) -> str:
    gated_insurance_context = (
        insurance_context if _insurance_context_triggered(insurance_context) else ""
    )
    combined = "\n".join(
        [
            filing_intelligence_context,
            industry_cycle_context,
            company_business_model_context,
            gated_insurance_context,
            metals_mining_context,
            commodity_context,
            peer_comparison_context,
            investor_interaction_context,
            policy_planning_context,
            web_fact_check_context,
            knowledge_planet_context,
        ]
    )
    playbook, kpis = _detect_playbook(symbol, combined)
    evidence = _matching_lines(
        combined,
        (
            r"revenue|profit|gross margin|ASP|price|latest_price|change_over_window",
            r"capacity|utilization|shipment|installation|GWh|market share|share",
            r"contract liabilit|backlog|order|inventory|cash flow|capex",
            r"NBV|embedded value|P/EV|solvency|COR|loss ratio|expense ratio|investment yield|bancassurance|agent productivity|CSM|NCSM",
            r"hog|pig|piglet|sow|live hog|slaughter|complete cost|breeding sow|pork|DCE|LH\d+|ASP",
            r"\u751f\u732a|\u5546\u54c1\u732a|\u4ed4\u732a|\u79cd\u732a|\u80fd\u7e41\u6bcd\u732a|\u6bcd\u732a\u5b58\u680f|\u732a\u4ef7|\u732a\u5468\u671f|\u51fa\u680f|\u5c60\u5bb0|\u5b8c\u5168\u6210\u672c|\u81ea\u7e41\u81ea\u517b|\u732a\u8089",
            r"铝|铜|锌|铅|锡|金|银|氧化铝|电力|电价|铝土矿|加工费|TC/RC|AISC|品位|储量|权益产量|锂|电池|储能|装机|份额|产能|利用率|合同负债|库存|价格|毛利|现金流",
            r"ARPU|subscriber|broadband|cloud|IDC|capex|dividend|payout|用户|宽带|天翼云|智算|资本开支|分红|派息",
        ),
        limit=10,
    )
    analyst_instructions = [
        "- Do not let a generic sector label replace the KPI map. State which KPI layers are verified, partial, or missing.",
        "- If the report uses cycle language, connect it to at least demand, price/spread, inventory/backlog, and capacity/utilization evidence.",
        "- If a thesis-critical KPI is missing, cap conviction or move the item to the verification calendar instead of converting it into a hard trigger.",
    ]
    if playbook == "hog breeding / live-hog cycle":
        analyst_instructions.insert(
            2,
            "- For hog breeders, do not use consumer-staples or battery-chain KPIs. Force the analysis through hog ASP, complete cost, sales kilograms, breeding-sow supply, cash survival, and hog-price sensitivity.",
        )
    if playbook == "insurance / integrated financial services":
        analyst_instructions.insert(
            2,
            "- For insurers, PE is only a cross-check. Force the thesis through NBV, EV/P-EV, solvency, investment-yield spread, P&C COR, dividend capacity, and SOTP/subsidiary separation.",
        )
    missing_rows = [
        f"- {name}: verify {metric}; explain impact on {driver}."
        for name, metric, driver in kpis
    ]
    return "\n".join(
        [
            f"# Industry KPI Checklist for {symbol} as of {curr_date}",
            "",
            f"- Playbook: {playbook}",
            "- Purpose: force the report to verify sector-native operating data before drawing cycle, moat, or valuation conclusions.",
            "",
            "## Required KPI Map",
            "| KPI layer | Required public evidence | Financial driver |",
            "| --- | --- | --- |",
            *[f"| {name} | {metric} | {driver} |" for name, metric, driver in kpis],
            "",
            "## Knowledge Planet Treatment",
            "- If Knowledge Planet provides industry weekly data, channel checks, company research feedback, or PDF research lenses, map each useful clue into the KPI layer above with evidence status: private/proxy, public-verified, stale, conflicting, or unverified.",
            "- Sell-side promotion and target-market-cap language cannot directly upgrade a KPI. Convert it into product price, volume, cost, inventory, order, cash-flow, or valuation assumptions before using it.",
            "",
            "## Evidence Already Present",
            *([f"- {line}" for line in evidence] if evidence else ["- No compact KPI evidence was extracted from existing contexts."]),
            "",
            "## Missing / High-Priority Public Data",
            *missing_rows,
            "",
            "## Analyst Instructions",
            *analyst_instructions,
        ]
    )


def get_industry_kpi_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
) -> str:
    supplied = dict(contexts or {})
    return build_industry_kpi_context(
        ticker,
        curr_date,
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        industry_cycle_context=supplied.get("industry_cycle_context", ""),
        company_business_model_context=supplied.get("company_business_model_context", ""),
        commodity_context=supplied.get("commodity_context", ""),
        metals_mining_context=supplied.get("metals_mining_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        investor_interaction_context=supplied.get("investor_interaction_context", ""),
        policy_planning_context=supplied.get("policy_planning_context", ""),
        web_fact_check_context=supplied.get("web_fact_check_context", ""),
        insurance_context=supplied.get("insurance_context", ""),
        knowledge_planet_context=supplied.get("knowledge_planet_context", ""),
    )
