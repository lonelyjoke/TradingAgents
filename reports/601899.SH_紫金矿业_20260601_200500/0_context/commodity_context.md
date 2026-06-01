# Commodity and product price context for 601899.SH as of 2026-06-01

- Company/product map: Zijin Mining
- Look-back window for futures proxies: 90 days
- Spread note: Use metal futures as price proxies; mine cost curves still require external research.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - stable hard evidence | official MOA monthly data + company sales announcements | capacity direction, realized company price/volume after parsing | monthly and usually delayed |
| 2 - timely proxy | DCE live-hog futures via Tushare | market-implied cycle/timing signal | proxy, not company realized spot price |
| 3 - optional high-frequency spot | authorized third-party spot datasets | daily regional hog price, piglet price, slaughter weight, secondary fattening | requires source permission and口径 validation before hard triggers |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | main product | Tushare futures proxy | CU.SHF | 104680 | 20260601 | 2.53% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2606.SHF close=104610, oi=49970, vol=14397 | CU2607.SHF close=104680, oi=177344, vol=71092 | CU2608.SHF close=104750, oi=112948, vol=22468 | CU2609.SHF close=104740, oi=75684, vol=10918 | CU2610.SHF close=104730, oi=24265, vol=2541 | CU2611.SHF close=104750, oi=13622, vol=605 |
| Gold | main product | Tushare futures proxy | AU.SHF | 983.58 | 20260601 | -16.79% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=ALL, prefix=AU, selected by open interest/volume; curve=AU2606.SHF close=981, oi=8757, vol=3785 | AU2607.SHF close=982.48, oi=1947, vol=3923 | AU2608.SHF close=983.58, oi=193569, vol=240345 | AU2610.SHF close=986.02, oi=51432, vol=34720 | AU2612.SHF close=988.48, oi=32886, vol=11091 | AU2702.SHF close=991.02, oi=5789, vol=1512 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- For livestock companies, prioritize stable official/company evidence first, then use timely futures or authorized spot feeds to monitor the turn.
- Treat official MOA market pages as high-confidence cycle evidence, but do not quantify the cycle unless the exact monthly/weekly series is parsed from the source.
- If the current-month breeding-sow inventory has not yet been officially released, state the latest available month and keep the current month as a verification item.
- Do not state R32, R125, lithium, copper, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.