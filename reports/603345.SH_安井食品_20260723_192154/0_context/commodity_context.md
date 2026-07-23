# Commodity and product price context for 603345.SH as of 2026-07-23

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

## Company Commodity Earnings Bridge
No ticker-specific deterministic commodity earnings bridge is registered. Price evidence may inform direction only; it cannot set EPS, fair value, rating or sizing until output, realized-price, unit-cost, tax/ownership and capacity controls are supplied.

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | window_price_range | window_average_price | latest_price_percentile | annualized_volatility | distribution_scenario_band | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | meat raw-material cost proxy | Tushare futures proxy | LH2607.DCE | 10000 | 20260723 | -6.59% | 9840 - 11320 | 10304.6 | 28.6% | 34.39% | P20=9980; P50=10205; P80=10592 | N/A | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=LH, selected nearest active contract; main/open-interest contract kept as reference; main_contract=LH.DCE close=11330, oi=192345; curve=LH2607.DCE close=10000, oi=11, vol=0 | LH2609.DCE close=11330, oi=192345, vol=132541 | LH2611.DCE close=12325, oi=142975, vol=53575 | LH2701.DCE close=13015, oi=98123, vol=17937 | LH2703.DCE close=12835, oi=91189, vol=12520 | LH2705.DCE close=13880, oi=35277, vol=4860 |
| Soybean meal futures | feed and protein-chain cost proxy | Tushare futures proxy | M2608.DCE | 3153 | 20260723 | 5.91% | 2880 - 3153 | 2983.69 | 100.0% | 11.46% | P20=2924; P50=2957; P80=3039 | N/A | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=M, selected nearest active contract; main/open-interest contract kept as reference; main_contract=M.DCE close=3175, oi=2052273; curve=M2608.DCE close=3153, oi=17245, vol=5758 | M2609.DCE close=3175, oi=2052273, vol=1680654 | M2611.DCE close=3212, oi=512813, vol=137135 | M2612.DCE close=3248, oi=274615, vol=20647 | M2701.DCE close=3233, oi=1463484, vol=558908 | M2703.DCE close=3148, oi=287898, vol=44282 |
| Corn futures | feed and starch/flour-chain cost proxy | Tushare futures proxy | C2609.DCE | 2278 | 20260723 | -2.65% | 2269 - 2349 | 2315.14 | 11.4% | 8.11% | P20=2299; P50=2320; P80=2337 | N/A | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=C, selected nearest active contract; main/open-interest contract kept as reference; main_contract=C.DCE close=2278, oi=945377; curve=C2609.DCE close=2278, oi=945377, vol=467037 | C2611.DCE close=2255, oi=388469, vol=104982 | C2701.DCE close=2260, oi=138632, vol=36303 | C2703.DCE close=2270, oi=179839, vol=14908 | C2705.DCE close=2307, oi=24529, vol=4933 | C2707.DCE close=2318, oi=12276, vol=4825 |
| Palm oil futures | edible-oil cost proxy for prepared dishes | Tushare futures proxy | P2608.DCE | 9332 | 20260723 | -2.72% | 8955 - 9628 | 9198.83 | 88.6% | 18.04% | P20=9090.6; P50=9163; P80=9234.4 | N/A | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=P, selected nearest active contract; main/open-interest contract kept as reference; main_contract=P.DCE close=9515, oi=439006; curve=P2608.DCE close=9332, oi=2248, vol=275 | P2609.DCE close=9515, oi=439006, vol=813078 | P2610.DCE close=9573, oi=36765, vol=7350 | P2611.DCE close=9624, oi=37009, vol=8745 | P2612.DCE close=9713, oi=22788, vol=3097 | P2701.DCE close=9795, oi=252160, vol=229234 |

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