# Commodity and product price context for 300750.SZ as of 2026-07-06

- Company/product map: CATL
- Look-back window for futures proxies: 90 days
- Spread note: For battery makers, lithium carbonate is a cost proxy rather than a direct revenue product.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
| metal | domestic_price_chain | contract_example | overseas_cross_check | coverage_status |
| --- | --- | --- | --- | --- |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | raw material proxy | Tushare futures proxy | LC.GFE | 164560 | 20260706 | 3.28% | 46708 | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=161000, oi=1739, vol=194 | LC2608.GFE close=163960, oi=15905, vol=4979 | LC2609.GFE close=164560, oi=416855, vol=174787 | LC2610.GFE close=165100, oi=11772, vol=941 | LC2611.GFE close=165340, oi=38586, vol=5608 | LC2612.GFE close=166380, oi=15237, vol=1277 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.