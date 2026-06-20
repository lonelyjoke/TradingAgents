# Baijiu verification context for 605499.SH as of 2026-06-20

Status: triggered
- Company: 东鹏饮料
- Industry: 软饮料
- Trigger: company name / Tushare industry / filing text contains baijiu terms

## How This Layer Should Be Used
- This layer is only for baijiu/liquor targets. Do not apply its channel-price logic to unrelated consumer names.
- Treat wholesale price, channel inventory, and dealer payment evidence as thesis-critical. If they are missing, cap conviction instead of substituting generic PE or technical patterns.
- Contract liabilities must be read with seasonality: compare same-quarter YoY and multi-year seasonal baselines before calling a Q4-to-Q1 move demand deterioration.
- For Maotai specifically, separate Feitian loose-bottle, original-carton, retail price, wholesale/reference price, ex-factory price, and company guided price.

## Revenue and Profit Trend
| end_date | total_revenue | revenue | n_income_attr_p | n_income | total_revenue_yoy | revenue_yoy | n_income_attr_p_yoy | n_income_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 20875273117.52 | 20875273117.52 | 4415263147.79 | 4414018535.7 | 31.8 | 31.8 | 32.72 | 32.7 |
| 20241231 | 15838851828.27 | 15838851828.27 | 3326708852.44 | 3326429004.69 | N/A | N/A | N/A | N/A |

## Channel Payment and Inventory Signals
| end_date | contract_liab | adv_receipts | inventories | money_cap | accounts_receiv | contract_liab_qoq | adv_receipts_qoq | inventories_qoq | money_cap_qoq | accounts_receiv_qoq |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260331 | 4899929035.25 | N/A | 567851791.57 | 14954258943.81 | 103729764.46 | -17.98 | N/A | -13.56 | 163.28 | 14.07 |
| 20251231 | 5974383093.28 | N/A | 656962778.37 | 5680038991.67 | 90933632.77 | 67.68 | N/A | 19.05 | -0.7 | -10.01 |
| 20250930 | 3562994166.81 | N/A | 551850154.88 | 5719964050.09 | 101045584.93 | -2.84 | N/A | -18.64 | 8.7 | -6.6 |
| 20250630 | 3667087920.36 | N/A | 678321265.33 | 5262129442.18 | 108191306.25 | -5.23 | N/A | -20.76 | -5.37 | 66.72 |
| 20250331 | 3869618812.56 | N/A | 856068900.21 | 5560577226.54 | 64895475.3 | -18.71 | N/A | -19.85 | -1.63 | -20.19 |
| 20241231 | 4760551285.38 | N/A | 1068083706.94 | 5652549123.16 | 81308865.28 | 100.04 | N/A | 173.1 | -7.76 | -31.77 |
| 20240930 | 2379803925.7 | N/A | 391102553.7 | 6128366002.98 | 119166054.27 | -4.85 | N/A | -14.4 | -23.16 | 28.19 |
| 20240630 | 2501121924.56 | N/A | 456876302.19 | 7975257732.77 | 92960932.58 | N/A | N/A | N/A | N/A | N/A |

## Cash Conversion Quality
| end_date | n_cashflow_act | c_fr_sale_sg | n_income_attr_p | n_income | ocf_to_profit |
| --- | --- | --- | --- | --- | --- |
| 20260331 | 452489461.34 | 5599372908.24 | 1257422750.29 | 1256891210.69 | 0.36 |
| 20251231 | 6174239867.75 | 25122459877.7 | 4415263147.79 | 4414018535.7 | 1.4 |
| 20250930 | 3132633683.92 | 17857339119.03 | 3760923286.24 | 3759812719.14 | 0.83 |
| 20250630 | 1740460562.79 | 11072372353.01 | 2374750785.44 | 2374514563.8 | 0.73 |
| 20250331 | 631493112.47 | 4863482384.47 | 980009530.26 | 979955373.16 | 0.64 |
| 20241231 | 5789408508.54 | 20430143600.25 | 3326708852.44 | 3326429004.69 | 1.74 |

