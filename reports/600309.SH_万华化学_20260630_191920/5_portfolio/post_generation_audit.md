# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=11, research_errors=1, warnings=13.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Deterministic contradictions, failed structured generation, blocked company underwriting, and missing mandatory deep-research sections block formal publication.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| thesis_financial_bridge | warning | blocks formal publication | decisive claims are not translated through assumptions and formulas into earnings/cash-or-capital/fair-value effects |
| moat_evidence_scorecard | warning | blocks formal publication | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| valuation_closure | warning | blocks formal publication | valuation does not close mutually exclusive buckets to probability-weighted per-share value, expected return and double-counting control |
| business_segment_breakdown | warning | blocks formal publication | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | blocks formal publication | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | blocks formal publication | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | blocks formal publication | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | blocks formal publication | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| profit_pe_per_share_bridge | error | blocks formal publication | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| moat_evidence_scorecard | warning | blocks formal publication | claimed moat mechanisms remain narrative because no observable test is proven or partially proven |
| valuation_closure | warning | blocks formal publication | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| underwriting_question_usage | warning | review only | PM memo does not visibly answer any company-specific question from the shared underwriting packet |