from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_a_share_precomputed_context_specs_include_relative_strength():
    source = _read("tradingagents/graph/trading_graph.py")

    assert '"relative_strength_context",' in source
    assert '"get_relative_strength_context",' in source
    assert '"relative_strength": relative_strength_context' in source


def test_propagator_carries_relative_strength_context():
    source = _read("tradingagents/graph/propagation.py")

    assert 'relative_strength_context: str = ""' in source
    assert '"relative_strength_context": relative_strength_context' in source


def test_relative_strength_context_reaches_agents_and_pm():
    files = [
        "tradingagents/agents/analysts/fundamentals_analyst.py",
        "tradingagents/agents/researchers/bull_researcher.py",
        "tradingagents/agents/researchers/bear_researcher.py",
        "tradingagents/agents/managers/research_manager.py",
        "tradingagents/agents/managers/portfolio_manager.py",
    ]

    for path in files:
        source = _read(path)
        assert "relative_strength_context" in source, path
    assert "## 相对走势与指数联动" in _read("tradingagents/agents/managers/portfolio_manager.py")


def test_relative_strength_context_has_coverage_failure_pattern():
    source = _read("tradingagents/dataflows/data_coverage.py")

    assert "# relative strength / index linkage context unavailable" in source
