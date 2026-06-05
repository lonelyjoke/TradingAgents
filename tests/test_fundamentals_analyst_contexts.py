from pathlib import Path


FUNDAMENTALS_ANALYST_PATH = (
    Path(__file__).resolve().parents[1]
    / "tradingagents"
    / "agents"
    / "analysts"
    / "fundamentals_analyst.py"
)


def test_fundamentals_analyst_uses_official_contexts_and_coverage_audit():
    source = FUNDAMENTALS_ANALYST_PATH.read_text(encoding="utf-8")

    assert "raw_investor_interaction_context" in source
    assert "raw_policy_planning_context" in source
    assert "investor_interaction_context = prompt_contexts" in source
    assert "policy_planning_context = prompt_contexts" in source
    assert "data_coverage_context = prompt_contexts" in source
    assert "get_investor_interaction_context" in source
    assert "get_policy_planning_context" in source
    assert "Precomputed official investor-interaction context" in source
    assert "Precomputed official policy-planning context" in source
    assert "Precomputed data coverage audit" in source
