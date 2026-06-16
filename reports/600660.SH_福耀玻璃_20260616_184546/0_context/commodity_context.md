# Commodity and product price context for 600660.SH as of 2026-06-16

- Company/product map: 福耀玻璃
- Look-back window for futures proxies: 90 days
- Spread note: Products inferred from stock name/industry and recent filing text. Verify whether these proxies match the company's actual revenue mix.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
No exchange-traded metal source audit applies to the mapped products.

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rebar | industry proxy | Tushare futures proxy | RB2610.SHF | 3169 | 20260616 | 0.13% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=RB, selected by open interest/volume; curve=RB2607.SHF close=3189, oi=41237, vol=13330 | RB2608.SHF close=3131, oi=2875, vol=96 | RB2609.SHF close=3148, oi=237017, vol=26766 | RB2610.SHF close=3169, oi=1620085, vol=589396 | RB2611.SHF close=3182, oi=160715, vol=11510 | RB2612.SHF close=3197, oi=4259, vol=23 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.