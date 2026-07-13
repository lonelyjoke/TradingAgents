# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- REVIEW: blocking_errors=0, research_errors=2, warnings=14.
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
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| underwriting_readiness | error | review only | shared company underwriting packet is blocked: LLM company underwriting failed; only deterministic skeleton is available. |
| company_operating_model | error | review only | company revenue/profit operating equations are absent from the shared underwriting packet |
| company_disaggregation | warning | review only | business units exist but none carries a revenue or profit driver equation |
| thesis_financial_bridge | warning | review only | shared model has no decisive thesis translated into a quantified or partially quantified financial bridge |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01, KSI02 |
| rating_valuation_consistency | warning | review only | Hold rating sits beside deterministic expected return -15.4%; explain the rating band/horizon or revise the rating |