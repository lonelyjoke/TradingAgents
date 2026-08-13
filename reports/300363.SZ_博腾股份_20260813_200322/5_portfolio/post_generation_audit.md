# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=1, research_errors=7, warnings=12.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: 博腾的护城河方向存在，但当前只能给部分验证。端到端小分子CDMO能力由2025年核心小分子收入增长约13%和2026H1收入+8%-12%得到方向性支持，这是客户继续外包和认证产能的证据。高活OEB5 payload-linker产能已落位上海和新泽西，属于稀缺能力，但2025年新分子收入仅0.68亿元，无利用率和利润，因此只能算未证明期权。客户切换成本未被 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| expectation_gap_evidence | warning | review only | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| unverified_disclosure_calendar | warning | review only | memo assumes a half-year earnings preview without citing an official calendar, announcement, or applicable disclosure rule |
| alternative_intelligence_transmission | error | review only | KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| transaction_rights_attribution | error | review only | Material transaction ownership/cash attribution is incomplete: TXN_SLOVENIA_TERMINATION_2026H1,TXN_PORTON_EUROPE_MINORITY_2024 |
| underwriting_question_closure | error | review only | PM verdicts do not map one-to-one to the shared underwriting questions: missing=UQ06 |
| critical_evidence_utilization | error | review only | Decisive evidence is not fully and uniquely dispositioned: undisposed=KPE05 |
| structured_kpe_usage | warning | review only | grounded quantified KPE rows are absent from the PM memo: KPE07, KPE08 |
| alternative_intelligence_decision_ledger | warning | review only | material full-text KPE claims lack a PM model/probability/verification/rejection decision: KPE08 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01, KSI02, KSI03 |
| structured_conflict_usage | warning | review only | structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them |
| official_guidance_full_year_reconciliation | error | blocks formal publication | official H1 parent-profit guidance=-250.00 CNY mn is not explicitly bridged through Q1, implied Q2, H1, H2 and FY in the public forecast |