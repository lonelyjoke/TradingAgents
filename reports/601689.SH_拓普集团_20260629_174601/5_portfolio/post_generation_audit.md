# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- FAIL: errors=6, warnings=8.
- Any error must be reconciled before the memo is treated as publication- or investment-committee-ready.

## Findings

| section | severity | issue |
| --- | --- | --- |
| segment_prosperity_analysis | warning | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| filing_internal_quality | warning | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| evidence_grade_table | warning | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| three_year_forecast_completion | error | final memo invokes a forecast bridge but does not provide three distinct forward years |
| alternative_intelligence_transmission | error | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| underwriting_readiness | error | shared company underwriting packet is blocked: LLM company underwriting failed; only deterministic skeleton is available. |
| company_operating_model | error | company revenue/profit operating equations are absent from the shared underwriting packet |
| shared_model_change_audit | error | PM memo does not reconcile the fundamental/bull/bear changes to the shared underwriting model |
| structured_conflict_usage | warning | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |