# Commodity and product price context for 300750.SZ as of 2026-06-27

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
| Lithium carbonate | raw material proxy | Tushare futures proxy | LC.GFE | 150220 | 20260626 | -12.47% | 48544 | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=145960, oi=17346, vol=5867 | LC2608.GFE close=149160, oi=19091, vol=5335 | LC2609.GFE close=150220, oi=443472, vol=321674 | LC2610.GFE close=151140, oi=10598, vol=2534 | LC2611.GFE close=150380, oi=37331, vol=13906 | LC2612.GFE close=151800, oi=13183, vol=1585 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral for direction and only as a confidence cap; it cannot prove margin deterioration or margin resilience by itself.