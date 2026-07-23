# Commodity and product price context for 000933.SZ as of 2026-07-21

- Company/product map: 神火股份
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
| Aluminum | Tushare fut_daily -> SHFE AL contracts | AL.SHF | LME aluminum | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Coking coal | industry proxy | Tushare futures proxy | JM.DCE | 1275 | 20260721 | -7.41% | N/A | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=JM, selected by open interest/volume; curve=JM2608.DCE close=1275, oi=8942, vol=4327 | JM2609.DCE close=1275, oi=417542, vol=789368 | JM2610.DCE close=1287.5, oi=50488, vol=9347 | JM2611.DCE close=1297.5, oi=43612, vol=5603 | JM2612.DCE close=1300.5, oi=38264, vol=4489 | JM2701.DCE close=1483.5, oi=198207, vol=96381 |
| Aluminum | industry proxy | Tushare futures proxy | AL.SHF | 23160 | 20260721 | -4.93% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHFE, prefix=AL, selected by open interest/volume; curve=AL2608.SHF close=23155, oi=127470, vol=73837 | AL2609.SHF close=23160, oi=261945, vol=204658 | AL2610.SHF close=23150, oi=94807, vol=43706 | AL2611.SHF close=23150, oi=33986, vol=11955 | AL2612.SHF close=23165, oi=36190, vol=10482 | AL2701.SHF close=23165, oi=16342, vol=6814 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.