# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=10, research_errors=3, warnings=9.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Deterministic contradictions, failed structured generation, blocked company underwriting, and missing mandatory deep-research sections block formal publication.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| business_segment_breakdown | warning | blocks formal publication | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | blocks formal publication | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | blocks formal publication | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | blocks formal publication | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | blocks formal publication | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| scenario_sensitivity_bridge | warning | blocks formal publication | valuation or safety-price conclusion lacks bull/base/bear, sensitivity, or explicit multi-period assumption bridge |
| evidence_grade_table | warning | blocks formal publication | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| pb_bvps_arithmetic | error | blocks formal publication | stated BVPS 27.90 does not reconcile to current price/PB 8.00/1.92=4.17 |
| profit_pe_per_share_bridge | error | blocks formal publication | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| three_year_forecast_completion | error | blocks formal publication | final memo invokes a forecast bridge but does not provide three distinct forward years |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |