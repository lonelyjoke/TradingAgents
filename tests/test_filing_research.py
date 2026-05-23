from tradingagents.dataflows.filing_research import (
    BusinessModelFinding,
    FilingCoverageAudit,
    FilingTextSignal,
    FinancialRelationInsight,
    GrowthVectorFinding,
    SegmentEconomicsFinding,
    _audit_filing_coverage,
    _answer_questions,
    _build_business_segment_valuation_map,
    _build_business_model_map,
    _build_paragraph_reading_pack,
    _build_industry_reading_pack,
    _build_report_to_report_bridge,
    _detect_report_type,
    _extract_filing_evidence,
    _extract_banking_kpi_pack,
    _extract_deep_reading_excerpts,
    _extract_growth_vectors,
    _extract_segment_economics,
    _extract_material_filing_findings,
    _extract_note_findings,
    _extract_statement_table_signals,
    _extract_textual_filing_signals,
    _distill_filing_insights,
    _infer_financial_relations,
    _promote_core_discussion_items,
    _question_candidates,
    _select_industry_profile,
)


def test_filing_research_extracts_multisided_operating_evidence():
    reports = [
        (
            "2025年年度报告",
            """
            公司在手订单充足，合同负债同比增长。
            公司持续扩产，新增产能项目预计于下半年投产。
            受招投标竞争影响，部分产品价格下降，毛利率承压。
            应收账款增加，经营活动现金流净额下降。
            公司持续推进海外客户导入与新产品研发。
            公司对外担保规模上升，并计提资产减值准备。
            """,
        )
    ]

    evidence = _extract_filing_evidence(reports)
    categories = {item.category for item in evidence}

    assert "demand_visibility" in categories
    assert "capacity_and_capex" in categories
    assert "pricing_and_margin" in categories
    assert "cash_and_working_capital" in categories
    assert "customer_and_geography" in categories
    assert "innovation_and_product" in categories
    assert "balance_sheet_and_risk" in categories


def test_filing_research_caps_snippets_per_category():
    reports = [
        (
            "2025年年度报告",
            "\n".join(
                [
                    "公司新增订单增长。",
                    "公司在手订单增长。",
                    "公司订单储备增长。",
                    "公司中标多个项目。",
                ]
            ),
        )
    ]

    evidence = _extract_filing_evidence(reports, max_per_category=2)
    demand_rows = [item for item in evidence if item.category == "demand_visibility"]

    assert len(demand_rows) == 2


def test_report_type_detection_covers_quarterly_half_year_and_annual():
    assert _detect_report_type("2026年一季度报告") == "quarterly"
    assert _detect_report_type("2025年半年度报告") == "semiannual"
    assert _detect_report_type("2025年年度报告") == "annual"


def test_industry_playbook_selects_wind_power_profile():
    reports = [("2025年年度报告", "公司深耕风电整机、海上风电与大兆瓦机型。")]

    assert _select_industry_profile("金风科技", "电气设备", reports) == "wind_power_equipment"


def test_question_driven_answers_prioritize_industry_questions():
    reports = [
        (
            "2026年一季度报告",
            "新增订单增长，合同负债提升。招投标价格仍有压力，风机毛利率承压。",
        ),
        (
            "2025年年度报告",
            "公司海外业务持续推进，海上风电和大兆瓦机型占比提升。",
        ),
    ]
    questions = _question_candidates("wind_power_equipment")
    answers = _answer_questions(reports, questions)
    answer_ids = {answer.question_id for answer in answers}

    assert "wind_orders" in answer_ids
    assert "wind_pricing" in answer_ids
    assert "wind_mix" in answer_ids


def test_industry_playbook_selects_new_priority_profiles():
    cases = [
        ("江西铜业", "有色金属", "公司拥有铜矿资源储量与冶炼产能。", "metals_mining"),
        ("宁德时代", "电池", "公司动力电池与储能电池出货量增长。", "lithium_battery"),
        (
            "九号公司",
            "摩托车",
            "公司主营智能短交通，覆盖电动两轮车、电动滑板车、全地形车、割草机器人和Segway品牌。",
            "smart_mobility",
        ),
        ("山西汾酒", "白酒", "公司持续优化批价与经销商库存。", "baijiu"),
        ("中国国航", "航空运输", "公司客座率提升，航油成本仍需关注，机队稳步扩张。", "airlines"),
        ("中国平安", "保险", "公司新业务价值与内含价值持续改善。", "insurance"),
    ]

    for company_name, industry, report_text, expected in cases:
        assert (
            _select_industry_profile(company_name, industry, [("2025年年度报告", report_text)])
            == expected
        )


def test_industry_playbook_selects_livestock_hog_before_incidental_environment_mentions():
    reports = [
        (
            "2025年年度报告",
            "公司主营生猪养殖，披露能繁母猪、PSY、仔猪、出栏量和完全成本，同时持续推进环保投入。",
        )
    ]

    assert _select_industry_profile("牧原股份", "畜牧养殖", reports) == "livestock_hog"


def test_question_candidates_include_new_priority_playbooks():
    assert any(q.question_id == "metals_resource_volume" for q in _question_candidates("metals_mining"))
    assert any(q.question_id == "battery_capacity_utilization" for q in _question_candidates("lithium_battery"))
    assert any(q.question_id == "baijiu_channel_inventory" for q in _question_candidates("baijiu"))
    assert any(q.question_id == "airline_traffic_yield" for q in _question_candidates("airlines"))
    assert any(q.question_id == "insurance_nbv" for q in _question_candidates("insurance"))
    assert any(q.question_id == "hog_cycle" for q in _question_candidates("livestock_hog"))
    assert any(q.question_id == "mobility_product_mix" for q in _question_candidates("smart_mobility"))



