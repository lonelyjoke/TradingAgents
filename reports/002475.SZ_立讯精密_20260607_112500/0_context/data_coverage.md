# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 002475.SZ as of 2026-06-07 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 002475.SZ as of 2026-06-07 |
| relative_strength | ready | # Relative strength and index linkage for 002475.SZ as of 2026-06-07 |
| shipping_cycle | not_applicable | # Shipping cycle context for 002475.SZ as of 2026-06-07 |
| financial_report_intelligence | ready | # Financial-report intelligence for 002475.SZ as of 2026-06-07 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 002475.SZ as of 2026-06-07 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 002475.SZ as of 2026-06-07 |
| earnings_model | ready | # Earnings-model context for 002475.SZ as of 2026-06-07 |
| market_expectation | failed | # Market-expectation context unavailable |
| price_eps_pe_decomposition | failed | # Price-EPS-PE decomposition unavailable |
| management_capital_allocation | ready | # Management and capital-allocation context for 002475.SZ as of 2026-06-07 |
| shareholder_structure | ready | # Shareholder-structure context for 002475.SZ as of 2026-06-07 |
| investor_interaction | ready | # Investor interaction context for 002475.SZ as of 2026-06-07 |
| policy_planning | ready | # Policy-planning context for 002475.SZ as of 2026-06-07 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| baijiu | not_applicable | # Baijiu verification context for 002475.SZ as of 2026-06-07 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 002475.SZ as of 2026-06-07 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 002475.SZ as of 2026-06-07 |
| building_materials | not_applicable | # Building-materials verification context for 002475.SZ as of 2026-06-07 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 002475.SZ |
| optical_module | not_applicable | # AI optical-module context for 002475.SZ |
| biopharma | not_applicable | # Biopharma verification context for 002475.SZ |
| software | not_applicable | # Software verification context for 002475.SZ |
| insurance | not_applicable | # Insurance verification context for 002475.SZ as of 2026-06-07 |
| medical_device | failed | # Medical-device verification context unavailable |
| metals_mining | not_applicable | # Metals-mining verification context for 002475.SZ |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.