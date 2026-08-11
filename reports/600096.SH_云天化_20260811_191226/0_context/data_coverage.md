# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 600096.SH as of 2026-08-11 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 600096.SH as of 2026-08-11 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 600096.SH as of 2026-08-11 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 600096.SH as of 2026-08-11 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 云天化2025年第三季度报告: PDF downloaded but no readable text was extracted from 092f08a4bdb2cca6305817247ab8617880fcc590.pdf. / |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 600096.SH as of 2026-08-11 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 600096.SH as of 2026-08-11 |
| shipping_cycle | not_applicable | # Shipping cycle context for 600096.SH as of 2026-08-11 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 云天化2025年第三季度报告: PDF downloaded but no readable text was extracted from 092f08a4bdb2cca6305817247ab8617880fcc590.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 600096.SH as of 2026-08-11 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 600096.SH as of 2026-08-11 |
| earnings_model | ready | # Earnings-model context for 600096.SH as of 2026-08-11 |
| company_events | ready | # Tushare A-share event research for 600096.SH as of 2026-08-11 |
| market_expectation | ready | # Market-expectation context for 600096.SH as of 2026-08-11 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 600096.SH as of 2026-08-11 |
| management_capital_allocation | ready | # Management and capital-allocation context for 600096.SH as of 2026-08-11 |
| shareholder_structure | ready | # Shareholder-structure context for 600096.SH as of 2026-08-11 |
| investor_interaction | ready | # Investor interaction context for 600096.SH as of 2026-08-11 |
| policy_planning | ready | # Policy-planning context for 600096.SH as of 2026-08-11 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 600096.SH |
| baijiu | not_applicable | # Baijiu verification context for 600096.SH as of 2026-08-11 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 600096.SH as of 2026-08-11 |
| dividend_defensive | ready | # Dividend defensive verification context for 600096.SH as of 2026-08-11 |
| building_materials | not_applicable | # Building-materials verification context for 600096.SH as of 2026-08-11 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 600096.SH |
| optical_module | not_applicable | # AI optical-module context for 600096.SH |
| biopharma | not_applicable | # Biopharma verification context for 600096.SH |
| software | not_applicable | # Software verification context for 600096.SH |
| insurance | not_applicable | # Insurance verification context for 600096.SH as of 2026-08-11 |
| medical_device | not_applicable | # Medical-device verification context for 600096.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 600096.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitabi... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 云天化2025年年度... | primary_or_structured_filing | model_estimate | 2025, 年度, 2024 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / visibility_not_yet_profit... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2024, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgra... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2024, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 云天化2024年第三季度报告: 交易性金融资产 931,700.00 85,900.00 ... | primary_or_structured_filing | reported_fact | 2024, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth is conditional because visibility_not_yet_profitability weakens durability. / quantified disclosure / 云天化2025年年度报告:... | primary_or_structured_filing | reported_fact | 2025, 年度, 20251231 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclos... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_new-product-platform / already monetized; can enter core valuation if margin and cash conversion are also visible. / quantified disclosure / ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| consumer staples | Sell-through / channel inventory | partial | financial_report_intelligence: / inventory / quarterly / 云天化2024年第三季度报告: 应收股利 0 16,400,000.00 买入返售金融资产 0 0 存货 5,075,462,348.52 7,544,576,139.23 / Inventory reveals whether production is ah... |
| consumer staples | Price system / ASP | private_proxy | knowledge_planet: / KPE02 / 2026-08-10T13:31 / stream_item:23037 / channel_check / high_private_channel_hard_to_verify / probability/verification proxy / 化工金秋，低位重估 当前化工... 化工金... |
| consumer staples | Contract liabilities | ready | industry_kpi_checklist: / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 云天化2024年第三季度报告: 交易性金融资产 931,700.00 85,900.00 ... |
| consumer staples | Gross margin and raw materials | ready | industry_kpi_checklist: / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitabi... |
| consumer staples | Food safety / quality risk | missing | No explicit source-backed evidence found. |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.
- Treat `private_proxy` rows from Knowledge Planet as alternative-intelligence clues only. They may adjust probabilities, timing, sizing, or verification tasks, but they cannot serve as filing-grade facts unless cross-checked by announcements, Tushare/financial data, reputable news, or market price/volume evidence.