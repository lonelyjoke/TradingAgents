# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 002470.SZ as of 2026-08-08 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 002470.SZ as of 2026-08-08 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 002470.SZ as of 2026-08-08 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 002470.SZ as of 2026-08-08 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from 2cf7e801116f42e7cd3ba98fee91d3e6274f2176.pdf. / |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 002470.SZ as of 2026-08-08 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 002470.SZ as of 2026-08-08 |
| shipping_cycle | not_applicable | # Shipping cycle context for 002470.SZ as of 2026-08-08 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from 2cf7e801116f42e7cd3ba98fee91d3e6274f2176.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 002470.SZ as of 2026-08-08 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 002470.SZ as of 2026-08-08 |
| earnings_model | ready | # Earnings-model context for 002470.SZ as of 2026-08-08 |
| company_events | ready | # Tushare A-share event research for 002470.SZ as of 2026-08-08 |
| market_expectation | ready | # Market-expectation context for 002470.SZ as of 2026-08-08 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 002470.SZ as of 2026-08-08 |
| management_capital_allocation | ready | # Management and capital-allocation context for 002470.SZ as of 2026-08-08 |
| shareholder_structure | ready | # Shareholder-structure context for 002470.SZ as of 2026-08-08 |
| investor_interaction | ready | # Investor interaction context for 002470.SZ as of 2026-08-08 |
| policy_planning | ready | # Policy-planning context for 002470.SZ as of 2026-08-08 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 002470.SZ |
| baijiu | not_applicable | # Baijiu verification context for 002470.SZ as of 2026-08-08 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 002470.SZ as of 2026-08-08 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 002470.SZ as of 2026-08-08 |
| building_materials | not_applicable | # Building-materials verification context for 002470.SZ as of 2026-08-08 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 002470.SZ |
| optical_module | not_applicable | # AI optical-module context for 002470.SZ |
| biopharma | not_applicable | # Biopharma verification context for 002470.SZ |
| software | not_applicable | # Software verification context for 002470.SZ |
| insurance | not_applicable | # Insurance verification context for 002470.SZ as of 2026-08-08 |
| medical_device | not_applicable | # Medical-device verification context for 002470.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 002470.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | valuation input | / partial / annual/quarterly/semiannual / none / 9/9 / thin / Readable filings exist, but either cross-period coverage or answer density is incomplete; use f... | primary_or_structured_filing | reported_fact | unspecified |
| KF02 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / impairment: 2026年一季度报告: 财务费用... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF03 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF04 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / inventory: 2026年一季度报告: （3... | primary_or_structured_filing | reported_fact | 2026, 季度, 上年同期 |
| KF05 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF06 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度, 2026 |
| KF07 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 2026年一季度报告: （3）报告期，投资收益较上年同期增加1612.64%，主要系本期公司对... | primary_or_structured_filing | reported_fact | 2026, 季度, 上年同期 |
| KF09 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| automotive components | Customer/model volume bridge | missing | No explicit source-backed evidence found. |
| automotive components | Content per vehicle / ASP | partial | financial_report_intelligence: / core_product_line / semiannual / 2025年半年度报告: 公司所处行业是肥料行业，公司的主营业务为常规复合肥、新型肥料、磷肥以及土壤调理剂等土壤所需全系列产品的 研发、生产和销售以及为种植户提供相关的种植业解决方案服务。 1、复合肥及磷化工发展状况、趋势 （1）粮食安全战略持续... |
| automotive components | Segment revenue / gross margin | ready | forecast_model_scaffold: / Gross margin / 11.1792% / -0.75pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| automotive components | Capacity utilization / SOP | partial | financial_report_intelligence: / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... |
| automotive components | Working capital / FCF | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| automotive components | Incremental ROIC | partial | financial_report_intelligence: / cash_conversion / quarterly / 主要会计数据和财务指标发生变动的情况及原因 / Did earnings turn into cash? / 2025年三季度报告: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 1、资产负债表项目 单位：元 项目 期末余额 ... |
| automotive components | Second-curve order-to-revenue | partial | financial_report_intelligence: / pre_debate_segment_valuation / valuation / 不同业务、地区、渠道或第二曲线应如何分开估值，而不是简单套一个合并PE/PB？ / 2025年年度报告: 境外业务产生的营业收入或净利润占公司最近一个会计年度经审计营业收入或净利润 10%以上 / quantified di... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.