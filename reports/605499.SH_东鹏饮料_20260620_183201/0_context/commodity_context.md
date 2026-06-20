# Commodity and product price context for 605499.SH as of 2026-06-20

- Company/product map: 东鹏饮料
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
| Gold | Tushare fut_daily -> SHFE AU contracts | AU.SHF | COMEX GC futures; LBMA gold benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gold | industry proxy | Tushare futures proxy | AU.SHF | 937.96 | 20260618 | -0.22% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AU, selected by open interest/volume; curve=AU2607.SHF close=936.9, oi=2385, vol=1925 | AU2608.SHF close=937.96, oi=167662, vol=258473 | AU2609.SHF close=938.24, oi=275, vol=182 | AU2610.SHF close=939.9, oi=63949, vol=43441 | AU2612.SHF close=941.8, oi=36144, vol=10198 | AU2702.SHF close=944.14, oi=5974, vol=1118 |
| Silver | industry proxy | Tushare futures proxy | AG.SHF | 16493 | 20260618 | 7.02% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2607.SHF close=16478, oi=12628, vol=22458 | AG2608.SHF close=16493, oi=245422, vol=761381 | AG2609.SHF close=16518, oi=17939, vol=66106 | AG2610.SHF close=16528, oi=108463, vol=349469 | AG2611.SHF close=16557, oi=7430, vol=4182 | AG2612.SHF close=16560, oi=63419, vol=46090 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral for direction and only as a confidence cap; it cannot prove margin deterioration or margin resilience by itself.