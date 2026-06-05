# Dividend defensive verification context for 603345.SH as of 2026-06-05

Status: triggered
Defensive Dividend Rating: medium
- Company: 安井食品
- Industry: 食品
- Dividend stability: fail
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
| dv_ttm | N/A | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 86.68 | 18.9083 | 1.7995 | N/A | 2888948.4626 |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 16192613033.59 | 1359237139.62 | 2316722978.59 | 873464939.66 | 1064864073.2 | 1443258038.93 | 0.7834 |
| 20241231 | 15126651674.36 | 1484831242.06 | 2103844668.23 | 901279791.42 | 929784589.68 | 1202564876.81 | 0.6262 |
| 20231231 | 14045234826.03 | 1478066338.58 | 1955654340.14 | 1444458112.92 | 568996953.26 | 511196227.22 | 0.385 |
| 20221231 | 12182663119.36 | 1101029966.93 | 1407225497.62 | 1073070703.18 | 219286412.48 | 334154794.44 | 0.1992 |
| 20211231 | 9272201669.79 | 682296084.71 | 538203778.55 | 911896509.6 | 195406903.78 | -373692731.05 | 0.2864 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603345.SH | 安井食品 | 食品 | 2888948.4626 | 18.9083 | 1.7995 | N/A | 3.5703 | 3.516 | 42.7438 | 19.8771 | 62.9 |
| 603288.SH | 海天味业 | 食品 | 19913760.2844 | 27.3547 | 4.7388 | N/A | 5.8636 | 5.2564 | 10.9683 | 12.0851 | 58.9 |
| 600186.SH | 莲花控股 | 食品 | 1816070.5813 | 51.6515 | 9.6193 | N/A | 7.4533 | 5.0892 | 42.0606 | 45.3737 | 55.2 |
| 300999.SZ | 金龙鱼 | 食品 | 13938911.8391 | 38.1552 | 1.4425 | N/A | 1.5251 | 0.9889 | 50.9791 | 54.0301 | 55 |
| 000895.SZ | 双汇发展 | 食品 | 8578501.1634 | 16.3116 | 4.3139 | N/A | 5.869 | 4.1895 | 13.5898 | 47.4843 | 53.4 |
| 600737.SH | 中粮糖业 | 食品 | 3094913.3859 | 31.2547 | 2.6607 | N/A | 1.8733 | 1.2696 | 22.036 | 46.0012 | 47.5 |
| 300765.SZ | 新诺威 | 食品 | 3497436.4306 | N/A | 13.5716 | N/A | N/A | N/A | N/A | N/A | 45 |
| 600298.SH | 安琪酵母 | 食品 | 3050488.0786 | 19.0629 | 2.4476 | N/A | 3.4787 | 2.2606 | 15.08 | 47.9289 | 44.9 |
| 300972.SZ | 万辰集团 | 食品 | 3650671.008 | 20.7481 | 18.9608 | N/A | N/A | N/A | N/A | N/A | 44.5 |
| 600873.SH | 梅花生物 | 食品 | 2571489.5931 | 10.8041 | 1.5663 | N/A | 0.7198 | 0.5981 | -88.4244 | 36.7807 | 40.2 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000858.SZ | 五粮液 | 白酒 | 31472077.7045 | 24.9764 | 2.4588 | N/A | 6.5041 | 5.2115 | 82.5678 | 34.3133 | 63.4 |
| 600900.SH | 长江电力 | 水力发电 | 67556749.1139 | 18.7226 | 2.9643 | N/A | 3.01 | 1.8364 | 30.5016 | 57.3271 | 62.5 |
| 600519.SH | 贵州茅台 | 白酒 | 159117886.6649 | 19.2369 | 5.9396 | N/A | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.8 |
| 601998.SH | 中信银行 | 银行 | 41010484.5886 | 5.7593 | 0.5521 | N/A | 2.3976 | N/A | 3.0191 | 91.5368 | 56.9 |
| 601939.SH | 建设银行 | 银行 | 267355589.8511 | 7.8209 | 0.7537 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 55.6 |
| 600036.SH | 招商银行 | 银行 | 97298164.3287 | 6.4544 | 0.8592 | N/A | 2.9627 | N/A | 1.518 | 90.4294 | 55.3 |
| 601166.SH | 兴业银行 | 银行 | 39362914.565 | 5.0788 | 0.4728 | N/A | 2.6272 | N/A | 0.1513 | 91.8059 | 52.8 |
| 601288.SH | 农业银行 | 银行 | 222589209.5432 | 7.5635 | 0.8004 | N/A | 2.3014 | N/A | 4.5238 | 93.5269 | 52.2 |
| 601988.SH | 中国银行 | 银行 | 194938509.1475 | 7.9473 | 0.7132 | N/A | 1.8365 | N/A | 4.17 | 91.7975 | 50.6 |
| 601328.SH | 交通银行 | 银行 | 60352464.6243 | 6.2598 | 0.5184 | N/A | 2.044 | N/A | 3.1137 | 92.0004 | 48.8 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.