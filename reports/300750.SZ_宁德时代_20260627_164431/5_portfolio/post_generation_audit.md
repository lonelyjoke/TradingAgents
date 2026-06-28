# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- FAIL: errors=4, warnings=7.
- Any error must be reconciled before the memo is treated as publication- or investment-committee-ready.

## Findings

| section | severity | issue |
| --- | --- | --- |
| expectation_gap_evidence | warning | expectation gap is asserted without enough market-implied or consensus/holder/technical evidence |
| underwriting_modules | warning | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| evidence_grade_table | warning | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| eps_profit_share_count_consistency | error | net-profit/EPS rows imply share-count proxies that differ by 6.4%; reconcile units, actual-vs-TTM EPS, dilution, and the share-count assumption |
| three_year_forecast_completion | error | final memo invokes a forecast bridge but does not provide three distinct forward years |
| financial_calendar_period | error | Q2/half-year disclosure is linked to October; verify whether the memo has confused the half-year and Q3 reporting windows |
| period_comparator_lineage | error | final memo labels 1.46pp as YoY, but the matching earnings-model row does not carry a same-period YoY comparison basis |
| alternative_intelligence_lineage | warning | Knowledge Planet affects the memo but no KPE evidence id is cited |
| price_move_causal_attribution | warning | memo makes a causal flow/sentiment attribution without flow, block-trade, holder-change, or equivalent evidence |