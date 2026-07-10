# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 000933.SZ as of 2026-07-09 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 000933.SZ as of 2026-07-09 |
| company_business_model | ready | # Company Business Model Primer for 000933.SZ as of 2026-07-09 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 000933.SZ as of 2026-07-09 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 000933.SZ as of 2026-07-09 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure, Aluminum spread driver coverage |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 000933.SZ as of 2026-07-09 |
| commodity_product_price | ready | # Commodity and product price context for 000933.SZ as of 2026-07-09 |
| price_move_attribution | ready | # Price-move attribution context for 000933.SZ as of 2026-07-09 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 000933.SZ as of 2026-07-09 |
| shipping_cycle | not_applicable | # Shipping cycle context for 000933.SZ as of 2026-07-09 |
| financial_report_intelligence | ready | # Financial-report intelligence for 000933.SZ as of 2026-07-09 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 000933.SZ as of 2026-07-09 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 000933.SZ as of 2026-07-09 |
| earnings_model | ready | # Earnings-model context for 000933.SZ as of 2026-07-09 |
| market_expectation | ready | # Market-expectation context for 000933.SZ as of 2026-07-09 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 000933.SZ as of 2026-07-09 |
| management_capital_allocation | ready | # Management and capital-allocation context for 000933.SZ as of 2026-07-09 |
| shareholder_structure | ready | # Shareholder-structure context for 000933.SZ as of 2026-07-09 |
| investor_interaction | ready | # Investor interaction context for 000933.SZ as of 2026-07-09 |
| policy_planning | ready | # Policy-planning context for 000933.SZ as of 2026-07-09 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 000933.SZ |
| baijiu | not_applicable | # Baijiu verification context for 000933.SZ as of 2026-07-09 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 000933.SZ as of 2026-07-09 |
| dividend_defensive | ready | # Dividend defensive verification context for 000933.SZ as of 2026-07-09 |
| building_materials | not_applicable | # Building-materials verification context for 000933.SZ as of 2026-07-09 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 000933.SZ |
| optical_module | not_applicable | # AI optical-module context for 000933.SZ |
| biopharma | not_applicable | # Biopharma verification context for 000933.SZ |
| software | not_applicable | # Software verification context for 000933.SZ |
| insurance | not_applicable | # Insurance verification context for 000933.SZ as of 2026-07-09 |
| medical_device | not_applicable | # Medical-device verification context for 000933.SZ |
| metals_mining | ready | # Metals-mining verification context for 000933.SZ as of 2026-07-09 |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 2026年一季... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度, 2002 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgra... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 价值发生变动。 报告期内，公司铝加工板块量价齐 3 应收账款 1,... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度, 2002 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / already monetized; can enter core valuation if margin and cash conversion are also visible. / quantified disclosure / 20... | primary_or_structured_filing | model_estimate | 2026, 季度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| consumer staples | Sell-through / channel inventory | ready | financial_report_intelligence: / impairment / quarterly / 2026年一季度报告: 报告期末，公司铝加工板块应收账 款规模增加，根据会计政策以固定 17 信用减值损失 -7,873,058.09 -2,019,699.18 -289.81 / Impairment lines expose the cost of pr... |
| consumer staples | Price system / ASP | ready | thesis_question_context: / AL-1 / Is the company a low-cost integrated aluminum profit pool, or just an aluminum-price beta vehicle? / prove realized aluminum ASP, alumina self-suppl... |
| consumer staples | Contract liabilities | ready | financial_report_intelligence: / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026... |
| consumer staples | Gross margin and raw materials | ready | thesis_question_context: / AL-1 / Is the company a low-cost integrated aluminum profit pool, or just an aluminum-price beta vehicle? / prove realized aluminum ASP, alumina self-suppl... |
| consumer staples | Food safety / quality risk | missing | No explicit source-backed evidence found. |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.