# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=23, research_errors=25, warnings=13.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Deterministic contradictions, failed structured generation, blocked company underwriting, and missing mandatory deep-research sections block formal publication.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| company_disaggregation | warning | review only | company map does not separate reported segments from economic product/channel/geography/customer/project units with disclosure limits |
| thesis_financial_bridge | warning | review only | decisive claims are not translated through assumptions and formulas into earnings/cash-or-capital/fair-value effects |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| valuation_closure | warning | review only | valuation does not close mutually exclusive buckets to probability-weighted per-share value, expected return and double-counting control |
| business_segment_breakdown | warning | review only | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | review only | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| alternative_intelligence_transmission | error | review only | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| shared_model_change_audit | error | blocks formal publication | PM memo does not reconcile the fundamental/bull/bear changes to the shared underwriting model |
| structured_segment_usage | error | review only | PM memo omits material structured segment(s): 采选冶炼行业 |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped current dilutedshares |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e evenue |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e evenue |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e evenue |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e rossrofit |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e rossrofit |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e rossrofit |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e peratingrofit |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e peratingrofit |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e peratingrofit |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e etrofitarent |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e etrofitarent |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e etrofitarent |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e asic |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e asic |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e asic |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e  |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e  |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e  |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2026e eps |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2027e eps |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager canonical snapshot dropped 2028e eps |
| pm_format_contract | warning | review only | public PM renderer should emit exactly eight fixed H2 sections; got sections=20. Re-render from the validated PM payload. |