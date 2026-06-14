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


def test_classifies_narrative_filing_text_gap_as_partial_when_structured_context_exists():
    text = (
        "# Financial-report intelligence\n"
        "- Extraction status: Narrative filing text extraction unavailable: no readable annual, semiannual, or quarterly report body was retrieved.\n"
        "## Filing Reading Coverage Audit\n"
        "| coverage_grade | core_pack_status |\n"
        "| --- | --- |\n"
        "| text_unavailable | unavailable |\n"
        + ("structured financial row\n" * 100)
    )

    coverage = classify_context_coverage("filing", text)

    assert coverage.status == "partial"


def test_classifies_successful_filing_context_with_partial_instruction_as_ready():
    text = (
        "# Financial-report intelligence\n"
        "- Extraction status: Financial-report text extraction succeeded.\n"
        "## Filing Reading Coverage Audit\n"
        "| coverage_grade | core_pack_status |\n"
        "| --- | --- |\n"
        "| strong | ready |\n"
        "## Analyst Instructions\n"
        "- If the coverage audit is partial, state the confidence downgrade.\n"
        + ("verified row\n" * 100)
    )

    coverage = classify_context_coverage("filing", text)

    assert coverage.status == "ready"


def test_build_data_coverage_instructs_manager_on_gaps():
    audit = build_data_coverage_context(
        {
            "earnings_model": "# Earnings Snapshots\n| --- | --- |\n" + ("x" * 200),
            "filing_intelligence": "# Financial-report intelligence unavailable",
        }
    )
    assert "filing_intelligence | failed" in audit
    assert "Do not treat failed or missing modules as neutral evidence" in audit


def test_classifies_unmapped_supply_chain_as_not_applicable():
    text = (
        "# Supply-chain position comparison for 601728.SH\n\n"
        "- No curated or inferred supply-chain map is available for this ticker yet.\n"
        "- Do not invent a cross-position verdict when the value chain has not been explicitly mapped."
    )

    coverage = classify_context_coverage("supply_chain_comparison", text)

    assert coverage.status == "not_applicable"


def test_classifies_telecom_commodity_context_as_not_applicable():
    text = (
        "# Commodity and product price context\n\n"
        "- Spread note: Not applicable: telecom operators do not have a primary commodity/product-price spread driver."
    )

    coverage = classify_context_coverage("commodity_product_price", text)

    assert coverage.status == "not_applicable"
