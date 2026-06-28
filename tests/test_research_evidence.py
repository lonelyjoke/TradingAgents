from tradingagents.dataflows.research_evidence import (
    build_evidence_record,
    classify_evidence_text,
    infer_model_variable,
)


def test_question_and_model_gap_are_not_promoted_to_facts():
    assert classify_evidence_text(
        "industry_kpi",
        "Capacity utilization remains a model gap.",
    ) == ("gap", "missing")
    assert classify_evidence_text(
        "thesis_questions",
        "What is the capacity utilization?",
    ) == ("question", "non_evidence")


def test_reported_fact_carries_source_tier_period_and_variable():
    record = build_evidence_record(
        "EV001",
        "financial_report_intelligence",
        "2025 annual report: power-battery shipments were 541GWh.",
    )

    assert record.status == "reported"
    assert record.source_tier == "primary_or_structured_filing"
    assert record.model_variable == "segment_volume"
    assert "2025" in record.period


def test_generic_model_variable_mapping_is_cross_industry():
    assert infer_model_variable("bank NIM fell 8bps") == "segment_margin"
    assert infer_model_variable("hog complete cost was 13.1 yuan/kg") == "unit_cost"
    assert infer_model_variable("project backlog and capacity utilization improved") == "utilization_or_backlog"
