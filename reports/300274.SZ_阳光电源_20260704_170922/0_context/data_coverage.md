# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 300274.SZ as of 2026-07-04 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 300274.SZ as of 2026-07-04 |
| company_business_model | not_applicable | # Company Business Model Primer for 300274.SZ as of 2026-07-04 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 300274.SZ as of 2026-07-04 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 300274.SZ as of 2026-07-04 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 300274.SZ as of 2026-07-04 |
| commodity_product_price | ready | # Commodity and product price context for 300274.SZ as of 2026-07-04 |
| price_move_attribution | ready | # Price-move attribution context for 300274.SZ as of 2026-07-04 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 300274.SZ as of 2026-07-04 |
| shipping_cycle | not_applicable | # Shipping cycle context for 300274.SZ as of 2026-07-04 |
| financial_report_intelligence | ready | # Financial-report intelligence for 300274.SZ as of 2026-07-04 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 300274.SZ as of 2026-07-04 |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 300274.SZ as of 2026-07-04 |
| earnings_model | ready | # Earnings-model context for 300274.SZ as of 2026-07-04 |
| market_expectation | ready | # Market-expectation context for 300274.SZ as of 2026-07-04 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 300274.SZ as of 2026-07-04 |
| management_capital_allocation | ready | # Management and capital-allocation context for 300274.SZ as of 2026-07-04 |
| shareholder_structure | ready | # Shareholder-structure context for 300274.SZ as of 2026-07-04 |
| investor_interaction | ready | # Investor interaction context for 300274.SZ as of 2026-07-04 |
| policy_planning | ready | # Policy-planning context for 300274.SZ as of 2026-07-04 |
| web_fact_check | ready | # Web fact-check context for 300274.SZ as of 2026-07-04 |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 300274.SZ |
| baijiu | not_applicable | # Baijiu verification context for 300274.SZ as of 2026-07-04 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 300274.SZ as of 2026-07-04 |
| dividend_defensive | ready | # Dividend defensive verification context for 300274.SZ as of 2026-07-04 |
| building_materials | not_applicable | # Building-materials verification context for 300274.SZ as of 2026-07-04 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 300274.SZ |
| optical_module | not_applicable | # AI optical-module context for 300274.SZ |
| biopharma | not_applicable | # Biopharma verification context for 300274.SZ |
| software | not_applicable | # Software verification context for 300274.SZ |
| insurance | not_applicable | # Insurance verification context for 300274.SZ as of 2026-07-04 |
| medical_device | ready | # Medical-device verification context for 300274.SZ as of 2026-07-04 |
| metals_mining | not_applicable | # Metals-mining verification context for 300274.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_op... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 7,129,735,973.85 致； 主要系收到的银行承兑汇票 ... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: / Rebar / steel cost proxy / Tushare futures proxy / RB.SHF / 3062 / 20260703 / -0.94% / N/A / Verified by Tushare futures daily data. / exchange=SHFE, query... |
| metals/mining | Reserve / resource quality | ready | thesis_question_context: / G-3 / What would make the bull case clearly wrong, and what would make the bear case clearly wrong? / state falsification signals and upgrade triggers with... |
| metals/mining | Equity output / volume | ready | commodity_product_price: / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cost, and cash-flow conversi... |
| metals/mining | AISC / unit cost | ready | commodity_product_price: / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cost, and cash-flow conversi... |
| metals/mining | NAV / SOTP | partial | medical_device: / Distributor / overseas channel checks / channel inventory, sell-through, localization, FX, service network / neutral retrieval task when unavailable; do no... |
| metals/mining | Capex / project ramp | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.