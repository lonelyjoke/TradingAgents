# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thematic_catalyst | partial | Extraction status: Financial-report text extraction unavailable or no readable report text was retrieved. |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| financial_report_intelligence | partial | / risk_update / semiannual / 风险因素 / Which risks are newly forming or fading? / 九号有限公司2025年半年度报告: 四、风险因素 √适用 □不适用 1、宏观经济波动风险 21 / 159 九号有限公司2025 年半年度报告 宏观经济波动风险。目前国际经济形势复杂多变，全球经济... |
| peer_comparison | ready | # Tushare same-industry peer comparison for 689009.SH as of 2026-05-23 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 689009.SH as of 2026-05-23 |
| earnings_model | ready | # Earnings-model context for 689009.SH as of 2026-05-23 |
| market_expectation | ready | # Market-expectation context for 689009.SH as of 2026-05-23 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 689009.SH as of 2026-05-23 |
| management_capital_allocation | ready | # Management and capital-allocation context for 689009.SH as of 2026-05-23 |
| shareholder_structure | ready | # Shareholder-structure context for 689009.SH as of 2026-05-23 |
| investor_interaction | ready | # Investor interaction context for 689009.SH as of 2026-05-23 |
| policy_planning | ready | # Policy-planning context for 689009.SH as of 2026-05-23 |
| web_fact_check | ready | # Web fact-check context for 689009.SH as of 2026-05-23 |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.