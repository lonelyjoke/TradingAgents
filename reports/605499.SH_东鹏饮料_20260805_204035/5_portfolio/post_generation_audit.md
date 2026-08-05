# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=4, research_errors=5, warnings=13.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: - **品牌认知与消费习惯（proven）：** 东鹏特饮通过”累了困了喝东鹏特饮”的广告语和低价大容量产品，在价格敏感型消费者中建立了强大的品牌认知和消费习惯；能量饮料占主营业务收入71.92%，显示消费者高度依赖；集团ROE高达51.6%，证明品牌溢价和强定价权；市场份额领先，高毛利率（46%+）和高资本回报率（ROE>50%）。 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| second_curve_optionality | warning | review only | second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e eps |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager silently changed 2026e epsdiluted from 6.565 CNY/share to 6.319493420014211 CNY/share |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e epsdiluted |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e epsdiluted |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 6053.80 and parent profit 4496.30 lack complete finance/other, tax and minority bridge lines |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |