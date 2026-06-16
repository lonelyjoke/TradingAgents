# Commodity and product price context for 600338.SH as of 2026-06-16

- Company/product map: 西藏珠峰
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
| Lead | Tushare fut_daily -> SHFE PB contracts | PB.SHF | LME lead | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Zinc | Tushare fut_daily -> SHFE ZN contracts | ZN.SHF | LME zinc | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silver | industry proxy | Tushare futures proxy | AG2608.SHF | 16716 | 20260616 | -16.29% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2607.SHF close=16678, oi=14906, vol=16195 | AG2608.SHF close=16716, oi=261018, vol=547167 | AG2609.SHF close=16730, oi=18298, vol=44298 | AG2610.SHF close=16746, oi=106139, vol=252347 | AG2611.SHF close=16749, oi=7600, vol=3545 | AG2612.SHF close=16765, oi=61717, vol=29490 |
| Lead | industry proxy | Tushare futures proxy | PB2607.SHF | 16310 | 20260616 | -2.34% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=PB, selected by open interest/volume; curve=PB2607.SHF close=16310, oi=72615, vol=58506 | PB2608.SHF close=16355, oi=69301, vol=30567 | PB2609.SHF close=16385, oi=17731, vol=7464 | PB2610.SHF close=16415, oi=397, vol=72 | PB2611.SHF close=16500, oi=169, vol=60 | PB2612.SHF close=16490, oi=86, vol=4 |
| Zinc | industry proxy | Tushare futures proxy | ZN2608.SHF | 24765 | 20260616 | 5.77% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=ZN, selected by open interest/volume; curve=ZN2607.SHF close=24720, oi=60824, vol=73345 | ZN2608.SHF close=24765, oi=80630, vol=52678 | ZN2609.SHF close=24815, oi=27354, vol=14982 | ZN2610.SHF close=24840, oi=6478, vol=2252 | ZN2611.SHF close=24850, oi=3612, vol=228 | ZN2612.SHF close=24825, oi=1266, vol=70 |
| Lithium carbonate | industry proxy | Tushare futures proxy | LC2609.GFE | 169980 | 20260616 | 13.30% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=165220, oi=37649, vol=10863 | LC2608.GFE close=169580, oi=15242, vol=3132 | LC2609.GFE close=169980, oi=449952, vol=187954 | LC2610.GFE close=170500, oi=9266, vol=312 | LC2611.GFE close=170900, oi=31534, vol=5730 | LC2612.GFE close=172640, oi=13309, vol=1823 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.