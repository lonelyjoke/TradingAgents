# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 600309.SH as of 2026-06-30 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 600309.SH as of 2026-06-30 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 600309.SH as of 2026-06-30 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 600309.SH as of 2026-06-30 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 600309.SH as of 2026-06-30 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 600309.SH as of 2026-06-30 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 600309.SH as of 2026-06-30 |
| shipping_cycle | not_applicable | # Shipping cycle context for 600309.SH as of 2026-06-30 |
| financial_report_intelligence | ready | # Financial-report intelligence for 600309.SH as of 2026-06-30 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 600309.SH as of 2026-06-30 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 600309.SH as of 2026-06-30 |
| earnings_model | ready | # Earnings-model context for 600309.SH as of 2026-06-30 |
| market_expectation | ready | # Market-expectation context for 600309.SH as of 2026-06-30 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 600309.SH as of 2026-06-30 |
| management_capital_allocation | ready | # Management and capital-allocation context for 600309.SH as of 2026-06-30 |
| shareholder_structure | ready | # Shareholder-structure context for 600309.SH as of 2026-06-30 |
| investor_interaction | ready | # Investor interaction context for 600309.SH as of 2026-06-30 |
| policy_planning | ready | # Policy-planning context for 600309.SH as of 2026-06-30 |
| web_fact_check | ready | # Web fact-check context for 600309.SH as of 2026-06-30 |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 600309.SH |
| baijiu | not_applicable | # Baijiu verification context for 600309.SH as of 2026-06-30 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 600309.SH as of 2026-06-30 |
| dividend_defensive | ready | # Dividend defensive verification context for 600309.SH as of 2026-06-30 |
| building_materials | ready | # Building-materials verification context for 600309.SH as of 2026-06-30 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 600309.SH |
| optical_module | not_applicable | # AI optical-module context for 600309.SH |
| biopharma | not_applicable | # Biopharma verification context for 600309.SH |
| software | ready | # Software verification context for 600309.SH as of 2026-06-30 |
| insurance | not_applicable | # Insurance verification context for 600309.SH as of 2026-06-30 |
| medical_device | not_applicable | # Medical-device verification context for 600309.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 600309.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | valuation input | / partial / annual/quarterly/semiannual / none / 9/9 / thin / Readable filings exist, but either cross-period coverage or answer density is incomplete; use f... | primary_or_structured_filing | reported_fact | unspecified |
| KF02 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 万华化学202... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF03 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 万华化学2025年年... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF04 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 万华化学... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF05 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF06 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 万华化学2026年一季度报告: 交易性金融资产 2,502,946,515.31 衍生金融... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF09 | financial_report_intelligence | calculated | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | calculation | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| bank | NIM / net interest spread | ready | financial_report_intelligence: For banks, preserve the exact spread terminology from filings: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. If the filing only supports 净利差 1.77% and ... |
| bank | Asset quality | missing | No explicit source-backed evidence found. |
| bank | Capital adequacy | missing | No explicit source-backed evidence found. |
| bank | ROE / PB valuation bridge | ready | thesis_question_context: / ts_code / name / industry / total_mv / total_mv_cny_100m / pe_ttm / pb / ps_ttm / dv_ttm / roe_annual / roa_annual / roe / roa / netprofit_yoy / debt_to_as... |
| bank | Dividend coverage | ready | industry_kpi_checklist: / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... |
| insurance | NBV growth and margin | missing | No explicit source-backed evidence found. |
| insurance | EV / CSM bridge | missing | No explicit source-backed evidence found. |
| insurance | Solvency and capital | missing | No explicit source-backed evidence found. |
| insurance | P&C COR | ready | thesis_question_context: / ts_code / name / industry / total_mv / total_mv_cny_100m / pe_ttm / pb / ps_ttm / dv_ttm / roe_annual / roa_annual / roe / roa / netprofit_yoy / debt_to_as... |
| insurance | Dividend coverage | ready | industry_kpi_checklist: / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.