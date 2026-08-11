# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 002407.SZ as of 2026-08-10 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 002407.SZ as of 2026-08-10 |
| company_business_model | ready | # Company Business Model Primer for 002407.SZ as of 2026-08-10 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 002407.SZ as of 2026-08-10 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 002407.SZ as of 2026-08-10 |
| sell_side_quality_audit | partial | Weak or incomplete modules: Shared company underwriting model, Thesis-to-financial transmission, Moat evidence tests, Valuation closure, Industry KPI checklist, Three-year forec... |
| thematic_catalyst | partial | / pdf_text_extraction / failed / 2025年年度报告: PDF downloaded but no readable text was extracted from c871940ab53b25e7b0f76baa75afb0f6492340a6.pdf. / |
| commodity_product_price | ready | # Commodity and product price context for 002407.SZ as of 2026-08-10 |
| price_move_attribution | ready | # Price-move attribution context for 002407.SZ as of 2026-08-10 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 002407.SZ as of 2026-08-10 |
| shipping_cycle | not_applicable | # Shipping cycle context for 002407.SZ as of 2026-08-10 |
| financial_report_intelligence | partial | / pdf_text_extraction / failed / 2025年年度报告: PDF downloaded but no readable text was extracted from c871940ab53b25e7b0f76baa75afb0f6492340a6.pdf. / |
| peer_comparison | ready | # Tushare same-industry peer comparison for 002407.SZ as of 2026-08-10 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 002407.SZ as of 2026-08-10 |
| earnings_model | ready | # Earnings-model context for 002407.SZ as of 2026-08-10 |
| company_events | ready | # Tushare A-share event research for 002407.SZ as of 2026-08-10 |
| market_expectation | ready | # Market-expectation context for 002407.SZ as of 2026-08-10 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 002407.SZ as of 2026-08-10 |
| management_capital_allocation | ready | # Management and capital-allocation context for 002407.SZ as of 2026-08-10 |
| shareholder_structure | ready | # Shareholder-structure context for 002407.SZ as of 2026-08-10 |
| investor_interaction | ready | # Investor interaction context for 002407.SZ as of 2026-08-10 |
| policy_planning | ready | # Policy-planning context for 002407.SZ as of 2026-08-10 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 002407.SZ |
| baijiu | not_applicable | # Baijiu verification context for 002407.SZ as of 2026-08-10 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 002407.SZ as of 2026-08-10 |
| dividend_defensive | not_applicable | # Dividend defensive verification context for 002407.SZ as of 2026-08-10 |
| building_materials | not_applicable | # Building-materials verification context for 002407.SZ as of 2026-08-10 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 002407.SZ |
| optical_module | not_applicable | # AI optical-module context for 002407.SZ |
| biopharma | not_applicable | # Biopharma verification context for 002407.SZ |
| software | not_applicable | # Software verification context for 002407.SZ |
| insurance | not_applicable | # Insurance verification context for 002407.SZ as of 2026-08-10 |
| medical_device | not_applicable | # Medical-device verification context for 002407.SZ |
| metals_mining | not_applicable | # Metals-mining verification context for 002407.SZ |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | reported | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 202... | primary_or_structured_filing | reported_fact | 20251231, 20260331 |
| KF02 | financial_report_intelligence | estimated | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... | primary_or_structured_filing | model_estimate | 2025, 年度, 2010 |
| KF03 | financial_report_intelligence | reported | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2025... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF04 | financial_report_intelligence | estimated | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF05 | financial_report_intelligence | reported | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF06 | financial_report_intelligence | reported | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF07 | financial_report_intelligence | reported | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 2025年年度报告: 产线存在减值迹象，公司根据行业发展 资产减值 -57,654,408.0... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF08 | financial_report_intelligence | reported | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF09 | financial_report_intelligence | reported | core valuation input | / core_revenue_and_profit_engine / growth is conditional because leverage_funding_growth weakens durability. / quantified disclosure / 2025年年度报告: 境外业务产生的营业收入... | primary_or_structured_filing | reported_fact | 2025, 年度 |
| KF10 | financial_report_intelligence | calculated | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... | primary_or_structured_filing | calculation | 2025, 年度, 2010 |
| KF11 | financial_report_intelligence | estimated | core valuation input | / growth_vector_overseas-expansion / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified disclos... | primary_or_structured_filing | model_estimate | 2025, 年度 |
| KF12 | financial_report_intelligence | estimated | core valuation input | / growth_vector_new-product-platform / has demand visibility, but ramp, delivery, margin, and cash collection still decide sustainability. / quantified discl... | primary_or_structured_filing | model_estimate | 2025, 年度 |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| metals/mining | Metal price proxy | ready | industry_cycle_scan: / Silver / industry proxy / Tushare futures proxy / AG2610.SHF / 15635 / 20260807 / -14.04% / 13545 - 18550 / 15264.6 / 69.6% / 48.69% / P20=14239; P50=14787... |
| metals/mining | Reserve / resource quality | ready | industry_kpi_checklist: / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports ... |
| metals/mining | Equity output / volume | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | AISC / unit cost | ready | company_business_model: / product_or_commodity / / 1 - company hard evidence / official filings, production reports, and sales announcements / realized product mix, output, unit cos... |
| metals/mining | NAV / SOTP | private_proxy | knowledge_planet: / KPE03 / 2026-08-06T16:12 / stream_item:21773 / channel_check / promotional_private_unverified / probability/verification proxy / 8月6日复盘笔记：煤炭/电子特... annotat... |
| metals/mining | Capex / project ramp | ready | industry_kpi_checklist: / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction... |

## Required Manager Treatment
- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.
- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell.
- Treat `private_proxy` rows from Knowledge Planet as alternative-intelligence clues only. They may adjust probabilities, timing, sizing, or verification tasks, but they cannot serve as filing-grade facts unless cross-checked by announcements, Tushare/financial data, reputable news, or market price/volume evidence.