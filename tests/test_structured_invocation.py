import json
from types import SimpleNamespace

from pydantic import BaseModel

from tradingagents.agents.schemas import (
    CanonicalModelLine,
    ForecastAssumption,
    ModelHandoffChange,
    PortfolioRating,
    SellSideEditorialReview,
    SellSidePMDecision,
    normalize_sell_side_pm_decision,
    render_sell_side_pm_decision,
)
from tradingagents.agents.managers.portfolio_manager import (
    _analytical_structure_issues,
    _canonical_handoff_issues,
    _editorial_revision_prompt,
    _enforce_forecast_methodology,
    _merge_manager_canonical_snapshot,
    _normalize_sell_side_lineage,
)
from tradingagents.agents.managers.research_manager import (
    _complete_unchanged_handoff_lines,
    _research_manager_handoff_issues,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)
from tradingagents.dataflows.pm_report_compaction import split_pm_public_report


class TinyDecision(BaseModel):
    rating: str
    report: str


def test_common_pm_schema_aliases_do_not_trigger_free_text_fallback():
    assumption = ForecastAssumption.model_validate(
        {
            "parameter": "volume growth",
            "affected_business": "group",
            "historical_anchor": "FY25",
            "evidence_status": "estimated",
            "base_case": "10%",
            "bull_case": "15%",
            "bear_case": "0%",
            "rationale_and_evidence": "analyst model",
            "sensitivity": "1pp volume changes profit",
            "confidence": "medium",
            "verification_gate": "FY26 results",
        }
    )
    change = ModelHandoffChange.model_validate(
        {
            "line_id": "rating",
            "old_value": "Overweight",
            "new_value": "Hold",
            "unit": "rating",
            "reason": "risk changed",
            "eps_fcf_valuation_impact": "none",
            "disposition": "accepted",
        }
    )

    assert assumption.evidence_status == "analyst_estimate"
    assert change.old_value is None
    assert change.new_value is None


class FailingStructured:
    def invoke(self, _prompt):
        raise ValueError("provider schema validation failed")


class JsonFallbackLLM:
    def invoke(self, _prompt):
        return SimpleNamespace(
            content=json.dumps({"rating": "Hold", "report": "deep report"})
        )


class ThinkingNoToolChoiceLLM:
    def __init__(self):
        self.prompts = []

    def with_structured_output(self, _schema):
        raise NotImplementedError("thinking mode does not support tool_choice")

    def invoke(self, prompt):
        self.prompts.append(str(prompt))
        return SimpleNamespace(
            content=json.dumps({"rating": "Hold", "report": "validated report"})
        )


def test_free_text_json_is_revalidated_and_rendered_as_structured_output():
    rendered, metadata = invoke_structured_or_freetext(
        FailingStructured(),
        JsonFallbackLLM(),
        "prompt",
        lambda value: f"{value.rating}: {value.report}",
        "Portfolio Manager",
        return_metadata=True,
        fallback_schema=TinyDecision,
    )

    assert rendered == "Hold: deep report"
    assert metadata["mode"] == "schema_repaired_fallback"
    assert "provider schema validation failed" in metadata["structured_error"]


def test_thinking_model_uses_single_schema_prompt_without_tool_choice():
    llm = ThinkingNoToolChoiceLLM()
    structured = bind_structured(llm, TinyDecision, "Research Manager")

    rendered, metadata = invoke_structured_or_freetext(
        structured,
        llm,
        "prompt",
        lambda value: f"{value.rating}: {value.report}",
        "Research Manager",
        return_metadata=True,
        fallback_schema=TinyDecision,
    )

    assert rendered == "Hold: validated report"
    assert metadata["mode"] == "schema_prompt_structured"
    assert len(llm.prompts) == 1
    assert "STRUCTURED OUTPUT CONTRACT" in llm.prompts[0]


