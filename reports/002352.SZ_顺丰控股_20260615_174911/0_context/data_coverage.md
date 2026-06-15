# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| industry_cycle_scan | partial | Cycle verdict: cycle evidence insufficient |
| company_business_model | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 002352.SZ as of 2026-06-15 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 002352.SZ as of 2026-06-15 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Industry cycle stage |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 002352.SZ as of 2026-06-15 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 002352.SZ as of 2026-06-15 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 002352.SZ as of 2026-06-15 |
| shipping_cycle | not_applicable | # Shipping cycle context for 002352.SZ as of 2026-06-15 |
| financial_report_intelligence | ready | # Financial-report intelligence for 002352.SZ as of 2026-06-15 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 002352.SZ as of 2026-06-15 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 002352.SZ as of 2026-06-15 |
| earnings_model | ready | # Earnings-model context for 002352.SZ as of 2026-06-15 |
| market_expectation | ready | # Market-expectation context for 002352.SZ as of 2026-06-15 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 002352.SZ as of 2026-06-15 |
| management_capital_allocation | ready | # Management and capital-allocation context for 002352.SZ as of 2026-06-15 |
| shareholder_structure | ready | # Shareholder-structure context for 002352.SZ as of 2026-06-15 |
| investor_interaction | ready | # Investor interaction context for 002352.SZ as of 2026-06-15 |
| policy_planning | ready | # Policy-planning context for 002352.SZ as of 2026-06-15 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| baijiu | not_applicable | # Baijiu verification context for 002352.SZ as of 2026-06-15 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 002352.SZ as of 2026-06-15 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 002352.SZ as of 2026-06-15 |
| building_materials | not_applicable | # Building-materials verification context for 002352.SZ as of 2026-06-15 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 002352.SZ |
| optical_module | not_applicable | # AI optical-module context for 002352.SZ |
| biopharma | not_applicable | # Biopharma verification context for 002352.SZ |
| software | ready | # Software verification context for 002352.SZ as of 2026-06-15 |
| insurance | not_applicable | # Insurance verification context for 002352.SZ as of 2026-06-15 |
| medical_device | ready | # Medical-device verification context for 002352.SZ as of 2026-06-15 |
| metals_mining | not_applicable | # Metals-mining verification context for 002352.SZ |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, keep the rating label clean and put the limitation in conviction, sizing, Evidence Gaps, and Verification Calendar. Use an evidence-limited rating label only when a core module for the thesis is failed/partial or the decisive valuation driver lacks direct evidence.