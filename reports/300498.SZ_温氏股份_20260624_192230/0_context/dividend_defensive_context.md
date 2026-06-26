# Dividend defensive verification context for 300498.SZ as of 2026-06-24

Status: triggered
Defensive Dividend Rating: weak
- Company: 温氏股份
- Industry: 农业综合
- Dividend stability: fail
- Dividend coverage: pass
- Industry durability: fail
- Valuation buffer: pass
- Dividend trap risk: high

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 4.2314 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 23 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.1888 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260624 | 11.79 | 35.9351 | 1.9829 | 4.2314 | 7844982.6447 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.4 | 2 |
| 20250930 | 0.6 | 2 |
| 20250630 | 0 | 1 |
| 20241231 | 0.6 | 3 |
| 20240930 | 0.45 | 3 |
| 20240630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 103862188499.72 | 5266415817.82 | 11807445685.82 | 10737358062.01 | 4070518710.27 | 1070087623.81 | 0.7729 |
| 20241231 | 104924353752.25 | 9230418856.62 | 19586123379.19 | 9135258924.17 | 2476550952.19 | 10450864455.02 | 0.2683 |
| 20231231 | 89921099545.85 | -6389662358.5 | 7593935845.43 | 9774628961.17 | 2424878326.48 | -2180693115.74 | 0.3795 |
| 20221231 | 83725111925.72 | 5289005087.07 | 11074527590.93 | 9352451112.82 | 1863152179.88 | 1722076478.11 | 0.3523 |
| 20211231 | 64964594187.23 | -13404359150.48 | 766161193.39 | 13239799903.52 | 2479427931.07 | -12473638710.13 | 0.185 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002299.SZ | 圣农发展 | 农业综合 | 1918121.3531 | 12.913 | 1.6718 | 3.2288 | 2.2299 | 1.1619 | 71.4079 | 53.4955 | 67.8 |
| 300761.SZ | 立华股份 | 农业综合 | 1376144.4498 | 26.1334 | 1.4495 | 2.1295 | 1.6463 | 1.0426 | -24.8494 | 43.3835 | 67.6 |
| 002714.SZ | 牧原股份 | 农业综合 | 18779555.988 | 19.2001 | 2.177 | 4.1109 | -1.4728 | -0.3308 | -127.05 | 50.7312 | 64.4 |
| 000061.SZ | 农产品 | 农业综合 | 1121503.078 | 25.9097 | 1.2975 | N/A | 1.5744 | 1.1031 | 80.891 | 52.0504 | 61.5 |
| 300498.SZ | 温氏股份 | 农业综合 | 7844982.6447 | 35.9351 | 1.9829 | 4.2314 | -2.5963 | -0.97 | -153.1524 | 53.1422 | 60 |
| 002458.SZ | 益生股份 | 农业综合 | 1153541.6386 | 40.9289 | 2.6016 | 1.4105 | 2.3561 | 1.6316 | 884.1125 | 36.2396 | 57.8 |
| 600201.SH | 生物股份 | 农业综合 | 1366338.0462 | 131.034 | 2.5018 | 0.2959 | 1.4893 | 1.3029 | 5.4418 | 14.8828 | 48.6 |
| 002157.SZ | 正邦科技 | 农业综合 | 2599295.6625 | N/A | 2.4884 | N/A | -3.8844 | -2.5878 | -342.8554 | 52.2816 | 40 |
| 605296.SH | 神农集团 | 农业综合 | 1309287.178 | N/A | 3.0595 | 1.5631 | -14.1091 | -9.5377 | -383.6163 | 33.9763 | 28.9 |
| 000048.SZ | 京基智农 | 农业综合 | 1075251.2784 | N/A | 2.863 | 1.8341 | -5.898 | -2.1506 | -306.2703 | 62.3494 | 23.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 138834995.634 | 11.1368 | 1.6585 | 4.3519 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 69.1 |
| 600036.SH | 招商银行 | 银行 | 92708152.4256 | 6.1499 | 0.8187 | 8.1964 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 601857.SH | 中国石油 | 石油开采 | 172222740.1098 | 10.8875 | 1.0601 | 4.9947 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 63.1 |
| 600519.SH | 贵州茅台 | 白酒 | 150969854.6688 | 18.2518 | 5.573 | 4.2838 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601318.SH | 中国平安 | 保险 | 88944737.504 | 6.6985 | 0.8735 | 5.4967 | 2.479 | N/A | -7.3808 | 89.8779 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 86866184.3715 | 16.8453 | 1.8063 | 7.2854 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | 中国移动 | 电信运营 | 192296409.276 | 14.1596 | 1.3516 | 5.3029 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.1 |
| 600028.SH | 中国石化 | 石油加工 | 56351289.6172 | 15.8508 | 0.6764 | 4.2932 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 53.8 |
| 600900.SH | 长江电力 | 水力发电 | 65085459.082 | 18.0377 | 2.8558 | 3.5451 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |
| 601398.SH | 工商银行 | 银行 | 257325317.6262 | 6.9295 | 0.6527 | 4.2978 | 2.0286 | N/A | 3.3093 | 92.1901 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.