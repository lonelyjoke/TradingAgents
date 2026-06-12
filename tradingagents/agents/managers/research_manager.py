"""Research Manager: turns the bull/bear debate into a structured investment plan for the trader."""

from __future__ import annotations

from tradingagents.agents.schemas import ResearchPlan, render_research_plan
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_baijiu_instruction,
    get_biopharma_instruction,
    get_building_materials_instruction,
    get_buy_side_thesis_instruction,
    get_buy_side_underwriting_modules_instruction,
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
    get_price_move_attribution_instruction,
    get_investor_interaction_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_material_catalyst_instruction,
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
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)
from tradingagents.dataflows.prompt_compaction import (
    compact_debate_history,
    compact_for_prompt,
    compact_state_fields,
)


def create_research_manager(llm):
    structured_llm = bind_structured(llm, ResearchPlan, "Research Manager")

    def research_manager_node(state) -> dict:
        instrument_context = build_instrument_context(state["company_of_interest"])
        history = state["investment_debate_state"].get("history", "")
        recent_decision_context = compact_for_prompt(
            state.get("recent_decision_context", ""),
            label="recent_decision_context",
            profile="research",
        )
        prompt_contexts = compact_state_fields(state, profile="research")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        price_move_attribution_context = prompt_contexts["price_move_attribution_context"]
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
        data_coverage_context = prompt_contexts["data_coverage_context"]
        prompt_history = compact_debate_history(history, profile="research")
        continuity_context = (
            f"""
**Most Recent Same-Ticker Decision (may still be pending outcome):**
{recent_decision_context}
"""
            if recent_decision_context
            else ""
        )

        investment_debate_state = state["investment_debate_state"]

        prompt = f"""As the Research Manager and debate facilitator, your role is to critically evaluate this round of debate and deliver a clear, actionable investment plan for the trader.

{instrument_context}

---

**Rating Scale** (use exactly one):
- **Buy**: Strong conviction in the bull thesis; recommend taking or growing the position
- **Overweight**: Constructive view; recommend gradually increasing exposure
- **Hold**: Balanced view; recommend maintaining the current position
- **Underweight**: Cautious view; recommend trimming exposure
- **Sell**: Strong conviction in the bear thesis; recommend exiting or avoiding the position

Commit to a clear stance whenever the core bet has attractive probability/payoff. Reserve Hold for cases where there is no clear tradable thesis, the expectation gap is weak, or the risk/reward is not attractive. Do not use Hold merely because the evidence set is imperfect.

**Buy-Side Thesis Framework:**
- First answer: if we are bullish, what exactly are we betting on?
- Judge whether that boom-bust or business-cycle expectation can plausibly realize using verified evidence, proxy evidence, and bounded inference.
- Separate facts, proxy evidence, inference, and unverified assumptions.
- A thesis can be investable before every data point is proven if the probability/payoff is attractive and the falsification path is clear.
- Prefer Overweight over Hold when the thesis has positive expected value but still has important evidence gaps.
- Prefer Underweight over Hold when the negative thesis has positive expected value but still needs confirmation.
- For every direction, specify expectation gap, probability/payoff, catalyst path, falsification signals, and conviction level.

**Fair Cycle-Valuation Calibration:**
- Judge every stock through the same valuation x prosperity lens.
- Low valuation/low prosperity is not automatically bearish; ask whether pessimism is priced and whether an inflection is plausible.
- High prosperity/high valuation is not automatically bullish; ask whether growth durability and earnings upgrades can digest valuation.
- Low valuation/high prosperity can be attractive, but test whether earnings are sustainable or temporarily inflated.
- High valuation/low prosperity normally requires a clear future inflection, scarce growth, or other special evidence to avoid Underweight.
- The rating should reflect expected value, not style preference.

**Market-Regime Calibration:**
- Start from company evidence, then adjust for market/sector mood.
- In a normal bull market, a high-quality stock with reasonable valuation can receive a slightly more constructive rating, but an expensive/crowded stock should not be upgraded mechanically.
- In a normal bear market, keep ratings more conservative unless valuation, balance sheet, and catalysts are strong.
- In extreme pessimism with depressed valuations, allow contrarian watch or staged-entry logic for resilient companies, but avoid upgrading fragile balance sheets simply because prices are low.
- In extreme optimism with high valuations, require stronger evidence for Buy/Overweight and emphasize trimming discipline.
- For cyclical, commodity, shipping, high-beta, or event-driven stocks, calibrate the rating using the stock's own cycle drivers, not only broad-market mood.

**Evidence-Gap Calibration:**
- Missing core operating data is not neutral evidence. It is a research gap that should reduce conviction in the affected thesis.
- Missing data is also not adverse evidence by itself. Do not convert an unavailable data point into Underweight/Sell unless verified negative evidence independently supports the downside case.
- Do not let PE/PB and technical indicators replace missing product-price, spread, inventory, freight-rate, policy, capacity, or order-book evidence.
- If the unavailable data is central to the bull thesis, prefer evidence-limited Overweight/Hold or a staged watch plan over a high-conviction Buy.
- If the unavailable data is central to the bear thesis, do not issue a strong Sell solely because evidence is missing; explain the risk scenario and what would confirm it.
- If the same missing variable is central to both bull and bear cases, default to an evidence-limited Hold/watch-plan unless the verified financial, valuation, or cycle evidence already gives one side positive expected value.
- Hold should mean balanced verified evidence, not "we could not fetch the important data."

**Supply-Demand Fallback:**
- If micro product price, spread, inventory, or freight data is missing, ask whether macro supply-demand evidence can still say something useful.
- This fallback must be specific to the product or route: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Treat macro proxies as lower-confidence evidence than verified micro prices. They can shape scenarios and watch ranges, but should not be presented as exact product-price conclusions.
- If macro supply-demand evidence points clearly one way, do not default to Hold purely because product quotes are missing; instead state an evidence-limited directional view and what data would confirm or refute it.
- Do not let a bull or bear case use unverified exact wholesale prices, product prices, spreads, inventories, or date-specific market statistics as decisive facts. Keep them in an evidence-gap/watchlist bucket unless the source context labels them verified.

**Decision-Continuity Rules:**
- Reassess the company fully, but do not silently reverse a recent same-ticker stance.
- If the recommendation differs from the most recent same-ticker decision, explicitly identify the new decisive evidence, the core facts that remain unchanged, and why the prior stance is no longer preferred.
- A lower share price by itself is not a new fundamental fact. It may change valuation or trading posture, but it cannot alone justify a reversal across the neutral line.
- If there is no new decisive evidence, prefer preserving the prior directional stance while adjusting conviction, sizing, or watch levels.
- If a recent same-ticker decision is present and you are writing free text rather than structured fields, include explicit sections titled **Prior Rating**, **New Evidence Since Prior**, **Unchanged Core Facts**, and **Rating Change Audit**.
- If any verified theme matters to the thesis and you are writing free text rather than structured fields, include an explicit section titled **Thematic Valuation Bridge** that explains whether the theme belongs in core valuation, scenario valuation, SOTP/NAV, or only qualitative optionality.
- If you are writing free text rather than structured fields, include explicit sections titled **Company Quality Verdict**, **Current Odds Verdict**, and **Relative Allocation Verdict** so that business quality, today's risk/reward, and best deployment choice are not collapsed into one view.
- If you are writing free text rather than structured fields, also include **Management & Capital Allocation Verdict** and **Shareholder Structure Verdict** whenever the hard-signal contexts are available.
- If official investor-interaction context is available, keep an **Investor Communication Verdict** explicit enough for the downstream trader and risk team to understand the live concern map and disclosure quality.
- Keep an **Industry Cycle Verdict** explicit enough to state the current cycle stage before valuation: downturn, bottom-testing, bottom-right validation, early upcycle, mid-cycle expansion, peak/rollover, or evidence insufficient. Do not let company PE or one-quarter profit alone establish the cycle stage.
- Keep a **Business Model / Segment Economics Verdict** explicit enough to teach how the company makes money, which segments are mature core value, which are second-curve/scenario value, what moat is actually evidenced, and which segment disclosures are still missing.
- Keep an **Industry KPI Verdict** explicit enough to say which sector-native KPI layers are verified, partial, or missing, and whether those gaps change conviction, sizing, valuation, or the verification calendar.
- Keep a **Forward Forecast Model Verdict** explicit enough to connect the rating to a two-to-three-year revenue, margin, net profit/EPS, and cash-flow bridge. If the bridge is missing, do not allow target-price confidence to outrun the evidence.
- Keep a **Key Number Audit Verdict** explicit enough to police decisive PE/PB/EV multiples, target price, safety price, dividend yield, margins, ASP, shipments, utilization, backlog, and contract-liability claims. Require formula, period, source, and evidence status when those numbers drive the rating.
- If official policy context is available, keep a **Policy Direction Verdict** explicit enough to distinguish industry support from company-specific monetization.
- If historical price/EPS/PE decomposition context is available, keep the valuation-cycle verdict explicit enough to say whether the current price is supported by earnings improvement, multiple expansion, both, or neither.
- Preserve a concise standalone **Safety Price / Defensive Build Anchor** when financial state supports it; when writing Chinese, title it `## 安全价格区间 / 防御性建仓锚`. For value stocks, blue chips, banks, defensive dividend names, and mature cash-flow compounders, anchor it in normalized low-cycle EPS or FCF, sustainable dividend yield, book value/PB and ROE, cash conversion, leverage or net cash, asset quality, payout capacity, and peer/historical valuation floors. For commodity/resource/cyclical names, anchor it in cycle-trough or stress-case earnings, conservative product prices, unit-cost resilience, balance-sheet survival, maintenance capex, and normalized PE/PB floors. Include only the practical anchor: price band, valuation bridge, business conditions that must remain true, slow-build plan, and deterioration that invalidates it. Prefer one short paragraph or a compact 3-4 row table, not a second valuation essay. If the company is structurally impaired, highly leveraged, deeply cyclical without survivable trough economics, or evidence-thin, still keep the section and say no reliable safety price can be assigned.
- If industry-specific filing context is available, keep an **Industry Driver Verdict** explicit enough to preserve the real sector-native variables that decide the thesis.
- If the filing context contains **Growth Sustainability & Ramp Conditions**, keep a **Growth Sustainability Verdict** explicit enough to judge whether revenue/profit growth can continue or ramp further. Require the debate to separate verified drivers, inferred drivers, needed ramp conditions, and falsification signals before accepting any Buy/Underweight conclusion.
- If the filing context contains **Pre-Debate Underwriting Questions**, use them as the judging agenda. Decide which side better answered the company-specific business-model, moat, growth-driver, second-curve, cash-quality, segment-valuation, and risk questions. Populate the structured `question_led_debate_audit` field with a compact issue-log table covering question, initial skepticism, bull answer, bear attack, evidence verdict, valuation/sizing impact, and next verification. Do not let the final plan ignore an unanswered pre-debate question that is central to the rating.
- If the filing context contains a Business Segment Valuation Map or Segment Economics Pack, keep a **Business Segment Valuation Verdict** explicit enough to split mature core businesses from emerging second curves, geographies, and channels. Do not allow the debate to collapse a multi-business company into one blended PE unless the filings do not support a meaningful split.
- If the filing context contains Internal Filing Quality Modules, keep a **Filing Internal Quality Verdict** explicit enough to summarize accounting reconciliation, segment economics, footnotes, cash-flow quality, capex/CIP returns, MD&A text changes, non-recurring profit quality, balance-sheet leading signals, shareholder-return authenticity, and disclosure quality. Synthesize the material points; do not mechanically repeat all ten if some are immaterial.
- If commodity/product-price context is available, keep a **Commodity Cycle Verdict** explicit enough to say whether the product-price evidence supports or contradicts the margin/EPS/inventory part of the thesis.
- If price-move attribution context is available, keep a **Sharp Move Attribution Verdict** explicit enough to say whether a recent move is market-led, same-metal sector-led, cross-metal residual, mapped-commodity-led, stock-specific, failed-rebound/trend continuation, or possible emotion kill. Do not call a drop mispriced until valuation/NAV support and event checks pass.
- If relative-strength/index-linkage context is available, keep a **Relative Strength Verdict** explicit enough to decide whether the stock is stronger or weaker than its style index and same-industry basket, whether correlation/Beta suggest benchmark beta or company alpha, and how that changes timing, sizing, and thesis validation.
- If shipping/freight-rate context is available, keep a **Shipping Cycle Verdict** explicit enough to separate broad proxies (BDTI/BCTI/BDI/BCI/BPI) from route-level economics (VLCC TD3C/TCE/CTFI), and explicitly test two-sided Hormuz mechanisms: reopening can reduce risk premium and improve vessel turnover, while restocking, queue normalization, and renewed cargo flows can support near-term cargo demand. Missing route-level freight is a conviction cap, not automatically bearish evidence.
- If gated baijiu context says `Status: triggered`, keep a **Baijiu Channel Verification Verdict** explicit enough to separate product wholesale price evidence, channel inventory/payment quality, contract-liability seasonality, product mix, peer-basket comparison, and missing data. If it says `Status: not_applicable`, do not force baijiu analysis into the stock.
- If gated compute-leasing context says `Status: triggered`, keep a **Compute-Leasing Verification Verdict** explicit enough to separate legacy value, verified compute-leasing value, unverified compute optionality, unit-economics gaps, capex/funding risk, and transition credibility. If it says `Status: not_applicable`, do not force compute-leasing analysis into the stock.
- If gated dividend-defensive context says `Status: triggered`, keep a **Dividend Defensive Verdict** explicit enough to say whether this is a true defensive dividend candidate, a dividend-trap risk, or inferior to peer alternatives. If it says `Status: not_applicable`, do not force a high-dividend thesis into the stock.
- If gated building-materials context says `Status: triggered`, use it as a discipline layer: anchor first on company filings and management wording, then classify the industry stage and likely evolution path, and then cover product price/ASP, regional demand, property-completion/infrastructure/renovation exposure, capacity/utilization, upstream costs, inventory, receivables, cash collection, payout safety, and whether low PB/high dividend is real safety or a value trap. Add a dedicated **Building Materials Operating Cycle Verdict** only when it changes the rating, valuation, sizing, or action plan; otherwise integrate the relevant points into the main business/valuation/risk discussion. Treat repurchases and dividends as shareholder-return, safety-margin, and controlling-shareholder-attitude evidence, not as the whole thesis. If it says `Status: not_applicable`, do not force building-materials logic into the stock.
- If gated consumer-staples context says `Status: triggered`, keep a **Consumer Staples Verification Verdict** explicit enough to decide whether the thesis is category demand, channel restocking, cost pass-through, product-mix upgrade, prepared-dish optionality, dividend defensiveness, or merely valuation mean reversion. For frozen-food names such as Anjoy, explicitly test Spring Festival seasonality, distributor inventory, contract liabilities/advance receipts, inventory-to-revenue, raw-material cost proxies, promotion intensity, and Q2/Q3 margin follow-through. If it says `Status: not_applicable`, do not force food/beverage logic into the stock.
- If gated optical-module context says `Status: triggered`, keep an **AI Optical-Module Verification Verdict** explicit enough to decide whether the thesis is 800G share gain, 1.6T ramp, overseas cloud customer orders, product price/mix, exchange-rate tailwind, capacity/yield, AI capex durability, or merely valuation momentum. For Zhongji Innolight, Eoptolink, and similar names, explicitly test customer qualification, shipment mix, inventory/revenue, receivables/revenue, operating cash flow, gross margin, customer concentration, export/tariff risk, and CPO/LPO/silicon-photonics route risk. If it says `Status: not_applicable`, do not force optical-module or AI datacom logic into the stock.
- If gated biopharma context says `Status: triggered`, keep a **Biopharma Verification Verdict** explicit enough to separate commercialized products, label expansion, late-stage pipeline, early pipeline, regulatory review, reimbursement/pricing, BD economics, R&D spend, cash runway, and dilution risk. For CRO/CDMO/pharma-services names, separate order visibility, customer funding cycle, project conversion, capacity utilization, capex returns, geopolitical risk, and FCF durability from drug-owner pipeline logic. Clinical or regulatory missing data caps conviction and belongs in the research-gap section; it is not proof of either approval or failure.
- If gated software context says `Status: triggered`, keep a **Software Verification Verdict** explicit enough to classify the software model and separate subscription/ARR quality, paid users, ARPU, renewal/churn, contract-liability conversion, project acceptance, receivables/cash collection, AI paid adoption, and model-labeled peer valuation. If these metrics are missing, cap conviction rather than letting AI or broad software-service peer narratives carry the rating.
- If gated insurance context says `Status: triggered`, keep an **Insurance Verification Verdict** explicit enough to separate life/health NBV and EV, channel quality, solvency, investment-yield spread, P&C COR, bank-subsidiary contribution, dividends, and SOTP optionality. If it says `Status: not_applicable`, do not force insurance analysis into the stock.
- If gated medical-device context says `Status: triggered`, keep a **Medical Device Verification Verdict** explicit enough to separate equipment installed base/replacement cycle, IVD analyzer plus reagent pull-through, consumables/procedure volume, VBP/procurement price pressure, registration/overseas channel quality, receivables/cash conversion, and product-mix/gross-margin durability. If it says `Status: not_applicable`, do not force medical-device analysis into the stock.
- If gated metals/mining context says `Status: triggered`, keep a **Metals / Mining Verification Verdict** explicit enough to separate exchange price proxies, realized selling price, reserve/resource quality, grade, equity production, AISC/unit cost, smelting/trading split, hedging/inventory, project capex/ramp, jurisdiction risk, balance-sheet survival, and NAV/SOTP. If it says `Status: not_applicable`, do not force metals/mining analysis into the stock.
- If verified but non-base-case optionality matters, keep a **Strategic Optionality Verdict** explicit enough that downstream agents do not erase a second growth curve, investee holding, asset revaluation path, or live thematic catalyst merely because it does not flip today's rating.
- If the thematic valuation bridge contains material `asset-revaluation` or primary-investment holdings, build an explicit **Primary Investment NAV Verdict**. Separate operating earnings from investee/NAV value; use conservative/base/upside values with liquidity, lock-up, exit-probability, and double-counting haircuts. Do not collapse verified non-listed equity holdings into a vague "small imagination premium" when ownership value, materiality, and an IPO/exit path are disclosed.
- Always read the Data Coverage Audit before ruling. If a module is failed, missing, or partial and touches the core bet, explicitly state the gap and cap conviction; do not let the final plan sound more certain than the data coverage allows.
- If financial-report intelligence says narrative filing text or readable report body was unavailable, do not write that the system failed to retrieve all financial data. First check whether structured statements, market data, peer comparison, valuation, and earnings-model contexts are present. Describe the gap narrowly as missing report-body/segment/management-discussion evidence unless those other modules also failed.

---

{continuity_context}
**Thematic Catalyst Cross-Check And Valuation Bridge:**
{thematic_catalyst_context}

**Industry Cycle Scan:**
{industry_cycle_context}

**Company Business Model Primer:**
{company_business_model_context}

**Industry KPI Checklist:**
{industry_kpi_context}

**Forward Forecast Model Scaffold:**
{forecast_model_context}

**Sell-Side Depth And Key-Number Audit:**
{quality_audit_context}

**Commodity/Product-Price Context:**
{commodity_context}

**Price-Move Attribution Context:**
{price_move_attribution_context}

**Relative-Strength / Index-Linkage Context:**
{relative_strength_context}

**Shipping/Freight-Rate Context:**
{shipping_context}

**Financial-Report Intelligence:**
{filing_intelligence_context}

**Same-Industry Peer Comparison:**
{peer_comparison_context}

**Cross-Position Supply-Chain Comparison:**
{supply_chain_comparison_context}

**Earnings-Model Context:**
{earnings_model_context}

**Market-Expectation Context:**
{market_expectation_context}

**Historical Price-EPS-PE Decomposition Context:**
{price_earnings_decomposition_context}

**Management/Capital-Allocation Context:**
{management_capital_allocation_context}

**Shareholder-Structure Context:**
{shareholder_structure_context}

**Official Investor-Interaction Context:**
{investor_interaction_context}

**Official Policy-Planning Context:**
{policy_planning_context}

**Web Fact-Check Context:**
{web_fact_check_context}

**Gated Baijiu Verification Context:**
{baijiu_context}

**Gated Compute-Leasing Verification Context:**
{compute_leasing_context}

**Gated Dividend Defensive Verification Context:**
{dividend_defensive_context}

**Gated Building-Materials Verification Context:**
{building_materials_context}

**Gated Consumer-Staples Verification Context:**
{consumer_staples_context}

**Gated AI Optical-Module Verification Context:**
{optical_module_context}

**Gated Biopharma Verification Context:**
{biopharma_context}

**Gated Software Verification Context:**
{software_context}

**Gated Insurance Verification Context:**
{insurance_context}

**Gated Medical-Device Verification Context:**
{medical_device_context}

**Gated Metals/Mining Verification Context:**
{metals_mining_context}

**Data Coverage Audit:**
{data_coverage_context}

**Debate History:**
{prompt_history}

{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_buy_side_underwriting_modules_instruction()}
{get_material_catalyst_instruction()}
{get_thematic_valuation_instruction()}
{get_filing_intelligence_instruction()}
{get_question_led_debate_instruction()}
{get_insurance_instruction()}
{get_medical_device_instruction()}
{get_metals_mining_instruction()}
{get_price_move_attribution_instruction()}
{get_peer_selection_instruction()}
{get_supply_chain_selection_instruction()}
{get_earnings_model_instruction()}
{get_market_expectation_instruction()}
{get_price_earnings_decomposition_instruction()}
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
{get_consumer_staples_instruction()}
{get_optical_module_instruction()}
{get_biopharma_instruction()}
{get_software_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_focused_report_instruction()}
If a bull or bear argument contains an exact product price, inventory figure, product spread, percentage change, or date-specific market claim that is not supported by the analyst reports or corroborated web fact-check context, downgrade that argument and list it as an unverified key assumption."""

        investment_plan = invoke_structured_or_freetext(
            structured_llm,
            llm,
            prompt,
            render_research_plan,
            "Research Manager",
        )

        new_investment_debate_state = {
            "judge_decision": investment_plan,
            "history": investment_debate_state.get("history", ""),
            "bear_history": investment_debate_state.get("bear_history", ""),
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": investment_plan,
            "count": investment_debate_state["count"],
        }

        return {
            "investment_debate_state": new_investment_debate_state,
            "investment_plan": investment_plan,
        }

    return research_manager_node
