

from tradingagents.agents.utils.agent_utils import (
    get_baijiu_instruction,
    get_biopharma_instruction,
    get_building_materials_instruction,
    get_buy_side_thesis_instruction,
    get_compute_leasing_instruction,
    get_consumer_staples_instruction,
    get_dividend_defensive_instruction,
    get_evidence_instruction,
    get_earnings_model_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_insurance_instruction,
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_optical_module_instruction,
    get_investor_interaction_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
    get_supply_chain_selection_instruction,
    get_shareholder_structure_instruction,
    get_software_instruction,
    get_three_layer_conclusion_instruction,
    get_thematic_valuation_instruction,
    get_web_fact_check_instruction,
)
from tradingagents.dataflows.prompt_compaction import (
    compact_analyst_report,
    compact_debate_history,
    compact_for_prompt,
    compact_state_fields,
)


def create_bull_researcher(llm):
    def bull_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bull_history = investment_debate_state.get("bull_history", "")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = compact_analyst_report(state["market_report"], profile="research")
        sentiment_report = compact_analyst_report(state["sentiment_report"], profile="research")
        news_report = compact_analyst_report(state["news_report"], profile="research")
        fundamentals_report = compact_analyst_report(state["fundamentals_report"], profile="research")
        prompt_contexts = compact_state_fields(state, profile="research")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        shipping_context = prompt_contexts["shipping_context"]
        filing_intelligence_context = prompt_contexts["filing_intelligence_context"]
        peer_comparison_context = prompt_contexts["peer_comparison_context"]
        supply_chain_comparison_context = prompt_contexts["supply_chain_comparison_context"]
        earnings_model_context = prompt_contexts["earnings_model_context"]
        market_expectation_context = prompt_contexts["market_expectation_context"]
        price_earnings_decomposition_context = prompt_contexts["price_earnings_decomposition_context"]
        management_capital_allocation_context = prompt_contexts["management_capital_allocation_context"]
        shareholder_structure_context = prompt_contexts["shareholder_structure_context"]
        investor_interaction_context = prompt_contexts["investor_interaction_context"]
        policy_planning_context = prompt_contexts["policy_planning_context"]
        web_fact_check_context = prompt_contexts["web_fact_check_context"]
        baijiu_context = prompt_contexts["baijiu_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
        building_materials_context = prompt_contexts["building_materials_context"]
        consumer_staples_context = prompt_contexts["consumer_staples_context"]
        optical_module_context = prompt_contexts["optical_module_context"]
        biopharma_context = prompt_contexts["biopharma_context"]
        software_context = prompt_contexts["software_context"]
        insurance_context = prompt_contexts["insurance_context"]
        medical_device_context = prompt_contexts["medical_device_context"]
        metals_mining_context = prompt_contexts["metals_mining_context"]
        prompt_history = compact_debate_history(history, profile="research")
        prompt_current_response = compact_for_prompt(
            current_response,
            label="debate_history",
            profile="research",
            max_chars=3500,
        )
        round_instruction = (
            "This is a follow-up debate turn. Do not restate your full bull memo. "
            "Respond only to the latest bear objections, add genuinely new evidence "
            "or a sharper inference, and close with the single point that most "
            "improves the bull case. Avoid repeating prior Core Bet / Expectation "
            "Gap / Probability-Payoff sections unless you materially revise them."
            if history.strip()
            else (
                "This is the opening bull turn. Present the core thesis clearly, "
                "but keep it focused enough that later turns can add new debate "
                "points instead of repeating the full memo."
            )
        )

        prompt = f"""You are a Bull Analyst advocating for investing in the stock. Your task is to build a strong, evidence-based case emphasizing growth potential, competitive advantages, and positive market indicators. Leverage the provided research and data to address concerns and counter bearish arguments effectively.

Key points to focus on:
- Core Bet: State what future variable the bullish thesis is underwriting.
- Boom-Bust Expectation: Explain why the relevant industry/product/freight/business-cycle expectation may realize.
- Expectation Gap: Explain what the market may be underpricing.
- Probability/Payoff: Argue why the upside probability and payoff justify a constructive stance.
- Positive Indicators: Use financial health, industry trends, valuation, high-frequency/proxy data, and recent news as evidence.
- Thematic Catalyst Discipline: Discuss the valuable themes extracted by the system, including credible tier-3 narrative options if they are not fantastical. For each material theme, explain how it could affect A-share expectations, probability/payoff, or valuation; distinguish core proof from optionality; state what evidence would upgrade it; and do not silently ignore a theme just because it is not yet valuation-grade.
- Primary-Investment Optionality Discipline: When the thematic bridge contains verified primary investments, non-listed equity holdings, investee IPOs, or asset-revaluation candidates, make them part of the bull testimony. Separate (a) pure value-investing incremental NAV after liquidity, lock-up, exit-probability, and double-counting haircuts from (b) A-share theme imagination and trading optionality. Explain why the market may pay attention, how much value could reasonably accrue, what catalyst could unlock it, and why it should or should not change the rating.
- Investor-Interaction Discipline: If official Q&A context is available, discuss what investors are repeatedly worried about, whether management answered substantively or evasively, and whether the answer pattern strengthens the bull case through credibility, disclosure quality, or catalyst visibility.
- Policy-Planning Discipline: If official national or industry policy context is available, explain whether policy widens the industry's future demand pool, whether this company has a credible transmission path into orders/revenue/margins, and whether policy support improves the durability of the bull case rather than merely adding slogans.
- Commodity/Product-Price Discipline: If commodity/product-price context is available, use it as a hard cycle variable. Explain whether product prices, spreads, or futures proxies support ASP, margin, inventory, and cash-flow improvement; do not substitute thematic news for commodity evidence.
- Shipping/Freight-Rate Discipline: If shipping context is available, use it as the hard freight-cycle layer. Separate broad proxies (BDTI/BCTI/BDI) from route-level rates (VLCC TD3C/TCE/CTFI), and test whether Hormuz reopening creates a bullish restocking/ton-mile/cargo-flow expectation rather than only reducing risk premium.
- Industry-Driver Discipline: Use the industry reading pack from the filing context to identify the sector-native variables that truly decide the thesis, then connect each one to outside evidence such as policy, investor Q&A, thematic catalysts, peers, and market expectations. Do not lean on generic revenue growth when the real industry question is backlog quality, NBV, channel inventory, asset quality, utilization, or freight rate.
- Business-Segment Valuation Discipline: Use the Business Segment Valuation Map and Segment Economics Pack to argue from business buckets, not only from consolidated PE. Separate the mature core business from emerging second curves, geography, and channel mix; explain which bucket deserves core valuation credit and which remains scenario/SOTP optionality.
- Relative Allocation Discipline: Explicitly answer why this stock deserves capital versus stronger same-industry peers or a better-positioned segment elsewhere in the chain; do not stop at saying the company itself is improving.
- Market-Implied Expectation Discipline: State what the current quote already appears to assume, then identify the precise assumption the market is still too pessimistic about.
- Historical Price/EPS/PE Discipline: Use the decomposition context to argue whether the upside is supported by EPS recovery/growth, multiple expansion, or a double-engine setup; do not present pure multiple expansion as hard fundamental proof.
- Web Fact-Check Discipline: If web fact-check context is available, use it to verify simple high-frequency facts such as wholesale prices, channel inventory, terminal discounts, and product price changes. Do not make a single web result into hard proof.
- Baijiu Discipline: If gated baijiu context says `Status: triggered`, the bull case must pass channel-price, contract-liability seasonality, product mix, cash conversion, and peer-basket checks. If prices or peers are missing, keep the thesis evidence-limited.
- Compute-Leasing Discipline: If gated compute-leasing context says `Status: triggered`, make the bull case pass asset, contract, unit-economics, capex/funding, and transition-credibility gates. If it says `Status: not_applicable`, do not use compute leasing as a bull theme.
- Dividend-Defensive Discipline: If gated dividend defensive context says `Status: triggered`, argue only from sustainable payout evidence: dividend stability, profit/cash-flow or bank-capital coverage, non-declining industry logic, valuation buffer, and alternatives. Do not call a high yield defensive if the context flags dividend-trap risk.
- Building-Materials Discipline: If gated building-materials context says `Status: triggered`, use it to discipline the bull case rather than expand the memo mechanically. Anchor on company filings and management wording, then state the industry stage and likely evolution path, then pass sector-native checks: product ASP or price inflection, regional demand, property-completion/infrastructure/renovation exposure, capacity and utilization, upstream energy/raw-material costs, inventory, receivables, cash collection, and capital-return proof. For low-PB/high-dividend names, explain why the discount is mispriced rather than a value trap; buybacks and dividends are shareholder-return and safety-margin evidence, not substitutes for operating proof.
- Optical-Module Discipline: If gated optical-module context says `Status: triggered`, build the bull case from supply-chain role, AI capex bridge, 800G/1.6T migration, overseas cloud customer orders, customer qualification, shipment mix, gross margin, inventory/revenue, receivables/revenue, OCF, and technology-route optionality. Do not let a generic AI hardware narrative replace evidence of delivery quality and valuation digestion.
- Biopharma Discipline: If gated biopharma context says `Status: triggered`, build the bull case from approved product sales, label expansion, clinical/regulatory milestones, reimbursement/pricing, risk-adjusted pipeline value, BD economics, and cash runway. For CRO/CDMO names, use order backlog, customer funding, capacity utilization, geopolitical risk, and FCF rather than drug-owner pipeline logic. Do not turn Phase I/II assets or unaudited pipeline wording into base-case valuation credit.
- Software Discipline: If gated software context says `Status: triggered`, build the bull case from the right software business model. For SaaS/product-led names, require paid users, ARPU, renewal, contract-liability conversion, and AI paid adoption before claiming ARPU uplift. For project-heavy software, require order backlog, acceptance, receivables, and collection. Do not use broad `software service` peer screens as valuation proof until peers are model-labeled.
- Insurance Discipline: If gated insurance context says `Status: triggered`, build the bull case from NBV/EV recovery, channel quality, solvency buffer, investment-yield spread, P&C COR, bank-subsidiary contribution, dividend durability, and SOTP optionality. Do not let a bank subsidiary turn an integrated insurer into a pure bank memo.
- Medical-Device Discipline: If gated medical-device context says `Status: triggered`, build the bull case from installed base, replacement cycle, tender cadence, reagent/consumable pull-through, VBP volume offset, product registration, overseas channel quality, service attach rate, receivables/cash conversion, and gross-margin durability. Do not value a device company like an innovative-drug pipeline.
- Metals-Mining Discipline: If gated metals/mining context says `Status: triggered`, build the bull case from reserve quality, grade, equity output, AISC/unit cost, project ramp, commodity-price source-chain evidence, hedging discipline, capex, balance-sheet survival, and NAV/SOTP. Do not let metal-price beta alone carry the thesis.
- Bear Counterpoints: Critically analyze the bear argument with specific data and sound reasoning, addressing concerns thoroughly and showing why the bull perspective holds stronger merit.
- Engagement: Present your argument in a conversational style, engaging directly with the bear analyst's points and debating effectively rather than just listing data.
- Anti-repetition discipline: {round_instruction}

Resources available:
Market research report: {market_research_report}
Social media sentiment report: {sentiment_report}
Latest world affairs news: {news_report}
Company fundamentals report: {fundamentals_report}
Thematic catalyst cross-check and valuation bridge: {thematic_catalyst_context}
Commodity/product-price context: {commodity_context}
Shipping/freight-rate context: {shipping_context}
Financial-report intelligence: {filing_intelligence_context}
Same-industry peer comparison: {peer_comparison_context}
Cross-position supply-chain comparison: {supply_chain_comparison_context}
Earnings-model context: {earnings_model_context}
Market-expectation context: {market_expectation_context}
Historical price-EPS-PE decomposition context: {price_earnings_decomposition_context}
Management/capital-allocation context: {management_capital_allocation_context}
Shareholder-structure context: {shareholder_structure_context}
Official investor-interaction context: {investor_interaction_context}
Official policy-planning context: {policy_planning_context}
Web fact-check context: {web_fact_check_context}
Gated baijiu verification context: {baijiu_context}
Gated compute-leasing verification context: {compute_leasing_context}
Gated dividend defensive verification context: {dividend_defensive_context}
Gated building-materials verification context: {building_materials_context}
Gated consumer-staples verification context: {consumer_staples_context}
Gated AI optical-module verification context: {optical_module_context}
Gated biopharma verification context: {biopharma_context}
Gated software verification context: {software_context}
Gated insurance verification context: {insurance_context}
Gated medical-device verification context: {medical_device_context}
Gated metals/mining verification context: {metals_mining_context}
Conversation history of the debate: {prompt_history}
Last bear argument: {prompt_current_response}
Use this information to deliver a compelling bull argument, refute the bear's concerns, and engage in a dynamic debate that demonstrates the strengths of the bull position.
{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_thematic_valuation_instruction()}
{get_filing_intelligence_instruction()}
{get_peer_selection_instruction()}
{get_supply_chain_selection_instruction()}
{get_earnings_model_instruction()}
{get_market_expectation_instruction()}
{get_price_earnings_decomposition_instruction()}
{get_consumer_staples_instruction()}
{get_investor_interaction_instruction()}
{get_policy_planning_instruction()}
{get_three_layer_conclusion_instruction()}
{get_management_capital_allocation_instruction()}
{get_shareholder_structure_instruction()}
{get_web_fact_check_instruction()}
{get_baijiu_instruction()}
{get_compute_leasing_instruction()}
{get_dividend_defensive_instruction()}
{get_building_materials_instruction()}
{get_optical_module_instruction()}
{get_biopharma_instruction()}
{get_software_instruction()}
{get_insurance_instruction()}
{get_medical_device_instruction()}
{get_metals_mining_instruction()}
{get_focused_report_instruction()}
"""

        response = llm.invoke(prompt)

        argument = f"Bull Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bull_history": bull_history + "\n" + argument,
            "bear_history": investment_debate_state.get("bear_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bull_node
