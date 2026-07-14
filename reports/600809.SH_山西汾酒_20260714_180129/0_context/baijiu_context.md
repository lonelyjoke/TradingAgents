# Baijiu verification context for 600809.SH as of 2026-07-14

Status: triggered
- Company: 山西汾酒
- Industry: 白酒
- Trigger: curated A-share baijiu ticker list

## How This Layer Should Be Used
- This layer is only for baijiu/liquor targets. Do not apply its channel-price logic to unrelated consumer names.
- Treat wholesale price, channel inventory, and dealer payment evidence as thesis-critical. If unavailable, keep them as neutral retrieval tasks; do not substitute generic PE/technicals or mechanically alter the rating.
- Contract liabilities must be read with seasonality: compare same-quarter YoY and multi-year seasonal baselines before calling a Q4-to-Q1 move demand deterioration.
- For Maotai specifically, separate Feitian loose-bottle, original-carton, retail price, wholesale/reference price, ex-factory price, and company guided price.

## Revenue and Profit Trend
| end_date | total_revenue | revenue | n_income_attr_p | n_income | total_revenue_yoy | revenue_yoy | n_income_attr_p_yoy | n_income_yoy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 38718257657.74 | 38718257657.74 | 12246329337.25 | 12295255202.62 | 7.52 | 7.52 | 0.03 | 0.34 |
| 20241231 | 36010992321.46 | 36010992321.46 | 12242884323.77 | 12253094625.74 | N/A | N/A | N/A | N/A |

## Channel Payment and Inventory Signals
| end_date | contract_liab | adv_receipts | inventories | money_cap | accounts_receiv | contract_liab_qoq | adv_receipts_qoq | inventories_qoq | money_cap_qoq | accounts_receiv_qoq |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260331 | 7903656836.25 | N/A | 13650291620.48 | 12513587586.94 | 93685.45 | 12.8 | N/A | -5.15 | 28.12 | -3.23 |
| 20251231 | 7006704329.89 | N/A | 14391528589.51 | 9766895738.57 | 96807.5 | 21.21 | N/A | 10.67 | -13.62 | -94.32 |
| 20250930 | 5780613914.4 | N/A | 13003746739.19 | 11307089303.57 | 1704129.88 | -3.38 | N/A | -1.47 | -18.81 | 449.04 |
| 20250630 | 5982937738.11 | 261904.76 | 13197969349.12 | 13926550498.24 | 310383.85 | 2.83 | N/A | 5.78 | 93.91 | -16.69 |
| 20250331 | 5818303800.8 | N/A | 12476607813.71 | 7182016289.44 | 372558.44 | -32.91 | N/A | -5.98 | 14.28 | 394.92 |
| 20241231 | 8672424895.58 | N/A | 13270210934.11 | 6284730706.32 | 75276 | 58.23 | N/A | 14.93 | -42.49 | -75.72 |
| 20240930 | 5480852085.54 | N/A | 11546649680 | 10927261042.33 | 309983.58 | -4.38 | N/A | -0.48 | -18.51 | 71.85 |
| 20240630 | 5731869577.83 | N/A | 11602070576.19 | 13409312958.31 | 180378 | N/A | N/A | N/A | N/A | N/A |

## Cash Conversion Quality
| end_date | n_cashflow_act | c_fr_sale_sg | n_income_attr_p | n_income | ocf_to_profit |
| --- | --- | --- | --- | --- | --- |
| 20260331 | 8253609929.89 | 16021846385.76 | 5382557651 | 5404494317.94 | 1.53 |
| 20251231 | 9013519822.15 | 35456808289.34 | 12246329337.25 | 12295255202.62 | 0.74 |
| 20250930 | 8982107362.78 | 29074310214.96 | 11404509070.8 | 11450125486.02 | 0.79 |
| 20250630 | 5980102739.72 | 20731009110.7 | 8505077281.27 | 8523288032.84 | 0.7 |
| 20250331 | 7026539469.24 | 13790399130.74 | 6647582867.87 | 6655583906.21 | 1.06 |
| 20241231 | 12172323337.21 | 36609130569.36 | 12242884323.77 | 12253094625.74 | 0.99 |

