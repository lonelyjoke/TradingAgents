# Metals-mining verification context for 600338.SH as of 2026-06-16

- Status: triggered
- Company: 西藏珠峰
- Tushare industry: 铅锌
- Business model: metals / mining / smelting company
- Metals covered: Lead, Zinc
- Trigger reason: commodity map contains exchange-traded metal products

## Company Watchlist
- resource / reserve quality, grade, and equity production
- unit cost, AISC, sustaining capex, and project ramp
- commodity price, FX, inventory, hedging, and impairment sensitivity
- mining / smelting / trading split, leverage, and NAV / SOTP bridge

## Metals / Mining KPI Screen
| pe_ttm | pb | dv_ttm | roe_annual | grossprofit_margin | netprofit_yoy | debt_to_assets | ocf_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 29.7754 | 3.7301 | 0.2984 | N/A | 71.0622 | 42.7298 | 33.234 | N/A |

## Metal Price Source Chain Audit
| metal | domestic_chain | overseas_cross_check | analyst_rule |
| --- | --- | --- | --- |
| Lead | Tushare fut_daily -> SHFE PB contracts (PB.SHF) | LME lead | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Zinc | Tushare fut_daily -> SHFE ZN contracts (ZN.SHF) | LME zinc | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |

## Commodity Price Evidence Handoff
# Commodity and product price context for 600338.SH as of 2026-06-16

- Company/product map: 西藏珠峰
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
| Silver | Tushare fut_daily -> SHFE AG contracts | AG.SHF | COMEX SI futures; LBMA silver benchmark | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lead | Tushare fut_daily -> SHFE PB contracts | PB.SHF | LME lead | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Zinc | Tushare fut_daily -> SHFE ZN contracts | ZN.SHF | LME zinc | live domestic futures via Tushare; overseas sources are research cross-checks, not fetched by this module |
| Lithium carbonate | Tushare fut_daily -> GFEX LC contracts | LC.GFE | Fastmarkets / Benchmark / SMM lithium carbonate or hydroxide assessments | live GFEX futures via Tushare; global spot assessment sources require separate licensed data |

## Evidence Table
| product | role | data_type | latest_contract_or_source | latest_price | latest_date | change_over_window | inventory_or_receipt | evidence_status | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silver | industry proxy | Tushare futures proxy | AG2608.SHF | 16716 | 20260616 | 7.57% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=AG, selected by open interest/volume; curve=AG2607.SHF close=16678, oi=14906, vol=16195 | AG2608.SHF close=16716, oi=261018, vol=547167 | AG2609.SHF close=16730, oi=18298, vol=44298 | AG2610.SHF close=16746, oi=106139, vol=252347 | AG2611.SHF close=16749, oi=7600, vol=3545 | AG2612.SHF close=16765, oi=61717, vol=29490 |
| Lead | industry proxy | Tushare futures proxy | PB2607.SHF | 16310 | 20260616 | -3.61% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=PB, selected by open interest/volume; curve=PB2607.SHF close=16310, oi=72615, vol=58506 | PB2608.SHF close=16355, oi=69301, vol=30567 | PB2609.SHF close=16385, oi=17731, vol=7464 | PB2610.SHF close=16415, oi=397, vol=72 | PB2611.SHF close=16500, oi=169, vol=60 | PB2612.SHF close=16490, oi=86, vol=4 |
| Zinc | industry proxy | Tushare futures proxy | ZN2608.SHF | 24765 | 20260616 | 7.60% | N/A | Verified by Tushare futures daily data. | exchange=SHFE, query_exchange=SHF, prefix=ZN, selected by open interest/volume; curve=ZN2607.SHF close=24720, oi=60824, vol=73345 | ZN2608.SHF close=24765, oi=80630, vol=52678 | ZN2609.SHF close=24815, oi=27354, vol=14982 | ZN2610.SHF close=24840, oi=6478, vol=2252 | ZN2611.SHF close=24850, oi=3612, vol=228 | ZN2612.SHF close=24825, oi=1266, vol=70 |
| Lithium carbonate | industry proxy | Tushare futures proxy | LC2609.GFE | 169980 | 20260616 | 57.86% | N/A | Verified by Tushare futures daily data. | exchange=GFEX, query_exchange=GFE, prefix=LC, selected by open interest/volume; curve=LC2607.GFE close=165220, oi=37649, vol=10863 | LC2608.GFE close=169580, oi=15242, vol=3132 | LC2609.GFE close=169980, oi=449952, vol=187954 | LC2610.GFE close=170500, oi=9266, vol=312 | LC2611.GFE close=170900, oi=31534, vol=5730 | LC2612.GFE close=172640, oi=13309, vol=1823 |

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
Not an aluminum-focused profile; use the broader nonferrous cycle gate instead.

