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
from tradingagents.dataflows.tushare_a_stock import is_a_share_symbol
from tradingagents.dataflows.config import get_config
from tradingagents.dataflows.prompt_compaction import compact_state_fields


def create_news_analyst(llm):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])
        prompt_contexts = compact_state_fields(
            state,
            profile="analyst",
            keys={
                "thematic_catalyst_context",
                "price_move_attribution_context",
                "policy_planning_context",
                "web_fact_check_context",
                "data_coverage_context",
            },
        )
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        price_move_attribution_context = prompt_contexts["price_move_attribution_context"]
        policy_planning_context = prompt_contexts["policy_planning_context"]
        web_fact_check_context = prompt_contexts["web_fact_check_context"]
        data_coverage_context = prompt_contexts["data_coverage_context"]

        is_a_share = is_a_share_symbol(state["company_of_interest"])
        tools = [get_news, get_global_news, get_company_events]
        if is_a_share:
            # For A-share tickers, get_news routes to the same Tushare event
            # path as get_company_events. Exposing both makes the model often
            # duplicate the slow announcements/news scan. Global news is also
            # often rate-limited and lower signal than company/policy events
            # for single-name A-share reports.
            tools = [get_company_events]
        if not thematic_catalyst_context:
            tools.append(get_thematic_catalyst_context)

        system_message = (
            "You are an event and policy researcher. Write a focused catalyst memo, not a broad news digest. "
            "Use get_news(query, start_date, end_date) for targeted company/industry searches, get_global_news(curr_date, look_back_days, limit) only when macro news is directly relevant and the tool is available, get_company_events for A-share announcements, company/industry news, and policy signals, and get_thematic_catalyst_context to validate news-discovered themes against filing text while also checking whether filing-origin themes have recent catalysts. "
            "For A-share tickers, use `get_company_events`; do not duplicate it with `get_news` because both use the same Tushare event path, and rely on the policy-planning context rather than global-news scraping for broad macro policy. "
            "If precomputed filing/news thematic cross-check is provided below, use it directly instead of calling `get_thematic_catalyst_context` again. Otherwise, call `get_thematic_catalyst_context` once before finalizing the material-catalyst section. "
            "Separate company-specific events, industry events, and macro policy events. Cite dates, titles, and sources where available. Explain whether each event strengthens the Core Bet, weakens it, or is background noise. If an event source is unavailable because of Tushare permissions, state that limitation instead of inventing news. "
            "For A-share reports, do not say the whole news interface is disconnected when only Tushare major_news/news/cctv_news is permission-limited. Split the evidence path: official announcements/CNINFO or local filing cache, Tushare news permissions, precomputed price-move News & Rumor Probe, web fact-check, and policy-planning context. If one path fails, use the remaining precomputed contexts and mark that path as a limitation rather than treating all catalysts as unavailable."
            + get_evidence_instruction()
            + get_buy_side_thesis_instruction()
            + get_material_catalyst_instruction()
            + (
                "\n\nPrecomputed filing/news thematic cross-check:\n"
                + thematic_catalyst_context
                if thematic_catalyst_context
                else ""
            )
            + (
                "\n\nPrecomputed price-move attribution and News & Rumor Probe:\n"
                + price_move_attribution_context
                if price_move_attribution_context
                else ""
            )
            + (
                "\n\nPrecomputed policy-planning context:\n"
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
                "\n\nPrecomputed data coverage audit:\n"
                + data_coverage_context
                if data_coverage_context
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
