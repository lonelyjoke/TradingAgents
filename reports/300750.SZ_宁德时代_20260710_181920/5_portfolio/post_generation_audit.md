# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=2, research_errors=3, warnings=18.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation or unreadable structured generation block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| business_segment_breakdown | warning | review only | segment discussion lacks revenue/growth/margin/profit/cash/valuation depth |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | review only | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| financial_calendar_period | error | blocks formal publication | Q2/half-year disclosure is linked to October; verify whether the memo has confused the half-year and Q3 reporting windows |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| sell_side_expectation_usage | warning | review only | sell-side forecast/valuation observations are absent from the PM expectation-gap analysis: KSI01, KSI03 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI04 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager silently changed current dilutedshares from 4626.63 mn shares to 4360.0 mn shares |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 117000.00 and parent profit 92500.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 153000.00 and parent profit 115000.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 184000.00 and parent profit 135000.00 lack complete finance/other, tax and minority bridge lines |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing counterargument/boundary, market-pricing implication, falsification condition |