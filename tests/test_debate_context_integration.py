from types import SimpleNamespace

import pytest

from tradingagents.agents.managers.portfolio_manager import create_portfolio_manager
from tradingagents.agents.managers.research_manager import create_research_manager
from tradingagents.agents.risk_mgmt.aggressive_debator import create_aggressive_debator
from tradingagents.agents.risk_mgmt.conservative_debator import create_conservative_debator
from tradingagents.agents.risk_mgmt.neutral_debator import create_neutral_debator
from tradingagents.agents.researchers.bear_researcher import create_bear_researcher
from tradingagents.agents.researchers.bull_researcher import create_bull_researcher
from tradingagents.agents.schemas import (
    PortfolioDecision,
    PortfolioRating,
    ResearchPlan,
    render_pm_decision,
    render_research_plan,
)
from tradingagents.agents.trader.trader import create_trader
from tradingagents.agents.utils.agent_states import AgentState
from tradingagents.graph.propagation import Propagator


def _research_state():
    return {
        "market_report": "market",
        "sentiment_report": "sentiment",
        "news_report": "news",
        "fundamentals_report": "fundamentals",
        "thematic_catalyst_context": "themes",
        "filing_intelligence_context": "filings",
        "peer_comparison_context": "peers",
        "supply_chain_comparison_context": "chain",
        "earnings_model_context": "earnings",
        "market_expectation_context": "expectations",
        "management_capital_allocation_context": "management",
        "shareholder_structure_context": "holders",
        "investor_interaction_context": "official interaction signal",
        "policy_planning_context": "official policy signal",
        "investment_debate_state": {
            "history": "",
            "bull_history": "",
            "bear_history": "",
            "current_response": "",
            "judge_decision": "",
            "count": 0,
        },
    }


@pytest.mark.unit
def test_propagator_carries_investor_interaction_context():
    state = Propagator().create_initial_state(
        "002202.SZ",
        "2026-05-16",
        investor_interaction_context="qa-context",
    )
    assert state["investor_interaction_context"] == "qa-context"


@pytest.mark.unit
def test_propagator_carries_policy_planning_context():
    state = Propagator().create_initial_state(
        "002202.SZ",
        "2026-05-16",
        policy_planning_context="policy-context",
    )
    assert state["policy_planning_context"] == "policy-context"


@pytest.mark.unit
def test_agent_state_schema_keeps_new_context_fields():
    assert "investor_interaction_context" in AgentState.__annotations__
    assert "policy_planning_context" in AgentState.__annotations__


@pytest.mark.unit
def test_bull_prompt_forces_interaction_relative_allocation_and_market_expectation():
    captured = {}

    class FakeLLM:
        def invoke(self, prompt):
            captured["prompt"] = prompt
            return SimpleNamespace(content="bull")

    create_bull_researcher(FakeLLM())(_research_state())
    prompt = captured["prompt"]
    assert "official interaction signal" in prompt
    assert "official policy signal" in prompt
    assert "Investor-Interaction Discipline" in prompt
    assert "Policy-Planning Discipline" in prompt
    assert "Primary-Investment Optionality Discipline" in prompt
    assert "Relative Allocation Discipline" in prompt
    assert "Market-Implied Expectation Discipline" in prompt


@pytest.mark.unit
def test_bear_prompt_forces_interaction_relative_allocation_and_market_expectation():
    captured = {}

    class FakeLLM:
        def invoke(self, prompt):
            captured["prompt"] = prompt
            return SimpleNamespace(content="bear")

    create_bear_researcher(FakeLLM())(_research_state())
    prompt = captured["prompt"]
    assert "official interaction signal" in prompt
    assert "official policy signal" in prompt
    assert "Investor-Interaction Discipline" in prompt
    assert "Policy-Planning Discipline" in prompt
    assert "Relative Allocation Discipline" in prompt
    assert "Market-Implied Expectation Discipline" in prompt


@pytest.mark.unit
def test_portfolio_manager_prompt_includes_investor_interaction_context():
    captured = {}

    class FakeStructuredLLM:
        def invoke(self, prompt):
            captured["prompt"] = prompt
            raise NotImplementedError("force freetext fallback")

    class FakeLLM:
        def with_structured_output(self, *_args, **_kwargs):
            return FakeStructuredLLM()

        def invoke(self, prompt):
            captured["fallback_prompt"] = prompt
            return SimpleNamespace(content="pm")

    state = _research_state() | {
        "company_of_interest": "002202.SZ",
        "investment_plan": "plan",
        "trader_investment_plan": "trade",
        "risk_debate_state": {
            "history": "risk",
            "aggressive_history": "",
            "conservative_history": "",
            "neutral_history": "",
            "latest_speaker": "",
            "current_aggressive_response": "",
            "current_conservative_response": "",
            "current_neutral_response": "",
            "judge_decision": "",
            "count": 0,
        },
    }

    create_portfolio_manager(FakeLLM())(state)
    prompt = captured["fallback_prompt"]
    assert "official interaction signal" in prompt
    assert "official policy signal" in prompt
    assert "Investor Communication Verdict" in prompt
    assert "Policy Direction Verdict" in prompt
    assert "Business Segment Breakdown" in prompt
    assert "Peer Comparison Summary" in prompt
    assert "Buy-Side Depth Audit" in prompt
    assert "Use this narrative order" in prompt
    assert "materiality gates, not a checklist" in prompt
    assert "Final-Rating Consistency Rules" in prompt
    assert "The structured `rating` field is the final Portfolio Manager rating" in prompt
    assert "Research Manager, Trader, and risk-analyst ratings are upstream, non-final inputs" in prompt
    assert "holder/builder action" in prompt


