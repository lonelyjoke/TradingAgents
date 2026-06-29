"""Tests for saved-report parsing used by validation scripts."""

import json

from tradingagents.evaluation.research_validator import (
    audit_context_alignment,
    audit_decision_depth,
    audit_decision_integrity,
    audit_structured_research_usage,
    _extract_rating,
    _extract_section,
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
    text = (
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
    text = (
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
    text = (
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
    text = (
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
