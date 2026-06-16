from pathlib import Path

from tradingagents.dataflows.thesis_question_research import build_thesis_question_context


def test_aluminum_thesis_questions_force_alumina_power_and_sotp_debate():
    context = build_thesis_question_context(
        "601600.SH",
        "2026-06-16",
        industry_kpi_context=(
            "Playbook: nonferrous metals / aluminum chain. Required KPI Map: "
            "alumina price, power tariff, LME-SHFE spread, segment economics."
        ),
        forecast_model_context=(
            "Primary aluminum revenue; Alumina / upstream spread; Smelting margin; Segment SOTP value."
        ),
        quality_audit_context="Aluminum spread driver coverage | partial | missing power cost",
        commodity_context="| Aluminum | 23830 |\n| Alumina | spread driver |",
        metals_mining_context="# Metals-mining verification context\n\n- Status: triggered\n- Metals covered: Aluminum",
    )

    assert "aluminum integrated producer" in context
    assert "AL-1" in context
    assert "alumina self-supply" in context
    assert "power cost" in context
    assert "segment gross margin" in context
    assert "PM implication" in context
    assert "neutral for direction" in context
    assert "missing alumina, power, or anode cost evidence cannot prove profit deterioration" in context


def test_copper_miner_thesis_questions_force_resource_cost_and_relative_allocation():
    context = build_thesis_question_context(
        "601168.SH",
        "2026-06-16",
        industry_kpi_context=(
            "Playbook: nonferrous metals / copper-mining-smelting. Required KPI Map: "
            "reserve/resource tonnage, grade, AISC, TC/RC, Segment/SOTP."
        ),
        forecast_model_context="Mining revenue; Smelting / refining spread; NAV / SOTP value.",
        peer_comparison_context="Peer sample includes Zijin Mining and Jiangxi Copper.",
        metals_mining_context="# Metals-mining verification context\n\n- Status: triggered\n- Metals covered: Copper, Zinc, Lead",
    )

    assert "copper / multi-metal miner-smelter" in context
    assert "CM-1" in context
    assert "reserve/resource quality" in context
    assert "AISC" in context
    assert "Why own this miner instead of Zijin" in context


def test_thesis_question_context_is_wired_into_graph_and_key_prompts():
    root = Path(__file__).resolve().parents[1]
    graph = (root / "tradingagents" / "graph" / "trading_graph.py").read_text(encoding="utf-8")
    bull = (root / "tradingagents" / "agents" / "researchers" / "bull_researcher.py").read_text(encoding="utf-8")
    bear = (root / "tradingagents" / "agents" / "researchers" / "bear_researcher.py").read_text(encoding="utf-8")
    manager = (root / "tradingagents" / "agents" / "managers" / "research_manager.py").read_text(encoding="utf-8")
    pm = (root / "tradingagents" / "agents" / "managers" / "portfolio_manager.py").read_text(encoding="utf-8")

    assert "build_thesis_question_context" in graph
    assert "thesis_question_context=thesis_question_context" in graph
    assert "Thesis-question context" in bull
    assert "Thesis-question context" in bear
    assert "Thesis Question Context" in manager
    assert "Thesis-question context" in pm