def test_sell_side_schema_renders_all_six_company_depth_contracts():
    long_300 = "evidence mechanism financial impact valuation implication. " * 10
    long_500 = "evidence mechanism financial impact valuation implication. " * 18
    long_600 = "evidence mechanism financial impact valuation implication. " * 22
    long_700 = "evidence mechanism financial impact valuation implication. " * 26
    long_800 = "evidence mechanism financial impact valuation implication. " * 30
    decision = SellSidePMDecision(
        rating=PortfolioRating.HOLD,
        rating_posture="Hold / Positive Watch",
        research_readiness="partial",
        one_line_thesis="Operating evidence is improving but valuation is balanced.",
        research_questions=["Can volume growth offset price pressure?"],
        question_verdicts=[
            {
                "question": "Can volume growth offset price pressure?",
                "why_decisive": "It determines revenue growth and fixed-cost absorption.",
                "conclusion": "Current evidence supports only a partial offset.",
                "evidence_used": ["EV01: 2025A volume", "EV02: 2026Q1 margin"],
                "strongest_counterevidence": "ASP and utilization are not disclosed.",
                "model_or_valuation_effect": "Base revenue retained; probability unchanged.",
                "confidence": "medium",
                "next_verification": "2026H1 filing",
            }
        ],
        forecast_takeaways=[
            {
                "takeaway": "Earnings growth depends on margin stability, not multiple expansion.",
                "evidence_anchor": "2025A margin and 2026Q1 checkpoint.",
                "financial_implication": "A 1ppt margin move changes EPS and fair value materially.",
                "confidence_and_risk": "Medium; utilization is not disclosed.",
            }
        ],
        forecast_assumptions=[
            {
                "parameter": "gross margin",
                "affected_business": "group",
                "historical_anchor": "2025A 25%",
                "evidence_status": "reported",
                "base_case": "25%",
                "bull_case": "26%",
                "bear_case": "23%",
                "rationale_and_evidence": "Annual filing and Q1 checkpoint.",
                "sensitivity": "1ppt changes parent profit and EPS through gross profit.",
                "confidence": "medium",
                "verification_gate": "2026H1 filing",
            }
        ],
        core_theses=[
            {
                "rank": 1,
                "takeaway": "The cost moat is investable only if margin remains stable.",
                "decisive_question": "Does scale translate into durable unit economics?",
                "evidence": "Reported margin and cash conversion.",
                "strongest_counterevidence": "Price competition may absorb cost savings.",
                "financial_transmission": "Utilization -> unit cost -> margin -> EPS -> PE.",
                "market_pricing": "The current multiple assumes no material margin expansion.",
                "falsification_gate": "Two reporting periods below the bear margin threshold.",
                "verdict": "partial",
            }
        ],
        investment_conclusion_and_core_conflict=long_300,
        canonical_model_snapshot=[
            CanonicalModelLine(
                line_id="shares",
                period="current",
                metric="diluted shares",
                value=1000,
                unit="mn shares",
                status="calculated",
                formula="market cap / close",
            ),
            CanonicalModelLine(line_id="2026E_revenue", period="2026E", metric="revenue", value=100, unit="CNY mn", status="estimated"),
            CanonicalModelLine(line_id="2027E_revenue", period="2027E", metric="revenue", value=110, unit="CNY mn", status="estimated"),
            CanonicalModelLine(line_id="2028E_revenue", period="2028E", metric="revenue", value=120, unit="CNY mn", status="estimated"),
        ],
        business_model_mechanisms=[
            {
                "link": "order to delivery",
                "how_it_works": "customers place project orders before delivery",
                "economic_driver": "volume and delivery cycle",
                "cash_and_capital_feature": "contract liabilities and working capital",
                "evidence_or_gap": "reported order indicators",
                "analyst_conclusion": "cash timing matters for earnings quality",
            }
        ],
        segment_economics=[
            {
                "business_unit": "core product",
                "economic_role": "mature core",
                "disclosure_basis": "analyst_estimate",
                "scale_and_growth": "reported revenue direction, exact split unavailable",
                "margin_and_cash": "margin proxy with disclosed limits",
                "driver_equation": "volume x ASP x margin",
                "valuation_treatment": "core",
                "evidence_ids": ["EV01"],
                "missing_or_next_check": "next filing segment table",
            }
        ],
        company_disaggregation=long_600,
        industry_cycle_and_competition=long_500,
        autonomous_forecast_model=long_800,
        thesis_financial_bridge=long_700,
        moat_evidence_scorecard=long_500,
        accounting_and_capital_allocation=long_500,
        expectation_gap_and_market_pricing=long_500,
        valuation_closure=long_600,
        risks_catalysts_verification=long_600,
        handoff_integrity_audit="Model v2 units, years and unresolved cells are preserved.",
        shared_model_change_audit="No silent assumption changes.",
        report_quality_self_check="All mandatory contracts are present.",
    )

    rendered = render_sell_side_pm_decision(decision)
    assert "中性（Hold）" in rendered

    for heading in (
        "## 一、投资结论",
        "## 二、公司画像、商业模式与利润池",
        "## 三、行业格局、竞争优势与护城河",
        "## 四、经营质量、财务特征与资本配置",
        "## 五、核心投资逻辑与关键分歧",
        "## 六、盈利预测与关键变量",
        "## 七、市场预期差与估值",
        "## 八、风险、催化剂与跟踪",
    ):
        assert heading in rendered
    public, appendix, moved = split_pm_public_report(rendered)
    assert sum(1 for line in public.splitlines() if line.startswith("## ")) == 8
    assert "Company Disaggregation" not in public
    assert "2026E_revenue" not in public
    assert "预测take-aways" in public
    assert "本报告要回答的关键问题" not in public
    assert "核心问题裁决" not in public
    assert "核心假设与敏感性" in public
    assert "evidence mechanism financial impact" in public
    assert "### 商业模式如何运转" not in public
    assert "### 分部经济与价值归属" not in public
    assert "### 商业模式如何运转" in appendix
    assert "### 交接完整性审计" in appendix
    assert moved == ["内部附录A：业务机制与分部经济", "内部附录E：模型交接与报告质量审计"]