## Profitability and Balance-Sheet Quality
| end_date | roe | roe_waa | grossprofit_margin | netprofit_margin | netprofit_yoy | or_yoy | debt_to_assets |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20260331 | 8.4144 | 8.42 | 46.8897 | 21.3458 | 28.3072 | 21.4555 | 44.4817 |
| 20251231 | 51.6141 | 51.61 | 44.905 | 21.1447 | 32.7217 | 31.7979 | 64.7323 |
| 20250930 | 45.6247 | 43.35 | 45.1688 | 22.3214 | 38.9131 | 34.1264 | 63.2415 |
| 20250630 | 28.9191 | 28.18 | 45.1465 | 22.116 | 37.2219 | 36.3678 | 61.8635 |
| 20250331 | 11.9908 | 11.99 | 44.4688 | 20.2133 | 47.6184 | 39.2257 | 61.8114 |
| 20241231 | 47.4852 | 46.93 | 44.8094 | 21.0017 | 63.0921 | 40.6299 | 66.081 |

## Filing Evidence: Channel and Payments
| report | evidence |
| --- | --- |
| 东鹏饮料（集团）股份有限公司2026年第一季度报告 | 预收款项 |
| 东鹏饮料（集团）股份有限公司2026年第一季度报告 | 合同负债 4,899,929,035.25 5,974,383,093.28 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 渠道端，我们已实现全国地级市 100%覆盖，拥有 3400 余家经销商、450 余万家终端网点，构 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 至报告期末，公司拥有超过 3,400 家经销商，有效活跃终端网点突破 450 万家，实现广泛渗透与 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 至报告期末，公司拥有超过 3,400 家经销商，有效活跃终端网点突破 450 万家，实现广泛渗透与 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 端到端深度服务。销售人员以实地拜访、动销协作与培训指导为核心，持续赋能经销商库存优化、 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 营销数字化系统，实现对渠道库存、终端动销的实时监控与数据反馈，精准匹配营销资源与服务 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 公司加速推进智能化升级：面向经销商的移动化小程序整合订购与营销功能，提升下单效率； |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 合同负债 5,974,383,093.28 22.36 4,760,551,285.38 20.99 25.50 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 在成熟区域市场，公司推行精耕模式，通过专业团队与经销商紧密协作，强化终端陈列与网 |

## Filing Evidence: Product Mix and Direct Sales
| report | evidence |
| --- | --- |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 实施直营模式以进行精细化运营。 |

## Filing Evidence: Policy and Governance
| report | evidence |
| --- | --- |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 和行业经验，能够独立、客观地发表意见，在公司重大关联交易、董事及高级管理人员任免与薪 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 规范关联交易的承诺函，并严格遵守相关法律法规及公司内部管理制度。关联交易均遵循市场公 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 8、关于 2024 年度日常性关联交易确 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 认及 2025 年度日常性关联交易预计 |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 解决关联交易 备注六 备注六 备注六 备注六 / / |
| 东鹏饮料（集团）股份有限公司2025年年度报告 | 备注六：公司减少和规范关联交易的主要措施及承诺 |

## Required Peer Basket
| symbol | company |
| --- | --- |
| 600519.SH | 贵州茅台 |
| 000858.SZ | 五粮液 |
| 000568.SZ | 泸州老窖 |
| 600809.SH | 山西汾酒 |
| 002304.SZ | 洋河股份 |
| 000596.SZ | 古井贡酒 |
| 603369.SH | 今世缘 |
| 600779.SH | 水井坊 |
| 600702.SH | 舍得酒业 |
| 603198.SH | 迎驾贡酒 |
| 603589.SH | 口子窖 |
| 600559.SH | 老白干酒 |
| 000799.SZ | 酒鬼酒 |
| 600197.SH | 伊力特 |
| 000995.SZ | 皇台酒业 |

## Analyst Checklist
- Verify latest Feitian / core product wholesale prices from dated and reputable channel-price sources; if unavailable, state that price evidence is missing.
- Compare contract liabilities against prior Q1/Q2/Q3/Q4 observations, not just the previous quarter.
- Compare target against high-end and regional baijiu peers on growth, ROE, cash conversion, dividend/buyback yield, PE/PB, and channel health.
- Separate bull/bear cases into volume, price, mix, channel inventory, and valuation-multiple assumptions.
- If peer comparison or high-frequency price evidence fails, final rating should carry an explicit low-confidence tag.