from tradingagents.dataflows.filing_research import (
    _answer_questions,
    _detect_report_type,
    _extract_filing_evidence,
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
        ("山西汾酒", "白酒", "公司持续优化批价与经销商库存。", "baijiu"),
        ("中国国航", "航空运输", "公司客座率提升，航油成本仍需关注，机队稳步扩张。", "airlines"),
        ("中国平安", "保险", "公司新业务价值与内含价值持续改善。", "insurance"),
    ]

    for company_name, industry, report_text, expected in cases:
        assert (
            _select_industry_profile(company_name, industry, [("2025年年度报告", report_text)])
            == expected
        )


def test_question_candidates_include_new_priority_playbooks():
    assert any(q.question_id == "metals_resource_volume" for q in _question_candidates("metals_mining"))
    assert any(q.question_id == "battery_capacity_utilization" for q in _question_candidates("lithium_battery"))
    assert any(q.question_id == "baijiu_channel_inventory" for q in _question_candidates("baijiu"))
    assert any(q.question_id == "airline_traffic_yield" for q in _question_candidates("airlines"))
    assert any(q.question_id == "insurance_nbv" for q in _question_candidates("insurance"))
