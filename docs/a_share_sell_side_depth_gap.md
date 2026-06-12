# A-share Sell-side Depth Gap Note

This note records the current state of the A-share research system after the
recent sell-side-depth upgrades. It is meant to answer two questions:

1. Which new modules are already part of the system?
2. What still prevents the system from producing consistently deep sell-side
   reports across different companies and industries?

## Newly Recorded Modules

The following derived research modules are now treated as part of the A-share
sell-side depth layer, not one-off company patches:

| Module | Purpose |
| --- | --- |
| `industry_cycle_context` | Summarizes industry cycle position, demand/supply balance, price/cost variables, and cycle evidence gaps before valuation. |
| `company_business_model_context` | Converts filing evidence into a business-model memo: products, revenue engines, segment economics, value-chain position, moat, and evidence gaps. |
| `industry_kpi_context` | Builds an industry-native KPI checklist so each company is judged by the variables that matter in its own sector. |
| `forecast_model_context` | Provides a driver-based forecast scaffold linking volume, ASP, cost, margin, operating profit, EPS, cash flow, and valuation assumptions. |
| `quality_audit_context` | Audits whether the final report has enough source, number, period, formula, peer, and falsification discipline to support its conclusion. |

The CLI report saver now persists these modules into `0_context` so a completed
report can be audited after the run:

- `industry_cycle.md`
- `company_business_model.md`
- `industry_kpi.md`
- `forecast_model.md`
- `quality_audit.md`

## Current Strengths

The system already has several traits required for deep sell-side research:

- Data hard gates: A-share reports require structured market/financial data and
  readable filing text before LLM generation.
- Broad evidence base: Tushare, CNINFO fallback, local disclosure cache,
  investor interaction, policy/planning, peer comparison, valuation, price
  attribution, commodity, supply-chain, and web fact-check contexts.
- Filing-first company understanding: financial-report intelligence extracts
  business model, segment economics, management discussion, cash conversion, and
  accounting-quality clues.
- Industry toolkits: gated sector playbooks exist for major tracks such as
  baijiu, compute leasing, defensive dividend, building materials, consumer
  staples, optical modules, biopharma, software/SaaS, insurance, medical
  devices, and metals/mining.
- Debate and decision structure: bull/bear/research-manager debate and PM
  decision prompts force investment thesis, contrary evidence, conviction,
  position, and verification checklist.
- Post-run audit: `data_coverage` and report-depth validators can flag missing
  business-segment breakdown, weak peer comparison, shallow valuation logic, and
  missing falsification conditions.

## Current Gaps

The system is still not yet a stable deep sell-side report machine. The main
gaps are structural:

- Industry coverage is uneven. Some companies trigger rich sector playbooks,
  while others fall back to generic contexts unless their industry-native
  variables are inferred from filing text.
- Peer universes are still too broad in many industries. Tushare industry labels
  are useful for screening, but they do not always define true operating peers,
  substitute assets, or value-chain alternatives.
- External high-frequency data is incomplete. ASP, channel inventory, tender
  data, order backlog, customer certification, utilization, regional price, and
  spot spread data often depend on web fact checks or manual sources.
- Forecasting is still scaffold-first. The system can ask for driver bridges,
  but it does not yet always produce a fully populated three-year segment model
  with sensitivity tables and explicit valuation math.
- Final report compliance is not hard enough. Validators can flag shallow
  output, but a weak report is not always blocked or automatically rerun with
  missing evidence questions.
- Source discipline needs to be stricter. Sell-side-grade reports need exact
  source, date, period, unit, formula, and whether each figure is reported,
  calculated, estimated, or unverified.
- Feedback is not yet fully automated. When one company report is shallow, the
  system should convert that failure into reusable industry rules, data
  probes, validators, and regression tests rather than company-specific patches.

## Latest Generalization From Report Failures

The recent Hunan Yuneng versus Ganfeng Lithium comparison exposed a systemic
problem: report depth depended too much on curated ticker mappings. Ganfeng had
commodity and supply-chain mappings, while Hunan Yuneng initially did not, so
its report missed lithium-material economics.

The fix generalizes beyond one ticker:

- Commodity research now infers lithium-material exposure from company name,
  Tushare industry, and recent filing text.
- Supply-chain research now infers lithium-chain segments from stock metadata
  and filing terms instead of requiring a curated ticker map.
- Industry KPI and forecast scaffolds now include a battery-material/cathode
  playbook covering demand, ASP, lithium carbonate cost, spread, capacity,
  customers, cash flow, and working capital.
- The report-depth validator now has battery-material gates so shallow reports
  can be flagged when they discuss cathode/lithium materials without driver
  bridges.

## Direction To Reach Stable Deep Sell-side Reports

The next phase should focus on stability, not more isolated modules:

1. Build industry-native playbooks for the major uncovered A-share sectors.
2. Replace broad peer screens with value-chain and business-model peer sets.
3. Add hard report gates that block or rerun reports when required sections are
   missing.
4. Convert every shallow-report postmortem into reusable inference rules,
   source probes, validators, and tests.
5. Expand data sources for high-frequency sector variables and record their
   reliability in `data_coverage`.
6. Make the final PM report explicitly tie rating and position to forecast
   drivers, valuation assumptions, peer alternatives, and falsification signals.

