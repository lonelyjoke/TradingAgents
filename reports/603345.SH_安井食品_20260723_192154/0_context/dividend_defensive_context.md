# Dividend defensive verification context for 603345.SH as of 2026-07-23

Status: triggered
Defensive Dividend Rating: strong
- Company: 安井食品
- Industry: 食品
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
| dv_ttm | 3.2756 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 19 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 0.9155 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260723 | 87.12 | 19.0043 | 1.8086 | 3.2756 | 2903612.8968 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 4.32 | 3 |
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
| 000895.SZ | 双汇发展 | 食品 | 8682440.9672 | 16.5092 | 3.832 | 5.7861 | 5.869 | 4.1895 | 13.5898 | 47.4843 | 69 |
| 603288.SH | 海天味业 | 食品 | 21446938.2585 | 29.4601 | 5.1037 | 3.7066 | 5.8636 | 5.2564 | 10.9683 | 12.0851 | 65.2 |
| 603345.SH | 安井食品 | 食品 | 2903612.8968 | 19.0043 | 1.8086 | 3.2756 | 3.5703 | 3.516 | 42.7438 | 19.8771 | 63.4 |
| 300146.SZ | 汤臣倍健 | 食品 | 1696752.1313 | 23.2648 | 1.4727 | 4.4427 | 3.5502 | 3.4477 | -11.6226 | 17.6112 | 59.4 |
| 600873.SH | 梅花生物 | 食品 | 2363975.7531 | 9.9323 | 1.4399 | 5.0759 | 0.7198 | 0.5981 | -88.4244 | 36.7807 | 53.7 |
| 300999.SZ | 金龙鱼 | 食品 | 14134089.0405 | 38.6895 | 1.444 | 0.8822 | 1.5251 | 0.9889 | 50.9791 | 54.0301 | 49.1 |
| 600737.SH | 中粮糖业 | 食品 | 2684254.491 | 27.1076 | 2.3077 | 3.2669 | 1.8733 | 1.2696 | 22.036 | 46.0012 | 47.6 |
| 300972.SZ | 万辰集团 | 食品 | 3694479.6592 | 20.997 | 18.3225 | 0.5168 | 35.9913 | 12.4979 | 193.1214 | 68.1839 | 45.3 |
| 600298.SH | 安琪酵母 | 食品 | 3373327.8969 | 21.0804 | 2.7064 | 1.415 | 3.4787 | 2.2606 | 15.08 | 47.9289 | 42.8 |
| 300765.SZ | 石药创新 | 食品 | 5423133.1869 | N/A | 21.0441 | N/A | -3.5793 | -1.7543 | -248.8816 | 56.9987 | 24.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 199126823.8464 | 12.5883 | 1.2257 | 4.3199 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 62.2 |
| 600036.SH | 招商银行 | 银行 | 98130419.2296 | 6.5096 | 0.8666 | 5.1812 | 2.9627 | N/A | 1.518 | 90.4294 | 60.7 |
| 000333.SZ | 美的集团 | 家用电器 | 64539121.5553 | 14.6024 | 2.7782 | 4.9671 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 58.9 |
| 600938.SH | 中国海油 | 石油开采 | 156801318.246 | 12.578 | 1.8731 | 3.4705 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 57.7 |
| 600941.SH | 中国移动 | 电信运营 | 204759144.1609 | 15.0773 | 1.4392 | 4.9812 | 2.084 | 1.759 | -4.2082 | 33.7319 | 56.3 |
| 600519.SH | 贵州茅台 | 白酒 | 161511792.8016 | 19.5263 | 5.9622 | 4.0265 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 54.9 |
| 601318.SH | 中国平安 | 保险 | 98324496.06 | 7.4048 | 0.9656 | 4.9724 | 2.479 | N/A | -7.3808 | 89.8779 | 54.8 |
| 601328.SH | 交通银行 | 银行 | 61412830.035 | 6.3698 | 0.5275 | 4.672 | 2.044 | N/A | 3.1137 | 92.0004 | 50.2 |
| 601398.SH | 工商银行 | 银行 | 273720005.4528 | 7.371 | 0.6942 | 4.0404 | 2.0286 | N/A | 3.3093 | 92.1901 | 48.6 |
| 600028.SH | 中国石化 | 石油加工 | 62760341.8698 | 17.6536 | 0.7533 | 3.8548 | 2.0481 | 1.2478 | 28.2117 | N/A | 48.1 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.