def test_editorial_review_is_advisory_and_section_specific():
    review = SellSideEditorialReview(
        revision_required=True,
        company_understanding_score=3,
        independent_model_score=4,
        evidence_and_counterevidence_score=2,
        valuation_closure_score=3,
        readability_and_synthesis_score=4,
        strongest_aspects=["The forecast is independently driver-based."],
        findings=[
            {
                "section": "thesis_moat_financial_bridge",
                "priority": "must_revise",
                "issue": "The moat conclusion lacks counterevidence.",
                "evidence_or_logic_gap": "Peer margin erosion is available but unused.",
                "revision_instruction": "Add the peer counterexample and trace the base-case margin impact.",
            }
        ],
        overall_editorial_verdict="Revise one section; do not change the rating.",
    )

    assert review.findings[0].section == "thesis_moat_financial_bridge"
    assert review.revision_required is True


def test_editorial_revision_reuses_draft_without_original_full_prompt():
    prompt = _editorial_revision_prompt(
        decision_payload={"rating": "Hold", "company_disaggregation": "existing depth"},
        review_payload={"revision_required": True, "findings": []},
        handoff_issues=[],
        manager_payload={"canonical_model_snapshot": [{"line_id": "2026E_revenue"}]},
        structured_research_context="STRUCTURED_SOURCE",
        fundamentals_context="FUNDAMENTAL_SOURCE",
        lessons_line="- Lessons from prior decisions and outcomes:\nPRIOR_LESSON\n",
        recent_decision_line="- Most recent same-ticker decision:\nPRIOR_DECISION\n",
    )

    assert "Original PM draft JSON" in prompt
    assert "existing depth" in prompt
    assert "STRUCTURED_SOURCE" in prompt
    assert "FUNDAMENTAL_SOURCE" in prompt
    assert "PRIOR_LESSON" in prompt
    assert "PRIOR_DECISION" in prompt
    assert "recreate unaffected sections from raw module dumps" in prompt


def test_forecast_methodology_is_downgraded_when_segment_rows_do_not_reconcile():
    payload, notes = _enforce_forecast_methodology(
        {
            "autonomous_forecast_model": "本报告采用自下而上的分部三年预测模型。",
            "segment_economics": [
                {"business_unit": "动力电池", "valuation_treatment": "core"},
                {"business_unit": "储能电池", "valuation_treatment": "core"},
            ],
        },
        {
            "underwriting_packet": {
                "forecast_lines": [
                    {
                        "segment": "consolidated",
                        "year_1_value": 1,
                        "year_2_value": 2,
                        "year_3_value": 3,
                    }
                ]
            }
        },
    )

    assert "混合模型" in payload["autonomous_forecast_model"]
    assert "自下而上" not in payload["autonomous_forecast_model"]
    assert notes


