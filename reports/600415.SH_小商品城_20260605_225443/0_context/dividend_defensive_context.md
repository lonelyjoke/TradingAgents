# Dividend defensive verification context for 600415.SH as of 2026-06-05

Status: triggered
Defensive Dividend Rating: medium
- Company: 小商品城
- Industry: 商品城
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
| dv_ttm | 2.7943 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.5522 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 11.81 | 14.7497 | 2.7132 | 2.7943 | 6476083.4459 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.5 | 1 |
| 20250630 | 0 | 1 |
| 20241231 | 0.99 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.6 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 19927252694.51 | 4203546946.97 | 10529211443 | 2182072518.33 | 1993385493.06 | 8347138924.67 | 0.4742 |
| 20241231 | 15737383922.24 | 3073677494.86 | 4491339090.33 | 1500262163.77 | 1402224958.9 | 2991076926.56 | 0.4562 |
| 20231231 | 11299686665.89 | 2676182133.26 | 1845059849.92 | 2627630588.71 | 594916647.3 | -782570738.79 | 0.2223 |
| 20221231 | 7619693742.6 | 1104719091.71 | 1400090713.77 | 4114901826.31 | 652035197.63 | -2714811112.54 | 0.5902 |
| 20211231 | 6033842972.95 | 1334095906.95 | 2033082507.76 | 2042626824.44 | 650819017.71 | -9544316.68 | 0.4878 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600415.SH | 小商品城 | 商品城 | 6476083.4459 | 14.7497 | 2.7132 | 2.7943 | 4.2312 | 2.7865 | 23.293 | 45.7309 | 72.5 |
| 600790.SH | 轻纺城 | 商品城 | 586316.3712 | 19.3208 | 0.9857 | 2.7792 | 6.0319 | 3.5788 | 1079.7838 | 49.3416 | 70 |
| 002344.SZ | 海宁皮城 | 商品城 | 501503.2314 | 104.2177 | 0.593 | 0.9719 | 0.4417 | 0.4561 | -37.6439 | 34.2155 | 46.2 |
| 000058.SZ | 深赛格 | 商品城 | 870458.8751 | 122.2217 | 4.3348 | 0.3395 | 1.2198 | 1.0467 | 2.145 | 49.9572 | 31.2 |

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