def test_industry_profile_prefers_power_operator_over_incidental_wind_mentions():
    reports = [("annual", "\u98ce\u7535\u9879\u76ee\u4ec5\u4e3a\u80cc\u666f\u63d0\u53ca")]
    assert _select_industry_profile("\u534f\u946b\u80fd\u79d1", "\u65b0\u578b\u7535\u529b", reports) == "power_operator"


def test_industry_profile_detects_precision_equipment_before_wind_false_positive():
    reports = [("annual", "\u516c\u53f8\u4ece\u4e8b\u592a\u9633\u80fd\u3001\u534a\u5bfc\u4f53\u3001\u663e\u793a\u8bbe\u5907\uff0c\u540c\u65f6\u62ab\u9732\u98ce\u7535\u5ba2\u6237")]
    assert _select_industry_profile("\u8fc8\u4e3a\u80a1\u4efd", "\u4e13\u7528\u673a\u68b0", reports) == "precision_equipment"


def test_material_filing_findings_promote_contracted_new_business():
    reports = [
        (
            "2025年年度报告",
            "公司生产绿色甲醇，同时与马士基、赫伯罗特等国际航运客户签订长期协议，形成产能建设到市场消纳的良性循环。",
        )
    ]

    findings = _extract_material_filing_findings(reports)
    types = {item.finding_type for item in findings}

    assert "contracted-commercialization" in types
    assert "named-customer-validation" in types
    assert "capacity-to-demand-bridge" in types


def test_wind_profile_wins_when_reports_are_clearly_wind_specific():
    reports = [
        (
            "2025年年度报告",
            "公司风电、风机、海上风电业务持续扩张，同时披露部分显示设备客户。",
        )
    ]

    assert _select_industry_profile("金风科技", "电气设备", reports) == "wind_power_equipment"


def test_business_model_map_reads_long_cycle_documents_first():
    reports = [
        ("2026年一季度报告", "营业收入增长63%。"),
        ("2025年年度报告", "公司主营业务为风力发电机组销售，同时披露境外收入与研发投入。"),
    ]

    rows = _build_business_model_map(reports)
    by_lens = {row.lens: row for row in rows}

    assert by_lens["core_revenue_engine"].report_type == "annual"
    assert "主营业务" in by_lens["core_revenue_engine"].evidence


def test_growth_vector_map_stages_contracted_second_curve():
    reports = [
        (
            "2025年年度报告",
            "公司生产绿色甲醇，并与国际航运巨头签订长期协议，形成产能建设到市场消纳的良性循环。",
        )
    ]

    rows = _extract_growth_vectors(reports)
    row = next(item for item in rows if item.vector == "green-fuels")

    assert row.stage == "contracted"


def test_report_bridge_pairs_long_cycle_story_with_quarterly_checkpoint():
    reports = [
        ("2025年年度报告", "公司在手订单持续增长，推进新业务建设。"),
        ("2026年一季度报告", "公司在手订单总计53,934.25MW。"),
    ]

    rows = _build_report_to_report_bridge(reports)
    row = next(item for item in rows if item.topic == "orders_and_visibility")

    assert row.bridge_status == "checkpoint-available"
    assert row.bridge_read == "confirmed"
    assert "年度报告" in row.long_cycle_evidence
    assert "一季度报告" in row.checkpoint_evidence


def test_growth_vector_map_ignores_accounting_noise():
    reports = [
        ("2026年一季度报告", "香港中央结算（代理人）有限公司 境外上市外资。"),
        ("2025年年度报告", "公司海外订单持续增长。"),
    ]

    rows = _extract_growth_vectors(reports)

    assert all("境外上市外资" not in row.evidence for row in rows)
    assert any(row.vector == "overseas-expansion" for row in rows)


def test_deep_reading_excerpts_collect_annual_and_quarterly_sections():
    reports = [
        (
            "2025年年度报告",
            "公司业务概要\n公司主营业务为风机制造。\n经营情况讨论与分析\n报告期内公司海外订单增长。",
        ),
        (
            "2026年一季度报告",
            "主要会计数据和财务指标发生变动的情况及原因\n营业收入同比增长。",
        ),
    ]

    rows = _extract_deep_reading_excerpts(reports)
    sections = {(row.report_type, row.section) for row in rows}

    assert ("annual", "公司业务概要") in sections
    assert ("quarterly", "主要会计数据和财务指标发生变动的情况及原因") in sections



def test_growth_vector_map_rejects_macro_only_policy_mentions():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u56fd\u5bb6\u653f\u7b56\u652f\u6301\u7eff\u8272\u7532\u9187\u548c\u50a8\u80fd\u53d1\u5c55\uff0c\u884c\u4e1a\u5e02\u573a\u7a7a\u95f4\u5e7f\u9614\u3002",
        ),
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u5df2\u5efa\u8bbe\u7eff\u8272\u7532\u9187\u9879\u76ee\uff0c\u5e76\u4e0e\u5ba2\u6237\u7b7e\u8ba2\u957f\u671f\u534f\u8bae\u3002",
        ),
    ]

    rows = _extract_growth_vectors(reports)

    assert all("\u56fd\u5bb6\u653f\u7b56\u652f\u6301" not in row.evidence for row in rows)
    assert any(row.vector == "green-fuels" for row in rows)



