from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_balance_sheet,
    get_buy_side_accounting_radar_instruction,
    get_buy_side_thesis_instruction,
    get_company_depth_contract_instruction,
    get_commodity_context,
    get_compute_leasing_context,
    get_compute_leasing_instruction,
    get_consumer_staples_context,
    get_consumer_staples_instruction,
    get_dividend_defensive_context,
    get_dividend_defensive_instruction,
    get_earnings_model_context,
    get_earnings_model_instruction,
    get_evidence_instruction,
    get_cashflow,
    get_derived_financial_metric_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_fundamentals,
    get_financial_report_intelligence_context,
    get_income_statement,
    get_insurance_context,
    get_insurance_instruction,
    get_intraday_behavior_context,
    get_investor_interaction_context,
    get_investor_interaction_instruction,
    get_medical_device_context,
    get_medical_device_instruction,
    get_metals_mining_context,
    get_metals_mining_instruction,
    get_optical_module_context,
    get_optical_module_instruction,
    get_price_move_attribution_context,
    get_price_move_attribution_instruction,
    get_insider_transactions,
    get_knowledge_planet_context,
    get_knowledge_planet_instruction,
    get_language_instruction,
    get_material_catalyst_instruction,
    get_market_sector_risk,
    get_market_expectation_context,
    get_market_expectation_instruction,
    get_market_timing_context,
    get_relative_strength_context,
    get_management_capital_allocation_context,
    get_management_capital_allocation_instruction,
    get_baijiu_context,
    get_baijiu_instruction,
    get_biopharma_context,
    get_biopharma_instruction,
    get_building_materials_context,
    get_building_materials_instruction,
    get_software_context,
    get_software_instruction,
    get_policy_planning_context,
    get_policy_planning_instruction,
    get_peer_comparison,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_context,
    get_price_earnings_decomposition_instruction,
    get_research_gap_instruction,
    get_shipping_context,
    get_shareholder_structure_context,
    get_shareholder_structure_instruction,
    get_supply_chain_comparison,
    get_supply_chain_selection_instruction,
    get_three_layer_conclusion_instruction,
    get_supply_demand_fallback_instruction,
    get_thematic_catalyst_context,
    get_valuation_percentiles,
    get_web_fact_check_context,
    get_web_fact_check_instruction,
)
from tradingagents.dataflows.tushare_a_stock import is_a_share_symbol
from tradingagents.dataflows.config import get_config
from tradingagents.dataflows.prompt_compaction import compact_state_fields
from tradingagents.dataflows.structured_research import compact_structured_research_for_prompt


def create_fundamentals_analyst(llm):
    def fundamentals_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])
        raw_thematic_catalyst_context = state.get("thematic_catalyst_context", "")
        raw_commodity_context = state.get("commodity_context", "")
        raw_price_move_attribution_context = state.get("price_move_attribution_context", "")
        raw_intraday_behavior_context = state.get("intraday_behavior_context", "")
        raw_relative_strength_context = state.get("relative_strength_context", "")
        raw_filing_intelligence_context = state.get("filing_intelligence_context", "")
        raw_peer_comparison_context = state.get("peer_comparison_context", "")
        raw_supply_chain_comparison_context = state.get("supply_chain_comparison_context", "")
        raw_earnings_model_context = state.get("earnings_model_context", "")
        raw_market_expectation_context = state.get("market_expectation_context", "")
        raw_price_earnings_decomposition_context = state.get("price_earnings_decomposition_context", "")
        raw_management_capital_allocation_context = state.get("management_capital_allocation_context", "")
        raw_shareholder_structure_context = state.get("shareholder_structure_context", "")
        raw_investor_interaction_context = state.get("investor_interaction_context", "")
        raw_policy_planning_context = state.get("policy_planning_context", "")
        raw_shipping_context = state.get("shipping_context", "")
        raw_web_fact_check_context = state.get("web_fact_check_context", "")
        raw_knowledge_planet_context = state.get("knowledge_planet_context", "")
        raw_baijiu_context = state.get("baijiu_context", "")
        raw_compute_leasing_context = state.get("compute_leasing_context", "")
        raw_dividend_defensive_context = state.get("dividend_defensive_context", "")
        raw_building_materials_context = state.get("building_materials_context", "")
        raw_consumer_staples_context = state.get("consumer_staples_context", "")
        raw_optical_module_context = state.get("optical_module_context", "")
        raw_biopharma_context = state.get("biopharma_context", "")
        raw_software_context = state.get("software_context", "")
        raw_insurance_context = state.get("insurance_context", "")
        raw_medical_device_context = state.get("medical_device_context", "")
        raw_metals_mining_context = state.get("metals_mining_context", "")
        raw_industry_cycle_context = state.get("industry_cycle_context", "")
        raw_company_business_model_context = state.get("company_business_model_context", "")
        raw_industry_kpi_context = state.get("industry_kpi_context", "")
        raw_forecast_model_context = state.get("forecast_model_context", "")
        raw_quality_audit_context = state.get("quality_audit_context", "")
        raw_thesis_question_context = state.get("thesis_question_context", "")
        prompt_contexts = compact_state_fields(state, profile="analyst")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        price_move_attribution_context = prompt_contexts["price_move_attribution_context"]
        intraday_behavior_context = prompt_contexts["intraday_behavior_context"]
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
        data_coverage_context = prompt_contexts["data_coverage_context"]
        structured_research_context = compact_structured_research_for_prompt(
            state.get("structured_research_context", {}),
        )
        is_a_share = is_a_share_symbol(state["company_of_interest"])

        tools = [
            get_fundamentals,
            get_balance_sheet,
            get_cashflow,
            get_income_statement,
            get_valuation_percentiles,
            get_market_sector_risk,
            get_market_timing_context,
        ]
        if is_a_share and not raw_commodity_context:
            tools.append(get_commodity_context)
        if is_a_share and not raw_price_move_attribution_context:
            tools.append(get_price_move_attribution_context)
        if is_a_share and not raw_intraday_behavior_context:
            tools.append(get_intraday_behavior_context)
        if is_a_share and not raw_relative_strength_context:
            tools.append(get_relative_strength_context)
        if is_a_share and not raw_shipping_context:
            tools.append(get_shipping_context)
        if not raw_peer_comparison_context:
            tools.append(get_peer_comparison)
        if not raw_supply_chain_comparison_context:
            tools.append(get_supply_chain_comparison)
        if not raw_thematic_catalyst_context:
            tools.append(get_thematic_catalyst_context)
        if not raw_filing_intelligence_context:
            tools.append(get_financial_report_intelligence_context)
        if not raw_earnings_model_context:
            tools.append(get_earnings_model_context)
        if not raw_market_expectation_context:
            tools.append(get_market_expectation_context)
        if not raw_price_earnings_decomposition_context:
            tools.append(get_price_earnings_decomposition_context)
        if not raw_management_capital_allocation_context:
            tools.append(get_management_capital_allocation_context)
        if not raw_shareholder_structure_context:
            tools.append(get_shareholder_structure_context)
        if is_a_share and not raw_investor_interaction_context:
            tools.append(get_investor_interaction_context)
        if is_a_share and not raw_policy_planning_context:
            tools.append(get_policy_planning_context)
        if is_a_share and not raw_web_fact_check_context:
            tools.append(get_web_fact_check_context)
        if is_a_share and not raw_knowledge_planet_context:
            tools.append(get_knowledge_planet_context)
        if is_a_share and not raw_baijiu_context:
            tools.append(get_baijiu_context)
        if is_a_share and not raw_compute_leasing_context:
            tools.append(get_compute_leasing_context)
        if is_a_share and not raw_dividend_defensive_context:
            tools.append(get_dividend_defensive_context)
        if is_a_share and not raw_building_materials_context:
            tools.append(get_building_materials_context)
        if is_a_share and not raw_consumer_staples_context:
            tools.append(get_consumer_staples_context)
        if is_a_share and not raw_optical_module_context:
            tools.append(get_optical_module_context)
        if is_a_share and not raw_biopharma_context:
            tools.append(get_biopharma_context)
        if is_a_share and not raw_software_context:
            tools.append(get_software_context)
        if is_a_share and not raw_insurance_context:
            tools.append(get_insurance_context)
        if is_a_share and not raw_medical_device_context:
            tools.append(get_medical_device_context)
        if is_a_share and not raw_metals_mining_context:
            tools.append(get_metals_mining_context)

        system_message = (
            "You are a buy-side fundamental researcher. Write a focused investment memo, not an exhaustive data dump. "
            "Focused does not mean short or conclusion-first. The memo's main purpose is to make a knowledgeable reader understand how this specific company operates before discussing valuation or action. Prefer four to six thick analytical sections, and complete each material claim through evidence, operating mechanism, financial transmission, counterevidence and verification. Do not spend more space on rating/action language than on company economics and the three-year model. "
            "Your job is to identify the tradable thesis, test whether the business-cycle or boom-bust expectation can plausibly realize, and explain what evidence supports or weakens the thesis. "
            "Use `get_fundamentals`, `get_balance_sheet`, `get_cashflow`, and `get_income_statement` for core financial quality. "
            "Pay special attention to accounting items that may preview future performance, including contract liabilities, advance receipts, contract assets, receivables, inventories, prepayments, payables, goodwill, net cash, and working capital. "
            "For A-share tickers, the system may provide precomputed industry-cycle scan, company business-model primer, thesis-question context, thematic, commodity/product-price, price-move attribution, intraday minute-line behavior, relative-strength/index-linkage, shipping/freight-rate, filing, peer, supply-chain, earnings-model, market-expectation, price/EPS/PE decomposition, management/capital-allocation, shareholder-structure, investor-interaction, policy-planning, web fact-check, gated compute-leasing, gated dividend-defensive, gated building-materials, gated consumer-staples, gated optical-module/AI datacom, gated biopharma, gated software, gated insurance, gated medical-device, and gated metals/mining context below. Use any precomputed context directly and do not call the same context tool again. Also use `get_valuation_percentiles` for historical valuation zones, `get_market_sector_risk` for broad/sector risk, `get_market_timing_context` for market mood, and `get_relative_strength_context` / `get_intraday_behavior_context` for stock-versus-index and minute-line validation when those extra lenses are material. "
            "For commodity/resource/cyclical companies, treat the commodity/product-price context as a hard cycle variable: connect it to ASP, gross margin, inventory write-down/reversal risk, cash conversion, and valuation, and do not let news headlines substitute for product-price evidence. "
            "For shipping companies, treat shipping/freight-rate context as the hard cycle variable: separate route-level VLCC TD3C/TCE/CTFI evidence from broad BDTI/BCTI/BDI proxies, and explicitly test two-sided Hormuz mechanisms such as risk-premium compression versus restocking and ton-mile recovery. "
            "For A-share tickers, also use `get_supply_chain_comparison` when a curated chain map exists, so the memo can distinguish between a merely good company and the best profit pool in the chain. "
            "For A-share tickers, if precomputed thematic and financial-report intelligence are present below, treat those as satisfying the catalyst / filing-evidence requirement. If they are absent, call the corresponding context tool once before concluding those sections. "
            "Before forming the thesis, read the filing context in industry order: first identify the sector-native variables that actually decide economics, then inspect the paragraph-level filing evidence around those variables, and only then synthesize generic financial metrics. "
            "Before using words such as `cycle bottom`, `周期底部`, `cycle reversal`, or `景气反转`, first cite the Industry Cycle Scan and say whether the evidence is confirmed, bottom-right validation, bottom-testing, downcycle, or insufficient. "
            "For an unfamiliar company, first explain its disclosed main businesses from the Company Business Model Primer and financial reports, then use the Business Segment Valuation Map / Segment Economics Pack to split mature core businesses, new second-curve businesses, geographies, and channels before discussing valuation. Do not apply one blended PE multiple until you have explained why split valuation is unnecessary. "
            "The Structured Research Bundle contains a shared `underwriting_packet`. Treat its company model, segment driver chains, company-specific questions, forecast lines and evidence-change rules as the common analytical workbench used by every downstream agent. Your job is to deepen and correct that model, not write an independent narrative. Organize the memo around how the company works, material segment causal chains, the three-year model and unresolved questions. End with a compact `Shared Model Update Ledger` showing forecast/question line, old assumption, new evidence, new assumption, EPS/FCF/value effect, and unchanged/rejected items. "
            "Use the Industry KPI Checklist as the sector-native evidence agenda: state which KPI layers are verified, partial, or missing, and do not turn a missing KPI into a hard positive or negative fact. "
            "Use the Forward Forecast Model Scaffold to produce three explicit forward years (or four forward quarters) connecting segment drivers to the model-profile-appropriate consolidated earnings, cash/capital, asset-quality and per-share lines. Use revenue/margin/net profit/EPS/OCF/capex/FCF for ordinary companies, but bank-, insurance-, securities- or REIT-native drivers for financial/property vehicles. If assumptions are missing, put `missing/not disclosed` in the affected cell, name the required input, and label valuation confidence evidence-limited; a one-year profit range is not a completed forecast bridge. "
            "Use the Sell-Side Depth And Key-Number Audit to police decisive numbers: PE/PB/EV multiples, target price, safety price, dividend yield, margins, ASP, shipments, utilization, backlog, and contract liabilities need formula, source period, and evidence status. "
            "Use the Thesis Question Context as the memo's interrogation agenda: answer the company-specific soul questions before broad positives or negatives, and make unanswered thesis-critical questions explicit research gaps. "
            "Use Knowledge Planet stream/PDF intelligence through the Single-Stock Knowledge Fusion Pack first: label private/proxy clues, separate industry data from promotion, map PDF assumptions into sector-native KPIs, and cross-check them against filings, Tushare financials, peers, price/volume, and official announcements before they affect valuation or rating. Cite each used clue by KPE id and give one auditable result: numeric assumption old->new, probability triplet before->after, unchanged/watch with verification gate, or rejected with reason. "
            "For multi-business companies, complete a segment prosperity matrix before assigning a consolidated label. Show each material segment's same-period revenue weight, growth, margin and margin change, then explain demand -> supply/capacity -> ASP/volume -> utilization/mix -> margin -> working capital/cash -> EPS/FCF. Never call a segment fastest-growing without comparing all disclosed segments for the same period. "
            "Keep period and per-share arithmetic explicit: H1 is cumulative Q1+Q2; Q2 single-quarter and H1 thresholds need different labels. Reconcile BVPS=current price/PB, EPS=parent profit/diluted shares, and price=EPSxPE or BVPSxPB before publishing a safety/target price; otherwise withhold the range. "
            "Prioritize: Core Bet, key supporting evidence, key negative evidence, earnings bridge, market-implied expectation, expectation gap, probability/payoff, company quality, current odds, relative allocation, catalysts, falsification signals, and data gaps. "
            "If another peer looks better than the target, explain why with metrics and caveats. If the sector looks high-risk while the target looks relatively low, discuss whether this is a mispricing opportunity or a company-specific warning. "
            "Do not mechanically upgrade in bull markets or downgrade in bear markets: explain how market mood interacts with the company's valuation, quality, beta, cyclicality, balance sheet, and catalysts. "
            "Append a compact Markdown table only for the most decision-relevant points."
            + get_evidence_instruction()
            + get_research_gap_instruction()
            + get_supply_demand_fallback_instruction()
            + get_derived_financial_metric_instruction()
            + get_buy_side_accounting_radar_instruction()
            + get_buy_side_thesis_instruction()
            + get_company_depth_contract_instruction()
            + get_material_catalyst_instruction()
            + get_filing_intelligence_instruction()
            + get_peer_selection_instruction()
            + get_supply_chain_selection_instruction()
            + get_earnings_model_instruction()
            + get_market_expectation_instruction()
            + get_price_earnings_decomposition_instruction()
            + get_three_layer_conclusion_instruction()
            + get_management_capital_allocation_instruction()
            + get_shareholder_structure_instruction()
            + get_investor_interaction_instruction()
            + get_policy_planning_instruction()
            + get_web_fact_check_instruction()
            + get_knowledge_planet_instruction()
            + get_baijiu_instruction()
            + get_compute_leasing_instruction()
            + get_dividend_defensive_instruction()
            + get_building_materials_instruction()
            + get_consumer_staples_instruction()
            + get_optical_module_instruction()
            + get_biopharma_instruction()
            + get_software_instruction()
            + get_insurance_instruction()
            + get_medical_device_instruction()
            + get_metals_mining_instruction()
            + get_price_move_attribution_instruction()
            + (
                "\n\nPrecomputed industry-cycle scan:\n"
                + industry_cycle_context
                if industry_cycle_context
                else ""
            )
            + (
                "\n\nPrecomputed company business-model primer:\n"
                + company_business_model_context
                if company_business_model_context
                else ""
            )
            + (
                "\n\nStructured research bundle (JSON source of record):\n"
                + structured_research_context
                if structured_research_context != "{}"
                else ""
            )
            + (
                "\n\nPrecomputed industry KPI checklist:\n"
                + industry_kpi_context
                if industry_kpi_context
                else ""
            )
            + (
                "\n\nPrecomputed forward forecast-model scaffold:\n"
                + forecast_model_context
                if forecast_model_context
                else ""
            )
            + (
                "\n\nPrecomputed sell-side depth and key-number audit:\n"
                + quality_audit_context
                if quality_audit_context
                else ""
            )
            + (
                "\n\nPrecomputed thesis-question context:\n"
                + thesis_question_context
                if thesis_question_context
                else ""
            )
            + (
                "\n\nPrecomputed filing/news thematic cross-check:\n"
                + thematic_catalyst_context
                if thematic_catalyst_context
                else ""
            )
            + (
                "\n\nPrecomputed commodity/product-price context:\n"
                + commodity_context
                if commodity_context
                else ""
            )
            + (
                "\n\nPrecomputed price-move attribution context:\n"
                + price_move_attribution_context
                if price_move_attribution_context
                else ""
            )
            + (
                "\n\nPrecomputed intraday minute-line behavior context:\n"
                + intraday_behavior_context
                if intraday_behavior_context
                else ""
            )
            + (
                "\n\nPrecomputed relative-strength / index-linkage context:\n"
                + relative_strength_context
                if relative_strength_context
                else ""
            )
            + (
                "\n\nPrecomputed shipping/freight-rate context:\n"
                + shipping_context
                if shipping_context
                else ""
            )
            + (
                "\n\nPrecomputed financial-report intelligence:\n"
                + filing_intelligence_context
                if filing_intelligence_context
                else ""
            )
            + (
                "\n\nPrecomputed same-industry peer comparison:\n"
                + peer_comparison_context
                if peer_comparison_context
                else ""
            )
            + (
                "\n\nPrecomputed cross-position supply-chain comparison:\n"
                + supply_chain_comparison_context
                if supply_chain_comparison_context
                else ""
            )
            + (
                "\n\nPrecomputed earnings-model context:\n"
                + earnings_model_context
                if earnings_model_context
                else ""
            )
            + (
                "\n\nPrecomputed market-expectation context:\n"
                + market_expectation_context
                if market_expectation_context
                else ""
            )
            + (
                "\n\nPrecomputed historical price-EPS-PE decomposition context:\n"
                + price_earnings_decomposition_context
                if price_earnings_decomposition_context
                else ""
            )
            + (
                "\n\nPrecomputed management/capital-allocation context:\n"
                + management_capital_allocation_context
                if management_capital_allocation_context
                else ""
            )
            + (
                "\n\nPrecomputed shareholder-structure context:\n"
                + shareholder_structure_context
                if shareholder_structure_context
                else ""
            )
            + (
                "\n\nPrecomputed official investor-interaction context:\n"
                + investor_interaction_context
                if investor_interaction_context
                else ""
            )
            + (
                "\n\nPrecomputed official policy-planning context:\n"
                + policy_planning_context
                if policy_planning_context
                else ""
            )
            + (
                "\n\nPrecomputed web fact-check context:\n"
                + web_fact_check_context
                if web_fact_check_context
                else ""
            )
            + (
                "\n\nPrecomputed Knowledge Planet stream/PDF intelligence:\n"
                + knowledge_planet_context
                if knowledge_planet_context
                else ""
            )
            + (
                "\n\nPrecomputed gated baijiu verification context:\n"
                + baijiu_context
                if baijiu_context
                else ""
            )
            + (
                "\n\nPrecomputed gated compute-leasing verification context:\n"
                + compute_leasing_context
                if compute_leasing_context
                else ""
            )
            + (
                "\n\nPrecomputed gated dividend defensive verification context:\n"
                + dividend_defensive_context
                if dividend_defensive_context
                else ""
            )
            + (
                "\n\nPrecomputed gated building-materials verification context:\n"
                + building_materials_context
                if building_materials_context
                else ""
            )
            + (
                "\n\nPrecomputed gated consumer-staples verification context:\n"
                + consumer_staples_context
                if consumer_staples_context
                else ""
            )
            + (
                "\n\nPrecomputed gated AI optical-module verification context:\n"
                + optical_module_context
                if optical_module_context
                else ""
            )
            + (
                "\n\nPrecomputed gated biopharma verification context:\n"
                + biopharma_context
                if biopharma_context
                else ""
            )
            + (
                "\n\nPrecomputed gated software verification context:\n"
                + software_context
                if software_context
                else ""
            )
            + (
                "\n\nPrecomputed gated insurance verification context:\n"
                + insurance_context
                if insurance_context
                else ""
            )
            + (
                "\n\nPrecomputed gated medical-device verification context:\n"
                + medical_device_context
                if medical_device_context
                else ""
            )
            + (
                "\n\nPrecomputed gated metals/mining verification context:\n"
                + metals_mining_context
                if metals_mining_context
                else ""
            )
            + (
                "\n\nPrecomputed data coverage audit:\n"
                + data_coverage_context
                if data_coverage_context
                else ""
            )
            + get_fair_cycle_valuation_instruction()
            + get_focused_report_instruction()
            + get_language_instruction(),
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you are unable to fully answer, that's OK; another assistant with different tools"
                    " will help where you left off. Execute what you can to make progress."
                    " Your deliverable is an analyst memo only. Do not issue FINAL TRANSACTION PROPOSAL lines;"
                    " final trading actions are produced later by the Trader and Portfolio Manager."
                    " You have access to the following tools: {tool_names}.\n{system_message}"
                    "For your reference, the current date is {current_date}. {instrument_context}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(instrument_context=instrument_context)

        chain = prompt | llm.bind_tools(tools)

        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "fundamentals_report": report,
        }

    return fundamentals_analyst_node
