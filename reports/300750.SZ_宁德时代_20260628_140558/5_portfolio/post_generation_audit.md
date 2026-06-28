# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- FAIL: errors=1, warnings=12.
- Any error must be reconciled before the memo is treated as publication- or investment-committee-ready.

## Findings

| section | severity | issue |
| --- | --- | --- |
| business_segment_breakdown | warning | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| scenario_sensitivity_bridge | warning | valuation or safety-price conclusion lacks bull/base/bear, sensitivity, or explicit multi-period assumption bridge |
| second_curve_optionality | warning | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| three_year_forecast_completion | error | final memo invokes a forecast bridge but does not provide three distinct forward years |
| alternative_intelligence_lineage | warning | Knowledge Planet affects the memo but no KPE evidence id is cited |
| price_move_causal_attribution | warning | memo makes a causal flow/sentiment attribution without flow, block-trade, holder-change, or equivalent evidence |