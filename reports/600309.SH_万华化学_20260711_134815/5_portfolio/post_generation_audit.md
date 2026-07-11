# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=3, research_errors=5, warnings=22.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation or unreadable structured generation block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| verification_calendar | warning | review only | missing action-linked verification calendar for add/hold/trim/downgrade decisions |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| battery_material_evidence_gate | warning | review only | battery-material report lacks ASP/lithium-cost/spread/utilization/customer/cash-conversion evidence-gate depth |
| battery_material_driver_bridge | warning | review only | battery-material report does not turn industry KPIs into forecast drivers, conviction caps, sizing, and verification calendar |
| unverified_disclosure_calendar | warning | review only | memo assumes a half-year earnings preview without citing an official calendar, announcement, or applicable disclosure rule |
| alternative_intelligence_transmission | error | review only | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE07, KPE09, KPE10, KPE11, KPE12 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2026e revenue from 220000.0 CNY mn to 225000.0 mn CNY |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2026e parentnetprofit from 18700.0 CNY mn to 18700.0 mn CNY |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 23100.00 and parent profit 18700.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 26400.00 and parent profit 20500.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 31200.00 and parent profit 22900.00 lack complete finance/other, tax and minority bridge lines |
| public_key_number_consistency | error | blocks formal publication | public memo uses conflicting current price values [0.3, 68.71]; state one definition/period or reconcile the definitions explicitly |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing market-pricing implication |