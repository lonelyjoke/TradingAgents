from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_balance_sheet,
    get_buy_side_thesis_instruction,
    get_commodity_context,
    get_evidence_instruction,
    get_cashflow,
    get_focused_report_instruction,
    get_fundamentals,
    get_income_statement,
    get_insider_transactions,
    get_language_instruction,
    get_market_sector_risk,
    get_market_timing_context,
    get_peer_comparison,
    get_research_gap_instruction,
    get_shipping_context,
    get_supply_demand_fallback_instruction,
    get_valuation_percentiles,
)
from tradingagents.dataflows.config import get_config


def create_fundamentals_analyst(llm):
    def fundamentals_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])

        tools = [
            get_fundamentals,
            get_balance_sheet,
            get_cashflow,
            get_income_statement,
            get_commodity_context,
            get_shipping_context,
            get_peer_comparison,
            get_valuation_percentiles,
            get_market_sector_risk,
            get_market_timing_context,
        ]

        system_message = (
            "You are a buy-side fundamental researcher. Write a focused investment memo, not an exhaustive data dump. "
            "Your job is to identify the tradable thesis, test whether the business-cycle or boom-bust expectation can plausibly realize, and explain what evidence supports or weakens the thesis. "
            "Use `get_fundamentals`, `get_balance_sheet`, `get_cashflow`, and `get_income_statement` for core financial quality. "
            "For A-share tickers, also use `get_commodity_context` for product/futures exposure, `get_shipping_context` for freight-cycle exposure, `get_peer_comparison` for same-industry alternatives, `get_valuation_percentiles` for historical valuation zones, `get_market_sector_risk` for broad/sector risk, and `get_market_timing_context` for market mood. "
            "Prioritize: Core Bet, key supporting evidence, key negative evidence, expectation gap, probability/payoff, catalysts, falsification signals, and data gaps. "
            "If another peer looks better than the target, explain why with metrics and caveats. If the sector looks high-risk while the target looks relatively low, discuss whether this is a mispricing opportunity or a company-specific warning. "
            "Do not mechanically upgrade in bull markets or downgrade in bear markets: explain how market mood interacts with the company's valuation, quality, beta, cyclicality, balance sheet, and catalysts. "
            "Append a compact Markdown table only for the most decision-relevant points."
            + get_evidence_instruction()
            + get_research_gap_instruction()
            + get_supply_demand_fallback_instruction()
            + get_buy_side_thesis_instruction()
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
                    " If you or any other assistant has the FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** or deliverable,"
                    " prefix your response with FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** so the team knows to stop."
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
