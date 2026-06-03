# Dividend defensive verification context for 002714.SZ as of 2026-06-03

Status: triggered
Defensive Dividend Rating: medium
- Company: 牧原股份
- Industry: 农业综合
- Dividend stability: fail
- Dividend coverage: watch
- Industry durability: pass
- Valuation buffer: pass
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 3.6378 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260602 | 36.76 | 21.6968 | 2.5316 | 3.6378 | 21221530.7853 |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p |
| --- | --- | --- |
| 20251231 | 144144965371.68 | 15486891254.04 |
| 20241231 | 137946892076.87 | 17881260485.27 |
| 20231231 | 110860727714.4 | -4263280820.31 |
| 20221231 | 124826212177.74 | 13266156512.39 |
| 20211231 | 78889870566.4 | 6903777691.92 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002714.SZ | 牧原股份 | 农业综合 | 21221530.7853 | 21.6968 | 2.5316 | 3.6378 | -1.4728 | -0.3308 | -127.05 | 50.7312 | 68.1 |
| 002299.SZ | 圣农发展 | 农业综合 | 2130693.4898 | 14.344 | 1.8982 | 2.9066 | 2.2299 | 1.1619 | 71.4079 | 53.4955 | 67.9 |
| 002458.SZ | 益生股份 | 农业综合 | 1193614.9945 | 42.3507 | 2.6919 | 1.3632 | 2.3561 | 1.6316 | 884.1125 | 36.2396 | 60.1 |
| 300761.SZ | 立华股份 | 农业综合 | 1669515.6642 | 31.7047 | 1.7981 | 1.7553 | N/A | N/A | N/A | N/A | 57.1 |
| 300498.SZ | 温氏股份 | 农业综合 | 8796492.0109 | 40.0765 | 2.2234 | 2.2665 | -2.5963 | -0.97 | -153.1524 | 53.1422 | 54.5 |
| 000930.SZ | 中粮科技 | 农业综合 | 959780.7187 | N/A | 0.9224 | N/A | -1.1557 | -0.5869 | -399.6242 | 38.8177 | 52 |
| 000061.SZ | 农产品 | 农业综合 | 1258465.3995 | 29.0612 | 1.456 | 0.9439 | N/A | N/A | N/A | N/A | 46.2 |
| 002157.SZ | 正邦科技 | 农业综合 | 2876800.5652 | N/A | 2.754 | N/A | -3.8844 | -2.5878 | -342.8554 | 52.2816 | 38.4 |
| 600201.SH | 生物股份 | 农业综合 | 1276286.5042 | 122.3979 | 2.337 | 0.259 | N/A | N/A | N/A | N/A | 38.1 |
| 605296.SH | 神农集团 | 农业综合 | 1388526.65 | N/A | 3.2447 | 1.4739 | -14.1091 | -9.5377 | -383.6163 | 33.9763 | 37.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600036.SH | 招商银行 | 银行 | 97853000.9319 | 6.4912 | 0.8641 | 7.7655 | 2.9627 | N/A | 1.518 | 90.4294 | 64.2 |
| 601398.SH | 工商银行 | 银行 | 261602192.7033 | 7.0447 | 0.6738 | 4.2275 | N/A | N/A | N/A | N/A | 60.6 |
| 600028.SH | 中国石化 | 石油加工 | 58286097.855 | 16.3951 | 0.6996 | 4.7343 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 104629831.0825 | 20.2901 | 2.089 | 6.0485 | N/A | N/A | N/A | N/A | 56.2 |
| 600519.SH | 贵州茅台 | 白酒 | 163413167.0459 | 19.7561 | 6.0999 | 3.9576 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 56.1 |
| 600941.SH | 中国移动 | 电信运营 | 217602250.6433 | 16.023 | 1.5294 | 4.774 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.1 |
| 600900.SH | 长江电力 | 水力发电 | 68413136.7339 | 18.9599 | 3.0018 | 3.3727 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 53.9 |
| 601857.SH | 中国石油 | 石油开采 | 195100362.354 | 12.2838 | 1.201 | 4.409 | N/A | N/A | N/A | N/A | 53.8 |
| 601318.SH | 中国平安 | 保险 | 97926127.909 | 7.3748 | 0.9617 | 4.7522 | 2.479 | N/A | -7.3808 | 89.8779 | 52.7 |
| 601288.SH | 农业银行 | 银行 | 225739056.8481 | 7.6705 | 0.8117 | 3.8682 | 2.3014 | N/A | 4.5238 | 93.5269 | 51.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.