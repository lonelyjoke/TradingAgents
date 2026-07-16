# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=1, research_errors=5, warnings=15.
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
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| thesis_financial_bridge | warning | review only | shared model has no decisive thesis translated into a quantified or partially quantified financial bridge |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| structured_segment_usage | error | review only | PM memo omits material structured segment(s): 情况 其他主营业务 |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE07 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI03, KSI06 |
| industry_playbook_alignment | error | review only | saved contexts mix telecom-operator evidence with lithium-battery/metals playbook, supply-chain, or forecast drivers |
| income_statement_bridge_completion | warning | review only | 2026e operating profit 7742.20 and parent profit 6184.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 9527.40 and parent profit 7785.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 11434.00 and parent profit 9520.00 lack complete finance/other, tax and minority bridge lines |
| position_valuation_consistency | error | blocks formal publication | buy/build instruction reaches 60.00, above deterministic safe-buy ceiling 0.00: - **对于准备建仓者（建仓者）**：**绝对禁止在当前位置建立新头寸**。即使极度看好其十年远景，也应等待以下两大条件同时出现：① 股价回归到安全价格区间，即**30-60 元（基于 2028E 熊市-基准估值，手工计算）**；② 半年度报告证实库存/营收比开始趋势性回落，且毛利率企稳回升。在此之前，所有买入行为都是投机。 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing market-pricing implication |