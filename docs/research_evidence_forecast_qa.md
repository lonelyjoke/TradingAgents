# Research Evidence, Forecast, and QA Contract

This contract applies to every industry. Industry playbooks define the native
drivers, while the common pipeline controls evidence quality, forecast
reconciliation, expectation gaps, alternative intelligence, and final-output QA.

## 1. Evidence semantics

Every candidate input is classified as one of:

- `reported`: a source-backed numeric fact;
- `calculated`: a reproducible calculation from sourced inputs;
- `estimated`: a model or scenario estimate;
- `private_proxy`: Knowledge Planet/channel/research evidence that still needs an objective anchor;
- `missing`: an explicit gap or undisclosed variable;
- `non_evidence`: a question, instruction, formula, or narrative without a usable number.

Questions, checklists, and phrases such as “capacity utilization remains a model
gap” must never satisfy a core-variable evidence gate.

### Machine-readable source of record

Before analysts run, the pipeline now builds a typed `structured_research_context`
and saves it as `0_context/structured_research.json`. It contains segment
identities, grounded metrics, periods, units, evidence status, source conflicts,
and Knowledge Planet impacts. Markdown files remain human-readable excerpts and
backward-compatible fallbacks; agents are instructed to prefer the JSON bundle.

The quick model performs semantic preprocessing because company segments,
business causality, and new information change over time. Deterministic controls
then downgrade any semantic metric whose source quote is not grounded, whose
period is missing, or whose probability/financial arithmetic does not reconcile.

## 2. Cross-industry model structure

The industry playbook supplies business-bucket formulas such as battery GWh x
ASP, bank earning assets x NIM, insurer premium x NBV margin, mining output x
realized price less AISC, or hog sales kg x unit spread. Every report must then:

1. fill three forward years or four forward quarters by material business bucket;
2. reconcile bucket revenue and profit to consolidated revenue, EPS, OCF, and FCF;
3. label each decisive cell with evidence status and evidence ids;
4. keep unsupported precision as a range or an explicit gap rather than inventing a point estimate.

### Segment-level prosperity

For a multi-business company, prosperity is assessed by business segment before
the consolidated conclusion. Each material segment must include:

- revenue and profit weight;
- current prosperity level and marginal direction;
- a written demand -> supply/capacity -> price/volume -> utilization/mix ->
  margin -> cash-flow causal chain;
- dated support across at least three relevant data dimensions and normally two
  source types;
- strongest counterevidence, confidence, EPS/FCF impact, valuation treatment,
  and next verification.

The company-level verdict is weighted by revenue, gross profit/profit, cash
intensity, and capital intensity. A small high-growth second curve must not
define the entire company, and prosperity level must not be confused with
direction: high-but-decelerating and low-but-recovering are different states.

## 3. Expectation layers

Do not merge these layers:

1. current-price implied expectations;
2. company-specific analyst consensus, when a dated forecast set exists;
3. one-broker or industry-report hypotheses;
4. the TradingAgents forecast.

A valid expectation gap names the differing variable, period, magnitude,
evidence grade, and next event capable of resolving the difference.

## 4. Knowledge Planet transmission

Every promoted clue must cite its `KPE` id and end in exactly one audited outcome:

- numeric old-to-new model assumption;
- bull/base/bear probability before-to-after;
- unchanged/watch with an objective verification gate;
- rejected with reason.

Accepted changes must be transmitted through segment revenue/profit, EPS/FCF,
scenario values, probabilities, and probability-weighted value. Knowledge Planet
does not become filing-grade evidence merely because it is information-rich.

The structured bundle attempts physical and financial quantification for each
KPE item using explicit fields: baseline, revised assumption, unit, segment
revenue base, revenue impact, margin impact, incremental net margin, tax rate,
share count, and cash conversion. Deterministic code calculates revenue, parent
profit, EPS, and FCF deltas. When a required input is absent, the row remains
`unquantified` or `probability_only` and records the missing input instead of
inventing a contribution.

## 5. Final-output QA

After the PM memo is generated, the save pipeline writes
`5_portfolio/post_generation_audit.md`. It checks report depth plus deterministic
integrity, including:

