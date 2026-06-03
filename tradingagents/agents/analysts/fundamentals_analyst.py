from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_balance_sheet,
    get_buy_side_accounting_radar_instruction,
    get_buy_side_thesis_instruction,
    get_commodity_context,
    get_compute_leasing_context,
    get_compute_leasing_instruction,
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
    get_insider_transactions,
    get_language_instruction,
    get_material_catalyst_instruction,
    get_market_sector_risk,
    get_market_expectation_context,
    get_market_expectation_instruction,
    get_market_timing_context,
    get_management_capital_allocation_context,
    get_management_capital_allocation_instruction,
    get_baijiu_context,
    get_baijiu_instruction,
    get_building_materials_context,
    get_building_materials_instruction,
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


def create_fundamentals_analyst(llm):
    def fundamentals_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])
        raw_thematic_catalyst_context = state.get("thematic_catalyst_context", "")
        raw_commodity_context = state.get("commodity_context", "")
        raw_filing_intelligence_context = state.get("filing_intelligence_context", "")
        raw_peer_comparison_context = state.get("peer_comparison_context", "")
        raw_supply_chain_comparison_context = state.get("supply_chain_comparison_context", "")
        raw_earnings_model_context = state.get("earnings_model_context", "")
        raw_market_expectation_context = state.get("market_expectation_context", "")
        raw_price_earnings_decomposition_context = state.get("price_earnings_decomposition_context", "")
        raw_management_capital_allocation_context = state.get("management_capital_allocation_context", "")
        raw_shareholder_structure_context = state.get("shareholder_structure_context", "")
        raw_shipping_context = state.get("shipping_context", "")
        raw_web_fact_check_context = state.get("web_fact_check_context", "")
        raw_baijiu_context = state.get("baijiu_context", "")
        raw_compute_leasing_context = state.get("compute_leasing_context", "")
        raw_dividend_defensive_context = state.get("dividend_defensive_context", "")
        raw_building_materials_context = state.get("building_materials_context", "")
        prompt_contexts = compact_state_fields(state, profile="analyst")
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
        web_fact_check_context = prompt_contexts["web_fact_check_context"]
        baijiu_context = prompt_contexts["baijiu_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
        building_materials_context = prompt_contexts["building_materials_context"]
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
        if is_a_share and not raw_web_fact_check_context:
            tools.append(get_web_fact_check_context)
        if is_a_share and not raw_baijiu_context:
            tools.append(get_baijiu_context)
        if is_a_share and not raw_compute_leasing_context:
            tools.append(get_compute_leasing_context)
        if is_a_share and not raw_dividend_defensive_context:
            tools.append(get_dividend_defensive_context)
        if is_a_share and not raw_building_materials_context:
            tools.append(get_building_materials_context)

        system_message = (
            "You are a buy-side fundamental researcher. Write a focused investment memo, not an exhaustive data dump. "
            "Your job is to identify the tradable thesis, test whether the business-cycle or boom-bust expectation can plausibly realize, and explain what evidence supports or weakens the thesis. "
            "Use `get_fundamentals`, `get_balance_sheet`, `get_cashflow`, and `get_income_statement` for core financial quality. "
            "Pay special attention to accounting items that may preview future performance, including contract liabilities, advance receipts, contract assets, receivables, inventories, prepayments, payables, goodwill, net cash, and working capital. "
            "For A-share tickers, the system may provide precomputed thematic, commodity/product-price, shipping/freight-rate, filing, peer, supply-chain, earnings-model, market-expectation, price/EPS/PE decomposition, management/capital-allocation, shareholder-structure, web fact-check, gated compute-leasing, gated dividend-defensive, and gated building-materials context below. Use any precomputed context directly and do not call the same context tool again. Also use `get_valuation_percentiles` for historical valuation zones, `get_market_sector_risk` for broad/sector risk, and `get_market_timing_context` for market mood when those extra lenses are material. "
            "For commodity/resource/cyclical companies, treat the commodity/product-price context as a hard cycle variable: connect it to ASP, gross margin, inventory write-down/reversal risk, cash conversion, and valuation, and do not let news headlines substitute for product-price evidence. "
            "For shipping companies, treat shipping/freight-rate context as the hard cycle variable: separate route-level VLCC TD3C/TCE/CTFI evidence from broad BDTI/BCTI/BDI proxies, and explicitly test two-sided Hormuz mechanisms such as risk-premium compression versus restocking and ton-mile recovery. "
            "For A-share tickers, also use `get_supply_chain_comparison` when a curated chain map exists, so the memo can distinguish between a merely good company and the best profit pool in the chain. "
            "For A-share tickers, if precomputed thematic and financial-report intelligence are present below, treat those as satisfying the catalyst / filing-evidence requirement. If they are absent, call the corresponding context tool once before concluding those sections. "
            "Before forming the thesis, read the filing context in industry order: first identify the sector-native variables that actually decide economics, then inspect the paragraph-level filing evidence around those variables, and only then synthesize generic financial metrics. "
            "For an unfamiliar company, first explain its disclosed main businesses from financial reports, then use the Business Segment Valuation Map / Segment Economics Pack to split mature core businesses, new second-curve businesses, geographies, and channels before discussing valuation. Do not apply one blended PE multiple until you have explained why split valuation is unnecessary. "
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
            + get_web_fact_check_instruction()
            + get_baijiu_instruction()
            + get_compute_leasing_instruction()
            + get_dividend_defensive_instruction()
            + get_building_materials_instruction()
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
                "\n\nPrecomputed web fact-check context:\n"
                + web_fact_check_context
                if web_fact_check_context
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
