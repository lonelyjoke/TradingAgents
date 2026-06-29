import json
from types import SimpleNamespace

from tradingagents.dataflows.underwriting_packet import (
    build_company_underwriting_packet,
)


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
