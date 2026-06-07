"""Tests for structured-output agents (Trader and Research Manager).

The Portfolio Manager has its own coverage in tests/test_memory_log.py
(which exercises the full memory-log → PM injection cycle).  This file
covers the parallel schemas, render functions, and graceful-fallback
behavior we added for the Trader and Research Manager so all three
decision-making agents share the same shape.
"""

from unittest.mock import MagicMock

import pytest

from tradingagents.agents.managers.research_manager import create_research_manager
from tradingagents.agents.schemas import (
    PortfolioDecision,
    PortfolioRating,
    ResearchPlan,
    TraderAction,
    TraderProposal,
    render_pm_decision,
    render_research_plan,
    render_trader_proposal,
)
from tradingagents.agents.trader.trader import create_trader


# ---------------------------------------------------------------------------
# Render functions
# ---------------------------------------------------------------------------


@pytest.mark.unit
class TestRenderTraderProposal:
    def test_minimal_required_fields(self):
        p = TraderProposal(action=TraderAction.HOLD, reasoning="Balanced setup; no edge.")
        md = render_trader_proposal(p)
        assert "**Action**: Hold" in md
        assert "**Reasoning**: Balanced setup; no edge." in md
        # The trailing FINAL TRANSACTION PROPOSAL line is preserved for the
        # analyst stop-signal text and any external code that greps for it.
        assert "FINAL TRANSACTION PROPOSAL: **HOLD**" in md

    def test_optional_fields_included_when_present(self):
        p = TraderProposal(
            action=TraderAction.BUY,
            reasoning="Strong technicals + fundamentals.",
            entry_price=189.5,
            stop_loss=178.0,
            position_sizing="6% of portfolio",
        )
        md = render_trader_proposal(p)
        assert "**Action**: Buy" in md
        assert "**Entry Price**: 189.5" in md
        assert "**Stop Loss**: 178.0" in md
        assert "**Position Sizing**: 6% of portfolio" in md
        assert "FINAL TRANSACTION PROPOSAL: **BUY**" in md

    def test_optional_fields_omitted_when_absent(self):
        p = TraderProposal(action=TraderAction.SELL, reasoning="Guidance cut.")
        md = render_trader_proposal(p)
        assert "Entry Price" not in md
        assert "Stop Loss" not in md
        assert "Position Sizing" not in md
        assert "FINAL TRANSACTION PROPOSAL: **SELL**" in md


@pytest.mark.unit
class TestRenderResearchPlan:
    def test_required_fields(self):
        p = ResearchPlan(
            recommendation=PortfolioRating.OVERWEIGHT,
            rationale="Bull case carried; tailwinds intact.",
            strategic_actions="Build position over two weeks; cap at 5%.",
        )
        md = render_research_plan(p)
        assert "**Recommendation**: Overweight" in md
        assert "**Rationale**: Bull case carried" in md
        assert "**Strategic Actions**: Build position" in md

    def test_all_5_tier_ratings_render(self):
        for rating in PortfolioRating:
            p = ResearchPlan(
                recommendation=rating,
                rationale="r",
                strategic_actions="s",
            )
            md = render_research_plan(p)
            assert f"**Recommendation**: {rating.value}" in md


