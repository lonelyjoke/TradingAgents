# Financial-report intelligence for 000426.SZ as of 2026-05-20

- Company: 兴业银锡
- Vendor industry: 铅锌
- Reading profile: metals_mining
- Research hygiene: industry-specific playbooks are conservative by design; if identity is ambiguous, generic questions are safer than a wrong template.
- Financial-report look-back: 900 days
- Extraction status: Financial-report text extraction succeeded.

## Financial Reports Considered
- 20260430: 2026年一季度报告
- 20260422: 2025年年度报告
- 20251202: 年报信息披露重大差错责任追究制度（2025年12月）
- 20251031: 2025年三季度报告

## Filing Reading Coverage Audit
| coverage_grade | report_types_seen | missing_report_types | answered_questions | core_pack_status | confidence_read |
| --- | --- | --- | --- | --- | --- |
| strong | annual/quarterly | semiannual | 9/9 | ready | Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. |

## Selected Filing Question Playbook
| question_id | category | question | preferred_reports |
| --- | --- | --- | --- |
| generic_revenue_quality | revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | quarterly/semiannual/annual |
| generic_profit_quality | profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | quarterly/semiannual/annual |
| generic_cash_conversion | cash_quality | 利润能否转成现金，还是被应收、存货、预付款拖住？ | quarterly/semiannual/annual |
| generic_capital_allocation | capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | semiannual/annual |
| generic_risk_disclosure | risk | 财报中新增或升级了哪些真正会改变股权价值的风险？ | semiannual/annual |
| metals_resource_volume | resource | 资源储量、品位、权益产量和达产节奏有没有继续兑现？ | semiannual/annual |
| metals_price_cost | pricing | 金属价格上行能否穿透到利润，还是被冶炼费、能源和单位成本吃掉？ | quarterly/semiannual/annual |
| metals_capex | capital_allocation | 扩产、并购和海外矿山投入是在低位锁资源，还是在高位资本开支？ | semiannual/annual |
| metals_inventory_hedging | risk | 库存、套保和汇率暴露会不会放大利润波动？ | quarterly/semiannual/annual |

## Business Model Map
| lens | report_type | filing_evidence | why_it_matters |
| --- | --- | --- | --- |
| core_revenue_engine | annual | 2025年年度报告: 年度总营业收入的 99.64%。影响采选板块经营业绩的主要因素包括主要产品产销量、市场 | Defines what actually drives the income statement. |
| segment_mix | annual | 2025年年度报告: 与分行业、分产品相关的对外交易收入情况如下： | Shows whether different profit pools are being mixed together. |
| customer_and_channel | annual | 2025年年度报告: 前五名客户合计销售金额（元） 5,121,804,108.53 | Reveals demand source, concentration, and market validation. |
| geography | annual | 2025年年度报告: 韩瑞霞，女，1984 年 10 月出生，博士学历。曾任中国进出口银行投资经理、MEC | Explains whether growth depends on a specific geography or expansion lane. |
| reinvestment_engine | annual | 2025年年度报告: 研发投入占营业收入比例 3.06% 3.27% -0.21% | Shows how today's cash is being converted into tomorrow's earnings power. |

## Growth Vector Map
| vector | stage | filing_evidence | valuation_treatment | verification_need |
| --- | --- | --- | --- | --- |
| overseas-expansion | monetized | 2025年年度报告: 源，进一步完善了锡矿国际化布局，也为公司长远发展储备了重要战略资源。 公司主要业绩来源于有色金属采选业务，报告期内，有色金属采选业务收入占 2025 年度总营业收入的 99.64%。影响采选板块经营业绩的主要因素包括主要产品产销量、市场 | eligible for valuation bridge review | check segment revenue, margin, and recurrence |
| ai-and-digital | capacity-building | 2025年年度报告: 造与碳足迹体系建设，向低能耗、低排放、高附加值的绿色制造模式加速迈进。 2. 数智化全面渗透 以 5G、人工智能、工业互联网、数字孪生为代表的新技术与采选冶全流程深度融合。 | scenario upside, not yet fully valuation-grade | check utilization, offtake, and commissioning timetable |
| overseas-expansion | planned | 2025年年度报告: 根据《矿产资源储量规模划分标准》（DZ/T 0400-2022）中锡矿大型矿山划分标准，大西 洋锡业拥有的 Achmmach 锡矿目前已相当于 5 个大型矿床。公司通过本次整合境外锡矿资 源，进一步完善了锡矿国际化布局，也为公司长远发展储备了重要战略资源。 | narrative or early optionality only | check customers, orders, capacity, and revenue evidence |
| new-product-platform | planned | 2025年年度报告: 新业务布局，2024 年 12 月 23 日，经总经理办公会审议，公司决定将自身持有的铜都矿业 | narrative or early optionality only | check customers, orders, capacity, and revenue evidence |
| new-product-platform | planned | 2025年年度报告: 新业务布局，2024 年 12 月 23 日，经总经理办公会审议，公司决定将自身持有的铜都矿业 49%股权和拥有的铜都矿业 3,409.80 万元债权，转让给赤峰市鸿升建筑工程有限责任公司 | narrative or early optionality only | check customers, orders, capacity, and revenue evidence |

