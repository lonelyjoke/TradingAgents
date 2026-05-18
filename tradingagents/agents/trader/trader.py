"""Trader: turns the Research Manager's investment plan into a concrete transaction proposal."""

from __future__ import annotations

import functools

from langchain_core.messages import AIMessage

from tradingagents.agents.schemas import TraderProposal, render_trader_proposal
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_buy_side_thesis_instruction,
    get_evidence_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_investor_interaction_instruction,
    get_policy_planning_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
    get_thematic_valuation_instruction,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)


def create_trader(llm):
    structured_llm = bind_structured(llm, TraderProposal, "Trader")

    def trader_node(state, name):
        company_name = state["company_of_interest"]
        instrument_context = build_instrument_context(company_name)
        investment_plan = state["investment_plan"]
        thematic_catalyst_context = state.get("thematic_catalyst_context", "")
        filing_intelligence_context = state.get("filing_intelligence_context", "")
        investor_interaction_context = state.get("investor_interaction_context", "")
        policy_planning_context = state.get("policy_planning_context", "")

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a trading agent analyzing market data to make investment decisions. "
                    "Based on your analysis, provide a specific recommendation to buy, sell, or hold. "
                    "Anchor your reasoning in the analysts' reports and the research plan. "
                    "If the view is bullish, include a reasonable staged profit-taking or trimming range. "
                    "If the view is bearish or cautious, include an entry or re-entry watch range where risk/reward may become attractive again. "
                    "Calibrate action and ranges against market mood, sector valuation risk, stock beta/cyclicality, and company-specific quality. "
                    "Translate the core bet, expectation gap, probability/payoff, and conviction level into action and position sizing."
                    f"{get_evidence_instruction()}"
                    f"{get_research_gap_instruction()}"
                    f"{get_supply_demand_fallback_instruction()}"
                    f"{get_buy_side_thesis_instruction()}"
                    f"{get_fair_cycle_valuation_instruction()}"
                    f"{get_thematic_valuation_instruction()}"
                    f"{get_filing_intelligence_instruction()}"
                    f"{get_investor_interaction_instruction()}"
                    f"{get_policy_planning_instruction()}"
                    f"{get_focused_report_instruction()}"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Based on a comprehensive analysis by a team of analysts, here is an investment "
                    f"plan tailored for {company_name}. {instrument_context} This plan incorporates "
                    f"insights from current technical market trends, macroeconomic indicators, and "
                    f"social media sentiment. Use this plan as a foundation for evaluating your next "
                    f"trading decision.\n\nProposed Investment Plan: {investment_plan}\n\n"
                    f"Verified thematic catalyst bridge: {thematic_catalyst_context}\n\n"
                    f"Financial-report intelligence and promoted discussion items: {filing_intelligence_context}\n\n"
                    f"Official investor-interaction context: {investor_interaction_context}\n\n"
                    f"Official policy-planning context: {policy_planning_context}\n\n"
                    f"Leverage these insights to make an informed and strategic decision."
                ),
            },
        ]

        trader_plan = invoke_structured_or_freetext(
            structured_llm,
            llm,
            messages,
            render_trader_proposal,
            "Trader",
        )

        return {
            "messages": [AIMessage(content=trader_plan)],
            "trader_investment_plan": trader_plan,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")
