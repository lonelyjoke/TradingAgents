# Industry Cycle Scan for 002487.SZ as of 2026-06-12

- Cycle verdict: downcycle / failed-rebound risk
- Confidence: medium
- Use: this is a pre-valuation gate. Company earnings and valuation should be read after this cycle stage is stated.

## Cycle Evidence Matrix
| layer | stage read | evidence read |
| --- | --- | --- |
| commodity/product price | downcycle / failed-rebound risk | Mapped product proxy fell 24.1% over the look-back window; margin and inventory assumptions require stress-case treatment. |

## Extracted Evidence Lines
- | product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
- | Silver | industry proxy | Tushare futures proxy | AG.SHF | 15416 | 20260611 | -24.06% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2606.SHF close=15390, oi=5194, vol=172 | AG2607.SHF close=15393, oi=19873, vol=35438 | AG2608.
- - Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- ## Freight Index Evidence
- - Use BDTI as a broad crude/dirty tanker proxy, not a specific VLCC TD3C TCE quote.
- - Use BCTI as a broad clean/product tanker proxy, not a specific MR/LR route quote.
- - Use BDI/BCI/BPI/BSI as broad dry bulk proxies, not exact voyage rates.
- - If VLCC TD3C, TCE, SCFI/CCFI, LNG, or route-level rates are not in the evidence table, list them as unverified key variables.

## Analyst Instructions
- Do not write `cycle bottom`, `周期底部`, or `cycle reversal` as a fact unless this scan and company financials both support it.
- If cycle evidence says bottom-testing or evidence-limited, use language such as `bottom-right validation stage`, `右侧待验证`, or `needs confirmation`.
- Tie the cycle verdict to the earnings bridge: ASP/price, spread, volume, utilization, inventory, cash conversion, and valuation multiple.
- State falsification signals: price/spread breakdown, inventory rebuild, order/contract-liability deterioration, cash-conversion failure, or peer-relative evidence that contradicts the cycle read.