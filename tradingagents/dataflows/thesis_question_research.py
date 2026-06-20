"""Company-specific thesis questions for deeper bull/bear debate.

This module is deterministic and evidence-first: it turns the already fetched
A-share context pack into a compact interrogation agenda that downstream agents
must answer before they can sound highly confident.
"""

from __future__ import annotations

import re

from .industry_identity import is_hog_breeding_text


QuestionRow = tuple[str, str, str, str, str, str]


def _lower(text: str | None) -> str:
    return (text or "").lower()


def _triggered(context: str | None) -> bool:
    return "status: triggered" in _lower(context)


def _find_lines(text: str | None, patterns: tuple[str, ...], *, limit: int = 8) -> list[str]:
    if not text:
        return []
    regexes = [re.compile(pattern, re.I) for pattern in patterns]
    rows: list[str] = []
    for raw in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        line = raw.strip()
        if not line:
            continue
        if any(regex.search(line) for regex in regexes):
            rows.append(line[:280])
        if len(rows) >= limit:
            break
    return rows


def _detect_archetype(
    symbol: str,
    *,
    filing_intelligence_context: str = "",
    company_business_model_context: str = "",
    industry_kpi_context: str = "",
    metals_mining_context: str = "",
    consumer_staples_context: str = "",
    optical_module_context: str = "",
    software_context: str = "",
    insurance_context: str = "",
    medical_device_context: str = "",
    biopharma_context: str = "",
    building_materials_context: str = "",
    dividend_defensive_context: str = "",
    compute_leasing_context: str = "",
    shipping_context: str = "",
    knowledge_planet_context: str = "",
) -> str:
    text = "\n".join(
        [
            symbol,
            filing_intelligence_context,
            company_business_model_context,
            industry_kpi_context,
            metals_mining_context,
            consumer_staples_context,
            optical_module_context,
            software_context,
            insurance_context,
            medical_device_context,
            biopharma_context,
            building_materials_context,
            dividend_defensive_context,
            compute_leasing_context,
            shipping_context,
            knowledge_planet_context,
        ]
    )
    lower = _lower(text)
    if is_hog_breeding_text(symbol, text):
        return "hog-breeding cyclical company"
    if _triggered(metals_mining_context):
        if "aluminum" in lower or "601600" in lower or "000807" in lower:
            return "aluminum integrated producer"
        if "copper" in lower or any(code in lower for code in ("601168", "601899", "600362", "000630", "000878")):
            return "copper / multi-metal miner-smelter"
        if "gold" in lower or "precious" in lower or "600547" in lower:
            return "precious-metal miner"
        return "metals / mining company"
    if _triggered(consumer_staples_context):
        return "consumer-staples operating company"
    if _triggered(optical_module_context):
        return "AI optical-module hardware company"
    if _triggered(software_context):
        return "software / SaaS company"
    if _triggered(insurance_context):
        return "insurance company"
    if _triggered(medical_device_context):
        return "medical-device company"
    if _triggered(biopharma_context):
        return "biopharma / pharma-services company"
    if _triggered(building_materials_context):
        return "building-materials cyclical company"
    if _triggered(compute_leasing_context):
        return "compute-leasing transition company"
    if _triggered(dividend_defensive_context):
        return "dividend-defensive candidate"
    if "telecom operator" in lower or "601728" in lower:
        return "telecom operator / high-dividend SOE"
    if "banking" in lower or "bank" in lower:
        return "bank / financial institution"
    if "shipping" in lower or "freight" in lower:
        return "shipping / freight-cycle company"
    return "general A-share company"


