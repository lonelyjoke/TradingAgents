# Dividend defensive verification context for 689009.SH as of 2026-06-22

Status: triggered
Defensive Dividend Rating: medium
- Company: 九号公司-WD
- Industry: 摩托车
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: watch
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 1.208 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 7 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.1137 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260622 | 34 | 16.5157 | 3.3581 | 1.208 | 2486222.8 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 12.514 | 1 |
| 20250630 | 12.6673 | 3 |
| 20241231 | 13.572 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.8505 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 21277876666.95 | 1758171535.84 | 4444116067.49 | 1221181361.89 | 1104050264.95 | 3222934705.6 | 0.628 |
| 20241231 | 14195808623.28 | 1084126917.88 | 3353676329.25 | 546380055.82 | 199875599.15 | 2807296273.43 | 0.1844 |
| 20231231 | 10222083359.99 | 597994833.29 | 2319465051.8 | 826695461.17 | N/A | 1492769590.63 | N/A |
| 20221231 | 10124318048.95 | 450553095.67 | 1589096254.56 | 433201319.27 | 653179.04 | 1155894935.29 | 0.0014 |
| 20211231 | 9146053585.08 | 410598753.65 | -161451665.8 | 266351997.62 | 3958412.35 | -427803663.42 | 0.0096 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603766.SH | 隆鑫通用 | 摩托车 | 2334877.1403 | 14.4825 | 2.4189 | 6.1566 | 4.9004 | 3.0494 | -7.0127 | 41.3414 | 73.7 |
| 603129.SH | 春风动力 | 摩托车 | 3553433.7856 | 21.1152 | 4.4395 | 1.8141 | 5.4518 | 2.398 | 1.8077 | 57.02 | 60.9 |
| 301345.SZ | 涛涛车业 | 摩托车 | 2336701.972 | 25.7796 | 6.1839 | 1.4 | 4.7654 | 3.7201 | 104.503 | 37.2157 | 58.6 |
| 601777.SH | 千里科技 | 摩托车 | 4118722.1911 | 365.3496 | 3.98 | N/A | 0.4688 | -0.1728 | 141.3118 | 38.1698 | 58.5 |
| 603787.SH | 新日股份 | 摩托车 | 223239.486 | 48.6867 | 1.4459 | 2.0619 | 1.6422 | 0.6403 | -15.8671 | 51.0352 | 52.7 |
| 000913.SZ | 钱江摩托 | 摩托车 | 575367.223 | 6.7569 | 1.0797 | 10.0656 | -0.7277 | -0.6748 | -144.8908 | 45.4967 | 51.5 |
| 603529.SH | 爱玛科技 | 摩托车 | 1742729.144 | 10.7185 | 1.7627 | 5.8408 | 1.9416 | 0.8211 | -67.5675 | 58.6022 | 49.9 |
| 001696.SZ | 宗申动力 | 摩托车 | 2751499.6407 | 45.0454 | 4.9506 | 0.8323 | 3.1351 | 1.7549 | -24.161 | 52.9722 | 41.1 |
| 689009.SH | 九号公司-WD | 摩托车 | 2486222.8 | 16.5157 | 3.3581 | 1.208 | 2.7927 | 1.0433 | -55.4184 | 63.6306 | 39.3 |
| 301322.SZ | 绿通科技 | 摩托车 | 818987.5219 | 631.8726 | 2.8921 | 0.0871 | -0.0993 | 0.0197 | -109.9363 | 23.4809 | 33.8 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 177164306.5104 | 11.1999 | 1.0906 | 4.8554 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600938.SH | 中国海油 | 石油开采 | 145156479.516 | 11.6439 | 1.734 | 4.1623 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 94952718.684 | 6.2988 | 0.8385 | 8.0027 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅台 | 白酒 | 155186379.9056 | 18.7616 | 5.7287 | 4.1674 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.5 |
| 601318.SH | 中国平安 | 保险 | 94123523.116 | 7.0885 | 0.9243 | 5.1943 | 2.479 | N/A | -7.3808 | 89.8779 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 90032841.7793 | 17.4594 | 1.8722 | 7.0292 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600028.SH | 中国石化 | 石油加工 | 57681470.2734 | 16.225 | 0.6923 | 4.1942 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 55.3 |
| 600941.SH | 中国移动 | 电信运营 | 199298860.2564 | 14.6753 | 1.4008 | 5.1166 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 601398.SH | 工商银行 | 银行 | 256612505.112 | 6.9103 | 0.6508 | 4.3097 | 2.0286 | N/A | 3.3093 | 92.1901 | 52.2 |
| 600900.SH | 长江电力 | 水力发电 | 65917378.4838 | 18.2682 | 2.8923 | 3.5004 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.