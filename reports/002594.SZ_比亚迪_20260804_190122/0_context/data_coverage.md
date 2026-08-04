# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 002594.SZ as of 2026-08-04 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 002594.SZ as of 2026-08-04 |
| company_business_model | ready | # Company Business Model Primer for 002594.SZ as of 2026-08-04 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 002594.SZ as of 2026-08-04 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 002594.SZ as of 2026-08-04 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from 28d4ecf7cf185d6513034cc83bc06e2b54f6ec7b.pdf. / |
| commodity_product_price | ready | # Commodity and product price context for 002594.SZ as of 2026-08-04 |
| price_move_attribution | ready | # Price-move attribution context for 002594.SZ as of 2026-08-04 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 002594.SZ as of 2026-08-04 |
| shipping_cycle | not_applicable | # Shipping cycle context for 002594.SZ as of 2026-08-04 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from 28d4ecf7cf185d6513034cc83bc06e2b54f6ec7b.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 002594.SZ as of 2026-08-04 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 002594.SZ as of 2026-08-04 |
| earnings_model | ready | # Earnings-model context for 002594.SZ as of 2026-08-04 |
| company_events | ready | # Tushare A-share event research for 002594.SZ as of 2026-08-04 |
| market_expectation | ready | # Market-expectation context for 002594.SZ as of 2026-08-04 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 002594.SZ as of 2026-08-04 |
| management_capital_allocation | ready | # Management and capital-allocation context for 002594.SZ as of 2026-08-04 |
| shareholder_structure | ready | # Shareholder-structure context for 002594.SZ as of 2026-08-04 |
| investor_interaction | ready | # Investor interaction context for 002594.SZ as of 2026-08-04 |
| policy_planning | ready | # Policy-planning context for 002594.SZ as of 2026-08-04 |
| web_fact_check | ready | # Web fact-check context for 002594.SZ as of 2026-08-04 |
| knowledge_planet | partial | / KPE07 / 2026-07-29T09:00 / stream_item:18730 / industry_weekly_data / private_data_requires_methodology_check / KPI/forecast proxy / 20260728复盘 人工智... 20260728复盘 人工智能： 1. 康宁财报... |
| baijiu | not_applicable | # Baijiu verification context for 002594.SZ as of 2026-08-04 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 002594.SZ as of 2026-08-04 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 002594.SZ as of 2026-08-04 |
| building_materials | not_applicable | # Building-materials verification context for 002594.SZ as of 2026-08-04 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 002594.SZ |
| optical_module | ready | # AI optical-module context for 002594.SZ as of 2026-08-04 |
| biopharma | not_applicable | # Biopharma verification context for 002594.SZ |
| software | not_applicable | # Software verification context for 002594.SZ |
| insurance | not_applicable | # Insurance verification context for 002594.SZ as of 2026-08-04 |
| medical_device | not_applicable | # Medical-device verification context for 002594.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 002594.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_op... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 2026年一季度报告: 减： 所得税费用 735,464,000.00 1,747,743,0... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_new-product-platform / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified discl... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| metals/mining | Reserve / resource quality | ready | company_business_model: / core_product_line / annual / 2025年年度报告: 营业收入合计 803,964,958,000.00 100% 777,102,455,000.00 100% 3.46% 分行业 日用电子器件制 155,236,528,000.00 19.31% 159,608,576,000.... |
| metals/mining | Equity output / volume | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | AISC / unit cost | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | NAV / SOTP | partial | company_events: If a section is unavailable because of data permission, state that limitation explicitly. |
| metals/mining | Capex / project ramp | ready | thesis_question_context: / OM-2 / Can cash conversion keep up with reported AI growth? / prove OCF, receivables, inventory, and capex discipline / attack working-capital absorption a... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.