def _rows_for_archetype(archetype: str) -> list[QuestionRow]:
    if archetype == "aluminum integrated producer":
        return [
            ("AL-1", "Is the company a low-cost integrated aluminum profit pool, or just an aluminum-price beta vehicle?", "prove realized aluminum ASP, alumina self-supply, power cost, and segment margin advantage", "attack alumina, bauxite, power, anode, and inventory lags that erase aluminum-price upside", "realized ASP vs SHFE/LME, alumina/bauxite/power/anode cost, segment gross margin", "decides whether valuation should be SOTP/cost-advantage credit or simple cyclical beta"),
            ("AL-2", "Where are we in the aluminum cycle, and what would move the cycle from bottom-testing to confirmed upcycle?", "prove inventories, operating rates, demand mix, and supply discipline are turning together", "attack property/export weakness, restarts, policy loosening, or weak premium/discount evidence", "LME/SHFE inventory, LME-SHFE spread, import arbitrage, operating rate, demand channels", "sets rating confidence and whether position should be staged"),
            ("AL-3", "Which segment actually creates incremental profit: alumina, primary aluminum, trading, energy, or overseas assets?", "separate segment revenue, margin, capex, and utilization; show profit-pool durability", "attack over-blended PE and low-quality trading revenue", "segment profit split, capex/CIP, project ramp, minority interest, cash conversion", "drives SOTP/NAV and prevents consolidated PE shortcuts"),
            ("AL-4", "What is the downside if aluminum price falls but alumina or power cost stays sticky?", "show trough earnings, balance-sheet survival, and dividend/FCF coverage", "stress margin compression, working capital, debt cost, capex, and impairment", "stress-case price deck, unit cost bridge, OCF/NI, leverage, dividend coverage", "defines safety price and invalidation triggers"),
        ]
    if archetype == "copper / multi-metal miner-smelter":
        return [
            ("CM-1", "Is the value in scarce mine resources or in lower-multiple smelting/trading throughput?", "prove reserve/resource quality, grade, mine life, equity output, and AISC advantage", "attack weak resource disclosure, falling grade, high AISC, and smelting/trading dilution", "mine-by-mine reserves, grade, recovery, equity output, AISC/cash cost, segment margin", "decides NAV/SOTP weight and whether market should pay resource scarcity premium"),
            ("CM-2", "Can the company compound output and NAV, or is it mostly copper-price pass-through?", "prove project ramp, capex discipline, permits, and commissioning path", "attack capex overrun, delay, jurisdiction, minority interest, and execution risk", "project timetable, capex/CIP, permits, commissioning, equity ownership, jurisdiction haircut", "drives multi-year EPS/FCF bridge and catalyst calendar"),
            ("CM-3", "How much of earnings sensitivity comes from copper price, by-products, TC/RC, and unit cost?", "show commodity-price sensitivity by metal and profit pool", "attack unhedged inventory/derivative losses and poor TC/RC pass-through", "price deck, output by metal, TC/RC, hedging, inventory, derivative marks", "sets scenario valuation and position sizing"),
            ("CM-4", "Why own this miner instead of Zijin, Jiangxi Copper, or a purer upstream peer?", "prove better risk/reward, valuation discount, balance sheet, or asset quality", "attack opportunity cost versus higher-quality or cleaner exposures", "peer NAV/PB/PE, output growth, reserves, cost curve, leverage, dividend", "forces relative allocation instead of isolated improvement"),
        ]
    if archetype == "consumer-staples operating company":
        return [
            ("CS-1", "Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality?", "prove sell-through, distributor inventory, contract liabilities, and category demand", "attack Q1/holiday timing, channel stuffing, promotions, and weak repeat demand", "channel inventory, advance receipts, receivables, raw-material cost, gross margin by category", "decides whether growth deserves a durable multiple"),
            ("CS-2", "Can gross margin improvement survive raw-material, promotion, and mix normalization?", "prove cost pass-through and durable high-margin mix", "attack temporary input-cost tailwind and rising promotion intensity", "raw-material proxies, ASP, promotion, inventory, segment gross margin", "drives EPS sustainability and safety price"),
            ("CS-3", "Is the company better than same-category peers after adjusting for growth quality and cash conversion?", "prove relative share gain and superior FCF/ROIC", "attack cheaper/better-quality peer alternatives", "peer growth, margin, inventory, receivables, OCF/NI, ROIC", "drives relative allocation"),
        ]
    if archetype == "AI optical-module hardware company":
        return [
            ("OM-1", "Is the thesis 800G/1.6T share gain, price/mix, capacity, or temporary AI supply tightness?", "prove customer qualification, shipment mix, ASP, yield, and backlog", "attack ASP erosion, customer concentration, export risk, and inventory build", "customer/order evidence, shipment mix, inventory/revenue, receivables/revenue, gross margin", "separates durable growth from cycle peak"),
            ("OM-2", "Can cash conversion keep up with reported AI growth?", "prove OCF, receivables, inventory, and capex discipline", "attack working-capital absorption and capacity overbuild", "OCF/NI, DSO, inventory days, capex, depreciation, customer payment terms", "caps valuation if earnings are not cash-backed"),
        ]
    if archetype == "software / SaaS company":
        return [
            ("SW-1", "Is this recurring product software or project-heavy delivery revenue?", "prove ARR/paid users/ARPU/renewal or backlog/acceptance economics", "attack receivables, implementation risk, low renewal visibility, and vague AI monetization", "ARR/MRR, paid users, ARPU, renewal, contract liabilities, receivables, acceptance", "decides whether SaaS-like valuation is allowed"),
            ("SW-2", "Does AI or localization change paid adoption and margins, or only narrative temperature?", "prove customer conversion, pricing, usage, and margin uplift", "attack unsupported AI optionality and commoditized service revenue", "AI paid seats, attach rate, gross margin, R&D/sales spend, retention", "keeps optionality separate from base valuation"),
        ]
    if archetype == "insurance company":
        return [
            ("IN-1", "Is value driven by NBV/EV recovery, investment spread, P&C COR, bank subsidiary, or dividend?", "prove the precise value engine and avoid mixed financial conglomerate shortcuts", "attack channel quality, solvency, investment-yield drag, COR deterioration, or SOTP over-credit", "NBV, EV, solvency, investment yield, COR, dividend coverage, subsidiary valuation", "sets P/EV, PB/ROE, and SOTP weights"),
            ("IN-2", "Is dividend yield sustainable under capital and asset-quality stress?", "prove payout capacity, capital buffer, and recurring profit", "attack capital constraints, asset impairments, and profit volatility", "payout ratio, solvency, free surplus, investment losses, regulatory capital", "defines defensive status"),
        ]
    if archetype == "hog-breeding cyclical company":
        return [
            ("HG-1", "Where exactly are we in the hog cycle: downcycle, bottom-testing, bottom-right validation, or early upcycle?", "prove the cycle stage with hog ASP, piglet price, sow inventory, slaughter/output, frozen inventory, and futures/spot confirmation", "attack false-bottom risk, inventory rebuild, weak demand, or one-source private data", "company ASP, national spot, DCE LH curve, piglet/sow price, breeding-sow inventory, slaughter volume, frozen inventory", "sets whether valuation should lean on PB floor, normalized earnings, or recovery option value"),
            ("HG-2", "Is the company creating alpha through cost advantage or just carrying hog-price beta?", "prove complete cost, PSY/FCR, mortality, feed cost, finance cost, scale efficiency, and cash survival versus peers", "attack cost disclosure sparsity, disease/mortality risk, debt pressure, capex burden, and peer cost catch-up", "monthly complete cost, feed cost, OCF, debt maturity, biological assets, impairment, peer cost", "decides whether it deserves premium PB/normalized PE and higher position size"),
            ("HG-3", "What hog price and cost spread is already implied by the current market cap?", "reverse-engineer implied hog ASP/spread and show upside if ASP moves to 14/16/18/20 CNY/kg", "attack optimism if current price already discounts recovery or if PB floor is eroding", "market cap, sales kg, cost deck, normalized PE, PB/NAV floor, losses/impairments", "prevents target-price tables from mixing PE and PB inconsistently"),
            ("HG-4", "Which Knowledge Planet clues are real operating data versus sell-side promotion?", "map private data into piglet/sow price, industry destocking, company cost/output, and catalyst clock", "attack stale, biased, non-company-specific, or unverified claims and target-market-cap leaps", "Knowledge Planet source type, date, KPI, verification status, PDF framework, public cross-check", "determines whether private intelligence upgrades the expectation gap or only creates a watch item"),
        ]
    if archetype == "bank / financial institution":
        return [
            ("BK-1", "Is low PB pricing asset-quality fear, weak ROE, or a mispriced deposit franchise?", "prove NIM, credit cost, capital, and deposit advantage", "attack NPL migration, provision weakness, fee-income pressure, and ROE dilution", "NIM, deposit cost, NPL/SML/overdue, provision coverage, CET1, ROE", "sets PB/ROE/COE valuation"),
            ("BK-2", "Why this bank rather than a higher-quality or higher-yield peer?", "prove quality received versus price paid", "attack peer opportunity cost and dividend-trap risk", "peer PB/ROE, asset quality, payout, capital, fee income", "forces relative allocation"),
        ]
    return [
        ("G-1", "What is the one variable that must be right for this stock to work over the next 6-24 months?", "identify the core bet and show verified/proxy evidence", "attack whether the core bet is already priced, too small, or contradicted by operating data", "industry KPI, forecast bridge, market expectation, valuation, recent disclosures", "prevents a generic balanced memo"),
        ("G-2", "Is the company quality good, or are we only buying a cheap valuation or hot theme?", "prove segment economics, cash conversion, moat, and capital allocation", "attack weak disclosure, poor OCF/NI, receivables/inventory, capex returns, and peer quality", "segment margin, OCF/NI, ROIC/ROE, capex, peers, management actions", "separates business quality from current odds"),
        ("G-3", "What would make the bull case clearly wrong, and what would make the bear case clearly wrong?", "state falsification signals and upgrade triggers with dates or next disclosures", "attack vague catalysts without measurable evidence", "verification calendar, next report, product prices, orders, utilization, policy, peer data", "turns research into a usable debate and action plan"),
        ("G-4", "Why is this stock the best expression versus same-industry peers or adjacent profit pools?", "prove superior probability/payoff after valuation and evidence gaps", "attack opportunity cost and cleaner alternatives", "peer valuation, margins, growth, balance sheet, position in chain", "forces capital-allocation discipline"),
    ]