@pytest.mark.unit
def test_research_manager_prompt_includes_investor_interaction_and_policy_context():
    captured = {}

    class FakeStructuredLLM:
        def invoke(self, prompt):
            captured["prompt"] = prompt
            raise NotImplementedError("force freetext fallback")

    class FakeLLM:
        def with_structured_output(self, *_args, **_kwargs):
            return FakeStructuredLLM()

        def invoke(self, prompt):
            captured["fallback_prompt"] = prompt
            return SimpleNamespace(content="manager")

    state = _research_state() | {
        "company_of_interest": "002202.SZ",
        "recent_decision_context": "",
    }
    create_research_manager(FakeLLM())(state)
    prompt = captured["fallback_prompt"]
    assert "official interaction signal" in prompt
    assert "official policy signal" in prompt


@pytest.mark.unit
def test_trader_prompt_keeps_promoted_contexts():
    captured = {}

    class FakeStructuredLLM:
        def invoke(self, messages):
            captured["messages"] = messages
            raise NotImplementedError("force freetext fallback")

    class FakeLLM:
        def with_structured_output(self, *_args, **_kwargs):
            return FakeStructuredLLM()

        def invoke(self, messages):
            captured["fallback_messages"] = messages
            return SimpleNamespace(content="trade")

    state = _research_state() | {
        "company_of_interest": "002202.SZ",
        "investment_plan": "plan",
    }
    create_trader(FakeLLM())(state)
    user_prompt = captured["fallback_messages"][1]["content"]
    assert "themes" in user_prompt
    assert "filings" in user_prompt
    assert "official interaction signal" in user_prompt
    assert "official policy signal" in user_prompt


@pytest.mark.unit
@pytest.mark.parametrize(
    ("factory", "latest_key"),
    [
        (create_aggressive_debator, "current_aggressive_response"),
        (create_conservative_debator, "current_conservative_response"),
        (create_neutral_debator, "current_neutral_response"),
    ],
)
def test_risk_prompts_keep_promoted_contexts(factory, latest_key):
    captured = {}

    class FakeLLM:
        def invoke(self, prompt):
            captured["prompt"] = prompt
            return SimpleNamespace(content="risk")

    state = _research_state() | {
        "trader_investment_plan": "trade",
        "risk_debate_state": {
            "history": "",
            "aggressive_history": "",
            "conservative_history": "",
            "neutral_history": "",
            "latest_speaker": "",
            "current_aggressive_response": "",
            "current_conservative_response": "",
            "current_neutral_response": "",
            "judge_decision": "",
            "count": 0,
        },
    }
    result = factory(FakeLLM())(state)
    prompt = captured["prompt"]
    assert "themes" in prompt
    assert "filings" in prompt
    assert "official interaction signal" in prompt
    assert "official policy signal" in prompt
    assert latest_key in result["risk_debate_state"]


@pytest.mark.unit
def test_pm_renderer_preserves_new_verdict_fields():
    decision = PortfolioDecision(
        rating=PortfolioRating.UNDERWEIGHT,
        company_snapshot="company",
        one_line_thesis="thesis",
        business_driver_map="drivers",
        bull_bear_debate="debate",
        debate_verdict="verdict",
        investment_logic_chain="chain",
        executive_summary="summary",
        verification_and_falsification="verify",
        investment_thesis="investment thesis",
        business_segment_breakdown="segment revenue growth margin",
        forward_forecast_model="forecast revenue margin eps",
        valuation_framework="SOTP core and scenario value",
        market_behavior_validation="minute-line validation only",
        peer_comparison_summary="peer rank and comparable alternatives",
        investor_communication_verdict="communication",
        policy_direction_verdict="policy",
        industry_driver_verdict="industry",
        strategic_optionality_verdict="optionality",
        buy_side_depth_audit="remaining thin spots",
    )
    rendered = render_pm_decision(decision)
    assert "Business Segment Breakdown: segment revenue growth margin" in rendered
    assert "Forward forecast model: forecast revenue margin eps" in rendered
    assert "Valuation framework: SOTP core and scenario value" in rendered
    assert "Market behavior validation: minute-line validation only" in rendered
    assert "**Supporting Evidence Integration**" in rendered
    assert "Peer Comparison Summary: peer rank and comparable alternatives" in rendered
    assert "Buy-side depth audit: remaining thin spots" in rendered
    assert "Investor communication: communication" in rendered
    assert "Policy and demand backdrop: policy" in rendered
    assert "Industry-native variables: industry" in rendered
    assert "Strategic optionality: optionality" in rendered


@pytest.mark.unit
def test_research_plan_renderer_preserves_new_verdict_fields():
    plan = ResearchPlan(
        recommendation=PortfolioRating.UNDERWEIGHT,
        core_bet="bet",
        expectation_gap="gap",
        probability_payoff="payoff",
        cycle_valuation_assessment="cycle",
        catalyst_path="catalyst",
        falsification_signals="falsify",
        conviction_level="medium",
        rationale="rationale",
        strategic_actions="actions",
        investor_communication_verdict="communication",
        policy_direction_verdict="policy",
        industry_driver_verdict="industry",
        strategic_optionality_verdict="optionality",
    )
    rendered = render_research_plan(plan)
    assert "**Investor Communication Verdict**: communication" in rendered
    assert "**Policy Direction Verdict**: policy" in rendered
    assert "**Industry Driver Verdict**: industry" in rendered
    assert "**Strategic Optionality Verdict**: optionality" in rendered
