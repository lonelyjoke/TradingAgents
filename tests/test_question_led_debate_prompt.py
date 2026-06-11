from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_question_led_debate_instruction_is_wired_through_research_chain():
    files = [
        "tradingagents/agents/researchers/bull_researcher.py",
        "tradingagents/agents/researchers/bear_researcher.py",
        "tradingagents/agents/managers/research_manager.py",
        "tradingagents/agents/managers/portfolio_manager.py",
    ]

    for path in files:
        text = _read(path)
        assert "get_question_led_debate_instruction" in text
        assert "Pre-Debate Underwriting Questions" in text


def test_question_led_debate_schema_requires_audit_loop():
    text = _read("tradingagents/agents/schemas.py")

    assert "question_led_debate_audit" in text
    assert "initial skepticism" in text
    assert "valuation/sizing impact" in text
