# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 600031.SH as of 2026-08-02 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 600031.SH as of 2026-08-02 |
| company_business_model | partial | / product_or_commodity / - Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. / |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 600031.SH as of 2026-08-02 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 600031.SH as of 2026-08-02 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 三一重工股份有限公司2026年第一季度报告: PDF downloaded but no readable text was extracted from 31dd730c056aea10f603f7d2d6e58032b43ef8f7.pdf. / |
| commodity_product_price | partial | Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims. |
| price_move_attribution | ready | # Price-move attribution context for 600031.SH as of 2026-08-02 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 600031.SH as of 2026-08-02 |
| shipping_cycle | not_applicable | # Shipping cycle context for 600031.SH as of 2026-08-02 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 三一重工股份有限公司2026年第一季度报告: PDF downloaded but no readable text was extracted from 31dd730c056aea10f603f7d2d6e58032b43ef8f7.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 600031.SH as of 2026-08-02 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 600031.SH as of 2026-08-02 |
| earnings_model | ready | # Earnings-model context for 600031.SH as of 2026-08-02 |
| company_events | ready | # Tushare A-share event research for 600031.SH as of 2026-08-02 |
| market_expectation | ready | # Market-expectation context for 600031.SH as of 2026-08-02 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 600031.SH as of 2026-08-02 |
| management_capital_allocation | ready | # Management and capital-allocation context for 600031.SH as of 2026-08-02 |
| shareholder_structure | ready | # Shareholder-structure context for 600031.SH as of 2026-08-02 |
| investor_interaction | ready | # Investor interaction context for 600031.SH as of 2026-08-02 |
| policy_planning | ready | # Policy-planning context for 600031.SH as of 2026-08-02 |
| web_fact_check | ready | # Web fact-check context for 600031.SH as of 2026-08-02 |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 600031.SH |
| baijiu | not_applicable | # Baijiu verification context for 600031.SH as of 2026-08-02 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 600031.SH as of 2026-08-02 |
| dividend_defensive | ready | # Dividend defensive verification context for 600031.SH as of 2026-08-02 |
| building_materials | not_applicable | # Building-materials verification context for 600031.SH as of 2026-08-02 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 600031.SH |
| optical_module | not_applicable | # AI optical-module context for 600031.SH |
| biopharma | not_applicable | # Biopharma verification context for 600031.SH |
| software | not_applicable | # Software verification context for 600031.SH |
| insurance | not_applicable | # Insurance verification context for 600031.SH as of 2026-08-02 |
| medical_device | not_applicable | # Medical-device verification context for 600031.SH |
| metals_mining | not_applicable | # Metals-mining verification context for 600031.SH |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 三一重工股份有... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 三一重工股份有限公司... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 三一重工... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 三一重工股份有限公司2025年年度报告: 告期间实现归属母公司净利润 84.1 亿元，同比大幅... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_ai-and-digital / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclos... | primary_or_structured_filing | model_estimate | 2025, 年度, 2006 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table. |
| metals/mining | Reserve / resource quality | ready | thesis_question_context: / G-3 / What would make the bull case clearly wrong, and what would make the bear case clearly wrong? / state falsification signals and upgrade triggers with... |
| metals/mining | Equity output / volume | partial | financial_report_intelligence: / inventory / annual / 三一重工股份有限公司2025年年度报告: 告期间实现归属母公司净利润 84.1 亿元，同比大幅增长 41.2%，销售净利率达 9.5%，同比提升 1.7 个百分点。 经营效率持续改善：公司持续优化存货及货款管理水平，存货、在外货款的规模、质量、周 / Inventor... |
| metals/mining | AISC / unit cost | partial | commodity_product_price: / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cost, and cash-flow conversi... |
| metals/mining | NAV / SOTP | partial | web_fact_check: Search provider errors on 1 query path(s); treat this context as unavailable rather than evidence. |
| metals/mining | Capex / project ramp | ready | thesis_question_context: / G-2 / Is the company quality good, or are we only buying a cheap valuation or hot theme? / prove segment economics, cash conversion, moat, and capital allo... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.