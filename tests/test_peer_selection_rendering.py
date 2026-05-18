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
    assert "\u540c\u4e1a\u6bd4\u8f83\uff1aPeer A is superior on ROE and growth." in rendered
    assert "\u4ea7\u4e1a\u94fe\u4f4d\u7f6e\uff1aUpstream resources are currently more attractive than manufacturing." in rendered
    assert "\u516c\u53f8\u8d28\u91cf=Quality is mixed." in rendered
    assert "\u5f53\u524d\u8d54\u7387=Odds are weak." in rendered
    assert "\u76f8\u5bf9\u914d\u7f6e=Upstream is better." in rendered
    assert "\u7ba1\u7406\u5c42\u4e0e\u8d44\u672c\u914d\u7f6e\uff1aCapital allocation is aggressive." in rendered
    assert "\u80a1\u4e1c\u4e0e\u7b79\u7801\uff1aUnlock and sell-down pressure exist." in rendered
