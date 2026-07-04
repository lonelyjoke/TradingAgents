from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_pm_and_research_prompts_calibrate_insurance_defensive_ratings():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")

    for source in (pm_source, research_source):
        assert "insurance/high-dividend defensive candidates" in source
        assert "one-quarter net profit" in source
        assert "operating cash flow" in source
        assert "OPAT/core operating profit" in source
        assert "solvency" in source
        assert "staged/cautious Overweight" in source or "Staged/Cautious Overweight" in source
        assert "hard negative cash-flow signal with unresolved attribution" in source


def test_insurance_pm_prompt_requires_full_valuation_bridge():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")

    assert "Insurance valuation bridge requirement" in pm_source
    assert "P/EV or EV growth" in pm_source
    assert "NBV multiple" in pm_source
    assert "PB-ROE" in pm_source
    assert "dividend yield and payout/solvency coverage" in pm_source
    assert "SOTP for life/health, P&C, bank" in pm_source
    assert "interim dividend, final dividend, full-year DPS" in pm_source
    assert "segment formula" in pm_source
    assert "per-share conversion" in pm_source
    assert "double-counting checks" in pm_source
    assert "absolute downside" in pm_source
    assert "defensive-basket suitability" in pm_source


def test_insurance_prompts_reconcile_cautious_overweight_and_peer_role():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")
    shared_source = (
        ROOT / "tradingagents" / "agents" / "utils" / "agent_utils.py"
    ).read_text(encoding="utf-8")
    schema_source = (
        ROOT / "tradingagents" / "agents" / "schemas.py"
    ).read_text(encoding="utf-8")

    for source in (pm_source, research_source, shared_source, schema_source):
        assert "Overweight" in source
        assert "subjective PM" in source or "subjective scenario probabilities" in source
        assert "higher-beta" in source
        assert "SOTP" in source
        assert "recovery" in source

    assert "latest annual EV only as a stale base" in shared_source
    assert "conflicting dividend-per-share" in shared_source
    assert "figures must be flagged" in shared_source
    assert "holding-company" in schema_source
    assert "discount" in schema_source


def test_insurance_peer_screen_cannot_drive_underweight_without_native_checks():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")
    shared_source = (
        ROOT / "tradingagents" / "agents" / "utils" / "agent_utils.py"
    ).read_text(encoding="utf-8")
    schema_source = (
        ROOT / "tradingagents" / "agents" / "schemas.py"
    ).read_text(encoding="utf-8")

    for source in (pm_source, research_source, shared_source, schema_source):
        assert "PE" in source
        assert "PB" in source
        assert "ROE" in source
        assert "NBV growth" in source
        assert "NBV margin" in source
        assert "OCF/cash" in source
        assert "solvency" in source
        assert "payout coverage" in source

    assert "cap the PM rating at Hold" in pm_source
    assert "do not mechanically force Hold/Underweight" in research_source
    assert "not a verified substitute" in pm_source
    assert "Rating Evidence Audit" in pm_source
    assert "Rating Evidence Audit" in schema_source


def test_starter_insurance_position_does_not_automatically_map_to_overweight():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")
    schema_source = (
        ROOT / "tradingagents" / "agents" / "schemas.py"
    ).read_text(encoding="utf-8")

    for source in (pm_source, research_source, schema_source):
        assert "starter" in source or "1/3-1/2 target weight" in source
        assert "Hold" in source
        assert "positive" in source or "positive-bias" in source
        assert "standalone basis" in source or "expected value" in source or "standalone fundamental chain" in source

    assert "The Underweight case is not proven" in pm_source
    assert "not `Overweight`" in research_source
    assert "do not default the rating to Hold" in pm_source
    assert "default recommendation should be Hold/positive watch" in research_source
    for source in (pm_source, research_source):
        assert "staged/cautious Overweight" in source or "Staged/Cautious Overweight" in source
        assert "only when" in source


def test_hold_ratings_must_expose_action_posture():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")
    shared_source = (
        ROOT / "tradingagents" / "agents" / "utils" / "agent_utils.py"
    ).read_text(encoding="utf-8")
    schema_source = (
        ROOT / "tradingagents" / "agents" / "schemas.py"
    ).read_text(encoding="utf-8")

    for source in (pm_source, research_source, schema_source):
        assert "Hold / Positive Watch" in source
        assert "Hold / Defensive Starter" in source
        assert "Hold / Neutral Wait" in source
        assert "Hold / Negative Watch" in source

    assert "rating_posture" in pm_source
    assert "rating_posture" in schema_source
    assert "does not hide the intended trade" in shared_source


def test_pm_requires_information_utilization_audit():
    pm_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "portfolio_manager.py"
    ).read_text(encoding="utf-8")
    research_source = (
        ROOT / "tradingagents" / "agents" / "managers" / "research_manager.py"
    ).read_text(encoding="utf-8")
    schema_source = (
        ROOT / "tradingagents" / "agents" / "schemas.py"
    ).read_text(encoding="utf-8")
    kp_source = (
        ROOT / "tradingagents" / "dataflows" / "knowledge_planet_research.py"
    ).read_text(encoding="utf-8")

    assert "information_utilization_audit" in pm_source
    assert "information_utilization_audit" in schema_source
    assert "Information Utilization Audit" in schema_source
    assert "probability adjustment" in pm_source
    assert "sizing/timing adjustment" in pm_source
    assert "not as a standalone proof" in research_source
    assert "not company-specific" in kp_source
    assert "scenario probabilities" in kp_source