def test_sell_side_lineage_replaces_invented_alias_with_exact_ksi_id():
    payload, notes = _normalize_sell_side_lineage(
        {
            "sell_side_expectation_matrix": [
                {
                    "source_ids": ["KSI_dongwu"],
                    "institution": "东吴证券",
                    "published_at": "2026-07-01",
                    "forecast_and_valuation": "目标价632元，2026E净利润962亿元",
                    "comparison_with_our_model": "本模型882亿元",
                }
            ],
            "alternative_intelligence_decisions": [
                {
                    "kpe_ids": ["KPE01"],
                    "source_type": "channel_check",
                    "evidence_grade": "B_private_edge",
                    "public_crosscheck": "待核验。",
                }
            ],
        },
        {
            "sell_side_intelligence": [
                {
                    "intelligence_id": "KSI02",
                    "kpe_ids": "KPE01",
                    "institution": "东吴电新",
                    "valuation_facts": "target_price=632元",
                    "forecast_facts": "2026E净利润962亿元",
                }
            ],
            "known_kpe_ledger": {"KPE01": {"source_type": "sell_side_push"}},
        },
    )

    assert payload["sell_side_expectation_matrix"][0]["source_ids"] == [
        "KSI02",
        "KPE01",
    ]
    alt = payload["alternative_intelligence_decisions"][0]
    assert alt["source_type"] == "sell_side_view"
    assert alt["evidence_grade"] == "C_market_narrative"
    assert "不构成独立交叉验证" in alt["public_crosscheck"]
    assert notes


def test_sell_side_lineage_drops_unlinked_kpe_claim():
    payload, notes = _normalize_sell_side_lineage(
        {
            "sell_side_expectation_matrix": [
                {
                    "source_ids": ["KSI01", "KPE02"],
                    "institution": "未公开渠道",
                    "published_at": "2026-07-02",
                    "forecast_and_valuation": "FY26利润预测",
                    "comparison_with_our_model": "低于本模型",
                }
            ]
        },
        {
            "sell_side_intelligence": [
                {
                    "intelligence_id": "KSI01",
                    "kpe_ids": [],
                    "institution": "未公开渠道",
                }
            ]
        },
    )

    assert payload["sell_side_expectation_matrix"][0]["source_ids"] == ["KSI01"]
    assert notes


