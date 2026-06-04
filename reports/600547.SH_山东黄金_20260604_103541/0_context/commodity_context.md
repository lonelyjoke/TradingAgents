# Commodity and product price context for 600547.SH as of 2026-06-04

- Company/product map: 山东黄金
- Look-back window for futures proxies: 90 days
- Spread note: Products inferred from stock name/industry. Verify whether these proxies match the company's actual revenue mix.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gold | industry proxy | Tushare futures proxy | AU.SHF | 977.08 | 20260603 | -14.35% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AU, selected by open interest/volume; curve=AU2606.SHF close=973.74, oi=6018, vol=1536 | AU2607.SHF close=975.08, oi=2162, vol=1242 | AU2608.SHF close=977.08, oi=192532, vol=153332 | AU2610.SHF close=979.26, oi=53140, vol=30176 | AU2612.SHF close=981.46, oi=33871, vol=8332 | AU2702.SHF close=984.32, oi=5987, vol=796 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.