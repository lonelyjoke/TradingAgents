# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 000933.SZ as of 2026-07-21 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 000933.SZ as of 2026-07-21 |
| company_business_model | ready | # Company Business Model Primer for 000933.SZ as of 2026-07-21 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 000933.SZ as of 2026-07-21 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 000933.SZ as of 2026-07-21 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Valuation closure |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from 642ea6525c84aad39c4ed97359c261c89247271c.pdf. / |
| commodity_product_price | ready | # Commodity and product price context for 000933.SZ as of 2026-07-21 |
| price_move_attribution | ready | # Price-move attribution context for 000933.SZ as of 2026-07-21 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 000933.SZ as of 2026-07-21 |
| shipping_cycle | not_applicable | # Shipping cycle context for 000933.SZ as of 2026-07-21 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 2026年一季度报告: PDF downloaded but no readable text was extracted from 642ea6525c84aad39c4ed97359c261c89247271c.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 000933.SZ as of 2026-07-21 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 000933.SZ as of 2026-07-21 |
| earnings_model | ready | # Earnings-model context for 000933.SZ as of 2026-07-21 |
| company_events | ready | # Tushare A-share event research for 000933.SZ as of 2026-07-21 |
| market_expectation | ready | # Market-expectation context for 000933.SZ as of 2026-07-21 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 000933.SZ as of 2026-07-21 |
| management_capital_allocation | ready | # Management and capital-allocation context for 000933.SZ as of 2026-07-21 |
| shareholder_structure | ready | # Shareholder-structure context for 000933.SZ as of 2026-07-21 |
| investor_interaction | ready | # Investor interaction context for 000933.SZ as of 2026-07-21 |
| policy_planning | ready | # Policy-planning context for 000933.SZ as of 2026-07-21 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 000933.SZ |
| baijiu | not_applicable | # Baijiu verification context for 000933.SZ as of 2026-07-21 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 000933.SZ as of 2026-07-21 |
| dividend_defensive | ready | # Dividend defensive verification context for 000933.SZ as of 2026-07-21 |
| building_materials | not_applicable | # Building-materials verification context for 000933.SZ as of 2026-07-21 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 000933.SZ |
| optical_module | not_applicable | # AI optical-module context for 000933.SZ |
| biopharma | not_applicable | # Biopharma verification context for 000933.SZ |
| software | not_applicable | # Software verification context for 000933.SZ |
| insurance | not_applicable | # Insurance verification context for 000933.SZ as of 2026-07-21 |
| medical_device | not_applicable | # Medical-device verification context for 000933.SZ |
| metals_mining | ready | # Metals-mining verification context for 000933.SZ as of 2026-07-21 |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 2026年一季... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度, 2002 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... | primary_or_structured_filing | model_estimate | 2026, 季度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgra... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 价值发生变动。 报告期内，公司铝加工板块量价齐 3 应收账款 1,... | primary_or_structured_filing | reported_fact | 2026, 季度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | reported | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | reported_fact | 2025, 年度, 2002 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_energy-storage / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclosure ... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / already monetized; can enter core valuation if margin and cash conversion are also visible. / quantified disclosure / 20... | primary_or_structured_filing | model_estimate | 2026, 季度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | thesis_question_context: / AL-1 / Is the company a low-cost integrated aluminum profit pool, or just an aluminum-price beta vehicle? / prove realized aluminum ASP, alumina self-suppl... |
| metals/mining | Reserve / resource quality | ready | company_business_model: / resource_cycle / 资源周期 / 商品价格型 / quantified disclosure / 2025年半年度报告: 公司主营业务为铝产品、煤炭的生产、加工和销售。报告期内，公司的核心业务未发生重大变化。电解铝业务的主 要产品为液铝和铝锭，主要运用于建筑、电力、交通运输等行业。煤炭业务的主要... |
| metals/mining | Equity output / volume | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | AISC / unit cost | ready | thesis_question_context: / AL-4 / What is the downside if aluminum price falls but alumina or power cost stays sticky? / show trough earnings, balance-sheet survival, and dividend/FC... |
| metals/mining | NAV / SOTP | ready | thesis_question_context: / AL-1 / Is the company a low-cost integrated aluminum profit pool, or just an aluminum-price beta vehicle? / prove realized aluminum ASP, alumina self-suppl... |
| metals/mining | Capex / project ramp | ready | thesis_question_context: / AL-3 / Which segment actually creates incremental profit: alumina, primary aluminum, trading, energy, or overseas assets? / separate segment revenue, margi... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.