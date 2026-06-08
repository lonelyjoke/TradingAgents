# Commodity and product price context for 600362.SH as of 2026-06-08

- Company/product map: Jiangxi Copper
- Look-back window for futures proxies: 90 days
- Spread note: Use SHFE copper as the timely proxy; separate mining, smelting TC/RC, inventory, and trading exposure.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
| metal | domestic_price_chain | contract_example | overseas_cross_check | coverage_status |
| --- | --- | --- | --- | --- |
| Copper | Tushare fut_daily -> SHFE CU contracts | CU.SHF | COMEX HG futures; LME copper | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | main product | Tushare futures proxy | CU.SHF | 105150 | 20260605 | 3.58% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2606.SHF close=105170, oi=30595, vol=17530 | CU2607.SHF close=105150, oi=173561, vol=110386 | CU2608.SHF close=105240, oi=122679, vol=44354 | CU2609.SHF close=105300, oi=80882, vol=17423 | CU2610.SHF close=105340, oi=25468, vol=3337 | CU2611.SHF close=105250, oi=14878, vol=2343 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.