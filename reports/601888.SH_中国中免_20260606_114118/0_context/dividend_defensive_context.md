# Dividend defensive verification context for 601888.SH as of 2026-06-06

Status: triggered
Defensive Dividend Rating: weak
- Company: 中国中免
- Industry: 旅游服务
- Dividend stability: fail
- Dividend coverage: watch
- Industry durability: fail
- Valuation buffer: watch
- Dividend trap risk: high

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 2.2727 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3592 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 57.2 | 29.7376 | 2.0507 | 2.2727 | 11884996.8037 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.45 | 1 |
| 20250930 | 0.75 | 3 |
| 20250630 | 0 | 1 |
| 20241231 | 3.15 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 4.95 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 53693579201.52 | 3586177592.36 | 6058560224.26 | 1273061670.55 | 3100916807.35 | 4785498553.71 | 0.8647 |
| 20241231 | 56473848287.07 | 4267111672.66 | 7939327277.01 | 1118981469.64 | 3556287787.81 | 6820345807.37 | 0.8334 |
| 20231231 | 67540104550.94 | 6713686688.57 | 15126419298.22 | 1801600787.99 | 2524860421.48 | 13324818510.23 | 0.3761 |
| 20221231 | 54432851387.25 | 5030381552.61 | -3415245341.32 | 2995380376.95 | 3676147989.42 | -6410625718.27 | 0.7308 |
| 20211231 | 67675515093.08 | 9653739902.26 | 8328824733 | 2154846659.59 | 3430862498.22 | 6173978073.41 | 0.3554 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601888.SH | 中国中免 | 旅游服务 | 11884996.8037 | 29.7376 | 2.0507 | 2.2727 | 4.1407 | 3.31 | 21.1803 | 25.544 | 83.5 |
| 002159.SZ | 三特索道 | 旅游服务 | 256377.716 | 19.1532 | 1.732 | 1.7289 | 1.4058 | 1.974 | -31.4586 | 18.6181 | 62.4 |
| 600185.SH | 珠免集团 | 旅游服务 | 978318.0076 | N/A | 113.3172 | N/A | 40.6617 | 2.2134 | 142.9063 | 82.1329 | 56.2 |
| 000524.SZ | 岭南控股 | 旅游服务 | 614581.2834 | 80.5017 | 2.6568 | 0.8724 | 1.4288 | 1.0111 | 23.6348 | 38.9852 | 54.1 |
| 000796.SZ | 凯撒旅业 | 旅游服务 | 728120.1679 | 206.0005 | 8.0161 | N/A | 0.3103 | 0.5451 | 161.7095 | 45.5167 | 48.5 |
| 000610.SZ | *ST西旅 | 旅游服务 | 175666.9425 | N/A | N/A | N/A | N/A | -1.2233 | 17.5845 | 106.6196 | 38.8 |
| 300859.SZ | 西域旅游 | 旅游服务 | 461900 | 59.5253 | 6.5184 | 1.0067 | -3.4743 | -2.5122 | 9.8467 | 26.5226 | 38.4 |
| 002707.SZ | 众信旅游 | 旅游服务 | 543441.4132 | N/A | 6.0365 | N/A | 1.1036 | 0.8225 | -47.8193 | 71.3749 | 38.1 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 167210378.1157 | 13.413 | 1.9975 | 3.6134 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 600036.SH | 招商银行 | 银行 | 97298164.3287 | 6.4544 | 0.8592 | 7.8097 | 2.9627 | N/A | 1.518 | 90.4294 | 60.9 |
| 601857.SH | 中国石油 | 石油开采 | 194185257.4649 | 12.2262 | 1.1953 | 4.4298 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.3 |
| 000333.SZ | 美的集团 | 家用电器 | 62192502.4029 | 14.0714 | 2.669 | 4.904 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60 |
| 600028.SH | 中国石化 | 石油加工 | 59132576.4546 | 16.6332 | 0.7098 | 4.6665 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.5 |
| 600519.SH | 贵州茅台 | 白酒 | 159117886.6649 | 19.2369 | 5.9396 | 4.0644 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 105237135.243 | 20.4078 | 2.1011 | 6.0136 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | XD中国移 | 电信运营 | 211005744.6669 | 15.5373 | 1.5345 | 4.8327 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.4 |
| 600900.SH | 长江电力 | 水力发电 | 67556749.1139 | 18.7226 | 2.9643 | 3.4154 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |
| 601318.SH | 中国平安 | 保险 | 96839669.3893 | 7.293 | 0.951 | 4.8055 | 2.479 | N/A | -7.3808 | 89.8779 | 50 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.