def test_growth_vector_map_rejects_policy_reference_lines_without_company_bridge():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "2025\u5e748\u670827\u65e5\uff0c\u56fd\u5bb6\u53d1\u5c55\u6539\u9769\u59d4\u3001\u56fd\u5bb6\u80fd\u6e90\u5c40\u5370\u53d1\u300a\u65b0\u578b\u50a8\u80fd\u89c4\u6a21\u5316\u5efa\u8bbe\u4e13\u9879\u884c\u52a8\u65b9\u6848\u300b\u3002",
        ),
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u5df2\u5efa\u8bbe\u50a8\u80fd\u9879\u76ee\uff0c\u5e76\u4e0e\u5ba2\u6237\u7b7e\u8ba2\u8ba2\u5355\u3002",
        ),
    ]

    rows = _extract_growth_vectors(reports)

    assert all("\u56fd\u5bb6\u53d1\u5c55\u6539\u9769\u59d4" not in row.evidence for row in rows)
    assert any(row.vector == "energy-storage" for row in rows)


def test_capacity_to_demand_bridge_rejects_generic_consumption_line():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u63a8\u8fdb\u5149\u4f0f\u5efa\u7b51\u4e00\u4f53\u5316\u5efa\u8bbe\uff0c\u66f4\u597d\u4fc3\u8fdb\u65b0\u80fd\u6e90\u5c31\u5730\u6d88\u7eb3\u3002",
        )
    ]

    findings = _extract_material_filing_findings(reports)

    assert all(item.finding_type != "capacity-to-demand-bridge" for item in findings)


def test_business_model_map_avoids_header_only_segment_lines():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u5206\u4ea7\u54c1\n\u516c\u53f8\u4e3b\u8425\u4e1a\u52a1\u6309\u4ea7\u54c1\u5206\u4e3a\u98ce\u673a\u9500\u552e\u3001\u98ce\u7535\u573a\u5f00\u53d1\u548c\u98ce\u7535\u670d\u52a1\uff0c\u5176\u4e2d\u98ce\u673a\u9500\u552e\u6536\u5165\u5360\u6bd4\u6700\u9ad8\u3002",
        ),
    ]

    rows = _build_business_model_map(reports)
    by_lens = {row.lens: row for row in rows}

    assert "\u5206\u4ea7\u54c1" not in by_lens["segment_mix"].evidence
    assert "\u98ce\u673a\u9500\u552e" in by_lens["segment_mix"].evidence


def test_business_model_map_does_not_use_customer_table_as_core_engine():
    reports = [
        (
            "2025年年度报告",
            "\n".join(
                [
                    "报告期内公司贸易业务收入占营业收入比例超过 10%的贸易业务前五名销售客户 销售额 1,870,855,566.27",
                    "公司主营业务为智能短交通和服务机器人产品，主要产品包括电动两轮车、电动滑板车、全地形车和割草机器人。",
                ]
            ),
        )
    ]

    rows = _build_business_model_map(reports)
    by_lens = {row.lens: row for row in rows}

    assert "智能短交通" in by_lens["core_revenue_engine"].evidence
    assert "前五名销售客户" not in by_lens["core_revenue_engine"].evidence


def test_segment_economics_pack_extracts_product_and_geography_rows():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u5206\u4ea7\u54c1 \u8425\u4e1a\u6536\u5165 \u8425\u4e1a\u6210\u672c \u6bdb\u5229\u7387\uff08%\uff09\n"
            "\u8305\u53f0\u9152 1,250.00 80.00 93.60 \u540c\u6bd4 12.00%\n"
            "\u7cfb\u5217\u9152 240.00 48.00 80.00 \u540c\u6bd4 11.25%\n"
            "\u5206\u5730\u533a \u5883\u5185 1,320.00 \u5883\u5916 170.00 \u540c\u6bd4 25.00%",
        )
    ]

    rows = _extract_segment_economics(reports)
    evidence = "\n".join(row.evidence for row in rows)

    assert any(row.segment_type == "product" for row in rows)
    assert "\u8305\u53f0\u9152" in evidence
    assert "\u7cfb\u5217\u9152" in evidence
    assert "\u5883\u5916" in evidence


def test_segment_economics_filters_financial_assets_and_customer_tables():
    reports = [
        (
            "2025年年度报告",
            "\n".join(
                [
                    "银行理财产品投资 1,260,163,242.83 2,288,385,549.09 其他权益工具投资 69,134,417.81",
                    "报告期内公司贸易业务收入占营业收入比例超过 10%的贸易业务前五名销售客户 销售额 1,870,855,566.27",
                    "第一季度 第二季度 第三季度 第四季度 营业收入 5,112,484,338.21 6,629,649,256.44 6,647,531,252.20 2,888,211,820.10",
                    "主营业务分产品情况 电动两轮车 营业收入 10,000.00 营业成本 7,000.00 毛利率 30.00 同比 45.00%",
                ]
            ),
        )
    ]

    rows = _extract_segment_economics(reports)
    evidence = "\n".join(row.evidence for row in rows)

    assert "电动两轮车" in evidence
    assert "银行理财产品" not in evidence
    assert "前五名销售客户" not in evidence
    assert "第一季度" not in evidence


def test_business_segment_valuation_map_splits_core_and_new_business():
    business_model_map = [
        BusinessModelFinding(
            lens="core_revenue_engine",
            report_type="annual",
            evidence="2025 annual: 公司主营业务为环保装备及服务，营业收入保持稳定。",
            why_it_matters="Defines the core engine.",
        )
    ]
    segment_economics = [
        # Mature disclosed business.
        SegmentEconomicsFinding(
            segment_type="business",
            report_type="annual",
            evidence="2025 annual: 环保主业 营业收入 100.00 营业成本 75.00 毛利率 25.00 同比 8.00%",
            analyst_use="",
        ),
        # Second curve that should not be blended into the old business.
        SegmentEconomicsFinding(
            segment_type="business",
            report_type="annual",
            evidence="2025 annual: 算力租赁业务 收入 5.00 毛利率 40.00 同比 200.00%",
            analyst_use="",
        ),
    ]
    growth_vectors = [
        GrowthVectorFinding(
            vector="ai-and-digital",
            stage="monetized",
            evidence="2025 annual: 算力租赁业务规模扩大并实现收入。",
            valuation_treatment="eligible for valuation bridge review",
            verification_need="check segment margin and cash conversion",
        )
    ]

    rows = _build_business_segment_valuation_map(
        business_model_map,
        segment_economics,
        growth_vectors,
    )

    assert rows[0].business_bucket == "core_revenue_engine"
    assert any(row.business_bucket == "emerging_or_second_curve" for row in rows)
    assert any("SOTP" in row.valuation_anchor for row in rows)
    assert any("normalized earnings" in row.valuation_anchor for row in rows)



