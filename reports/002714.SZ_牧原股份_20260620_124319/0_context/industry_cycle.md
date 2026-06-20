# Industry Cycle Scan for 002714.SZ as of 2026-06-20

- Cycle verdict: cycle evidence insufficient
- Confidence: low
- Use: this is a pre-valuation gate. Company earnings and valuation should be read after this cycle stage is stated.

## Cycle Evidence Matrix
| layer | stage read | evidence read |
| --- | --- | --- |
| general industry | cycle evidence insufficient | No usable sector-native cycle module was available. Do not claim a cycle bottom/top from company PE, PB, or one-quarter financials alone. |

## Extracted Evidence Lines
- | product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
- | Breeding sow inventory | capacity leading signal | official livestock market evidence | https://www.moa.gov.cn/ztzl/szcpxx/jdsj/2026/202603/ | See official source | See official source | Not computed | N/A | Fetched official MOA livestock archive page; use as verified cycle evidence, parse exact series before quantif
- | Live hog futures | timely market-implied price signal | Tushare futures proxy | LH2607.DCE | 9900 | 20260618 | -10.24% | 3910 | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=LH, selected nearest active contract; main/open-interest contract kept as reference; main_contract=LH.DCE c
- - If the current-month breeding-sow inventory has not yet been officially released, state the latest available month and keep the current month as a verification item.
- - Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- ## Freight Index Evidence
- - Use BDTI as a broad crude/dirty tanker proxy, not a specific VLCC TD3C TCE quote.
- - Use BCTI as a broad clean/product tanker proxy, not a specific MR/LR route quote.

## Analyst Instructions
- Do not write `cycle bottom`, `周期底部`, or `cycle reversal` as a fact unless this scan and company financials both support it.
- If cycle evidence says bottom-testing or evidence-limited, use language such as `bottom-right validation stage`, `右侧待验证`, or `needs confirmation`.
- Tie the cycle verdict to the earnings bridge: ASP/price, spread, volume, utilization, inventory, cash conversion, and valuation multiple.
- State falsification signals: price/spread breakdown, inventory rebuild, order/contract-liability deterioration, cash-conversion failure, or peer-relative evidence that contradicts the cycle read.