def build_thesis_question_context(
    symbol: str,
    curr_date: str,
    *,
    industry_cycle_context: str = "",
    company_business_model_context: str = "",
    industry_kpi_context: str = "",
    forecast_model_context: str = "",
    quality_audit_context: str = "",
    filing_intelligence_context: str = "",
    peer_comparison_context: str = "",
    supply_chain_comparison_context: str = "",
    earnings_model_context: str = "",
    market_expectation_context: str = "",
    price_earnings_decomposition_context: str = "",
    management_capital_allocation_context: str = "",
    shareholder_structure_context: str = "",
    investor_interaction_context: str = "",
    policy_planning_context: str = "",
    web_fact_check_context: str = "",
    commodity_context: str = "",
    shipping_context: str = "",
    baijiu_context: str = "",
    compute_leasing_context: str = "",
    dividend_defensive_context: str = "",
    building_materials_context: str = "",
    consumer_staples_context: str = "",
    optical_module_context: str = "",
    biopharma_context: str = "",
    software_context: str = "",
    insurance_context: str = "",
    medical_device_context: str = "",
    metals_mining_context: str = "",
    knowledge_planet_context: str = "",
) -> str:
    archetype = _detect_archetype(
        symbol,
        filing_intelligence_context=filing_intelligence_context,
        company_business_model_context=company_business_model_context,
        industry_kpi_context=industry_kpi_context,
        metals_mining_context=metals_mining_context,
        consumer_staples_context=consumer_staples_context,
        optical_module_context=optical_module_context,
        software_context=software_context,
        insurance_context=insurance_context,
        medical_device_context=medical_device_context,
        biopharma_context=biopharma_context,
        building_materials_context=building_materials_context,
        dividend_defensive_context=dividend_defensive_context,
        compute_leasing_context=compute_leasing_context,
        shipping_context=shipping_context,
        knowledge_planet_context=knowledge_planet_context,
    )
    rows = _rows_for_archetype(archetype)
    question_table = [
        "| id | soul question | bull must prove | bear must attack | decisive evidence | PM implication |",
        "|---|---|---|---|---|---|",
    ]
    question_table.extend(
        f"| {qid} | {question} | {bull} | {bear} | {evidence} | {impact} |"
        for qid, question, bull, bear, evidence, impact in rows
    )

    decisive_lines = _find_lines(
        "\n".join(
            [
                industry_kpi_context,
                forecast_model_context,
                quality_audit_context,
                knowledge_planet_context,
            ]
        ),
        (
            r"playbook|required KPI|driver|forecast|scaffold|audit|missing|partial|verified|evidence status",
            r"price|spread|margin|output|capacity|utilization|inventory|backlog|cash|debt|NAV|SOTP|AISC|TC/RC",
        ),
        limit=10,
    )
    market_lines = _find_lines(
        "\n".join(
            [
                peer_comparison_context,
                market_expectation_context,
                price_earnings_decomposition_context,
                management_capital_allocation_context,
                shareholder_structure_context,
                investor_interaction_context,
                policy_planning_context,
                web_fact_check_context,
                commodity_context,
                shipping_context,
                knowledge_planet_context,
            ]
        ),
        (
            r"peer|expectation|valuation|PE|PB|EV|ROE|dividend|policy|question|Q&A",
            r"price|inventory|spread|freight|rate|corroborated|conflicting|unverified|missing",
        ),
        limit=10,
    )

    lines = [
        f"# Thesis Question Context for {symbol} as of {curr_date}",
        "",
        f"- Company-specific archetype: {archetype}",
        "- Purpose: force each report to start from the target's real economic contradictions, not a generic industry template.",
        "- Debate use: the bull must answer the bull-proof column; the bear must attack the bear-attack column; the PM must cap conviction when a thesis-critical question remains unanswered.",
        "",
        "## Company-Specific Soul Questions",
        *question_table,
        "",
        "## Extracted Evidence Agenda",
    ]
    if decisive_lines:
        lines.extend(["", "### Operating / Forecast / Audit Signals", *[f"- {line}" for line in decisive_lines]])
    else:
        lines.append("- No high-signal operating or forecast lines were extracted; treat this as a research-depth gap.")
    if market_lines:
        lines.extend(["", "### Market / Peer / Verification Signals", *[f"- {line}" for line in market_lines]])
    else:
        lines.append("- No high-signal market, peer, or verification lines were extracted; keep relative allocation lower-confidence.")
    lines.extend(
        [
            "",
            "## Debate And Report Rules",
            "- Opening bull case: answer at least the top three soul questions before adding broad positives.",
            "- Opening bear case: attack the same question IDs; do not introduce generic downside without linking it to a question.",
            "- Missing evidence rule: a missing thesis-critical answer is neutral for direction but reduces confidence, SOTP credit, and position size.",
            "- Aluminum cost rule: missing alumina, power, or anode cost evidence cannot prove profit deterioration; bearish margin claims need verified cost squeeze, segment-margin compression, inventory/cash deterioration, peer opportunity cost, or valuation stress.",
            "- Hog-breeder rule: force bull, bear, and PM to answer HG questions when triggered. Do not accept PE-only valuation, generic consumer-staples framing, or a scenario table that mixes PE and PB without a selected-value reconciliation.",
            "- Research manager: render a compact question-led issue log with question, bull answer, bear attack, evidence verdict, valuation/sizing impact, and next verification.",
            "- Portfolio manager: unresolved thesis-critical questions must appear in Evidence Gaps & Data Coverage or Verification Calendar and should cap rating/sizing confidence.",
        ]
    )
    return "\n".join(lines)