def test_paragraph_reading_pack_collects_cross_report_lenses():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u4e1a\u52a1\u6982\u8981\n\u516c\u53f8\u4e3b\u8425\u4e1a\u52a1\u4e3a\u98ce\u673a\u9500\u552e\uff0c\u540c\u65f6\u5e03\u5c40\u7eff\u8272\u7532\u9187\u65b0\u4e1a\u52a1\u3002\n\u6838\u5fc3\u7ade\u4e89\u529b\u5206\u6790\n\u516c\u53f8\u5177\u5907\u6280\u672f\u548c\u5e02\u573a\u5730\u4f4d\u4f18\u52bf\u3002\n\u91cd\u5927\u98ce\u9669\u63d0\u793a\n\u539f\u6750\u6599\u4ef7\u683c\u6ce2\u52a8\u53ef\u80fd\u5f71\u54cd\u6bdb\u5229\u7387\u3002",
        ),
        (
            "2025\u5e74\u534a\u5e74\u5ea6\u62a5\u544a",
            "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u4e0e\u5206\u6790\n\u516c\u53f8\u6536\u5165\u589e\u957f\uff0c\u6d77\u5916\u8ba2\u5355\u6301\u7eed\u63d0\u5347\u3002",
        ),
        (
            "2026\u5e74\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u4e3b\u8981\u4f1a\u8ba1\u6570\u636e\u548c\u8d22\u52a1\u6307\u6807\u53d1\u751f\u53d8\u52a8\u7684\u60c5\u51b5\u53ca\u539f\u56e0\n\u8425\u4e1a\u6536\u5165\u540c\u6bd4\u589e\u957f\uff0c\u9884\u4ed8\u6b3e\u4e0e\u5e94\u6536\u8d26\u6b3e\u589e\u52a0\u3002",
        ),
    ]

    rows = _build_paragraph_reading_pack(reports)
    lenses = {row.lens for row in rows}

    assert "business_model" in lenses
    assert "second_curve" in lenses
    assert "moat" in lenses
    assert "long_cycle_risk" in lenses
    assert "trend_formation" in lenses
    assert "short_cycle_execution" in lenses


def test_paragraph_reading_pack_prefers_relevant_annual_sections():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u4e1a\u52a1\u6982\u8981\n\u516c\u53f8\u4e3b\u8425\u4e1a\u52a1\u4e3a\u9500\u552e\u4ea7\u54c1\u3002\n\u516c\u53f8\u672a\u6765\u53d1\u5c55\u7684\u5c55\u671b\n\u516c\u53f8\u5df2\u5e03\u5c40\u65b0\u4e1a\u52a1\uff0c\u5e76\u4e0e\u5ba2\u6237\u7b7e\u8ba2\u8ba2\u5355\u3002",
        ),
    ]

    rows = _build_paragraph_reading_pack(reports)
    second_curve = next(row for row in rows if row.lens == "second_curve")

    assert second_curve.section == "\u516c\u53f8\u672a\u6765\u53d1\u5c55\u7684\u5c55\u671b"
    assert "\u5ba2\u6237\u7b7e\u8ba2\u8ba2\u5355" in second_curve.excerpt



def test_paragraph_reading_pack_supports_financial_company_headings():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u53ca\u5206\u6790\n\u96c6\u56e2\u7efc\u5408\u91d1\u878d\u4e1a\u52a1\u5b9e\u73b0\u6536\u5165\u589e\u957f\u3002\n\u672a\u6765\u53d1\u5c55\u5c55\u671b\n\u516c\u53f8\u5c06\u7ee7\u7eed\u5e03\u5c40\u533b\u7597\u517b\u8001\u548c\u79d1\u6280\u8d4b\u80fd\u3002\n\u98ce\u9669\u7ba1\u7406\n\u5229\u7387\u3001\u5e02\u573a\u548c\u4fe1\u7528\u98ce\u9669\u9700\u8981\u6301\u7eed\u5173\u6ce8\u3002",
        ),
        (
            "2026\u5e74\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u5b63\u5ea6\u7ecf\u8425\u5206\u6790\n\u8425\u4e1a\u6536\u5165\u4e0b\u964d\uff0c\u7ecf\u8425\u6d3b\u52a8\u73b0\u91d1\u6d41\u91cf\u51c0\u989d\u4e0b\u964d\u3002",
        ),
    ]

    rows = _build_paragraph_reading_pack(reports)
    lenses = {row.lens for row in rows}

    assert "business_model" in lenses
    assert "second_curve" in lenses
    assert "long_cycle_risk" in lenses
    assert "short_cycle_execution" in lenses



