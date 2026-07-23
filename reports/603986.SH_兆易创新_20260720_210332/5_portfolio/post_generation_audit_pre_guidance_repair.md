# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=7, research_errors=11, warnings=13.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| unverified_disclosure_calendar | warning | review only | memo assumes a half-year earnings preview without citing an official calendar, announcement, or applicable disclosure rule |
| alternative_intelligence_transmission | error | review only | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| thesis_financial_bridge | warning | review only | shared model has no decisive thesis translated into a quantified or partially quantified financial bridge |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| structured_segment_extraction | error | review only | structured preprocessing produced no segment rows despite having deterministic evidence; segment prosperity cannot be considered complete |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2026e revenue from 25000.0 CNY mn to 21000.0 CNY mn |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2027e revenue from 30000.0 CNY mn to 17000.0 CNY mn |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2026e grossmargin from 58.0 % to 56.0 % |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2026e parentnetprofit from 15000.0 CNY mn to 10000.0 CNY mn |
| handoff_numeric_consistency | error | blocks formal publication | Research Manager silently changed 2027e parentnetprofit from 18000.0 CNY mn to 5500.0 CNY mn |
| official_guidance_full_year_reconciliation | error | blocks formal publication | official H1 parent-profit guidance=6900.00 CNY mn is not explicitly bridged through Q1, implied Q2, H1, H2 and FY in the public forecast |
| official_guidance_full_year_reconciliation | error | blocks formal publication | official H1 parent profit 6900.00 CNY mn already exceeds full-year scenario input(s) ['bear FY=4500.00 CNY mn']; no explicit H2 loss/fair-value-reversal bridge is provided |
| income_statement_bridge_completion | warning | review only | 2027e operating profit 12000.00 and parent profit 5500.00 lack complete finance/other, tax and minority bridge lines |
| income_statement_bridge_completion | warning | review only | 2028e operating profit 11550.00 and parent profit 3000.00 lack complete finance/other, tax and minority bridge lines |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing market-pricing implication |