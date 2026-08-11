# Commodity and product price context for 002407.SZ as of 2026-08-10

- Company/product map: 多氟多
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
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Company Commodity Earnings Bridge
No ticker-specific deterministic commodity earnings bridge is registered. Price evidence may inform direction only; it cannot set EPS, fair value, rating or sizing until output, realized-price, unit-cost, tax/ownership and capacity controls are supplied.

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | window_price_range | window_average_price | latest_price_percentile | annualized_volatility | distribution_scenario_band | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silver | industry proxy | Tushare futures proxy | AG2610.SHF | 15635 | 20260807 | -14.04% | 13545 - 18550 | 15264.6 | 69.6% | 48.69% | P20=14239; P50=14787.5; P80=16485 | 1261244 | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHFE, prefix=AG, selected by open interest/volume; curve=AG2608.SHF close=15583, oi=7770, vol=7872 | AG2609.SHF close=15617, oi=23030, vol=27659 | AG2610.SHF close=15635, oi=322723, vol=743843 | AG2611.SHF close=15657, oi=11068, vol=42594 | AG2612.SHF close=15664, oi=118399, vol=106188 | AG2701.SHF close=15699, oi=8439, vol=5797 |
| Lithium carbonate | industry proxy | Tushare futures proxy | LC2609.GFE | 140000 | 20260807 | -21.74% | 137760 - 178900 | 156274 | 8.7% | 40.47% | P20=143480; P50=155570; P80=167400 | 29873 | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFEX, prefix=LC, selected by open interest/volume; curve=LC2608.GFE close=139580, oi=3874, vol=305 | LC2609.GFE close=140000, oi=291475, vol=199880 | LC2610.GFE close=139320, oi=19622, vol=2585 | LC2611.GFE close=138960, oi=82610, vol=17199 | LC2612.GFE close=138800, oi=24866, vol=3754 | LC2701.GFE close=138660, oi=214967, vol=76300 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.
- Build bull/base/bear price decks from the dated range, average, percentile, volatility and futures curve shown above; label them as contract-history proxies, not company realized prices.
- A product-price sensitivity must show volume x price shock first. Gross-profit impact cannot exceed the revenue shock, and attributable net-profit impact must be lower after tax/minority interest unless a separate evidenced cost or by-product offset is shown.
- A production or sales scenario cannot exceed reported capacity unless the model separately identifies purchased/traded volume or dated commissioned capacity.
- Match coal grade and region. Do not use DCE JM coking coal, Qinhuangdao thermal coal or another broad coal index as a direct realized-price input for anthracite/lean-coal producers without an evidenced basis bridge.