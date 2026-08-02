# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=1, research_errors=2, warnings=14.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: 公司被公认为煤化工行业成本领先者。2026年Q1毛利率22.28%的大幅跃升和历史上持续高于同业的表现（应收账款极低也是侧面印证）支持这一论断。然而，缺乏与主要竞争对手（宝丰能源、鲁西化工）同期毛利率和单位成本的直接量化对比，使得我们无法精确衡量其领先幅度。目前该护城河判定为“部分验证”，需通过公开可比数据来进一步确认。若后续证明公司毛利率持续高于同业均值2 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE04, KPE06 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01, KSI02 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| official_guidance_extraction | error | blocks formal publication | an official half-year earnings preview is present, but its numeric parent-profit guidance was not extracted; retrieve the announcement PDF/text before forecasting |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 5100.00 and parent profit 4000.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 6100.00 and parent profit 5100.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 6900.00 and parent profit 5800.00 lack complete finance/other, tax and minority bridge lines |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |