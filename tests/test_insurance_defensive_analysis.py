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
        assert "relative Underweight/watch" in source or "wait-for-H1-validation" in source


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
    assert "absolute downside" in pm_source
    assert "defensive-basket suitability" in pm_source
