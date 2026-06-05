# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thematic_catalyst | partial | Extraction status: Financial-report text extraction unavailable or no readable report text was retrieved. |
| commodity_product_price | ready | # Commodity and product price context for 603345.SH as of 2026-06-05 |
| price_move_attribution | ready | # Price-move attribution context for 603345.SH as of 2026-06-05 |
| shipping_cycle | not_applicable | # Shipping cycle context for 603345.SH as of 2026-06-05 |
| financial_report_intelligence | partial | Extraction status: Narrative filing text extraction unavailable: no readable annual, semiannual, or quarterly report body was retrieved. Treat this as a filing-text/segment-evid... |
| peer_comparison | ready | # Tushare same-industry peer comparison for 603345.SH as of 2026-06-05 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 603345.SH as of 2026-06-05 |
| earnings_model | ready | # Earnings-model context for 603345.SH as of 2026-06-05 |
| market_expectation | ready | # Market-expectation context for 603345.SH as of 2026-06-05 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 603345.SH as of 2026-06-05 |
| management_capital_allocation | ready | # Management and capital-allocation context for 603345.SH as of 2026-06-05 |
| shareholder_structure | ready | # Shareholder-structure context for 603345.SH as of 2026-06-05 |
| investor_interaction | ready | # Investor interaction context for 603345.SH as of 2026-06-05 |
| policy_planning | ready | # Policy-planning context for 603345.SH as of 2026-06-05 |
| web_fact_check | ready | # Web fact-check context for 603345.SH as of 2026-06-05 |
| baijiu | not_applicable | # Baijiu verification context for 603345.SH as of 2026-06-05 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 603345.SH as of 2026-06-05 |
| dividend_defensive | ready | # Dividend defensive verification context for 603345.SH as of 2026-06-05 |
| building_materials | not_applicable | # Building-materials verification context for 603345.SH as of 2026-06-05 |
| consumer_staples | ready | # Consumer-staples verification context for 603345.SH as of 2026-06-05 |
| biopharma | not_applicable | # Biopharma verification context for 603345.SH |
| software | not_applicable | # Software verification context for 603345.SH |
| insurance | not_applicable | # Insurance verification context for 603345.SH as of 2026-06-05 |
| medical_device | not_applicable | # Medical-device verification context for 603345.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 603345.SH |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.