def test_industry_reading_pack_for_wind_prioritizes_backlog_margin_and_second_curve():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u4e3b\u8425\u4e1a\u52a1\u5206\u6790\n\u516c\u53f8\u5728\u624b\u8ba2\u5355\u589e\u957f\uff0c\u6d77\u5916\u8ba2\u5355\u63d0\u5347\uff0c\u7eff\u8272\u7532\u9187\u5df2\u6295\u4ea7\u5e76\u4e0e\u5ba2\u6237\u7b7e\u8ba2\u8ba2\u5355\u3002\n\u516c\u53f8\u672a\u6765\u53d1\u5c55\u7684\u5c55\u671b\n\u516c\u53f8\u5c06\u7ee7\u7eed\u63a8\u8fdb\u50a8\u80fd\u548c\u6d77\u5916\u4e1a\u52a1\u3002",
        ),
        (
            "2026\u5e74\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u4e3b\u8981\u4f1a\u8ba1\u6570\u636e\u548c\u8d22\u52a1\u6307\u6807\u53d1\u751f\u53d8\u52a8\u7684\u60c5\u51b5\u53ca\u539f\u56e0\n\u8425\u4e1a\u6210\u672c\u589e\u52a0\uff0c\u6bdb\u5229\u7387\u627f\u538b\u3002",
        ),
    ]

    rows = _build_industry_reading_pack(reports, "wind_power_equipment")
    lenses = {row.lens for row in rows}

    assert {"backlog_quality", "pricing_margin", "second_curve_monetization"}.issubset(lenses)


def test_industry_reading_pack_for_insurance_reads_value_and_ecosystem():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u53ca\u5206\u6790\n\u65b0\u4e1a\u52a1\u4ef7\u503c\u589e\u957f\uff0c\u533b\u7597\u517b\u8001\u670d\u52a1\u6b63\u6210\u4e3a\u7b2c\u4e8c\u589e\u957f\u66f2\u7ebf\uff0c\u7efc\u5408\u6295\u8d44\u6536\u76ca\u7387\u4fdd\u6301\u7a33\u5065\u3002",
        ),
        (
            "2026\u5e74\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u5b63\u5ea6\u7ecf\u8425\u5206\u6790\n\u65b0\u4e1a\u52a1\u4ef7\u503c\u7ee7\u7eed\u63d0\u5347\u3002",
        ),
    ]

    rows = _build_industry_reading_pack(reports, "insurance")
    lenses = {row.lens for row in rows}

    assert {"franchise_recovery", "investment_spread", "service_ecosystem"}.issubset(lenses)


def test_industry_reading_pack_for_banking_reads_asset_quality_and_spread():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u53ca\u5206\u6790\n\u4e0d\u826f\u8d37\u6b3e\u7387\u4e0b\u964d\uff0c\u62e8\u5907\u8986\u76d6\u7387\u63d0\u5347\uff0c\u51c0\u606f\u5dee\u4ecd\u627f\u538b\uff0c\u624b\u7eed\u8d39\u6536\u5165\u589e\u957f\u3002",
        ),
    ]

    rows = _build_industry_reading_pack(reports, "banking")
    lenses = {row.lens for row in rows}

    assert {"asset_quality", "spread_and_mix"}.issubset(lenses)


def test_banking_profile_wins_over_incidental_metal_and_capex_terms():
    reports = [
        (
            "2026年第一季度报告",
            "本行净息差、净利息收益率、不良贷款率和拨备覆盖率保持行业领先。"
            "金融投资包括债券投资，风险管理中提及贵金属、铜、铝等市场价格风险。",
        )
    ]

    assert _select_industry_profile("招商银行", "银行", reports) == "banking"
    question_ids = {question.question_id for question in _question_candidates("banking")}

    assert {"bank_asset_quality", "bank_nim", "bank_fees", "bank_capital", "bank_retail_book"}.issubset(question_ids)
    assert "generic_cash_conversion" not in question_ids


def test_banking_kpi_pack_extracts_bank_specific_metrics():
    reports = [
        (
            "2026年第一季度报告",
            "净利差1.77%，净利息收益率1.83%。不良贷款率0.94%，拨备覆盖率387.76%。"
            "核心一级资本充足率13.50%，管理零售客户总资产(AUM)较上年末增长。",
        )
    ]

    rows = _extract_banking_kpi_pack(reports)
    lenses = {row["lens"] for row in rows}

    assert {"spread_profitability", "asset_quality", "capital_and_payout", "retail_wealth_engine"}.issubset(lenses)


def test_material_findings_read_across_pdf_line_breaks():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u7eff\u8272\u7532\u9187\u9879\u76ee\u5df2\u6295\u4ea7\uff0c\n"
            "\u5e76\u4e0e\u9a6c\u58eb\u57fa\u3001\u8d6b\u4f2f\u7f57\u7279\u7b7e\u8ba2\u957f\u671f\u534f\u8bae\uff0c\n"
            "\u4e3a\u65b0\u4e1a\u52a1\u63d0\u4f9b\u9700\u6c42\u9501\u5b9a\u3002",
        )
    ]

    findings = _extract_material_filing_findings(reports)
    types = {item.finding_type for item in findings}

    assert "contracted-commercialization" in types
    assert "named-customer-validation" in types
    assert "capacity-to-demand-bridge" in types


def test_question_answers_read_across_pdf_line_breaks():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u5728\u624b\u8ba2\u5355\u6301\u7eed\u589e\u957f\uff0c\n"
            "\u5408\u540c\u8d1f\u503a\u4e0e\u6536\u5165\u786e\u8ba4\u540c\u5411\u6539\u5584\u3002",
        )
    ]

    answers = _answer_questions(reports, _question_candidates("precision_equipment"))
    answer_ids = {item.question_id for item in answers}

    assert "equipment_orders" in answer_ids


