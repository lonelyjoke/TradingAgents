# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 300274.SZ as of 2026-07-08 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 300274.SZ as of 2026-07-08 |
| company_business_model | ready | # Company Business Model Primer for 300274.SZ as of 2026-07-08 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 300274.SZ as of 2026-07-08 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 300274.SZ as of 2026-07-08 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 300274.SZ as of 2026-07-08 |
| commodity_product_price | ready | # Commodity and product price context for 300274.SZ as of 2026-07-08 |
| price_move_attribution | ready | # Price-move attribution context for 300274.SZ as of 2026-07-08 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 300274.SZ as of 2026-07-08 |
| shipping_cycle | not_applicable | # Shipping cycle context for 300274.SZ as of 2026-07-08 |
| financial_report_intelligence | ready | # Financial-report intelligence for 300274.SZ as of 2026-07-08 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 300274.SZ as of 2026-07-08 |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 300274.SZ as of 2026-07-08 |
| earnings_model | ready | # Earnings-model context for 300274.SZ as of 2026-07-08 |
| market_expectation | ready | # Market-expectation context for 300274.SZ as of 2026-07-08 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 300274.SZ as of 2026-07-08 |
| management_capital_allocation | ready | # Management and capital-allocation context for 300274.SZ as of 2026-07-08 |
| shareholder_structure | ready | # Shareholder-structure context for 300274.SZ as of 2026-07-08 |
| investor_interaction | ready | # Investor interaction context for 300274.SZ as of 2026-07-08 |
| policy_planning | ready | # Policy-planning context for 300274.SZ as of 2026-07-08 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 300274.SZ |
| baijiu | not_applicable | # Baijiu verification context for 300274.SZ as of 2026-07-08 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 300274.SZ as of 2026-07-08 |
| dividend_defensive | ready | # Dividend defensive verification context for 300274.SZ as of 2026-07-08 |
| building_materials | not_applicable | # Building-materials verification context for 300274.SZ as of 2026-07-08 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 300274.SZ |
| optical_module | not_applicable | # AI optical-module context for 300274.SZ |
| biopharma | not_applicable | # Biopharma verification context for 300274.SZ |
| software | not_applicable | # Software verification context for 300274.SZ |
| insurance | not_applicable | # Insurance verification context for 300274.SZ as of 2026-07-08 |
| medical_device | not_applicable | # Medical-device verification context for 300274.SZ |
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
| clean-energy power electronics | PV inverter shipments / regional mix | missing | No explicit source-backed evidence found. |
| clean-energy power electronics | ESS awarded orders / backlog | ready | thematic_catalyst: / order-ramp / business-realization / 2026年一季度报告: 合同负债 12,204,269,402.38 10,655,117,674.16 / no / no / |
| clean-energy power electronics | ESS ASP / battery-cost pass-through | ready | company_business_model: / investor_interaction / / 2026-04-28 / 2026-05-14 / “市场传闻Q1储能业务出现了‘面粉比面包贵’的倒挂现象。请披露Q1储能系统的实际毛利率区间。对于碳酸锂等原材料涨价，公司是依靠牺牲毛利保份额，还是已通过新订单实现了成本传导？” / 感谢您对公司的关注。202... |
| clean-energy power electronics | Segment gross margin / unit profit | ready | company_business_model: / high_r_and_d_technology / 高研发技术产品型 / quantified disclosure / 2025年半年度报告: 三、主营业务分析 （一）主营业务分析概述 报告期内，公司实现营业收入 435.33 亿元，同比增加 40.34%；营业成本 285.76 亿元，同比增加 36.31... |
| clean-energy power electronics | Orders-to-cash conversion | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |
| clean-energy power electronics | Bankability / certification / service moat | ready | company_business_model: / energy-storage / contracted / 2025年年度报告: 分布式电源 指 分布式电源装置，即功率为数千瓦至 50MW 小型模块式的、与环境兼容的独立电源 储能 指 电能的储存 UL 指 权威认证机构，全球应用安全科学专家，服务全球 100 多个国家和地区的客户 / eligible f... |
| clean-energy power electronics | AIDC / SST commercialization | ready | forecast_model_scaffold: / UQ04 / What is the realistic revenue and profit contribution from AIDC storage and SST power beyond 2027, and can SunGrow's first-mover advantage translate... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.