from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


spec = spec_from_file_location(
    "schemas_for_test",
    Path(__file__).resolve().parents[1] / "tradingagents" / "agents" / "schemas.py",
)
schemas = module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(schemas)

PortfolioDecision = schemas.PortfolioDecision
PortfolioRating = schemas.PortfolioRating
ResearchPlan = schemas.ResearchPlan
render_pm_decision = schemas.render_pm_decision
render_research_plan = schemas.render_research_plan


def test_research_plan_renders_peer_selection_verdict():
    plan = ResearchPlan(
        recommendation=PortfolioRating.OVERWEIGHT,
        core_bet="需求恢复。",
        expectation_gap="市场低估恢复。",
        probability_payoff="赔率尚可。",
        cycle_valuation_assessment="低估值/低景气。",
        catalyst_path="订单改善。",
        falsification_signals="订单未改善。",
        conviction_level="Medium",
        rationale="多空比较后偏多。",
        strategic_actions="分批建仓。",
        peer_selection_verdict="同行里暂未出现更优替代。",
        supply_chain_position_verdict="目标所处环节仍是当前更优利润池。",
        earnings_model_bridge="基准情景由销量增长和毛利率企稳共同驱动。",
        market_implied_expectation="当前股价已部分计入修复，但尚未计入利润率改善。",
        company_quality_verdict="好公司。",
        current_odds_verdict="赔率一般。",
        relative_allocation_verdict="同业中可配，但不是绝对最优。",
        management_capital_allocation_verdict="资本配置总体克制。",
        shareholder_structure_verdict="筹码结构稳定。",
    )

    rendered = render_research_plan(plan)
    assert "### Peer Selection Verdict\n同行里暂未出现更优替代。" in rendered
    assert "### Supply-Chain Position Verdict\n目标所处环节仍是当前更优利润池。" in rendered
    assert "### Company Quality Verdict\n好公司。" in rendered
    assert "### Current Odds Verdict\n赔率一般。" in rendered
    assert "### Relative Allocation Verdict\n同业中可配，但不是绝对最优。" in rendered
    assert "### Management & Capital Allocation Verdict\n资本配置总体克制。" in rendered
    assert "### Shareholder Structure Verdict\n筹码结构稳定。" in rendered


def test_portfolio_decision_renders_peer_selection_verdict():
    decision = PortfolioDecision(
        rating=PortfolioRating.HOLD,
        company_snapshot="Company snapshot.",
        one_line_thesis="Watch first.",
        business_driver_map="Price; volume.",
        bull_bear_debate="Bull-bear split.",
        debate_verdict="Evidence is not enough yet.",
        investment_logic_chain="Variables affect earnings and valuation.",
        executive_summary="Keep tracking.",
        verification_and_falsification="Watch orders and margins.",
        investment_thesis="No clear edge yet.",
        peer_selection_verdict="Peer A is superior on ROE and growth.",
        supply_chain_position_verdict="Upstream resources are currently more attractive than manufacturing.",
        earnings_model_bridge="Bear case comes from continued price pressure.",
        market_implied_expectation="The market already prices a strong recovery.",
        company_quality_verdict="Quality is mixed.",
        current_odds_verdict="Odds are weak.",
        relative_allocation_verdict="Upstream is better.",
        management_capital_allocation_verdict="Capital allocation is aggressive.",
        shareholder_structure_verdict="Unlock and sell-down pressure exist.",
    )

    rendered = render_pm_decision(decision)
    assert "**Supporting Evidence Integration**" in rendered
    assert "Peer comparison: Peer A is superior on ROE and growth." in rendered
    assert "Supply-chain position: Upstream resources are currently more attractive than manufacturing." in rendered
    assert "company quality=Quality is mixed." in rendered
    assert "current odds=Odds are weak." in rendered
    assert "relative allocation=Upstream is better." in rendered
    assert "Management and capital allocation: Capital allocation is aggressive." in rendered
    assert "Shareholder and float structure: Unlock and sell-down pressure exist." in rendered


def test_portfolio_decision_renders_core_research_questions_before_thesis():
    decision = PortfolioDecision(
        rating=PortfolioRating.OVERWEIGHT,
        company_snapshot="Company snapshot.",
        one_line_thesis="Watch the core questions.",
        business_driver_map="Rent; cash conversion.",
        business_model_supply_chain_primer="Business model primer.",
        core_research_questions=(
            "| question | debate-informed answer |\n"
            "| --- | --- |\n"
            "| Is growth durable? | Bulls proved visibility; bears exposed cash timing. |"
        ),
        bull_bear_debate="Bull-bear split.",
        debate_verdict="Staged Overweight.",
        investment_logic_chain="Variables affect earnings and valuation.",
        executive_summary="Keep tracking.",
        verification_and_falsification="Watch contract liabilities and cash flow.",
        investment_thesis="The thesis follows from debate-tested evidence.",
    )

    rendered = render_pm_decision(decision)

    assert "**Core Research Questions & Debate-Informed Answers**" in rendered
    assert "Is growth durable?" in rendered
    assert rendered.index("**Business Model & Industry Chain Primer**") < rendered.index(
        "**Core Research Questions & Debate-Informed Answers**"
    )
    assert rendered.index("**Core Research Questions & Debate-Informed Answers**") < rendered.index(
        "**Investment Thesis**"
    )