## Profitability and Balance-Sheet Quality
| end_date | roe | roe_waa | grossprofit_margin | netprofit_margin | netprofit_yoy | or_yoy | debt_to_assets |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20260331 | 12.7163 | 12.57 | 75.0468 | 36.2153 | -19.0299 | -9.6801 | 29.2569 |
| 20251231 | 32.926 | 33.48 | 74.8525 | 31.7557 | 0.0281 | 7.5179 | 28.7429 |
| 20250930 | 31.0185 | 31.82 | 76.0997 | 34.777 | 0.4805 | 4.9966 | 27.9976 |
| 20250630 | 24.086 | 23.77 | 76.65 | 35.5671 | 1.1318 | 5.3536 | 35.8001 |
| 20250331 | 18.176 | 17.26 | 78.7981 | 40.2816 | 6.1503 | 7.7229 | 30.747 |
| 20241231 | 39.1204 | 39.68 | 76.2026 | 34.026 | 17.2902 | 12.7864 | 34.1913 |

## Filing Evidence: Channel and Payments
| report | evidence |
| --- | --- |
| 2026年第一季度报告 | 预收款项 |
| 2026年第一季度报告 | 合同负债 7,903,656,836.25 7,006,704,329.89 |
| 2025年年度报告 | 4.在销售产品环节，公司实行以厂方为主导、厂商共建的营销模式，地区级、县级经销商为 |
| 2025年年度报告 | 主要系本期销售回款及 |
| 2025年年度报告 | 公司实行以厂方为主导、厂商共建的营销模式，地区级、县级经销商为主体，辅以专卖店加 |
| 2025年年度报告 | (4).经销商情况 |
| 2025年年度报告 | 区域名称 产品种类 报告期末经销商数量 报告期内增加数量 报告期内减少数量 |
| 2025年年度报告 | 公司经销商数量按照报告期末签订并执行合同的经销商进行统计。 |
| 2025年年度报告 | 经销商管理情况 |
| 2025年年度报告 | 公司经销商实行分类管理，并根据公司的考核办法进行年度考核。 |

## Filing Evidence: Product Mix and Direct Sales
| report | evidence |
| --- | --- |
| 2025年年度报告 | 品牌矩阵根基稳固，青花 20、玻汾百亿级产品地位进一步夯实，杏花村酒深耕宴席渠道发力大众 |
| 2025年年度报告 | 青花汾酒、巴拿马汾酒、 |
| 2025年年度报告 | 察审计部部长、规划发展部部长、汾酒股份公司监事，汾酒集团副总会计师；汾酒股份公司总经理助理，山西杏花村汾酒厂系列酒公司党支 |
| 2025年年度报告 | 本公司主营汾酒、竹叶青酒、杏花村酒及系列酒的生产、销售，本公司将酒销售给客户，属 |
| 2025年年度报告 | 山西杏花村汾酒厂系列酒有限公司 |
| 2025年年度报告 | （以下简称“系列酒公司”） |
| 2025年年度报告 | 系列酒公司 50,000,000.00 50,000,000.00 |
| 2025年半年度报告 | 本公司主营汾酒、竹叶青酒、杏花村酒及系列酒的生产、销售，本公司将酒销售给客户，属 |
| 2025年半年度报告 | 山西杏花村汾酒厂系列酒有限公司（以下简称“系列酒公司”） 汾阳市杏花村 5,000.00 汾阳市杏花村 商业 100.00 设立 |
| 2025年半年度报告 | 系列酒公司 50,000,000.00 50,000,000.00 |

## Filing Evidence: Policy and Governance
| report | evidence |
| --- | --- |
| 2025年年度报告 | 十二、重大关联交易 |
| 2025年年度报告 | (一)与日常经营相关的关联交易 |
| 2025年年度报告 | 2025 年 4 月 30 日，公司就 2025 年度日常关联交易进行预计并公告，该事项已经第八届董事 |
| 2025年年度报告 | 会第七十一次会议审议通过。预计 2025 年发生的日常关联交易总额不超过 21,986 万元。报告期 |
| 2025年年度报告 | 内，公司与控股股东汾酒集团及其下属子公司发生日常关联交易金额合计 14,645.89 万元，详见财 |
| 2025年年度报告 | 务报表附注十四、5 关联交易情况。 |

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