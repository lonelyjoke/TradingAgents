from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_intraday_context_is_precomputed_and_logged():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
        encoding="utf-8"
    )
    assert '"intraday_behavior_context",' in source
    assert '"get_intraday_behavior_context",' in source
    assert '"intraday_minute_behavior": intraday_behavior_context' in source
    assert '"intraday_behavior_context": final_state.get(' in source


def test_propagator_carries_intraday_context():
    source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )
    assert 'intraday_behavior_context: str = ""' in source
    assert '"intraday_behavior_context": intraday_behavior_context' in source


def test_pm_prompt_receives_intraday_context():
    source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    assert 'prompt_contexts["intraday_behavior_context"]' in source
    assert "Historical minute K-line / intraday behavior context" in source
    assert "Minute-line behavior may adjust timing" in source