def test_deterministic_pm_engine_calculates_eps_fcf_scenarios_and_safe_price():
    payload = {
        "rating": "Hold", "rating_posture": "Hold / Positive Watch", "research_readiness": "partial",
        "one_line_thesis": "Wait for evidence and a safer price.",
        "investment_conclusion_and_core_conflict": "Conclusion.",
        "canonical_model_snapshot": [
            {"line_id": "shares", "period": "current", "metric": "diluted_share_count", "value": 2000, "unit": "mn shares", "status": "calculated"},
            {"line_id": "base_fair_value", "period": "scenario", "metric": "Fair Value (Base)", "value": 200000, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "fair_value_per_share", "period": "consolidated", "metric": "Fair Value / Share", "value": 999, "unit": "CNY/share", "status": "estimated"},
            {"line_id": "2027E_revenue", "period": "2027E", "metric": "revenue", "value": 20000, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "2028E_revenue", "period": "2028E", "metric": "revenue", "value": 30000, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "2028E_gross_margin", "period": "2028E", "metric": "gross_margin", "value": 40, "unit": "%", "status": "estimated"},
            {"line_id": "2028E_cost", "period": "2028E", "metric": "costofsales", "value": 1, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "2028E_operating_profit", "period": "2028E", "metric": "operatingprofit", "value": 15000, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "2028E_operating_margin", "period": "2028E", "metric": "operatingmargin", "value": 1, "unit": "%", "status": "estimated"},
            {"line_id": "2028E_net_margin", "period": "2028E", "metric": "netmargin", "value": 1, "unit": "%", "status": "estimated"},
            {"line_id": "2028E_profit", "period": "2028E", "metric": "parent_net_profit", "value": 12000, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "2028E_ocf", "period": "2028E", "metric": "ocf", "value": 13000, "unit": "CNY mn", "status": "estimated"},
            {"line_id": "2028E_capex", "period": "2028E", "metric": "capex", "value": 3000, "unit": "CNY mn", "status": "estimated"},
        ],
        "company_disaggregation": "Company economics.", "industry_cycle_and_competition": "Industry cycle.",
        "forecast_assumptions": [
            {
                "parameter": "FY28E revenue growth",
                "affected_business": "group",
                "historical_anchor": "FY27E canonical revenue",
                "evidence_status": "analyst_estimate",
                "base_case": "+20%",
                "bull_case": "+60%",
                "bear_case": "+10%",
                "rationale_and_evidence": "capacity ramp",
                "sensitivity": "1pp",
                "confidence": "medium",
                "verification_gate": "FY28 filing",
            }
        ],
        "autonomous_forecast_model": "FY28E revenue growth is +20% on capacity ramp.",
        "thesis_financial_bridge": (
            "AI收入占比60% × AI毛利率36% + 非AI收入占比40% × 非AI毛利率27% "
            "→ 综合毛利率34.0% → FY26E净利润。"
        ),
        "moat_evidence_scorecard": "Moat evidence.",
        "valuation_closure": "Method limits.\n- 概率加权股权价值 = 999亿元，预期收益2.7%。",
        "accounting_and_capital_allocation": "Accounting quality.",
        "expectation_gap_and_market_pricing": "Expectation gap.",
        "risks_catalysts_verification": (
            "首仓40%已于126元附近建立。Risk and verification.\n"
            "- 股价低于240元可以启动分批建仓。"
        ),
        "handoff_change_rows": [
            {
                "line_id": "2028E_ocf_to_ni_ratio",
                "old_value": 1.6,
                "new_value": 1.4,
                "unit": "ratio",
                "evidence_ids": ["EV-CASH"],
                "reason": "working-capital risk",
                "eps_fcf_valuation_impact": "recalculate OCF and FCF",
                "disposition": "accepted",
            }
        ],
        "handoff_integrity_audit": "Preserved.", "shared_model_change_audit": "No silent changes.",
        "report_quality_self_check": "Checked.",
        "business_model_mechanisms": [
            {
                "link": "customer purchase",
                "how_it_works": "project owner selects a bankable system supplier",
                "economic_driver": "tender win rate and project ASP",
                "cash_and_capital_feature": "advance payment, delivery and collection cycle",
                "evidence_or_gap": "reported contract liabilities; collection period missing",
                "analyst_conclusion": "order quality depends on delivery and cash conversion",
            }
        ],
        "moat_mechanisms": [
            {
                "moat_source": "bankability and service network",
                "operating_mechanism": "reduces project financing and downtime risk",
                "observed_proof": "repeat orders and true-peer win rate",
                "economic_result": "share and margin resilience",
                "durability_and_threat": "local competitors and price pressure",
                "verdict": "partial",
            }
        ],
        "sell_side_expectation_matrix": [
            {
                "source_ids": ["KSI01", "KPE01"],
                "institution": "中信证券",
                "published_at": "2026-07-01",
                "observation_type": "single_broker",
                "forecast_and_valuation": "2028E EPS 6.2元，给予22倍PE",
                "revision_or_dispersion": "EPS较前次上调5%",
                "comparison_with_our_model": "高于本模型2028E EPS 6.0元约3.3%",
                "evidence_status": "private_text",
                "decision_use": "仅作基准情景交叉验证",
            }
        ],
        "safe_valuation_assumptions": {
            "current_price_cny": 126.16, "required_annual_return_pct": 20,
            "holding_period_years": 1, "margin_of_safety_pct": 20, "maximum_bear_loss_pct": 15,
            "optionality_inputs": [
                {
                    "name": "AIDC SST",
                    "metric_name": "2029E revenue",
                    "metric_value_cny_mn": 5000,
                    "valuation_multiple": 1,
                    "probability_pct": 20,
                    "ownership_pct": 100,
                    "execution_haircut_pct": 0,
                    "assumption_summary": "first commercial order remains unverified",
                    "evidence_ids": ["KPE01"],
                },
                {
                    "name": "Bull volume increment",
                    "metric_name": "incremental_equity_value",
                    "metric_value_cny_mn": 3000,
                    "valuation_multiple": 1,
                    "probability_pct": 50,
                    "ownership_pct": 100,
                    "execution_haircut_pct": 0,
                    "assumption_summary": "Bull versus Base volume increment already in scenarios",
                    "evidence_ids": ["KPE02"],
                }
            ],
            "scenarios": [
                {"scenario": "bull", "probability_pct": 20, "valuation_method": "PE", "parent_net_profit_cny_mn": 12000, "valuation_multiple": 22, "assumption_summary": "bull"},
                {"scenario": "base", "probability_pct": 60, "valuation_method": "PE", "parent_net_profit_cny_mn": 10000, "valuation_multiple": 20, "assumption_summary": "base"},
                {"scenario": "bear", "probability_pct": 20, "valuation_method": "PE", "parent_net_profit_cny_mn": 8000, "valuation_multiple": 19.25, "assumption_summary": "bear"},
            ],
        },
    }

    decision, notes = normalize_sell_side_pm_decision(payload)
    line_map = {(row.period, row.metric): row for row in decision.canonical_model_snapshot}

    assert round(line_map[("2028E", "eps")].value, 2) == 6.00
    assert line_map[("2028E", "costofsales")].value == 18000
    assert line_map[("2028E", "operatingmargin")].value == 50
    assert line_map[("2028E", "netmargin")].value == 40
    assert line_map[("2028E", "ocf")].value == 16800
    assert line_map[("2028E", "ocf")].status == "calculated"
    assert line_map[("2028E", "fcf")].value == 13800
    assert decision.deterministic_valuation.status == "closed"
    assert round(decision.deterministic_valuation.optionality_per_share_cny, 2) == 0.50
    assert decision.deterministic_valuation.optionality_rows[0]["equity_value_cny_mn"] == 1000
    assert len(decision.deterministic_valuation.optionality_rows) == 1
    assert round(decision.deterministic_valuation.safe_buy_price_ceiling_cny, 2) == 80.00
    assert any("added deterministic 2028E EPS" in note for note in notes)
    assert any("excluded overlapping optionality" in note for note in notes)
    assert any("reconciled 2028E revenue growth assumption to +50.0%" in note for note in notes)
    assert any("public revenue growth claim" in note for note in notes)
    assert any("unreconciled segment margin bridge" in note for note in notes)
    assert any("added deterministic probability-weighted core equity value" in note for note in notes)
    assert any("synchronized total fair value per share" in note for note in notes)
    assert any("manual deterministic valuation" in note for note in notes)
    assert any("unsafe buy/build" in note for note in notes)
    weighted_line = next(
        row for row in decision.canonical_model_snapshot
        if row.line_id == "probability_weighted_core_value"
    )
    assert weighted_line.value == 203600
    base_line = next(
        row for row in decision.canonical_model_snapshot
        if row.line_id == "base_fair_value"
    )
    assert base_line.value == 200000
    fair_value_line = next(
        row for row in decision.canonical_model_snapshot
        if row.line_id == "fair_value_per_share"
    )
    assert round(fair_value_line.value, 2) == 102.30
    assert decision.forecast_assumptions[0].base_case.startswith("+50.0%")
    assert "+50.0%" in decision.autonomous_forecast_model
    assert "+20%" not in decision.autonomous_forecast_model
    assert "分部毛利率桥已撤销" in decision.thesis_financial_bridge
    assert "综合毛利率34.0% →" not in decision.thesis_financial_bridge
    assert "高于程序化安全买入上限" in decision.rating_posture
    assert "首仓40%" not in decision.risks_catalysts_verification
    assert "240元" not in decision.risks_catalysts_verification
    assert "999亿元" not in decision.valuation_closure
    normalized_twice, _ = normalize_sell_side_pm_decision(decision)
    assert normalized_twice.risks_catalysts_verification.count("程序化执行约束") == 1
    rendered = render_sell_side_pm_decision(decision)
    assert "| 基准 |" in rendered
    assert "incremental_equity_value" not in rendered
    assert "安全买入价上限：80元" in rendered
    assert "安全买入价上限的计算公式为" in rendered
    assert "min(83.33元，80元，90.59元) = 80元" in rendered
    assert "不等同于目标价、综合公允价值或评级锚" in rendered
    assert "期权价值：0.5元/股" in rendered
    assert "程序化期权价值" in rendered
    assert "AIDC SST" in rendered
    assert "卖方预测、估值与预期差" in rendered
    assert "KSI01/KPE01" in rendered
    assert "单家机构" in rendered
    assert "私域文字信息" in rendered
    assert "single_broker" not in rendered
    assert "商业模式如何运转" in rendered
    assert "护城河的形成机制与经济结果" in rendered
    assert "另类信息增量（知识星球）" not in rendered
    assert "程序化公允价值" not in rendered.split("## 一、投资结论", 1)[0]


def test_handoff_check_detects_only_undocumented_material_changes():
    manager = {
        "canonical_model_snapshot": [
            {"line_id": "shares", "value": 1000, "unit": "mn shares"},
            {"line_id": "2027e_eps", "value": 2.0, "unit": "CNY/share"},
        ]
    }
    pm = {
        "canonical_model_snapshot": [
            {"line_id": "shares", "value": 1000, "unit": "mn shares"},
            {"line_id": "2027e_eps", "value": 2.2, "unit": "CNY/share"},
        ],
        "handoff_change_rows": [],
    }

    assert _canonical_handoff_issues(manager, pm) == [
        "silent change 2027e_eps: 2.0 cny/share -> 2.2 cny/share"
    ]
    pm["handoff_change_rows"] = [
        {"line_id": "2027e_eps", "disposition": "accepted"}
    ]
    assert _canonical_handoff_issues(manager, pm) == []


def test_handoff_check_accepts_raw_shares_to_million_shares_normalization():
    manager = {
        "canonical_model_snapshot": [
            {
                "line_id": "diluted_shares",
                "metric": "Diluted Shares",
                "value": 701_745_100,
                "unit": "shares",
            }
        ]
    }
    pm = {
        "canonical_model_snapshot": [
            {
                "line_id": "diluted_shares",
                "metric": "Diluted Shares",
                "value": 701.7451,
                "unit": "mn shares",
            }
        ],
        "handoff_change_rows": [],
    }

    assert _canonical_handoff_issues(manager, pm) == []
    merged, notes = _merge_manager_canonical_snapshot(manager, pm)
    assert notes == []
    assert merged["canonical_model_snapshot"][0]["value"] == 701_745_100


