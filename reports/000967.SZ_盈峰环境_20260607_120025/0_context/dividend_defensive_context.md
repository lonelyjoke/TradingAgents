# Dividend defensive verification context for 000967.SZ as of 2026-06-07

Status: triggered
Defensive Dividend Rating: weak
- Company: 盈峰环境
- Industry: 环境保护
- Dividend stability: watch
- Dividend coverage: watch
- Industry durability: fail
- Valuation buffer: fail
- Dividend trap risk: high

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 1.7178 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 22 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.2 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 10.6 | 59.7227 | 1.9458 | 1.7178 | 3484316.8522 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.26 | 2 |
| 20250630 | 0 | 1 |
| 20241231 | 0.567 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.375 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 13843807632.45 | 549799271.94 | 962875753.97 | 996553827.63 | 772364549.83 | -33678073.66 | 1.4048 |
| 20241231 | 13117894323.95 | 513514275.54 | 1162049481.48 | 806085373.66 | 530172889.26 | 355964107.82 | 1.0324 |
| 20231231 | 12631050967.34 | 498383730 | 1385556509.49 | 1119006242.88 | 471087036.44 | 266550266.61 | 0.9452 |
| 20221231 | 12255992938.42 | 418794179.13 | 1662482287.71 | 1083515734.97 | 451503767.45 | 578966552.74 | 1.0781 |
| 20211231 | 11813537444.48 | 728467910.42 | 809218720.13 | 1734581869.14 | 491122899.6 | -925363149.01 | 0.6742 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600323.SH | 瀚蓝环境 | 环境保护 | 2438703.3137 | 11.4387 | 1.6038 | 3.5105 | 3.8837 | 1.8276 | 37.8281 | 68.9699 | 65.5 |
| 603568.SH | 伟明环保 | 环境保护 | 3076185.0114 | 15.8816 | 2.1517 | 3.3356 | 2.8897 | 1.8612 | -38.6266 | 42.9486 | 62.7 |
| 002266.SZ | 浙富控股 | 环境保护 | 2578320.0726 | 17.7908 | 2.0386 | 1.0015 | 4.8802 | 2.5261 | 122.404 | 54.0218 | 59.1 |
| 300140.SZ | 节能环境 | 环境保护 | 1809855.1373 | 19.8871 | 1.2764 | 2.0548 | 2.2589 | 1.5901 | 13.7991 | 50.6914 | 57.7 |
| 600388.SH | 龙净环保 | 环境保护 | 2129867.6334 | 18.1834 | 1.9834 | 2.2621 | 2.2 | 1.0668 | 31.8895 | 60.4237 | 54.4 |
| 603588.SH | 高能环境 | 环境保护 | 2065505.9237 | 16.9823 | 2.0456 | 0.7282 | 6.0592 | 3.3984 | 168.4032 | 60.5287 | 53.8 |
| 000967.SZ | 盈峰环境 | 环境保护 | 3484316.8522 | 59.7227 | 1.9458 | 1.7178 | 1.2397 | 0.8964 | 18.606 | 53.6099 | 51.9 |
| 301500.SZ | 飞南资源 | 环境保护 | 1443092.7437 | 20.9869 | 2.7816 | 0.3622 | 8.1406 | 3.16 | 7919.3671 | 61.5279 | 47.6 |
| 000711.SZ | ST京蓝 | 环境保护 | 1697930.2782 | N/A | 25.643 | N/A | 1.4923 | 0.8438 | 171.8097 | 50.3983 | 46 |
| 300779.SZ | 惠城环保 | 环境保护 | 1708986.4391 | 248.0336 | 5.5151 | 0.114 | 0.1159 | 0.3325 | 130.252 | 66.0034 | 21.3 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 167210378.1157 | 13.413 | 1.9975 | 3.6134 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63 |
| 600036.SH | 招商银行 | 银行 | 97298164.3287 | 6.4544 | 0.8592 | 7.8097 | 2.9627 | N/A | 1.518 | 90.4294 | 61.3 |
| 000333.SZ | 美的集团 | 家用电器 | 62192502.4029 | 14.0714 | 2.669 | 4.904 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.5 |
| 601857.SH | 中国石油 | 石油开采 | 194185257.4649 | 12.2262 | 1.1953 | 4.4298 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60 |
| 600519.SH | 贵州茅台 | 白酒 | 159117886.6649 | 19.2369 | 5.9396 | 4.0644 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 600028.SH | 中国石化 | 石油加工 | 59132576.4546 | 16.6332 | 0.7098 | 4.6665 | 2.0481 | 1.2478 | 28.2117 | N/A | 55.6 |
| 601088.SH | 中国神华 | 煤炭开采 | 105237135.243 | 20.4078 | 2.1011 | 6.0136 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.4 |
| 600941.SH | XD中国移 | 电信运营 | 211005744.6669 | 15.5373 | 1.5345 | 4.8327 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.2 |
| 600900.SH | 长江电力 | 水力发电 | 67556749.1139 | 18.7226 | 2.9643 | 3.4154 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.9 |
| 601318.SH | 中国平安 | 保险 | 96839669.3893 | 7.293 | 0.951 | 4.8055 | 2.479 | N/A | -7.3808 | 89.8779 | 50.4 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.