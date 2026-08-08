# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 300723.SZ as of 2026-08-08 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 300723.SZ as of 2026-08-08 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 300723.SZ as of 2026-08-08 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 300723.SZ as of 2026-08-08 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 2025年年度报告: PDF downloaded but no readable text was extracted from c94be0ac8fa58e7f93add8974c086f8d92dd6c9d.pdf. / |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 300723.SZ as of 2026-08-08 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 300723.SZ as of 2026-08-08 |
| shipping_cycle | not_applicable | # Shipping cycle context for 300723.SZ as of 2026-08-08 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 2025年年度报告: PDF downloaded but no readable text was extracted from c94be0ac8fa58e7f93add8974c086f8d92dd6c9d.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 300723.SZ as of 2026-08-08 |
| supply_chain_comparison | not_applicable | # Supply-chain position comparison for 300723.SZ as of 2026-08-08 |
| earnings_model | ready | # Earnings-model context for 300723.SZ as of 2026-08-08 |
| company_events | ready | # Tushare A-share event research for 300723.SZ as of 2026-08-08 |
| market_expectation | failed | # Market-expectation context unavailable |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 300723.SZ as of 2026-08-08 |
| management_capital_allocation | ready | # Management and capital-allocation context for 300723.SZ as of 2026-08-08 |
| shareholder_structure | ready | # Shareholder-structure context for 300723.SZ as of 2026-08-08 |
| investor_interaction | ready | # Investor interaction context for 300723.SZ as of 2026-08-08 |
| policy_planning | ready | # Policy-planning context for 300723.SZ as of 2026-08-08 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 300723.SZ |
| baijiu | not_applicable | # Baijiu verification context for 300723.SZ as of 2026-08-08 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 300723.SZ as of 2026-08-08 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 300723.SZ as of 2026-08-08 |
| building_materials | not_applicable | # Building-materials verification context for 300723.SZ as of 2026-08-08 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 300723.SZ |
| optical_module | not_applicable | # AI optical-module context for 300723.SZ |
| biopharma | ready | # Biopharma verification context for 300723.SZ as of 2026-08-08 |
| software | not_applicable | # Software verification context for 300723.SZ |
| insurance | not_applicable | # Insurance verification context for 300723.SZ as of 2026-08-08 |
| medical_device | not_applicable | # Medical-device verification context for 300723.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 300723.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / {'lens': 'retail_wealth_engi... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 一品红药业集团股份有... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF03 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgra... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | reported | valuation input | / regulated_pipeline / 监管审批 / 产品管线型 / quantified disclosure / 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / archetype_ramp_regulated_pipeline / the primary business archetype sets the company-specific ramp variables; growth is only durable when those variables im... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | insurance-native input | / pre_debate_business_model / business_model / 一品红到底靠什么赚钱，收入、利润和资产之间如何形成经营闭环？ / 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF09 | financial_report_intelligence | estimated | valuation input | / pre_debate_archetype_regulated_pipeline / company_archetype / 核心价值来自已商业化产品，还是监管审批/临床管线的可选项？医保、集采、注册和商业化节奏如何改变利润曲线？ / 一品红药业集团股份有限公司 2026 年第一季度报告 [local disc... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF10 | financial_report_intelligence | reported | valuation input | / pre_debate_archetype_product_manufacturer / company_archetype / 这家公司增长来自价格、销量、产能利用率、产品结构还是成本下降？扩产、库存和原材料波动会怎样影响毛利率和现金流？ / 一品红药业集团股份有限公司 2026 年第一季度报告 [local... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF11 | financial_report_intelligence | estimated | valuation input | / pre_debate_growth_driver / growth_driver / 未来增长主要来自价格、销量/客流、利用率/出租率、产能、客户、区域扩张，还是产品/服务结构升级？ / 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 12 一品红药业... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF12 | financial_report_intelligence | reported | balance-sheet input | / pre_debate_segment_valuation / valuation / 不同业务、地区、渠道或第二曲线应如何分开估值，而不是简单套一个合并PE/PB？ / 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现... | primary_or_structured_filing | reported_fact | 2026, 季度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| metals/mining | Reserve / resource quality | ready | thesis_question_context: / G-3 / What would make the bull case clearly wrong, and what would make the bear case clearly wrong? / state falsification signals and upgrade triggers with... |
| metals/mining | Equity output / volume | partial | commodity_product_price: / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cost, and cash-flow conversi... |
| metals/mining | AISC / unit cost | partial | commodity_product_price: / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cost, and cash-flow conversi... |
| metals/mining | NAV / SOTP | partial | web_fact_check: Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| metals/mining | Capex / project ramp | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.