- scenario probabilities, contributions, and weighted value;
- net-profit/EPS/share-count consistency;
- three-year forecast completion and placeholder leakage;
- YoY versus sequential/annual comparison lineage;
- Q2/half-year versus Q3 reporting-calendar confusion;
- KPE citation and before/after/rejection treatment;
- unsupported price-move causal attribution;
- industry/playbook context alignment.

The audit never changes or independently assigns the investment rating. Any
publication blocker must be reconciled before the report is treated as
publication- or investment-committee-ready. Blockers include deterministic
arithmetic/period/unit contradictions, a blocked shared company-underwriting
packet, failed Portfolio Manager structured generation, omitted material
segments, an unreconciled three-year model, and missing mandatory deep-research
sections. Missing source availability remains neutral evidence, but it must be
named with a retrieval task.

When blocked, the raw PM response is retained only as
`5_portfolio/decision_draft.md`; ratings, target prices, sizing, substitutes, and
trade instructions are suppressed from `decision.md` and `complete_report.md`.
`5_portfolio/generation_status.json` records whether the PM response was native
structured output, schema-repaired fallback, or unvalidated free text.

The public `complete_report.md` contains only the schema-valid company deep-dive.
Raw analyst/debate/risk records remain in the numbered internal subdirectories so
modules stay auditable without generating a second reader-facing report or turning
the public memo into a concatenated transcript.

## 6. Universal company-depth contract (schema v2)

Every A-share company passes the same six analytical contracts, while
`model_profile` selects industry-native metrics:

1. **Company disaggregation** separates filing segments from the product,
   channel, geography, customer, project/asset, or financial-business units
   that actually drive economics. Analytical units may organize diligence but
   may not receive invented revenue, margin, or value.
2. **Autonomous three-year model** starts from operating drivers and reconciles
   material units to group earnings, cash/capital, and per-share lines. Banks,
   insurers, securities firms, and REITs retain their native model lines.
3. **Thesis-to-financial bridges** map each decisive claim through a formula and
   bull/base/bear assumptions to earnings, cash/capital, and fair value.
4. **Moat evidence tests** classify claimed advantages as proven, partial,
   unproven, or rejected using observable history/true-peer evidence,
   counterevidence, and financial transmission.
5. **Valuation closure** uses mutually exclusive core/scenario/optionality/
   excluded buckets and reconciles probability, share count, per-share value,
   expected return, rating consistency, and double-counting checks.
6. **Lossless handoff** preserves economic units, all three forecast years,
   thesis bridges, valuation buckets, reported facts, estimates, and unresolved
   cells across Fundamental Analyst, Bull/Bear, Research Manager, and PM.

The PM renderer emits explicit sections for all six contracts. Missing or shallow
analysis is sent to the selected deep model's senior sell-side editorial pass for
section-specific revision; it is not a mechanical publication blocker. Ordinary
unavailable source data remains neutral: the affected cell stays missing with an
explicit retrieval task and confidence cap instead of invented precision or a mechanical
rating change.

## 7. Deterministic depth and report-length controls

The shared company model selects one `operating_model_family`. The validator
then checks the corresponding native driver chain, rather than accepting a
generic revenue-growth narrative. Supported families cover volume/price/cost,
store traffic/conversion/ticket, users/ARPU/retention, project backlog/delivery,
commodity output/realized price/cash cost, bank spread/credit, insurance value,
and REIT occupancy/rent economics. Missing drivers keep the model partial and
are named as retrieval/modeling tasks.

Chinese and English forecast-line aliases are canonicalized before required
rows are added, so one economic metric cannot appear once as a populated Chinese
row and again as an empty English row. When the same snapshot contains market
capitalization and latest close, diluted shares are calculated as market cap /
close; EPS, FCF, scenario PE value, valuation-bucket per-share value,
probability-weighted value, and expected return are recalculated deterministically.

A moat cannot remain `proven` or `partial` without a valid `EV`, `KPE`, or `KF`
evidence id. The final audit also recalculates reported-to-forecast growth,
option-value formulas, scenario-weighted ranges, and fair-value returns.
Research Manager and PM free-text fallbacks are saved for diagnosis but block
formal publication because the model handoff is not schema-valid.

