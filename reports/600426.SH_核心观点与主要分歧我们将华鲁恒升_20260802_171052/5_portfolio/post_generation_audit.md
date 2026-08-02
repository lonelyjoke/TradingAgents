# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=1, research_errors=4, warnings=11.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: - **一体化柔性多产品平台带来的成本领先（proven）：** 客户选择华鲁恒升的产品是基于其价格竞争力和供应稳定性。公司煤气化平台生产的合成气可根据市场价差灵活调配，降低生产成本，提供多样化的产品组合，满足不同下游行业的一站式采购需求；历史数据显示，华鲁恒升综合毛利率持续高于鲁西化工等煤化工同业2-5个百分点，且在2025年行业低谷仍维持22.28%的毛 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| semantic_preprocessing_failure | error | review only | semantic LLM preprocessing failed; the memo may use deterministic filing-row fallback but cannot claim full semantic segment/conflict/KPE processing |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01, KSI02 |
| share_count_source_conflict | error | blocks formal publication | current share-count reconciliation failed: underwriting packet uses 2115.341 mn shares versus 2749.943 mn from same-snapshot market cap/close (23.08% difference); deterministic valuation uses 2115.341 mn shares versus 2749.943 mn from same-snapshot market cap/close (23.08% difference); canonical model snapshot uses 2115.341 mn shares versus 2749.943 mn from same-snapshot market cap/close (23.08% difference) |
| public_table_density | warning | review only | public memo contains 5 tables; keep tables for comparable numbers and convert narrative matrices to subsections |
| public_table_readability | warning | review only | mobile-unfriendly table detected: columns=6, rows=5, average_cell_chars=6.8, max_cell_chars=25; use short subsections for causal prose |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing counterargument/boundary, market-pricing implication |