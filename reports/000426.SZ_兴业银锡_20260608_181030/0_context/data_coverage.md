# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 000426.SZ as of 2026-06-08 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 000426.SZ as of 2026-06-08 |
| relative_strength | partial | / style_index_daily / failed / CSI 500 / 中证500; 0 observations / |
| shipping_cycle | not_applicable | # Shipping cycle context for 000426.SZ as of 2026-06-08 |
| financial_report_intelligence | ready | # Financial-report intelligence for 000426.SZ as of 2026-06-08 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 000426.SZ as of 2026-06-08 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 000426.SZ as of 2026-06-08 |
| earnings_model | ready | # Earnings-model context for 000426.SZ as of 2026-06-08 |
| market_expectation | ready | # Market-expectation context for 000426.SZ as of 2026-06-08 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 000426.SZ as of 2026-06-08 |
| management_capital_allocation | ready | # Management and capital-allocation context for 000426.SZ as of 2026-06-08 |
| shareholder_structure | ready | # Shareholder-structure context for 000426.SZ as of 2026-06-08 |
| investor_interaction | ready | # Investor interaction context for 000426.SZ as of 2026-06-08 |
| policy_planning | ready | # Policy-planning context for 000426.SZ as of 2026-06-08 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| baijiu | not_applicable | # Baijiu verification context for 000426.SZ as of 2026-06-08 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 000426.SZ as of 2026-06-08 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 000426.SZ as of 2026-06-08 |
| building_materials | not_applicable | # Building-materials verification context for 000426.SZ as of 2026-06-08 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 000426.SZ |
| optical_module | not_applicable | # AI optical-module context for 000426.SZ |
| biopharma | not_applicable | # Biopharma verification context for 000426.SZ |
| software | not_applicable | # Software verification context for 000426.SZ |
| insurance | not_applicable | # Insurance verification context for 000426.SZ as of 2026-06-08 |
| medical_device | not_applicable | # Medical-device verification context for 000426.SZ |
| metals_mining | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.