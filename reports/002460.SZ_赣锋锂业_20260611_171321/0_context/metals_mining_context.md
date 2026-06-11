# Metals-mining verification context for 002460.SZ as of 2026-06-11

- Status: triggered
- Company: 赣锋锂业
- Tushare industry: 小金属
- Business model: lithium resource, processing, and battery-materials platform
- Metals covered: Lithium carbonate
- Trigger reason: curated A-share metals / mining ticker list

## Company Watchlist
- lithium carbonate price, spodumene cost, inventory, and impairment
- mine ramp, processing utilization, and downstream demand
- equity-accounted assets, capex, and cycle-trough survival

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 38.5285 | 3.1564 | N/A | N/A | 29.7187 | 616.3357 | 55.2582 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts (LC.GFE) | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Commodity Price Evidence Handoff
# Commodity and product price context for 002460.SZ as of 2026-06-11

- Company/product map: Ganfeng Lithium
- Look-back window for futures proxies: 180 days
- Spread note: Lithium carbonate futures proxy product price; lithium concentrate costs require external data.

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
| Lithium carbonate | main product | Tushare futures proxy | LC.GFE | 174600 | 20260611 | 72.77% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2606.GFE close=169000, oi=360, vol=314 | LC2607.GFE close=170300, oi=48594, vol=18166 | LC2608.GFE close=173700, oi=14493, vol=2686 | LC2609.GFE close=174600, oi=448867, vol=244951 | LC2610.GFE close=175060, oi=9398, vol=334 | LC2611.GFE close=175900, oi=29420, vol=9207 |

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
| 2026年一季度报告 | ...司信息披露解释性公告第 1 号——非经常性损益》中列举的非经常性损益项目界定为 经常性损益的项目的情形。 （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 资产负债表项目 2026 年 3 月 31 日 2025 年 12 月 31 日 变动比例 原因分析 主要系为防范汇率波动风险， 交易性金融资产 306,755,472.37 140,305,754.66 118.63% 增持美元交易性金融资产所 致； 主要系本期衍生金融工具公允 衍生金融资产 16,556,014.00 32,958,800.00 -49.77% 价值变动所致； 主要系收到的银行承兑票据增 应收款项融资 2,737,393,323.83 1,548,922,381.86 76.73% 加所致； 主要系本期收回部分应收股利 其他应收款 829,358,205.05 1,446,785,471.94 -42.68% 所致； 主要系基于资金管理，本期定 其他流动资产 2,739,71... |
| 2025年年度报告 | ...前， 新能源汽车销量对政府补贴、充电网络建设、汽车上牌政策等仍有一定依赖 性，如果未来相关政策进行调整或政策不能得到有效落实，将会对公司所处 的锂行业产生不利影响。 应对措施：公司密切关注政府政策及行业走势，及时跟踪了解市场需求 变化，加强风险管理，加深对行业特征、产品走势分析和研判，对公司战略 进行动态管控，保持对市场及时反应。 2 江西赣锋锂业集团股份有限公司 2025 年年度报告全文 2、锂资源开发风险 根据相关行业准则，如 JORC 规则作出的锂资源量及储量的估计仍具有 不确定性，不能作为开采或加工原材料锂资源的保证。估算的锂资源量及储 量需要基于专业知识、经验及行业惯例等不同因素判断锂辉石、卤水、锂黏 土等锂资源中锂的含量及品位，以及能否以经济实惠的方法开采并加工，提 取数量、取样结果、样品分析及作出估计的人员采用的方法及经验等多种因 素均会影响估算的准确程度。所开发的锂资源可能于质量、产量、开采成本 或加工成本等多种方式与锂资源储量的估计有所不同，或不具备... |
| 2025年三季度报告 | ...告期金额 年初至报告期期末金额 说明 非流动性资产处置损益（包 主要系处置部分储能电站和 括已计提资产减值准备的冲 -757,641.77 498,192,433.81 联营企业 LAC 产生的收益 销部分） 计入当期损益的政府补助 （与公司正常经营业务密切 相关、符合国家政策规定、 43,738,480.63 194,626,537.90 按照确定的标准享有、对公 司损益产生持续影响的政府 补助除外） 除同公司正常经营业务相关 的有效套期保值业务外，非 主要系持有的金融资产产生 金融企业持有金融资产和金 588,606,329.37 371,422,693.14 的公允价值变动损益以及处 融负债产生的公允价值变动 置金融资产产生的投资损益 损益以及处置金融资产和金 融负债产生的损益 计入当期损益的对非金融企 28,277,868.41 90,811,418.65 业收取的资金占用费 单独进行减值测试的应收款 639,000.00 4,337,905.40 项减值准备... |
| 2025年半年度报告 | ...发展、政府政策以及全球及地区经 济状况等，锂需求取决于终端市场锂的使用情况以及整体经济状况。近年 来，锂需求增加主要由电动汽车电池及储能电池的需求迅速增长所推动，各 国政府大力发展新能源汽车产业，推出优惠政策鼓励购买电动汽车。目前， 新能源汽车销量对政府补贴、充电网络建设、汽车上牌政策等仍有一定依赖 性，如果未来相关政策进行调整或政策不能得到有效落实，将会对公司所处 的锂行业产生不利影响。 2、锂资源开发风险 根据相关行业准则，如 JORC 规则作出的锂资源量及储量的估计仍具有 不确定性，不能作为开采或加工原材料锂资源的保证。估算的锂资源量及储 量需要基于专业知识、经验及行业惯例等不同因素判断锂辉石、卤水、锂黏 2 江西赣锋锂业集团股份有限公司 2025 年半年度报告全文 土等锂资源中锂的含量及品位，以及能否以经济实惠的方法开采并加工，提 取数量、取样结果、样品分析及作出估计的人员采用的方法及经验等多种因 素均会影响估算的准确程度。所开发的锂资源可能于质量、产量、开采... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000629.SZ | 钒钛股份 | 373.789 | 2.3143 | N/A | 10.4624 | 13.5669 | 173.3322 |
| 000633.SZ | 合金投资 | 275.0487 | 10.2025 | N/A | 12.292 | 58.1709 | -10.5209 |
| 000657.SZ | 中钨高新 | 89.6701 | 16.6244 | N/A | 30.4503 | 59.3819 | 264.4444 |
| 000762.SZ | 西藏矿业 | 6910.1865 | 5.2004 | N/A | 45.445 | 48.3217 | 241.2626 |
| 000831.SZ | 中国稀土 | 239.3296 | 11.5386 | N/A | 20.8361 | 11.0458 | 90.7983 |
| 000960.SZ | 锡业股份 | 24.5723 | 2.8245 | N/A | 10.044 | 47.3526 | 73.71 |
| 000962.SZ | 东方钽业 | 119.2913 | 7.6301 | N/A | 14.8854 | 23.5338 | -3.8159 |
| 000969.SZ | 安泰科技 | 61.234 | 3.9707 | N/A | 17.1293 | 43.4399 | 20.1947 |

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