# Dividend defensive verification context for 002840.SZ as of 2026-06-24

Status: triggered
Defensive Dividend Rating: medium
- Company: 华统股份
- Industry: 食品
- Dividend stability: watch
- Dividend coverage: fail
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
| dv_ttm | N/A | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 18 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6518 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260624 | 7.41 | N/A | 1.6528 | N/A | 594405.3024 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0 | 2 |
| 20250630 | 0 | 1 |
| 20241231 | 0 | 2 |
| 20240630 | 0 | 1 |
| 20231231 | 0 | 2 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 8072002990.88 | -136017659.72 | 525132576 | 647585454.93 | 172607443.76 | -122452878.93 | 1.269 |
| 20241231 | 9091691841.33 | 73038293.56 | 525646757.21 | 885043414.39 | 188355348.6 | -359396657.18 | 2.5789 |
| 20231231 | 8578492006.25 | -604857321.1 | 526046148.77 | 1095693468.23 | 198636464.88 | -569647319.46 | 0.3284 |
| 20221231 | 9452164593.11 | 87744730.86 | 374496839.73 | 1131688997.57 | 191405390.32 | -757192157.84 | 2.1814 |
| 20211231 | 8342248673.41 | -192463534.51 | 251565008.71 | 2228942953.11 | 141449686.5 | -1977377944.4 | 0.7349 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603288.SH | 海天味业 | 食品 | 20487238.9749 | 28.1418 | 4.8753 | 3.8802 | 5.8636 | 5.2564 | 10.9683 | 12.0851 | 67.9 |
| 000895.SZ | 双汇发展 | 食品 | 7819740.3284 | 14.8688 | 3.4513 | 6.4245 | 5.869 | 4.1895 | 13.5898 | 47.4843 | 67 |
| 603345.SH | 安井食品 | 食品 | 2816291.205 | 18.4328 | 1.7542 | 3.3771 | 3.5703 | 3.516 | 42.7438 | 19.8771 | 64.8 |
| 600186.SH | 莲花控股 | 食品 | 2542140.2609 | 72.3019 | 13.4652 | N/A | 7.4533 | 5.0892 | 42.0606 | 45.3737 | 56 |
| 600737.SH | 中粮糖业 | 食品 | 2489619.3048 | 25.142 | 2.1404 | 3.5223 | 1.8733 | 1.2696 | 22.036 | 46.0012 | 53.4 |
| 300999.SZ | 金龙鱼 | 食品 | 12946760.502 | 35.4394 | 1.3227 | 0.9631 | 1.5251 | 0.9889 | 50.9791 | 54.0301 | 52.1 |
| 600298.SH | 安琪酵母 | 食品 | 3099955.5564 | 19.372 | 2.4871 | 1.5398 | 3.4787 | 2.2606 | 15.08 | 47.9289 | 45.2 |
| 300972.SZ | 万辰集团 | 食品 | 3433801.9736 | 19.5155 | 17.0297 | 0.556 | 35.9913 | 12.4979 | 193.1214 | 68.1839 | 44.6 |
| 600873.SH | 梅花生物 | 食品 | 2232176.3932 | 9.3785 | 1.3597 | N/A | 0.7198 | 0.5981 | -88.4244 | 36.7807 | 43 |
| 300765.SZ | 石药创新 | 食品 | 3656155.3187 | N/A | 14.1874 | N/A | -3.5793 | -1.7543 | -248.8816 | 56.9987 | 26 |

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