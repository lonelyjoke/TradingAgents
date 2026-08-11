# Post-Generation Research Integrity Audit

- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.
- This audit does not change or independently assign the investment rating.

## Verdict

- BLOCKED: blocking_errors=5, research_errors=11, warnings=16.
- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.
- Only unresolved material contradictions in ticker/period/unit/arithmetic/valuation, unreadable structured generation, or a blocked/missing shared underwriting model block formal publication; depth and coverage gaps remain REVIEW items.

## Findings

| section | severity | publication impact | issue |
| --- | --- | --- | --- |
| company_disaggregation | warning | review only | company map does not separate reported segments from economic product/channel/geography/customer/project units with disclosure limits |
| autonomous_forecast_model | warning | review only | independent operating-driver model does not preserve three explicit forward years |
| moat_evidence_scorecard | warning | review only | moat claims lack observable history/true-peer tests, counterevidence and financial transmission |
| moat_evidence_lineage | error | review only | moat is labelled proven without an EV/KPE/KF evidence id: **成本优势（部分已验证）**：多氟多在6F领域最核心的护城河是其从氢氟酸开始的一体化成本优势。这在行业低谷期有助于生存，在上行期则放大利润弹性。Q1毛利率逆势提升14个百分点，在营收大跌6成的情况下依然盈利改善，是其成本优势的间接证据。但这一优势并非绝对，龙头天赐材料凭借更大的规模可能拥有同等或更低的成本。 |
| segment_prosperity_analysis | warning | review only | multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission |
| peer_comparison_summary | warning | review only | missing explicit Peer Comparison Summary in the final thesis |
| underwriting_modules | warning | review only | missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable |
| filing_internal_quality | warning | review only | missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence |
| true_peer_alternatives | warning | review only | peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions |
| evidence_grade_table | warning | review only | decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified |
| profit_pe_per_share_bridge | error | review only | a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge |
| q2_h1_period_semantics | error | blocks formal publication | the same profit threshold is assigned to Q2 single-quarter and H1 cumulative periods; reconcile H1 = Q1 + Q2 and relabel every trigger |
| three_year_forecast_completion | error | review only | final memo invokes a forecast bridge but does not provide three distinct forward years |
| alternative_intelligence_lineage | warning | review only | Knowledge Planet affects the memo but no KPE evidence id is cited |
| underwriting_readiness | warning | review only | shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence |
| company_operating_model | error | blocks formal publication | company revenue/profit operating equations are absent from the shared underwriting packet |
| company_disaggregation | warning | review only | business units exist but none carries a revenue or profit driver equation |
| thesis_financial_bridge | warning | review only | shared model has no decisive thesis translated into a quantified or partially quantified financial bridge |
| valuation_closure | warning | review only | shared model does not close mutually exclusive valuation buckets to auditable per-share fair value |
| critical_evidence_utilization | error | review only | Decisive evidence is not fully and uniquely dispositioned: unknown=KSI01 |
| evidence_disposition_quality | error | review only | Evidence dispositions are not decision-useful: KPE06:invalid question_id; KPE01:invalid question_id; KSI01:invalid question_id; KPE09:invalid question_id |
| structured_segment_usage | error | review only | PM memo omits material structured segment(s): 新能源电池板块 |
| sell_side_expectation_lineage | warning | review only | PM expectation matrix cites KSI ids absent from the deterministic sell-side ledger: KSI01, KSI02, KSI03 |
| official_guidance_extraction | error | blocks formal publication | an official half-year earnings preview is present, but its numeric parent-profit guidance was not extracted; retrieve the announcement PDF/text before forecasting |
| share_count_source_conflict | error | blocks formal publication | current share-count reconciliation failed: deterministic valuation uses 1220.000 mn shares versus 1190.432 mn from same-snapshot market cap/close (2.48% difference); canonical model snapshot uses 1220.000 mn shares versus 1190.432 mn from same-snapshot market cap/close (2.48% difference) |
| public_report_language | error | blocks formal publication | Chinese public memo contains English-heavy reader-facing sentence(s); translate upstream prose before rendering: - **Customer/Value Proposition：** Provides lithium hexafluorophosphate (6F) to electrolyte manufacturers and battery makers；核心变量是6F demand driven by EV/energy s / - **现金与边界：** Product sale with typical receivables cycle；6F requires heavy capex for capacity；H1 preview confirms profit explosion；product certification and bat / - **Pricing and Revenue Recognition：** 6F price is set in competitive spot/long-term contracts, highly volatile. Revenue recognized up；核心变量是6F ASP is the main p |
| valuation_information_ownership | warning | review only | detailed valuation is repeated across four or more public chapters; keep exact multiples, target/safe prices and scenario values in section 7 |