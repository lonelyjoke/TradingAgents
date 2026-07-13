"""Tests for saved-report parsing used by validation scripts."""

import json

from tradingagents.evaluation.research_validator import (
    audit_context_alignment,
    audit_decision_depth,
    audit_decision_integrity,
    audit_handoff_numeric_consistency,
    audit_canonical_financial_reconciliation,
    audit_pm_unit_scale_arithmetic,
    audit_position_valuation_consistency,
    audit_public_forecast_growth_consistency,
    audit_public_key_number_consistency,
    audit_rating_valuation_consistency,
    audit_report_redundancy,
    audit_public_process_leakage,
    audit_structured_research_usage,
    audit_weighted_margin_arithmetic,
    render_post_generation_audit,
    _extract_rating,
    _extract_section,
    _is_publication_blocker,
    _normalize_rating,
)

_DEEP_BRIDGE_PHRASE = (
    "True operating peers are separated from broad industry screens; substitute "
    "alternatives and relative allocation are compared. Evidence grades are "
    "reported, calculated, estimated, proxy, missing, unverified, and source period. "
    "Bull/base/bear 2026E 2027E 2028E sensitivity assumptions are shown. "
    "Second curve treatment separates scenario value from core value with unit economics, "
    "utilization, capex, cash conversion, control rights, and customer evidence. "
)

_SIX_DEPTH_CONTRACT = """
## Company Disaggregation

The reported core segment is separated from analytical product, channel, geography,
customer group and project units. Each unit states what is disclosed, calculated,
analytical or missing; its revenue and profit driver; cash conversion; evidence period;
growth, gross margin and valuation treatment. No revenue or margin is allocated to an analytical unit when
the filing does not disclose it. Missing channel economics remain a retrieval task.

## Autonomous Three-Year Forecast Model

The independent model covers 2026E, 2027E and 2028E. Unit volume x ASP produces revenue;
revenue x margin less operating expenses produces parent profit; parent profit divided
by diluted shares produces EPS; operating profit plus non-cash items less working capital
produces OCF; OCF less capex produces FCF. Every year includes revenue, gross margin,
parent net profit, EPS, OCF, capex and FCF, with reported facts separated from assumptions.
The unit rows reconcile to the consolidated rows and consensus is only a cross-check.

## Thesis-to-Financial Bridge

For each decisive claim the formula, base assumption, bull assumption and bear assumption
are explicit. The table shows revenue, profit, EPS, FCF or capital, and fair value impact.
Unsupported effects remain missing rather than being described as quantified upside.

## Moat Evidence Scorecard

Scale EV001 and customer stickiness EV002 are rated proven, partial, unproven or rejected using history
and true peer evidence. Counterevidence is shown, together with transmission to market share,
margin, cash conversion and ROIC. Management claims without observable evidence are unproven.

## Valuation Closure

Core, scenario, optionality and excluded buckets are mutually exclusive. The bridge shows
current price, diluted share count, per share value, probability weights, ownership and
haircut, expected return and rating consistency. Double counting is checked before fair value
is published, including acquired businesses already captured by consolidated earnings.

## Handoff Integrity Audit

Model version v2 is preserved. All business units, 2026E/2027E/2028E forecast lines, thesis
bridges and valuation buckets were preserved. Any revised old value and new value carries an
evidence id and recalculated impact. Unresolved cells remain explicit in the final handoff.

"""


def test_missing_inputs_and_lineage_gaps_are_review_only():
    for section in (
        "underwriting_readiness",
        "period_comparator_lineage",
        "sell_side_expectation_lineage",
    ):
        assert not _is_publication_blocker(section, "error")

    assert _is_publication_blocker("handoff_numeric_consistency", "error")
    assert _is_publication_blocker("scenario_probability_math", "error")


def test_audit_decision_depth_flags_missing_buy_side_sections():
    issues = audit_decision_depth(
        "**Investment Thesis**: The company is good and valuation is fair.\n\n"
        "**Verification & Falsification**: Keep watching."
    )
    sections = {issue.section for issue in issues}

    assert "business_segment_breakdown" in sections
    assert "peer_comparison_summary" in sections
    assert "valuation_expectation" in sections
    assert "verification_and_falsification" in sections
    assert "key_data_check" in sections
    assert "expectation_gap_evidence" in sections
    assert "underwriting_modules" in sections
    assert "filing_internal_quality" in sections
    assert "verification_calendar" in sections
    assert "true_peer_alternatives" in sections
    assert "evidence_grade_table" in sections
    assert "company_disaggregation" in sections
    assert "autonomous_forecast_model" in sections
    assert "thesis_financial_bridge" in sections
    assert "moat_evidence_scorecard" in sections
    assert "valuation_closure" in sections


def test_audit_decision_depth_flags_shallow_medical_device_gate():
    issues = audit_decision_depth(
        "**Investment Thesis**: Business Segment Breakdown: 医疗器械 IVD 平台收入增长很好，"
        "Peer Comparison Summary: peer rank, comparable valuation, ROE, margin, growth, leverage.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash flow falls; "
        "downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, hold if stable, "
        "trim on weak cash flow, downgrade and exit on failed evidence."
    )
    sections = {issue.section for issue in issues}

    assert "medical_device_evidence_gate" in sections
    assert "medical_device_follow_up_questions" in sections


def test_audit_decision_depth_accepts_rich_buy_side_sections():
    text = _SIX_DEPTH_CONTRACT + (
        "**Investment Thesis**: Business Segment Breakdown: core business revenue, "
        "growth, gross margin, net margin, profit, cash conversion, valuation, "
        "and not disclosed second-curve economics are discussed. "
        "Peer Comparison Summary: peer rank, comparable universe, valuation, ROE, "
        "margin, growth, leverage, and allocation impact are discussed. "
        "Market-implied expectation: current PE multiple implied EPS and ROE recovery, "
        "but cash flow must confirm. Key data check: reconcile revenue, net profit, "
        "EPS, market cap, PE, PB, operating cash flow, capex, and contract liabilities. "
        "Expectation-gap evidence: valuation percentile, price-EPS decomposition, "
        "consensus, holder behavior, technical action, and investor interaction. "
        "Filing internal quality review: accounting reconciliation, segment economics, "
        "footnote radar, cash-flow quality, capex CIP return bridge, MD&A text change, "
        "non-recurring profit, balance-sheet forward signals, shareholder-return "
        "authenticity, and disclosure quality are integrated into risk and valuation. "
        f"{_DEEP_BRIDGE_PHRASE}"
        "Unit-economics bridge: platform GMV x take rate x margin; breakeven not disclosed. "
        "Project ramp capacity bridge: occupancy and utilization drive capex ROIC. "
        "Financing / listing scenario: use of proceeds and dilution are tested.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash "
        "flow falls; downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, "
        "hold if stable, trim on weak cash flow, downgrade and exit on failed evidence."
    )

    assert audit_decision_depth(text) == []


def test_audit_decision_depth_accepts_medical_device_gate_depth():
    text = _SIX_DEPTH_CONTRACT + (
        "**Investment Thesis**: Business Segment Breakdown: medical device IVD reagent "
        "platform revenue, growth, gross margin, net margin, profit, cash conversion, "
        "valuation, and not disclosed second-curve economics are discussed. "
        "Peer Comparison Summary: peer rank, comparable universe, valuation, ROE, "
        "margin, growth, leverage, and allocation impact are discussed. "
        "Medical-device evidence gate: installed base, replacement cycle, tender, "
        "procurement, VBP, registration, FDA, CE, NMPA, channel inventory, "
        "distributor, reagent pull-through, service attach, segment gross margin, "
        "receivables, inventory, contract liabilities, cash conversion, and SOTP are "
        "answered. Company-specific follow-up questions are carried into research gaps, "
        "conviction cap, sizing, and verification calendar. Market-implied expectation: "
        "current PE multiple implied EPS and ROE recovery, but cash flow must confirm. "
        "Key data check: reconcile revenue, net profit, EPS, market cap, PE, PB, "
        "operating cash flow, capex, and contract liabilities. Expectation-gap evidence: "
        "valuation percentile, price-EPS decomposition, consensus, holder behavior, "
        "technical action, and investor interaction. Filing internal quality review: "
        "accounting reconciliation, segment economics, footnote radar, cash-flow quality, "
        "capex CIP return bridge, MD&A text change, non-recurring profit, balance-sheet "
        "forward signals, shareholder-return authenticity, and disclosure quality are "
        f"integrated. {_DEEP_BRIDGE_PHRASE}Unit-economics bridge: platform GMV x take rate x margin; breakeven "
        "not disclosed. Project ramp capacity bridge: occupancy and utilization drive "
        "capex ROIC. Financing / listing scenario: use of proceeds and dilution are tested.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash "
        "flow falls; downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, "
        "hold if stable, trim on weak cash flow, downgrade and exit on failed evidence."
    )

    assert audit_decision_depth(text) == []


def test_audit_decision_depth_flags_shallow_battery_material_gate():
    issues = audit_decision_depth(
        "**Investment Thesis**: Business Segment Breakdown: 磷酸铁锂正极材料 公司毛利改善。"
        "Peer Comparison Summary: peer rank, comparable valuation, ROE, margin, growth, leverage.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash flow falls; "
        "downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, hold if stable, "
        "trim on weak cash flow, downgrade and exit on failed evidence."
    )
    sections = {issue.section for issue in issues}

    assert "battery_material_evidence_gate" in sections
    assert "battery_material_driver_bridge" in sections


