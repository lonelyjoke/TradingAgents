# Metals-mining verification context for 000933.SZ as of 2026-07-21

- Status: triggered
- Company: 神火股份
- Tushare industry: 铝
- Business model: metals / mining / smelting company
- Metals covered: Aluminum
- Trigger reason: commodity map contains exchange-traded metal products

## Company Watchlist
- resource / reserve quality, grade, and equity production
- unit cost, AISC, sustaining capex, and project ramp
- commodity price, FX, inventory, hedging, and impairment sensitivity
- mining / smelting / trading split, leverage, and NAV / SOTP bridge

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9.8466 | 2.0454 | 3.2482 | N/A | 33.4845 | 223.2834 | 40.8811 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Aluminum | Tushare fut_daily -> SHFE AL contracts (AL.SHF) | LME aluminum | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Commodity Price Evidence Handoff
# Commodity and product price context for 000933.SZ as of 2026-07-21

- Company/product map: 神火股份
- Look-back window for futures proxies: 180 days
- Spread note: Products inferred from stock name/industry and recent filing text. Verify whether these proxies match the company's actual revenue mix.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
| metal | domestic_price_chain | contract_example | overseas_cross_check | coverage_status |
| --- | --- | --- | --- | --- |
| Aluminum | Tushare fut_daily -> SHFE AL contracts | AL.SHF | LME aluminum | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Coking coal | industry proxy | Tushare futures proxy | JM.DCE | 1275 | 20260721 | -7.41% | N/A | Verified by Tushare futures daily data. | exchange=DCE, query_exchange=DCE, prefix=JM, selected by open interest/volume; curve=JM2608.DCE close=1275, oi=8942, vol=4327 | JM2609.DCE close=1275, oi=417542, vol=789368 | JM2610.DCE close=1287.5, oi=50488, vol=9347 | JM2611.DCE close=1297.5, oi=43612, vol=5603 | JM2612.DCE close=1300.5, oi=38264, vol=4489 | JM2701.DCE close=1483.5, oi=198207, vol=96381 |
| Aluminum | industry proxy | Tushare futures proxy | AL.SHF | 23160 | 20260721 | -4.93% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHFE, prefix=AL, selected by open interest/volume; curve=AL2608.SHF close=23155, oi=127470, vol=73837 | AL2609.SHF close=23160, oi=261945, vol=204658 | AL2610.SHF close=23150, oi=94807, vol=43706 | AL2611.SHF close=23150, oi=33986, vol=11955 | AL2612.SHF close=23165, oi=36190, vol=10482 | AL2701.SHF close=23165, oi=16342, vol=6814 |

## Analyst Instructions
- Treat Tushare futures data as a proxy only when it matches the company's main product or key input.
- Treat whitelist web pages as evidence snippets unless an exact price/date/unit is parsed and shown.
- Do not state R32, R125, lithium, copper, gold, inventory, or spread changes as facts unless they appear in the evidence table.
- If the product has no reliable data source, list it as an unverified key variable instead of inventing a price change.
- If a thesis-critical input is marked missing, treat it as neutral non-evidence and a retrieval task; it cannot prove margin deterioration/resilience or mechanically change rating, conviction, or sizing.

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

## Sell-Side Metals Deep-Dive Template
| section | must_answer | output_standard |
| --- | --- | --- |
| 1. Cycle and price deck | cycle stage, SHFE/LME/COMEX price deck, inventory/spread/import-export evidence, bull/base/bear metal prices | state whether the thesis is structural tightness, restocking, or peak-cycle extension |
| 2. Asset and production table | reserve/resource tonnage, grade, recovery rate, mine life, equity output, ramp schedule by material mine | mark each mine/asset as reported, estimated, proxy, stale, or missing |
| 3. Cost curve and margins | cash cost, AISC/unit cost, sustaining capex, by-product credits, energy/labor/FX, TC/RC for smelting | show why margin expands or compresses under each metal-price scenario |
| 4. Segment SOTP / NAV | mining NAV, smelting/refining earnings value, trading value, new-project optionality, minority interest and debt | do not value pass-through trading revenue at scarce-resource multiples |
| 5. Sensitivity and balance sheet | net profit/EPS/FCF sensitivity to metal price, output, AISC, FX, capex, hedging and inventory marks | connect target price, entry band, and stop-loss to explicit scenario assumptions |
| 6. Verification calendar | dated catalysts, production reports, interim reports, project milestones, contract-liability conversion, dividend/capex signals | turn each missing thesis-critical item into a dated follow-up item |

