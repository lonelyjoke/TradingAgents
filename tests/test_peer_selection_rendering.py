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

    assert "**Peer Selection Verdict**: 同行里暂未出现更优替代。" in render_research_plan(plan)
    assert (
        "**Supply-Chain Position Verdict**: 目标所处环节仍是当前更优利润池。"
        in render_research_plan(plan)
    )
    assert "**Company Quality Verdict**: 好公司。" in render_research_plan(plan)
    assert "**Current Odds Verdict**: 赔率一般。" in render_research_plan(plan)
    assert "**Relative Allocation Verdict**: 同业中可配，但不是绝对最优。" in render_research_plan(plan)
    assert "**Management & Capital Allocation Verdict**: 资本配置总体克制。" in render_research_plan(plan)
    assert "**Shareholder Structure Verdict**: 筹码结构稳定。" in render_research_plan(plan)


def test_portfolio_decision_renders_peer_selection_verdict():
    decision = PortfolioDecision(
        rating=PortfolioRating.HOLD,
        company_snapshot="公司简介。",
        one_line_thesis="先观察。",
        business_driver_map="价格；销量。",
        bull_bear_debate="多空分歧。",
        debate_verdict="证据尚不足。",
        investment_logic_chain="变量变化会影响利润与估值。",
        executive_summary="继续跟踪。",
        verification_and_falsification="看订单与利润率。",
        investment_thesis="当前尚未形成优势。",
        peer_selection_verdict="同行A在ROE和成长性上更优，当前更适合优先建仓。",
        supply_chain_position_verdict="当前链条内更值得布局的是上游资源，而非目标所在的制造环节。",
        earnings_model_bridge="悲观情景来自价格战继续压缩毛利率。",
        market_implied_expectation="市场已在定价较强恢复。",
        company_quality_verdict="公司质量中等。",
        current_odds_verdict="当前赔率偏弱。",
        relative_allocation_verdict="同链条上游更优。",
        management_capital_allocation_verdict="资本配置偏进取。",
        shareholder_structure_verdict="存在解禁与减持压力。",
    )

    assert (
        "**Peer Selection Verdict**: 同行A在ROE和成长性上更优，当前更适合优先建仓。"
        in render_pm_decision(decision)
    )
    assert (
        "**Supply-Chain Position Verdict**: 当前链条内更值得布局的是上游资源，而非目标所在的制造环节。"
        in render_pm_decision(decision)
    )
    assert "**Company Quality Verdict**: 公司质量中等。" in render_pm_decision(decision)
    assert "**Current Odds Verdict**: 当前赔率偏弱。" in render_pm_decision(decision)
    assert "**Relative Allocation Verdict**: 同链条上游更优。" in render_pm_decision(decision)
    assert "**Management & Capital Allocation Verdict**: 资本配置偏进取。" in render_pm_decision(decision)
    assert "**Shareholder Structure Verdict**: 存在解禁与减持压力。" in render_pm_decision(decision)
