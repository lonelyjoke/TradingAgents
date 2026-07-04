# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=1, research_errors=1, warnings=16.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Deterministic contradictions, failed structured generation, blocked company underwriting, and missing mandatory deep-research sections block formal publication.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| company_disaggregation | warning | review only | company map does not separate reported segments from economic product/channel/geography/customer/project units with disclosure limits |
| autonomous_forecast_model | warning | review only | independent operating-driver model does not preserve three explicit forward years |
| thesis_financial_bridge | warning | review only | decisive claims are not translated through assumptions and formulas into earnings/cash-or-capital/fair-value effects |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| valuation_closure | warning | review only | valuation does not close mutually exclusive buckets to probability-weighted per-share value, expected return and double-counting control |
| handoff_integrity_audit | warning | review only | final memo does not prove that business units, all forecast years, thesis bridges and valuation buckets survived the agent handoff |
| business_segment_breakdown | warning | review only | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | review only | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | blocks formal publication | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |