# Commodity and product price context for 603345.SH as of 2026-06-15

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
| Live hog futures | meat raw-material cost proxy | Tushare futures proxy | LH2607.DCE | 10170 | 20260615 | -16.05% | 1945 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=LH, selected nearest active contract; main/open-interest contract kept as reference; main_contract=LH.DCE close=12145, oi=199891; curve=LH2607.DCE close=10170, oi=36295, vol=16165 | LH2609.DCE close=12145, oi=199891, vol=150862 | LH2611.DCE close=13120, oi=125403, vol=65859 | LH2701.DCE close=13600, oi=81942, vol=17830 | LH2703.DCE close=13405, oi=72515, vol=12613 | LH2705.DCE close=14005, oi=20438, vol=4902 |
| Soybean meal futures | feed and protein-chain cost proxy | Tushare futures proxy | M2607.DCE | 2764 | 20260615 | -4.62% | 40204 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=M, selected nearest active contract; main/open-interest contract kept as reference; main_contract=M.DCE close=2941, oi=2187566; curve=M2607.DCE close=2764, oi=269309, vol=53844 | M2608.DCE close=2925, oi=286488, vol=15917 | M2609.DCE close=2941, oi=2187566, vol=752215 | M2611.DCE close=2968, oi=339692, vol=20396 | M2612.DCE close=3009, oi=192229, vol=11446 | M2701.DCE close=3000, oi=986322, vol=173723 |
| Corn futures | feed and starch/flour-chain cost proxy | Tushare futures proxy | C2607.DCE | 2322 | 20260615 | -3.09% | 76084 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=C, selected nearest active contract; main/open-interest contract kept as reference; main_contract=C2609.DCE close=2320, oi=814863; curve=C2607.DCE close=2322, oi=677349, vol=525740 | C2609.DCE close=2320, oi=814863, vol=485385 | C2611.DCE close=2284, oi=347730, vol=73136 | C2701.DCE close=2285, oi=83849, vol=29260 | C2703.DCE close=2290, oi=142426, vol=9386 | C2705.DCE close=2316, oi=14928, vol=1141 |
| Palm oil futures | edible-oil cost proxy for prepared dishes | Tushare futures proxy | P2607.DCE | 8977 | 20260615 | -8.92% | 1057 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=P, selected nearest active contract; main/open-interest contract kept as reference; main_contract=P.DCE close=9232, oi=546990; curve=P2607.DCE close=8977, oi=28283, vol=18134 | P2608.DCE close=9081, oi=39032, vol=7531 | P2609.DCE close=9232, oi=546990, vol=627560 | P2610.DCE close=9299, oi=25957, vol=3127 | P2611.DCE close=9355, oi=13304, vol=2525 | P2612.DCE close=9432, oi=4599, vol=1301 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.