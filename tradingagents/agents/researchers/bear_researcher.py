

from tradingagents.agents.utils.agent_utils import (
    get_buy_side_thesis_instruction,
    get_evidence_instruction,
    get_earnings_model_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_investor_interaction_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
    get_supply_chain_selection_instruction,
    get_shareholder_structure_instruction,
    get_three_layer_conclusion_instruction,
    get_thematic_valuation_instruction,
)


def create_bear_researcher(llm):
    def bear_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bear_history = investment_debate_state.get("bear_history", "")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]
        thematic_catalyst_context = state.get("thematic_catalyst_context", "")
        filing_intelligence_context = state.get("filing_intelligence_context", "")
        peer_comparison_context = state.get("peer_comparison_context", "")
        supply_chain_comparison_context = state.get("supply_chain_comparison_context", "")
        earnings_model_context = state.get("earnings_model_context", "")
        market_expectation_context = state.get("market_expectation_context", "")
        management_capital_allocation_context = state.get("management_capital_allocation_context", "")
        shareholder_structure_context = state.get("shareholder_structure_context", "")
        investor_interaction_context = state.get("investor_interaction_context", "")
        policy_planning_context = state.get("policy_planning_context", "")
        round_instruction = (
            "This is a follow-up debate turn. Do not restate your full bear memo. "
            "Respond only to the latest bull objections, add genuinely new evidence "
            "or a sharper inference, and close with the single point that most "
            "improves the bear case. Avoid repeating prior Core Bear Bet / Negative "
            "Expectation Gap / Probability-Payoff sections unless you materially revise them."
            if history.strip()
            else (
                "This is the opening bear turn. Present the core risk thesis clearly, "
                "but keep it focused enough that later turns can add new debate "
                "points instead of repeating the full memo."
            )
        )

        prompt = f"""You are a Bear Analyst making the case against investing in the stock. Your goal is to present a well-reasoned argument emphasizing risks, challenges, and negative indicators. Leverage the provided research and data to highlight potential downsides and counter bullish arguments effectively.

Key points to focus on:

- Core Bear Bet: State what future variable would make the stock unattractive or mispriced on the downside.
- Boom-Bust Risk: Explain why the relevant industry/product/freight/business-cycle expectation may fail or reverse.
- Negative Expectation Gap: Explain what downside risk the market may be underpricing.
- Probability/Payoff: Argue why downside probability and payoff justify caution.
- Risks and Challenges: Highlight factors like market saturation, financial instability, macroeconomic threats, product-price/freight weakness, or policy risks that could hinder the stock's performance.
- Competitive Weaknesses: Emphasize vulnerabilities such as weaker market positioning, declining innovation, or threats from competitors.
- Negative Indicators: Use evidence from financial data, market trends, or recent adverse news to support your position.
- Thematic Catalyst Discipline: Discuss the valuable themes extracted by the system, including credible tier-3 narrative options if they are not fantastical. For each material theme, assess whether it is too small, too slow, too weakly evidenced, already priced, or disconnected from economics; state what would falsify it; and do not silently ignore a theme merely because it is not yet valuation-grade.
- Investor-Interaction Discipline: If official Q&A context is available, discuss what investors keep pressing on, where management answers are non-committal or incomplete, and whether the answer pattern exposes unresolved risks, weak disclosure, or low catalyst visibility.
- Policy-Planning Discipline: If official national or industry policy context is available, test whether policy merely expands the industry while competitors capture the economics, whether support is already priced, and whether the company is a real beneficiary rather than only adjacent to a favored direction.
- Industry-Driver Discipline: Use the industry reading pack from the filing context to identify the sector-native variables that truly decide the thesis, then attack the weak links with outside evidence such as policy, investor Q&A, thematic catalysts, peers, and market expectations. Do not let generic revenue growth obscure the real industry question if the decisive variable is backlog quality, NBV, channel inventory, asset quality, utilization, or freight rate.
- Relative Allocation Discipline: Explicitly answer why capital should not be deployed into a stronger peer or a better-positioned segment elsewhere in the same chain if such alternatives exist.
- Market-Implied Expectation Discipline: State what the current quote already appears to assume, then identify the precise assumption the market is still too optimistic about.
- Bull Counterpoints: Critically analyze the bull argument with specific data and sound reasoning, exposing weaknesses or over-optimistic assumptions.
- Engagement: Present your argument in a conversational style, directly engaging with the bull analyst's points and debating effectively rather than simply listing facts.
- Anti-repetition discipline: {round_instruction}

Resources available:

Market research report: {market_research_report}
Social media sentiment report: {sentiment_report}
Latest world affairs news: {news_report}
Company fundamentals report: {fundamentals_report}
Thematic catalyst cross-check and valuation bridge: {thematic_catalyst_context}
Financial-report intelligence: {filing_intelligence_context}
Same-industry peer comparison: {peer_comparison_context}
Cross-position supply-chain comparison: {supply_chain_comparison_context}
Earnings-model context: {earnings_model_context}
Market-expectation context: {market_expectation_context}
Management/capital-allocation context: {management_capital_allocation_context}
Shareholder-structure context: {shareholder_structure_context}
Official investor-interaction context: {investor_interaction_context}
Official policy-planning context: {policy_planning_context}
Conversation history of the debate: {history}
Last bull argument: {current_response}
Use this information to deliver a compelling bear argument, refute the bull's claims, and engage in a dynamic debate that demonstrates the risks and weaknesses of investing in the stock.
{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_thematic_valuation_instruction()}
{get_filing_intelligence_instruction()}
{get_peer_selection_instruction()}
{get_supply_chain_selection_instruction()}
{get_earnings_model_instruction()}
{get_market_expectation_instruction()}
{get_investor_interaction_instruction()}
{get_policy_planning_instruction()}
{get_three_layer_conclusion_instruction()}
{get_management_capital_allocation_instruction()}
{get_shareholder_structure_instruction()}
{get_focused_report_instruction()}
"""

        response = llm.invoke(prompt)

        argument = f"Bear Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bear_history": bear_history + "\n" + argument,
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bear_node
