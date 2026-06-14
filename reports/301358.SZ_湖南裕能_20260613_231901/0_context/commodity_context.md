# Commodity and product price context for 301358.SZ as of 2026-06-13

- Company/product map: Hunan Yuneng
- Look-back window for futures proxies: 90 days
- Spread note: For LFP cathode producers, lithium carbonate is a critical raw-material cost proxy, not the realized cathode selling price. Margin work still needs LFP cathode ASP, iron phosphate cost, processing fee, capacity utilization, customer mix, and inventory-cost lag evidence.

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
| Lithium carbonate | LFP cathode raw-material cost proxy | Tushare futures proxy | LC.GFE | 175300 | 20260612 | 9.82% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2606.GFE close=172800, oi=0, vol=113 | LC2607.GFE close=170640, oi=45900, vol=12250 | LC2608.GFE close=174320, oi=15050, vol=1912 | LC2609.GFE close=175300, oi=447123, vol=196809 | LC2610.GFE close=175780, oi=9371, vol=328 | LC2611.GFE close=176180, oi=30212, vol=4645 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.