def test_audit_decision_depth_accepts_battery_material_gate_depth():
    text = _SIX_DEPTH_CONTRACT + (
        "**Investment Thesis**: Business Segment Breakdown: 磷酸铁锂正极材料 revenue, "
        "growth, gross margin, net margin, profit, cash conversion, valuation, and "
        "not disclosed second-curve economics are discussed. Peer Comparison Summary: "
        "peer rank, comparable universe, valuation, ROE, margin, growth, leverage, "
        "and allocation impact are discussed. Battery-material evidence gate: ASP, "
        "lithium carbonate, processing fee, spread, pass-through, capacity utilization, "
        "shipment, customer mix, CATL, BYD, contract liabilities, receivables, "
        "inventory, OCF, credit impairment, and capex are tested. KPI evidence gate "
        "feeds the forecast driver bridge and verification calendar; unresolved "
        "research gap items cap conviction and sizing. Market-implied expectation: "
        "current PE multiple implied EPS and ROE recovery, but cash flow must confirm. "
        "Key data check: reconcile revenue, net profit, EPS, market cap, PE, PB, "
        "operating cash flow, capex, and contract liabilities. Expectation-gap evidence: "
        "valuation percentile, price-EPS decomposition, consensus, holder behavior, "
        "technical action, and investor interaction. Filing internal quality review: "
        "accounting reconciliation, segment economics, footnote radar, cash-flow quality, "
        "capex CIP return bridge, MD&A text change, non-recurring profit, balance-sheet "
        "forward signals, shareholder-return authenticity, and disclosure quality are "
        f"integrated. {_DEEP_BRIDGE_PHRASE}Unit-economics bridge: volume x ASP less lithium carbonate cost "
        "and processing fee; breakeven not disclosed. Project ramp capacity bridge: "
        "occupancy and utilization drive capex ROIC. Financing / listing scenario: use "
        "of proceeds and dilution are tested.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash "
        "flow falls; downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, "
        "hold if stable, trim on weak cash flow, downgrade and exit on failed evidence."
    )

    assert audit_decision_depth(text) == []


def test_audit_decision_depth_flags_project_order_report_without_full_bridge():
    issues = audit_decision_depth(
        "**Investment Thesis**: Business Segment Breakdown: project revenue, growth, gross margin, "
        "net margin, profit, cash conversion, valuation. Peer Comparison Summary: peer rank, comparable "
        "valuation, ROE, margin, growth, leverage. The thesis depends on overseas orders, backlog, "
        "contract liabilities and project delivery. Valuation uses PE and EPS but only one case.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash flow falls; "
        "downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, hold if stable, "
        "trim on weak cash flow, downgrade and exit on failed evidence."
    )
    sections = {issue.section for issue in issues}

    assert "order_backlog_bridge" in sections
    assert "true_peer_alternatives" in sections
    assert "scenario_sensitivity_bridge" in sections
    assert "evidence_grade_table" in sections


def test_audit_decision_depth_accepts_project_order_bridge_depth():
    text = _SIX_DEPTH_CONTRACT + (
        "**Investment Thesis**: Business Segment Breakdown: project revenue, growth, gross margin, "
        "net margin, profit, cash conversion, valuation are discussed. Peer Comparison Summary: "
        "peer rank, comparable universe, valuation, ROE, margin, growth, leverage, and allocation "
        f"impact are discussed. {_DEEP_BRIDGE_PHRASE}Key data check: reconcile revenue, net profit, "
        "EPS, market cap, PE, PB, operating cash flow, capex, and contract liabilities. "
        "Order bridge: opening backlog + new orders - delivered orders = ending backlog; "
        "receivables, inventory, goods shipped, and cash collection reconcile delivery quality. "
        "Market-implied expectation: current PE multiple implied EPS and ROE recovery, but cash flow "
        "must confirm. Expectation-gap evidence: valuation percentile, price-EPS decomposition, "
        "consensus, holder behavior, technical action, and investor interaction. Filing internal "
        "quality review: accounting reconciliation, segment economics, footnote radar, cash-flow "
        "quality, capex CIP return bridge, MD&A text change, non-recurring profit, balance-sheet "
        "forward signals, shareholder-return authenticity, and disclosure quality are integrated. "
        "Unit-economics bridge: project ASP x delivered volume x margin. Project ramp capacity "
        "bridge: utilization and capex ROIC are tested. Financing / listing scenario: use of "
        "proceeds and dilution are tested.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash flow falls; "
        "downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, hold if stable, "
        "trim on weak cash flow, downgrade and exit on failed evidence."
    )

    assert audit_decision_depth(text) == []


def test_audit_context_alignment_flags_wind_lithium_playbook_mismatch(tmp_path):
    context_dir = tmp_path / "0_context"
    context_dir.mkdir()
    (context_dir / "company_business_model.md").write_text(
        "公司主营海上风电装备、塔筒、管桩、导管架和海外海工订单。",
        encoding="utf-8",
    )
    (context_dir / "industry_kpi.md").write_text(
        "Playbook: battery / energy-storage chain\nRequired KPI Map: lithium carbonate, power battery GWh.",
        encoding="utf-8",
    )
    (context_dir / "forecast_model.md").write_text(
        "Driver Bridge: Cathode / material revenue, lithium carbonate cost.",
        encoding="utf-8",
    )

    issues = audit_context_alignment(tmp_path)

    assert [issue.section for issue in issues] == ["industry_playbook_alignment"]
    assert issues[0].severity == "error"


def test_audit_context_alignment_flags_telecom_lithium_playbook_mismatch(tmp_path):
    context_dir = tmp_path / "0_context"
    context_dir.mkdir()
    (context_dir / "company_business_model.md").write_text(
        "中国电信为电信运营商，核心变量包括移动用户、宽带、ARPU、天翼云和分红。",
        encoding="utf-8",
    )
    (context_dir / "industry_kpi.md").write_text(
        "Playbook: lithium / metals cycle\nRequired KPI Map: lithium carbonate and battery demand.",
        encoding="utf-8",
    )
    (context_dir / "forecast_model.md").write_text(
        "Driver Bridge: Cathode / material revenue, lithium carbonate cost.",
        encoding="utf-8",
    )

    issues = audit_context_alignment(tmp_path)

    assert [issue.section for issue in issues] == ["industry_playbook_alignment"]
    assert "telecom-operator" in issues[0].issue


