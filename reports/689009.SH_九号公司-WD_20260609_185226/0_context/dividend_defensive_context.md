# Dividend defensive verification context for 689009.SH as of 2026-06-09

Status: triggered
Defensive Dividend Rating: strong
- Company: 九号公司-WD
- Industry: 摩托车
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: pass
- Dividend trap risk: low

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 4.173 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 7 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.1137 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260609 | 36.08 | 17.5261 | 3.5585 | 4.173 | 2638323.0122 |

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
| 603766.SH | 隆鑫通用 | 摩托车 | 2583355.6473 | 16.0237 | 2.9948 | 5.5644 | 4.9004 | 3.0494 | -7.0127 | 41.3414 | 74.2 |
| 601777.SH | 千里科技 | 摩托车 | 4313129.4677 | 382.5944 | 4.1679 | N/A | 0.4688 | -0.1728 | 141.3118 | 38.1698 | 57 |
| 603129.SH | 春风动力 | 摩托车 | 3683586.312 | 21.8886 | 5.0052 | 1.75 | 5.4518 | 2.398 | 1.8077 | 57.02 | 56.6 |
| 301345.SZ | 涛涛车业 | 摩托车 | 2177709.9479 | 24.0255 | 6.0239 | 1.5023 | 4.7654 | 3.7201 | 104.503 | 37.2157 | 55.8 |
| 000913.SZ | 钱江摩托 | 摩托车 | 580631.333 | 6.8188 | 1.1582 | 9.9744 | -0.7277 | -0.6748 | -144.8908 | 45.4967 | 51.5 |
| 603529.SH | 爱玛科技 | 摩托车 | 1849479.9446 | 11.375 | 1.9645 | 5.5037 | 1.9416 | 0.8211 | -67.5675 | 58.6022 | 49.9 |
| 603787.SH | 新日股份 | 摩托车 | 226001.2018 | 49.289 | 1.486 | 2.0367 | 1.6422 | 0.6403 | -15.8671 | 51.0352 | 49.9 |
| 689009.SH | 九号公司-WD | 摩托车 | 2638323.0122 | 17.5261 | 3.5585 | 4.173 | 2.7927 | 1.0433 | -55.4184 | 63.6306 | 48.7 |
| 001696.SZ | 宗申动力 | 摩托车 | 2009522.2446 | 32.8983 | 3.6156 | 1.1396 | 3.1351 | 1.7549 | -24.161 | 52.9722 | 41.1 |
| 301322.SZ | 绿通科技 | 摩托车 | 790741.5318 | 610.08 | 2.7844 | 0.0902 | -0.0993 | 0.0197 | -109.9363 | 23.4809 | 35.3 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 166544958.7599 | 13.3596 | 1.9895 | 3.6278 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 601857.SH | 中国石油 | 石油开采 | 189243691.0638 | 11.9151 | 1.1649 | 4.5455 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.3 |
| 600036.SH | 招商银行 | 银行 | 97071185.7182 | 6.4393 | 0.8572 | 7.828 | 2.9627 | N/A | 1.518 | 90.4294 | 60.3 |
| 000333.SZ | 美的集团 | 家用电器 | 62704282.8381 | 14.1872 | 2.692 | 4.864 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 58.4 |
| 600519.SH | 贵州茅台 | 白酒 | 157010249.0856 | 18.9821 | 5.8609 | 4.119 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.5 |
| 600028.SH | 中国石化 | 石油加工 | 57923321.3123 | 16.293 | 0.6952 | 4.764 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.5 |
| 601088.SH | 中国神华 | 煤炭开采 | 106234849.221 | 20.6013 | 2.121 | 5.9572 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | 中国移动 | 电信运营 | 207818870.685 | 15.3026 | 1.5113 | 4.9068 | 2.084 | 1.759 | -4.2082 | 33.7319 | 55 |
| 601318.SH | 中国平安 | 保险 | 97654513.279 | 7.3544 | 0.959 | 4.7654 | 2.479 | N/A | -7.3808 | 89.8779 | 50.6 |
| 600900.SH | 长江电力 | 水力发电 | 67605685.5493 | 18.7361 | 2.9664 | 3.413 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.