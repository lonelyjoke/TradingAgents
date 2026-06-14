# Commodity and product price context for 300285.SZ as of 2026-06-12

- Company/product map: 国瓷材料
- Look-back window for futures proxies: 90 days
- Spread note: Products inferred from stock name/industry and recent filing text. Verify whether these proxies match the company's actual revenue mix.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
| metal | domestic_price_chain | contract_example | overseas_cross_check | coverage_status |
| --- | --- | --- | --- | --- |
| Copper | Tushare fut_daily -> SHFE CU contracts | CU.SHF | COMEX HG futures; LME copper | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | industry proxy | Tushare futures proxy | CU2607.SHF | 104660 | 20260612 | 4.68% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2606.SHF close=104570, oi=6015, vol=8155 | CU2607.SHF close=104660, oi=149144, vol=97909 | CU2608.SHF close=104640, oi=126498, vol=63667 | CU2609.SHF close=104650, oi=88055, vol=24129 | CU2610.SHF close=104540, oi=31224, vol=6554 | CU2611.SHF close=104540, oi=17027, vol=2474 |
| Silver | industry proxy | Tushare futures proxy | AG2608.SHF | 15972 | 20260612 | -21.12% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2606.SHF close=15982, oi=5132, vol=136 | AG2607.SHF close=15965, oi=18581, vol=29738 | AG2608.SHF close=15972, oi=268836, vol=888666 | AG2609.SHF close=15990, oi=19064, vol=64447 | AG2610.SHF close=15999, oi=104980, vol=373757 | AG2611.SHF close=16018, oi=7690, vol=4407 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.