## Deep Reading Excerpts
| report_type | section | excerpt | reading_purpose |
| --- | --- | --- | --- |
| quarterly | 主要会计数据和财务指标发生变动的情况及原因 | 2026年一季度报告: （三） 主要会计数据和财务指标发生变动的情况及原因 ☑适用 □不适用 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% 应收款项融资 注3 33,057,191.77 95,832,500.00 -65.51% 存货 注4 348,893,984.00 574,712,791.40 -39.29% 其他流动资产 注5 11,088,629.54 5,565,724.50 99.23% | Check short-cycle proof or disproof. |
| quarterly | 经营活动产生的现金流量净额 | 2026年一季度报告: 经营活动产生的现金流量净额（元） 1,216,893,859.45 1,198,191,035.20 1.56% 基本每股收益（元/股） 0.7533 0.2108 257.35% 稀释每股收益（元/股） 0.7533 0.2108 257.35% 加权平均净资产收益率 13.17% 4.63% 8.54% 本报告期末比上年 本报告期末 上年度末 度末增减（%） 总资产（元） 19,688,831,640.66 17,152,227,998.95 14.79% 归属于上市公司股东的所有者权益（元） 10,825,466,631.38 9,489,556,432.87 14.08% | Check cash conversion. |
| annual | 主营业务分析 | 2025年年度报告: 四、主营业务分析 1、概述 2025 年是公司“二三”规划（2024—2026 年）的深化之年，也是高质量发展的攻坚 之年。面对全球宏观经济复杂多变、大宗商品价格高位震荡、行业合规监管和绿色发展要 求持续提升的外部环境，公司董事会始终坚持“立足内蒙，专注资源主业；面向全球，布 局产业延伸”的战略目标，统筹推进战略落地及生产经营各项工作。紧抓银锡价格上行的 有利契机，以战略性并购整合关键资源，推动海外战略布局实现重要突破；同时聚焦主业 | Read segment mix, pricing, and profit pools. |
| annual | 核心竞争力分析 | 2025年年度报告: 三、核心竞争力分析 （一）区位优势 公司所在的内蒙古自治区地域辽阔，资源丰富，成矿条件优越，矿产资源储量居全国 之首，发现和已查明储量的矿种多，储量大，矿产地分布广且相对集中，公司注册地赤峰 市及重要矿产资源所在地锡林郭勒盟均拥有丰富的矿产资源储备，地勘市场旺盛，风险勘 查活跃。得天独厚的区位优势保障公司增储潜力，更有利于公司积极参与地区及行业资源 整合，凭借自身的规模优势和资本嫁接能力，通过招拍挂和合作开发等多种方式取得资源 勘探权和采矿权，增强持续盈利能力。 | Read moat claims and what protects economics. |
| annual | 公司未来发展的展望 | 2025年年度报告: 十一、公司未来发展的展望 （一）行业竞争格局和发展趋势 有色金属作为国民经济的基础性、战略性产业，是支撑科技进步、产业升级与国家安 全的关键物质基础。当前，全球经济复苏不均衡、地缘政治冲突持续及产业链重构加速， 国际矿产资源争夺日趋白热化。中国作为全球最大的有色金属生产与消费国，在保障国家 资源安全、稳定全球供应链中的地位愈发重要。报告期内，伴随“双碳”目标深化与新能 | Read strategy and second-curve ambitions. |
| annual | 未来发展展望 | 2025年年度报告: 公司已在本报告第三节“管理层讨论与分析”项下“公司未来发展展望” 中“公司面临的风险和应对措施”部分，对可能面临的风险进行描述，敬请 广大投资者留意查阅。 《中国证券报》《上海证券报》《证券时报》《证券日报》和巨潮资讯 网（www.cninfo.com.cn）为公司指定的信息披露媒体，本公司所有信息均以 | Read strategy and second-curve ambitions. |
| quarterly | 主要会计数据和财务指标发生变动的情况及原因 | 2025年三季度报告: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 单元：元 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 1,918,713,862.43 1,138,780,376.95 68.49% 应收账款 注2 178,241.67 4,456,440.71 -96.00% 预付款项 注3 16,134,145.67 5,247,587.23 207.46% 在建工程 注4 743,305,251.91 497,820,293.57 49.31% | Check short-cycle proof or disproof. |
| quarterly | 经营活动产生的现金流量净额 | 2025年三季度报告: 经营活动产生的现金流量净额 — — 2,741,992,001.13 118.66% （元） 基本每股收益（元/股） 0.3201 41.20% 0.7682 8.58% 稀释每股收益（元/股） 0.3201 41.20% 0.7682 8.58% 加权平均净资产收益率 6.30% 0.74% 15.88% -2.47% 本报告期末 上年度末 本报告期末比上年度末增减 总资产（元） 17,513,385,052.52 12,165,254,397.20 43.96% 归属于上市公司股东的所有者 9,158,367,964.93 7,900,537,526.26 15.92% | Check cash conversion. |

## Paragraph Reading Pack
| lens | report_type | section | reading_question | paragraph_excerpt | why_it_matters |
| --- | --- | --- | --- | --- | --- |
| business_model | annual | 主营业务分析 | What actually earns money today? | 2025年年度报告: 五、非主营业务分析 □适用 不适用 六、资产及负债状况分析 1、资产构成重大变动情况 单位：元 2025 年末 2025 年初 占总资 占总资 比重增减 重大变动说明 金额 金额 产比例 产比例 报告期公司收购宇邦 货币资金 1,293,473,077.33 7.54% 1,138,780,376.95 9.36% -1.82% 矿业 85%股权，总资 产增加所致。 报告期公司产品销售 | Separates the real profit engine from slogans and incidental businesses. |
| second_curve | annual | 主营业务分析 | What could become the next material earnings engine? | 2025年年度报告: 四、主营业务分析 1、概述 2025 年是公司“二三”规划（2024—2026 年）的深化之年，也是高质量发展的攻坚 之年。面对全球宏观经济复杂多变、大宗商品价格高位震荡、行业合规监管和绿色发展要 求持续提升的外部环境，公司董事会始终坚持“立足内蒙，专注资源主业；面向全球，布 局产业延伸”的战略目标，统筹推进战略落地及生产经营各项工作。紧抓银锡价格上行的 有利契机，以战略性并购整合关键资源，推动海外战略布局实现重要突破；同时聚焦主业 提质增效，严守安全生产底线，深化生产运营精细化管理，强化技术研发创新，健全风险 防控体系，持续提升公司治理水平，稳步推进产能落地，顺利完成年度各项经营指标，公 司经营质量稳步提升，发展韧性持续增强。 2025 年，公司实现营业收入 555,525.36 万元，较上年同期增长 30.09%；利润总额 209,623.70 万元，较上年同期增长 18.75%；归属上市公司股东净利润... | Identifies whether optionality is still a story or already has an economic bridge. |
| long_cycle_risk | annual | 风险管理 | What could permanently impair equity value? | 2025年年度报告: 金融工具有关的风险，以及本公司为降低这些风险所采取的风险管理政策如下所述。 （1）市场风险 本公司采用敏感性分析技术分析风险变量的合理、可能变化对当期损益或股东权益可能 产生的影响。由于任何风险变量很少孤立地发生变化，而变量之间存在的相关性对某一风险 变量的变化的最终影响金额将产生重大作用，因此下述内容是在假设每一变量的变化是在独 立的情况下进行的。 1）汇率风险 汇率风险是指影响本公司财务成果和现金流的外汇汇率的变动中的风险。本公司承受外 汇风险主要与所持有的外币货币资金、应收账款、其他应收款、应付账款和其他应付款有关， 由于外币资产和负债与本公司的功能货币之间的汇率变动使本公司面临外汇风险。但本公司 管理层认为，该等外币资产和负债于本公司总资产和总负债所占比例较小，此外本公司主要 经营活动均以人民币结算，故本公司所面临的外汇风险并不重大。 敏感性分析： 本公司承受外汇风险主要为美元、港币、澳元、摩洛哥迪... | Keeps long-cycle downside visible instead of overfitting to recent earnings. |
| short_cycle_execution | quarterly | 主要会计数据和财务指标发生变动的情况及原因 | Did the last quarter confirm or weaken the thesis? | 2026年一季度报告: （三） 主要会计数据和财务指标发生变动的情况及原因 ☑适用 □不适用 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% 应收款项融资 注3 33,057,191.77 95,832,500.00 -65.51% 存货 注4 348,893,984.00 574,712,791.40 -39.29% 其他流动资产 注5 11,088,629.54 5,565,724.50 99.23% 长期股权投资 注6 370,670,178.46 233,539,085.82 58.72% 递延所得税资产 注7 349,752,790.08 241,340,824.29 44.92% 交易性金融负债 注8 8,343,390.00 ... | Turns quarterly reports into proof tests rather than headline snapshots. |
| cash_conversion | quarterly | 主要会计数据和财务指标发生变动的情况及原因 | Did earnings turn into cash? | 2026年一季度报告: （三） 主要会计数据和财务指标发生变动的情况及原因 ☑适用 □不适用 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% 应收款项融资 注3 33,057,191.77 95,832,500.00 -65.51% 存货 注4 348,893,984.00 574,712,791.40 -39.29% 其他流动资产 注5 11,088,629.54 5,565,724.50 99.23% 长期股权投资 注6 370,670,178.46 233,539,085.82 58.72% 递延所得税资产 注7 349,752,790.08 241,340,824.29 44.92% 交易性金融负债 注8 8,343,390.00 ... | Catches revenue quality and working-capital stress early. |