def test_filing_coverage_audit_marks_strong_pack():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u4e1a\u52a1\u6982\u8981\n"
            "\u516c\u53f8\u4e3b\u8425\u4e1a\u52a1\u4e3a\u98ce\u673a\u9500\u552e\uff0c\u540c\u65f6\u5e03\u5c40\u7eff\u8272\u7532\u9187\u3002\n"
            "\u516c\u53f8\u672a\u6765\u53d1\u5c55\u7684\u5c55\u671b\n"
            "\u516c\u53f8\u5728\u624b\u8ba2\u5355\u589e\u957f\uff0c\u7eff\u8272\u7532\u9187\u5df2\u6295\u4ea7\u5e76\u4e0e\u5ba2\u6237\u7b7e\u8ba2\u8ba2\u5355\u3002",
        ),
        (
            "2025\u5e74\u534a\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u6d77\u5916\u8ba2\u5355\u63d0\u5347\uff0c\u7ecf\u8425\u8d8b\u52bf\u6539\u5584\u3002",
        ),
        (
            "2026\u5e74\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u4e3b\u8981\u4f1a\u8ba1\u6570\u636e\u548c\u8d22\u52a1\u6307\u6807\u53d1\u751f\u53d8\u52a8\u7684\u60c5\u51b5\u53ca\u539f\u56e0\n"
            "\u516c\u53f8\u5728\u624b\u8ba2\u5355\u589e\u957f\uff0c\u8425\u4e1a\u6536\u5165\u540c\u6bd4\u589e\u957f\uff0c\u6bdb\u5229\u7387\u627f\u538b\u3002",
        ),
    ]
    questions = _question_candidates("wind_power_equipment")
    answers = _answer_questions(reports, questions)
    audit = _audit_filing_coverage(
        report_texts=reports,
        questions=questions,
        answers=answers,
        business_model_map=_build_business_model_map(reports),
        paragraph_reading_pack=_build_paragraph_reading_pack(reports),
        industry_reading_pack=_build_industry_reading_pack(reports, "wind_power_equipment"),
    )

    assert audit.coverage_grade == "strong"
    assert audit.core_pack_status == "ready"
    assert audit.missing_report_types == ()


def test_core_discussion_promotion_queue_prioritizes_investable_findings():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u7eff\u8272\u7532\u9187\u9879\u76ee\u5df2\u6295\u4ea7\uff0c"
            "\u5e76\u4e0e\u9a6c\u58eb\u57fa\u7b7e\u8ba2\u957f\u671f\u534f\u8bae\u3002",
        ),
        (
            "2026\u5e74\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u5728\u624b\u8ba2\u5355\u589e\u957f\uff0c\u6bdb\u5229\u7387\u627f\u538b\u3002",
        ),
    ]
    findings = _extract_material_filing_findings(reports)
    growth = _extract_growth_vectors(reports)
    questions = _question_candidates("wind_power_equipment")
    answers = _answer_questions(reports, questions)
    promoted = _promote_core_discussion_items(
        material_findings=findings,
        growth_vectors=growth,
        answers=answers,
        report_bridge=_build_report_to_report_bridge(reports),
    )

    assert promoted[0].priority == "core"
    assert any(item.topic == "green-fuels" and item.priority == "core" for item in promoted)


def test_statement_table_pack_reads_key_financial_rows():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u5408\u540c\u8d1f\u503a 19,760,000,000.00 11,940,000,000.00\n"
            "\u5e94\u6536\u8d26\u6b3e 33,936,000,000.00 32,300,000,000.00\n"
            "\u957f\u671f\u80a1\u6743\u6295\u8d44 3,560,000,000.00 2,980,000,000.00",
        )
    ]

    rows = _extract_statement_table_signals(reports)
    accounts = {item.account for item in rows}

    assert {"contract_liabilities", "receivables", "long_term_equity_investments"}.issubset(accounts)


def test_note_pack_reads_footnote_risks():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u524d\u4e94\u5927\u5ba2\u6237\u9500\u552e\u989d\u5360\u6bd4 42.5%\n"
            "\u516c\u53f8\u5b58\u5728\u5173\u8054\u65b9\u4ea4\u6613\uff0c\u5e76\u62ab\u9732\u5bf9\u5916\u62c5\u4fdd\u4f59\u989d\u3002",
        )
    ]

    rows = _extract_note_findings(reports)
    note_types = {item.note_type for item in rows}

    assert {"customer_concentration", "related_party", "guarantees"}.issubset(note_types)


def test_core_discussion_queue_promotes_table_and_note_signals():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u5408\u540c\u8d1f\u503a 19,760,000,000.00 11,940,000,000.00\n"
            "\u524d\u4e94\u5927\u5ba2\u6237\u9500\u552e\u989d\u5360\u6bd4 42.5%",
        )
    ]
    promoted = _promote_core_discussion_items(
        material_findings=[],
        growth_vectors=[],
        answers=[],
        report_bridge=[],
        statement_table_signals=_extract_statement_table_signals(reports),
        note_findings=_extract_note_findings(reports),
    )
    by_topic = {item.topic: item for item in promoted}

    assert by_topic["contract_liabilities"].priority == "core"
    assert by_topic["customer_concentration"].priority == "core"


def test_financial_relations_identify_cash_absorbing_growth():
    import pandas as pd

    derived = pd.DataFrame(
        [
            {
                "end_date": "20260331",
                "revenue_base": 160.0,
                "reported_gross_margin": 16.8,
                "derived_operating_margin": 8.0,
                "derived_net_margin": 5.0,
                "ocf_to_net_profit": -1.7,
                "receivables_to_revenue": 55.8,
                "inventory_to_revenue": 27.7,
                "prepayment_to_revenue": 5.0,
                "contract_like_liab": 197.6,
                "debt_to_assets_derived": 60.0,
                "finance_expense_ratio": 1.5,
            },
            {
                "end_date": "20251231",
                "revenue_base": 100.0,
                "reported_gross_margin": 21.8,
                "derived_operating_margin": 10.0,
                "derived_net_margin": 6.0,
                "ocf_to_net_profit": 1.1,
                "receivables_to_revenue": 45.1,
                "inventory_to_revenue": 23.0,
                "prepayment_to_revenue": 2.0,
                "contract_like_liab": 119.4,
                "debt_to_assets_derived": 58.0,
                "finance_expense_ratio": 1.0,
            },
        ]
    )

    rows = _infer_financial_relations(derived)
    relation_types = {item.relation_type for item in rows}

    assert "growth_without_margin" in relation_types
    assert "cash_absorbing_growth" in relation_types
    assert "visibility_not_yet_profitability" in relation_types


