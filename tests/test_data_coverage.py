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
    assert "Treat failed, missing or partial modules as neutral non-evidence" in audit


def test_quality_audit_none_detected_is_not_partial():
    text = "# Sell-side depth and key-number audit\n\nWeak or incomplete modules: none detected\n"
    coverage = classify_context_coverage("sell_side_quality_audit", text + ("x" * 200))

    assert coverage.status == "ready"


def test_build_data_coverage_adds_key_fact_ledger():
    audit = build_data_coverage_context(
        {
            "earnings_model": (
                "# Earnings Snapshots\n"
                "| metric | value |\n"
                "| --- | --- |\n"
                "| operating cash flow | -11.66 billion yuan |\n"
                "| net profit | -10.70 billion yuan |\n"
            ),
            "market_expectation": "# Market expectation\nPE 35.9x and PB 1.98x.",
        }
    )

    assert "## Key Facts Ledger" in audit
    assert "KF01" in audit
    assert "operating cash flow" in audit
    assert "Use Key Facts Ledger fact_ids" in audit


def test_build_data_coverage_adds_bank_core_variable_gates():
    audit = build_data_coverage_context(
        {
            "industry_kpi_checklist": (
                "# Bank KPI checklist\n"
                "- NIM: 1.95% latest disclosed value.\n"
                "- CET1 ratio: 12.4%.\n"
                "- PB valuation bridge: 0.85x PB versus 13% ROE.\n"
            ),
            "earnings_model": "# Earnings model\n" + ("bank row\n" * 50),
        }
    )

    assert "## Core Variable Gates" in audit
    assert "| bank | NIM / net interest spread | ready |" in audit
    assert "| bank | Asset quality | missing |" in audit
    assert "Use Core Variable Gates as coverage and retrieval guardrails" in audit


def test_build_data_coverage_prefers_explicit_battery_profile_over_incidental_noise():
    audit = build_data_coverage_context(
        {
            "industry_kpi_checklist": (
                "# Industry KPI Checklist\n"
                "- Playbook: battery / energy-storage chain\n"
                "- Power-battery shipments: 661GWh.\n"
                "- Segment gross margin: 24.8%.\n"
                "- Capacity utilization remains a model gap.\n"
            ),
            "forecast_model_scaffold": (
                "# Forecast Model\n"
                "Power battery revenue = GWh shipments x ASP.\n"
                "OCF and capex determine FCF.\n"
            ),
            "insurance_context": (
                "# Insurance verification context\n"
                "- Status: not_applicable\n"
                "Do not force NBV, EV, solvency or COR analysis into this stock.\n"
            ),
            "dividend_context": "For banks, capital adequacy can constrain dividends.\n" + "x" * 150,
        }
    )

    assert "| battery / energy storage | Power-battery shipments / share | ready |" in audit
    assert "| battery / energy storage | Capacity utilization | missing |" in audit
    assert "Capacity utilization remains a model gap" in audit
    assert "| bank |" not in audit
    assert "| insurance |" not in audit


def test_build_data_coverage_treats_knowledge_planet_kpe_as_private_proxy():
    audit = build_data_coverage_context(
        {
            "knowledge_planet": (
                "# Knowledge Planet Alternative Intelligence Context\n"
                "### Private / Proxy Evidence Ledger\n"
                "| evidence_id | date | source | type | credibility | decision_role | evidence | verification |\n"
                "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
                "| KPE01 | 2026-06-19 | stream_item | industry_weekly_data | broker_survey_or_industry_data | KPI/forecast proxy | hog price improved and piglet price rose | check with Tushare and official monthly sales |\n"
                "### Hog KPI Extraction\n"
                "| core_variable | status | evidence_ids | clue |\n"
                "| --- | --- | --- | --- |\n"
                "| hog ASP / live-hog price | private_proxy | KPE01 | hog price improved |\n"
                "| piglet price | private_proxy | KPE01 | piglet price rose |\n"
            )
        }
    )

    assert "## Key Facts Ledger" in audit
    assert "| KF01 | knowledge_planet | private_proxy | KPI/forecast proxy |" in audit
    assert "## Core Variable Gates" in audit
    assert "| hog breeding | Hog ASP / futures curve | private_proxy |" in audit
    assert "Treat `private_proxy` rows from Knowledge Planet" in audit


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