@pytest.mark.unit
class TestRenderPortfolioDecision:
    def test_reader_takeaway_build_price_band_renders_after_thesis(self):
        decision = PortfolioDecision(
            rating=PortfolioRating.UNDERWEIGHT,
            company_snapshot="Good business, expensive stock.",
            one_line_thesis="Current odds are weak, but the franchise has value.",
            reader_takeaway_entry_band=(
                "Consider rebuilding only near 18-20x clean mid-cycle earnings, "
                "provided cash conversion stays positive."
            ),
            reader_action_guidance=(
                "Full holders should trim to benchmark weight; prospective builders "
                "should wait for the valuation band before starting."
            ),
            business_driver_map="Revenue, margin, cash conversion.",
            bull_bear_debate="Bull sees growth; bear sees valuation risk.",
            debate_verdict="Bear case wins at today's price.",
            investment_logic_chain="If earnings normalize, valuation compresses.",
            executive_summary="Underweight now; wait for better odds.",
            verification_and_falsification="Watch next quarter cash flow.",
            investment_thesis="The market prices too much perfection.",
        )
        md = render_pm_decision(decision)
        assert "**Reader Take-away / Build Price Band**:" in md
        assert "**Reader Action Guidance / Holders vs Builders**:" in md
        assert "18-20x clean mid-cycle earnings" in md
        assert "Full holders should trim to benchmark weight" in md
        assert md.index("**One-Line Thesis**") < md.index("**Reader Take-away / Build Price Band**")
        assert md.index("**Reader Take-away / Build Price Band**") < md.index(
            "**Reader Action Guidance / Holders vs Builders**"
        )
        assert md.index("**Reader Action Guidance / Holders vs Builders**") < md.index("**Investment Thesis**")

    def test_buy_rating_includes_staged_builder_guidance(self):
        decision = PortfolioDecision(
            rating=PortfolioRating.OVERWEIGHT,
            company_snapshot="Strong franchise with improving cash flow.",
            one_line_thesis="The evidence supports adding exposure in stages.",
            reader_takeaway_entry_band=(
                "Start near 22x clean forward earnings and add on verified order "
                "conversion rather than chasing a one-day move."
            ),
            reader_action_guidance=(
                "Full holders can keep the core position and add only on pullbacks; "
                "prospective builders can open a starter tranche, then add after "
                "margin and cash-flow confirmation."
            ),
            business_driver_map="Orders, gross margin, cash conversion.",
            bull_bear_debate="Bull sees order conversion; bear sees valuation risk.",
            debate_verdict="Bull case wins with staged sizing.",
            investment_logic_chain="If order conversion holds, earnings visibility improves.",
            executive_summary="Overweight with staged entry.",
            verification_and_falsification="Track orders and margin.",
            investment_thesis="Risk/reward is constructive but should be built gradually.",
        )
        md = render_pm_decision(decision)
        assert "**Reader Action Guidance / Holders vs Builders**:" in md
        assert "Full holders can keep the core position" in md
        assert "prospective builders can open a starter tranche" in md

    def test_core_research_questions_render_between_primer_and_thesis(self):
        decision = PortfolioDecision(
            rating=PortfolioRating.OVERWEIGHT,
            company_snapshot="Asset-light market operator.",
            one_line_thesis="The market underprices durable rent visibility.",
            reader_action_guidance="Build in stages after cash-flow confirmation.",
            business_driver_map="Rent, occupancy, contract liabilities, cash conversion.",
            business_model_supply_chain_primer=(
                "The company earns rent and service income from merchants, then "
                "uses the market ecosystem to add trade services."
            ),
            core_research_questions=(
                "| question | debate-informed answer |\n"
                "| --- | --- |\n"
                "| Can rent growth persist? | Bulls proved visibility, bears exposed cash-flow timing. |"
            ),
            bull_bear_debate="Bull sees contract liabilities; bear sees cash-flow timing.",
            debate_verdict="Overweight wins, but only with staged sizing.",
            investment_logic_chain="If rent converts to cash, valuation can recover.",
            executive_summary="Starter position only.",
            verification_and_falsification="Confirm cash conversion and occupancy.",
            investment_thesis="Contract liabilities support revenue visibility.",
        )

        md = render_pm_decision(decision)

        assert "**Core Research Questions & Debate-Informed Answers**" in md
        assert "Can rent growth persist?" in md
        assert md.index("**Business Model & Industry Chain Primer**") < md.index(
            "**Core Research Questions & Debate-Informed Answers**"
        )
        assert md.index("**Core Research Questions & Debate-Informed Answers**") < md.index(
            "**Investment Thesis**"
        )

    def test_value_stock_safety_price_renders_before_action_guidance(self):
        decision = PortfolioDecision(
            rating=PortfolioRating.HOLD,
            company_snapshot="Blue-chip cash generator with a resilient balance sheet.",
            one_line_thesis="Current odds are fair, but a lower price would offer a margin of safety.",
            reader_takeaway_entry_band="Wait for a valuation floor before building.",
            value_stock_safety_price=(
                "Safety price is 8.0-8.5, derived from normalized low-cycle EPS, "
                "FCF, dividend yield, PB/ROE, cash conversion, leverage, payout "
                "capacity, and peer valuation floor; invalidate if cash flow or "
                "asset quality deteriorates."
            ),
            reader_action_guidance="Builders should accumulate slowly only around the safety band.",
            business_driver_map="FCF, payout, ROE, balance-sheet resilience.",
            bull_bear_debate="Bull sees cash returns; bear sees limited growth.",
            debate_verdict="Hold until price improves.",
            investment_logic_chain="Value appears only if price falls to the safety band.",
            executive_summary="Hold with a defensive build anchor.",
            verification_and_falsification="Confirm cash flow and payout; downgrade if leverage rises.",
            investment_thesis="The franchise is stable but not cheap enough today.",
        )
        md = render_pm_decision(decision)
        assert "## Safety Price / Defensive Build Anchor" in md
        assert "8.0-8.5" in md
        assert md.index("**Reader Take-away / Build Price Band**") < md.index(
            "## Safety Price / Defensive Build Anchor"
        )
        assert md.index("## Safety Price / Defensive Build Anchor") < md.index(
            "**Reader Action Guidance / Holders vs Builders**"
        )


# ---------------------------------------------------------------------------
# Trader agent: structured happy path + fallback
# ---------------------------------------------------------------------------


def _make_trader_state():
    return {
        "company_of_interest": "NVDA",
        "investment_plan": "**Recommendation**: Buy\n**Rationale**: ...\n**Strategic Actions**: ...",
    }


