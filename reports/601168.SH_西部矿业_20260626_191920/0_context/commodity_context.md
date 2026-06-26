# Commodity and product price context for 601168.SH as of 2026-06-26

- Company/product map: 西部矿业
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
| Gold | Tushare fut_daily -> SHFE AU contracts | AU.SHF | COMEX GC futures; LBMA gold benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Tin | Tushare fut_daily -> SHFE SN contracts | SN.SHF | LME tin | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | industry proxy | Tushare futures proxy | CU.SHF | 101560 | 20260626 | 6.06% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2607.SHF close=101530, oi=66162, vol=43745 | CU2608.SHF close=101560, oi=159247, vol=119672 | CU2609.SHF close=101570, oi=120696, vol=43673 | CU2610.SHF close=101520, oi=44345, vol=7717 | CU2611.SHF close=101520, oi=22037, vol=3241 | CU2612.SHF close=101490, oi=37291, vol=3601 |
| Gold | industry proxy | Tushare futures proxy | AU.SHF | 883.3 | 20260626 | -12.97% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AU, selected by open interest/volume; curve=AU2607.SHF close=881.84, oi=853, vol=2522 | AU2608.SHF close=883.3, oi=148354, vol=272086 | AU2609.SHF close=884.32, oi=344, vol=638 | AU2610.SHF close=885.1, oi=76106, vol=44204 | AU2612.SHF close=887.4, oi=38335, vol=13948 | AU2702.SHF close=889.24, oi=5971, vol=1158 |
| Silver | industry proxy | Tushare futures proxy | AG.SHF | 14212 | 20260626 | -19.74% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2607.SHF close=14191, oi=6917, vol=10261 | AG2608.SHF close=14212, oi=240550, vol=1056428 | AG2609.SHF close=14239, oi=21882, vol=105890 | AG2610.SHF close=14248, oi=132188, vol=501718 | AG2611.SHF close=14256, oi=8124, vol=8725 | AG2612.SHF close=14278, oi=67367, vol=75928 |
| Tin | industry proxy | Tushare futures proxy | SN.SHF | 387220 | 20260626 | 4.45% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=SN, selected by open interest/volume; curve=SN2607.SHF close=386360, oi=10138, vol=103104 | SN2608.SHF close=387220, oi=38781, vol=292437 | SN2609.SHF close=387600, oi=19565, vol=61607 | SN2610.SHF close=388150, oi=5880, vol=9277 | SN2611.SHF close=388330, oi=825, vol=1996 | SN2612.SHF close=389010, oi=651, vol=675 |
| Lithium carbonate | industry proxy | Tushare futures proxy | LC.GFE | 150220 | 20260626 | -12.47% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=145960, oi=17346, vol=5867 | LC2608.GFE close=149160, oi=19091, vol=5335 | LC2609.GFE close=150220, oi=443472, vol=321674 | LC2610.GFE close=151140, oi=10598, vol=2534 | LC2611.GFE close=150380, oi=37331, vol=13906 | LC2612.GFE close=151800, oi=13183, vol=1585 |
| Rebar | industry proxy | Tushare futures proxy | RB.SHF | 3093 | 20260626 | -1.47% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=RB, selected by open interest/volume; curve=RB2607.SHF close=3144, oi=30530, vol=9786 | RB2608.SHF close=3071, oi=2242, vol=373 | RB2609.SHF close=3066, oi=255288, vol=41871 | RB2610.SHF close=3093, oi=1901198, vol=684521 | RB2611.SHF close=3108, oi=181399, vol=8921 | RB2612.SHF close=3120, oi=4243, vol=56 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral for direction and only as a confidence cap; it cannot prove margin deterioration or margin resilience by itself.