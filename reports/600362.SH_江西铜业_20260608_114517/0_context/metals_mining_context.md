# Metals-mining verification context for 600362.SH as of 2026-06-08

- Status: triggered
- Company: 江西铜业
- Tushare industry: 铜
- Business model: copper mining, smelting, and trading platform
- Metals covered: Copper
- Trigger reason: curated A-share metals / mining ticker list

## Company Watchlist
- mine output versus smelting / trading mix
- TC/RC, cathode copper spread, inventory, and working capital
- copper-price beta versus smelting-margin compression

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 19.2121 | 1.8263 | 2.4672 | N/A | 5.0699 | 44.3105 | 62.4705 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Copper | Tushare fut_daily -> SHFE CU contracts (CU.SHF) | COMEX HG futures; LME copper | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Commodity Price Evidence Handoff
# Commodity and product price context for 600362.SH as of 2026-06-08

- Company/product map: Jiangxi Copper
- Look-back window for futures proxies: 180 days
- Spread note: Use SHFE copper as the timely proxy; separate mining, smelting TC/RC, inventory, and trading exposure.

## Source Priority
| priority | source | use | limitation |
| --- | --- | --- | --- |
| 1 - company hard evidence | official filings, production reports, and sales announcements | realized product mix, output, unit cost, and cash-flow conversion | usually delayed and may not include daily spot prices |
| 2 - exchange market proxy | Tushare futures daily data for mapped SHFE/DCE/CZCE/GFEX/INE contracts | timely product-price direction, curve shape, and scenario stress | proxy, not the company's realized selling price or mine cost curve |

## Metal Price Source Audit
| metal | domestic_price_chain | contract_example | overseas_cross_check | coverage_status |
| --- | --- | --- | --- | --- |
| Copper | Tushare fut_daily -> SHFE CU contracts | CU.SHF | COMEX HG futures; LME copper | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | main product | Tushare futures proxy | CU.SHF | 105150 | 20260605 | 14.48% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2606.SHF close=105170, oi=30595, vol=17530 | CU2607.SHF close=105150, oi=173561, vol=110386 | CU2608.SHF close=105240, oi=122679, vol=44354 | CU2609.SHF close=105300, oi=80882, vol=17423 | CU2610.SHF close=105340, oi=25468, vol=3337 | CU2611.SHF close=105250, oi=14878, vol=2343 |

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
| 江西铜业股份有限公司2026年第一季度报告 | ...变更。 (二)非经常性损益项目和金额 √适用 □不适用 单位:元 币种:人民币 2 / 14 江西铜业股份有限公司2026 年第一季度报告 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减 1,245,877 值准备的冲销部分 计入当期损益的政府补助，但与公司正常经 营业务密切相关、符合国家政策规定、按照 67,552,782 确定的标准享有、对公司损益产生持续影响 的政府补助除外 除同公司正常经营业务相关的有效套期保值 业务外，非金融企业持有金融资产和金融负 -396,195,702 债产生的公允价值变动损益以及处置金融资 产和金融负债产生的损益 计入当期损益的对非金融企业收取的资金占 用费 委托他人投资或管理资产的损益 对外委托贷款取得的损益 因不可抗力因素，如遭受自然灾害而产生的 各项资产损失 单独进行减值测试的应收款项减值准备转回 22,729,883 企业取得子公司、联营企业及合营企业的投 资成本小于取得投资时应享有被投资单位可 辨认... |
| 江西铜业股份有限公司2025年年度报告 | ...签署的对年度报告的书面确认意见 董事会审议通过本次年度报告的决议 4 / 91 江西铜业股份有限公司 2025 年年度报告 第一节 释义 一、 释义 在本报告书中，除非文义另有所指，下列词语具有如下含义： 常用词语释义 中国证监会 指 中国证券监督管理委员会 上交所 指 上海证券交易所 本公司、公司、江铜 指 江西铜业股份有限公司 本集团 指 本公司及所属子公司 江铜集团 指 江西铜业集团有限公司及所属子公司，但不含本集团。 铜精矿是低品位的含铜原矿石经过选矿工艺处理达到一定质量指 铜精矿 指 标的精矿，可直接供冶炼厂炼铜。 江西铜业拥有的位于江西省内的五座在产矿山之一，位于江西省 永平铜矿 指 上饶市铅山县，也指江西铜业股份有限公司永平铜矿。 江西铜业拥有的位于江西省内的五座在产矿山之一，位于江西省 武山铜矿 指 九江市瑞昌市，也指江西铜业股份有限公司武山铜矿。 江西铜业拥有的位于江西省内的五座在产矿山之一，位于江西省 城门山铜矿 指 九江市，也指江西铜业股份有限公... |
| 江西铜业股份有限公司2025年第三季度报告 | ... 非经常性损益项目和金额 √适用 □不适用 单位：元 币种：人民币 非经常性损益项目 本期金额 年初至报告期末金额 说明 非流动性资产处置损益，包括已计提 4,145,472 -1,178,660 资产减值准备的冲销部分 计入当期损益的政府补助，但与公司 正常经营业务密切相关、符合国家政 策规定、按照确定的标准享有、对公 207,563,833 404,378,420 司损益产生持续影响的政府补助除 外 除同公司正常经营业务相关的有效 套期保值业务外，非金融企业持有金 融资产和金融负债产生的公允价值 -349,388,098 -858,208,669 变动损益以及处置金融资产和金融 负债产生的损益 计入当期损益的对非金融企业收取 的资金占用费 委托他人投资或管理资产的损益 对外委托贷款取得的损益 因不可抗力因素，如遭受自然灾害而 产生的各项资产损失 单独进行减值测试的应收款项减值 10,308,161 17,674,938 准备转回 企业取得子公司、联营企业及合营企 ... |
| 江西铜业股份有限公司2025年半年度报告 | ...告的决议 监事会以监事会决议的形式提出的对本次半年度报告的书面审核意见 3 / 50 江西铜业股份有限公司 2025 年半年度报告 第一节 释义 在本报告书中，除非文义另有所指，下列词语具有如下含义： 常用词语释义 中国证监会 指 中国证券监督管理委员会 上交所 指 上海证券交易所 本公司、公司、江铜 指 江西铜业股份有限公司 本集团 指 本公司及所属子公司 江铜集团 指 江西铜业集团有限公司及所属子公司，但不含本集团。 指 铜精矿是低品位的含铜原矿石经过选矿工艺处理达到 铜精矿 一定质量指标的精矿，可直接供冶炼厂炼铜。 指 江西铜业拥有的位于江西省内的五座在产矿山之一， 永平铜矿 位于江西省上饶市铅山县，也指江西铜业股份有限公 司永平铜矿。 指 江西铜业拥有的位于江西省内的五座在产矿山之一， 武山铜矿 位于江西省九江市瑞昌市，也指江西铜业股份有限公 司武山铜矿。 指 江西铜业拥有的位于江西省内的五座在产矿山之一， 城门山铜矿 位于江西省九江市，也指江西铜业股份有限公... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000630.SZ | 铜陵有色 | 33.1583 | 2.3216 | N/A | 7.577 | 54.3423 | 19.1171 |
| 000737.SZ | 北方铜业 | 25.518 | 3.5504 | N/A | 12.506 | 64.6004 | 65.7394 |
| 000878.SZ | 云南铜业 | 29.6387 | 2.3505 | N/A | 4.3974 | 65.4474 | 7.9318 |
| 600362.SH | 江西铜业 | 19.2121 | 1.8263 | N/A | 5.0699 | 62.4705 | 44.3105 |
| 600490.SH | 鹏欣资源 | 68.422 | 2.4512 | N/A | 24.4886 | 22.7948 | 2.3472 |
| 601168.SH | 西部矿业 | 16.4565 | 3.6458 | N/A | 22.6008 | 58.5159 | 96.3409 |
| 002171.SZ | 楚江新材 | 53.2532 | 2.3761 | N/A | 3.4958 | 59.5994 | 6.387 |
| 002203.SZ | 海亮股份 | 42.1895 | 2.5579 | N/A | 5.02 | 62.2225 | 26.4155 |

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