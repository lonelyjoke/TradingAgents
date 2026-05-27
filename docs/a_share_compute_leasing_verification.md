# A-share compute-leasing verification layer

This layer is intentionally gated. It should only affect the research flow when
official or semi-official evidence indicates that the target has compute-leasing,
AI-compute, GPU-rental, or intelligent-computing-center exposure.

## Routing Rule

- `Status: triggered`: downstream agents must analyze the compute-leasing thesis.
- `Status: not_applicable`: downstream agents must not inject compute-leasing,
  GPU, IDC, or data-center valuation assumptions into the stock.
- News-only mentions can create a watch item, but cannot trigger base-case
  valuation uplift.

## Evidence Hierarchy

1. Official filings and announcements.
2. Official investor interaction.
3. Reputable news or web corroboration.
4. Market rumor.

A-share compute-leasing details are often hard to obtain. Missing GPU counts,
customer identity, utilization, lease price, power cost, or financing terms are
research gaps, not neutral evidence and not negative proof.

## Verification Gates

- Asset gate: GPU/server model, quantity, delivery, ownership versus financing
  lease, data-center location, rack capacity, power, PUE, network, and O&M.
- Contract gate: signed customer contracts, customer quality, related-party
  status, contract duration, pricing, minimum usage, receivables, prepayments,
  and cash collection.
- Unit-economics gate: revenue per card/rack/month, utilization, electricity,
  rack, bandwidth, O&M, depreciation, financing cost, EBITDA, ROIC, and payback.
- Capex/funding gate: procurement commitments, fixed assets, construction in
  progress, financing-lease liabilities, guarantees, debt maturity, cash balance,
  and impairment risk.
- Transition-credibility gate: synergy with legacy business, management
  capability, IDC/cloud/GPU operation experience, and whether the move looks like
  disciplined capital allocation rather than theme chasing.
- SOTP gate: legacy business, verified compute business, and unverified compute
  option must be valued separately.
