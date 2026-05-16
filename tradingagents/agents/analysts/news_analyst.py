from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_buy_side_thesis_instruction,
    get_company_events,
    get_evidence_instruction,
    get_focused_report_instruction,
    get_global_news,
    get_language_instruction,
    get_material_catalyst_instruction,
    get_news,
    get_thematic_catalyst_context,
)
from tradingagents.dataflows.config import get_config


def create_news_analyst(llm):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])
        thematic_catalyst_context = state.get("thematic_catalyst_context", "")

        tools = [
            get_news,
            get_global_news,
            get_company_events,
            get_thematic_catalyst_context,
        ]

        system_message = (
            "You are an event and policy researcher. Write a focused catalyst memo, not a broad news digest. "
            "Use get_news(query, start_date, end_date) for targeted company/industry searches, get_global_news(curr_date, look_back_days, limit) only when macro news is directly relevant, get_company_events for A-share announcements, company/industry news, and policy signals, and get_thematic_catalyst_context to validate news-discovered themes against filing text while also checking whether filing-origin themes have recent catalysts. "
            "For A-share tickers, call `get_thematic_catalyst_context` at least once before finalizing the material-catalyst section. "
            "Separate company-specific events, industry events, and macro policy events. Cite dates, titles, and sources where available. Explain whether each event strengthens the Core Bet, weakens it, or is background noise. If an event source is unavailable because of Tushare permissions, state that limitation instead of inventing news."
            + get_evidence_instruction()
            + get_buy_side_thesis_instruction()
            + get_material_catalyst_instruction()
            + (
                "\n\nPrecomputed filing/news thematic cross-check:\n"
                + thematic_catalyst_context
                if thematic_catalyst_context
                else ""
            )
            + get_focused_report_instruction()
            + """ Append a compact Markdown table only for material catalysts, rejected themes, risk events, and verification dates."""
            + get_language_instruction()
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
            "news_report": report,
        }

    return news_analyst_node
