# Commodity and product price context for 002487.SZ as of 2026-06-12

- Company/product map: 大金重工
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
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silver | industry proxy | Tushare futures proxy | AG.SHF | 15416 | 20260611 | -24.06% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2606.SHF close=15390, oi=5194, vol=172 | AG2607.SHF close=15393, oi=19873, vol=35438 | AG2608.SHF close=15416, oi=279388, vol=1018532 | AG2609.SHF close=15421, oi=19480, vol=82014 | AG2610.SHF close=15434, oi=104903, vol=400465 | AG2611.SHF close=15435, oi=7733, vol=6372 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.