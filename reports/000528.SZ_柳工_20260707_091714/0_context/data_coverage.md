# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 000528.SZ as of 2026-07-07 |
| industry_cycle_scan | partial | Cycle verdict: cycle evidence insufficient |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 000528.SZ as of 2026-07-07 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 000528.SZ as of 2026-07-07 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure, Industry cycle stage, Three-year forecast bridge, Battery forecast bridge |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 000528.SZ as of 2026-07-07 |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 000528.SZ as of 2026-07-07 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | failed | # Relative strength / index linkage context unavailable |
| shipping_cycle | not_applicable | # Shipping cycle context for 000528.SZ as of 2026-07-07 |
| financial_report_intelligence | ready | # Financial-report intelligence for 000528.SZ as of 2026-07-07 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 000528.SZ as of 2026-07-07 |
| supply_chain_comparison | failed | # Supply-chain position comparison unavailable |
| earnings_model | ready | # Earnings-model context for 000528.SZ as of 2026-07-07 |
| market_expectation | ready | # Market-expectation context for 000528.SZ as of 2026-07-07 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 000528.SZ as of 2026-07-07 |
| management_capital_allocation | ready | # Management and capital-allocation context for 000528.SZ as of 2026-07-07 |
| shareholder_structure | ready | # Shareholder-structure context for 000528.SZ as of 2026-07-07 |
| investor_interaction | ready | # Investor interaction context for 000528.SZ as of 2026-07-07 |
| policy_planning | partial | / 中共中央关于制定国民经济和社会发展第十五个五年规划的建议 / 中国政府网 / 2025-10-28 / national-plan / failed / https://www.gov.cn/gongbao/2025/issue_12386/202511/content_7047415.html / |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | partial | # Knowledge Planet Alternative Intelligence Context for 000528.SZ |
| baijiu | not_applicable | # Baijiu verification context for 000528.SZ as of 2026-07-07 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 000528.SZ as of 2026-07-07 |
| dividend_defensive | ready | # Dividend defensive verification context for 000528.SZ as of 2026-07-07 |
| building_materials | not_applicable | # Building-materials verification context for 000528.SZ as of 2026-07-07 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 000528.SZ |
| optical_module | not_applicable | # AI optical-module context for 000528.SZ |
| biopharma | not_applicable | # Biopharma verification context for 000528.SZ |
| software | not_applicable | # Software verification context for 000528.SZ |
| insurance | not_applicable | # Insurance verification context for 000528.SZ as of 2026-07-07 |
| medical_device | not_applicable | # Medical-device verification context for 000528.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 000528.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | valuation input | / partial / annual/quarterly/semiannual / none / 9/9 / thin / Readable filings exist, but either cross-period coverage or answer density is incomplete; use f... | primary_or_structured_filing | reported_fact | unspecified |
| KF02 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 202... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF03 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF04 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / contract_liabilities: 202... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF05 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF06 | financial_report_intelligence | calculated | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | calculation | 2025, 年度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / contract_liabilities: 2026年一季度报告: 短期借款 7,534,350,347.67 5,... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF09 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth is conditional because leverage_funding_growth weakens durability. / quantified disclosure / 2025年年度报告: 销业务成功开拓国内多个... | primary_or_structured_filing | reported_fact | 2025, 年度, 20251231 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度, 2030 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| battery / energy storage | Power-battery shipments / share | missing | sell_side_quality_audit: / Battery forecast bridge / partial / battery forecast must show segment GWh x ASP, segment margins, earnings/FCF conversion, scenario inputs, and monotonic ... |
| battery / energy storage | Energy-storage shipments / orders | ready | thematic_catalyst: / 储能 / business-realization / 2025年半年度报告: 条储能方案，为全球客户提供多元化能源解决方案。 / no / no / |
| battery / energy storage | Battery ASP / pass-through | partial | forecast_model_scaffold: / KPE04 / realized ASP / price pass-through / private/proxy prior; quantify delta or reject, never use as a hard fact / cross-check with filings/Tushare/pric... |
| battery / energy storage | Lithium/material cost | ready | thematic_catalyst: / unclassified / investor-interaction / tier-3 narrative option / small imagination premium only / cninfo_irm / Q: 请问公司今年产品涨价情况，如有，产品的综合涨幅能否覆盖上游原材料的涨幅，谢谢！ / ... |
| battery / energy storage | Capacity utilization | ready | thesis_question_context: / G-3 / What would make the bull case clearly wrong, and what would make the bear case clearly wrong? / state falsification signals and upgrade triggers with... |
| battery / energy storage | Segment gross margin | ready | industry_kpi_checklist: / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 202... |
| battery / energy storage | OCF / FCF / capex | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.