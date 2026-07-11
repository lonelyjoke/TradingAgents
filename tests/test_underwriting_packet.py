import json
from types import SimpleNamespace

from tradingagents.dataflows.underwriting_packet import (
    CompanyOperatingModel,
    CompanyUnderwritingPacket,
    ForecastLine,
    MoatEvidenceTest,
    ScenarioUnderwriting,
    ValuationBucket,
    ValuationClosure,
    _validate_packet,
    build_company_underwriting_packet,
    compact_underwriting_packet,
)
from tradingagents.dataflows.structured_research import _deterministic_segment_profiles


class RepairingFakeLLM:
    def with_structured_output(self, _schema):
        raise RuntimeError("structured output unavailable")

    def invoke(self, prompt):
        if str(prompt).startswith("Repair the malformed JSON"):
            payload = {
                "schema_version": 1,
                "symbol": "601689.SH",
                "as_of_date": "2026-06-29",
                "forecast_years": ["2026E", "2027E", "2028E"],
                "research_readiness": "partial",
                "readiness_reasons": ["Forecast assumptions need analyst verification."],
                "company_model": {
                    "model_profile": "corporate",
                    "business_archetype": "automotive component platform supplier",
                    "revenue_equation": "sum(customer vehicle volume x platform share x content per vehicle)",
                    "profit_equation": "segment revenue x segment margin - operating expenses",
                    "cash_flow_equation": "net profit + D&A - working capital - capex",
                    "capital_intensity_and_reinvestment": "new plants and tooling require capex and utilization validation",
                },
                "segment_models": [],
                "underwriting_questions": [],
                "forecast_lines": [],
                "scenarios": [],
                "evidence_change_rules": [],
                "reconciliation_checks": [],
                "analyst_instructions": [],
                "preprocessing_notes": [],
            }
            return SimpleNamespace(content=json.dumps(payload, ensure_ascii=False))
        return SimpleNamespace(content='{"schema_version":1 "symbol":"601689.SH"}')


class NullOptionalFieldLLM:
    def with_structured_output(self, _schema):
        raise RuntimeError("structured output unavailable")

    def invoke(self, _prompt):
        payload = {
            "schema_version": 1,
            "symbol": "601689.SH",
            "as_of_date": "2026-06-29",
            "forecast_years": ["2026E", "2027E", "2028E"],
            "research_readiness": "partial",
            "readiness_reasons": [],
            "company_model": {
                "model_profile": "corporate",
                "business_archetype": "automotive component platform supplier",
                "revenue_equation": "vehicle volume x content per vehicle x sourcing share",
                "profit_equation": "revenue x gross margin - operating expenses",
                "cash_flow_equation": "profit + D&A - working capital - capex",
                "share_count_evidence_id": None,
                "moat_mechanisms": None,
            },
            "segment_models": [],
            "underwriting_questions": [],
            "forecast_lines": [],
            "scenarios": [],
            "evidence_change_rules": [],
            "reconciliation_checks": [],
            "analyst_instructions": [],
            "preprocessing_notes": [],
        }
        return SimpleNamespace(content=json.dumps(payload, ensure_ascii=False))


def test_deterministic_preprocessing_recovers_all_filing_product_rows():
    filing_context = (
        "| product | annual | 拓普集团2025年年度报告: 分产品 营业收入 营业成本 毛利率 "
        "减震系统 4,255,569,426.20 3,392,822,605.40 20.27 -3.33 -0.83 "
        "热管理系统 2,091,304,714.40 1,749,547,261.44 16.34 -2.26 -0.77 "
        "机器人执行器 13,591,176.43 9,751,669.09 28.25 1.22 -22.65 |"
    )

    rows = _deterministic_segment_profiles(
        {"filing_intelligence": filing_context}
    )
    by_name = {row.segment: row for row in rows}

    assert "减震系统" in by_name
    assert by_name["热管理系统"].gross_margin_pct == 16.34
    assert by_name["机器人执行器"].revenue_reported_value == 13_591_176.43


