# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- REVIEW: blocking_errors=0, research_errors=7, warnings=15.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| alternative_intelligence_transmission | error | review only | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| semantic_preprocessing_failure | error | review only | semantic LLM preprocessing failed; the memo may use deterministic filing-row fallback but cannot claim full semantic segment/conflict/KPE processing |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| moat_evidence_scorecard | warning | review only | claimed moat mechanisms remain narrative because no observable test is proven or partially proven |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| transaction_rights_attribution | error | review only | Material transaction ownership/cash attribution is incomplete: T1 |
| underwriting_question_closure | error | review only | PM verdicts do not map one-to-one to the shared underwriting questions: missing=Q3 |
| critical_evidence_utilization | error | review only | Decisive evidence is not fully and uniquely dispositioned: undisposed=EV024,EV029,EV039,KPE04 |
| structured_segment_extraction | error | review only | structured preprocessing produced no segment rows despite having deterministic evidence; segment prosperity cannot be considered complete |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01 |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 6760.00 and parent profit 5200.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 6894.00 and parent profit 5304.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 7033.00 and parent profit 5410.00 lack complete finance/other, tax and minority bridge lines |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |