# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- REVIEW: blocking_errors=0, research_errors=4, warnings=12.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: - **成本领先与规模制造（proven）：** 超大规模分摊固定成本，高自动化率降低人工成本，内部供应电池削减核心物料开支；合并毛利率高于特斯拉（约 16%），但 Q1 经营利润率仅 3.13%，远低于特斯拉，说明成本优势被价格战稀释；毛利率相对行业有保护垫，但未能稳定提升。 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| alternative_intelligence_lineage | warning | review only | Knowledge Planet affects the memo but no KPE evidence id is cited |
| semantic_preprocessing_failure | error | review only | semantic LLM preprocessing failed; the memo may use deterministic filing-row fallback but cannot claim full semantic segment/conflict/KPE processing |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| structured_segment_extraction | error | review only | structured preprocessing produced no segment rows despite having deterministic evidence; segment prosperity cannot be considered complete |
| sell_side_expectation_usage | warning | review only | sell-side forecast/valuation observations are absent from the PM expectation-gap analysis: KSI04 |
| public_table_readability | warning | review only | mobile-unfriendly table detected: columns=6, rows=1, average_cell_chars=27.7, max_cell_chars=141; use short subsections for causal prose |