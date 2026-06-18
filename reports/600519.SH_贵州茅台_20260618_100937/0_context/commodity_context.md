# Commodity and product price context for 600519.SH as of 2026-06-18

- Company/product map: 贵州茅台
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
| Silver | industry proxy | Tushare futures proxy | AG.SHF | 16865 | 20260617 | -4.31% | 250881 | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2607.SHF close=16824, oi=14113, vol=13398 | AG2608.SHF close=16865, oi=257889, vol=504536 | AG2609.SHF close=16889, oi=18109, vol=41430 | AG2610.SHF close=16901, oi=108548, vol=243274 | AG2611.SHF close=16916, oi=7570, vol=2215 | AG2612.SHF close=16921, oi=62265, vol=25700 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral for direction and only as a confidence cap; it cannot prove margin deterioration or margin resilience by itself.