def test_deterministic_preprocessing_repairs_pdf_wrapped_segment_delta_columns():
    filing_context = "\n".join(
        [
            "公司主营业务为汽车零部件的研发、生产及销售，产品包括减震系统。",
            (
                "| product | annual | 拓普集团2025年年度报告: 分产品 营业收入 营业成本 "
                "毛利率 比上年增减 减震系 4,255,569,426.20 3,392,822,605.40 "
                "20.27 -3.33 -2.32 减少 0.83 |"
            ),
            (
                "| product | annual | 拓普集团2025年年度报告: 分行业 营业收入 营业成本 "
                "毛利率 比上年增减 汽车零 减少 1.38 27,524,056,756.31 "
                "22,558,076,816.32 18.04 10.04 11.93 |"
            ),
        ]
    )

    rows = _deterministic_segment_profiles(
        {"filing_intelligence": filing_context}
    )
    by_name = {row.segment: row for row in rows}

    assert by_name["减震系统"].gross_margin_change_pp == -0.83
    assert by_name["汽车零部件"].gross_margin_change_pp == -1.38
    assert by_name["汽车零部件"].revenue_growth_pct == 10.04
    assert not any("减少" in name or any(char.isdigit() for char in name) for name in by_name)


def test_underwriting_packet_repairs_malformed_llm_json_instead_of_blank_fallback():
    packet = build_company_underwriting_packet(
        "601689.SH",
        "2026-06-29",
        contexts={"filing_intelligence": "汽车零部件平台供应商。"},
        structured_research={
            "segments": [],
            "semantic_metrics": [],
            "deterministic_evidence": [],
            "conflicts": [],
            "kpe_impacts": [],
        },
        llm=RepairingFakeLLM(),
        enable_llm=True,
    )

    assert packet["company_model"]["business_archetype"] == "automotive component platform supplier"
    assert packet["company_model"]["revenue_equation"].startswith("sum(customer vehicle volume")
    assert "LLM company underwriting failed" not in " ".join(packet["readiness_reasons"])


def test_underwriting_packet_normalizes_null_optional_defaults_without_losing_model():
    packet = build_company_underwriting_packet(
        "601689.SH",
        "2026-06-29",
        contexts={"filing_intelligence": "汽车零部件平台供应商。"},
        structured_research={
            "segments": [],
            "semantic_metrics": [],
            "deterministic_evidence": [],
            "conflicts": [],
            "kpe_impacts": [],
        },
        llm=NullOptionalFieldLLM(),
        enable_llm=True,
    )

    assert packet["company_model"]["share_count_evidence_id"] == ""
    assert packet["company_model"]["moat_mechanisms"] == []
    assert packet["company_model"]["revenue_equation"].startswith("vehicle volume")
    assert "LLM company underwriting failed" not in " ".join(packet["readiness_reasons"])
    assert packet["schema_version"] == 2
    assert packet["handoff_manifest"]["downstream_must_preserve"]
    assert "valuation_closure" in packet


def test_company_depth_contract_survives_downstream_prompt_compaction():
    packet = {
        "schema_version": 2,
        "symbol": "000001.SZ",
        "as_of_date": "2026-06-30",
        "forecast_years": ["2026E", "2027E", "2028E"],
        "research_readiness": "partial",
        "company_model": {"model_profile": "bank"},
        "business_unit_map": [
            {
                "unit_id": "BU01",
                "unit_name": "retail banking",
                "unit_type": "financial_business",
                "disclosure_basis": "reported",
                "revenue_driver_equation": "earning assets x NIM + fees",
            }
        ],
        "segment_models": [],
        "underwriting_questions": [],
        "forecast_lines": [],
        "scenarios": [],
        "thesis_financial_bridges": [
            {
                "bridge_id": "TFB01",
                "thesis_or_question": "Can NIM stabilize?",
                "quantification_status": "partially_quantified",
            }
        ],
        "moat_evidence_tests": [
            {"moat_mechanism": "deposit franchise", "status": "partial"}
        ],
        "valuation_buckets": [
            {"bucket": "bank", "inclusion": "core", "valuation_method": "PB-ROE"}
        ],
        "valuation_closure": {"status": "partial"},
        "llm_analysis_layer": {
            "business_question_tree": ["Can NIM stabilize?"],
            "profit_pool_priority": "retail deposits drive funding cost",
            "expectation_gap_analysis": "market prices weak ROE recovery",
            "red_team_counterarguments": ["credit cost could rise"],
            "final_editorial_synthesis": "synthesize as a bank spread/credit note",
        },
        "handoff_manifest": {"downstream_must_preserve": ["2026E-2028E"]},
    }

    compact = compact_underwriting_packet(packet)

    assert compact["business_unit_map"][0]["unit_name"] == "retail banking"
    assert compact["thesis_financial_bridges"][0]["bridge_id"] == "TFB01"
    assert compact["moat_evidence_tests"][0]["status"] == "partial"
    assert compact["valuation_buckets"][0]["valuation_method"] == "PB-ROE"
    assert compact["llm_analysis_layer"]["business_question_tree"] == [
        "Can NIM stabilize?"
    ]
    assert "weak ROE" in compact["llm_analysis_layer"]["expectation_gap_analysis"]
    assert compact["handoff_manifest"]["downstream_must_preserve"] == ["2026E-2028E"]


