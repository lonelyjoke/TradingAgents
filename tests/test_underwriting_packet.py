import json
from types import SimpleNamespace

from tradingagents.dataflows.underwriting_packet import (
    build_company_underwriting_packet,
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
