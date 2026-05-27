# TradingAgents/graph/propagation.py

from typing import Dict, Any, List, Optional
from tradingagents.agents.utils.agent_states import (
    AgentState,
    InvestDebateState,
    RiskDebateState,
)


class Propagator:
    """Handles state initialization and propagation through the graph."""

    def __init__(self, max_recur_limit=100):
        """Initialize with configuration parameters."""
        self.max_recur_limit = max_recur_limit

    def create_initial_state(
        self,
        company_name: str,
        trade_date: str,
        past_context: str = "",
        recent_decision_context: str = "",
        thematic_catalyst_context: str = "",
        commodity_context: str = "",
        filing_intelligence_context: str = "",
        peer_comparison_context: str = "",
        supply_chain_comparison_context: str = "",
        earnings_model_context: str = "",
        market_expectation_context: str = "",
        price_earnings_decomposition_context: str = "",
        management_capital_allocation_context: str = "",
        shareholder_structure_context: str = "",
        investor_interaction_context: str = "",
        policy_planning_context: str = "",
        web_fact_check_context: str = "",
        baijiu_context: str = "",
        compute_leasing_context: str = "",
        dividend_defensive_context: str = "",
        data_coverage_context: str = "",
    ) -> Dict[str, Any]:
        """Create the initial state for the agent graph."""
        return {
            "messages": [("human", company_name)],
            "company_of_interest": company_name,
            "trade_date": str(trade_date),
            "past_context": past_context,
            "recent_decision_context": recent_decision_context,
            "thematic_catalyst_context": thematic_catalyst_context,
            "commodity_context": commodity_context,
            "filing_intelligence_context": filing_intelligence_context,
            "peer_comparison_context": peer_comparison_context,
            "supply_chain_comparison_context": supply_chain_comparison_context,
            "earnings_model_context": earnings_model_context,
            "market_expectation_context": market_expectation_context,
            "price_earnings_decomposition_context": price_earnings_decomposition_context,
            "management_capital_allocation_context": management_capital_allocation_context,
            "shareholder_structure_context": shareholder_structure_context,
            "investor_interaction_context": investor_interaction_context,
            "policy_planning_context": policy_planning_context,
            "web_fact_check_context": web_fact_check_context,
            "baijiu_context": baijiu_context,
            "compute_leasing_context": compute_leasing_context,
            "dividend_defensive_context": dividend_defensive_context,
            "data_coverage_context": data_coverage_context,
            "investment_debate_state": InvestDebateState(
                {
                    "bull_history": "",
                    "bear_history": "",
                    "history": "",
                    "current_response": "",
                    "judge_decision": "",
                    "count": 0,
                }
            ),
            "risk_debate_state": RiskDebateState(
                {
                    "aggressive_history": "",
                    "conservative_history": "",
                    "neutral_history": "",
                    "history": "",
                    "latest_speaker": "",
                    "current_aggressive_response": "",
                    "current_conservative_response": "",
                    "current_neutral_response": "",
                    "judge_decision": "",
                    "count": 0,
                }
            ),
            "market_report": "",
            "fundamentals_report": "",
            "sentiment_report": "",
            "news_report": "",
        }

    def get_graph_args(self, callbacks: Optional[List] = None) -> Dict[str, Any]:
        """Get arguments for the graph invocation.

        Args:
            callbacks: Optional list of callback handlers for tool execution tracking.
                       Note: LLM callbacks are handled separately via LLM constructor.
        """
        config = {"recursion_limit": self.max_recur_limit}
        if callbacks:
            config["callbacks"] = callbacks
        return {
            "stream_mode": "values",
            "config": config,
        }