## Industry Reading Pack
No filing-derived evidence snippets found.

## Statement Table Reading Pack
| account | report_type | table_evidence | why_it_matters | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- |
| operating_cash_flow | quarterly | 2026年一季度报告: 890,782,896.21 374,445,318.76 137.89% 的净利润（元） 经营活动产生的现金流量净额（元） 1,216,893,859.45 1,198,191,035.20 1.56% | Operating cash flow is the hard checkpoint for earnings quality. | Use improvement to validate operating leverage and conversion. | Use deterioration to challenge reported profit quality. |
| operating_cash_flow | quarterly | 2026年一季度报告: 的净利润（元） 经营活动产生的现金流量净额（元） 1,216,893,859.45 1,198,191,035.20 1.56% | Operating cash flow is the hard checkpoint for earnings quality. | Use improvement to validate operating leverage and conversion. | Use deterioration to challenge reported profit quality. |
| receivables | quarterly | 2026年一季度报告: 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% | Receivables decide whether reported growth becomes collectible cash. | Use stable receivables relative to sales as proof of healthy conversion. | Use receivable inflation to attack revenue quality and future impairment risk. |
| receivables | quarterly | 2026年一季度报告: 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% | Receivables decide whether reported growth becomes collectible cash. | Use stable receivables relative to sales as proof of healthy conversion. | Use receivable inflation to attack revenue quality and future impairment risk. |
| inventory | quarterly | 2026年一季度报告: 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% 应收款项融资 注3 33,057,191.77 95,832,500.00 -65.51% 存货 注4 348,893,984.00 574,712,791.40 -39.29% | Inventory reveals whether production is ahead of sell-through or preparing for demand. | Use controlled inventory with rising deliveries as evidence of healthy execution. | Use inventory build to test overproduction, price cuts, and future write-down risk. |
| inventory | quarterly | 2026年一季度报告: 应收款项融资 注3 33,057,191.77 95,832,500.00 -65.51% 存货 注4 348,893,984.00 574,712,791.40 -39.29% | Inventory reveals whether production is ahead of sell-through or preparing for demand. | Use controlled inventory with rising deliveries as evidence of healthy execution. | Use inventory build to test overproduction, price cuts, and future write-down risk. |
| long_term_equity_investments | quarterly | 2026年一季度报告: 存货 注4 348,893,984.00 574,712,791.40 -39.29% 其他流动资产 注5 11,088,629.54 5,565,724.50 99.23% 长期股权投资 注6 370,670,178.46 233,539,085.82 58.72% | Investment assets can matter for SOTP/NAV and reveal capital-allocation behavior. | Use named assets and realization history to support hidden value or skill. | Challenge valuation, liquidity, and whether optionality is too small to matter. |
| long_term_equity_investments | quarterly | 2026年一季度报告: 其他流动资产 注5 11,088,629.54 5,565,724.50 99.23% 长期股权投资 注6 370,670,178.46 233,539,085.82 58.72% | Investment assets can matter for SOTP/NAV and reveal capital-allocation behavior. | Use named assets and realization history to support hidden value or skill. | Challenge valuation, liquidity, and whether optionality is too small to matter. |
| impairment | quarterly | 2026年一季度报告: 注 19 8,343,390.00 100.00% 列） 信用减值损失（损失以“－”号填列） 注 20 -2,704,803.36 -513,358.60 -426.88% | Impairment lines expose the cost of prior weak underwriting or poor sell-through. | Use falling impairment only when it matches healthier assets. | Use rising impairment to attack asset quality and repeatability of profits. |
| impairment | quarterly | 2026年一季度报告: 列） 信用减值损失（损失以“－”号填列） 注 20 -2,704,803.36 -513,358.60 -426.88% | Impairment lines expose the cost of prior weak underwriting or poor sell-through. | Use falling impairment only when it matches healthier assets. | Use rising impairment to attack asset quality and repeatability of profits. |
| prepayments | quarterly | 2026年一季度报告: 应收账款 49,348,852.81 2,536,382.91 应收款项融资 33,057,191.77 95,832,500.00 预付款项 25,458,453.04 27,725,956.21 | Supplier prepayments show whether growth is consuming cash before delivery. | Use disciplined prepayments to support supply assurance for real orders. | Use sharp increases to challenge cash quality and supplier bargaining position. |
| prepayments | quarterly | 2026年一季度报告: 应收款项融资 33,057,191.77 95,832,500.00 预付款项 25,458,453.04 27,725,956.21 | Supplier prepayments show whether growth is consuming cash before delivery. | Use disciplined prepayments to support supply assurance for real orders. | Use sharp increases to challenge cash quality and supplier bargaining position. |
| construction_in_progress | quarterly | 2026年一季度报告: 投资性房地产 固定资产 4,519,707,909.36 4,607,116,816.48 在建工程 904,448,696.08 844,413,386.25 | Construction in progress turns strategy into capital already committed. | Use when capex is tied to visible demand or higher-return expansion. | Challenge utilization, payback period, and capex-before-demand risk. |
| construction_in_progress | quarterly | 2026年一季度报告: 固定资产 4,519,707,909.36 4,607,116,816.48 在建工程 904,448,696.08 844,413,386.25 | Construction in progress turns strategy into capital already committed. | Use when capex is tied to visible demand or higher-return expansion. | Challenge utilization, payback period, and capex-before-demand risk. |
| contract_liabilities | quarterly | 2026年一季度报告: 应付票据 32,500,000.00 32,500,000.00 应付账款 592,909,915.47 1,013,652,795.28 预收款项 | Prepayments from customers are a direct visibility and bargaining-power signal. | Use sustained growth as support for demand visibility if it later converts into revenue and cash. | Challenge whether higher advances reflect true pricing power or merely altered payment terms. |
| contract_liabilities | quarterly | 2026年一季度报告: 应付账款 592,909,915.47 1,013,652,795.28 预收款项 | Prepayments from customers are a direct visibility and bargaining-power signal. | Use sustained growth as support for demand visibility if it later converts into revenue and cash. | Challenge whether higher advances reflect true pricing power or merely altered payment terms. |

