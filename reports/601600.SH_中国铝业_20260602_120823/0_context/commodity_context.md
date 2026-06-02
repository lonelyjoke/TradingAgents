# Commodity and product price context for 601600.SH as of 2026-06-02

- Company/product map: 中国铝业
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
| Aluminum | industry proxy | Tushare futures proxy | AL.SHF | 24360 | 20260601 | -1.75% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AL, selected by open interest/volume; curve=AL2606.SHF close=24290, oi=51960, vol=8554 | AL2607.SHF close=24360, oi=293773, vol=175312 | AL2608.SHF close=24425, oi=168987, vol=53546 | AL2609.SHF close=24480, oi=95446, vol=23245 | AL2610.SHF close=24510, oi=36911, vol=2974 | AL2611.SHF close=24525, oi=12468, vol=1196 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.