def test_post_generation_integrity_catches_period_calendar_and_kpe_failures():
    decision = (
        "盈利预测桥仅列示2026E和2027E。2026年Q1毛利率同比下降1.46pp。"
        "知识星球信息提高牛市概率，但未说明调整幅度。下一个节点为Q2半年报，预计10月发布。"
    )
    earnings = (
        "| driver | latest_signal | change_vs_prior_report | comparison_basis |\n"
        "| --- | --- | --- | --- |\n"
        "| Gross margin | 24.82% | -1.46pp | sequential-report fallback: 20260331 vs 20251231 |"
    )

    sections = {
        issue.section
        for issue in audit_decision_integrity(
            decision,
            earnings_model_context=earnings,
        )
    }

    assert "three_year_forecast_completion" in sections
    assert "financial_calendar_period" in sections
    assert "period_comparator_lineage" in sections
    assert "alternative_intelligence_lineage" in sections


def test_post_generation_integrity_accepts_explicit_chinese_unchanged_kpe_outcome():
    decision = (
        "知识星球 KPE01、KPE02 仅作观察，无模型影响，"
        "不改变模型假设、情景概率、评级或仓位。"
    )

    sections = {issue.section for issue in audit_decision_integrity(decision)}

    assert "alternative_intelligence_transmission" not in sections


def test_period_semantics_does_not_confuse_revenue_threshold_with_profit_ratio():
    decision = (
        "升级信号：H1收入≥500亿元（Q2环比+25%），毛利率≥31%，OCF/净利润≥0.7。\n"
        "下调信号：H1收入<450亿元，或OCF/净利润仍低于0.6。"
    )

    sections = {issue.section for issue in audit_decision_integrity(decision)}

    assert "q2_h1_period_semantics" not in sections


def test_period_semantics_blocks_reused_q2_and_h1_profit_threshold():
    decision = "Q2单季归母净利润低于50亿元则下调；H1归母净利润低于50亿元则下调。"

    sections = {issue.section for issue in audit_decision_integrity(decision)}

    assert "q2_h1_period_semantics" in sections


def test_profit_pe_bridge_accepts_explicit_numeric_share_count_elsewhere():
    decision = (
        "| 指标 | 2026E | 2027E |\n"
        "| --- | ---: | ---: |\n"
        "| EPS | 4.58 | 5.55 |\n\n"
        "基准情景：2027E归母净利润115亿×18倍PE=2070亿元，"
        "约100元/股（20.73亿股）。"
    )

    sections = {issue.section for issue in audit_decision_integrity(decision)}

    assert "profit_pe_per_share_bridge" not in sections


def test_pm_unit_scale_audit_blocks_tenfold_sensitivity_and_scenario(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    payload = {
        "canonical_model_snapshot": [
            {
                "line_id": "2026E_revenue",
                "period": "2026E",
                "metric": "consolidated_revenue",
                "value": 94535,
                "unit": "CNY mn",
            },
            {
                "line_id": "2026E_profit",
                "period": "2026E",
                "metric": "parent_net_profit",
                "value": 11500,
                "unit": "CNY mn",
            },
        ],
        "thesis_financial_bridge": "1pp毛利率下降使税前利润减少约95亿。",
        "autonomous_forecast_model": "牛市：收入9900亿，净利润1250亿。",
        "forecast_assumptions": [
            {"sensitivity": "0.5pp变化约47亿税前利润。"}
        ],
    }
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(payload, ensure_ascii=False), encoding="utf-8"
    )

    issues = audit_pm_unit_scale_arithmetic(tmp_path)

    assert [issue.section for issue in issues] == ["pm_unit_scale_arithmetic"]
    assert "95" in issues[0].issue
    assert "9900" in issues[0].issue


def test_report_redundancy_flags_same_substantive_sentence_three_times():
    sentence = "合同负债转化必须同时带来收入确认、毛利兑现和经营现金回收，否则不能证明订单质量改善"

    issues = audit_report_redundancy("。".join([sentence, sentence, sentence]))

    assert [issue.section for issue in issues] == ["report_redundancy"]


def test_public_process_leakage_flags_internal_checklist_and_kpe_dump():
    labels = "\n".join(
        [
            "**结论：** 修复",
            "**核心证据：** 订单",
            "**最强反证与边界：** 现金差",
            "**财务传导：** 利润",
            "**市场定价：** 未反映",
            "**证伪门：** 毛利率下降",
        ]
    )
    text = labels + "\n### 另类信息增量（知识星球）\nKPE01"

    sections = {issue.section for issue in audit_public_process_leakage(text)}

    assert "public_process_language" in sections
    assert "public_alternative_intelligence_ledger" in sections


def test_integrity_audit_recalculates_forecast_and_valuation_ranges():
    decision = """
营业收入 2026E 2,150-2,200亿；2026E收入增速 8-10%。
收入80亿 × 2.5x PS × 50% = 40-80亿。
30% × (85-95) + 50% × (70-78) + 20% × (55-62) → 74-82。

## Valuation Closure

当前股价 68.41；公允价值 72-80；预期收益约 8-12%。
"""
    earnings = "| latest annual | FY | 20251231 | 203,200,000,000 |"

    sections = {
        issue.section
        for issue in audit_decision_integrity(
            decision,
            earnings_model_context=earnings,
        )
    }

    assert "forecast_growth_arithmetic" in sections
    assert "option_value_arithmetic" in sections
    assert "scenario_weighted_range_math" in sections
    assert "expected_return_range_math" in sections


