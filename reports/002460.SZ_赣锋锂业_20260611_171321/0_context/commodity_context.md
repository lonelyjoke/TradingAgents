# Commodity and product price context for 002460.SZ as of 2026-06-11

- Company/product map: Ganfeng Lithium
- Look-back window for futures proxies: 90 days
- Spread note: Lithium carbonate futures proxy product price; lithium concentrate costs require external data.

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
| Lithium carbonate | main product | Tushare futures proxy | LC.GFE | 174600 | 20260611 | 14.81% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2606.GFE close=169000, oi=360, vol=314 | LC2607.GFE close=170300, oi=48594, vol=18166 | LC2608.GFE close=173700, oi=14493, vol=2686 | LC2609.GFE close=174600, oi=448867, vol=244951 | LC2610.GFE close=175060, oi=9398, vol=334 | LC2611.GFE close=175900, oi=29420, vol=9207 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.