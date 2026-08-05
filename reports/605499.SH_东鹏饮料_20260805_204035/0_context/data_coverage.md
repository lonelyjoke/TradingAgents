# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 605499.SH as of 2026-08-05 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 605499.SH as of 2026-08-05 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 605499.SH as of 2026-08-05 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 605499.SH as of 2026-08-05 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Knowledge Planet intelligence |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 东鹏饮料（集团）股份有限公司2026年半年度报告: PDF downloaded but no readable text was extracted from 233d137773bd77a8239f95fa12292b6c30f21f05.pdf. / |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 605499.SH as of 2026-08-05 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 605499.SH as of 2026-08-05 |
| shipping_cycle | not_applicable | # Shipping cycle context for 605499.SH as of 2026-08-05 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 东鹏饮料（集团）股份有限公司2026年半年度报告: PDF downloaded but no readable text was extracted from 233d137773bd77a8239f95fa12292b6c30f21f05.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 605499.SH as of 2026-08-05 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 605499.SH as of 2026-08-05 |
| earnings_model | ready | # Earnings-model context for 605499.SH as of 2026-08-05 |
| company_events | ready | # Tushare A-share event research for 605499.SH as of 2026-08-05 |
| market_expectation | ready | # Market-expectation context for 605499.SH as of 2026-08-05 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 605499.SH as of 2026-08-05 |
| management_capital_allocation | ready | # Management and capital-allocation context for 605499.SH as of 2026-08-05 |
| shareholder_structure | ready | # Shareholder-structure context for 605499.SH as of 2026-08-05 |
| investor_interaction | ready | # Investor interaction context for 605499.SH as of 2026-08-05 |
| policy_planning | ready | # Policy-planning context for 605499.SH as of 2026-08-05 |
| web_fact_check | ready | # Web fact-check context for 605499.SH as of 2026-08-05 |
| knowledge_planet | failed | # Knowledge Planet topic-text intelligence context unavailable |
| baijiu | ready | # Baijiu verification context for 605499.SH as of 2026-08-05 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 605499.SH as of 2026-08-05 |
| dividend_defensive | ready | # Dividend defensive verification context for 605499.SH as of 2026-08-05 |
| building_materials | not_applicable | # Building-materials verification context for 605499.SH as of 2026-08-05 |
| consumer_staples | ready | # Consumer-staples verification context for 605499.SH as of 2026-08-05 |
| optical_module | ready | # AI optical-module context for 605499.SH as of 2026-08-05 |
| biopharma | not_applicable | # Biopharma verification context for 605499.SH |
| software | not_applicable | # Software verification context for 605499.SH |
| insurance | not_applicable | # Insurance verification context for 605499.SH as of 2026-08-05 |
| medical_device | not_applicable | # Medical-device verification context for 605499.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 605499.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | valuation input | / partial / annual/quarterly/semiannual / none / 9/9 / thin / Readable filings exist, but either cross-period coverage or answer density is incomplete; use f... | primary_or_structured_filing | reported_fact | unspecified |
| KF02 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_op... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF03 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 东鹏饮料（集团）股份... | primary_or_structured_filing | model_estimate | 2026, 半年, 2015 |
| KF04 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 东鹏饮料... | primary_or_structured_filing | reported_fact | 2026, 半年 |
| KF05 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 半年 |
| KF06 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 半年 |
| KF08 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / contract_liabilities: 东鹏饮料（集团）股份有限公司2026年半年度报告: 固定资产 6,638... | primary_or_structured_filing | reported_fact | 2026, 半年 |
| KF09 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2026, 半年 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2026, 半年 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2026, 半年 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| consumer staples | Sell-through / channel inventory | ready | thesis_question_context: / CS-1 / Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality? / prove sell-through, distributor inventory, contract ... |
| consumer staples | Price system / ASP | ready | thesis_question_context: / CS-2 / Can gross margin improvement survive raw-material, promotion, and mix normalization? / prove cost pass-through and durable high-margin mix / attack ... |
| consumer staples | Contract liabilities | ready | thesis_question_context: / CS-1 / Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality? / prove sell-through, distributor inventory, contract ... |
| consumer staples | Gross margin and raw materials | ready | thesis_question_context: / CS-1 / Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality? / prove sell-through, distributor inventory, contract ... |
| consumer staples | Food safety / quality risk | missing | No explicit source-backed evidence found. |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.