## Filing Note Reading Pack
| note_type | importance | note_evidence | why_it_matters | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- |
| impairment_policy | supporting | 2026年一季度报告: 单位：元 项目 本报告期金额 说明 非流动性资产处置损益（包括已计提资产减值准备的 报告期公司转让双源有色 60%股权， | Provisioning language explains whether accounting conservatism is strengthening or weakening. | Use conservative provisioning only when it lowers future surprise risk. | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| impairment_policy | supporting | 2026年一季度报告: 项目 本报告期金额 说明 非流动性资产处置损益（包括已计提资产减值准备的 报告期公司转让双源有色 60%股权， | Provisioning language explains whether accounting conservatism is strengthening or weakening. | Use conservative provisioning only when it lowers future surprise risk. | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| capitalized_development | supporting | 2026年一季度报告: 无形资产 8,321,456,610.05 8,365,889,503.22 其中：数据资源 开发支出 | Capitalized development can shift current profit at the cost of later amortization risk. | Use with commercialization evidence to support platform investment. | Challenge profit quality if capitalization rises ahead of monetization. |
| capitalized_development | supporting | 2026年一季度报告: 其中：数据资源 开发支出 | Capitalized development can shift current profit at the cost of later amortization risk. | Use with commercialization evidence to support platform investment. | Challenge profit quality if capitalization rises ahead of monetization. |
| customer_concentration | high | 2025年年度报告: （8） 主要销售客户和主要供应商情况 公司主要销售客户情况 前五名客户合计销售金额（元） 5,121,804,108.53 | Customer concentration changes the durability and bargaining power of revenue. | Use diversified customers or named blue-chip customers to support demand quality. | Challenge dependence, renewal risk, and negotiating leverage. |
| customer_concentration | high | 2025年年度报告: 公司主要销售客户情况 前五名客户合计销售金额（元） 5,121,804,108.53 | Customer concentration changes the durability and bargaining power of revenue. | Use diversified customers or named blue-chip customers to support demand quality. | Challenge dependence, renewal risk, and negotiating leverage. |
| related_party | high | 2025年年度报告: 成。 于收购赤峰宇邦 矿业有限公司 85% 股权暨关联交易 | Related-party disclosures are a governance and earnings-quality checkpoint. | Use low reliance on related parties as a governance positive. | Use heavy or opaque related-party flows to attack quality and independence. |
| related_party | high | 2025年年度报告: 矿业有限公司 85% 股权暨关联交易 | Related-party disclosures are a governance and earnings-quality checkpoint. | Use low reliance on related parties as a governance positive. | Use heavy or opaque related-party flows to attack quality and independence. |
| guarantees | high | 2025年年度报告: 董事会审议决策的重大事项，客观审慎地行使表决权，促进董事会决策的科学性和客观性。 同时，公司董事深入了解公司的生产经营、内部控制等情况，就报告期内公司发生的关联 交易、对外担保、股权收购、对外投资等重大事项，从各自专业角度提出了有价值的建议， | Guarantees can turn off-balance-sheet obligations into future downside. | Use limited guarantees to support balance-sheet resilience. | Use large or expanding guarantees to surface contingent risk. |
| guarantees | high | 2025年年度报告: 同时，公司董事深入了解公司的生产经营、内部控制等情况，就报告期内公司发生的关联 交易、对外担保、股权收购、对外投资等重大事项，从各自专业角度提出了有价值的建议， | Guarantees can turn off-balance-sheet obligations into future downside. | Use limited guarantees to support balance-sheet resilience. | Use large or expanding guarantees to surface contingent risk. |
| litigation | high | 2025年年度报告: 一、本单位/本人最近五年未受过与证券市场相关的 行政处罚、刑事处罚，没有涉及与经济纠纷有关的重 大民事诉讼或者仲裁；二、本单位/本人符合作为上 | Litigation and arbitration can change downside tails before they hit earnings. | Use resolved or immaterial cases only as risk relief. | Use unresolved material cases to attack tail-risk underpricing. |
| litigation | high | 2025年年度报告: 行政处罚、刑事处罚，没有涉及与经济纠纷有关的重 大民事诉讼或者仲裁；二、本单位/本人符合作为上 | Litigation and arbitration can change downside tails before they hit earnings. | Use resolved or immaterial cases only as risk relief. | Use unresolved material cases to attack tail-risk underpricing. |

## Financial Relationship Reading Pack
No filing-derived evidence snippets found.

