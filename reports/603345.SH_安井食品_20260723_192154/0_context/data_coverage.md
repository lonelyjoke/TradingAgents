# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 603345.SH as of 2026-07-23 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 603345.SH as of 2026-07-23 |
| company_business_model | ready | # Company Business Model Primer for 603345.SH as of 2026-07-23 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 603345.SH as of 2026-07-23 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 603345.SH as of 2026-07-23 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure, Hog-breeder valuation framework, Hog-cycle private-data bridge |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 安井食品关于参加厦门辖区上市公司2025年年报业绩说明会暨投资者网上集体接待日活动的公告: PDF downloaded but no readable text was extracted from cdbbd46c5a4e9496e47ae7f66c34c93e9fd14b24.pd... |
| commodity_product_price | ready | # Commodity and product price context for 603345.SH as of 2026-07-23 |
| price_move_attribution | ready | # Price-move attribution context for 603345.SH as of 2026-07-23 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 603345.SH as of 2026-07-23 |
| shipping_cycle | not_applicable | # Shipping cycle context for 603345.SH as of 2026-07-23 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 安井食品关于参加厦门辖区上市公司2025年年报业绩说明会暨投资者网上集体接待日活动的公告: PDF downloaded but no readable text was extracted from cdbbd46c5a4e9496e47ae7f66c34c93e9fd14b24.pd... |
| peer_comparison | ready | # Tushare same-industry peer comparison for 603345.SH as of 2026-07-23 |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 603345.SH as of 2026-07-23 |
| earnings_model | ready | # Earnings-model context for 603345.SH as of 2026-07-23 |
| company_events | ready | # Tushare A-share event research for 603345.SH as of 2026-07-23 |
| market_expectation | ready | # Market-expectation context for 603345.SH as of 2026-07-23 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 603345.SH as of 2026-07-23 |
| management_capital_allocation | ready | # Management and capital-allocation context for 603345.SH as of 2026-07-23 |
| shareholder_structure | ready | # Shareholder-structure context for 603345.SH as of 2026-07-23 |
| investor_interaction | ready | # Investor interaction context for 603345.SH as of 2026-07-23 |
| policy_planning | ready | # Policy-planning context for 603345.SH as of 2026-07-23 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 603345.SH |
| baijiu | not_applicable | # Baijiu verification context for 603345.SH as of 2026-07-23 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 603345.SH as of 2026-07-23 |
| dividend_defensive | ready | # Dividend defensive verification context for 603345.SH as of 2026-07-23 |
| building_materials | not_applicable | # Building-materials verification context for 603345.SH as of 2026-07-23 |
| consumer_staples | ready | # Consumer-staples verification context for 603345.SH as of 2026-07-23 |
| optical_module | not_applicable | # AI optical-module context for 603345.SH |
| biopharma | not_applicable | # Biopharma verification context for 603345.SH |
| software | not_applicable | # Software verification context for 603345.SH |
| insurance | not_applicable | # Insurance verification context for 603345.SH as of 2026-07-23 |
| medical_device | not_applicable | # Medical-device verification context for 603345.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 603345.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 安井食品202... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 安井食品2025年年... | primary_or_structured_filing | model_estimate | 2025, 年度, 2024 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 安井食品... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度, 2023 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 安井食品2026年第一季度报告: 交易性金融资产 3,613,546,171.26 3,6... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | calculated | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | calculation | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度, 上年同期 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度, 2023 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclos... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| consumer staples | Sell-through / channel inventory | ready | thesis_question_context: / CS-1 / Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality? / prove sell-through, distributor inventory, contract ... |
| consumer staples | Price system / ASP | ready | thesis_question_context: / CS-2 / Can gross margin improvement survive raw-material, promotion, and mix normalization? / prove cost pass-through and durable high-margin mix / attack ... |
| consumer staples | Contract liabilities | ready | thesis_question_context: / CS-1 / Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality? / prove sell-through, distributor inventory, contract ... |
| consumer staples | Gross margin and raw materials | ready | thesis_question_context: / CS-1 / Is growth driven by real end demand, channel restocking, product mix, or one-off seasonality? / prove sell-through, distributor inventory, contract ... |
| consumer staples | Food safety / quality risk | missing | No explicit source-backed evidence found. |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| metals/mining | Reserve / resource quality | ready | industry_kpi_checklist: / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports ... |
| metals/mining | Equity output / volume | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | AISC / unit cost | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | NAV / SOTP | partial | web_fact_check: Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| metals/mining | Capex / project ramp | ready | industry_kpi_checklist: / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.