## Aluminum Demand Bridge
| channel | analyst_rule |
| --- | --- |
| Property / construction | Treat as a cyclical drag or stabilizer; do not let it erase other demand channels without quantified evidence. |
| Grid, PV, EV, lightweighting | Use as core demand support only when volume, utilization, order, or policy evidence is supplied; otherwise mark as positive assumption. |
| Exports and domestic-overseas arbitrage | Check LME/SHFE spread, import/export incentives, tariffs, and inventory movement before claiming price-gap upside. |
| AI / robotics / new manufacturing | Keep as indirect optionality unless aluminum volume linkage is quantified; it can lift sentiment but should not dominate the base case. |
| Monetary / inflation beta | Separate broad liquidity beta from physical tightness; commodity inflation can help but does not replace supply-demand proof. |

## Filing Text Evidence Snippets
| report | snippet |
| --- | --- |
| 2026年一季度报告 | ...煤电股份有限公司 2026 年第一季度报告 本报告期较 序 期初余额/去年同期 项目 本期金额（元） 年初/上年同 变动原因及简要说明 号 （元） 期增减（%） 报告期内，受电解铝产品售价上涨 1 货币资金 7,604,892,403.01 3,017,300,280.50 152.04 影响，公司销售收入及回款规模增 加。 报告期内，公司子公司上海神火国 2 交易性金融资产 14,410,025.00 - 100.00 际贸易有限公司套期保值产品公允 价值发生变动。 报告期内，公司铝加工板块量价齐 3 应收账款 1,461,917,412.34 1,069,147,929.52 36.74 升带动营收增长，叠加客户账期较 长，应收账款相应增加。 报告期末，公司持有的承兑汇票较 4 应收款项融资 550,228,768.87 367,074,048.74 49.90 期初增加。 报告期内，公司收回了部分到期的 5 一年内到期的非流动资产 1,156,547,579.9... |
| 2025年年度报告 | ...南神火建筑安装工程有限公司 中国证监会 指 中国证券监督管理委员会 深交所 指 深圳证券交易所 《 证 券 时 报 》《 中 国 证 券 报 》《 上 海 证 券 报 》《 证 券 日 报 》 和 巨 潮 资 讯 网 指定媒体 指 （http://www.cninfo.com.cn） 元 指 人民币元 电解铝 指 以氧化铝为原材料，通过电解得到的单质铝，产品主要为液铝和铝锭。 氧化铝 指 铝电解生产中的主要原料，由铝土矿加工而成。 保有储量 指 一定时间内（截至报告日期）矿山所拥有的资源实际储量 在现有经济和技术条件下，可从矿藏（或油气藏）中采出的那一部分矿石量（或 可采储量 指 。 油气量） 煤炭产品 指 原煤及深加工产品，包括原煤、洗精煤、洗混煤、块煤、配煤等。 原煤 指 从地下开采出来后只选出规定粒度矸石，未经任何加工的煤炭。 煤化程度最高的煤；无烟煤固定碳含量高，挥发分产率低，密度大，硬度大，燃 无烟煤 指 点高，燃烧时不冒烟。 贫煤 指 变质程度高、挥发分最... |
| 2025年三季度报告 | ...（三）主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 本报告期较 序 期初余额/去年同期 项目 本期金额（元） 年初/上年同 变动原因及简要说明 号 （元） 期增减（%） 报告期内，公司盈利及票据贴现金 1 货币资金 10,173,245,409.63 3,282,589,519.74 209.92 额同比增加。 报告期末，公司子公司上海神火国 2 交易性金融资产 3,043,300.00 - 100.00 际贸易有限公司套期保值产品公允 价值发生变动。 报告期内，支付和到期了部分承兑 3 应收票据 23,620,072.89 77,600,279.48 -69.56 汇票。 报告期末，公司持有的信用等级较 4 应收款项融资 473,403,647.49 285,388,426.92 65.88 高的票据较期初增加。 报告期内，公司收到处置河南神火 5 其他应收款 218,421,972.50 347,573,332.98 -37.16 发电有限公司股权... |
| 2025年半年度报告 | ... 指 神火国际集团有限公司 中国证监会 指 中国证券监督管理委员会 深交所 指 深圳证券交易所 《 证 券 时 报 》《 中 国 证 券 报 》《 上 海 证 券 报 》《 证 券 日 报 》 和 巨 潮 资 讯 网 指定媒体 指 （http://www.cninfo.com.cn） 元 指 人民币元 电解铝 指 以氧化铝为原材料，通过电解得到的单质铝，产品主要为液铝和铝锭。 氧化铝 指 铝电解生产中的主要原料，由铝土矿加工而成。 保有储量 指 一定时间内（截至报告日期）矿山所拥有的资源实际储量 在现有经济和技术条件下，可从矿藏（或油气藏）中采出的那一部分矿石量（或 可采储量 指 。 油气量） 煤炭产品 指 原煤及深加工产品，包括原煤、洗精煤、洗混煤、块煤、配煤等。 原煤 指 从地下开采出来后只选出规定粒度矸石，未经任何加工的煤炭。 煤化程度最高的煤；无烟煤固定碳含量高，挥发分产率低，密度大，硬度大，燃 无烟煤 指 点高，燃烧时不冒烟。 贫煤 指 变质程度高、挥发分最... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000807.SZ | 云铝股份 | 10.0601 | 2.4493 | N/A | 31.5743 | 17.7381 | 269.4536 |
| 000933.SZ | 神火股份 | 9.8466 | 2.0454 | N/A | 33.4845 | 40.8811 | 223.2834 |
| 002540.SZ | 亚太科技 | 15.7279 | 1.0457 | N/A | 8.3789 | 35.6984 | -57.7303 |
| 002578.SZ | 闽发铝业 | N/A | 1.7434 | N/A | 8.1071 | 32.8252 | 410.9591 |
| 002824.SZ | 和胜股份 | 41.4975 | 2.9769 | N/A | 12.9699 | 57.0622 | 104.6516 |
| 002996.SZ | 顺博合金 | 17.3292 | 1.2098 | N/A | 4.3598 | 76.2108 | 8.0059 |
| 003038.SZ | 鑫铂股份 | N/A | 0.8352 | N/A | 4.3392 | 75.7971 | -122.7758 |
| 300057.SZ | 万顺新材 | N/A | 1.1498 | N/A | 8.107 | 53.9527 | 430.2331 |

