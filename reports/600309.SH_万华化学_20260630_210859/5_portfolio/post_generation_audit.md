# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=12, research_errors=1, warnings=16.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Deterministic contradictions, failed structured generation, blocked company underwriting, and missing mandatory deep-research sections block formal publication.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| company_disaggregation | warning | blocks formal publication | company map does not separate reported segments from economic product/channel/geography/customer/project units with disclosure limits |
| autonomous_forecast_model | warning | blocks formal publication | independent operating-driver model does not preserve three explicit forward years |
| moat_evidence_scorecard | warning | blocks formal publication | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| valuation_closure | warning | blocks formal publication | valuation does not close mutually exclusive buckets to probability-weighted per-share value, expected return and double-counting control |
| handoff_integrity_audit | warning | blocks formal publication | final memo does not prove that business units, all forecast years, thesis bridges and valuation buckets survived the agent handoff |
| peer_comparison_summary | warning | blocks formal publication | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | blocks formal publication | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | blocks formal publication | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | blocks formal publication | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| evidence_grade_table | warning | blocks formal publication | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| battery_material_evidence_gate | warning | review only | battery-material report lacks ASP/lithium-cost/spread/utilization/customer/cash-conversion evidence-gate depth |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | blocks formal publication | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| underwriting_question_usage | warning | review only | PM memo does not visibly answer any company-specific question from the shared underwriting packet |
| structured_segment_usage | error | blocks formal publication | PM memo omits material structured segment(s): 化工行业 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |