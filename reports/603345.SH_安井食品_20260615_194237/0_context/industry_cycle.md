# Industry Cycle Scan for 603345.SH as of 2026-06-15

- Cycle verdict: downcycle / failed-rebound risk
- Confidence: medium
- Use: this is a pre-valuation gate. Company earnings and valuation should be read after this cycle stage is stated.

## Cycle Evidence Matrix
| layer | stage read | evidence read |
| --- | --- | --- |
| commodity/product price | downcycle / failed-rebound risk | Mapped product proxy fell 16.1% over the look-back window; margin and inventory assumptions require stress-case treatment. |

## Extracted Evidence Lines
- | product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
- | Live hog futures | meat raw-material cost proxy | Tushare futures proxy | LH2607.DCE | 10170 | 20260615 | -16.05% | 1945 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=LH, selected nearest active contract; main/open-interest contract kept as reference; main_contract=LH.DCE close=
- | Soybean meal futures | feed and protein-chain cost proxy | Tushare futures proxy | M2607.DCE | 2764 | 20260615 | -4.62% | 40204 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=M, selected nearest active contract; main/open-interest contract kept as reference; main_contract=M.DCE c
- | Corn futures | feed and starch/flour-chain cost proxy | Tushare futures proxy | C2607.DCE | 2322 | 20260615 | -3.09% | 76084 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=C, selected nearest active contract; main/open-interest contract kept as reference; main_contract=C2609.DCE 
- | Palm oil futures | edible-oil cost proxy for prepared dishes | Tushare futures proxy | P2607.DCE | 8977 | 20260615 | -8.92% | 1057 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=P, selected nearest active contract; main/open-interest contract kept as reference; main_contract=P.DC
- - Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- ## Freight Index Evidence
- - Use BDTI as a broad crude/dirty tanker proxy, not a specific VLCC TD3C TCE quote.

## Analyst Instructions
- Do not write `cycle bottom`, `周期底部`, or `cycle reversal` as a fact unless this scan and company financials both support it.
- If cycle evidence says bottom-testing or evidence-limited, use language such as `bottom-right validation stage`, `右侧待验证`, or `needs confirmation`.
- Tie the cycle verdict to the earnings bridge: ASP/price, spread, volume, utilization, inventory, cash conversion, and valuation multiple.
- State falsification signals: price/spread breakdown, inventory rebuild, order/contract-liability deterioration, cash-conversion failure, or peer-relative evidence that contradicts the cycle read.