def test_financial_relations_identify_quality_growth():
    import pandas as pd

    derived = pd.DataFrame(
        [
            {
                "end_date": "20260331",
                "revenue_base": 120.0,
                "reported_gross_margin": 32.0,
                "derived_operating_margin": 18.0,
                "derived_net_margin": 12.0,
                "ocf_to_net_profit": 1.2,
                "receivables_to_revenue": 18.0,
                "inventory_to_revenue": 12.0,
                "prepayment_to_revenue": 1.0,
                "contract_like_liab": 20.0,
                "debt_to_assets_derived": 30.0,
                "finance_expense_ratio": 0.5,
            },
            {
                "end_date": "20251231",
                "revenue_base": 100.0,
                "reported_gross_margin": 29.0,
                "derived_operating_margin": 15.0,
                "derived_net_margin": 10.0,
                "ocf_to_net_profit": 1.0,
                "receivables_to_revenue": 20.0,
                "inventory_to_revenue": 13.0,
                "prepayment_to_revenue": 1.5,
                "contract_like_liab": 18.0,
                "debt_to_assets_derived": 31.0,
                "finance_expense_ratio": 0.5,
            },
        ]
    )

    rows = _infer_financial_relations(derived)
    relation_types = {item.relation_type for item in rows}

    assert "quality_growth" in relation_types


def test_core_discussion_queue_promotes_financial_relations():
    import pandas as pd

    derived = pd.DataFrame(
        [
            {
                "end_date": "20260331",
                "revenue_base": 160.0,
                "reported_gross_margin": 16.8,
                "derived_operating_margin": 8.0,
                "derived_net_margin": 5.0,
                "ocf_to_net_profit": -1.7,
                "receivables_to_revenue": 55.8,
                "inventory_to_revenue": 27.7,
                "prepayment_to_revenue": 5.0,
                "contract_like_liab": 197.6,
                "debt_to_assets_derived": 60.0,
                "finance_expense_ratio": 1.5,
            },
            {
                "end_date": "20251231",
                "revenue_base": 100.0,
                "reported_gross_margin": 21.8,
                "derived_operating_margin": 10.0,
                "derived_net_margin": 6.0,
                "ocf_to_net_profit": 1.1,
                "receivables_to_revenue": 45.1,
                "inventory_to_revenue": 23.0,
                "prepayment_to_revenue": 2.0,
                "contract_like_liab": 119.4,
                "debt_to_assets_derived": 58.0,
                "finance_expense_ratio": 1.0,
            },
        ]
    )
    relations = _infer_financial_relations(derived)
    promoted = _promote_core_discussion_items(
        material_findings=[],
        growth_vectors=[],
        answers=[],
        report_bridge=[],
        financial_relations=relations,
    )
    by_topic = {item.topic: item for item in promoted}

    assert by_topic["cash_absorbing_growth"].priority == "core"


def test_industry_profile_prefers_lithium_resource_over_incidental_environment_mentions():
    reports = [
        (
            "annual",
            "\u516c\u53f8\u4e3b\u8425\u78b3\u9178\u9502\u3001\u6c22\u6c27\u5316\u9502\u3001\u9502\u8f89\u77f3\u4ee5\u53ca\u76d0\u6e56\u5364\u6c34\u63d0\u9502\uff0c"
            "\u540c\u65f6\u5728\u7ae0\u8282\u4e2d\u63d0\u5230\u73af\u4fdd\u5408\u89c4\u548c\u56de\u6536\u4e1a\u52a1\u3002",
        )
    ]

    assert _select_industry_profile("\u8d63\u950b\u9502\u4e1a", "\u5c0f\u91d1\u5c5e", reports) == "lithium_battery"


def test_industry_profile_keeps_true_environmental_services():
    reports = [
        (
            "annual",
            "\u516c\u53f8\u4e3b\u8425\u73af\u536b\u4e00\u4f53\u5316\u3001\u5783\u573e\u711a\u70e7\u53ca\u73af\u5883\u670d\u52a1\u9879\u76ee\uff0c\u65b0\u589e\u8ba2\u5355\u548c\u5728\u624b\u9879\u76ee\u662f\u6838\u5fc3\u53d8\u91cf\u3002",
        )
    ]

    assert _select_industry_profile("\u67d0\u73af\u5883\u80a1\u4efd", "\u73af\u4fdd", reports) == "environmental_services"


def test_industry_profile_prefers_industrial_components_over_downstream_wind_mentions():
    reports = [
        (
            "annual",
            "\u516c\u53f8\u4e3b\u8425\u7d22\u5177\u3001\u540a\u88c5\u5e26\u3001\u94a2\u4e1d\u7ef3\u548c\u94fe\u6761\u7d22\u5177\uff0c"
            "\u4ea7\u54c1\u5e94\u7528\u4e8e\u6d77\u6d0b\u5de5\u7a0b\u3001\u7535\u529b\u3001\u98ce\u7535\u5ba2\u6237\u548c\u4f53\u80b2\u573a\u9986\u3002",
        )
    ]

    assert _select_industry_profile("\u5de8\u529b\u7d22\u5177", "\u673a\u68b0\u57fa\u4ef6", reports) == "industrial_components"
    assert any(q.question_id == "industrial_order_cash" for q in _question_candidates("industrial_components"))


