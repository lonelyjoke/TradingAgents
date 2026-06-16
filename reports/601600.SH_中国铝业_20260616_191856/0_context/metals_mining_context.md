# Metals-mining verification context for 601600.SH as of 2026-06-16

- Status: triggered
- Company: 中国铝业
- Tushare industry: 铝
- Business model: integrated aluminum and alumina producer
- Metals covered: Aluminum
- Trigger reason: curated A-share metals / mining ticker list

## Company Watchlist
- aluminum supply ceiling, domestic-overseas price gap, and import/export arbitrage
- aluminum price, alumina cost, power cost, and smelting capacity utilization
- downstream demand bridge across property, grid/PV, EV lightweighting, exports, and general manufacturing
- alumina self-sufficiency, power-cost position, integrated-margin resilience, and inventory
- capex, leverage, dividend coverage, and cash-flow sensitivity to aluminum/alumina spreads

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11.7791 | 2.1421 | 2.5622 | N/A | 25.8276 | 56.3465 | 43.2655 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Aluminum | Tushare fut_daily -> SHFE AL contracts (AL.SHF) | LME aluminum | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Commodity Price Evidence Handoff
# Commodity and product price context for 601600.SH as of 2026-06-16

- Company/product map: Chalco
- Look-back window for futures proxies: 180 days
- Spread note: Use SHFE aluminum as the timely proxy; alumina, power cost, and capacity utilization drive spreads.

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
| Aluminum | main product | Tushare futures proxy | AL2607.SHF | 23830 | 20260616 | 7.61% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AL, selected by open interest/volume; curve=AL2607.SHF close=23830, oi=229636, vol=223624 | AL2608.SHF close=23895, oi=211792, vol=159295 | AL2609.SHF close=23940, oi=115950, vol=72205 | AL2610.SHF close=23980, oi=47391, vol=31755 | AL2611.SHF close=24000, oi=15856, vol=2791 | AL2612.SHF close=24005, oi=16996, vol=2573 |

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
| 中国铝业2026年第一季度报告 | ...控制且该控制并非暂时性，构成同一控制下企业 合并，故对上年同期数进行重述。 (二)非经常性损益项目和金额 √适用 □不适用 单位:千元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 34,656 / 计入当期损益的政府补助，但与公司正常经营业务密切相关、符 合国家政策规定、按照确定的标准享有、对公司损益产生持续影 67,786 / 响的政府补助除外 除同公司正常经营业务相关的有效套期保值业务外，非金融企业 持有金融资产和金融负债产生的公允价值变动损益以及处置金 -91,413 / 融资产和金融负债产生的损益 单独进行减值测试的应收款项减值准备转回 124,601 / 除上述各项之外的其他营业外收入和支出 38,697 / 减：所得税影响额 7,509 / 少数股东权益影响额（税后） -16,823 / 合计 165,013 / 对公司将《公开发行证券的公司信息披露解释性公告第 1 号——非经常性损益》未列举的项... |
| 中国铝业2025年年度报告（全文） | ...025年 末期股息，总计派息金额约25.22亿元（含税）。公司本次不实施资本公积金转增股本。 上述年度利润分配方案待本公司2025年年度股东会审议批准后方可实施。 截至报告期末，母公司存在未弥补亏损的相关情况及其对公司分红等事项的影响 □适用 √不适用 六、前瞻性陈述的风险声明 √适用 □不适用 本年度报告包括前瞻性陈述。除历史事实陈述外，所有本公司预计或期待未来可能或即将发生的 业务活动、事件或发展动态的陈述（包括但不限于预测、目标、储量及其他估计以及营业计划） 都属于前瞻性陈述，不构成本公司对投资者的实质承诺，请投资者注意投资风险。受诸多可变因 素影响，未来的实际结果或发展趋势可能会与这些前瞻性陈述出现重大差异。本报告中的前瞻性 陈述为本公司于2026年3月27日作出，除非监管机构另有要求外，本公司没有义务或责任对该等 前瞻性陈述进行更新。 2 / 285 中国铝业股份有限公司2025 年年度报告 七、是否存在被控股股东及其他关联方非经营性占用资金情况 否 八、是... |
| 中国铝业2025年第三季度报告 | ...用 □不适用 单位:千元 币种:人民币 年初至报告 非经常性损益项目 本期金额 说明 期末金额 非流动性资产处置损益，包括已计提资产减值准备的 39,591 75,245 / 冲销部分 计入当期损益的政府补助，但与公司正常经营业务密 切相关、符合国家政策规定、按照确定的标准享有、 20,914 129,801 / 对公司损益产生持续影响的政府补助除外 处置长期股权投资产生的投资收益 - -21,413 / 除同公司正常经营业务相关的有效套期保值业务外， 非金融企业持有金融资产和金融负债产生的公允价值 -30,937 72,722 / 变动损益以及处置金融资产和金融负债产生的损益 单独进行减值测试的应收款项减值准备转回 - 12,085 / 同一控制下企业合并产生的子公司期初至合并日的当 -2,395 -5,569 / 期净损益 除上述各项之外的其他营业外收入和支出 -6,306 29,143 / 减：所得税影响额 1,184 -103,675 / 少数股东权益影响额（... |
| 中国铝业2025年半年度报告全文 | ...表归属于上市公司 股东净利润的 30%。 本公司预计将于2025年10月17日或之前完成2025年中期股息的派发。在实施本次权益分派的股权 登记日前如公司总股本发生变动，本公司将维持每股分配比例不变，相应调整分配总金额，并将 另行公告具体调整情况。 六、 前瞻性陈述的风险声明 √适用 □不适用 本半年度报告包括前瞻性陈述。除历史事实陈述外，所有本公司预计或期待未来可能或即将发生 的业务活动、事件或发展动态的陈述（包括但不限于预测、目标、储量及其他估计以及营业计划） 都属于前瞻性陈述，不构成本公司对投资者的实质承诺，请投资者注意投资风险。受诸多可变因 素影响，未来的实际结果或发展趋势可能会与这些前瞻性陈述出现重大差异。本报告中的前瞻性 陈述为本公司于2025年8月27日作出，除非监管机构另有要求，本公司没有义务或责任对该等前 瞻性陈述进行更新。 七、 是否存在被控股股东及其他关联方非经营性占用资金情况 否 八、 是否存在违反规定决策程序对外提供担保的情况 否 2 / 2... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000612.SZ | 焦作万方 | 9.2575 | 1.7064 | N/A | 36.437 | 15.0299 | 216.4622 |
| 000807.SZ | 云铝股份 | 10.14 | 2.4688 | N/A | 31.5743 | 17.7381 | 269.4536 |
| 000933.SZ | 神火股份 | 10.0277 | 2.083 | N/A | 33.4845 | 40.8811 | 223.2834 |
| 600219.SH | 南山铝业 | 13.0325 | 1.0571 | N/A | 21.6381 | 18.4404 | -35.3868 |
| 600361.SH | 创新新材 | 18.6431 | 1.3814 | N/A | 3.8001 | 62.5706 | 28.6994 |
| 600595.SH | 中孚实业 | 11.5244 | 1.419 | N/A | 20.4768 | 29.8486 | 256.6124 |
| 600615.SH | 鑫源智造 | -163.0272 | 3.1393 | N/A | 9.4985 | 39.831 | -179.7773 |
| 600768.SH | 宁波富邦 | 25.7355 | 4.5822 | N/A | 24.8055 | 54.8492 | 450.4867 |

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
- Write the public memo like a sell-side sector deep dive: cycle call first, then asset table, cost curve, segment SOTP/NAV, sensitivity, peer opportunity cost, and dated verification calendar.
- Price beta is not enough: connect exchange prices to realized selling price, volume, cost curve, inventory, hedging, capex, and balance-sheet survival.
- Missing reserve, grade, equity output, AISC, project-ramp, hedging, or NAV/SOTP evidence caps conviction and belongs in research gaps.
- If the final action is Underweight/Sell despite structural supply constraints, low PE, dividend support, or visible profit release, explicitly prove the profit-center downshift, cash-cycle deterioration, superior peer alternative, or over-pricing path.