def _structured_trader_llm(captured: dict, proposal: TraderProposal | None = None):
    """Build a MagicMock LLM whose with_structured_output binding captures the
    prompt and returns a real TraderProposal so render_trader_proposal works.
    """
    if proposal is None:
        proposal = TraderProposal(
            action=TraderAction.BUY,
            reasoning="Strong setup.",
        )
    structured = MagicMock()
    structured.invoke.side_effect = lambda prompt: (
        captured.__setitem__("prompt", prompt) or proposal
    )
    llm = MagicMock()
    llm.with_structured_output.return_value = structured
    return llm


@pytest.mark.unit
class TestTraderAgent:
    def test_structured_path_produces_rendered_markdown(self):
        captured = {}
        proposal = TraderProposal(
            action=TraderAction.BUY,
            reasoning="AI capex cycle intact; institutional flows constructive.",
            entry_price=189.5,
            stop_loss=178.0,
            position_sizing="6% of portfolio",
        )
        llm = _structured_trader_llm(captured, proposal)
        trader = create_trader(llm)
        result = trader(_make_trader_state())
        plan = result["trader_investment_plan"]
        assert "**Action**: Buy" in plan
        assert "**Entry Price**: 189.5" in plan
        assert "FINAL TRANSACTION PROPOSAL: **BUY**" in plan
        # The same rendered markdown is also added to messages for downstream agents.
        assert plan in result["messages"][0].content

    def test_prompt_includes_investment_plan(self):
        captured = {}
        llm = _structured_trader_llm(captured)
        trader = create_trader(llm)
        trader(_make_trader_state())
        # The investment plan is in the user message of the captured prompt.
        prompt = captured["prompt"]
        assert any("Proposed Investment Plan" in m["content"] for m in prompt)

    def test_falls_back_to_freetext_when_structured_unavailable(self):
        plain_response = (
            "**Action**: Sell\n\nGuidance cut hits margins.\n\n"
            "FINAL TRANSACTION PROPOSAL: **SELL**"
        )
        llm = MagicMock()
        llm.with_structured_output.side_effect = NotImplementedError("provider unsupported")
        llm.invoke.return_value = MagicMock(content=plain_response)
        trader = create_trader(llm)
        result = trader(_make_trader_state())
        assert result["trader_investment_plan"] == plain_response


# ---------------------------------------------------------------------------
# Research Manager agent: structured happy path + fallback
# ---------------------------------------------------------------------------


def _make_rm_state():
    return {
        "company_of_interest": "NVDA",
        "investment_debate_state": {
            "history": "Bull and bear arguments here.",
            "bull_history": "Bull says...",
            "bear_history": "Bear says...",
            "current_response": "",
            "judge_decision": "",
            "count": 1,
        },
    }


def _structured_rm_llm(captured: dict, plan: ResearchPlan | None = None):
    if plan is None:
        plan = ResearchPlan(
            recommendation=PortfolioRating.HOLD,
            rationale="Balanced view across both sides.",
            strategic_actions="Hold current position; reassess after earnings.",
        )
    structured = MagicMock()
    structured.invoke.side_effect = lambda prompt: (
        captured.__setitem__("prompt", prompt) or plan
    )
    llm = MagicMock()
    llm.with_structured_output.return_value = structured
    return llm


@pytest.mark.unit
class TestResearchManagerAgent:
    def test_structured_path_produces_rendered_markdown(self):
        captured = {}
        plan = ResearchPlan(
            recommendation=PortfolioRating.OVERWEIGHT,
            rationale="Bull case is stronger; AI tailwind intact.",
            strategic_actions="Build position gradually over two weeks.",
        )
        llm = _structured_rm_llm(captured, plan)
        rm = create_research_manager(llm)
        result = rm(_make_rm_state())
        ip = result["investment_plan"]
        assert "**Recommendation**: Overweight" in ip
        assert "**Rationale**: Bull case" in ip
        assert "**Strategic Actions**: Build position" in ip

    def test_prompt_uses_5_tier_rating_scale(self):
        """The RM prompt must list all five tiers so the schema enum matches user expectations."""
        captured = {}
        llm = _structured_rm_llm(captured)
        rm = create_research_manager(llm)
        rm(_make_rm_state())
        prompt = captured["prompt"]
        for tier in ("Buy", "Overweight", "Hold", "Underweight", "Sell"):
            assert f"**{tier}**" in prompt, f"missing {tier} in prompt"

    def test_falls_back_to_freetext_when_structured_unavailable(self):
        plain_response = "**Recommendation**: Sell\n\n**Rationale**: ...\n\n**Strategic Actions**: ..."
        llm = MagicMock()
        llm.with_structured_output.side_effect = NotImplementedError("provider unsupported")
        llm.invoke.return_value = MagicMock(content=plain_response)
        rm = create_research_manager(llm)
        result = rm(_make_rm_state())
        assert result["investment_plan"] == plain_response
