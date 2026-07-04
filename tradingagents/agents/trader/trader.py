"""Trader: turns the Research Manager's investment plan into a concrete transaction proposal."""

from __future__ import annotations

import functools

from langchain_core.messages import AIMessage

from tradingagents.agents.schemas import TraderProposal, render_trader_proposal
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_baijiu_instruction,
    get_buy_side_thesis_instruction,
    get_compute_leasing_instruction,
    get_dividend_defensive_instruction,
    get_evidence_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_insurance_instruction,
    get_knowledge_planet_instruction,
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_optical_module_instruction,
    get_investor_interaction_instruction,
    get_policy_planning_instruction,
    get_research_gap_instruction,
    get_software_instruction,
    get_supply_demand_fallback_instruction,
    get_thematic_valuation_instruction,
    get_web_fact_check_instruction,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)
from tradingagents.dataflows.prompt_compaction import compact_for_prompt, compact_state_fields


def create_trader(llm):
    structured_llm = bind_structured(llm, TraderProposal, "Trader")

    def trader_node(state, name):
        company_name = state["company_of_interest"]
        instrument_context = build_instrument_context(company_name)
        investment_plan = compact_for_prompt(
            state["investment_plan"],
            label="investment_plan",
            profile="trader",
        )
        prompt_contexts = compact_state_fields(
            state,
            profile="trader",
            keys={
                "thematic_catalyst_context",
                "commodity_context",
                "shipping_context",
                "filing_intelligence_context",
                "investor_interaction_context",
                "policy_planning_context",
                "web_fact_check_context",
                "knowledge_planet_context",
                "baijiu_context",
                "compute_leasing_context",
                "optical_module_context",
                "dividend_defensive_context",
                "biopharma_context",
                "software_context",
                "insurance_context",
                "medical_device_context",
                "metals_mining_context",
            },
        )
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        shipping_context = prompt_contexts["shipping_context"]
        filing_intelligence_context = prompt_contexts["filing_intelligence_context"]
        investor_interaction_context = prompt_contexts["investor_interaction_context"]
        policy_planning_context = prompt_contexts["policy_planning_context"]
        web_fact_check_context = prompt_contexts["web_fact_check_context"]
        knowledge_planet_context = prompt_contexts["knowledge_planet_context"]
        baijiu_context = prompt_contexts["baijiu_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        optical_module_context = prompt_contexts["optical_module_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
        biopharma_context = prompt_contexts["biopharma_context"]
        software_context = prompt_contexts["software_context"]
        insurance_context = prompt_contexts["insurance_context"]
        medical_device_context = prompt_contexts["medical_device_context"]
        metals_mining_context = prompt_contexts["metals_mining_context"]

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
                    "Translate the core bet, expectation gap, probability/payoff, and conviction level into action and position sizing. "
                    "Treat missing thesis-critical data as a confidence cap, not as bearish evidence; do not recommend trimming solely because a data source was unavailable."
                    " For shipping names, translate route-level freight evidence or its absence into sizing and watch triggers; do not collapse Hormuz reopening into a one-way bullish or bearish signal without freight-rate/cargo-flow confirmation."
                    f"{get_evidence_instruction()}"
                    f"{get_research_gap_instruction()}"
                    f"{get_supply_demand_fallback_instruction()}"
                    f"{get_buy_side_thesis_instruction()}"
                    f"{get_fair_cycle_valuation_instruction()}"
                    f"{get_thematic_valuation_instruction()}"
                    f"{get_filing_intelligence_instruction()}"
                    f"{get_investor_interaction_instruction()}"
                    f"{get_policy_planning_instruction()}"
                    f"{get_web_fact_check_instruction()}"
                    f"{get_knowledge_planet_instruction()}"
                    f"{get_baijiu_instruction()}"
                    f"{get_compute_leasing_instruction()}"
                    f"{get_optical_module_instruction()}"
                    f"{get_dividend_defensive_instruction()}"
                    f"{get_software_instruction()}"
                    f"{get_insurance_instruction()}"
                    f"{get_medical_device_instruction()}"
                    f"{get_metals_mining_instruction()}"
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
                    f"Commodity/product-price context: {commodity_context}\n\n"
                    f"Shipping/freight-rate context: {shipping_context}\n\n"
                    f"Financial-report intelligence and promoted discussion items: {filing_intelligence_context}\n\n"
                    f"Official investor-interaction context: {investor_interaction_context}\n\n"
                    f"Official policy-planning context: {policy_planning_context}\n\n"
                    f"Web fact-check context: {web_fact_check_context}\n\n"
                    f"Knowledge Planet topic-text intelligence: {knowledge_planet_context}\n\n"
                    f"Gated baijiu verification context: {baijiu_context}\n\n"
                    f"Gated compute-leasing verification context: {compute_leasing_context}\n\n"
                    f"Gated AI optical-module verification context: {optical_module_context}\n\n"
                    f"Gated dividend defensive verification context: {dividend_defensive_context}\n\n"
                    f"Gated biopharma verification context: {biopharma_context}\n\n"
                    f"Gated software verification context: {software_context}\n\n"
                    f"Gated insurance verification context: {insurance_context}\n\n"
                    f"Gated medical-device verification context: {medical_device_context}\n\n"
                    f"Gated metals/mining verification context: {metals_mining_context}\n\n"
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
