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
`error` must be reconciled before the report is treated as publication- or
investment-committee-ready.
