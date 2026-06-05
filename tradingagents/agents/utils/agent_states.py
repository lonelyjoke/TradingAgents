from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import MessagesState


# Researcher team state
class InvestDebateState(TypedDict):
    bull_history: Annotated[
        str, "Bullish Conversation history"
    ]  # Bullish Conversation history
    bear_history: Annotated[
        str, "Bearish Conversation history"
    ]  # Bullish Conversation history
    history: Annotated[str, "Conversation history"]  # Conversation history
    current_response: Annotated[str, "Latest response"]  # Last response
    judge_decision: Annotated[str, "Final judge decision"]  # Last response
    count: Annotated[int, "Length of the current conversation"]  # Conversation length


# Risk management team state
class RiskDebateState(TypedDict):
    aggressive_history: Annotated[
        str, "Aggressive Agent's Conversation history"
    ]  # Conversation history
    conservative_history: Annotated[
        str, "Conservative Agent's Conversation history"
    ]  # Conversation history
    neutral_history: Annotated[
        str, "Neutral Agent's Conversation history"
    ]  # Conversation history
    history: Annotated[str, "Conversation history"]  # Conversation history
    latest_speaker: Annotated[str, "Analyst that spoke last"]
    current_aggressive_response: Annotated[
        str, "Latest response by the aggressive analyst"
    ]  # Last response
    current_conservative_response: Annotated[
        str, "Latest response by the conservative analyst"
    ]  # Last response
    current_neutral_response: Annotated[
        str, "Latest response by the neutral analyst"
    ]  # Last response
    judge_decision: Annotated[str, "Judge's decision"]
    count: Annotated[int, "Length of the current conversation"]  # Conversation length


class AgentState(MessagesState):
    company_of_interest: Annotated[str, "Company that we are interested in trading"]
    trade_date: Annotated[str, "What date we are trading at"]

    sender: Annotated[str, "Agent that sent this message"]

    # research step
    market_report: Annotated[str, "Report from the Market Analyst"]
    sentiment_report: Annotated[str, "Report from the Social Media Analyst"]
    news_report: Annotated[
        str, "Report from the News Researcher of current world affairs"
    ]
    fundamentals_report: Annotated[str, "Report from the Fundamentals Researcher"]
    thematic_catalyst_context: Annotated[str, "Precomputed filing/news catalyst context"]
    commodity_context: Annotated[str, "Precomputed commodity/product-price context"]
    price_move_attribution_context: Annotated[str, "Precomputed short-horizon price-move attribution context"]
    shipping_context: Annotated[str, "Precomputed shipping/freight-rate cycle context"]
    filing_intelligence_context: Annotated[str, "Precomputed filing intelligence context"]
    peer_comparison_context: Annotated[str, "Precomputed same-industry peer context"]
    supply_chain_comparison_context: Annotated[str, "Precomputed cross-position chain context"]
    earnings_model_context: Annotated[str, "Precomputed earnings-model bridge context"]
    market_expectation_context: Annotated[str, "Precomputed market-implied expectation context"]
    price_earnings_decomposition_context: Annotated[str, "Precomputed historical price/EPS/PE decomposition context"]
    management_capital_allocation_context: Annotated[str, "Precomputed management/capital-allocation context"]
    shareholder_structure_context: Annotated[str, "Precomputed shareholder/chip context"]
    investor_interaction_context: Annotated[str, "Precomputed official investor-interaction context"]
    policy_planning_context: Annotated[str, "Precomputed national/industry policy-planning context"]
    web_fact_check_context: Annotated[str, "Precomputed web fact-check context for high-frequency facts"]
    baijiu_context: Annotated[str, "Precomputed gated baijiu/liquor verification context for A-share names"]
    compute_leasing_context: Annotated[str, "Precomputed gated compute-leasing verification context for A-share names"]
    dividend_defensive_context: Annotated[str, "Precomputed gated defensive-dividend verification context for A-share names"]
    building_materials_context: Annotated[str, "Precomputed gated building-materials verification context for A-share names"]
    biopharma_context: Annotated[str, "Precomputed gated biopharma/pharma-services verification context for A-share names"]
    software_context: Annotated[str, "Precomputed gated software/SaaS verification context for A-share names"]
    insurance_context: Annotated[str, "Precomputed gated insurance verification context for A-share insurers"]
    medical_device_context: Annotated[str, "Precomputed gated medical-device verification context for A-share names"]
    metals_mining_context: Annotated[str, "Precomputed gated metals/mining verification context for A-share names"]
    data_coverage_context: Annotated[str, "Audit of which precomputed context modules loaded successfully and which failed or are partial"]

    # researcher team discussion step
    investment_debate_state: Annotated[
        InvestDebateState, "Current state of the debate on if to invest or not"
    ]
    investment_plan: Annotated[str, "Plan generated by the Analyst"]

    trader_investment_plan: Annotated[str, "Plan generated by the Trader"]

    # risk management team discussion step
    risk_debate_state: Annotated[
        RiskDebateState, "Current state of the debate on evaluating risk"
    ]
    final_trade_decision: Annotated[str, "Final decision made by the Risk Analysts"]
    past_context: Annotated[str, "Memory log context injected at run start (same-ticker decisions + cross-ticker lessons)"]
