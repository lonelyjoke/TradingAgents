# Dividend defensive verification context for 000933.SZ as of 2026-07-21

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
| dv_ttm | 3.2482 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 35 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.5356 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260721 | 24.46 | 9.8466 | 2.0454 | 3.2482 | 5501064.7624 |

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
| 000807.SZ | 云铝股份 | 铝 | 8732316.7332 | 10.0601 | 2.4493 | 2.776 | 10.6372 | 10.6406 | 269.4536 | 17.7381 | 70 |
| 002532.SZ | 天山铝业 | 铝 | 5651688.4875 | 9.4533 | 1.8044 | 4.4667 | 7.288 | 5.0744 | 109.6965 | 39.9421 | 67.5 |
| 600595.SH | 中孚实业 | 铝 | 2468869.5416 | 11.1796 | 1.3765 | 2.8409 | 4.6874 | 4.1747 | 256.6124 | 29.8486 | 66 |
| 000933.SZ | 神火股份 | 铝 | 5501064.7624 | 9.8466 | 2.0454 | 3.2482 | 8.8986 | 7.1769 | 223.2834 | 40.8811 | 64.5 |
| 600219.SH | 南山铝业 | 铝 | 4800187.2688 | 11.6153 | 0.9421 | 10.3989 | 2.1898 | 1.8234 | -35.3868 | 18.4404 | 61 |
| 601600.SH | 中国铝业 | 铝 | 15713953.8024 | 10.7146 | 1.9485 | 2.8167 | 7.1058 | 5.384 | 56.3465 | 43.2655 | 51 |
| 601677.SH | 明泰铝业 | 铝 | 1963155.8574 | 8.8337 | 0.9908 | 1.9951 | 3.6076 | 3.037 | 59.6827 | 31.4242 | 48 |
| 002379.SZ | 宏桥控股 | 铝 | 23508137.2328 | 11.9278 | 4.4969 | 1.3858 | 13.8129 | 7.9201 | 37.5598 | 52.3604 | 43.5 |
| 603876.SH | 鼎胜新材 | 铝 | 1823222.2464 | 29.3401 | 2.3863 | 0.8665 | 2.5562 | 1.0844 | 127.2792 | 70.2262 | 28 |
| 603115.SH | 海星股份 | 铝 | 1690813.896 | 75.7552 | 7.8099 | 0.8584 | 1.8494 | 1.3166 | 74.7373 | 34.494 | 20.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 195283383.3126 | 12.3453 | 1.2021 | 4.4049 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 62.2 |
| 600036.SH | 招商银行 | 银行 | 95810193.4344 | 6.3557 | 0.8461 | 5.3066 | 2.9627 | N/A | 1.518 | 90.4294 | 61.3 |
| 000333.SZ | 美的集团 | 家用电器 | 64158449.6103 | 14.5162 | 2.7618 | 4.9981 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.5 |
| 600938.SH | 中国海油 | 石油开采 | 147010147.722 | 11.7926 | 1.7562 | 3.7017 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 57.7 |
| 601318.SH | 中国平安 | 保险 | 95771318.538 | 7.2126 | 0.9405 | 5.1049 | 2.479 | N/A | -7.3808 | 89.8779 | 55.1 |
| 600519.SH | 贵州茅台 | 白酒 | 163510673.28 | 19.7679 | 6.036 | 3.9773 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 54.9 |
| 600941.SH | 中国移动 | 电信运营 | 205865012.6722 | 15.1588 | 1.4469 | 4.9544 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.2 |
| 601328.SH | 交通银行 | 银行 | 60175737.0559 | 6.2415 | 0.5169 | 4.768 | 2.044 | N/A | 3.1137 | 92.0004 | 49.6 |
| 601398.SH | 工商银行 | 银行 | 269443130.3676 | 7.2558 | 0.6834 | 4.1045 | 2.0286 | N/A | 3.3093 | 92.1901 | 48.6 |
| 600028.SH | 中国石化 | 石油加工 | 61913863.2704 | 17.4155 | 0.7431 | 3.9075 | 2.0481 | 1.2478 | 28.2117 | N/A | 48.1 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.