The public PM memo uses eight stable reader-facing sections, but length follows company
complexity and analytical closure rather than a character quota. It is the only
reader-facing report: every decision-relevant fact, assumption, sensitivity,
counterargument and model-change implication must be synthesized there. Duplicate
summaries, raw debate retellings, generation self-checks and machine bookkeeping remain
internal JSON/audit/archive artifacts instead of becoming a second PM report.

## 8. Share-count, handoff, and fixed-PM controls

Diluted shares are deterministic master data. The pipeline first reads the
latest Tushare `pledge_stat.total_share` value (10,000 shares, converted to
million shares), then cross-checks market capitalization divided by the same
snapshot close. A difference above 2% blocks release. LLM-supplied share count
cannot override either source. Parent profit / diluted shares recalculates every
forecast and scenario EPS; PE fair value and equity-value/share conversions are
then recalculated. A non-PE per-share valuation built on a rejected denominator
is cleared and must be rebuilt rather than cosmetically rescaled.

Reported EPS extracted from filing text is cross-checked against same-period
parent profit and deterministic shares. A difference above 2% marks the EPS as
unverified with `pdf_table_column_shift_suspected`; it cannot enter the shared
model as a reported fact.

Research Manager and PM outputs now persist `canonical_model_snapshot` arrays
and explicit accepted change rows. Saved artifacts are
`2_research/canonical_plan.json` and
`5_portfolio/canonical_decision.json`. The release audit compares underwriting
packet -> Research Manager -> PM values and units. A changed or dropped line
without a matching accepted change row blocks publication.

The Research Manager now runs this underwriting-to-manager comparison immediately
after its first structured response. If a populated line was dropped or changed
without an accepted change row, the selected deep model receives one compact,
machine-actionable repair pass before Trader and PM execution. The repair must either
restore the packet value or document the debated replacement and its financial impact;
it cannot waive the inconsistency. Metric comparison lowercases before normalization
and treats spaces versus underscores as equivalent unit formatting, preventing false
handoff blockers such as `Revenue` -> `evenue` or `CNY mn` vs `CNY_mn`.

DeepSeek thinking models that reject `tool_choice` use one schema-prompt JSON
call followed by Pydantic validation. This is recorded as
`schema_prompt_structured`, not an unvalidated free-text fallback.

The PM renderer owns the normal report structure. The public memo has eight Chinese
sections: conclusion/core conflict; company/profit pools; industry/competition;
three-year forecast; thesis/moat/transmission; accounting/capital allocation;
valuation/expected return; and risks/catalysts/verification. Their depth and length adapt
to the company and available evidence. Model-change, handoff, quality and legacy overflow
text are moved to the research appendix. After the first schema-valid draft, the selected
deep model performs a senior sell-side editorial review and, when warranted, one targeted
revision. The review trace is saved as `5_portfolio/editorial_review.json`. Review failure
keeps the first draft and does not stop the pipeline; only unrecoverable numeric, unit,
period, structured-output, or canonical-handoff contradictions can block publication.

## 9. Reader-facing forecast and thesis spine

Research Manager and PM structured outputs carry four analytical objects across every
A-share industry: `research_questions`, `forecast_takeaways`,
`forecast_assumptions`, and `core_theses`. Forecast assumptions record a historical
anchor, evidence status, bull/base/bear range, sensitivity, confidence, and verification
gate. Missing shipment, ASP, utilization, renewal, NIM, credit-cost, commodity-spread,
or other industry-native evidence forces an explicitly top-down or bounded assumption;
it cannot be reverse-engineered and presented as verified bottom-up precision.

The public fourth section renders forecast take-aways, a reader-oriented financial table,
the assumption/sensitivity registry, and model limitations. The raw canonical snapshot
is audit metadata and lives in Appendix A. The fifth section renders only two to four
ranked thesis cards, each closing takeaway, evidence, strongest counterevidence,
financial transmission, market pricing, and falsification. Raw thesis/moat ledgers remain
in the appendix. Missing analytical objects trigger one advisory editorial revision but
do not mechanically block the pipeline.
