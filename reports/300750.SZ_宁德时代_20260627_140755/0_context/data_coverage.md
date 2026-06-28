# Data Coverage Audit

| module | status | note |
| --- | --- | --- |
| thesis_question_context | ready | # Thesis Question Context for 300750.SZ as of 2026-06-27 |
| industry_cycle_scan | ready | # Industry Cycle Scan for 300750.SZ as of 2026-06-27 |
| company_business_model | ready | # Company Business Model Primer for 300750.SZ as of 2026-06-27 |
| industry_kpi_checklist | ready | # Industry KPI Checklist for 300750.SZ as of 2026-06-27 |
| forecast_model_scaffold | ready | # Forward Forecast Model Scaffold for 300750.SZ as of 2026-06-27 |
| sell_side_quality_audit | ready | Weak or incomplete modules: none detected from supplied contexts |
| thematic_catalyst | ready | # Thematic catalyst cross-check for 300750.SZ as of 2026-06-27 |
| commodity_product_price | ready | # Commodity and product price context for 300750.SZ as of 2026-06-27 |
| price_move_attribution | ready | # Price-move attribution context for 300750.SZ as of 2026-06-27 |
| intraday_minute_behavior | ready | ## Intraday Minute-Line Behavior Context |
| relative_strength | ready | # Relative strength and index linkage for 300750.SZ as of 2026-06-27 |
| shipping_cycle | not_applicable | # Shipping cycle context for 300750.SZ as of 2026-06-27 |
| financial_report_intelligence | ready | # Financial-report intelligence for 300750.SZ as of 2026-06-27 |
| peer_comparison | ready | # Tushare same-industry peer comparison for 300750.SZ as of 2026-06-27 |
| supply_chain_comparison | ready | # Supply-chain position comparison for 300750.SZ as of 2026-06-27 |
| earnings_model | ready | # Earnings-model context for 300750.SZ as of 2026-06-27 |
| market_expectation | ready | # Market-expectation context for 300750.SZ as of 2026-06-27 |
| price_eps_pe_decomposition | ready | # Historical price-EPS-PE decomposition for 300750.SZ as of 2026-06-27 |
| management_capital_allocation | ready | # Management and capital-allocation context for 300750.SZ as of 2026-06-27 |
| shareholder_structure | ready | # Shareholder-structure context for 300750.SZ as of 2026-06-27 |
| investor_interaction | ready | # Investor interaction context for 300750.SZ as of 2026-06-27 |
| policy_planning | ready | # Policy-planning context for 300750.SZ as of 2026-06-27 |
| web_fact_check | partial | Context unavailable: search provider returned no relevant web fact rows after company relevance filtering. |
| knowledge_planet | ready | # Knowledge Planet Alternative Intelligence Context for 300750.SZ |
| baijiu | not_applicable | # Baijiu verification context for 300750.SZ as of 2026-06-27 |
| compute_leasing | not_applicable | # Compute-leasing verification layer for 300750.SZ as of 2026-06-27 |
| dividend_defensive | ready | # Dividend defensive verification context for 300750.SZ as of 2026-06-27 |
| building_materials | ready | # Building-materials verification context for 300750.SZ as of 2026-06-27 |
| consumer_staples | not_applicable | # Consumer-staples verification context for 300750.SZ |
| optical_module | ready | # AI optical-module context for 300750.SZ as of 2026-06-27 |
| biopharma | not_applicable | # Biopharma verification context for 300750.SZ |
| software | ready | # Software verification context for 300750.SZ as of 2026-06-27 |
| insurance | not_applicable | # Insurance verification context for 300750.SZ as of 2026-06-27 |
| medical_device | not_applicable | # Medical-device verification context for 300750.SZ |
| metals_mining | ready | # Metals-mining verification context for 300750.SZ as of 2026-06-27 |

## Key Facts Ledger

| fact_id | source_module | status | decision_role | evidence |
| --- | --- | --- | --- | --- |
| KF01 | financial_report_intelligence | ready | core valuation input | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性... |
| KF02 | financial_report_intelligence | ready | core valuation input | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告:... |
| KF03 | financial_report_intelligence | ready | core valuation input | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: ... |
| KF04 | financial_report_intelligence | ready | core valuation input | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_eq... |
| KF05 | financial_report_intelligence | ready | balance-sheet input | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_wi... |
| KF06 | financial_report_intelligence | ready | core valuation input | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and othe... |
| KF07 | financial_report_intelligence | ready | core valuation input | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金... |
| KF08 | financial_report_intelligence | ready | cash-quality input | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset... |
| KF09 | financial_report_intelligence | ready | insurance-native input | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports ... |
| KF10 | financial_report_intelligence | ready | valuation input | / project_delivery / 项目订单 / 交付回款型 / quantified disclosure / 2025年年度报告: [Runtime-compacted filing text for 2025年年度报告: original 499236 chars, budget 180000 cha... |
| KF11 | financial_report_intelligence | ready | core valuation input | / core_revenue_and_profit_engine / growth durability is not proven by the current readable filings; treat it as a verification item. / quantified disclosure ... |
| KF12 | financial_report_intelligence | ready | core valuation input | / segment_mix_and_profit_pool / segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. / quantif... |

## Core Variable Gates

| profile | core_variable | status | evidence |
| --- | --- | --- | --- |
| bank | NIM / net interest spread | ready | financial_report_intelligence: For banks, preserve the exact spread terminology from filings: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. If the filing only supports 净利差 1.77% and ... |
| bank | Asset quality | ready | dividend_defensive: For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically. |
| bank | Capital adequacy | ready | dividend_defensive: For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically. |
| bank | ROE / PB valuation bridge | ready | thesis_question_context: / ts_code / name / industry / total_mv / pe_ttm / pb / ps_ttm / dv_ttm / roe_annual / roa_annual / roe / roa / netprofit_yoy / debt_to_assets / v4_score / |
| bank | Dividend coverage | ready | thesis_question_context: / AL-4 / What is the downside if aluminum price falls but alumina or power cost stays sticky? / show trough earnings, balance-sheet survival, and dividend/FC... |
| insurance | NBV growth and margin | partial | insurance: Do not force NBV, EV, solvency, or COR analysis into this stock unless primary evidence proves insurance exposure. |
| insurance | EV / CSM bridge | missing | No explicit source-backed evidence found. |
| insurance | Solvency and capital | ready | dividend_defensive: For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically. |
| insurance | P&C COR | ready | thesis_question_context: / ts_code / name / industry / total_mv / pe_ttm / pb / ps_ttm / dv_ttm / roe_annual / roa_annual / roe / roa / netprofit_yoy / debt_to_assets / v4_score / |
| insurance | Dividend coverage | ready | thesis_question_context: / AL-4 / What is the downside if aluminum price falls but alumina or power cost stays sticky? / show trough earnings, balance-sheet survival, and dividend/FC... |

## Required Manager Treatment
- Do not treat failed or missing modules as neutral evidence.
- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.
- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.
- If other verified modules still support a directional view, keep the rating label clean and put the limitation in conviction, sizing, Evidence Gaps, and Verification Calendar. Use an evidence-limited rating label only when a core module for the thesis is failed/partial or the decisive valuation driver lacks direct evidence.
- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing.
- Use Core Variable Gates as rating-strength guardrails. Missing thesis-critical variables should cap conviction and normally prevent Buy/Overweight unless downside is independently bounded and the missing variable is explicitly placed in the Verification Calendar.