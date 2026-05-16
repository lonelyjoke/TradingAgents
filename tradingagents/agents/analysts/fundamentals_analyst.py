from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_balance_sheet,
    get_buy_side_accounting_radar_instruction,
    get_buy_side_thesis_instruction,
    get_commodity_context,
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
    get_peer_comparison,
    get_peer_selection_instruction,
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
)
from tradingagents.dataflows.config import get_config


def create_fundamentals_analyst(llm):
    def fundamentals_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])
        thematic_catalyst_context = state.get("thematic_catalyst_context", "")
        filing_intelligence_context = state.get("filing_intelligence_context", "")
        peer_comparison_context = state.get("peer_comparison_context", "")
        supply_chain_comparison_context = state.get("supply_chain_comparison_context", "")
        earnings_model_context = state.get("earnings_model_context", "")
        market_expectation_context = state.get("market_expectation_context", "")
        management_capital_allocation_context = state.get("management_capital_allocation_context", "")
        shareholder_structure_context = state.get("shareholder_structure_context", "")

        tools = [
            get_fundamentals,
            get_balance_sheet,
            get_cashflow,
            get_income_statement,
            get_commodity_context,
            get_shipping_context,
            get_peer_comparison,
            get_supply_chain_comparison,
            get_valuation_percentiles,
            get_market_sector_risk,
            get_market_timing_context,
            get_thematic_catalyst_context,
            get_financial_report_intelligence_context,
            get_earnings_model_context,
            get_market_expectation_context,
            get_management_capital_allocation_context,
            get_shareholder_structure_context,
        ]

        system_message = (
            "You are a buy-side fundamental researcher. Write a focused investment memo, not an exhaustive data dump. "
            "Your job is to identify the tradable thesis, test whether the business-cycle or boom-bust expectation can plausibly realize, and explain what evidence supports or weakens the thesis. "
            "Use `get_fundamentals`, `get_balance_sheet`, `get_cashflow`, and `get_income_statement` for core financial quality. "
            "Pay special attention to accounting items that may preview future performance, including contract liabilities, advance receipts, contract assets, receivables, inventories, prepayments, payables, goodwill, net cash, and working capital. "
            "For A-share tickers, also use `get_commodity_context` for product/futures exposure, `get_shipping_context` for freight-cycle exposure, `get_peer_comparison` for same-industry alternatives, `get_valuation_percentiles` for historical valuation zones, `get_market_sector_risk` for broad/sector risk, `get_market_timing_context` for market mood, `get_thematic_catalyst_context` to cross-check filing-origin themes against news and news-origin themes against filing text, `get_financial_report_intelligence_context` to mine operating evidence buried inside annual/half-year reports, `get_earnings_model_context` to anchor the thesis in an earnings bridge, `get_market_expectation_context` to read what the current quote already implies, `get_management_capital_allocation_context` to assess stewardship and capital deployment, and `get_shareholder_structure_context` to inspect ownership concentration, insider activity, pledge, and unlock risk. "
            "For A-share tickers, also use `get_supply_chain_comparison` when a curated chain map exists, so the memo can distinguish between a merely good company and the best profit pool in the chain. "
            "For A-share tickers, call `get_thematic_catalyst_context` and `get_financial_report_intelligence_context` at least once before concluding the catalyst / filing-evidence sections. "
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
            + get_three_layer_conclusion_instruction()
            + get_management_capital_allocation_instruction()
            + get_shareholder_structure_instruction()
            + (
                "\n\nPrecomputed filing/news thematic cross-check:\n"
                + thematic_catalyst_context
                if thematic_catalyst_context
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
