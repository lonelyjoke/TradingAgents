# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 300750.SZ as of 2026-07-01 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 300750.SZ as of 2026-07-01 |
| company_business_model | ready | # Company Business Model Primer for 300750.SZ as of 2026-07-01 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 300750.SZ as of 2026-07-01 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 300750.SZ as of 2026-07-01 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 300750.SZ as of 2026-07-01 |
| commodity_product_price | ready | # Commodity and product price context for 300750.SZ as of 2026-07-01 |
| price_move_attribution | ready | # Price-move attribution context for 300750.SZ as of 2026-07-01 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 300750.SZ as of 2026-07-01 |
| shipping_cycle | not_applicable | # Shipping cycle context for 300750.SZ as of 2026-07-01 |
| financial_report_intelligence | ready | # Financial-report intelligence for 300750.SZ as of 2026-07-01 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 300750.SZ as of 2026-07-01 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 300750.SZ as of 2026-07-01 |
| earnings_model | ready | # Earnings-model context for 300750.SZ as of 2026-07-01 |
| market_expectation | ready | # Market-expectation context for 300750.SZ as of 2026-07-01 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 300750.SZ as of 2026-07-01 |
| management_capital_allocation | ready | # Management and capital-allocation context for 300750.SZ as of 2026-07-01 |
| shareholder_structure | ready | # Shareholder-structure context for 300750.SZ as of 2026-07-01 |
| investor_interaction | ready | # Investor interaction context for 300750.SZ as of 2026-07-01 |
| policy_planning | ready | # Policy-planning context for 300750.SZ as of 2026-07-01 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 300750.SZ |
| baijiu | not_applicable | # Baijiu verification context for 300750.SZ as of 2026-07-01 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 300750.SZ as of 2026-07-01 |
| dividend_defensive | ready | # Dividend defensive verification context for 300750.SZ as of 2026-07-01 |
| building_materials | not_applicable | # Building-materials verification context for 300750.SZ as of 2026-07-01 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 300750.SZ |
| optical_module | not_applicable | # AI optical-module context for 300750.SZ |
| biopharma | not_applicable | # Biopharma verification context for 300750.SZ |
| software | not_applicable | # Software verification context for 300750.SZ |
| insurance | not_applicable | # Insurance verification context for 300750.SZ as of 2026-07-01 |
| medical_device | not_applicable | # Medical-device verification context for 300750.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 300750.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: ... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | valuation input | / project_delivery / 项目订单 / 交付回款型 / quantified disclosure / 2025年年度报告: [Runtime-compacted filing text for 2025年年度报告: original 499236 chars, budget 180000 cha... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| battery / energy storage | Power-battery shipments / share | ready | company_business_model: / reinvestment_engine / annual / 2025年年度报告: 项目的建设。报告期内公司锂电池产能 772GWh，期末在建产能 321GWh。 / Shows how today's cash is being converted into tomorrow's earnings powe... |
| battery / energy storage | Energy-storage shipments / orders | ready | industry_kpi_checklist: / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... |
| battery / energy storage | Battery ASP / pass-through | missing | No explicit source-backed evidence found. |
| battery / energy storage | Lithium/material cost | ready | industry_cycle_scan: / Lithium carbonate / raw material proxy / Tushare futures proxy / LC.GFE / 164560 / 20260701 / 3.41% / N/A / Verified by Tushare futures daily data. / excha... |
| battery / energy storage | Capacity utilization | ready | thesis_question_context: / G-3 / What would make the bull case clearly wrong, and what would make the bear case clearly wrong? / state falsification signals and upgrade triggers with... |
| battery / energy storage | Segment gross margin | ready | company_business_model: / earnings_model / / Gross margin / 24.8156% / +0.41pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / / |
| battery / energy storage | OCF / FCF / capex | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.