def test_pm_deterministically_restores_omitted_canonical_lines_and_changes():
    manager = {
        "canonical_model_snapshot": [
            {"line_id": "2027E_revenue", "value": 32300, "unit": "CNY mn"},
            {"line_id": "2027E_grossmargin", "value": 33.5, "unit": "%"},
        ]
    }
    pm = {
        "canonical_model_snapshot": [
            {"line_id": "2027E_revenue", "value": 40000, "unit": "CNY mn"},
            {"line_id": "2027E_eps", "value": 6.4, "unit": "CNY/share"},
        ],
        "handoff_change_rows": [],
    }

    merged, notes = _merge_manager_canonical_snapshot(manager, pm)
    rows = {row["line_id"]: row for row in merged["canonical_model_snapshot"]}

    assert rows["2027E_revenue"]["value"] == 32300
    assert rows["2027E_grossmargin"]["value"] == 33.5
    assert rows["2027E_eps"]["value"] == 6.4
    assert "restored undocumented canonical change 2027e_revenue" in notes
    assert "restored omitted canonical line 2027e_grossmargin" in notes
    assert _canonical_handoff_issues(manager, merged) == []


def test_pm_merge_keeps_explicitly_accepted_canonical_change():
    manager = {
        "canonical_model_snapshot": [
            {"line_id": "2027E_revenue", "value": 32300, "unit": "CNY mn"},
        ]
    }
    pm = {
        "canonical_model_snapshot": [
            {"line_id": "2027E_revenue", "value": 34500, "unit": "CNY mn"},
        ],
        "handoff_change_rows": [
            {"line_id": "2027E_revenue", "disposition": "accepted"},
        ],
    }

    merged, notes = _merge_manager_canonical_snapshot(manager, pm)

    assert merged["canonical_model_snapshot"][0]["value"] == 34500
    assert notes == []


def test_handoff_check_allows_program_recalculated_ocf():
    manager = {
        "canonical_model_snapshot": [
            {"line_id": "2027e_ocf", "value": 158200, "unit": "CNY mn"},
        ]
    }
    pm = {
        "canonical_model_snapshot": [
            {
                "line_id": "2027e_ocf",
                "value": 154420,
                "unit": "CNY mn",
                "status": "calculated",
                "formula": "OCF = parent net profit x accepted OCF/NI ratio (1.4x)",
            },
        ],
        "handoff_change_rows": [],
    }

    assert _canonical_handoff_issues(manager, pm) == []


def test_handoff_check_allows_program_recalculated_total_fair_value():
    manager = {
        "canonical_model_snapshot": [
            {"line_id": "fair_value_per_share", "value": 134, "unit": "CNY/share"},
        ]
    }
    pm = {
        "canonical_model_snapshot": [
            {
                "line_id": "fair_value_per_share",
                "value": 159.5,
                "unit": "CNY/share",
                "status": "calculated",
                "formula": "deterministic total fair value per share",
            },
        ],
        "handoff_change_rows": [],
    }

    assert _canonical_handoff_issues(manager, pm) == []


