# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 001309.SZ as of 2026-07-13 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 001309.SZ as of 2026-07-13 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 001309.SZ as of 2026-07-13 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 001309.SZ as of 2026-07-13 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Thesis-to-financial transmission, Moat evidence tests, Valuation closure |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 001309.SZ as of 2026-07-13 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 001309.SZ as of 2026-07-13 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 001309.SZ as of 2026-07-13 |
| shipping_cycle | not_applicable | # Shipping cycle context for 001309.SZ as of 2026-07-13 |
| financial_report_intelligence | ready | # Financial-report intelligence for 001309.SZ as of 2026-07-13 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 001309.SZ as of 2026-07-13 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 001309.SZ as of 2026-07-13 |
| earnings_model | ready | # Earnings-model context for 001309.SZ as of 2026-07-13 |
| company_events | ready | # Tushare A-share event research for 001309.SZ as of 2026-07-13 |
| market_expectation | ready | # Market-expectation context for 001309.SZ as of 2026-07-13 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 001309.SZ as of 2026-07-13 |
| management_capital_allocation | ready | # Management and capital-allocation context for 001309.SZ as of 2026-07-13 |
| shareholder_structure | ready | # Shareholder-structure context for 001309.SZ as of 2026-07-13 |
| investor_interaction | ready | # Investor interaction context for 001309.SZ as of 2026-07-13 |
| policy_planning | ready | # Policy-planning context for 001309.SZ as of 2026-07-13 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 001309.SZ |
| baijiu | not_applicable | # Baijiu verification context for 001309.SZ as of 2026-07-13 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 001309.SZ as of 2026-07-13 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 001309.SZ as of 2026-07-13 |
| building_materials | not_applicable | # Building-materials verification context for 001309.SZ as of 2026-07-13 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 001309.SZ |
| optical_module | not_applicable | # AI optical-module context for 001309.SZ |
| biopharma | not_applicable | # Biopharma verification context for 001309.SZ |
| software | not_applicable | # Software verification context for 001309.SZ |
| insurance | not_applicable | # Insurance verification context for 001309.SZ as of 2026-07-13 |
| medical_device | not_applicable | # Medical-device verification context for 001309.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 001309.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 致 主... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: ... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 致 主要系销售收入增长，收到的银行承兑 应收票据 87,806,0... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_new-product-platform / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified discl... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| consumer staples | Sell-through / channel inventory | ready | thematic_catalyst: / capacity-release / business-realization / 2025年年度报告: 纷纷提前锁定原厂长期订单，带来企业级存储行业需求的快速增长。在需求缺口的推动下存储原厂产能加速向企业级存 / filing-backed + monetization evidence / supply ... |
| consumer staples | Price system / ASP | ready | industry_kpi_checklist: / high_r_and_d_technology / 高研发技术产品型 / quantified disclosure / 2025年年度报告: 片到解决方案的战略闭环。公司通过构建分层、模块化的公共研发平台来厚植技术根基，加速自研算法与关键 IP 的组件 公司将围绕“自主可控、生态共赢”策略，强化产业链上下游... |
| consumer staples | Contract liabilities | ready | financial_report_intelligence: / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: ... |
| consumer staples | Gross margin and raw materials | ready | forecast_model_scaffold: / Gross margin / 57.4202% / +51.57pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| consumer staples | Food safety / quality risk | missing | No explicit source-backed evidence found. |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.