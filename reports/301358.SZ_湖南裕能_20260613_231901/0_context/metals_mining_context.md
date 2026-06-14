# Metals-mining verification context for 301358.SZ as of 2026-06-13

- Status: triggered
- Company: 湖南裕能
- Tushare industry: 电气设备
- Business model: metals / mining / smelting company
- Metals covered: Lithium carbonate
- Trigger reason: commodity map contains exchange-traded metal products

## Company Watchlist
- resource / reserve quality, grade, and equity production
- unit cost, AISC, sustaining capex, and project ramp
- commodity price, FX, inventory, hedging, and impairment sensitivity
- mining / smelting / trading split, leverage, and NAV / SOTP bridge

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 24.1351 | 3.2702 | 0.49 | N/A | 16.1572 | 1337.7746 | 61.2283 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts (LC.GFE) | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Commodity Price Evidence Handoff
# Commodity and product price context for 301358.SZ as of 2026-06-13

- Company/product map: Hunan Yuneng
- Look-back window for futures proxies: 180 days
- Spread note: For LFP cathode producers, lithium carbonate is a critical raw-material cost proxy, not the realized cathode selling price. Margin work still needs LFP cathode ASP, iron phosphate cost, processing fee, capacity utilization, customer mix, and inventory-cost lag evidence.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
| metal | domestic_price_chain | contract_example | overseas_cross_check | coverage_status |
| --- | --- | --- | --- | --- |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | LFP cathode raw-material cost proxy | Tushare futures proxy | LC.GFE | 175300 | 20260612 | 73.46% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2606.GFE close=172800, oi=0, vol=113 | LC2607.GFE close=170640, oi=45900, vol=12250 | LC2608.GFE close=174320, oi=15050, vol=1912 | LC2609.GFE close=175300, oi=447123, vol=196809 | LC2610.GFE close=175780, oi=9371, vol=328 | LC2611.GFE close=176180, oi=30212, vol=4645 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.

## Business Model / Evidence Gate
| bucket | must_verify | valuation_rule |
| --- | --- | --- |
| Mining asset quality | reserve / resource tonnage, grade, recovery rate, equity output, mine life | higher multiple only when reserve quality and low-cost output are evidenced |
| Unit economics | cash cost, AISC, sustaining capex, energy/labor/input cost, FX | cycle upside needs cost-curve resilience, not only rising metal prices |
| Smelting / trading split | TC/RC, processing margin, inventory exposure, realized price versus exchange proxy | do not value smelting/trading earnings like scarce mining NAV |
| Project ramp / capex | construction progress, capex budget, commissioning, permitting, jurisdiction risk | NAV/SOTP should haircut delayed, over-budget, or high-risk projects |
| Risk management | hedging, derivatives, inventory marks, debt maturity, FX, impairment | earnings quality haircut when commodity beta is amplified by leverage or MTM risk |

## Nonferrous Cycle Rating Gate
| layer | question | evidence_rule |
| --- | --- | --- |
| Industry Cycle View | Is the metal in structural tightness, ordinary restocking, or a fading price cycle? | Test supply ceiling/capacity policy, inventories, operating rates, LME/SHFE spreads, imports/exports, and downstream demand before judging prosperity. |
| Company Expression View | Does this company express the cycle through scarce resources, low-cost smelting, or pass-through processing? | Separate resource ownership, alumina/self-supply, power cost, equity output, segment margin, capex, and working-capital conversion. |
| Valuation/Odds View | Is low PE a peak-earnings trap or an ROE re-rating path despite high PB? | Compare TTM and forward/normalized PE, PB-ROE, dividend coverage, trough valuation, and peer opportunity cost rather than using PB alone. |
| Tactical Attribution View | Was the recent move caused by metal price, sector beta, company residual, news/rumor, or liquidity/positioning? | Use same-metal equities, cross-metal equities, futures, announcements, news/rumor probe, turnover, and trend state before calling emotion-kill or fundamental repricing. |

## Aluminum Demand Bridge
Not an aluminum-focused profile; use the broader nonferrous cycle gate instead.

