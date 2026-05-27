# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thematic_catalyst | partial | Extraction status: Financial-report text extraction unavailable or no readable report text was retrieved. |
| commodity_product_price | ready | # Commodity and product price context for 301396.SZ as of 2026-05-25 |
| financial_report_intelligence | partial | Extraction status: Narrative filing text extraction unavailable: no readable annual, semiannual, or quarterly report body was retrieved. Treat this as a filing-text/segment-evid... |
| peer_comparison | failed | # Same-industry peer comparison unavailable for 301396.SZ |
| supply_chain_comparison | ready | # Supply-chain position comparison for 301396.SZ as of 2026-05-25 |
| earnings_model | ready | # Earnings-model context for 301396.SZ as of 2026-05-25 |
| market_expectation | ready | # Market-expectation context for 301396.SZ as of 2026-05-25 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 301396.SZ as of 2026-05-25 |
| management_capital_allocation | ready | # Management and capital-allocation context for 301396.SZ as of 2026-05-25 |
| shareholder_structure | ready | # Shareholder-structure context for 301396.SZ as of 2026-05-25 |
| investor_interaction | ready | # Investor interaction context for 301396.SZ as of 2026-05-25 |
| policy_planning | ready | # Policy-planning context for 301396.SZ as of 2026-05-25 |
| web_fact_check | ready | # Web fact-check context for 301396.SZ as of 2026-05-25 |
| compute_leasing | ready | # Compute-leasing verification layer for 301396.SZ as of 2026-05-25 |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.