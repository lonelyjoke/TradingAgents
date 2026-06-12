# Metals-mining verification context for 300750.SZ as of 2026-06-11

- Status: triggered
- Company: 宁德时代
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
| 22.3902 | 4.9114 | 2.0688 | N/A | 24.8156 | 48.5237 | 62.3223 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts (LC.GFE) | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Commodity Price Evidence Handoff
# Commodity and product price context for 300750.SZ as of 2026-06-11

- Company/product map: CATL
- Look-back window for futures proxies: 180 days
- Spread note: For battery makers, lithium carbonate is a cost proxy rather than a direct revenue product.

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
| Lithium carbonate | raw material proxy | Tushare futures proxy | LC.GFE | 174600 | 20260611 | 72.77% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2606.GFE close=169000, oi=360, vol=314 | LC2607.GFE close=170300, oi=48594, vol=18166 | LC2608.GFE close=173700, oi=14493, vol=2686 | LC2609.GFE close=174600, oi=448867, vol=244951 | LC2610.GFE close=175060, oi=9398, vol=334 | LC2611.GFE close=175900, oi=29420, vol=9207 |

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
| 2026年一季度报告 | ...末增减 总资产（千元） 1,046,329,036 974,827,544 7.33% 归属于上市公司股东的所有 357,262,588 337,107,747 5.98% 者权益（千元） 1 宁德时代新能源科技股份有限公司 2026 年第一季度报告 （二） 非经常性损益项目和金额 适用 □不适用 单位：千元 项目 本报告期金额 说明 非流动性资产处置损益（包括已计提资产减值准备的冲销部分） 3,211 除同公司正常经营业务相关的有效套期保值业务外，非金融企业 持有金融资产和金融负债产生的公允价值变动损益以及处置金融 344,447 资产和金融负债产生的损益 单独进行减值测试的应收款项减值准备转回 1,206 除上述各项之外的其他营业外收入和支出 30,312 其他符合非经常性损益定义的损益项目 3,209,441 减：所得税影响额 693,833 少数股东权益影响额（税后） 249,711 合计 2,645,072 -- 其他符合非经常性损益定义的损益项目的具体情... |
| 2025年年度报告 | ...叠加的历史进程中，宁德时代始终在以行动回答一个问题：如何在不确定的世界中，构建确定性的 长期价值？ 这一年，我们的收入结构与增长质量持续优化，动力、储能电池出货量继续领跑全球，锂电池销量 同比增长近 4 成至 661GWh，“全域增量”业务引擎初具规模。 这一年，我们的港股 IPO 树立了全球资本市场标杆项目，为公司海外战略布局提供稳健的资本支 持，也与全球投资者共享了公司的成长。 这一年，我们的产品和服务走向更广阔的场景——在云端、在矿山、在江河湖海、在戈壁沙漠、在 零碳园区、在算力中心，宁德时代正在为中国及全球的发展持续注入澎湃动能。 我们清醒地看到，当地缘政治、产业周期与技术变革交织，不确定性成为全球经济常态，宁德时代 能够稳健增长，是建立在公司长期坚守的奋斗与创新价值观基石之上，让我们相较于同业，更经得起风 浪的洗礼。 “全域增量”，迈向零碳时代 新能源产业正站在新的历史节点：发展目标从“速度”转向“质量”，发展路径从新能源的产业化迈 向产业的新能源化。国际能... |
| 2025年三季度报告 | ...季度报告披露日股本是否因发行新股、增发、配股、股权激励行权、回购等原因发生变化且影响所有者权 益金额 是 □否 本报告期 年初至报告期末 用最新股本计算的全面摊薄每股收益 4.07 10.75 （元/股） （二）非经常性损益项目和金额 适用 □不适用 单位：千元 项目 本报告期金额 年初至报告期期末金额 说明 非流动性资产处置损益（包括已计 326,465 390,931 提资产减值准备的冲销部分） 除同公司正常经营业务相关的有效 套期保值业务外，非金融企业持有 金融资产和金融负债产生的公允价 895,655 1,187,624 值变动损益以及处置金融资产和金 融负债产生的损益 单独进行减值测试的应收款项减值 62 4,548 准备转回 除上述各项之外的其他营业外收入 168,109 160,089 和支出 其他符合非经常性损益定义的损益 1,557,156 5,963,843 项目 减：所得税影响额 552,966 1,501,055 少数股东权益影响额（税后）... |
| H股公告（2025年中期报告） | .... . . . . . . . 48 釋義 釋義項 指 釋義內容 本公司、公司、寧德時代 指 寧德時代新能源科技股份有限公司 本集團 指 寧德時代新能源科技股份有限公司及其附屬公司 中國證監會 指 中國證券監督管理委員會 深交所 指 深圳證券交易所 香港聯交所 指 香港聯合交易所有限公司 淨零倡議組織 指 一個全球性數據庫和分析工具，用於監測各國、地區、城市和大型企業的淨 Net Zero Tracker 零排放承諾 SNE Research 指 韓國新能源領域諮詢公司，提供電池行業全球市場研究和諮詢服務 Rho Motion 指 英國新能源領域市場研究公司，提供新能源汽車與電池、儲能、新能源車充 電基礎設施、電池回收等行業市場研究和諮詢服務 動力電池系統 指 動力電池裡的電芯、模組、電箱、電池包 儲能電池系統 指 儲能電池裡的電芯、模組、電箱、電池櫃 GWh 指 吉瓦時，一種電能單位，1吉瓦時=10億瓦時 MWh 指 兆瓦時，一種電能單位，1兆瓦時=1百萬瓦時 TW... |
| 2025年半年度报告 | .../www.szse.cn）。 4 宁德时代新能源科技股份有限公司 2025 年半年度报告全文 释义 释义项 指 释义内容 本公司、公司、宁德时代 指 宁德时代新能源科技股份有限公司 中国证监会 指 中国证券监督管理委员会 深交所 指 深圳证券交易所 香港联交所 指 香港联合交易所有限公司 一个全球性数据库和分析工具，用于监测各国、地区、城市和大型企业的净零排 净零倡议组织 Net Zero Tracker 指 放承诺 SNE Research 指 韩国新能源领域咨询公司，提供电池行业全球市场研究和咨询服务 英国新能源领域市场研究公司，提供新能源汽车与电池、储能、新能源车充电基 Rho Motion 指 础设施、电池回收等行业市场研究和咨询服务 动力电池系统 指 动力电池里的电芯、模组、电箱、电池包 储能电池系统 指 储能电池里的电芯、模组、电箱、电池柜 GWh 指 吉瓦时，一种电能单位， 1 吉瓦时=10 亿瓦时 MWh 指 兆瓦时，一种电能单位， 1 兆瓦时=1 百... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000009.SZ | 中国宝安 | 340.2457 | 1.7614 | N/A | 25.0018 | 60.1965 | -89.6412 |
| 000049.SZ | 德赛电池 | 26.6432 | 1.2843 | N/A | 9.8695 | 58.632 | 64.2285 |
| 000400.SZ | 许继电气 | 20.5594 | 1.7936 | N/A | 19.0118 | 47.5928 | -46.5044 |
| 000533.SZ | 顺钠股份 | 73.2119 | 7.379 | N/A | 19.1201 | 63.2533 | -13.2792 |
| 000576.SZ | 甘化科工 | 43.7649 | 1.8654 | N/A | 29.4864 | 28.3504 | -73.476 |
| 000682.SZ | 东方电子 | 15.4581 | 2.5803 | N/A | 30.4499 | 52.8068 | 95.0553 |
| 000720.SZ | 新能泰山 | N/A | 2.8188 | N/A | 0.3364 | 61.0342 | -237.1974 |
| 000809.SZ | 和展能源 | N/A | 1.2074 | N/A | 17.153 | 34.5879 | 122.862 |

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