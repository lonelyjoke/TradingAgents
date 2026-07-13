# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- REVIEW: blocking_errors=0, research_errors=1, warnings=16.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation or unreadable structured generation block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| unverified_disclosure_calendar | warning | review only | memo assumes a half-year earnings preview without citing an official calendar, announcement, or applicable disclosure rule |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE07, KPE09, KPE10, KPE11, KPE12 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01 |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 23100.00 and parent profit 18700.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 26400.00 and parent profit 20500.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 31200.00 and parent profit 22900.00 lack complete finance/other, tax and minority bridge lines |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing market-pricing implication |
| pm_format_contract | warning | review only | public PM renderer should emit exactly eight fixed H2 sections; got sections=13. Re-render from the validated PM payload. |