## Filing Text Evidence Snippets
| report | snippet |
| --- | --- |
| 2026年一季度报告 | ....74 188.11% 资金 应收账款 9,580,882,066.26 6,637,535,626.72 44.34% 本报告期营业收入大幅增长所致 预付款项 1,161,159,403.28 724,740,369.07 60.22% 主要系预付锂源采购款增加 本报告期期货保证金、押金保证金减少 其他应收款 192,113,644.94 299,775,395.17 -35.91% 及收回部分政府补助 主要系碳酸锂等材料价格上涨导致存货 存货 5,112,106,151.26 3,628,716,949.57 40.88% 金额增加 其他权益工具投资 150,000,000.00 不适用 本报告期新增对外股权投资 衍生金融负债 53,861,598.99 132,695,910.96 -59.41% 本报告期套期工具、衍生工具减少 应付票据 6,370,824,598.62 4,422,008,210.58 44.07% 本报告期开具的承兑汇票增加 应交税费 47... |
| 2025年三季度报告 | ... 年 12 月 31 日 变动率 重大变化说明 应收票据 2,136,536,548.74 692,518,775.89 208.52% 本报告期末已背书未到期的票据增加 应收账款 7,217,810,638.86 5,359,208,134.37 34.68% 本报告期销售规模增加，应收款项增加 预付款项 447,915,439.46 304,860,083.39 46.92% 本报告期产销规模增加，预付款增加 本报告期产销规模增加，存货备货数量增 存货 3,656,352,933.73 2,798,355,462.80 30.66% 加 在建工程 2,029,796,935.20 1,224,803,245.16 65.72% 本报告期工程投入增加 本报告期应收款项计提的坏账增加、股权 递延所得税资产 201,107,717.82 129,995,175.69 54.70% 激励费用增加，相应计提的递延所得税资 产增加 其他非流动资产 46,314,715.64 ... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000009.SZ | 中国宝安 | 350.6766 | 1.8154 | N/A | 25.0018 | 60.1965 | -89.6412 |
| 000049.SZ | 德赛电池 | 27.202 | 1.3112 | N/A | 9.8695 | 58.632 | 64.2285 |
| 000400.SZ | 许继电气 | 21.1207 | 1.8426 | N/A | 19.0118 | 47.5928 | -46.5044 |
| 000533.SZ | 顺钠股份 | 74.3243 | 7.4911 | N/A | 19.1201 | 63.2533 | -13.2792 |
| 000576.SZ | 甘化科工 | 44.8807 | 1.9129 | N/A | 29.4864 | 28.3504 | -73.476 |
| 000682.SZ | 东方电子 | 16.0587 | 2.6806 | N/A | 30.4499 | 52.8068 | 95.0553 |
| 000720.SZ | 新能泰山 | N/A | 2.7653 | N/A | 0.3364 | 61.0342 | -237.1974 |
| 000809.SZ | 和展能源 | N/A | 1.3222 | N/A | 17.153 | 34.5879 | 122.862 |

## Required Metals Valuation Bridge
- Build bull/base/bear cases from metal price, equity output, unit cost/AISC, FX, sustaining capex, and tax / minority interest.
- Separate mining NAV from smelting, refining, processing, trading, and investment income. Do not assign scarce-resource multiples to pass-through volume.
- Use mine-by-mine or segment SOTP when material assets have different metals, grades, jurisdictions, ramp status, or cost curves.
- Treat domestic exchange futures as timely proxies. Overseas COMEX/LME/LBMA or licensed spot sources are cross-checks unless explicitly fetched and dated.
- Safety-price work must use cycle-trough metal prices, survivable balance sheet, maintenance capex, and historical/peer trough valuation floors.
- For nonferrous names, split the rating into Industry Cycle View, Company Expression View, Valuation/Odds View, and Tactical Attribution View before issuing the final action.
- A low PE / high PB setup must be tested as either peak-earnings trap or ROE re-rating; PB alone is not enough for Underweight when earnings, cash flow, and dividends are being released.
- One-quarter receivables, contract liabilities, inventory, or impairment direction can cap conviction, but should not decide the rating without seasonality, aging, peer comparison, and cash-conversion evidence.

## Research Gaps To Close Before High Conviction
- resource / reserve tonnage, grade, recovery rate, and mine life
- equity output by mine, ramp schedule, and production guidance
- cash cost, AISC, sustaining capex, and unit cost in RMB and USD terms
- mining versus smelting / refining / trading split and segment margins
- commodity-price sensitivity table across metal price, FX, volume, and cost
- inventory, hedging / derivatives, working-capital, and impairment exposure
- project capex, construction-in-progress, jurisdiction risk, and NAV / SOTP bridge

## Analyst Instructions
- Treat this as the specialist metals / mining layer. It should override generic manufacturing or broad commodity framing when the target is a miner, smelter, or metal resource company.
- Price beta is not enough: connect exchange prices to realized selling price, volume, cost curve, inventory, hedging, capex, and balance-sheet survival.
- Missing reserve, grade, equity output, AISC, project-ramp, hedging, or NAV/SOTP evidence caps conviction and belongs in research gaps.
- If the final action is Underweight/Sell despite structural supply constraints, low PE, dividend support, or visible profit release, explicitly prove the profit-center downshift, cash-cycle deterioration, superior peer alternative, or over-pricing path.