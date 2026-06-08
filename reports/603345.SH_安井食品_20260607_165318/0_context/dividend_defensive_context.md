# Dividend defensive verification context for 603345.SH as of 2026-06-07

Status: triggered
Defensive Dividend Rating: medium
- Company: 安井食品
- Industry: 食品
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
| dv_ttm | 2.8038 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 19 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 0.899 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 86.68 | 18.9083 | 1.7995 | 2.8038 | 2888948.4626 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 2.88 | 2 |
| 20250630 | 2.85 | 2 |
| 20241231 | 3.045 | 3 |
| 20240930 | 1.9 | 2 |
| 20240630 | 2.76 | 2 |
| 20231231 | 5.325 | 3 |

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
| 603345.SH | 安井食品 | 食品 | 2888948.4626 | 18.9083 | 1.7995 | 2.8038 | 3.5703 | 3.516 | 42.7438 | 19.8771 | 67.4 |
| 000895.SZ | 双汇发展 | 食品 | 8578501.1634 | 16.3116 | 4.3139 | 5.8562 | 5.869 | 4.1895 | 13.5898 | 47.4843 | 67 |
| 603288.SH | 海天味业 | 食品 | 19913760.2844 | 27.3547 | 4.7388 | 1.6434 | 5.8636 | 5.2564 | 10.9683 | 12.0851 | 60.8 |
| 600737.SH | 中粮糖业 | 食品 | 3094913.3859 | 31.2547 | 2.6607 | 2.8334 | 1.8733 | 1.2696 | 22.036 | 46.0012 | 58.4 |
| 600186.SH | 莲花控股 | 食品 | 1816070.5813 | 51.6515 | 9.6193 | N/A | 7.4533 | 5.0892 | 42.0606 | 45.3737 | 54 |
| 300999.SZ | 金龙鱼 | 食品 | 13938911.8391 | 38.1552 | 1.4425 | 0.8946 | 1.5251 | 0.9889 | 50.9791 | 54.0301 | 52.1 |
| 600298.SH | 安琪酵母 | 食品 | 3050488.0786 | 19.0629 | 2.4476 | 1.5652 | 3.4787 | 2.2606 | 15.08 | 47.9289 | 45.7 |
| 300972.SZ | 万辰集团 | 食品 | 3650671.008 | 20.7481 | 18.9608 | 0.523 | 35.9913 | 12.4979 | 193.1214 | 68.1839 | 45.6 |
| 600873.SH | 梅花生物 | 食品 | 2571489.5931 | 10.8041 | 1.5663 | N/A | 0.7198 | 0.5981 | -88.4244 | 36.7807 | 44 |
| 300765.SZ | 新诺威 | 食品 | 3497436.4306 | N/A | 13.5716 | N/A | -3.5793 | -1.7543 | -248.8816 | 56.9987 | 25 |

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