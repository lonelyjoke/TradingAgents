# Commodity and product price context for 601600.SH as of 2026-06-04

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
| Aluminum | main product | Tushare futures proxy | AL.SHF | 24315 | 20260604 | -1.62% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AL, selected by open interest/volume; curve=AL2606.SHF close=24260, oi=34745, vol=8565 | AL2607.SHF close=24315, oi=274711, vol=205847 | AL2608.SHF close=24390, oi=180159, vol=78149 | AL2609.SHF close=24445, oi=98145, vol=30158 | AL2610.SHF close=24460, oi=38519, vol=6614 | AL2611.SHF close=24470, oi=12721, vol=1742 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.