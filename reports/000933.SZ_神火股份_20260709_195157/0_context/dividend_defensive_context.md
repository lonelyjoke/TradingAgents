# Dividend defensive verification context for 000933.SZ as of 2026-07-09

Status: triggered
Defensive Dividend Rating: strong
- Company: 神火股份
- Industry: 铝
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
| dv_ttm | 3.7214 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 24 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6432 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260709 | 21.35 | 8.5946 | 1.7853 | 3.7214 | 4801624.394 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 2.4 | 3 |
| 20250630 | 0 | 1 |
| 20241231 | 1.5 | 3 |
| 20240930 | 0.9 | 3 |
| 20240630 | 0 | 3 |
| 20231231 | 2.4 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 41240761541.38 | 4005359185.05 | 8743217687.83 | 861031236.94 | 2153375239.72 | 7882186450.89 | 0.5376 |
| 20241231 | 38372663537.44 | 4306779295.81 | 7718522005.69 | 1328292242.33 | 3289419005.67 | 6390229763.36 | 0.7638 |
| 20231231 | 37625079556.47 | 5905386622.42 | 11190206465.61 | 985370936.41 | 2777801131.15 | 10204835529.2 | 0.4704 |
| 20221231 | 42703853286.57 | 7571202799.16 | 14060764159.71 | 304148906.72 | 2065701754.89 | 13756615252.99 | 0.2728 |
| 20211231 | 34451566769.76 | 3234102540.1 | 11296305278.4 | 1910982933.49 | 1272512607.22 | 9385322344.91 | 0.3935 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000807.SZ | 云铝股份 | 铝 | 7591358.7486 | 8.7456 | 2.1293 | 3.1932 | 10.6372 | 10.6406 | 269.4536 | 17.7381 | 76.5 |
| 002532.SZ | 天山铝业 | 铝 | 4938862.9125 | 8.261 | 1.5768 | 5.1114 | 7.288 | 5.0744 | 109.6965 | 39.9421 | 67.5 |
| 000933.SZ | 神火股份 | 铝 | 4801624.394 | 8.5946 | 1.7853 | 3.7214 | 8.8986 | 7.1769 | 223.2834 | 40.8811 | 64.5 |
| 600219.SH | 南山铝业 | 铝 | 4604964.3416 | 11.1429 | 0.9038 | 10.8397 | 2.1898 | 1.8234 | -35.3868 | 18.4404 | 61 |
| 600595.SH | 中孚实业 | 铝 | 2284505.907 | 10.3448 | 1.2737 | 3.0702 | 4.6874 | 4.1747 | 256.6124 | 29.8486 | 60 |
| 601600.SH | 中国铝业 | 铝 | 13895526.834 | 9.4747 | 1.723 | 3.1853 | 7.1058 | 5.384 | 56.3465 | 43.2655 | 51 |
| 601677.SH | 明泰铝业 | 铝 | 1892288.2932 | 8.5148 | 0.9551 | 2.0698 | 3.6076 | 3.037 | 59.6827 | 31.4242 | 46 |
| 002379.SZ | 宏桥控股 | 铝 | 18439032.253 | 9.3558 | 3.5273 | 1.7668 | 13.8129 | 7.9201 | 37.5598 | 52.3604 | 43.5 |
| 603876.SH | 鼎胜新材 | 铝 | 2025802.496 | 32.6001 | 2.6514 | 0.7798 | 2.5562 | 1.0844 | 127.2792 | 70.2262 | 26.5 |
| 603115.SH | 海星股份 | 铝 | 2434626.876 | 109.0809 | 11.2455 | 0.5961 | 1.8494 | 1.3166 | 74.7373 | 34.494 | 23.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 134747419.59 | 10.8089 | 1.6097 | 4.4839 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 67.2 |
| 601857.SH | 中国石油 | 石油开采 | 172039719.132 | 10.8759 | 1.059 | 5 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64 |
| 600036.SH | 招商银行 | 银行 | 94700520.228 | 6.2821 | 0.8363 | 8.024 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 000333.SZ | 美的集团 | 家用电器 | 60397410.7937 | 13.6653 | 2.5999 | 5.3163 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.4 |
| 600519.SH | 贵州茅台 | 白酒 | 147783396.6704 | 17.8666 | 5.4554 | 4.4006 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.4 |
| 601939.SH | 建设银行 | 银行 | 258722777.3035 | 7.5684 | 0.7293 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 55.6 |
| 601318.SH | 中国平安 | 保险 | 89614720.258 | 6.7489 | 0.88 | 5.4556 | 2.479 | N/A | -7.3808 | 89.8779 | 55.2 |
| 600941.SH | 中国移动 | 电信运营 | 192356069.8773 | 14.164 | 1.352 | 5.3023 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.4 |
| 600028.SH | 中国石化 | 石油加工 | 58165172.3302 | 16.3611 | 0.6981 | 4.1594 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 51.2 |
| 600900.SH | 长江电力 | 水力发电 | 67948240.5529 | 18.8311 | 2.9814 | 3.3958 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 49.8 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.