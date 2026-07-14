# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=1, research_errors=3, warnings=16.
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
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE07, KPE10, KPE11 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI02 |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 14785.50 and parent profit 11061.70 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 15786.30 and parent profit 11355.80 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 16804.00 and parent profit 11820.40 lack complete finance/other, tax and minority bridge lines |
| position_valuation_consistency | error | blocks formal publication | buy/build instruction reaches 120.00, above deterministic safe-buy ceiling 87.03: 正面催化剂：（1）2026年8月底发布半年报，若毛利率保持在74%以上、合同负债同比依然正增长、且青花20/25保持增长势头，将证伪看空逻辑，此时基础情景公允价值可能从108.8元上修至115-120元，风险回报改善，但当前价格仍高于安全买入上限，新资金需等待价格回落或基本面证据进一步增强。（2）中秋国庆旺季动销超预期，若能观察到青花30批价回升至700元以 |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing counterargument/boundary |