def test_depth_audit_rejects_verified_moat_without_evidence_lineage():
    decision = """
## Moat Evidence Scorecard

规模成本优势——已验证；份额25%，成本低于同行，传导至毛利率与ROIC。
历史与同行反证尚未发现，但下一期继续核验。
"""

    sections = {issue.section for issue in audit_decision_depth(decision)}

    assert "moat_evidence_lineage" in sections


def test_post_generation_audit_blocks_portfolio_free_text_fallback(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "decision.md").write_text(
        "# PM memo\n\n**Rating**: Hold\n",
        encoding="utf-8",
    )
    (portfolio_dir / "generation_status.json").write_text(
        json.dumps(
            {
                "mode": "free_text_fallback",
                "schema": "SellSidePMDecision",
                "structured_error": "schema validation failed",
            }
        ),
        encoding="utf-8",
    )

    audit = render_post_generation_audit(tmp_path)

    assert "BLOCKED" in audit
    assert "pm_structured_generation" in audit
    assert "blocks formal publication" in audit


def test_post_generation_audit_blocks_research_manager_free_text_fallback(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "decision.md").write_text(
        "# PM memo\n\n**Rating**: Hold\n",
        encoding="utf-8",
    )
    research_dir = tmp_path / "2_research"
    research_dir.mkdir()
    (research_dir / "generation_status.json").write_text(
        json.dumps(
            {
                "mode": "free_text_fallback",
                "schema": "UnderwritingResearchPlan",
                "structured_error": "schema validation failed",
            }
        ),
        encoding="utf-8",
    )

    audit = render_post_generation_audit(tmp_path)

    assert "BLOCKED" in audit
    assert "research_manager_structured_generation" in audit
    assert "canonical debated model handoff is not schema-valid" in audit


