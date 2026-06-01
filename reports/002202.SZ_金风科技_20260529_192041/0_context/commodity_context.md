# Commodity and product price context for 002202.SZ as of 2026-05-29

- Company/product map: 金风科技
- Look-back window for futures proxies: 90 days
- Spread note: No commodity mapping found. Add this ticker to COMPANY_COMMODITY_MAP before making product-price claims.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - stable hard evidence | official MOA monthly data + company sales announcements | capacity direction, realized company price/volume after parsing | monthly and usually delayed |
| 2 - timely proxy | DCE live-hog futures via Tushare | market-implied cycle/timing signal | proxy, not company realized spot price |
| 3 - optional high-frequency spot | authorized third-party spot datasets | daily regional hog price, piglet price, slaughter weight, secondary fattening | requires source permission and口径 validation before hard triggers |

## Evidence Table
No commodity mapping is available for this ticker.

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- For livestock companies, prioritize stable official/company evidence first, then use timely futures or authorized spot feeds to monitor the turn.
- Treat official MOA market pages as high-confidence cycle evidence, but do not quantify the cycle unless the exact monthly/weekly series is parsed from the source.
- If the current-month breeding-sow inventory has not yet been officially released, state the latest available month and keep the current month as a verification item.
- Do not state R32, R125, lithium, copper, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.