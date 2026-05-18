

from tradingagents.agents.utils.agent_utils import (
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


def create_aggressive_debator(llm):
    def aggressive_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        aggressive_history = risk_debate_state.get("aggressive_history", "")

        current_conservative_response = risk_debate_state.get("current_conservative_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]
        thematic_catalyst_context = state.get("thematic_catalyst_context", "")
        filing_intelligence_context = state.get("filing_intelligence_context", "")
        investor_interaction_context = state.get("investor_interaction_context", "")
        policy_planning_context = state.get("policy_planning_context", "")

        trader_decision = state["trader_investment_plan"]

        prompt = f"""As the Aggressive Risk Analyst, your role is to actively champion high-reward, high-risk opportunities, emphasizing bold strategies and competitive advantages. When evaluating the trader's decision or plan, focus intently on the potential upside, growth potential, and innovative benefits—even when these come with elevated risk. Use the provided market data and sentiment analysis to strengthen your arguments and challenge the opposing views. Specifically, respond directly to each point made by the conservative and neutral analysts, countering with data-driven rebuttals and persuasive reasoning. Highlight where their caution might miss critical opportunities or where their assumptions may be overly conservative. Here is the trader's decision:

{trader_decision}

Your task is to create a compelling case for the trader's decision by questioning and critiquing the conservative and neutral stances to demonstrate why your high-reward perspective offers the best path forward. Incorporate insights from the following sources into your arguments:

Market Research Report: {market_research_report}
Social Media Sentiment Report: {sentiment_report}
Latest World Affairs Report: {news_report}
Company Fundamentals Report: {fundamentals_report}
Verified Thematic Catalyst Bridge: {thematic_catalyst_context}
Financial-Report Intelligence And Promoted Discussion Items: {filing_intelligence_context}
Official Investor-Interaction Context: {investor_interaction_context}
Official Policy-Planning Context: {policy_planning_context}
Here is the current conversation history: {history} Here are the last arguments from the conservative analyst: {current_conservative_response} Here are the last arguments from the neutral analyst: {current_neutral_response}. If there are no responses from the other viewpoints yet, present your own argument based on the available data.

Engage actively by addressing any specific concerns raised, refuting the weaknesses in their logic, and asserting the benefits of risk-taking to outpace market norms. Maintain a focus on debating and persuading, not just presenting data. Challenge each counterpoint to underscore why a high-risk approach is optimal. Preserve core discussion items that matter to the thesis even when they are optionality rather than base-case proof. {get_evidence_instruction()} {get_research_gap_instruction()} {get_supply_demand_fallback_instruction()} {get_buy_side_thesis_instruction()} {get_fair_cycle_valuation_instruction()} {get_thematic_valuation_instruction()} {get_filing_intelligence_instruction()} {get_investor_interaction_instruction()} {get_policy_planning_instruction()} {get_focused_report_instruction()} Output conversationally as if you are speaking without any special formatting."""

        response = llm.invoke(prompt)

        argument = f"Aggressive Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "aggressive_history": aggressive_history + "\n" + argument,
            "conservative_history": risk_debate_state.get("conservative_history", ""),
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Aggressive",
            "current_aggressive_response": argument,
            "current_conservative_response": risk_debate_state.get("current_conservative_response", ""),
            "current_neutral_response": risk_debate_state.get(
                "current_neutral_response", ""
            ),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return aggressive_node