## Filing Textual Signals
| signal_type | report_type | wording_stage | textual_evidence | investment_read | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| risk_language_upgrade | annual | risk-language | 2025年年度报告: 银元素回收研究 新型药剂研发：开发选择性高、环保型 统，银回收率提升 5%-8%，药剂成 用量及尾矿污染，降低环境污染风 增加将直接转化为额外利润； 的银捕收剂。智能化控制建设：引入在 本降低，尾矿污染风险有效减少 | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| risk_language_upgrade | annual | risk-language | 2025年年度报告: 用量及尾矿污染，降低环境污染风 增加将直接转化为额外利润； 的银捕收剂。智能化控制建设：引入在 本降低，尾矿污染风险有效减少 险，助力绿色矿山建设 3.填补锌精矿 同时药剂成本降低 15%-20%，将 | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| management_claim_with_evidence | annual | proof-backed | 2025年年度报告: 1、采购模式：公司及各所属企业在物资采购时均采用先做计划后采购的模式。采购 方式包括招标采购、询比价采购、竞争性谈判采购。公司及各所属企业针对采购计划的制 定、采购的实施、签订合同、物资到货验收与结算等各个环节均设定了严格的监督与审批 | Management language has a harder evidence bridge; debate materiality and economics rather than existence. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| management_claim_with_evidence | annual | proof-backed | 2025年年度报告: 方式包括招标采购、询比价采购、竞争性谈判采购。公司及各所属企业针对采购计划的制 定、采购的实施、签订合同、物资到货验收与结算等各个环节均设定了严格的监督与审批 14 | Management language has a harder evidence bridge; debate materiality and economics rather than existence. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| execution_progress_language | annual | execution-stage | 2025年年度报告: 数据来源于上海黄金交易所，其他金属价格数据均来源于上海有色网。 （二）行业政策及影响 1. 绿色转型深化落地，常态化监管压实合规经营底线 | The company is describing implementation progress; test whether execution reaches revenue, margin, or cash flow. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| execution_progress_language | annual | execution-stage | 2025年年度报告: （二）行业政策及影响 1. 绿色转型深化落地，常态化监管压实合规经营底线 | The company is describing implementation progress; test whether execution reaches revenue, margin, or cash flow. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| soft_strategy_language | annual | soft-intention | 2025年年度报告: 自动装药台车、喷浆台车等一批行业先进设备，大力推进“机械化换人、自动化减人”战 略，已取得阶段性成效。依托 5G 网络入井，持续完善安全监测与预警系统，提升矿山信 息化建设水平，不断拓展巡检机器人、井下智能回采作业面等智能化应用研究，稳步推进 | The company is still using intention/planning language; keep it below base-case valuation until proof appears. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| soft_strategy_language | annual | soft-intention | 2025年年度报告: 略，已取得阶段性成效。依托 5G 网络入井，持续完善安全监测与预警系统，提升矿山信 息化建设水平，不断拓展巡检机器人、井下智能回采作业面等智能化应用研究，稳步推进 | The company is still using intention/planning language; keep it below base-case valuation until proof appears. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| unquantified_strategy_language | annual | soft-intention | 2025年年度报告: （四）公司行业地位情况 公司主营业务为有色金属、贵金属及黑色金属采选，拥有三十多年的行业经验和得天 独厚的地域条件，储备了雄厚的矿产资源，生产能力及采选技术科技含量在同规模矿山企 | Strategic wording is not yet quantified; useful for questions, weak for valuation. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| unquantified_strategy_language | annual | soft-intention | 2025年年度报告: 公司主营业务为有色金属、贵金属及黑色金属采选，拥有三十多年的行业经验和得天 独厚的地域条件，储备了雄厚的矿产资源，生产能力及采选技术科技含量在同规模矿山企 | Strategic wording is not yet quantified; useful for questions, weak for valuation. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |

## Filing Insight Distillation Layer
| insight_type | analyst_question | distilled_read | evidence_basis | debate_use | what_would_change_mind |
| --- | --- | --- | --- | --- | --- |
| core_business_engine | What actually drives this company's revenue and profit pool? | Start the memo from the operating engine disclosed in filings, not from market labels, hot themes, or valuation screens. | 2025年年度报告: 年度总营业收入的 99.64%。影响采选板块经营业绩的主要因素包括主要产品产销量、市场 | Forces bulls and bears to debate the real business before discussing optionality. | A segment disclosure or order/customer evidence showing a different profit engine has become material. |
| second_curve_or_inflection_claim | Is there a credible second curve or operating inflection hidden in filings? | The filing contains a monetized growth vector; it deserves an earnings-bridge test, not just a narrative mention. | 2025年年度报告: 源，进一步完善了锡矿国际化布局，也为公司长远发展储备了重要战略资源。 公司主要业绩来源于有色金属采选业务，报告期内，有色金属采选业务收入占 2025 年度总营业收入的 99.64%。影响采选板块经营业绩的主要因素包括主要产品产销量、市场 | Bulls must quantify the bridge; bears must test scale, timing, margin, and whether it is already priced. | Segment revenue, margin, recurrence, and cash collection either confirm scale or reveal it is immaterial. |
| monetization_gap | What is the gap between the story and the income statement? | The filing has a growth narrative, but the system has not found enough clean financial confirmation to treat it as a base-case valuation driver. | 2025年年度报告: 源，进一步完善了锡矿国际化布局，也为公司长远发展储备了重要战略资源。 公司主要业绩来源于有色金属采选业务，报告期内，有色金属采选业务收入占 2025 年度总营业收入的 99.64%。影响采选板块经营业绩的主要因素包括主要产品产销量、市场 | Keeps the report from either ignoring the story or overpaying for it; use it as scenario evidence until economics are proven. | Quantified revenue/profit contribution, repeat orders, cash collection, and segment margin evidence. |
| capital_allocation_checkpoint | Is management turning reinvestment into future earnings power? | Investment assets can matter for SOTP/NAV and reveal capital-allocation behavior. | 2026年一季度报告: 存货 注4 348,893,984.00 574,712,791.40 -39.29% 其他流动资产 注5 11,088,629.54 5,565,724.50 99.23% 长期股权投资 注6 370,670,178.46 233,539,085.82 58.72% | Bulls must show reinvestment creates capacity, orders, or NAV; bears can attack trapped capital and weak ROIC. | Visible utilization, monetization, disposal gains, ROIC uplift, or impairment/disposal losses. |
| governance_or_tail_risk | Is there a footnote risk that changes the equity story? | Customer concentration changes the durability and bargaining power of revenue. | 2025年年度报告: （8） 主要销售客户和主要供应商情况 公司主要销售客户情况 前五名客户合计销售金额（元） 5,121,804,108.53 | Use as a thesis modifier: it can cap valuation even when operating momentum looks acceptable. | Resolution, quantified liability, customer diversification, related-party cleanup, or explicit non-materiality evidence. |
| textual_filing_signal | What is management language trying to prove, soften, or avoid? | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | 2025年年度报告: 银元素回收研究 新型药剂研发：开发选择性高、环保型 统，银回收率提升 5%-8%，药剂成 用量及尾矿污染，降低环境污染风 增加将直接转化为额外利润； 的银捕收剂。智能化控制建设：引入在 本降低，尾矿污染风险有效减少 | Use wording as a debate input: hard wording must still clear materiality; soft wording needs proof; risk wording can cap valuation. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| core_debate_item | Which filing-derived point must enter the bull/bear debate? | Is reinvestment translating into visible operating progress? | 2025年年度报告: 在建工程 844,413,386.25 4.92% 497,820,293.57 4.09% 0.83% 增加；另因银漫矿 || 2026年一季度报告: 价格较上年同期上涨；宇邦矿业产能逐步释放，矿产银产销量同比大幅增加；转让双源有色 60%股权实 | Do not leave this as background context; make it one of the main debate pillars. | Check whether the next report continues or reverses this bridge. |

