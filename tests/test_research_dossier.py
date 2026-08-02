import json

from tradingagents.dataflows.research_dossier import (
    CHAPTERS,
    build_reader_research_dossier,
    compact_reader_research_dossier,
    render_reader_research_dossier,
)
from tradingagents.dataflows.structured_research import (
    compact_structured_research_for_prompt,
)


def _bundle() -> dict:
    return {
        "schema_version": 3,
        "symbol": "600000.SH",
        "as_of_date": "2026-08-01",
        "semantic_metrics": [
            {
                "metric_id": "EV-REV",
                "source_module": "annual_report",
                "model_variable": "revenue",
                "period": "2025A",
                "status": "reported",
                "value_text": "营业收入100亿元",
            }
        ],
        "deterministic_evidence": [
            {
                "evidence_id": "EV-IND",
                "source_module": "industry_cycle",
                "variable": "industry_supply_chain",
                "period": "2026Q2",
                "evidence_status": "verified",
                "text": "上游供给增速放缓",
            }
        ],
        "kpe_impacts": [
            {
                "evidence_id": "KPE01",
                "variable": "volume",
                "quantification_status": "quantified",
                "decision_outcome": "销量假设100->110",
                "known_kpe": {
                    "evidence_id": "KPE01",
                    "source_type": "channel_check",
                    "date": "2026-07-20",
                    "evidence": "浦发银行渠道调研显示重点产品销量改善。",
                    "verification": "2026H1报告销量披露",
                    "source_reliability": "B_identified_professional",
                    "bias_profile": "sell_side_optimism",
                    "adoption_ceiling": "model_input_after_crosscheck",
                },
            },
            {
                "evidence_id": "KPE02",
                "variable": "expectation_gap",
                "quantification_status": "probability_only",
                "decision_outcome": "bull/base/bear 20/60/20 -> 25/55/20",
                "known_kpe": {
                    "evidence_id": "KPE02",
                    "source_type": "company_research",
                    "date": "2026-07-21",
                    "evidence": "浦发银行调研反馈显示市场预期存在分歧。",
                    "verification": "下一次业绩交流会",
                },
            },
            {
                "evidence_id": "KPE03",
                "variable": "margin",
                "disposition": "watch_unchanged",
                "decision_outcome": "unchanged/watch",
                "known_kpe": {
                    "evidence_id": "KPE03",
                    "source_type": "industry_data",
                    "date": "2026-07-22",
                    "evidence": "浦发银行相关产业价格信号尚待财报验证。",
                    "verification": "2026Q3毛利率",
                },
            },
            {
                "evidence_id": "KPE04",
                "variable": "valuation",
                "disposition": "rejected",
                "decision_outcome": "rejected: promotional target price",
                "known_kpe": {
                    "evidence_id": "KPE04",
                    "source_type": "sell_side_view",
                    "date": "2026-07-23",
                    "evidence": "浦发银行目标价宣传未给出盈利桥。",
                    "verification": "不进入模型",
                },
            },
        ],
        "sell_side_intelligence": [
            {"institution": "测试证券", "forecast_and_valuation": "2026E EPS 1.2元"}
        ],
        "underwriting_packet": {
            "research_readiness": "partial",
            "readiness_reasons": ["分部利润率待披露"],
            "forecast_years": ["2026E", "2027E", "2028E"],
            "company_model": {
                "business_archetype": "银行",
                "operating_model_family": "financial",
                "value_proposition_and_customers": "为企业和个人客户提供信贷与金融服务",
                "revenue_equation": "生息资产×净息差+手续费收入",
                "profit_equation": "收入-业务及管理费-信用减值",
                "cash_flow_equation": "金融企业现金流按资产负债结构解释",
                "capital_intensity_and_reinvestment": "资本充足率约束资产扩张",
                "moat_mechanisms": ["客户基础", "资金成本"],
                "structural_risks": ["信用成本上升"],
            },
            "business_unit_map": [
                {"business_unit": "公司金融", "economic_role": "核心利润池"}
            ],
            "segment_models": [
                {
                    "segment": "公司金融",
                    "industry_supply_and_capacity": "信贷供给受资本与需求共同约束",
                    "unit_cost_and_input_prices": "存款成本是关键输入",
                    "customers_and_channel": "企业客户与分支行渠道",
                    "demand_and_order_drivers": ["融资需求"],
                    "price_asp_take_rate": "贷款收益率与存款成本共同决定净息差",
                }
            ],
            "underwriting_questions": [
                {"question_id": "Q1", "question": "净息差能否企稳？"}
            ],
            "moat_evidence_tests": [
                {"mechanism": "低资金成本", "status": "partial"}
            ],
            "competition_landscapes": [
                {
                    "business_unit": "公司金融",
                    "market_boundary": "长三角对公贷款与综合金融服务",
                    "direct_competitors": ["招商银行", "宁波银行"],
                    "financial_transmission": "存款成本与贷款定价影响净息差",
                }
            ],
            "llm_analysis_layer": {
                "competition_and_substitution_analysis": "客户可在全国股份行与区域银行之间切换。"
            },
            "forecast_lines": [
                {"line_id": "2026E_revenue", "period": "2026E", "metric": "revenue"}
            ],
            "scenarios": [{"scenario": "base", "probability_pct": 55}],
            "valuation_closure": {"status": "partial"},
        },
    }


