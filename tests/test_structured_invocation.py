import json
from types import SimpleNamespace

from pydantic import BaseModel

from tradingagents.agents.schemas import (
    CanonicalModelLine,
    PortfolioRating,
    SellSideEditorialReview,
    SellSidePMDecision,
    render_sell_side_pm_decision,
)
from tradingagents.agents.managers.portfolio_manager import (
    _analytical_structure_issues,
    _canonical_handoff_issues,
)
from tradingagents.agents.managers.research_manager import _research_manager_handoff_issues
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)
from tradingagents.dataflows.pm_report_compaction import split_pm_public_report


class TinyDecision(BaseModel):
    rating: str
    report: str


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

    for heading in (
        "## 一、投资结论与核心矛盾",
        "## 二、公司业务与利润池拆解",
        "## 三、行业周期与竞争格局",
        "## 四、三年盈利及现金流预测",
        "## 五、核心论点、护城河与财务传导",
        "## 六、会计质量与资本配置",
        "## 七、估值、情景与预期收益",
        "## 八、风险、催化剂与验证日历",
    ):
        assert heading in rendered
    public, appendix, moved = split_pm_public_report(rendered)
    assert sum(1 for line in public.splitlines() if line.startswith("## ")) == 8
    assert "Company Disaggregation" not in public
    assert "2026E_revenue" not in public
    assert "预测take-aways" in public
    assert "核心问题裁决" in public
    assert "核心假设与敏感性" in public
    assert "论点1：The cost moat" in public
    assert appendix == ""
    assert moved == []


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
