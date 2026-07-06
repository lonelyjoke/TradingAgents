# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=3, research_errors=6, warnings=14.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation or unreadable structured generation block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: / 规模经济与成本优势 / 全球最大锂电池产能，单位固定成本分摊低，向上游布局碳酸锂及材料，采购议价力强。 / FY2025动力电池毛利率23.84%为全球头部水平；Q1 24.82%证明成本管控持续有效。显著高于亿纬锂能（18-20%）和国轩高科（<15%）。 / 高市场份额、高毛利率、高产能利用率。 / 可持续，但若竞争对手产能大幅扩张或碳酸锂价格长期低 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | review only | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| structured_segment_usage | error | review only | PM memo omits material structured segment(s): 采选冶炼行业 |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE06, KPE10, KPE11 |
| sell_side_expectation_usage | warning | review only | sell-side forecast/valuation observations are absent from the PM expectation-gap analysis: KSI01, KSI02, KSI03, KSI04, KSI05 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI_dongwu |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager silently changed 2027e 经营现金流ocf from 158200.0 CNY mn to 154420.0 CNY mn |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager silently changed 2028e 经营现金流ocf from 193200.0 CNY mn to 184520.0 CNY mn |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 110700.00 and parent profit 88200.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 141750.00 and parent profit 110300.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 174150.00 and parent profit 131800.00 lack complete finance/other, tax and minority bridge lines |
| segment_forecast_reconciliation | error | blocks formal publication | memo calls the forecast bottom-up, but the shared packet lacks numeric three-year forecast rows for each material business unit |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing counterargument/boundary, market-pricing implication |