# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=2, research_errors=5, warnings=18.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| company_disaggregation | warning | review only | company map does not separate reported segments from economic product/channel/geography/customer/project units with disclosure limits |
| autonomous_forecast_model | warning | review only | independent operating-driver model does not preserve three explicit forward years |
| thesis_financial_bridge | warning | review only | decisive claims are not translated through assumptions and formulas into earnings/cash-or-capital/fair-value effects |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| valuation_closure | warning | review only | valuation does not close mutually exclusive buckets to probability-weighted per-share value, expected return and double-counting control |
| business_segment_breakdown | warning | review only | missing explicit Business Segment Breakdown in the final thesis |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| three_year_forecast_completion | error | review only | final memo invokes a forecast bridge but does not provide three distinct forward years |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| moat_evidence_scorecard | warning | review only | claimed moat mechanisms remain narrative because no observable test is proven or partially proven |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| underwriting_question_usage | warning | review only | PM analytical ledger does not answer any company-specific question from the shared underwriting packet |
| shared_model_change_audit | error | review only | PM canonical payload does not reconcile the fundamental/bull/bear changes to the shared underwriting model |
| structured_segment_extraction | error | review only | structured preprocessing produced no segment rows despite having deterministic evidence; segment prosperity cannot be considered complete |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE03, KPE04, KPE07 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| handoff_numeric_consistency | error | blocks formal publication | canonical handoff artifact is missing or unreadable: [Errno 2] No such file or directory: 'C:\\Users\\zhanc\\Documents\\GitHub\\TradingAgents\\reports\\603986.SH_兆易创新_20260719_205634\\5_portfolio\\canonical_decision.json' |
| pm_format_contract | warning | review only | public PM renderer should emit exactly eight fixed H2 sections; got sections=0. Re-render from the validated PM payload. |
| pm_structured_generation | error | blocks formal publication | Portfolio Manager used free-text fallback; formal publication requires schema-valid SellSidePMDecision output; structured error: Expecting ',' delimiter: line 5 column 76 (char 177); fallback validation=180 validation errors for SellSidePMDecision
research_readiness
  Field required [type=missing, input_value={'rating': 'Underweight',...为被动持有者。'}, input_type=dict]
   |