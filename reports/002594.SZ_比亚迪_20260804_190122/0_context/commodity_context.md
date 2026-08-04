# Commodity and product price context for 002594.SZ as of 2026-08-04

- Company/product map: 比亚迪
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
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Company Commodity Earnings Bridge
No ticker-specific deterministic commodity earnings bridge is registered. Price evidence may inform direction only; it cannot set EPS, fair value, rating or sizing until output, realized-price, unit-cost, tax/ownership and capacity controls are supplied.

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | window_price_range | window_average_price | latest_price_percentile | annualized_volatility | distribution_scenario_band | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | lithium-battery-material raw-material cost proxy | Tushare futures proxy | LC.GFE | 139380 | 20260804 | -22.09% | 137760 - 178900 | 156872 | 7.1% | 41.53% | P20=144424; P50=157830; P80=167272 | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFEX, prefix=LC, selected by open interest/volume; curve=LC2608.GFE close=139500, oi=4818, vol=691 | LC2609.GFE close=139380, oi=315871, vol=134684 | LC2610.GFE close=138940, oi=18038, vol=1409 | LC2611.GFE close=138740, oi=77705, vol=14576 | LC2612.GFE close=139180, oi=23166, vol=2812 | LC2701.GFE close=138440, oi=191340, vol=51840 |

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