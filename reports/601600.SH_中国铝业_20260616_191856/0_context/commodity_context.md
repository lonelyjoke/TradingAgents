# Commodity and product price context for 601600.SH as of 2026-06-16

- Company/product map: Chalco
- Look-back window for futures proxies: 90 days
- Spread note: Use SHFE aluminum as the timely proxy; alumina, power cost, and capacity utilization drive spreads.

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
| Aluminum | main product | Tushare futures proxy | AL2607.SHF | 23830 | 20260616 | -4.22% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AL, selected by open interest/volume; curve=AL2607.SHF close=23830, oi=229636, vol=223624 | AL2608.SHF close=23895, oi=211792, vol=159295 | AL2609.SHF close=23940, oi=115950, vol=72205 | AL2610.SHF close=23980, oi=47391, vol=31755 | AL2611.SHF close=24000, oi=15856, vol=2791 | AL2612.SHF close=24005, oi=16996, vol=2573 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.