def test_valuation_closure_flags_double_counting_and_expected_return_mismatch():
    packet = CompanyUnderwritingPacket(
        symbol="000001.SZ",
        as_of_date="2026-06-30",
        forecast_years=["2026E", "2027E", "2028E"],
        company_model=CompanyOperatingModel(
            model_profile="bank",
            revenue_equation="earning assets x NIM + fee income",
            profit_equation="revenue - operating cost - credit cost",
        ),
        scenarios=[
            ScenarioUnderwriting(
                scenario="bull", probability_pct=30, fair_value_per_share=16
            ),
            ScenarioUnderwriting(
                scenario="base", probability_pct=50, fair_value_per_share=12
            ),
            ScenarioUnderwriting(
                scenario="bear", probability_pct=20, fair_value_per_share=8
            ),
        ],
        valuation_buckets=[
            ValuationBucket(
                bucket="core bank",
                inclusion="core",
                overlap_key="consolidated earnings",
            ),
            ValuationBucket(
                bucket="wealth subsidiary",
                inclusion="scenario",
                overlap_key="consolidated earnings",
            ),
        ],
        valuation_closure=ValuationClosure(
            current_price_cny=10,
            fair_value_per_share_cny=14,
            expected_return_pct=10,
            status="closed",
        ),
    )

    checked = _validate_packet(
        packet,
        {
            "segments": [],
            "semantic_metrics": [],
            "deterministic_evidence": [],
            "kpe_impacts": [],
        },
    )

    reasons = " ".join(checked.readiness_reasons)
    assert checked.valuation_closure.status == "partial"
    assert "double counting" in reasons.lower()
    assert "expected-return arithmetic" in reasons.lower()


def test_chinese_forecast_metric_aliases_do_not_create_empty_duplicate_rows():
    values = {
        "营业收入": (210_000, 225_000, 240_000, "CNY mn"),
        "毛利率": (17.0, 17.5, 18.0, "%"),
        "营业利润": (24_000, 27_000, 30_000, "CNY mn"),
        "归母净利润": (18_000, 20_500, 23_000, "CNY mn"),
        "每股收益": (None, None, None, "CNY/share"),
        "经营活动现金流净额": (30_000, 33_000, 36_000, "CNY mn"),
        "资本开支": (18_000, 17_000, 16_000, "CNY mn"),
        "自由现金流": (12_000, 16_000, 20_000, "CNY mn"),
    }
    packet = CompanyUnderwritingPacket(
        symbol="600309.SH",
        as_of_date="2026-06-30",
        forecast_years=["2026E", "2027E", "2028E"],
        company_model=CompanyOperatingModel(
            model_profile="corporate",
            operating_model_family="volume_price_cost",
            diluted_share_count_mn=3_130,
            revenue_equation="capacity x utilization x volume x ASP",
            profit_equation="volume x (ASP - raw material unit cost) = spread and margin",
            cash_flow_equation="profit + D&A - working capital - capex",
            capital_intensity_and_reinvestment="capex and ROIC gate capacity additions",
        ),
        forecast_lines=[
            ForecastLine(
                metric=metric,
                unit=unit,
                year_1_value=year_1,
                year_2_value=year_2,
                year_3_value=year_3,
            )
            for metric, (year_1, year_2, year_3, unit) in values.items()
        ],
    )

    checked = _validate_packet(packet, {})
    consolidated = [row for row in checked.forecast_lines if row.segment == "consolidated"]
    eps = next(row for row in consolidated if row.metric == "每股收益")

    assert len(consolidated) == 8
    assert not any(row.metric == "parent_net_profit" for row in consolidated)
    assert eps.year_1_value == 18_000 / 3_130
    assert "Required consolidated three-year forecast lines are incomplete." not in checked.readiness_reasons


def test_operating_model_family_surfaces_missing_industry_native_drivers():
    packet = CompanyUnderwritingPacket(
        symbol="600309.SH",
        as_of_date="2026-06-30",
        forecast_years=["2026E", "2027E", "2028E"],
        company_model=CompanyOperatingModel(
            model_profile="corporate",
            operating_model_family="volume_price_cost",
            revenue_equation="volume x ASP",
            profit_equation="revenue - cost",
        ),
    )

    checked = _validate_packet(packet, {})
    reasons = " ".join(checked.readiness_reasons)

    assert "volume_price_cost driver chain is incomplete" in reasons
    assert "capacity" in reasons
    assert "utilization" in reasons
    assert "capex/ROIC" in reasons


