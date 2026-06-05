from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_trading_graph_precomputes_optical_module_context():
    source = _read("tradingagents/graph/trading_graph.py")

    assert '"optical_module_context",' in source
    assert '"get_optical_module_context",' in source
    assert '"optical_module": optical_module_context' in source
    assert "get_optical_module_context" in source


def test_propagator_and_agent_state_carry_optical_module_context():
    propagation_source = _read("tradingagents/graph/propagation.py")
    state_source = _read("tradingagents/agents/utils/agent_states.py")

    assert "optical_module_context" in state_source
    assert "optical_module_context: str = \"\"" in propagation_source
    assert '"optical_module_context": optical_module_context' in propagation_source


def test_pm_research_and_debate_prompts_use_optical_module_context():
    files = [
        "tradingagents/agents/managers/portfolio_manager.py",
        "tradingagents/agents/managers/research_manager.py",
        "tradingagents/agents/researchers/bull_researcher.py",
        "tradingagents/agents/researchers/bear_researcher.py",
        "tradingagents/agents/risk_mgmt/aggressive_debator.py",
        "tradingagents/agents/risk_mgmt/conservative_debator.py",
        "tradingagents/agents/risk_mgmt/neutral_debator.py",
        "tradingagents/agents/trader/trader.py",
    ]

    for relative_path in files:
        source = _read(relative_path)
        assert "optical_module_context" in source, relative_path
        assert "get_optical_module_instruction()" in source, relative_path


def test_fundamentals_analyst_uses_optical_module_context_and_tool():
    source = _read("tradingagents/agents/analysts/fundamentals_analyst.py")

    assert "raw_optical_module_context" in source
    assert "optical_module_context = prompt_contexts" in source
    assert "get_optical_module_context" in source
    assert "get_optical_module_instruction()" in source
