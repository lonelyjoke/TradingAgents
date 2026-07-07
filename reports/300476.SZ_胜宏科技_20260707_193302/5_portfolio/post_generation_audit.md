# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=25, research_errors=27, warnings=10.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation or unreadable structured generation block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| order_backlog_bridge | warning | review only | project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE03, KPE04 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01 |
| sell_side_expectation_lineage | error | blocks formal publication | PM pairs KSI01 with ['KPE02'], but the deterministic ledger links it to ['no KPE id'] |
| industry_playbook_alignment | error | review only | saved contexts mix telecom-operator evidence with lithium-battery/metals playbook, supply-chain, or forecast drivers |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e costofsales |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e costofsales |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e costofsales |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e grossprofit |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e grossprofit |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e grossprofit |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e grossmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e grossmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e grossmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e operatingprofit |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e operatingprofit |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e operatingprofit |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e operatingmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e operatingmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e operatingmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e netmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e netmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e netmargin |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e ocf |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e ocf |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e ocf |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2026e capex |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2027e capex |
| handoff_numeric_consistency | error | blocks formal publication | Portfolio Manager canonical snapshot dropped 2028e capex |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |
| pm_analytical_spine | error | review only | PM structured analytical spine is incomplete: public thesis chapter missing market-pricing implication, falsification condition |