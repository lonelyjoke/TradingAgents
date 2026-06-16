# Commodity and product price context for 601168.SH as of 2026-06-16

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
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Tin | Tushare fut_daily -> SHFE SN contracts | SN.SHF | LME tin | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lead | Tushare fut_daily -> SHFE PB contracts | PB.SHF | LME lead | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Zinc | Tushare fut_daily -> SHFE ZN contracts | ZN.SHF | LME zinc | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | industry proxy | Tushare futures proxy | CU.SHF | 105590 | 20260615 | 7.10% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2606.SHF close=105610, oi=5535, vol=2260 | CU2607.SHF close=105590, oi=148486, vol=84449 | CU2608.SHF close=105690, oi=135087, vol=56591 | CU2609.SHF close=105660, oi=90413, vol=21439 | CU2610.SHF close=105530, oi=32338, vol=5029 | CU2611.SHF close=105480, oi=16569, vol=2328 |
| Silver | industry proxy | Tushare futures proxy | AG.SHF | 16876 | 20260615 | -15.54% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2606.SHF close=16800, oi=4736, vol=688 | AG2607.SHF close=16847, oi=16774, vol=25623 | AG2608.SHF close=16876, oi=263068, vol=766795 | AG2609.SHF close=16898, oi=18742, vol=62603 | AG2610.SHF close=16908, oi=106685, vol=320396 | AG2611.SHF close=16918, oi=7631, vol=5795 |
| Tin | industry proxy | Tushare futures proxy | SN.SHF | 425560 | 20260615 | 15.02% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=SN, selected by open interest/volume; curve=SN2606.SHF close=425200, oi=4344, vol=130 | SN2607.SHF close=425560, oi=36090, vol=220734 | SN2608.SHF close=426500, oi=25720, vol=64669 | SN2609.SHF close=427230, oi=15546, vol=26617 | SN2610.SHF close=428060, oi=3588, vol=2836 | SN2611.SHF close=429220, oi=556, vol=543 |
| Lead | industry proxy | Tushare futures proxy | PB.SHF | 16240 | 20260615 | -2.43% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=PB, selected by open interest/volume; curve=PB2606.SHF close=16190, oi=4360, vol=140 | PB2607.SHF close=16240, oi=80967, vol=69945 | PB2608.SHF close=16280, oi=69261, vol=37655 | PB2609.SHF close=16330, oi=16646, vol=9117 | PB2610.SHF close=16355, oi=409, vol=69 | PB2611.SHF close=16405, oi=204, vol=41 |
| Zinc | industry proxy | Tushare futures proxy | ZN2608.SHF | 24875 | 20260615 | 6.24% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=ZN, selected by open interest/volume; curve=ZN2606.SHF close=24815, oi=6000, vol=110 | ZN2607.SHF close=24830, oi=68599, vol=118628 | ZN2608.SHF close=24875, oi=79180, vol=79145 | ZN2609.SHF close=24910, oi=24680, vol=19265 | ZN2610.SHF close=24930, oi=5915, vol=2743 | ZN2611.SHF close=24905, oi=3532, vol=442 |
| Lithium carbonate | industry proxy | Tushare futures proxy | LC.GFE | 174440 | 20260615 | 16.20% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=169400, oi=42156, vol=9939 | LC2608.GFE close=173500, oi=15559, vol=1679 | LC2609.GFE close=174440, oi=450397, vol=177039 | LC2610.GFE close=175180, oi=9355, vol=264 | LC2611.GFE close=175660, oi=30739, vol=4112 | LC2612.GFE close=177700, oi=13786, vol=936 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.