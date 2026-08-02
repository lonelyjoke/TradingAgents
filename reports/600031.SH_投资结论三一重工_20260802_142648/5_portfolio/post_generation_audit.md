# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- REVIEW: blocking_errors=0, research_errors=1, warnings=18.
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
| order_backlog_bridge | warning | review only | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| moat_evidence_scorecard | warning | review only | claimed moat mechanisms remain narrative because no observable test is proven or partially proven |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE03, KPE04, KPE05, KPE06, KPE07, KPE08, KPE09, KPE10 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01, KSI02 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 13340.00 and parent profit 10260.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 15700.00 and parent profit 12120.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 17778.00 and parent profit 13750.00 lack complete finance/other, tax and minority bridge lines |
| rating_valuation_consistency | warning | review only | Hold rating sits beside deterministic expected return -17.5%; explain the rating band/horizon or revise the rating |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |