# Industry Cycle Scan for 600338.SH as of 2026-06-16

- Cycle verdict: downcycle / failed-rebound risk
- Confidence: medium
- Use: this is a pre-valuation gate. Company earnings and valuation should be read after this cycle stage is stated.

## Cycle Evidence Matrix
| layer | stage read | evidence read |
| --- | --- | --- |
| commodity/product price | downcycle / failed-rebound risk | Mapped product proxy fell 16.3% over the look-back window; margin and inventory assumptions require stress-case treatment. |
| metals/mining | metal-price and mine-economics verification required | Metals/mining context is available; realized prices, reserves, grade, AISC/unit cost, project ramp, hedging, and NAV/SOTP should govern cycle language. |

## Extracted Evidence Lines
- | product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
- | Silver | industry proxy | Tushare futures proxy | AG2608.SHF | 16716 | 20260616 | -16.29% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2607.SHF close=16678, oi=14906, vol=16195 | AG2608.SHF close=16716, oi=261018, vol=547167 
- | Lead | industry proxy | Tushare futures proxy | PB2607.SHF | 16310 | 20260616 | -2.34% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=PB, selected by open interest/volume; curve=PB2607.SHF close=16310, oi=72615, vol=58506 | PB2608.SHF close=16355, oi=69301, vol=30567 | PB2
- | Zinc | industry proxy | Tushare futures proxy | ZN2608.SHF | 24765 | 20260616 | 5.77% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=ZN, selected by open interest/volume; curve=ZN2607.SHF close=24720, oi=60824, vol=73345 | ZN2608.SHF close=24765, oi=80630, vol=52678 | ZN26
- | Lithium carbonate | industry proxy | Tushare futures proxy | LC2609.GFE | 169980 | 20260616 | 13.30% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=165220, oi=37649, vol=10863 | LC2608.GFE close=169580, oi=15242,
- - Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- ## Freight Index Evidence
- - Use BDTI as a broad crude/dirty tanker proxy, not a specific VLCC TD3C TCE quote.

## Analyst Instructions
- Do not write `cycle bottom`, `周期底部`, or `cycle reversal` as a fact unless this scan and company financials both support it.
- If cycle evidence says bottom-testing or evidence-limited, use language such as `bottom-right validation stage`, `右侧待验证`, or `needs confirmation`.
- Tie the cycle verdict to the earnings bridge: ASP/price, spread, volume, utilization, inventory, cash conversion, and valuation multiple.
- State falsification signals: price/spread breakdown, inventory rebuild, order/contract-liability deterioration, cash-conversion failure, or peer-relative evidence that contradicts the cycle read.