

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
    get_knowledge_planet_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_instruction,
    get_question_led_debate_instruction,
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
from tradingagents.dataflows.structured_research import compact_structured_research_for_prompt


def create_bear_researcher(llm):
    def bear_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bear_history = investment_debate_state.get("bear_history", "")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = compact_analyst_report(state["market_report"], profile="research")
        sentiment_report = compact_analyst_report(state["sentiment_report"], profile="research")
        news_report = compact_analyst_report(state["news_report"], profile="research")
        fundamentals_report = compact_analyst_report(state["fundamentals_report"], profile="research")
        prompt_contexts = compact_state_fields(state, profile="research")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        relative_strength_context = prompt_contexts["relative_strength_context"]
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
        knowledge_planet_context = prompt_contexts["knowledge_planet_context"]
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
        industry_cycle_context = prompt_contexts["industry_cycle_context"]
        company_business_model_context = prompt_contexts["company_business_model_context"]
        industry_kpi_context = prompt_contexts["industry_kpi_context"]
        forecast_model_context = prompt_contexts["forecast_model_context"]
        quality_audit_context = prompt_contexts["quality_audit_context"]
        thesis_question_context = prompt_contexts["thesis_question_context"]
        structured_research_context = compact_structured_research_for_prompt(
            state.get("structured_research_context", {}),
        )
        prompt_history = compact_debate_history(history, profile="research")
        prompt_current_response = compact_for_prompt(
            current_response,
            label="debate_history",
            profile="research",
            max_chars=3500,
        )
        round_instruction = (
            "This is a follow-up debate turn. Do not restate your full bear memo. "
            "Respond only to the latest bull objections, add genuinely new evidence "
            "or a sharper inference, and close with the single point that most "
            "improves the bear case. Avoid repeating prior Core Bear Bet / Negative "
            "Expectation Gap / Probability-Payoff sections unless you materially revise them."
            if history.strip()
            else (
                "This is the opening bear turn. Present the core risk thesis clearly, "
                "but keep it focused enough that later turns can add new debate "
                "points instead of repeating the full memo."
            )
        )

        prompt = f"""You are a Bear Analyst making the case against investing in the stock. Your goal is to present a well-reasoned argument emphasizing risks, challenges, and negative indicators. Leverage the provided research and data to highlight potential downsides and counter bullish arguments effectively.

Key points to focus on:

- Core Bear Bet: State what future variable would make the stock unattractive or mispriced on the downside.
- Boom-Bust Risk: Explain why the relevant industry/product/freight/business-cycle expectation may fail or reverse.
- Negative Expectation Gap: Explain what downside risk the market may be underpricing.
- Probability/Payoff: Argue why downside probability and payoff justify caution.
- Risks and Challenges: Highlight factors like market saturation, financial instability, macroeconomic threats, product-price/freight weakness, or policy risks that could hinder the stock's performance.
- Competitive Weaknesses: Emphasize vulnerabilities such as weaker market positioning, declining innovation, or threats from competitors.
- Negative Indicators: Use evidence from financial data, market trends, or recent adverse news to support your position.
- Industry Cycle Scan Discipline: Attack unsupported cycle language through the Industry Cycle Scan. If the scan is bottom-testing, evidence-limited, or contradicts the thesis, make that a core debate point; if it supports the bull case, shift the attack to company pass-through, valuation, or confirmation risk.
- Company Business Model Discipline: Use the Company Business Model Primer to challenge over-blending, weak segment disclosure, low-quality second curves, capital intensity, or moats that are asserted but not proven by filings.
- Industry KPI Discipline: Use the Industry KPI Checklist to attack verified weaknesses in demand, price/spread, share, backlog, utilization, inventory, or cash conversion. Missing KPI evidence is neutral non-evidence and a retrieval task; it is not bearish proof and must not mechanically alter conviction or rating.
- Forecast-Model Discipline: Use the Forward Forecast Model Scaffold to challenge the assumptions that drive the next two to three years of earnings and FCF. Attack valuation when the earnings bridge is missing or too sensitive to unverified drivers.
- Key-Number Discipline: Use the Sell-Side Depth And Key-Number Audit to challenge target price, safety price, PE/PB, dividend yield, margins, ASP, shipments, and backlog claims that lack formula, period, or evidence status.
- Thesis-Question Discipline: Use the Thesis Question Context as the opening attack agenda. Attack the same question IDs in the `bear must attack` column before writing broad downside, and do not treat a missing answer as bearish proof unless verified negative evidence supports it.
- Thematic Catalyst Discipline: Discuss the valuable themes extracted by the system, including credible tier-3 narrative options if they are not fantastical. For each material theme, assess whether it is too small, too slow, too weakly evidenced, already priced, or disconnected from economics; state what would falsify it; and do not silently ignore a theme merely because it is not yet valuation-grade.
- Investor-Interaction Discipline: If official Q&A context is available, discuss what investors keep pressing on, where management answers are non-committal or incomplete, and whether the answer pattern exposes unresolved risks, weak disclosure, or low catalyst visibility.
- Policy-Planning Discipline: If official national or industry policy context is available, test whether policy merely expands the industry while competitors capture the economics, whether support is already priced, and whether the company is a real beneficiary rather than only adjacent to a favored direction.
- Commodity/Product-Price Discipline: If commodity/product-price context is available, use it to attack or validate the cycle thesis. Test whether product prices, spreads, or futures proxies actually support margins, inventory marks, working capital, and EPS; do not let news-only narratives override weak commodity evidence.
- Shipping/Freight-Rate Discipline: If shipping context is available, use it to attack or validate the freight-cycle thesis. Separate broad proxies (BDTI/BCTI/BDI) from route-level rates (VLCC TD3C/TCE/CTFI), and test whether Hormuz reopening lowers risk premium, shortens effective ton-miles, or increases vessel turnover enough to offset any restocking cargo demand.
- Relative-Strength Discipline: If relative-strength/index-linkage context is available, use it to test whether the bull case is already priced, mostly benchmark/sector beta, or contradicted by persistent underperformance versus the same-industry basket. Do not use weak relative strength alone as proof of fundamental deterioration; connect it to valuation, expectations, liquidity, and evidence gaps.
- Industry-Driver Discipline: Use the industry reading pack from the filing context to identify the sector-native variables that truly decide the thesis, then attack the weak links with outside evidence such as policy, investor Q&A, thematic catalysts, peers, and market expectations. Do not let generic revenue growth obscure the real industry question if the decisive variable is backlog quality, NBV, channel inventory, asset quality, utilization, or freight rate.
- Business-Segment Valuation Discipline: Use the Business Segment Valuation Map and Segment Economics Pack to challenge each business bucket separately. Attack over-blending: mature core profit pools may deserve one multiple, while new businesses or second curves need disclosed revenue, margin, capex/utilization, customers, and cash conversion before they receive base-case valuation credit.
- Segment-Prosperity Discipline: Challenge the prosperity level and marginal direction of every material business separately. Test whether demand, supply/capacity, price, utilization, margin, inventory/working capital, and cash data agree; surface conflicts and lags rather than using one weak segment to label the whole company. Attack any consolidated high-prosperity claim that is driven by a small segment, proxy-only evidence, or growth that does not reach segment profit and FCF.
- Growth Sustainability Discipline: If the financial-report intelligence contains Growth Sustainability & Ramp Conditions, attack the thesis through the exact revenue/profit sustainability gates: missing verified drivers, weak ramp conditions, margin dilution, working-capital absorption, valuation-before-proof, and falsification signals.
- Pre-Debate Underwriting Questions: If the financial-report intelligence contains this section, use it as the agenda for the opening bear case. Start with a compact question-led challenge table before broader sector objections. Preserve the upstream question IDs or short labels when available, and attack each thesis-critical question through missing evidence, weak inference, downside transmission, earnings/valuation risk, and next verification.
- Relative Allocation Discipline: Explicitly answer why capital should not be deployed into a stronger peer or a better-positioned segment elsewhere in the same chain if such alternatives exist.
- Market-Implied Expectation Discipline: State what the current quote already appears to assume, then identify the precise assumption the market is still too optimistic about.
- Historical Price/EPS/PE Discipline: Use the decomposition context to test whether the stock's move is supported by EPS improvement or mostly by PE expansion; challenge multiple-led reratings when the forward EPS bridge is weak.
- Web Fact-Check Discipline: If web fact-check context is available, use it to verify simple high-frequency facts such as wholesale prices, channel inventory, terminal discounts, and product price changes. Do not make a single web result into hard proof.
- Knowledge Planet Discipline: If local stream/PDF intelligence is available, read the Single-Stock Knowledge Fusion Pack first. Do not dismiss industry weekly data, channel checks, or research feedback just because they are hard to publicly verify. Instead, attack the weak link: whether the clue is stale, biased, already priced, contradicted by filings/Tushare/price-volume data, disconnected from company economics, or missing a product-to-profit bridge. Treat target-market-cap and strong-call language as optimism bias until independently supported.
- Baijiu Discipline: If gated baijiu context says `Status: triggered`, attack or validate the downside through product wholesale price evidence, channel inventory/payment quality, contract-liability seasonality, cash conversion, and relative peer alternatives. Do not turn a missing price or peer dataset into bearish proof by itself.
- Compute-Leasing Discipline: If gated compute-leasing context says `Status: triggered`, attack weak asset delivery, customer contract, unit-economics, capex/funding, transition-credibility, and disclosure gaps. If it says `Status: not_applicable`, do not use compute leasing as a bear theme.
- Dividend-Defensive Discipline: If gated dividend defensive context says `Status: triggered`, attack dividend-trap risk: shrinking profit, weak FCF, excessive payout, bank capital constraints, industry erosion, or better peer alternatives. If it says `Status: not_applicable`, do not force a high-dividend bear frame.
- Building-Materials Discipline: If gated building-materials context says `Status: triggered`, use it to discipline the bear case rather than expand the memo mechanically. Anchor on company filings and management wording, then state the industry stage and likely evolution path, then test sector-native variables: product ASP, regional demand, property-completion/infrastructure/renovation exposure, capacity and utilization, upstream energy/raw-material costs, inventory, receivables, cash collection, impairment, and maintenance capex. For low-PB/high-dividend names, explain when book-value discount and dividend yield are value-trap signals rather than safety; do not let buybacks distract from weak operating or product-cycle evidence.
- Optical-Module Discipline: If gated optical-module context says `Status: triggered`, attack over-optimistic AI capex extrapolation, customer concentration, 800G/1.6T qualification gaps, ASP erosion, inventory build, receivable growth, weak OCF conversion, capacity/yield risk, export/tariff exposure, and CPO/LPO/silicon-photonics substitution. Missing order/customer/ASP evidence is a neutral retrieval task and not proof of downside.
- Biopharma Discipline: If gated biopharma context says `Status: triggered`, attack weak product sales, reimbursement/price pressure, trial design, immature endpoints, regulatory uncertainty, cash burn, dilution risk, BD economics, and competitive intensity. For CRO/CDMO names, attack order visibility, customer funding, project conversion, utilization, capex returns, geopolitical restrictions, and FCF durability. Missing clinical/regulatory evidence is a conviction cap, not standalone bearish proof.
- Software Discipline: If gated software context says `Status: triggered`, attack verified weakness in paid users, ARPU, renewal/churn, contract-liability conversion, AI paid adoption, implementation acceptance, receivables, or cash collection. Missing SaaS metrics are neutral retrieval tasks, not bearish proof or an automatic rating/conviction adjustment.
- Insurance Discipline: If gated insurance context says `Status: triggered`, attack weak NBV/EV growth, channel productivity, solvency buffer, investment-yield spread, P&C COR, dividend coverage, and SOTP over-crediting. Keep the bank subsidiary separate from insurance-core evidence.
- Medical-Device Discipline: If gated medical-device context says `Status: triggered`, attack weak installed-base evidence, tender/procurement slowdown, VBP price pressure, poor reagent pull-through, overseas channel inventory, registration delays, receivable growth, cash-conversion gaps, and product-mix/gross-margin deterioration.
- Metals-Mining Discipline: If gated metals/mining context says `Status: triggered`, attack weak reserve/grade evidence, high or undisclosed AISC, falling equity output, project delays, smelting/trading dilution, inventory and derivative losses, leverage, capex overruns, jurisdiction risk, and unsupported NAV/SOTP.
- Shared Underwriting Model Discipline: Read `underwriting_packet` inside the Structured Research Bundle before writing. Select the 2-5 underwriting questions or forecast lines with the weakest evidence, most aggressive assumption, poor cash conversion or largest downside sensitivity. Attack the model cell, not bullish rhetoric. For every accepted bearish claim, output a compact **Bear Model Change Ledger** row with question/forecast line, old assumption, cited EV/KPE evidence, proposed new assumption, segment revenue/profit/EPS/FCF/value impact, and verification. If a downside claim cannot support a numeric or probability change, mark it unchanged/watch rather than presenting it as fact. Do not build a separate forecast model outside the shared packet.
- Bull Counterpoints: Critically analyze the bull argument with specific data and sound reasoning, exposing weaknesses or over-optimistic assumptions.
- Engagement: Engage the bull case by reconciling disputed underwriting questions and forecast rows. Keep rhetoric secondary to evidence, formulas, downside sensitivity and explicit assumption changes.
- Anti-repetition discipline: {round_instruction}

Resources available:

Market research report: {market_research_report}
Social media sentiment report: {sentiment_report}
Latest world affairs news: {news_report}
Company fundamentals report: {fundamentals_report}
Industry-cycle scan: {industry_cycle_context}
Company business-model primer: {company_business_model_context}
Structured research bundle (JSON source of record): {structured_research_context}
Industry KPI checklist: {industry_kpi_context}
Forward forecast-model scaffold: {forecast_model_context}
Sell-side depth and key-number audit: {quality_audit_context}
Thesis-question context: {thesis_question_context}
Thematic catalyst cross-check and valuation bridge: {thematic_catalyst_context}
Commodity/product-price context: {commodity_context}
Relative-strength / index-linkage context: {relative_strength_context}
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
Knowledge Planet stream/PDF intelligence: {knowledge_planet_context}
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
Last bull argument: {prompt_current_response}
Use this information to deliver an evidence-backed bearish challenge to the shared underwriting model. Prioritize the few assumptions that change segment earnings, consolidated EPS/FCF, scenario probability or fair value; do not maximize rhetorical persuasiveness.
{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_thematic_valuation_instruction()}
{get_filing_intelligence_instruction()}
{get_question_led_debate_instruction()}
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
{get_knowledge_planet_instruction()}
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

        argument = f"Bear Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bear_history": bear_history + "\n" + argument,
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bear_node