def test_textual_filing_signals_classify_wording_strength_and_missing_proof():
    reports = [
        (
            "annual",
            "\u516c\u53f8\u5df2\u7b7e\u8ba2\u6d77\u5916\u5ba2\u6237\u8ba2\u5355\u5e76\u5df2\u4ea4\u4ed8\u90e8\u5206\u4ea7\u54c1\u3002\n"
            "\u516c\u53f8\u5c06\u79ef\u6781\u5e03\u5c40\u667a\u80fd\u88c5\u5907\u65b0\u4e1a\u52a1\u3002\n"
            "\u516c\u53f8\u9762\u4e34\u56de\u6b3e\u538b\u529b\u548c\u51cf\u503c\u98ce\u9669\u3002",
        )
    ]
    growth_vectors = [
        GrowthVectorFinding(
            vector="smart-equipment",
            stage="planned",
            evidence="annual: \u516c\u53f8\u5c06\u79ef\u6781\u5e03\u5c40\u667a\u80fd\u88c5\u5907\u65b0\u4e1a\u52a1\u3002",
            valuation_treatment="narrative or early optionality only",
            verification_need="check customers/orders/revenue",
        )
    ]

    rows = _extract_textual_filing_signals(reports, growth_vectors=growth_vectors)
    types = {row.signal_type for row in rows}

    assert "management_claim_with_evidence" in types
    assert "unquantified_strategy_language" in types
    assert "risk_language_upgrade" in types
    assert "watch_missing_monetization" in types


def test_filing_insight_distillation_promotes_story_quality_tension():
    coverage = FilingCoverageAudit(
        coverage_grade="strong",
        report_types_seen=("annual", "quarterly"),
        missing_report_types=("semiannual",),
        answered_question_count=6,
        total_question_count=8,
        core_pack_status="ready",
        confidence_read="Annual base text and quarterly checkpoint are both present.",
    )
    business_model = [
        BusinessModelFinding(
            lens="core_revenue_engine",
            report_type="annual",
            evidence="annual report: main revenue comes from industrial components and project delivery.",
            why_it_matters="Defines what actually drives the income statement.",
        )
    ]
    growth_vectors = [
        GrowthVectorFinding(
            vector="overseas-expansion",
            stage="contracted",
            evidence="annual report: won overseas stadium projects.",
            valuation_treatment="eligible for core discussion if scale and economics matter",
            verification_need="check contract value, delivery, margin, and cash collection",
        )
    ]
    relations = [
        FinancialRelationInsight(
            relation_type="cash_absorbing_growth",
            importance="high",
            evidence="revenue grew while operating cash flow stayed negative and prepayments rose.",
            investment_read="Growth currently consumes working capital before proving owner economics.",
            bull_use="Use only if cash conversion improves.",
            bear_use="Challenge whether growth is self-funding.",
        )
    ]
    textual_signals = [
        FilingTextSignal(
            signal_type="unquantified_strategy_language",
            report_type="annual",
            wording_stage="soft_or_intentional",
            evidence="annual report: management says it will actively expand a new growth area without disclosed revenue.",
            investment_read="Management is opening a second-curve narrative, but the filing has not yet proven monetization.",
            bull_use="Use as upside optionality only.",
            bear_use="Challenge proof, scale, timing, and cash cost before treating it as base-case value.",
        )
    ]

    insights = _distill_filing_insights(
        company_name="Example Co",
        coverage_audit=coverage,
        business_model_map=business_model,
        growth_vectors=growth_vectors,
        answers=[],
        financial_relations=relations,
        textual_signals=textual_signals,
    )
    insight_types = {item.insight_type for item in insights}

    assert "core_business_engine" in insight_types
    assert "second_curve_or_inflection_claim" in insight_types
    assert "quality_of_growth_tension" in insight_types
    assert "monetization_gap" in insight_types
    assert "textual_filing_signal" in insight_types


def test_compute_leasing_assets_and_revenue_enter_filing_findings():
    reports = [
        (
            "2025\u5e74\u5e74\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u667a\u4e91\u8ba1\u7b97\u677f\u5757\u5df2\u5f00\u5c55\u7b97\u529b\u79df\u8d41\u4e1a\u52a1\uff0c"
            "\u79df\u8d41\u4e1a\u52a1\u89c4\u6a2122\u4ebf\u5143\uff0c\u5e76\u5b9e\u73b0\u76f8\u5173\u8425\u6536\u3002\n"
            "\u5e7f\u4e1c\u76c8\u5cf0\u65b0\u589e1.39\u4ebf\u5143\u7f51\u7edc\u5de5\u7a0b\u5efa\u8bbe\u8d44\u4ea7\u3002\n"
            "\u5206\u4e1a\u52a1\u770b\uff0c\u7b97\u529b\u79df\u8d41\u8425\u4e1a\u6536\u5165\u589e\u957f\uff0c\u6bdb\u5229\u7387\u5c1a\u9700\u6301\u7eed\u8ddf\u8e2a\u3002",
        ),
        (
            "2026\u5e74\u7b2c\u4e00\u5b63\u5ea6\u62a5\u544a",
            "\u516c\u53f8\u7b97\u529b\u79df\u8d41\u6536\u5165\u7ee7\u7eed\u786e\u8ba4\uff0c\u76f8\u5173\u8d44\u4ea7\u6295\u5165\u589e\u52a0\u3002",
        ),
    ]

    material = _extract_material_filing_findings(reports)
    growth = _extract_growth_vectors(reports)
    segments = _extract_segment_economics(reports)

    assert any(row.finding_type == "compute-leasing-monetization" for row in material)
    assert any(row.vector == "ai-and-digital" and row.stage in {"monetized", "capacity-building"} for row in growth)
    assert any("\u7b97\u529b\u79df\u8d41" in row.evidence for row in segments)
