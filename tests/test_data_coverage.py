from tradingagents.dataflows.data_coverage import (
    build_data_coverage_context,
    classify_context_coverage,
)


def test_classifies_empty_context_as_missing():
    coverage = classify_context_coverage("filing", "")
    assert coverage.status == "missing"


def test_classifies_unavailable_context_as_failed():
    text = "# Financial-report intelligence unavailable\n\n- Reason: API error"
    coverage = classify_context_coverage("filing", text)
    assert coverage.status == "failed"


def test_classifies_large_context_with_extraction_failure_as_partial():
    text = (
        "# Financial-report intelligence\n"
        "- Extraction status: Financial-report text extraction unavailable.\n"
        "## Earnings Snapshots\n"
        "| --- | --- |\n"
        + ("verified row\n" * 100)
    )
    coverage = classify_context_coverage("filing", text)
    assert coverage.status == "partial"


def test_build_data_coverage_instructs_manager_on_gaps():
    audit = build_data_coverage_context(
        {
            "earnings_model": "# Earnings Snapshots\n| --- | --- |\n" + ("x" * 200),
            "filing_intelligence": "# Financial-report intelligence unavailable",
        }
    )
    assert "filing_intelligence | failed" in audit
    assert "Do not treat failed or missing modules as neutral evidence" in audit
