# Industry Cycle Scan for 300750.SZ as of 2026-06-16

- Cycle verdict: bottom-right validation stage
- Confidence: medium
- Use: this is a pre-valuation gate. Company earnings and valuation should be read after this cycle stage is stated.

## Cycle Evidence Matrix
| layer | stage read | evidence read |
| --- | --- | --- |
| commodity/product price | bottom-right validation stage | Mapped product proxy rose 13.2% over the look-back window; this supports bottoming language only if inventory, demand, and company cash conversion confirm. |
| building materials | construction-chain cycle verification required | Building-materials context is available; ASP, regional demand, capacity discipline, inventory, receivables, and cash collection should govern cycle language. |
| metals/mining | metal-price and mine-economics verification required | Metals/mining context is available; realized prices, reserves, grade, AISC/unit cost, project ramp, hedging, and NAV/SOTP should govern cycle language. |

## Extracted Evidence Lines
- | product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
- | Lithium carbonate | raw material proxy | Tushare futures proxy | LC.GFE | 169980 | 20260616 | 13.23% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=165220, oi=37649, vol=10863 | LC2608.GFE close=169580, oi=15242,
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