## Core Discussion Promotion Queue
| topic | priority | evidence_basis | why_it_matters | valuation_treatment | verification_need |
| --- | --- | --- | --- | --- | --- |
| capital_intensity:confirmed | core | 2025年年度报告: 在建工程 844,413,386.25 4.92% 497,820,293.57 4.09% 0.83% 增加；另因银漫矿 || 2026年一季度报告: 价格较上年同期上涨；宇邦矿业产能逐步释放，矿产银产销量同比大幅增加；转让双源有色 60%股权实 | Is reinvestment translating into visible operating progress? | changes thesis confidence | Check whether the next report continues or reverses this bridge. |
| contract_liabilities | core | 2026年一季度报告: 应付票据 32,500,000.00 32,500,000.00 应付账款 592,909,915.47 1,013,652,795.28 预收款项 | Prepayments from customers are a direct visibility and bargaining-power signal. | core debate candidate | Challenge whether higher advances reflect true pricing power or merely altered payment terms. |
| customer_concentration | core | 2025年年度报告: （8） 主要销售客户和主要供应商情况 公司主要销售客户情况 前五名客户合计销售金额（元） 5,121,804,108.53 | Customer concentration changes the durability and bargaining power of revenue. | risk/governance modifier | Challenge dependence, renewal risk, and negotiating leverage. |
| generic_cash_conversion | core | 2026年一季度报告: 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% | Direct filing answer for cash_quality. | core debate candidate | Use deteriorating working capital to challenge profit quality. |
| generic_profit_quality | core | 2026年一季度报告: 营业收入（元） 2,129,869,142.28 1,149,284,450.85 85.32% 归属于上市公司股东的净利润（元） 1,337,672,163.55 374,357,743.86 257.32% 归属于上市公司股东的扣除非经常性损益 | Direct filing answer for profit_quality. | core debate candidate | Separate operating earnings from accounting or one-off noise. |
| generic_revenue_quality | core | 2026年一季度报告: 本报告期 上年同期 期增减（%） 营业收入（元） 2,129,869,142.28 1,149,284,450.85 85.32% | Direct filing answer for revenue_quality. | core debate candidate | Attack any divergence between reported growth and cash realization. |
| guarantees | core | 2025年年度报告: 董事会审议决策的重大事项，客观审慎地行使表决权，促进董事会决策的科学性和客观性。 同时，公司董事深入了解公司的生产经营、内部控制等情况，就报告期内公司发生的关联 交易、对外担保、股权收购、对外投资等重大事项，从各自专业角度提出了有价值的建议， | Guarantees can turn off-balance-sheet obligations into future downside. | risk/governance modifier | Use large or expanding guarantees to surface contingent risk. |
| impairment | core | 2026年一季度报告: 注 19 8,343,390.00 100.00% 列） 信用减值损失（损失以“－”号填列） 注 20 -2,704,803.36 -513,358.60 -426.88% | Impairment lines expose the cost of prior weak underwriting or poor sell-through. | core debate candidate | Use rising impairment to attack asset quality and repeatability of profits. |
| inventory | core | 2026年一季度报告: 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% 应收款项融资 注3 33,057,191.77 95,832,500.00 -65.51% 存货 注4 348,893,984.00 574,712,791.40 -39.29% | Inventory reveals whether production is ahead of sell-through or preparing for demand. | core debate candidate | Use inventory build to test overproduction, price cuts, and future write-down risk. |
| litigation | core | 2025年年度报告: 一、本单位/本人最近五年未受过与证券市场相关的 行政处罚、刑事处罚，没有涉及与经济纠纷有关的重 大民事诉讼或者仲裁；二、本单位/本人符合作为上 | Litigation and arbitration can change downside tails before they hit earnings. | risk/governance modifier | Use unresolved material cases to attack tail-risk underpricing. |

## Unanswered Filing Questions
No filing-derived evidence snippets found.