def test_moat_cannot_be_proven_without_traceable_evidence_id():
    packet = CompanyUnderwritingPacket(
        symbol="600309.SH",
        as_of_date="2026-06-30",
        forecast_years=["2026E", "2027E", "2028E"],
        company_model=CompanyOperatingModel(
            model_profile="corporate",
            revenue_equation="volume x price",
            profit_equation="revenue x margin",
            moat_mechanisms=["scale cost advantage"],
        ),
        moat_evidence_tests=[
            MoatEvidenceTest(
                moat_mechanism="scale cost advantage",
                observable_test="unit cost below true peers",
                status="proven",
            )
        ],
    )

    checked = _validate_packet(packet, {})

    assert checked.moat_evidence_tests[0].status == "unproven"
    assert "lacks traceable evidence ids" in " ".join(checked.readiness_reasons)


def test_market_cap_and_close_restore_share_count_and_current_price():
    packet = CompanyUnderwritingPacket(
        symbol="600309.SH",
        as_of_date="2026-06-30",
        forecast_years=["2026E", "2027E", "2028E"],
        company_model=CompanyOperatingModel(
            model_profile="corporate",
            revenue_equation="volume x price",
            profit_equation="revenue x margin",
        ),
    )
    contexts = {
        "forecast_model": "| Market cap (CNY) | 214155562156 | current equity value |",
        "price_earnings_decomposition": "| metric | value |\n| close | 68.41 |",
    }

    checked = _validate_packet(packet, {}, contexts)

    assert round(checked.company_model.diluted_share_count_mn or 0, 1) == 3_130.5
    assert checked.valuation_closure.current_price_cny == 68.41
    assert "market cap / close" in checked.company_model.share_count_period


def test_reported_total_share_overrides_bad_llm_share_count_and_recalculates_eps():
    packet = CompanyUnderwritingPacket(
        symbol="600309.SH",
        as_of_date="2026-06-30",
        forecast_years=["2026E", "2027E", "2028E"],
        company_model=CompanyOperatingModel(
            model_profile="corporate",
            diluted_share_count_mn=173.5,
            revenue_equation="volume x price",
            profit_equation="revenue x margin",
        ),
        forecast_lines=[
            ForecastLine(
                metric="Parent Net Profit",
                unit="CNY mn",
                year_1_value=13_400,
                year_2_value=14_500,
                year_3_value=15_800,
            ),
            ForecastLine(
                metric="Diluted EPS",
                unit="CNY/share",
                year_1_value=77.23,
                year_2_value=83.57,
                year_3_value=91.07,
            ),
        ],
        scenarios=[
            ScenarioUnderwriting(
                scenario="base",
                probability_pct=100,
                parent_net_profit_cny_mn=14_500,
                eps_cny=83.57,
                valuation_method="PE",
                valuation_multiple=14,
                fair_value_per_share=1_170,
            )
        ],
    )
    contexts = {
        "shareholder_structure": (
            "| end_date | pledge_count | unrest_pledge | rest_pledge | total_share | pledge_ratio |\n"
            "| --- | ---: | ---: | ---: | ---: | ---: |\n"
            "| 20260626 | 14 | 13845 | 0 | 313047.16 | 4.42 |"
        ),
        "forecast_model": "| Market cap (CNY) | 214155562156 | current equity value |",
        "price_earnings_decomposition": "| close | 68.41 |",
    }

    checked = _validate_packet(packet, {}, contexts)
    eps = next(
        row for row in checked.forecast_lines if row.metric == "Diluted EPS"
    )

    assert checked.company_model.share_count_source_type == "reported_total_share"
    assert round(checked.company_model.diluted_share_count_mn or 0, 4) == 3130.4716
    assert round(eps.year_1_value or 0, 4) == round(13_400 / 3130.4716, 4)
    assert round(checked.scenarios[0].eps_cny or 0, 4) == round(14_500 / 3130.4716, 4)
    assert round(checked.scenarios[0].fair_value_per_share or 0, 4) == round(
        14_500 / 3130.4716 * 14,
        4,
    )
    assert any("LLM-supplied diluted shares rejected" in note for note in checked.preprocessing_notes)
