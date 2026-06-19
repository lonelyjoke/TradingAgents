# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | partial | # Same-industry peer comparison unavailable |
| industry_cycle_scan | ready | # Industry Cycle Scan for 601318.SH as of 2026-06-18 |
| company_business_model | not_applicable | No clean business-model or segment-economics filing section was available; the report must explicitly downgrade confidence before describing the business model. |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 601318.SH as of 2026-06-18 |
| forecast_model_scaffold | partial | No clean business-model or segment-economics filing section was available; the report must explicitly downgrade confidence before describing the business model. |
| sell_side_quality_audit | partial | Weak or incomplete modules: Business model / segment economics |
| thematic_catalyst | partial | / announcement_lookup / failed / anns unavailable: anns unavailable: configured_http_url: 请指定正确的接口名; cninfo announcement fallback unavailable: HTTPSConnectionPool(host='www.cnin... |
| commodity_product_price | ready | # Commodity and product price context for 601318.SH as of 2026-06-18 |
| price_move_attribution | ready | # Price-move attribution context for 601318.SH as of 2026-06-18 |
| intraday_minute_behavior | thin | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 601318.SH as of 2026-06-18 |
| shipping_cycle | not_applicable | # Shipping cycle context for 601318.SH as of 2026-06-18 |
| financial_report_intelligence | failed | # Financial-report intelligence unavailable |
| peer_comparison | failed | # Same-industry peer comparison unavailable |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 601318.SH as of 2026-06-18 |
| earnings_model | failed | # Earnings-model context unavailable |
| market_expectation | ready | # Market-expectation context for 601318.SH as of 2026-06-18 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 601318.SH as of 2026-06-18 |
| management_capital_allocation | ready | # Management and capital-allocation context for 601318.SH as of 2026-06-18 |
| shareholder_structure | ready | # Shareholder-structure context for 601318.SH as of 2026-06-18 |
| investor_interaction | ready | # Investor interaction context for 601318.SH as of 2026-06-18 |
| policy_planning | ready | # Policy-planning context for 601318.SH as of 2026-06-18 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| baijiu | not_applicable | # Baijiu verification context for 601318.SH as of 2026-06-18 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 601318.SH as of 2026-06-18 |
| dividend_defensive | ready | # Dividend defensive verification context for 601318.SH as of 2026-06-18 |
| building_materials | not_applicable | # Building-materials verification context for 601318.SH as of 2026-06-18 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 601318.SH |
| optical_module | not_applicable | # AI optical-module context for 601318.SH |
| biopharma | not_applicable | # Biopharma verification context for 601318.SH |
| software | not_applicable | # Software verification context for 601318.SH |
| insurance | ready | # Insurance verification context for 601318.SH as of 2026-06-18 |
| medical_device | not_applicable | # Medical-device verification context for 601318.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 601318.SH |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, keep the rating label clean and put the limitation in conviction, sizing, Evidence Gaps, and Verification Calendar. Use an evidence-limited rating label only when a core module for the thesis is failed/partial or the decisive valuation driver lacks direct evidence.