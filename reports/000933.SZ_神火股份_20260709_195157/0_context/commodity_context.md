# Commodity and product price context for 000933.SZ as of 2026-07-09

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
| Coking coal | industry proxy | Tushare futures proxy | JM.DCE | 1290 | 20260709 | 22.16% | 550 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=JM, selected by open interest/volume; curve=JM2607.DCE close=1218, oi=1015, vol=0 | JM2608.DCE close=1272.5, oi=40790, vol=8228 | JM2609.DCE close=1290, oi=440244, vol=492717 | JM2610.DCE close=1307.5, oi=48154, vol=2810 | JM2611.DCE close=1326, oi=39127, vol=2094 | JM2612.DCE close=1332.5, oi=31283, vol=1830 |
| Aluminum | industry proxy | Tushare futures proxy | AL.SHF | 23060 | 20260709 | -6.30% | 131035 | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AL, selected by open interest/volume; curve=AL2607.SHF close=23020, oi=21570, vol=6355 | AL2608.SHF close=23060, oi=227737, vol=165244 | AL2609.SHF close=23100, oi=217296, vol=84817 | AL2610.SHF close=23120, oi=69526, vol=22676 | AL2611.SHF close=23155, oi=28896, vol=4740 | AL2612.SHF close=23165, oi=29617, vol=3777 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.