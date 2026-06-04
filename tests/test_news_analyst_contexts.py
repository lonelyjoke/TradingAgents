from pathlib import Path


NEWS_ANALYST_PATH = (
    Path(__file__).resolve().parents[1]
    / "tradingagents"
    / "agents"
    / "analysts"
    / "news_analyst.py"
)


def test_news_analyst_uses_precomputed_fallback_contexts():
    source = NEWS_ANALYST_PATH.read_text(encoding="utf-8")

    assert "compact_state_fields" in source
    assert "price_move_attribution_context" in source
    assert "policy_planning_context" in source
    assert "web_fact_check_context" in source
    assert "data_coverage_context" in source
    assert "News & Rumor Probe" in source
    assert "do not say the whole news interface is disconnected" in source