## Question-Driven Filing Answers
| question_id | report_type | question | evidence_strength | filing_answer | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| generic_revenue_quality | quarterly | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | quantified disclosure | 2026年一季度报告: 本报告期 上年同期 期增减（%） 营业收入（元） 2,129,869,142.28 1,149,284,450.85 85.32% | Use matching revenue, cash, and receivable evidence to support quality growth. | Attack any divergence between reported growth and cash realization. |
| generic_profit_quality | quarterly | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | quantified disclosure | 2026年一季度报告: 营业收入（元） 2,129,869,142.28 1,149,284,450.85 85.32% 归属于上市公司股东的净利润（元） 1,337,672,163.55 374,357,743.86 257.32% 归属于上市公司股东的扣除非经常性损益 | Support durable earnings when the improvement clearly comes from core operations. | Separate operating earnings from accounting or one-off noise. |
| generic_cash_conversion | quarterly | 利润能否转成现金，还是被应收、存货、预付款拖住？ | quantified disclosure | 2026年一季度报告: 资产负债表项目 注释 期末余额 期初余额 变动幅度 货币资金 注1 3,889,352,676.72 1,293,473,077.33 200.69% 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% | Use improving conversion to validate the thesis. | Use deteriorating working capital to challenge profit quality. |
| generic_capital_allocation | annual | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | quantified disclosure | 2025年年度报告: 财务费用 218,890,960.77 118,747,324.67 84.33% 利息支出增加所致。 报告期公司子公司研发投入 | Argue reinvestment is building future earnings power. | Question return on capital, empire building, or delayed payback. |
| generic_risk_disclosure | annual | 财报中新增或升级了哪些真正会改变股权价值的风险？ | quantified disclosure | 2025年年度报告: 非流动性资产处置损益（包括已计提 -8,119,923.27 -15,494,654.41 -31,186,012.83 资产减值准备的冲销部分） | Use risk relief only when disclosures become visibly safer. | Surface tail risks the market may be underweighting. |
| metals_resource_volume | annual | 资源储量、品位、权益产量和达产节奏有没有继续兑现？ | quantified disclosure | 2025年年度报告: 5 内蒙古兴业银锡矿业股份有限公司 2025 年年度报告全文 有） 主营业务由原热力供应变更为有色金属采选，并于 2011 年 12 月 20 日在内 | Support reserve life, volume growth, and long-cycle earnings visibility. | Challenge reserve quality, dilution, and whether volume growth is value-accretive. |
| metals_price_cost | annual | 金属价格上行能否穿透到利润，还是被冶炼费、能源和单位成本吃掉？ | quantified disclosure | 2025年年度报告: 内蒙古兴业银锡矿业股份有限公司 2025 年年度报告全文 5、2025 年铜行情 2025 年铜价整体呈“上半年冲高回落再反弹，下半年强势上涨”的走势。上半年受美 | Support operating leverage when realized prices rise faster than costs. | Attack commodity beta if cost inflation or TC/RC pressure offsets price upside. |
| metals_capex | annual | 扩产、并购和海外矿山投入是在低位锁资源，还是在高位资本开支？ | quantified disclosure | 2025年年度报告: 2025 年 1 月，自然资源部印发《国家级绿色矿山名录移出管理工作要求》，建立动态 考核与退出机制，将环保、安全、资源利用情况纳入长期监管。 2025 年 2 月，国家标准《绿色矿山评价通则》正式实施，统一规范矿山建设、生态修 | Support resource replacement and counter-cyclical expansion. | Question project returns, jurisdiction risk, and peak-cycle overinvestment. |
| metals_inventory_hedging | quarterly | 库存、套保和汇率暴露会不会放大利润波动？ | quantified disclosure | 2026年一季度报告: 相关、符合国家政策规定、按照确定的标准享有、对 392,666.66 公司损益产生持续影响的政府补助除外） 除同公司正常经营业务相关的有效套期保值业务外， | Show disciplined risk management and cleaner earnings conversion. | Surface hidden mark-to-market, inventory, and FX risks. |

## Material Filing Findings
No filing-derived evidence snippets found.

## Report-to-Report Bridge
| topic | long_cycle_evidence | checkpoint_evidence | bridge_status | bridge_read | analyst_read |
| --- | --- | --- | --- | --- | --- |
| orders_and_visibility | 2025年年度报告: 合同负债 332,443,027.96 1.94% 34,749,864.79 0.29% 1.65% | 2026年一季度报告: 合同负债 310,724,678.83 332,443,027.96 | checkpoint-available | confirmed | Does the short-cycle report confirm the demand visibility described in long-cycle filings? |
| pricing_and_margin | 2025年年度报告: （5） 营业成本构成 | 2026年一季度报告: 其中：营业成本 658,846,620.61 510,674,547.68 | checkpoint-available | checkpoint-present-but-indeterminate | Does the latest checkpoint validate or weaken the prior margin story? |
| cash_conversion | 2025年年度报告: 经营活动现金流入小计 6,451,774,777.23 4,873,061,285.63 32.40% | 2026年一季度报告: 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% | checkpoint-available | checkpoint-present-but-indeterminate | Do newer filings show profits turning into cash? |
| growth_vectors | 2025年年度报告: 新业务布局，2024 年 12 月 23 日，经总经理办公会审议，公司决定将自身持有的铜都矿业 |  | awaiting-short-cycle-check | awaiting-evidence | Are long-cycle growth vectors gaining real evidence over time? |
| capital_intensity | 2025年年度报告: 在建工程 844,413,386.25 4.92% 497,820,293.57 4.09% 0.83% 增加；另因银漫矿 | 2026年一季度报告: 价格较上年同期上涨；宇邦矿业产能逐步释放，矿产银产销量同比大幅增加；转让双源有色 60%股权实 | checkpoint-available | confirmed | Is reinvestment translating into visible operating progress? |

## Company-Specific Watch Questions
| question_id | question | times_seen | last_seen | last_report_type |
| --- | --- | --- | --- | --- |
| generic_revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | 2 | 2026-05-20 | quarterly |
| generic_profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | 2 | 2026-05-20 | quarterly |
| generic_cash_conversion | 利润能否转成现金，还是被应收、存货、预付款拖住？ | 2 | 2026-05-20 | quarterly |
| generic_capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | 2 | 2026-05-20 | annual |
| generic_risk_disclosure | 财报中新增或升级了哪些真正会改变股权价值的风险？ | 2 | 2026-05-20 | annual |
| metals_resource_volume | 资源储量、品位、权益产量和达产节奏有没有继续兑现？ | 1 | 2026-05-20 | annual |
| metals_price_cost | 金属价格上行能否穿透到利润，还是被冶炼费、能源和单位成本吃掉？ | 1 | 2026-05-20 | annual |
| metals_capex | 扩产、并购和海外矿山投入是在低位锁资源，还是在高位资本开支？ | 1 | 2026-05-20 | annual |

