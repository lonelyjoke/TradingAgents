# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- FAIL: errors=2, warnings=9.
- Any error must be reconciled before the memo is treated as publication- or investment-committee-ready.

## Findings

| section | severity | issue |
| --- | --- | --- |
| business_segment_breakdown | warning | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| alternative_intelligence_transmission | error | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| underwriting_readiness | warning | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| structured_segment_usage | error | PM memo omits material structured segment(s): 汽车零部件 (八大业务板块), 车规级制氧 |
| structured_conflict_usage | warning | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |