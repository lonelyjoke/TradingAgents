# Metals-mining verification context for 601168.SH as of 2026-06-16

- Status: triggered
- Company: 西部矿业
- Tushare industry: 铜
- Business model: metals / mining / smelting company
- Metals covered: Copper
- Trigger reason: commodity map contains exchange-traded metal products

## Company Watchlist
- resource / reserve quality, grade, and equity production
- unit cost, AISC, sustaining capex, and project ramp
- commodity price, FX, inventory, hedging, and impairment sensitivity
- mining / smelting / trading split, leverage, and NAV / SOTP bridge

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 17.7016 | 3.9499 | 0.3045 | N/A | 22.6008 | 96.3409 | 58.5159 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Copper | Tushare fut_daily -> SHFE CU contracts (CU.SHF) | COMEX HG futures; LME copper | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Commodity Price Evidence Handoff
# Commodity and product price context for 601168.SH as of 2026-06-16

- Company/product map: 西部矿业
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
| Copper | Tushare fut_daily -> SHFE CU contracts | CU.SHF | COMEX HG futures; LME copper | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Tin | Tushare fut_daily -> SHFE SN contracts | SN.SHF | LME tin | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lead | Tushare fut_daily -> SHFE PB contracts | PB.SHF | LME lead | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Zinc | Tushare fut_daily -> SHFE ZN contracts | ZN.SHF | LME zinc | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Copper | industry proxy | Tushare futures proxy | CU.SHF | 105590 | 20260615 | 14.03% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=CU, selected by open interest/volume; curve=CU2606.SHF close=105610, oi=5535, vol=2260 | CU2607.SHF close=105590, oi=148486, vol=84449 | CU2608.SHF close=105690, oi=135087, vol=56591 | CU2609.SHF close=105660, oi=90413, vol=21439 | CU2610.SHF close=105530, oi=32338, vol=5029 | CU2611.SHF close=105480, oi=16569, vol=2328 |
| Silver | industry proxy | Tushare futures proxy | AG.SHF | 16876 | 20260615 | 8.73% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2606.SHF close=16800, oi=4736, vol=688 | AG2607.SHF close=16847, oi=16774, vol=25623 | AG2608.SHF close=16876, oi=263068, vol=766795 | AG2609.SHF close=16898, oi=18742, vol=62603 | AG2610.SHF close=16908, oi=106685, vol=320396 | AG2611.SHF close=16918, oi=7631, vol=5795 |
| Tin | industry proxy | Tushare futures proxy | SN.SHF | 425560 | 20260615 | 27.27% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=SN, selected by open interest/volume; curve=SN2606.SHF close=425200, oi=4344, vol=130 | SN2607.SHF close=425560, oi=36090, vol=220734 | SN2608.SHF close=426500, oi=25720, vol=64669 | SN2609.SHF close=427230, oi=15546, vol=26617 | SN2610.SHF close=428060, oi=3588, vol=2836 | SN2611.SHF close=429220, oi=556, vol=543 |
| Lead | industry proxy | Tushare futures proxy | PB.SHF | 16240 | 20260615 | -3.22% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=PB, selected by open interest/volume; curve=PB2606.SHF close=16190, oi=4360, vol=140 | PB2607.SHF close=16240, oi=80967, vol=69945 | PB2608.SHF close=16280, oi=69261, vol=37655 | PB2609.SHF close=16330, oi=16646, vol=9117 | PB2610.SHF close=16355, oi=409, vol=69 | PB2611.SHF close=16405, oi=204, vol=41 |
| Zinc | industry proxy | Tushare futures proxy | ZN2608.SHF | 24875 | 20260615 | 8.08% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=ZN, selected by open interest/volume; curve=ZN2606.SHF close=24815, oi=6000, vol=110 | ZN2607.SHF close=24830, oi=68599, vol=118628 | ZN2608.SHF close=24875, oi=79180, vol=79145 | ZN2609.SHF close=24910, oi=24680, vol=19265 | ZN2610.SHF close=24930, oi=5915, vol=2743 | ZN2611.SHF close=24905, oi=3532, vol=442 |
| Lithium carbonate | industry proxy | Tushare futures proxy | LC.GFE | 174440 | 20260615 | 64.32% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=169400, oi=42156, vol=9939 | LC2608.GFE close=173500, oi=15559, vol=1679 | LC2609.GFE close=174440, oi=450397, vol=177039 | LC2610.GFE close=175180, oi=9355, vol=264 | LC2611.GFE close=175660, oi=30739, vol=4112 | LC2612.GFE close=177700, oi=13786, vol=936 |

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
| 西部矿业2025年年度报告 | ... 干实事 出实效 点检定修 预知维修 经济运行 保产提效 2025年年度报告 | ANNUAL REPORT 廉政理念 质量理念 敬廉崇俭 忠诚干净 遵纪守规 拒腐防变 应需定质 质量至上 全员监督 精益求精 经营理念 科技理念 守法诚信 稳定发展 问题导向 提质增效 创新引领 技术先行 成果转化 服务发展 3 报告摘要 公司基本情况 西部矿业股份有限公司是青海省属国有控股的大型有色金属矿业上市公司，主营铜、铅、锌、铁等多金属矿的采选、冶炼 与深加工，并布局盐湖提锂等新能源材料业务，形成“传统主业稳固、新兴业务增长”的全产业链格局。公司坐拥玉龙铜矿、 锡铁山铅锌矿等优质资源，资源储备与产能规模位居国内行业前列，是中国西部重要的资源开发与新材料供应龙头，经营 业绩与现金流表现稳健，持续以资源优势与技术创新推动高质量发展。 主要财务指标 公司 2025 年度实现营业收入 616.87 亿元，较上年同期增加 23%，实现利润总额 70.69 亿元，较上年同期增加 18%，实... |
| 西部矿业2025年第三季度报告 | ...5,781,638 对公司将《公开发行证券的公司信息披露解释性公告第 1 号——非经常性损益》未列举的项目认 定为非经常性损益项目且金额重大的，以及将《公开发行证券的公司信息披露解释性公告第 1 号 ——非经常性损益》中列举的非经常性损益项目界定为经常性损益的项目，应说明原因。 □适用 √不适用 （三） 主要会计数据、财务指标发生变动的情况、原因 √适用 □不适用 项目名称 变动比例（%） 主要原因 营业收入_本报告期 43.20 本期冶炼铜、冶炼铅、金锭产销量以及价格较上年同 营业收入_年初至报告期末 31.90 期增长。 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股 报告期末表决权恢复的优先股股 报告期末普通股股东总数 113,505 0 东总数（如有） 前 10 名股东持股情况（不含通过转融通出借股份） 持股比 持有有 质押、标记或冻结 股东名称 股东性质 持股数量 例(%) 限售条 情况 2 / 11 西部矿... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000630.SZ | 铜陵有色 | 39.136 | 2.7901 | N/A | 7.577 | 54.3423 | 19.1171 |
| 000737.SZ | 北方铜业 | 27.7273 | 3.8578 | N/A | 12.506 | 64.6004 | 65.7394 |
| 000878.SZ | 云南铜业 | 31.196 | 2.474 | N/A | 4.3974 | 65.4474 | 7.9318 |
| 600362.SH | 江西铜业 | 20.5113 | 1.9498 | N/A | 5.0699 | 62.4705 | 44.3105 |
| 600490.SH | 鹏欣资源 | 73.2746 | 2.625 | N/A | 24.4886 | 22.7948 | 2.3472 |
| 601168.SH | 西部矿业 | 17.7016 | 3.9499 | N/A | 22.6008 | 58.5159 | 96.3409 |
| 002171.SZ | 楚江新材 | 57.0658 | 2.5463 | N/A | 3.4958 | 59.5994 | 6.387 |
| 002203.SZ | 海亮股份 | 54.9306 | 3.3304 | N/A | 5.02 | 62.2225 | 26.4155 |

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