## Required Metals Valuation Bridge
- Build bull/base/bear cases from metal price, equity output, unit cost/AISC, FX, sustaining capex, and tax / minority interest.
- Include a price-sensitivity table: for each key metal, show the assumed realized price, output, unit cost/AISC, gross-profit effect, net-profit/EPS effect, and evidence status.
- Separate mining NAV from smelting, refining, processing, trading, and investment income. Do not assign scarce-resource multiples to pass-through volume.
- Use mine-by-mine or segment SOTP when material assets have different metals, grades, jurisdictions, ramp status, or cost curves.
- If mine-level reserves, grade, equity output, or AISC are missing, keep the rating at observation/medium conviction unless the upside is explicitly sized as scenario value.
- Treat domestic exchange futures as timely proxies. Overseas COMEX/LME/LBMA or licensed spot sources are cross-checks unless explicitly fetched and dated.
- Safety-price work must use cycle-trough metal prices, survivable balance sheet, maintenance capex, and historical/peer trough valuation floors.
- For nonferrous names, split the rating into Industry Cycle View, Company Expression View, Valuation/Odds View, and Tactical Attribution View before issuing the final action.
- A low PE / high PB setup must be tested as either peak-earnings trap or ROE re-rating; PB alone is not enough for Underweight when earnings, cash flow, and dividends are being released.
- One-quarter receivables, contract liabilities, inventory, or impairment direction must not decide the rating without seasonality, aging, peer comparison, and cash-conversion evidence.

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
- Write the public memo like a sell-side sector deep dive: cycle call first, then asset table, cost curve, segment SOTP/NAV, sensitivity, peer opportunity cost, and dated verification calendar.
- Price beta is not enough: connect exchange prices to realized selling price, volume, cost curve, inventory, hedging, capex, and balance-sheet survival.
- Missing reserve, grade, equity output, AISC, project-ramp, hedging, or NAV/SOTP evidence is neutral non-evidence and belongs in retrieval tasks; it must not mechanically alter the rating.
- If the final action is Underweight/Sell despite structural supply constraints, low PE, dividend support, or visible profit release, explicitly prove the profit-center downshift, cash-cycle deterioration, superior peer alternative, or over-pricing path.