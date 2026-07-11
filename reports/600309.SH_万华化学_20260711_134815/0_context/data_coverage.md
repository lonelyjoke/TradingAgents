# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 600309.SH as of 2026-07-11 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 600309.SH as of 2026-07-11 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 600309.SH as of 2026-07-11 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 600309.SH as of 2026-07-11 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 600309.SH as of 2026-07-11 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 600309.SH as of 2026-07-11 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 600309.SH as of 2026-07-11 |
| shipping_cycle | not_applicable | # Shipping cycle context for 600309.SH as of 2026-07-11 |
| financial_report_intelligence | ready | # Financial-report intelligence for 600309.SH as of 2026-07-11 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 600309.SH as of 2026-07-11 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 600309.SH as of 2026-07-11 |
| earnings_model | ready | # Earnings-model context for 600309.SH as of 2026-07-11 |
| company_events | ready | # Tushare A-share event research for 600309.SH as of 2026-07-11 |
| market_expectation | ready | # Market-expectation context for 600309.SH as of 2026-07-11 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 600309.SH as of 2026-07-11 |
| management_capital_allocation | ready | # Management and capital-allocation context for 600309.SH as of 2026-07-11 |
| shareholder_structure | ready | # Shareholder-structure context for 600309.SH as of 2026-07-11 |
| investor_interaction | ready | # Investor interaction context for 600309.SH as of 2026-07-11 |
| policy_planning | ready | # Policy-planning context for 600309.SH as of 2026-07-11 |
| web_fact_check | ready | # Web fact-check context for 600309.SH as of 2026-07-11 |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 600309.SH |
| baijiu | not_applicable | # Baijiu verification context for 600309.SH as of 2026-07-11 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 600309.SH as of 2026-07-11 |
| dividend_defensive | ready | # Dividend defensive verification context for 600309.SH as of 2026-07-11 |
| building_materials | not_applicable | # Building-materials verification context for 600309.SH as of 2026-07-11 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 600309.SH |
| optical_module | not_applicable | # AI optical-module context for 600309.SH |
| biopharma | not_applicable | # Biopharma verification context for 600309.SH |
| software | not_applicable | # Software verification context for 600309.SH |
| insurance | not_applicable | # Insurance verification context for 600309.SH as of 2026-07-11 |
| medical_device | not_applicable | # Medical-device verification context for 600309.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 600309.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | valuation input | / partial / annual/quarterly/semiannual / none / 9/9 / thin / Readable filings exist, but either cross-period coverage or answer density is incomplete; use f... | primary_or_structured_filing | reported_fact | unspecified |
| KF02 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 万华化学202... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF03 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 万华化学2025年年... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF04 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 万华化学... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF05 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF08 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / prepayments: 万华化学2025年年度报告: 应收款项融资 2,777,227,576.55 0.86 1... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | calculated | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | calculation | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| consumer staples | Sell-through / channel inventory | ready | financial_report_intelligence: / impairment / annual / 万华化学2025年年度报告: 筹资活动产生的现金流量净额 2,143,880,788.98 6,186,159,622.30 -65.34 公允价值变动收益 266,157,485.20 -76,388,802.79 448.42 信用减值损失 42,755,376... |
| consumer staples | Price system / ASP | ready | financial_report_intelligence: / high_r_and_d_technology / 高研发技术产品型 / quantified disclosure / 万华化学2025年年度报告: 电池科技有限公司专注于电池材料及相关化学品领域，产品涵盖磷酸铁锂、石墨 负极、电池级硫酸盐、N-甲基吡咯烷酮（NMP）、聚丙烯酸（PAA）等，广泛应用于新 能... |
| consumer staples | Contract liabilities | ready | financial_report_intelligence: / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 万华化学... |
| consumer staples | Gross margin and raw materials | ready | forecast_model_scaffold: / Gross margin / 14.728% / -0.98pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| consumer staples | Food safety / quality risk | missing | No explicit source-backed evidence found. |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.