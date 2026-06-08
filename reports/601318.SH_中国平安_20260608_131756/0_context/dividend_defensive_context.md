# Dividend defensive verification context for 601318.SH as of 2026-06-08

Status: triggered
Defensive Dividend Rating: strong
- Company: 中国平安
- Industry: 保险
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
| dv_ttm | 4.8055 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 34 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0509 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 53.48 | 7.293 | 0.951 | 4.8055 | 96839669.3893 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 5.25 | 3 |
| 20250630 | 1.9 | 2 |
| 20241231 | 4.86 | 3 |
| 20240630 | 1.86 | 2 |
| 20231231 | 4.5 | 3 |
| 20230630 | 1.86 | 2 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 1050506000000 | 134778000000 | 658632000000 | 8355000000 | 77146000000 | 650277000000 | 0.5724 |
| 20241231 | 1028925000000 | 126607000000 | 382474000000 | 6678000000 | 74669000000 | 375796000000 | 0.5898 |
| 20231231 | 913789000000 | 85665000000 | 360403000000 | 7810000000 | 73087000000 | 352593000000 | 0.8532 |
| 20221231 | 1110568000000 | 83774000000 | 485905000000 | 8871000000 | 77791000000 | 477034000000 | 0.9286 |
| 20211231 | 1180444000000 | 101618000000 | 90116000000 | 12186000000 | 92829000000 | 77930000000 | 0.9135 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601601.SH | 中国太保 | 保险 | 29871160.2178 | 5.54 | 0.9346 | 3.4783 | 3.2299 | N/A | 4.3004 | 89.0876 | 63 |
| 601318.SH | 中国平安 | 保险 | 96839669.3893 | 7.293 | 0.951 | 4.8055 | 2.479 | N/A | -7.3808 | 89.8779 | 60 |
| 601336.SH | 新华保险 | 保险 | 17578645.091 | 4.7635 | 1.4227 | 4.7205 | 5.5304 | N/A | 10.5236 | 93.3325 | 60 |
| 601319.SH | 中国人保 | 保险 | 29055161.813 | 6.8187 | 0.9098 | 2.9221 | 2.8055 | N/A | -31.4032 | 78.5414 | 52 |
| 601628.SH | 中国人寿 | 保险 | 92764761.81 | 6.4072 | 1.5506 | 2.0963 | 3.2686 | N/A | -32.279 | 92.0676 | 35 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 167210378.1157 | 13.413 | 1.9975 | 3.6134 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 600036.SH | 招商银行 | 银行 | 97298164.3287 | 6.4544 | 0.8592 | 7.8097 | 2.9627 | N/A | 1.518 | 90.4294 | 60.9 |
| 601857.SH | 中国石油 | 石油开采 | 194185257.4649 | 12.2262 | 1.1953 | 4.4298 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.3 |
| 600028.SH | 中国石化 | 石油加工 | 59132576.4546 | 16.6332 | 0.7098 | 4.6665 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 60 |
| 000333.SZ | 美的集团 | 家用电器 | 62192502.4029 | 14.0714 | 2.669 | 4.904 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 59.7 |
| 601088.SH | 中国神华 | 煤炭开采 | 105237135.243 | 20.4078 | 2.1011 | 6.0136 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 57.8 |
| 600519.SH | 贵州茅台 | 白酒 | 159117886.6649 | 19.2369 | 5.9396 | 4.0644 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 600941.SH | 中国移动 | 电信运营 | 211005744.6669 | 15.5373 | 1.5345 | 4.8327 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 601288.SH | 农业银行 | 银行 | 222589209.5432 | 7.5635 | 0.8004 | 3.923 | 2.3014 | N/A | 4.5238 | 93.5269 | 51.2 |
| 601398.SH | 工商银行 | 银行 | 261602192.7033 | 7.0447 | 0.6738 | 4.2275 | 2.0286 | N/A | 3.3093 | 92.1901 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.