from cli.main import save_report_to_disk
from tradingagents.evaluation import research_validator


def test_failed_research_audit_suppresses_publishable_trade_instructions(tmp_path, monkeypatch):
    monkeypatch.setattr(
        research_validator,
        "render_post_generation_audit",
        lambda _report_dir: "# Post-Generation Audit\n\n- FAIL: errors=1, warnings=0.",
    )
    raw_decision = (
        "# Portfolio Decision\n\n"
        "**Rating**: Buy\n\nTarget price: 100.\n\nBuild a 5% position now."
    )
    state = {
        "risk_debate_state": {
            "history": "",
            "aggressive_history": "",
            "conservative_history": "",
            "neutral_history": "",
            "latest_speaker": "Judge",
            "current_aggressive_response": "",
            "current_conservative_response": "",
            "current_neutral_response": "",
            "judge_decision": raw_decision,
            "count": 1,
        }
    }

    report_path = save_report_to_disk(state, "601689.SH", tmp_path)

    published_decision = (tmp_path / "5_portfolio" / "decision.md").read_text(encoding="utf-8")
    draft_decision = (tmp_path / "5_portfolio" / "decision_draft.md").read_text(encoding="utf-8")
    complete_report = report_path.read_text(encoding="utf-8")

    assert "Publication status: BLOCKED" in published_decision
    assert "评级、目标价、仓位、替代标的与交易指令已自动抑制" in published_decision
    assert "Build a 5% position now" not in published_decision
    assert "Build a 5% position now" in draft_decision
    assert "Build a 5% position now" not in complete_report
