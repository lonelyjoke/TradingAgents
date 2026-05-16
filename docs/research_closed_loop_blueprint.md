# Research Closed-Loop Blueprint

The system should answer three different investment questions without
collapsing them into one opinion:

1. **Company quality** — is this a good business?
2. **Current odds** — does today's price offer attractive expected value?
3. **Relative allocation** — is this the best place to deploy capital versus
   peers and alternative positions in the same industrial chain?

## End-to-End Flow

```text
raw evidence
  -> verified facts / rejected themes / research gaps
  -> company operating diagnosis
  -> industry, peer, and supply-chain comparison
  -> earnings bridge
  -> market-implied expectation
  -> three-layer verdict
  -> rating, sizing, catalyst path, falsification
  -> future review against new evidence
```

## Module Responsibilities

| Layer | Main question | Representative context |
| --- | --- | --- |
| Evidence hygiene | What is verified? | thematic catalyst cross-check |
| Company reading | How does the business really work? | filing intelligence |
| Stewardship | Does management compound value? | management / capital-allocation context |
| Ownership and chips | Is the shareholder base stabilizing or creating overhang? | shareholder-structure context |
| Cross-sectional choice | Is there a better alternative? | peer comparison / supply-chain comparison |
| Earnings bridge | If the thesis is right, what moves in the P&L? | earnings-model context |
| Market expectations | What is already priced? | market-expectation context |
| Decision synthesis | What should we own now? | company quality / current odds / relative allocation verdicts |

## Closed-Loop Rules

- Every catalyst must connect to either an earnings lever or a valuation lever.
- Every thesis must state what the market currently appears to imply.
- Every final decision must separate business quality, current odds, and relative allocation.
- Every rating change must identify decisive new evidence rather than quietly reversing on noise.
- Every future run should compare new evidence with the previous decision, previous earnings bridge, and previous market-implied expectation.

## Current Implementation

- `tradingagents/dataflows/earnings_modeling.py`
  builds the earnings bridge.
- `tradingagents/dataflows/expectation_research.py`
  reverse-engineers the quote into approximate market expectations.
- `tradingagents/dataflows/governance_research.py`
  evaluates hard stewardship and capital-allocation signals.
- `tradingagents/dataflows/shareholder_research.py`
  evaluates ownership concentration, float, holder behavior, pledge, and unlock risk.
- `tradingagents/dataflows/filing_research.py`
  reads quarterly / half-year / annual reports as business documents.
- `tradingagents/dataflows/thematic_research.py`
  validates real thematic catalysts.
- `tradingagents/dataflows/tushare_research.py`
  supports peer comparison and valuation context.
- `tradingagents/dataflows/supply_chain_research.py`
  compares alternative profit pools inside curated industrial chains.

The final structured outputs now include:

- `earnings_model_bridge`
- `market_implied_expectation`
- `company_quality_verdict`
- `current_odds_verdict`
- `relative_allocation_verdict`
- `management_capital_allocation_verdict`
- `shareholder_structure_verdict`

These fields are intentionally separate from the headline rating so the system
can distinguish a good company from a good stock and from the best current
capital allocation choice.
