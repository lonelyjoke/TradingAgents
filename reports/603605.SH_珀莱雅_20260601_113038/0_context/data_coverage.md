# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 603605.SH as of 2026-06-01 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| financial_report_intelligence | partial | Extraction status: Narrative filing text extraction unavailable: no readable annual, semiannual, or quarterly report body was retrieved. Treat this as a filing-text/segment-evid... |
| peer_comparison | thin | No daily_basic valuation snapshot found for 603605.SH near 2026-06-01. |
| supply_chain_comparison | ready | # Supply-chain position comparison for 603605.SH as of 2026-06-01 |
| earnings_model | ready | # Earnings-model context for 603605.SH as of 2026-06-01 |
| market_expectation | ready | # Market-expectation context for 603605.SH as of 2026-06-01 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 603605.SH as of 2026-06-01 |
| management_capital_allocation | ready | # Management and capital-allocation context for 603605.SH as of 2026-06-01 |
| shareholder_structure | ready | # Shareholder-structure context for 603605.SH as of 2026-06-01 |
| investor_interaction | ready | # Investor interaction context for 603605.SH as of 2026-06-01 |
| policy_planning | ready | # Policy-planning context for 603605.SH as of 2026-06-01 |
| web_fact_check | ready | # Web fact-check context for 603605.SH as of 2026-06-01 |
| baijiu | not_applicable | # Baijiu verification context for 603605.SH as of 2026-06-01 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 603605.SH as of 2026-06-01 |
| dividend_defensive | ready | # Dividend defensive verification context for 603605.SH as of 2026-06-01 |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.