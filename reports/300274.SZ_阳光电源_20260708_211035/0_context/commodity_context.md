# Commodity and product price context for 300274.SZ as of 2026-07-08

- Company/product map: 阳光电源
- Look-back window for futures proxies: 90 days
- Spread note: Products inferred from stock name/industry and recent filing text. Verify whether these proxies match the company's actual revenue mix.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
No exchange-traded metal source audit applies to the mapped products.

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rebar | steel cost proxy | Tushare futures proxy | RB.SHF | 3096 | 20260708 | 0.00% | 18000 | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=RB, selected by open interest/volume; curve=RB2607.SHF close=3160, oi=10080, vol=2850 | RB2608.SHF close=3053, oi=2139, vol=196 | RB2609.SHF close=3085, oi=240736, vol=29809 | RB2610.SHF close=3096, oi=2042617, vol=854272 | RB2611.SHF close=3099, oi=219538, vol=23309 | RB2612.SHF close=3124, oi=2728, vol=1074 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.