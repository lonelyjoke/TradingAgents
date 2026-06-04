# Dividend defensive verification context for 601318.SH as of 2026-06-04

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
| dv_ttm | 4.7858 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 34 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0392 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260603 | 53.7 | 7.323 | 0.9549 | 4.7858 | 97238037.5132 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 1.75 | 1 |
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
| 601601.SH | 中国太保 | 保险 | 30130909.4371 | 5.5882 | 0.9428 | 3.4483 | 3.2299 | N/A | 4.3004 | 89.0876 | 63 |
| 601318.SH | 中国平安 | 保险 | 97238037.5132 | 7.323 | 0.9549 | 4.7858 | 2.479 | N/A | -7.3808 | 89.8779 | 60 |
| 601336.SH | 新华保险 | 保险 | 17965468.8694 | 4.8683 | 1.454 | 4.6189 | 5.5304 | N/A | 10.5236 | 93.3325 | 60 |
| 601319.SH | 中国人保 | 保险 | 29453177.7283 | 6.9121 | 0.9223 | 2.8826 | 2.8055 | N/A | -31.4032 | 78.5414 | 52 |
| 601628.SH | 中国人寿 | 保险 | 92934350.04 | 6.419 | 1.5534 | 2.0925 | 3.2686 | N/A | -32.279 | 92.0676 | 35 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 172438673.054 | 13.8324 | 2.0599 | 3.5038 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 601857.SH | 中国石油 | 石油开采 | 198577760.9325 | 12.5028 | 1.2224 | 4.3318 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.9 |
| 600036.SH | 招商银行 | 银行 | 97096405.5639 | 6.441 | 0.8575 | 7.826 | 2.9627 | N/A | 1.518 | 90.4294 | 60.9 |
| 000333.SZ | 美的集团 | 家用电器 | 62889821.9619 | 14.2292 | 2.6992 | 4.8497 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 59.7 |
| 600028.SH | 中国石化 | 石油加工 | 58769799.9119 | 16.5311 | 0.7054 | 4.6954 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 59.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 105952886.575 | 20.5466 | 2.1154 | 5.973 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 57.8 |
| 600519.SH | 贵州茅台 | 白酒 | 160249210.5138 | 19.3736 | 5.9818 | 4.0357 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 600941.SH | 中国移动 | 电信运营 | 217038851.0698 | 15.9815 | 1.5255 | 4.7864 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 601288.SH | 农业银行 | 银行 | 222589209.5432 | 7.5635 | 0.8004 | 3.923 | 2.3014 | N/A | 4.5238 | 93.5269 | 51.2 |
| 601398.SH | 工商银行 | 银行 | 259463755.1608 | 6.9871 | 0.6683 | 4.2624 | 2.0286 | N/A | 3.3093 | 92.1901 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.