## Filing-Derived Operating Evidence
| category | signal | filing_evidence | bull_use | bear_use |
| --- | --- | --- | --- | --- |
| demand_visibility | 预收款项 | 2026年一季度报告: 预收款项 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| demand_visibility | 合同负债 | 2026年一季度报告: 合同负债 310,724,678.83 332,443,027.96 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| demand_visibility | 合同负债 | 2025年年度报告: 合同负债 332,443,027.96 1.94% 34,749,864.79 0.29% 1.65% | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| commercialization | 营业收入 | 2026年一季度报告: 营业收入（元） 2,129,869,142.28 1,149,284,450.85 85.32% | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| commercialization | 营业收入 | 2026年一季度报告: 营业收入 2,129,869,142.28 1,149,284,450.85 85.32% | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| commercialization | 销售收入 | 2026年一季度报告: 注 1：货币资金期末数较年初数增加 200.69%，主要原因：报告期公司产品销售收入增加及发行 2 | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| pricing_and_margin | 价格 | 2026年一季度报告: 受宏观经济环境及市场对产品需求变化等因素影响，报告期公司主营的银、锡等矿产品销售价格较上年 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| pricing_and_margin | 价格 | 2026年一季度报告: 价格较上年同期上涨；宇邦矿业产能逐步释放，矿产银产销量同比大幅增加；转让双源有色 60%股权实 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| pricing_and_margin | 成本 | 2026年一季度报告: 公司已于 2026 年 3 月 2 日与交易对手签署《股权转让协议》，2026 年 3 月 8 日完成本次股权转让 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| capacity_and_capex | 产能 | 2026年一季度报告: 同期上涨；宇邦矿业产能逐步释放，矿产银产销量同比大幅增加。 | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| capacity_and_capex | 产能 | 2026年一季度报告: 价格较上年同期上涨；宇邦矿业产能逐步释放，矿产银产销量同比大幅增加；转让双源有色 60%股权实 | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| capacity_and_capex | 产量 | 2026年一季度报告: 矿产品 2026 年 1-3 月产量 2026 年 1-3 月销量 | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| customer_and_geography | 境外 | 2026年一季度报告: 亿美元境外高级无抵押可持续发展债券所致。 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| customer_and_geography | 客户 | 2026年一季度报告: 注 2：应收账款期末数较年初数增加 1845.64%，主要原因：报告期公司产品销售客户赊销增加所致。 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| customer_and_geography | 境外 | 2026年一季度报告: 香港中央结算有限公司 境外法人 4.80% 85,240,595.00 0 不适用 0 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| innovation_and_product | 研发 | 2026年一季度报告: 研发费用 注 15 17,755,979.09 12,375,182.12 43.48% | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| innovation_and_product | 研发 | 2026年一季度报告: 注 15：研发费用本期数较上期数增加 43.48%，主要原因：报告期公司子公司研发投入同比增加所 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| innovation_and_product | 研发 | 2026年一季度报告: 研发费用 17,755,979.09 12,375,182.12 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| cash_and_working_capital | 减值准备 | 2026年一季度报告: 非流动性资产处置损益（包括已计提资产减值准备的 报告期公司转让双源有色 60%股权， | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| cash_and_working_capital | 应收账款 | 2026年一季度报告: 应收账款 注2 49,348,852.81 2,536,382.91 1845.64% | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| cash_and_working_capital | 存货 | 2026年一季度报告: 存货 注4 348,893,984.00 574,712,791.40 -39.29% | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| balance_sheet_and_risk | 资产减值 | 2026年一季度报告: 非流动性资产处置损益（包括已计提资产减值准备的 报告期公司转让双源有色 60%股权， | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |
| balance_sheet_and_risk | 担保 | 2026年一季度报告: 股东赵天时通过长城证券股份有限公司客户信用交易担保证券账户 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |
| balance_sheet_and_risk | 担保 | 2026年一季度报告: 公司客户信用交易担保证券账户持有公司股票 11,442,892 股。 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |

## Analyst Instructions
- Start with the filing reading coverage audit. If coverage is partial, weak, or failed, explicitly downgrade confidence before using any filing-derived thesis.
- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.
- Start with the business model map, then use the growth vector map to separate mature engines from emerging second curves.
- Use the deep-reading excerpts as source text, not decorative context: annual-report excerpts define the company, semiannual excerpts test trend formation, and quarterly excerpts test short-cycle execution.
- Use the paragraph reading pack for genuine report reading: answer the paragraph-level question first, then decide whether the business model, second curve, moat, trend, or cash-conversion thesis changed.
- Use the industry reading pack as the specialist layer: the same filing should be read through the value drivers that matter for that business model, then linked to the external inputs named in `connect_to` before forming a conclusion.
- Use the statement table reading pack for the hard-accounting layer: contract liabilities, receivables, inventory, prepayments, capex, investment assets, operating cash flow, and impairment rows often decide whether the narrative survives contact with the numbers.
- Use the filing note reading pack for footnote discipline: customer concentration, related parties, guarantees, litigation, impairment assumptions, and capitalization policies often reveal risks that the headline statements hide.
- Use the financial relationship reading pack to connect the statements rather than reading metrics in isolation. Revenue growth only deserves praise if margin, cash conversion, and balance-sheet demands make sense together.
- Use the filing textual signals layer to read management wording strength, risk-language upgrades, abnormal silence, and strategic promises. Hard wording still needs materiality; soft wording belongs in scenarios/watchlist; risk wording can cap valuation. Keep a concise textual-signal module in the manager report when it changes the thesis.
- Use the filing insight distillation layer before writing the final thesis. It converts raw filing snippets into buy-side questions: core engine, second curve, quality of growth, monetization gap, capital allocation, and tail risk. The manager report should read like a company memo, not a list of disconnected data points.
- Start from the selected question playbook, then answer only with evidence actually found in filings.
- Use the core discussion promotion queue as the bridge from reading to investing: core items should enter bull/bear debate, supporting items should reinforce or challenge a thesis, scenario items belong in upside/downside cases, and watch items stay out of base-case valuation until upgraded.
- Treat unanswered filing questions as explicit research gaps, not neutral evidence. If a thesis depends on an unanswered question, reduce conviction or state what disclosure would close the gap.
- Promote materially decision-relevant findings such as signed long-term agreements, named customers, take-or-pay/offtake signals, capacity-to-demand bridges, and commercialization milestones into the core debate rather than leaving them buried as generic snippets.
- Use the report-to-report bridge to ask whether annual/semiannual narratives are being confirmed, weakened, or still waiting for quarterly proof.
- Treat annual reports, half-year reports, and quarterly reports as a linked evidence chain: annual reports define the long-cycle thesis, half-year reports test trend formation, and quarterly reports confirm, weaken, or leave unresolved the latest checkpoint.
- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.
- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.
- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.