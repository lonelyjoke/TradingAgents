import pytest
import importlib.util
from pathlib import Path


_SCHEMAS_PATH = Path(__file__).resolve().parents[1] / "tradingagents" / "agents" / "schemas.py"
_SPEC = importlib.util.spec_from_file_location("pm_schema_under_test", _SCHEMAS_PATH)
assert _SPEC and _SPEC.loader
_SCHEMAS = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_SCHEMAS)
normalize_sell_side_pm_decision = _SCHEMAS.normalize_sell_side_pm_decision
render_sell_side_pm_decision = _SCHEMAS.render_sell_side_pm_decision


def _minimal_pm_payload() -> dict:
    return {
        "rating": "Sell",
        "rating_posture": "Sell; valuation risk is high.",
        "research_readiness": "partial",
        "one_line_thesis": "Valuation is stretched versus the base case.",
        "investment_conclusion_and_core_conflict": "Conclusion text.",
        "company_disaggregation": "Company text.",
        "industry_cycle_and_competition": "Industry text.",
        "autonomous_forecast_model": "Forecast text.",
        "thesis_financial_bridge": "Thesis text.",
        "moat_evidence_scorecard": "Moat text.",
        "valuation_closure": (
            "Base fair value is hand-written here but should be replaced by the "
            "program-calculated table."
        ),
        "accounting_and_capital_allocation": "Accounting text.",
        "expectation_gap_and_market_pricing": "Expectation text.",
        "risks_catalysts_verification": "Risk text.",
        "handoff_integrity_audit": "Handoff text.",
        "shared_model_change_audit": "Change text.",
        "report_quality_self_check": "Quality text.",
        "canonical_model_snapshot": [
            {
                "line_id": "shares",
                "period": "20260714",
                "metric": "Total Diluted Shares",
                "value": 8_561_000_000,
                "unit": "shares",
                "status": "reported",
                "evidence_ids": ["EV_SHARES_CONFIRMED"],
                "formula": "",
            },
            {
                "line_id": "2026E_parent_net_profit",
                "period": "2026E",
                "metric": "Parent Net Profit",
                "value": 6184.0,
                "unit": "CNY mn",
                "status": "estimated",
                "evidence_ids": ["EV011"],
                "formula": "",
            },
            {
                "line_id": "2027E_parent_net_profit",
                "period": "2027E",
                "metric": "Parent Net Profit",
                "value": 7785.0,
                "unit": "CNY mn",
                "status": "estimated",
                "evidence_ids": ["EV011"],
                "formula": "",
            },
            {
                "line_id": "2028E_parent_net_profit",
                "period": "2028E",
                "metric": "Parent Net Profit",
                "value": 9520.0,
                "unit": "CNY mn",
                "status": "estimated",
                "evidence_ids": ["EV011"],
                "formula": "",
            },
            {
                "line_id": "2028E_eps",
                "period": "2028E",
                "metric": "EPS (Diluted)",
                "value": 1.11,
                "unit": "CNY/share",
                "status": "estimated",
                "evidence_ids": ["EV011"],
                "formula": "9520 mn / 8561 mn shares",
            },
        ],
        "safe_valuation_assumptions": {
            "current_price_cny": 160.99,
            "required_annual_return_pct": 20.0,
            "holding_period_years": 2.5,
            "margin_of_safety_pct": 20.0,
            "maximum_bear_loss_pct": 20.0,
            "optionality_inputs": [
                {
                    "name": "先进制程期权价值",
                    "metric_name": "牛市增量利润的权益价值",
                    "metric_value_cny_mn": 19120.0,
                    "valuation_multiple": 40.0,
                    "probability_pct": 20.0,
                    "ownership_pct": 100.0,
                    "execution_haircut_pct": 50.0,
                    "evidence_ids": ["KPE01"],
                    "assumption_summary": "Already represented in the bull scenario.",
                }
            ],
            "scenarios": [
                {
                    "scenario": "bear",
                    "probability_pct": 30.0,
                    "valuation_method": "PE",
                    "parent_net_profit_cny_mn": 6300.0,
                    "valuation_multiple": 20.0,
                    "assumption_summary": "Bear",
                    "evidence_ids": ["EV010"],
                },
                {
                    "scenario": "base",
                    "probability_pct": 50.0,
                    "valuation_method": "PE",
                    "parent_net_profit_cny_mn": 9520.0,
                    "valuation_multiple": 30.0,
                    "assumption_summary": "Base",
                    "evidence_ids": ["EV011"],
                },
                {
                    "scenario": "bull",
                    "probability_pct": 20.0,
                    "valuation_method": "PE",
                    "parent_net_profit_cny_mn": 14300.0,
                    "valuation_multiple": 35.0,
                    "assumption_summary": "Bull",
                    "evidence_ids": ["KPE01"],
                },
            ],
        },
    }


def test_pm_deterministic_valuation_normalizes_raw_share_count_units():
    decision, notes = normalize_sell_side_pm_decision(_minimal_pm_payload())

    valuation = decision.deterministic_valuation
    assert valuation.status == "closed"
    assert valuation.diluted_share_count_mn == pytest.approx(8561.0)
    assert valuation.scenario_rows[1]["fair_value_per_share_cny"] == pytest.approx(
        33.3606,
        rel=1e-4,
    )
    assert valuation.scenario_rows[1]["eps_cny"] == pytest.approx(1.1120, rel=1e-4)
    assert valuation.safe_buy_price_ceiling_cny == pytest.approx(18.3974, rel=1e-4)
    assert valuation.optionality_rows == []
    assert any("normalized diluted share count" in note for note in notes)
    assert any("excluded overlapping optionality" in note for note in notes)

    eps_rows = [
        row
        for row in decision.canonical_model_snapshot
        if row.period == "2028E" and row.metric.lower().startswith("eps")
    ]
    assert len(eps_rows) == 1
    assert eps_rows[0].value == pytest.approx(1.1120, rel=1e-4)


def test_foreign_sell_side_forecast_is_classified_and_disclosed_publicly():
    assert _SCHEMAS.infer_sell_side_adoption_level(
        {"decision_use": "增加看多证据，但不改变基准预测；仅作需求对照。"}
    ) == "cross_check_only"
    payload = _minimal_pm_payload()
    payload["sell_side_expectation_matrix"] = [
        {
            "source_ids": ["KSI01", "KPE01"],
            "institution": "野村证券",
            "published_at": "2026-07-16",
            "observation_type": "single_broker",
            "forecast_and_valuation": "上调2027E EPS至66.06元，按20倍PE估值。",
            "revision_or_dispersion": "较前次上调1.6T需求。",
            "comparison_with_our_model": "2027E EPS由58元上调至66.06元。",
            "key_assumptions_and_scenario": "1.6T需求7150万只、ASP年降约10%、毛利率47.5%，属于偏积极需求情景。",
            "evidence_status": "private_text",
            "decision_use": "直接采纳为基准预测和核心估值输入。",
        }
    ]

    decision, notes = normalize_sell_side_pm_decision(payload)
    row = decision.sell_side_expectation_matrix[0]

    assert row.institution_origin == "foreign_sell_side"
    assert row.adoption_level == "direct_base_input"
    assert row.forecast_posture == "optimistic"
    assert any("classified 野村证券" in note for note in notes)
    rendered = render_sell_side_pm_decision(decision)
    assert "外资卖方预测引用与情景假设" in rendered
    assert "不等同于公司指引" in rendered
    assert "直接进入基准预测" in rendered
    assert "1.6T需求7150万只" in rendered