def test_research_manager_handoff_requires_every_line_or_documented_change():
    packet = {
        "company_model": {"diluted_share_count_mn": 1000},
        "forecast_years": ["2026E", "2027E", "2028E"],
        "forecast_lines": [
            {
                "segment": "consolidated",
                "metric": "Revenue",
                "unit": "CNY mn",
                "year_1_value": 100,
                "year_2_value": 110,
                "year_3_value": 120,
            }
        ],
    }
    payload = {
        "canonical_model_snapshot": [
            {
                "line_id": "shares",
                "period": "2026E-2028E",
                "metric": "diluted_shares_outstanding",
                "value": 1000,
                "unit": "mn_shares",
            },
            {
                "line_id": "2026E_revenue",
                "period": "2026E",
                "metric": "consolidated_revenue",
                "value": 95,
                "unit": "CNY_mn",
            },
        ],
        "model_change_rows": [],
    }

    issues = _research_manager_handoff_issues(packet, payload)
    assert any("undocumented change 2026E_revenue" in issue for issue in issues)
    assert any("missing canonical line 2027E_revenue" in issue for issue in issues)
    assert not any("shares" in issue for issue in issues)

    payload["model_change_rows"] = [
        {"line_id": "2026E_revenue", "disposition": "accepted"}
    ]
    payload["canonical_model_snapshot"].extend(
        [
            {
                "line_id": "2027E_revenue", "period": "2027E",
                "metric": "consolidated_revenue", "value": 110, "unit": "CNY_mn",
            },
            {
                "line_id": "2028E_revenue", "period": "2028E",
                "metric": "consolidated_revenue", "value": 120, "unit": "CNY_mn",
            },
        ]
    )
    assert _research_manager_handoff_issues(packet, payload) == []


def test_research_manager_deterministically_copies_omitted_unchanged_lines():
    packet = {
        "company_model": {
            "diluted_share_count_mn": 1000,
            "share_count_period": "2025A",
            "share_count_source_type": "reported",
            "share_count_evidence_id": "EV-SHARES",
        },
        "forecast_years": ["2026E", "2027E", "2028E"],
        "forecast_lines": [
            {
                "segment": "consolidated",
                "metric": "Revenue",
                "unit": "CNY mn",
                "year_1_value": 100,
                "year_2_value": 110,
                "year_3_value": 120,
                "assumption_status": "analyst_estimate",
                "evidence_ids": ["EV-REV"],
                "formula": "volume x ASP",
            }
        ],
    }
    completed, copied = _complete_unchanged_handoff_lines(
        packet,
        {"canonical_model_snapshot": [], "model_change_rows": []},
    )

    assert copied == [
        "shares",
        "2026E_revenue",
        "2027E_revenue",
        "2028E_revenue",
    ]
    assert _research_manager_handoff_issues(packet, completed) == []
    rows = {row["line_id"]: row for row in completed["canonical_model_snapshot"]}
    assert rows["shares"]["status"] == "reported"
    assert rows["2026E_revenue"]["status"] == "estimated"
    assert rows["2026E_revenue"]["evidence_ids"] == ["EV-REV"]
    assert rows["2026E_revenue"]["formula"] == "volume x ASP"


def test_pm_analytical_structure_gaps_trigger_advisory_revision():
    assert _analytical_structure_issues({}) == [
        "analytical structure: company-specific research questions count=0, expected at least 3",
        "analytical structure: evidence-weighted question verdicts count=0, expected at least 3",
        "analytical structure: forecast take-aways count=0, expected at least 2",
        "analytical structure: auditable forecast assumptions count=0, expected at least 3",
        "analytical structure: ranked core theses count=0, expected at least 2",
    ]
    assert _analytical_structure_issues(
        {
            "research_questions": ["q1", "q2", "q3"],
            "question_verdicts": [{}, {}, {}],
            "forecast_takeaways": [{}, {}],
            "forecast_assumptions": [{}, {}, {}],
            "core_theses": [{}, {}],
        }
    ) == []


def test_pm_guidance_gap_triggers_revision_before_publication():
    payload = {
        "research_questions": ["q1", "q2", "q3"],
        "question_verdicts": [{}, {}, {}],
        "forecast_takeaways": [{}, {}],
        "forecast_assumptions": [{}, {}, {}],
        "core_theses": [{}, {}],
        "autonomous_forecast_model": "仅讨论全年预测，没有季度桥接。",
        "safe_valuation_assumptions": {
            "scenarios": [
                {"scenario": "bear", "parent_net_profit_cny_mn": 3500},
                {"scenario": "base", "parent_net_profit_cny_mn": 4185},
                {"scenario": "bull", "parent_net_profit_cny_mn": 7000},
            ]
        },
    }
    guidance = (
        "KSI private sell-side view: H1 parent net profit 5,400 CNY mn.\n\n"
        "## Official Earnings Guidance Override\n\n"
        "2026年半年度业绩预增公告：预计归属于上市公司股东的净利润为"
        "690,000万元左右。"
    )

    issues = _analytical_structure_issues(payload, guidance)

    assert any("H1 parent profit 6900.00 CNY mn" in issue for issue in issues)
    assert any("lacks Q1/Q2/H1/H2/FY bridge" in issue for issue in issues)
    assert any("full-year scenarios below reported H1" in issue for issue in issues)
