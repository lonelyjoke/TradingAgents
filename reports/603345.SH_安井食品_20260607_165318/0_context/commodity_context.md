# Commodity and product price context for 603345.SH as of 2026-06-07

- Company/product map: Anjoy Foods
- Look-back window for futures proxies: 90 days
- Spread note: For frozen-food processors, these are cost proxies rather than realized input prices. Fish paste/surimi, poultry, flour, packaging, cold-chain and channel promotion still require filings, official data, or reputable industry checks before quantification.

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
| Live hog futures | meat raw-material cost proxy | Tushare futures proxy | LH2607.DCE | 10235 | 20260605 | -16.79% | 300 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=LH, selected nearest active contract; main/open-interest contract kept as reference; main_contract=LH.DCE close=11780, oi=186171; curve=LH2607.DCE close=10235, oi=75140, vol=56602 | LH2609.DCE close=11780, oi=186171, vol=137021 | LH2611.DCE close=12635, oi=99545, vol=28171 | LH2701.DCE close=13345, oi=73880, vol=12046 | LH2703.DCE close=13140, oi=66424, vol=8430 | LH2705.DCE close=13730, oi=14537, vol=2961 |
| Soybean meal futures | feed and protein-chain cost proxy | Tushare futures proxy | M2607.DCE | 2749 | 20260605 | -5.34% | 36207 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=M, selected nearest active contract; main/open-interest contract kept as reference; main_contract=M.DCE close=2918, oi=2432078; curve=M2607.DCE close=2749, oi=337165, vol=68390 | M2608.DCE close=2903, oi=272009, vol=23196 | M2609.DCE close=2918, oi=2432078, vol=1196179 | M2611.DCE close=2946, oi=329178, vol=22617 | M2612.DCE close=2995, oi=172835, vol=9739 | M2701.DCE close=2993, oi=849580, vol=293475 |
| Corn futures | feed and starch/flour-chain cost proxy | Tushare futures proxy | C2607.DCE | 2323 | 20260605 | -3.37% | 129282 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=C, selected nearest active contract; main/open-interest contract kept as reference; main_contract=C.DCE close=2323, oi=960924; curve=C2607.DCE close=2323, oi=960924, vol=704119 | C2609.DCE close=2326, oi=683442, vol=331149 | C2611.DCE close=2285, oi=339917, vol=51115 | C2701.DCE close=2288, oi=71999, vol=21852 | C2703.DCE close=2293, oi=126288, vol=11290 | C2705.DCE close=2318, oi=13766, vol=2169 |
| Palm oil futures | edible-oil cost proxy for prepared dishes | Tushare futures proxy | P2606.DCE | 8967 | 20260605 | -7.84% | 849 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=P, selected nearest active contract; main/open-interest contract kept as reference; main_contract=P.DCE close=9382, oi=534188; curve=P2606.DCE close=8967, oi=703, vol=21 | P2607.DCE close=9116, oi=38936, vol=23177 | P2608.DCE close=9226, oi=41190, vol=7087 | P2609.DCE close=9382, oi=534188, vol=727489 | P2610.DCE close=9469, oi=22978, vol=3487 | P2611.DCE close=9534, oi=8238, vol=1697 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.