def test_handoff_numeric_audit_blocks_silent_pm_change(tmp_path):
    context_dir = tmp_path / "0_context"
    research_dir = tmp_path / "2_research"
    portfolio_dir = tmp_path / "5_portfolio"
    context_dir.mkdir()
    research_dir.mkdir()
    portfolio_dir.mkdir()
    (context_dir / "company_underwriting.json").write_text(
        json.dumps(
            {
                "forecast_years": ["2026E", "2027E", "2028E"],
                "company_model": {
                    "diluted_share_count_mn": 3130.0,
                    "share_count_period": "current",
                },
                "forecast_lines": [
                    {
                        "segment": "consolidated",
                        "metric": "Revenue",
                        "unit": "CNY mn",
                        "year_1_value": 100.0,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    manager = {
        "canonical_model_snapshot": [
            {"line_id": "shares", "period": "current", "metric": "diluted_shares_outstanding", "value": 3130.0, "unit": "mn_shares"},
            {"line_id": "2026E_revenue", "period": "2026E", "metric": "consolidated_revenue", "value": 100.0, "unit": "CNY_mn"},
        ],
        "model_change_rows": [],
    }
    pm = {
        "canonical_model_snapshot": [
            {"line_id": "shares", "period": "current", "metric": "diluted shares", "value": 3130.0, "unit": "mn shares"},
            {"line_id": "2026E_revenue", "period": "2026E", "metric": "revenue", "value": 110.0, "unit": "CNY mn"},
        ],
        "handoff_change_rows": [],
    }
    (research_dir / "canonical_plan.json").write_text(json.dumps(manager), encoding="utf-8")
    (portfolio_dir / "canonical_decision.json").write_text(json.dumps(pm), encoding="utf-8")

    issues = audit_handoff_numeric_consistency(tmp_path)

    assert any(
        issue.section == "handoff_numeric_consistency"
        and "silently changed" in issue.issue
        for issue in issues
    )

    pm["canonical_model_snapshot"][1]["value"] = 100.0
    manager["canonical_model_snapshot"].append(
        {"line_id": "2026E_gross_profit", "period": "2026E", "metric": "gross_profit", "value": 50.0, "unit": "CNY mn"}
    )
    pm["canonical_model_snapshot"].append(
        {
            "line_id": "2026E_gross_profit",
            "period": "2026E",
            "metric": "gross_profit",
            "value": 45.0,
            "unit": "CNY mn",
            "status": "calculated",
            "formula": "revenue x gross margin",
        }
    )
    manager["canonical_model_snapshot"].append(
        {
            "line_id": "probability_weighted_core_value",
            "period": "scenario",
            "metric": "equity_value_weighted",
            "value": 288083.0,
            "unit": "CNY mn",
        }
    )
    pm["canonical_model_snapshot"].append(
        {
            "line_id": "probability_weighted_core_value",
            "period": "scenario",
            "metric": "equity_value_weighted",
            "value": 225250.0,
            "unit": "CNY mn",
            "status": "calculated",
            "formula": "deterministic probability-weighted scenario equity value",
        }
    )
    (research_dir / "canonical_plan.json").write_text(json.dumps(manager), encoding="utf-8")
    (portfolio_dir / "canonical_decision.json").write_text(json.dumps(pm), encoding="utf-8")

    assert not any(
        "silently changed 2026e grossprofit" in issue.issue.lower()
        for issue in audit_handoff_numeric_consistency(tmp_path)
    )
    assert not any(
        "silently changed scenario equityvalueweighted" in issue.issue.lower()
        for issue in audit_handoff_numeric_consistency(tmp_path)
    )


def test_handoff_numeric_audit_accepts_unit_order_and_small_revenue_reconciliation(tmp_path):
    context_dir = tmp_path / "0_context"
    research_dir = tmp_path / "2_research"
    portfolio_dir = tmp_path / "5_portfolio"
    context_dir.mkdir()
    research_dir.mkdir()
    portfolio_dir.mkdir()
    (context_dir / "company_underwriting.json").write_text(
        json.dumps(
            {
                "forecast_years": ["2026E"],
                "forecast_lines": [
                    {
                        "segment": "consolidated",
                        "metric": "Revenue",
                        "unit": "CNY mn",
                        "year_1_value": 220000.0,
                    },
                    {
                        "segment": "consolidated",
                        "metric": "Parent Net Profit",
                        "unit": "CNY mn",
                        "year_1_value": 18700.0,
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    manager = {
        "canonical_model_snapshot": [
            {
                "line_id": "2026E_revenue",
                "period": "2026E",
                "metric": "Revenue",
                "value": 225000.0,
                "unit": "mn CNY",
            },
            {
                "line_id": "2026E_parent_net_profit",
                "period": "2026E",
                "metric": "Parent Net Profit",
                "value": 18700.0,
                "unit": "mn CNY",
            },
        ],
        "model_change_rows": [],
    }
    (research_dir / "canonical_plan.json").write_text(json.dumps(manager), encoding="utf-8")
    (portfolio_dir / "canonical_decision.json").write_text(json.dumps(manager), encoding="utf-8")

    assert audit_handoff_numeric_consistency(tmp_path) == []


def test_post_generation_audit_marks_missing_pm_analytical_spine_review_only(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "decision.md").write_text(
        "# PM\n\n" + "\n\n".join(f"## {index}\n\nbody" for index in range(1, 9)),
        encoding="utf-8",
    )
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "research_questions": [],
                "question_verdicts": [],
                "forecast_takeaways": [],
                "forecast_assumptions": [],
                "core_theses": [],
                "canonical_model_snapshot": [],
                "handoff_change_rows": [],
            }
        ),
        encoding="utf-8",
    )

    audit = render_post_generation_audit(tmp_path)

    assert "pm_analytical_spine" in audit
    assert "pm_analytical_spine | error | review only" in audit


def test_structured_segment_usage_accepts_aliases_and_does_not_treat_all_unknown_weights_as_material(tmp_path):
    context_dir = tmp_path / "0_context"
    context_dir.mkdir()
    bundle = {
        "preprocessing_mode": "llm_semantic_plus_deterministic_validation",
        "preprocessing_notes": [],
        "deterministic_evidence": [{"evidence_id": "EV01"}],
        "underwriting_packet": {"research_readiness": "partial", "company_model": {}},
        "segments": [
            {
                "segment": "汽车零部件 (八大业务板块)",
                "aliases": ["汽车零部件", "八大业务"],
                "revenue_weight_pct": None,
                "revenue_reported_value": None,
            },
            {
                "segment": "车规级制氧",
                "aliases": ["车规制氧", "制氧"],
                "revenue_weight_pct": None,
                "revenue_reported_value": None,
            },
        ],
        "kpe_impacts": [],
        "conflicts": [],
    }
    (context_dir / "structured_research.json").write_text(
        json.dumps(bundle, ensure_ascii=False),
        encoding="utf-8",
    )

    issues = audit_structured_research_usage(
        tmp_path,
        "业务分部包括汽车零部件（主营）以及尚在验证中的车规制氧。",
    )
    sections = {issue.section for issue in issues}

    assert "structured_segment_usage" not in sections


def test_structured_audit_flags_unused_sell_side_expectation_observation(tmp_path):
    context_dir = tmp_path / "0_context"
    portfolio_dir = tmp_path / "5_portfolio"
    context_dir.mkdir()
    portfolio_dir.mkdir()
    bundle = {
        "preprocessing_mode": "llm_semantic_plus_deterministic_validation",
        "preprocessing_notes": [],
        "deterministic_evidence": [],
        "underwriting_packet": {},
        "segments": [],
        "kpe_impacts": [],
        "sell_side_intelligence": [
            {
                "intelligence_id": "KSI01",
                "valuation_facts": "target_price=100",
                "forecast_facts": "2027E EPS 5.0",
            }
        ],
        "conflicts": [],
    }
    (context_dir / "structured_research.json").write_text(
        json.dumps(bundle, ensure_ascii=False), encoding="utf-8"
    )
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {"sell_side_expectation_matrix": [{"source_ids": ["KSI99"]}]},
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    issues = audit_structured_research_usage(tmp_path, "decision")

    assert "sell_side_expectation_usage" in {issue.section for issue in issues}
    assert "sell_side_expectation_lineage" in {issue.section for issue in issues}


def test_structured_audit_rejects_wrong_kpe_paired_with_ksi(tmp_path):
    context_dir = tmp_path / "0_context"
    portfolio_dir = tmp_path / "5_portfolio"
    context_dir.mkdir()
    portfolio_dir.mkdir()
    bundle = {
        "preprocessing_mode": "llm_semantic_plus_deterministic_validation",
        "preprocessing_notes": [],
        "deterministic_evidence": [],
        "underwriting_packet": {},
        "segments": [],
        "kpe_impacts": [],
        "sell_side_intelligence": [
            {"intelligence_id": "KSI01", "evidence_ids": ["KPE02"]}
        ],
        "conflicts": [],
    }
    (context_dir / "structured_research.json").write_text(
        json.dumps(bundle, ensure_ascii=False), encoding="utf-8"
    )
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "sell_side_expectation_matrix": [
                    {"source_ids": ["KSI01", "KPE01"]}
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    issues = audit_structured_research_usage(tmp_path, "decision")

    assert any(
        issue.section == "sell_side_expectation_lineage"
        and issue.severity == "error"
        and "KPE01" in issue.issue
        for issue in issues
    )


def test_structured_audit_accepts_string_kpe_ids_linked_to_ksi(tmp_path):
    context_dir = tmp_path / "0_context"
    portfolio_dir = tmp_path / "5_portfolio"
    context_dir.mkdir()
    portfolio_dir.mkdir()
    bundle = {
        "preprocessing_mode": "llm_semantic_plus_deterministic_validation",
        "preprocessing_notes": [],
        "deterministic_evidence": [],
        "underwriting_packet": {},
        "segments": [],
        "kpe_impacts": [],
        "sell_side_intelligence": [
            {
                "intelligence_id": "KSI01",
                "kpe_ids": "KPE02",
                "forecast_facts": "2027E EPS 5.0",
            }
        ],
        "conflicts": [],
    }
    (context_dir / "structured_research.json").write_text(
        json.dumps(bundle, ensure_ascii=False), encoding="utf-8"
    )
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "sell_side_expectation_matrix": [
                    {"source_ids": ["KSI01", "KPE02"]}
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    issues = audit_structured_research_usage(tmp_path, "decision")

    assert not any(
        issue.section == "sell_side_expectation_lineage"
        and issue.severity == "error"
        for issue in issues
    )


def test_post_generation_integrity_recomputes_scenario_value():
    decision = (
        "| 情景 | 目标价 | 概率 | 期望值贡献 |\n"
        "| --- | --- | --- | --- |\n"
        "| 牛市 | 500 | 40% | 200 |\n"
        "| 基准 | 400 | 40% | 160 |\n"
        "| 熊市 | 250 | 20% | 50 |\n"
        "| 期望价值 | 420 | - | - |"
    )

    sections = {issue.section for issue in audit_decision_integrity(decision)}

    assert "scenario_weighted_value_math" in sections


def test_post_generation_integrity_reconciles_profit_and_eps_share_count():
    decision = (
        "| 驱动因素 | 2025年实际 | 2026E | 2027E |\n"
        "| --- | --- | --- | --- |\n"
        "| 归母净利润（亿元） | 722 | 750-800 | 850-950 |\n"
        "| EPS（元） | 17.07 | 17.5-18.5 | 19-21 |"
    )

    sections = {issue.section for issue in audit_decision_integrity(decision)}

    assert "eps_profit_share_count_consistency" in sections


def test_canonical_financial_reconciliation_catches_income_statement_gap(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    payload = {
        "canonical_model_snapshot": [
            {"period": "2026E", "metric": "revenue", "value": 95000, "unit": "CNY mn"},
            {"period": "2026E", "metric": "gross_margin", "value": 33, "unit": "%"},
            {"period": "2026E", "metric": "gross_profit", "value": 31350, "unit": "CNY mn"},
            {"period": "2026E", "metric": "operating_profit", "value": 18450, "unit": "CNY mn"},
            {"period": "2026E", "metric": "finance_and_other_items", "value": -1140, "unit": "CNY mn"},
            {"period": "2026E", "metric": "income_tax", "value": 2080, "unit": "CNY mn"},
            {"period": "2026E", "metric": "minority_interest", "value": 1210, "unit": "CNY mn"},
            {"period": "2026E", "metric": "parent_net_profit", "value": 10500, "unit": "CNY mn"},
        ]
    }
    (portfolio_dir / "canonical_decision.json").write_text(json.dumps(payload), encoding="utf-8")

    issues = audit_canonical_financial_reconciliation(tmp_path)

    assert "canonical_financial_reconciliation" in {issue.section for issue in issues}


def test_public_key_number_consistency_catches_conflicting_net_cash():
    issues = audit_public_key_number_consistency(
        "Q1净现金166亿元，资产负债表稳健。随后测算Q1净现金246.8亿元。"
    )

    assert [issue.section for issue in issues] == ["public_key_number_consistency"]


def test_public_key_number_consistency_does_not_treat_current_value_as_current_price():
    issues = audit_public_key_number_consistency(
        "当前价68.71元。新材料期权的当前价值约为每股0.3元。"
    )

    assert issues == []


def test_public_forecast_growth_must_match_canonical_revenue(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "canonical_model_snapshot": [
                    {"period": "2026E", "metric": "revenue", "value": 27600},
                    {"period": "2027E", "metric": "revenue", "value": 32300},
                ]
            }
        ),
        encoding="utf-8",
    )

    issues = audit_public_forecast_growth_consistency(
        tmp_path,
        "FY27E收入增速下调至+25%，反映产能慢速爬坡。",
    )

    assert [issue.section for issue in issues] == [
        "public_forecast_growth_consistency"
    ]
    assert "17.0%" in issues[0].issue


def test_weighted_margin_equation_is_recalculated():
    issues = audit_weighted_margin_arithmetic(
        "AI收入占比60% × AI毛利率36% + 非AI收入占比40% × 非AI毛利率27% → 综合毛利率34.0%。"
    )

    assert [issue.section for issue in issues] == ["weighted_margin_arithmetic"]
    assert "32.40%" in issues[0].issue


def test_positive_rating_cannot_have_negative_deterministic_return(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "rating": "Buy",
                "deterministic_valuation": {
                    "status": "closed",
                    "expected_return_pct": -12.0,
                },
            }
        ),
        encoding="utf-8",
    )

    issues = audit_rating_valuation_consistency(tmp_path)

    assert [issue.section for issue in issues] == ["rating_valuation_consistency"]
    assert issues[0].severity == "error"


def test_position_instruction_cannot_exceed_deterministic_safe_ceiling(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "deterministic_valuation": {
                    "status": "closed",
                    "safe_buy_price_ceiling_cny": 102.14,
                }
            }
        ),
        encoding="utf-8",
    )

    issues = audit_position_valuation_consistency(
        tmp_path,
        "计划建仓者可在120-130元区域试探性买入。",
    )

    assert [issue.section for issue in issues] == ["position_valuation_consistency"]


def test_initial_position_claim_is_rejected_when_current_price_exceeds_safe_ceiling(tmp_path):
    portfolio_dir = tmp_path / "5_portfolio"
    portfolio_dir.mkdir()
    (portfolio_dir / "canonical_decision.json").write_text(
        json.dumps(
            {
                "safe_valuation_assumptions": {"current_price_cny": 374.51},
                "deterministic_valuation": {
                    "status": "closed",
                    "safe_buy_price_ceiling_cny": 336.07,
                },
            }
        ),
        encoding="utf-8",
    )

    issues = audit_position_valuation_consistency(
        tmp_path,
        "首仓40%已于374.51元附近建立。",
    )

    assert [issue.section for issue in issues] == ["position_valuation_consistency"]


def test_normalize_rating_handles_empty_label_value():
    assert _normalize_rating("") == "Unknown"


def test_extract_rating_handles_chinese_only_rating():
    text = "# Portfolio Manager\n\n**\u8bc4\u7ea7\uff1a\u5356\u51fa**\n\nBody"
    assert _extract_rating(text) == "Sell"


def test_extract_rating_handles_chinese_rating_with_english_alias():
    text = "**\u8bc4\u7ea7\uff1a\u4f4e\u914d\uff08Underweight\uff09**\n**Price: 76**"
    assert _extract_rating(text) == "Underweight"


def test_extract_rating_ignores_prior_rating_without_value():
    text = (
        "**Portfolio Manager Decision**\n\n"
        "**Investment Decision: Underweight**\n\n"
        "**Prior Rating:**\n\n"
        "No prior rating was available."
    )
    assert _extract_rating(text) == "Underweight"


def test_extract_core_bet_from_same_line_chinese_label():
    text = (
        "**\u6838\u5fc3\u5224\u65ad**\uff1a"
        "\u5f53\u524d\u62a5\u4ef7\u9690\u542b\u9ad8\u4f4d\u5546\u54c1"
        "\u4ef7\u683c\u4e0e\u4ea7\u91cf\u52a0\u901f\u7684\u7ec4\u5408\u5047\u8bbe\u3002"
    )
    assert _extract_section(text, ["\u6838\u5fc3\u5224\u65ad"]) == (
        "\u5f53\u524d\u62a5\u4ef7\u9690\u542b\u9ad8\u4f4d\u5546\u54c1"
        "\u4ef7\u683c\u4e0e\u4ea7\u91cf\u52a0\u901f\u7684\u7ec4\u5408\u5047\u8bbe\u3002"
    )


def test_extract_core_bet_from_header_and_next_paragraph():
    text = (
        "**\u6838\u5fc3\u62bc\u6ce8**\n"
        "\n"
        "\u5e02\u573a\u6b63\u5728\u4e3a\u53ef\u6301\u7eed\u76c8\u5229"
        "\u590d\u82cf\u5b9a\u4ef7\uff0c\u4f46\u73b0\u91d1\u8f6c\u6362"
        "\u8d28\u91cf\u4ecd\u9700\u9a8c\u8bc1\u3002\n"
    )
    assert _extract_section(text, ["\u6838\u5fc3\u62bc\u6ce8"]) == (
        "\u5e02\u573a\u6b63\u5728\u4e3a\u53ef\u6301\u7eed\u76c8\u5229"
        "\u590d\u82cf\u5b9a\u4ef7\uff0c\u4f46\u73b0\u91d1\u8f6c\u6362"
        "\u8d28\u91cf\u4ecd\u9700\u9a8c\u8bc1\u3002"
    )
