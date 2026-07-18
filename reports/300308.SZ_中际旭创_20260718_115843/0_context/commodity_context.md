# Commodity and product price context for 300308.SZ as of 2026-07-18

- Company/product map: 中际旭创
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
| Tin | Tushare fut_daily -> SHFE SN contracts | SN.SHF | LME tin | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | industry proxy | Tushare futures proxy | CU2609.SHF | 103370 | 20260717 | -1.31% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHFE, prefix=CU, selected by open interest/volume; curve=CU2608.SHF close=103550, oi=127472, vol=63668 | CU2609.SHF close=103370, oi=180125, vol=69929 | CU2610.SHF close=103160, oi=67956, vol=16536 | CU2611.SHF close=103200, oi=29791, vol=5181 | CU2612.SHF close=103080, oi=49738, vol=5766 | CU2701.SHF close=102930, oi=19012, vol=1574 |
| Tin | industry proxy | Tushare futures proxy | SN2608.SHF | 403970 | 20260717 | -6.64% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHFE, prefix=SN, selected by open interest/volume; curve=SN2608.SHF close=403970, oi=33178, vol=225621 | SN2609.SHF close=403660, oi=30720, vol=84285 | SN2610.SHF close=403460, oi=12095, vol=18467 | SN2611.SHF close=403050, oi=2197, vol=1597 | SN2612.SHF close=403070, oi=755, vol=337 | SN2701.SHF close=403000, oi=355, vol=284 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.