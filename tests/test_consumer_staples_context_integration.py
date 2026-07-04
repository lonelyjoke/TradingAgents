from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_a_share_precomputed_context_specs_include_consumer_staples():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(encoding="utf-8")

    assert '"consumer_staples_context",' in source
    assert '"get_consumer_staples_context",' in source
    assert '"consumer_staples": consumer_staples_context' in source


def test_propagator_and_agent_state_carry_consumer_staples_context():
    state_source = (ROOT / "tradingagents" / "agents" / "utils" / "agent_states.py").read_text(
        encoding="utf-8"
    )
    propagation_source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )

    assert "consumer_staples_context" in state_source
    assert "consumer_staples_context: str = \"\"" in propagation_source
    assert '"consumer_staples_context": consumer_staples_context' in propagation_source


def test_pm_and_research_prompts_use_consumer_staples_context():
    pm_source = (ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py").read_text(
        encoding="utf-8"
    )
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")

    assert "consumer_staples_context = prompt_contexts" in pm_source
    assert '("Consumer staples", consumer_staples_context, get_consumer_staples_instruction)' in pm_source
    assert "Consumer Staples Verification Verdict" in research_source
    assert "get_consumer_staples_instruction()" in research_source


def test_fundamentals_analyst_uses_consumer_staples_context_and_tool():
    source = (
        ROOT / "tradingagents" / "agents" / "analysts" / "fundamentals_analyst.py"
    ).read_text(encoding="utf-8")

    assert "raw_consumer_staples_context" in source
    assert "consumer_staples_context = prompt_contexts" in source
    assert "get_consumer_staples_context" in source
    assert "Precomputed gated consumer-staples verification context" in source
