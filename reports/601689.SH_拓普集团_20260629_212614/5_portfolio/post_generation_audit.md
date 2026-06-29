# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- REVIEW: blocking_errors=0, research_errors=5, warnings=8.
- Missing, partial or unavailable data is non-blocking and neutral for investment direction; it must be disclosed with a retrieval or verification task.
- Only deterministic arithmetic, period, classification or fact-consistency contradictions block formal publication.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| business_segment_breakdown | warning | review only | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| three_year_forecast_reconciliation | error | review only | three forward years are named but the memo does not reconcile enough of revenue, parent profit, EPS, OCF, capex, and FCF |
| underwriting_readiness | error | review only | shared company underwriting packet is blocked: LLM company underwriting failed; only deterministic skeleton is available. |
| company_operating_model | error | review only | company revenue/profit operating equations are absent from the shared underwriting packet |
| shared_model_change_audit | error | review only | PM memo does not reconcile the fundamental/bull/bear changes to the shared underwriting model |
| structured_segment_usage | error | review only | PM memo omits material structured segment(s): 汽车零 减少 1.38, 减震系 |