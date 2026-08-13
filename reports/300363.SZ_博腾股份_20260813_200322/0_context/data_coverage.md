# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 300363.SZ as of 2026-08-13 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 300363.SZ as of 2026-08-13 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 300363.SZ as of 2026-08-13 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 300363.SZ as of 2026-08-13 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from e6de5b74c6b9c1df8ba1075a884ccfed8fdad063.pdf. / |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 300363.SZ as of 2026-08-13 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 300363.SZ as of 2026-08-13 |
| shipping_cycle | not_applicable | # Shipping cycle context for 300363.SZ as of 2026-08-13 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from e6de5b74c6b9c1df8ba1075a884ccfed8fdad063.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 300363.SZ as of 2026-08-13 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 300363.SZ as of 2026-08-13 |
| earnings_model | ready | # Earnings-model context for 300363.SZ as of 2026-08-13 |
| company_events | ready | # Tushare A-share event research for 300363.SZ as of 2026-08-13 |
| market_expectation | ready | # Market-expectation context for 300363.SZ as of 2026-08-13 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 300363.SZ as of 2026-08-13 |
| management_capital_allocation | ready | # Management and capital-allocation context for 300363.SZ as of 2026-08-13 |
| shareholder_structure | ready | # Shareholder-structure context for 300363.SZ as of 2026-08-13 |
| investor_interaction | ready | # Investor interaction context for 300363.SZ as of 2026-08-13 |
| policy_planning | ready | # Policy-planning context for 300363.SZ as of 2026-08-13 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 300363.SZ |
| baijiu | not_applicable | # Baijiu verification context for 300363.SZ as of 2026-08-13 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 300363.SZ as of 2026-08-13 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 300363.SZ as of 2026-08-13 |
| building_materials | not_applicable | # Building-materials verification context for 300363.SZ as of 2026-08-13 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 300363.SZ |
| optical_module | not_applicable | # AI optical-module context for 300363.SZ |
| biopharma | ready | # Biopharma verification context for 300363.SZ as of 2026-08-13 |
| software | not_applicable | # Software verification context for 300363.SZ |
| insurance | not_applicable | # Insurance verification context for 300363.SZ as of 2026-08-13 |
| medical_device | not_applicable | # Medical-device verification context for 300363.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 300363.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 博腾股份：20... | primary_or_structured_filing | reported_fact | 2024, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 博腾股份... | primary_or_structured_filing | reported_fact | 2024, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2024, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgra... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2024, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 博腾股份：2024年三季度报告: 货币资金 1,402,462,655.01 1,966,... | primary_or_structured_filing | reported_fact | 2024, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | valuation input | / regulated_pipeline / 监管审批 / 产品管线型 / quantified disclosure / 2025年年度报告: 四、主营业务分析 1、概述 （1）2025年总体经营情况 2025年，受Biotech短期融资环境和创新药供应链区域化的影响，中国CDMO行业总体依然面临市场需求和竞争... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_new-product-platform / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified discl... | primary_or_structured_filing | model_estimate | 2024, 季度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| metals/mining | Reserve / resource quality | ready | thesis_question_context: / G-3 / What would make the bull case clearly wrong, and what would make the bear case clearly wrong? / state falsification signals and upgrade triggers with... |
| metals/mining | Equity output / volume | partial | financial_report_intelligence: / inventory / quarterly / 博腾股份：2024年三季度报告: 信用减值损失 -9,884,621.49 38,295,627.42 -48,180,248.91 -125.81 提的坏账准备转回增加所致 主要系本期计提存货跌价准备 / Inventory reveals whether p... |
| metals/mining | AISC / unit cost | partial | commodity_product_price: / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cost, and cash-flow conversi... |
| metals/mining | NAV / SOTP | ready | biopharma: / 2025年半年度报告 / 半年度报告 INTERIM REPORT 股票简称： 博腾股份 股票简称：博腾股份 股票代码： 300363 股票代码：300363 让好药更早惠及大众 全球化、全类别、端到端的制药服务平台 1 2 3 4 小分子原料药 小分子制剂 基因细胞治疗 新分子 服务的药物治疗领域 适应症 ... |
| metals/mining | Capex / project ramp | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.