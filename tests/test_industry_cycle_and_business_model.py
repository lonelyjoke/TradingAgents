from tradingagents.dataflows.business_model_research import (
    build_company_business_model_context,
)
from tradingagents.dataflows.industry_cycle_research import build_industry_cycle_context


def test_industry_cycle_scan_classifies_lithium_bottom_right_validation():
    commodity_context = """
# Commodity and product price context for 002460.SZ as of 2026-06-11

| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | main product | Tushare futures proxy | LC.GFE | 174600 | 20260611 | 14.81% | N/A | Verified by Tushare futures daily data. | curve=LC2609.GFE close=174600, LC2611.GFE close=175900 |
"""

    context = build_industry_cycle_context(
        "002460.SZ",
        "2026-06-11",
        commodity_context=commodity_context,
    )

    assert "Industry Cycle Scan" in context
    assert "bottom-right validation stage" in context
    assert "Do not write `cycle bottom`" in context
    assert "174600" in context


def test_industry_cycle_scan_marks_missing_sector_evidence_insufficient():
    context = build_industry_cycle_context("000001.SZ", "2026-06-11")

    assert "cycle evidence insufficient" in context
    assert "Do not claim a cycle bottom/top" in context


def test_company_business_model_primer_extracts_segment_and_valuation_sections():
    filing_context = """
# Financial-report intelligence for 002460.SZ as of 2026-06-11

- Company: 赣锋锂业
- Vendor industry: 小金属

## Company-Specific Business Archetype
| archetype_id | archetype_name | evidence_strength | evidence_basis | underwriting_focus |
| --- | --- | --- | --- | --- |
| cyclical_integrated_resource | 垂直一体化锂产业链 | medium | 公司覆盖锂资源、锂盐、电池及回收 | split lithium price beta from battery optionality |

## Business Model Map
| lens | report_type | filing_evidence | why_it_matters |
| --- | --- | --- | --- |
| core_revenue_engine | annual | 公司主营锂化合物、金属锂、锂电池及回收业务。 | Defines what actually drives the income statement. |

## Segment Economics Pack
| segment_type | report_type | filing_evidence | analyst_use |
| --- | --- | --- | --- |
| product | annual | 基础化学材料收入占比56.8%，锂电池、电芯及其回收收入占比35.5%。 | Split mature lithium-salt profit pool from battery second curve. |

## Business Segment Valuation Map
| business_bucket | report_type | filing_evidence | valuation_anchor | analyst_use | verification_need |
| --- | --- | --- | --- | --- | --- |
| mature/core | annual | 锂盐为核心盈利来源。 | normalized earnings / PE through cycle | core valuation anchor | realized price and cost |

## Growth Vector Map
| vector | stage | filing_evidence | valuation_treatment | verification_need |
| --- | --- | --- | --- | --- |
| 储能电池 | narrative | 储能出货增长，但利润未披露。 | scenario/SOTP only | segment margin and cash conversion |
"""

    primer = build_company_business_model_context(
        "002460.SZ",
        "2026-06-11",
        filing_intelligence_context=filing_context,
        peer_comparison_context="# Peer\n\n- 天齐锂业毛利率更高。",
        commodity_context="# Commodity\n\n- Lithium carbonate latest_price 174600.",
    )

    assert "Company Business Model Primer" in primer
    assert "赣锋锂业" in primer
    assert "基础化学材料收入占比56.8%" in primer
    assert "Segment Valuation / Evidence Gates" in primer
    assert "储能出货增长" in primer