## Filing Text Evidence Snippets
| report | snippet |
| --- | --- |
| 2025年年度报告 | ...珠峰资源股份有限公司 塔城国际、控股股东 指 公司控股股东新疆塔城国际资源有限公司 海成资源 指 塔城国际的间接控股股东上海海成资源（集团）有限公司 塔国、塔吉克斯坦 指 塔吉克斯坦共和国 阿根廷 指 阿根廷共和国 塔中矿业 指 公司在塔国的全资子公司塔中矿业有限公司 珠峰国贸 指 公司全资子公司珠峰国际贸易（上海）有限公司 公司控股的（持股 87.5%）西藏珠峰资源（香港）有限公司 珠峰香港 指 （Tibet Summit Resources HongKong Limited） 西藏珠峰资源（新加坡）有限公司（TIBET SUMMIT RESOURCES 珠峰新加坡 指 SINGAPORE PTE. LTD.），为珠峰香港在新加坡控股子公司 NNEL Holding Corp.（未视新能控股有限公司），为珠峰香 NNELH 指 港的全资子公司 原 加 拿 大 创 业 板 公 司 锂 X 能 源 有 限 公 司 （ Lithium X LithiumX、LIX、锂 X... |
| 2026年第一季度报告 | ...属于上市公司股东的所 4,516,975,024.34 4,475,513,555.42 0.93 有者权益 (二)非经常性损益项目和金额 √适用 □不适用 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减 值准备的冲销部分 计入当期损益的政府补助，但与公司正常经 营业务密切相关、符合国家政策规定、按照 确定的标准享有、对公司损益产生持续影响 的政府补助除外 除同公司正常经营业务相关的有效套期保值 业务外，非金融企业持有金融资产和金融负 债产生的公允价值变动损益以及处置金融资 产和金融负债产生的损益 计入当期损益的对非金融企业收取的资金占 用费 委托他人投资或管理资产的损益 对外委托贷款取得的损益 因不可抗力因素，如遭受自然灾害而产生的 各项资产损失 单独进行减值测试的应收款项减值准备转回 企业取得子公司、联营企业及合营企业的投 资成本小于取得投资时应享有被投资单位可 辨认净资产公允价值产生的收益 同一控制下企业合并产生... |
| 2025年第三季度报告 | ...注：“本报告期”指本季度初至本季度末 3 个月期间，下同。 （二） 非经常性损益项目和金额 √适用 □不适用 单位:元 币种:人民币 年初至报告期末 非经常性损益项目 本期金额 说明 金额 非流动性资产处置损益，包括已计提 -22,264.12 资产减值准备的冲销部分 计入当期损益的政府补助，但与公司 正常经营业务密切相关、符合国家政 策规定、按照确定的标准享有、对公 司损益产生持续影响的政府补助除 外 除同公司正常经营业务相关的有效 套期保值业务外，非金融企业持有金 融资产和金融负债产生的公允价值 变动损益以及处置金融资产和金融 负债产生的损益 计入当期损益的对非金融企业收取 的资金占用费 委托他人投资或管理资产的损益 对外委托贷款取得的损益 因不可抗力因素，如遭受自然灾害而 产生的各项资产损失 单独进行减值测试的应收款项减值 准备转回 企业取得子公司、联营企业及合营企 业的投资成本小于取得投资时应享 有被投资单位可辨认净资产公允价 值产生的收益 2 / 13 西藏... |
| 2025年半年度报告 | ...珠峰资源股份有限公司 塔城国际、控股股东 指 公司控股股东新疆塔城国际资源有限公司 海成资源 指 塔城国际的间接控股股东上海海成资源（集团）有限公司 塔国、塔吉克斯坦 指 塔吉克斯坦共和国 阿根廷 指 阿根廷共和国 塔中矿业 指 公司在塔国的全资子公司塔中矿业有限公司 珠峰国贸 指 公司全资子公司珠峰国际贸易（上海）有限公司 珠峰香港 指 公司控股的（持股 87.5%）西藏珠峰资源（香港）有限公 司（Tibet Summit Resources HongKong Limited） NNELH 指 NNEL Holding Corp.（未视新能控股有限公司），珠峰香 港的全资子公司 LithiumX、LIX、锂 X 能源 指 原加拿大创业板公司锂 X 能源有限公司（Lithium X EnergyCorp.,)，现已私有化退市，为 NNELH 的全资子公 司 阿根廷锂钾 指 阿根廷锂钾有限公司（Potasio y Litio de Argentina S.A.，）， 为... |

## Metals / Mining Peer Screen
| ts_code | name | pe_ttm | pb | roe_annual | grossprofit_margin | debt_to_assets | netprofit_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000060.SZ | 中金岭南 | 34.5025 | 1.7832 | N/A | 5.3491 | 60.5537 | 84.4542 |
| 000426.SZ | 兴业银锡 | 26.6323 | 6.5626 | N/A | 69.0663 | 41.4046 | 257.3246 |
| 000603.SZ | 盛达资源 | 31.6763 | 5.3481 | N/A | 61.4209 | 47.3339 | 858.5263 |
| 000688.SZ | 国城矿业 | 72.0946 | 16.4969 | N/A | 49.9037 | 67.8369 | -52.4674 |
| 000751.SZ | 锌业股份 | 74.9524 | 2.2999 | N/A | 6.3904 | 66.5229 | 158.8138 |
| 000758.SZ | 中色股份 | 29.0146 | 2.2702 | N/A | 15.9562 | 59.91 | 4.9353 |
| 600338.SH | 西藏珠峰 | 29.7754 | 3.7301 | N/A | 71.0622 | 33.234 | 42.7298 |
| 600497.SH | 驰宏锌锗 | 42.1988 | 2.9526 | N/A | 20.883 | 27.879 | 33.8762 |

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