def test_dossier_routes_company_model_and_exactly_seven_chapters():
    dossier = build_reader_research_dossier(
        "600000.SH",
        "2026-08-01",
        structured_research=_bundle(),
        contexts={
            "knowledge_planet": "Primary query terms: 浦发银行, 600000\nDirect terms: 浦发"
        },
    )

    assert dossier["reader_contract"]["chapter_count"] == 7
    assert [row[0] for row in CHAPTERS] == [
        row["chapter_id"] for row in dossier["chapter_packets"]
    ]
    assert dossier["company_introduction"]["business_archetype"] == "银行"
    assert dossier["industry_chain"]["upstream_cost_and_supply"][0]["segment"] == "公司金融"
    assert dossier["profit_pools"]["reported_or_analytical_units"][0]["business_unit"] == "公司金融"
    assert dossier["key_underwriting_questions"][0]["question_id"] == "Q1"
    assert dossier["competition_and_moat"]["landscapes"][0]["business_unit"] == "公司金融"
    assert dossier["competition_and_moat"]["competition_and_substitution_analysis"]


def test_knowledge_planet_is_entity_scoped_and_routed_by_decision_role():
    dossier = build_reader_research_dossier(
        "600000.SH",
        "2026-08-01",
        structured_research=_bundle(),
        contexts={"knowledge_planet": "Primary query terms: 浦发银行, 浦发"},
    )
    items = {row["evidence_id"]: row for row in dossier["knowledge_planet"]["items"]}

    assert items["KPE01"]["allowed_role"] == "model_input"
    assert items["KPE01"]["source_reliability"] == "B_identified_professional"
    assert items["KPE01"]["bias_profile"] == "sell_side_optimism"
    assert items["KPE02"]["allowed_role"] == "probability_adjustment"
    assert items["KPE03"]["allowed_role"] == "verification_item"
    assert items["KPE04"]["allowed_role"] == "rejected"
    assert all(row["entity_scope"] == "target_mentioned" for row in items.values())
    assert "浦发银行" in items["KPE01"]["target_excerpt"]
    assert "KPE04" not in {
        evidence_id
        for chapter in dossier["chapter_packets"]
        for evidence_id in chapter["knowledge_planet_ids"]
    }


def test_compact_bundle_keeps_reader_dossier_and_human_audit():
    bundle = _bundle()
    bundle["research_dossier"] = build_reader_research_dossier(
        "600000.SH",
        "2026-08-01",
        structured_research=bundle,
        contexts={"knowledge_planet": "Primary query terms: 浦发银行"},
    )

    compact = compact_reader_research_dossier(bundle["research_dossier"])
    assert len(compact["chapter_packets"]) == 7
    prompt_bundle = json.loads(compact_structured_research_for_prompt(bundle))
    assert prompt_bundle["research_dossier"]["reader_contract"]["chapter_count"] == 7
    markdown = render_reader_research_dossier(bundle["research_dossier"])
    assert "# 七章研究档案：600000.SH" in markdown
    assert "## 知识星球利用结果" in markdown
    assert "KPE01｜model_input" in markdown
