# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=3, research_errors=5, warnings=17.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| verification_calendar | warning | review only | missing action-linked verification calendar for add/hold/trim/downgrade decisions |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| decisive_evidence_conflict | error | review only | Decisive evidence conflicts remain unresolved: EV016 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager silently changed 2026-08-08 稀释后总股本 from 3286.0277 百万股 to 32.860277 mn shares |
| official_guidance_extraction | error | blocks formal publication | an official half-year earnings preview is present, but its numeric parent-profit guidance was not extracted; retrieve the announcement PDF/text before forecasting |
| income_statement_bridge_completion | warning | review only | 2026e operating profit -420.00 and parent profit -500.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 50.00 and parent profit -30.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 150.00 and parent profit 100.00 lack complete finance/other, tax and minority bridge lines |
| share_count_source_conflict | error | blocks formal publication | current share-count reconciliation failed: deterministic valuation uses 32.860 mn shares versus 3286.028 mn from same-snapshot market cap/close (99.00% difference) |
| rating_valuation_consistency | warning | review only | Hold rating sits beside deterministic expected return 2987.8%; explain the rating band/horizon or revise the rating |