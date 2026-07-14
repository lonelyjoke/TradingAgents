# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 600809.SH as of 2026-07-14 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 600809.SH as of 2026-07-14 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 600809.SH as of 2026-07-14 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 600809.SH as of 2026-07-14 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure, Hog-cycle private-data bridge |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 600809.SH as of 2026-07-14 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 600809.SH as of 2026-07-14 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 600809.SH as of 2026-07-14 |
| shipping_cycle | not_applicable | # Shipping cycle context for 600809.SH as of 2026-07-14 |
| financial_report_intelligence | ready | # Financial-report intelligence for 600809.SH as of 2026-07-14 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 600809.SH as of 2026-07-14 |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 600809.SH as of 2026-07-14 |
| earnings_model | ready | # Earnings-model context for 600809.SH as of 2026-07-14 |
| company_events | ready | # Tushare A-share event research for 600809.SH as of 2026-07-14 |
| market_expectation | ready | # Market-expectation context for 600809.SH as of 2026-07-14 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 600809.SH as of 2026-07-14 |
| management_capital_allocation | ready | # Management and capital-allocation context for 600809.SH as of 2026-07-14 |
| shareholder_structure | ready | # Shareholder-structure context for 600809.SH as of 2026-07-14 |
| investor_interaction | ready | # Investor interaction context for 600809.SH as of 2026-07-14 |
| policy_planning | ready | # Policy-planning context for 600809.SH as of 2026-07-14 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 600809.SH |
| baijiu | ready | # Baijiu verification context for 600809.SH as of 2026-07-14 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 600809.SH as of 2026-07-14 |
| dividend_defensive | ready | # Dividend defensive verification context for 600809.SH as of 2026-07-14 |
| building_materials | not_applicable | # Building-materials verification context for 600809.SH as of 2026-07-14 |
| consumer_staples | ready | # Consumer-staples verification context for 600809.SH as of 2026-07-14 |
| optical_module | not_applicable | # AI optical-module context for 600809.SH |
| biopharma | not_applicable | # Biopharma verification context for 600809.SH |
| software | not_applicable | # Software verification context for 600809.SH |
| insurance | not_applicable | # Insurance verification context for 600809.SH as of 2026-07-14 |
| medical_device | not_applicable | # Medical-device verification context for 600809.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 600809.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | valuation input | / partial / annual/quarterly/semiannual / none / 9/9 / thin / Readable filings exist, but either cross-period coverage or answer density is incomplete; use f... | primary_or_structured_filing | reported_fact | unspecified |
| KF02 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年第一季度报告: 衍生... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF03 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年半年度报告... | primary_or_structured_filing | model_estimate | 2025, 半年, 本报告期 |
| KF04 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年第一季度报告:... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF05 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF06 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgra... | primary_or_structured_filing | reported_fact | 2025, 年度, 2030 |
| KF07 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年第一季度报告: 衍生金融资产 应收票据 应收账款 93,685.45 96,80... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF09 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 半年, 2030 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| hog breeding | Hog ASP / futures curve | ready | thesis_question_context: / HG-1 / Where exactly are we in the hog cycle: downcycle, bottom-testing, bottom-right validation, or early upcycle? / prove the cycle stage with hog ASP, p... |
| hog breeding | Piglet and sow supply | ready | thesis_question_context: / HG-1 / Where exactly are we in the hog cycle: downcycle, bottom-testing, bottom-right validation, or early upcycle? / prove the cycle stage with hog ASP, p... |
| hog breeding | Complete breeding cost | ready | thesis_question_context: / HG-2 / Is the company creating alpha through cost advantage or just carrying hog-price beta? / prove complete cost, PSY/FCR, mortality, feed cost, finance ... |
| hog breeding | Monthly sales volume/price | missing | No explicit source-backed evidence found. |
| hog breeding | OCF / leverage survival | ready | thesis_question_context: / HG-2 / Is the company creating alpha through cost advantage or just carrying hog-price beta? / prove complete cost, PSY/FCR, mortality, feed cost, finance ... |
| hog breeding | PB / NAV stress floor | ready | thesis_question_context: / HG-1 / Where exactly are we in the hog cycle: downcycle, bottom-testing, bottom-right validation, or early upcycle? / prove the cycle stage with hog ASP, p... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.