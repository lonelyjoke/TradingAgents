# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 601689.SH as of 2026-06-29 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 601689.SH as of 2026-06-29 |
| company_business_model | not_applicable | # Company Business Model Primer for 601689.SH as of 2026-06-29 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 601689.SH as of 2026-06-29 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 601689.SH as of 2026-06-29 |
| sell_side_quality_audit | ready | Weak or incomplete modules: none detected from supplied contexts |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 601689.SH as of 2026-06-29 |
| commodity_product_price | ready | # Commodity and product price context for 601689.SH as of 2026-06-29 |
| price_move_attribution | ready | # Price-move attribution context for 601689.SH as of 2026-06-29 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 601689.SH as of 2026-06-29 |
| shipping_cycle | not_applicable | # Shipping cycle context for 601689.SH as of 2026-06-29 |
| financial_report_intelligence | ready | # Financial-report intelligence for 601689.SH as of 2026-06-29 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 601689.SH as of 2026-06-29 |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 601689.SH as of 2026-06-29 |
| earnings_model | ready | # Earnings-model context for 601689.SH as of 2026-06-29 |
| market_expectation | ready | # Market-expectation context for 601689.SH as of 2026-06-29 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 601689.SH as of 2026-06-29 |
| management_capital_allocation | ready | # Management and capital-allocation context for 601689.SH as of 2026-06-29 |
| shareholder_structure | ready | # Shareholder-structure context for 601689.SH as of 2026-06-29 |
| investor_interaction | ready | # Investor interaction context for 601689.SH as of 2026-06-29 |
| policy_planning | ready | # Policy-planning context for 601689.SH as of 2026-06-29 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 601689.SH |
| baijiu | not_applicable | # Baijiu verification context for 601689.SH as of 2026-06-29 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 601689.SH as of 2026-06-29 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 601689.SH as of 2026-06-29 |
| building_materials | not_applicable | # Building-materials verification context for 601689.SH as of 2026-06-29 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 601689.SH |
| optical_module | not_applicable | # AI optical-module context for 601689.SH |
| biopharma | not_applicable | # Biopharma verification context for 601689.SH |
| software | not_applicable | # Software verification context for 601689.SH |
| insurance | not_applicable | # Insurance verification context for 601689.SH as of 2026-06-29 |
| medical_device | not_applicable | # Medical-device verification context for 601689.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 601689.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitabi... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 拓普集团2025年年... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / visibility_not_yet_profit... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 拓普集团2026年第一季度报告: 交易性金融资产 601,000,000.00 400,0... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth is conditional because visibility_not_yet_profitability weakens durability. / quantified disclosure / 拓普集团2025年年度报告... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclos... | primary_or_structured_filing | model_estimate | 2025, 年度, 2026 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| automotive components | Customer/model volume bridge | missing | No explicit source-backed evidence found. |
| automotive components | Content per vehicle / ASP | ready | thematic_catalyst: / overseas-expansion / business-realization / 拓普集团2025年年度报告: 鹏等车企的合作不断扩大，单车配套金额及订单量持续提升。在国际市场，公司与美国的创新车 / no / no / |
| automotive components | Segment revenue / gross margin | ready | industry_kpi_checklist: / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitabi... |
| automotive components | Capacity utilization / SOP | ready | thematic_catalyst: / capacity-release / business-realization / 拓普集团2025年年度报告: 洲本土订单奠定基础。与此同时，泰国生产基地将于 2026 年上半年建成投产，可以进一步完善国 / filing-backed + monetization evidence / supply ca... |
| automotive components | Working capital / FCF | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| automotive components | Incremental ROIC | ready | forecast_model_scaffold: Reinvestment: 资本密集：年研发投入约占收入5%，产能扩张（波兰二期、泰国一期等）需要大量资本开支，在建工程和固定资产占比较高。再投资回报需待产能爬坡后释放，短期内ROIC承压。 |
| automotive components | Second-curve order-to-revenue | ready | thematic_catalyst: / 机器人 / business-realization / 拓普集团2026年第一季度报告: 司－华夏中证机器人 / no / no / |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, keep the rating label clean and put the limitation in conviction, sizing, Evidence Gaps, and Verification Calendar. Use an evidence-limited rating label only when a core module for the thesis is failed/partial or the decisive valuation driver lacks direct evidence.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as rating-strength guardrails. Missing thesis-critical variables should cap conviction and normally prevent Buy/Overweight unless downside is independently bounded and the missing variable is explicitly placed in the Verification Calendar.