def get_thesis_question_context(ticker: str, curr_date: str, **supplied: str) -> str:
    return build_thesis_question_context(
        ticker,
        curr_date,
        industry_cycle_context=supplied.get("industry_cycle_context", ""),
        company_business_model_context=supplied.get("company_business_model_context", ""),
        industry_kpi_context=supplied.get("industry_kpi_context", ""),
        forecast_model_context=supplied.get("forecast_model_context", ""),
        quality_audit_context=supplied.get("quality_audit_context", ""),
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        supply_chain_comparison_context=supplied.get("supply_chain_comparison_context", ""),
        earnings_model_context=supplied.get("earnings_model_context", ""),
        market_expectation_context=supplied.get("market_expectation_context", ""),
        price_earnings_decomposition_context=supplied.get("price_earnings_decomposition_context", ""),
        management_capital_allocation_context=supplied.get("management_capital_allocation_context", ""),
        shareholder_structure_context=supplied.get("shareholder_structure_context", ""),
        investor_interaction_context=supplied.get("investor_interaction_context", ""),
        policy_planning_context=supplied.get("policy_planning_context", ""),
        web_fact_check_context=supplied.get("web_fact_check_context", ""),
        commodity_context=supplied.get("commodity_context", ""),
        shipping_context=supplied.get("shipping_context", ""),
        baijiu_context=supplied.get("baijiu_context", ""),
        compute_leasing_context=supplied.get("compute_leasing_context", ""),
        dividend_defensive_context=supplied.get("dividend_defensive_context", ""),
        building_materials_context=supplied.get("building_materials_context", ""),
        consumer_staples_context=supplied.get("consumer_staples_context", ""),
        optical_module_context=supplied.get("optical_module_context", ""),
        biopharma_context=supplied.get("biopharma_context", ""),
        software_context=supplied.get("software_context", ""),
        insurance_context=supplied.get("insurance_context", ""),
        medical_device_context=supplied.get("medical_device_context", ""),
        metals_mining_context=supplied.get("metals_mining_context", ""),
        knowledge_planet_context=supplied.get("knowledge_planet_context", ""),
    )
