from cli.main import save_report_to_disk
from tradingagents.evaluation import research_validator


def test_blocked_audit_keeps_complete_report_visible_with_warning(tmp_path, monkeypatch):
    monkeypatch.setattr(
        research_validator,
        "render_post_generation_audit",
        lambda _report_dir: (
            "# Post-Generation Audit\n\n"
            "- BLOCKED: blocking_errors=1, research_errors=1, warnings=0."
        ),
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
    assert "完整研究报告仍然输出" in published_decision
    assert "Build a 5% position now" in published_decision
    assert "Build a 5% position now" in draft_decision
    assert "Build a 5% position now" in complete_report


def test_nonblocking_coverage_gaps_do_not_block_or_downgrade_report(tmp_path, monkeypatch):
    monkeypatch.setattr(
        research_validator,
        "render_post_generation_audit",
        lambda _report_dir: (
            "# Post-Generation Audit\n\n"
            "- REVIEW: blocking_errors=0, research_errors=2, warnings=3."
        ),
    )
    raw_decision = "# Portfolio Decision\n\n**Rating**: Buy\n\nTarget price: 100."
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
    complete_report = report_path.read_text(encoding="utf-8")

    assert "Publication status: REVIEW" in published_decision
    assert "数据缺失本身不改变评级方向" in published_decision
    assert "**Rating**: Buy" in published_decision
    assert "Target price: 100" in complete_report
    assert not (tmp_path / "5_portfolio" / "decision_draft.md").exists()
