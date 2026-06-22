# Dividend defensive verification context for 600036.SH as of 2026-06-22

Status: triggered
Defensive Dividend Rating: medium
- Company: 招商银行
- Industry: 银行
- Dividend stability: fail
- Dividend coverage: pass
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
| dv_ttm | 8.0864 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.2396 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260618 | 37.26 | 6.2336 | 0.8298 | 8.0864 | 93969144.7056 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 1.003 | 1 |
| 20250630 | 2.026 | 2 |
| 20241231 | 6 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 5.916 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 337532000000 | 150181000000 | 451457000000 | 28141000000 | 61752000000 | 423316000000 | 0.4112 |
| 20241231 | 337488000000 | 148391000000 | 447023000000 | 34930000000 | 61031000000 | 412093000000 | 0.4113 |
| 20231231 | 339123000000 | 146602000000 | 357753000000 | 30161000000 | 56342000000 | 327592000000 | 0.3843 |
| 20221231 | 344783000000 | 138012000000 | 570143000000 | 34892000000 | 56503000000 | 535251000000 | 0.4094 |
| 20211231 | 331253000000 | 119922000000 | 182048000000 | 24160000000 | 47083000000 | 157888000000 | 0.3926 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600036.SH | 招商银行 | 银行 | 93969144.7056 | 6.2336 | 0.8298 | 8.0864 | 2.9627 | N/A | 1.518 | 90.4294 | 69 |
| 601998.SH | 中信银行 | 银行 | 40454032.9921 | 5.6812 | 0.5446 | 5.2407 | 2.3976 | N/A | 3.0191 | 91.5368 | 67.5 |
| 601166.SH | 兴业银行 | 银行 | 36654072.3076 | 4.7293 | 0.4416 | 6.1547 | 2.6272 | N/A | 0.1513 | 91.8059 | 65 |
| 601288.SH | 农业银行 | 银行 | 222939192.5943 | 7.5754 | 0.7887 | 3.9168 | 2.3014 | N/A | 4.5238 | 93.5269 | 50.5 |
| 601398.SH | 工商银行 | 银行 | 255186880.0836 | 6.8719 | 0.6472 | 4.3338 | 2.0286 | N/A | 3.3093 | 92.1901 | 50 |
| 600000.SH | 浦发银行 | 银行 | 30275007.0147 | 6.0213 | 0.4016 | 4.099 | 2.1641 | N/A | 1.4945 | 91.8356 | 48 |
| 601939.SH | 建设银行 | 银行 | 259507578.448 | 7.5914 | 0.7316 | 1.873 | 2.3288 | N/A | 3.5273 | 92.0007 | 46 |
| 601328.SH | 交通银行 | 银行 | 59027007.861 | 6.1224 | 0.507 | 2.3398 | 2.044 | N/A | 3.1137 | 92.0004 | 44 |
| 601988.SH | 中国银行 | 银行 | 186238774.0204 | 7.5927 | 0.6813 | 1.8927 | 1.8365 | N/A | 4.17 | 91.7975 | 42.5 |
| 601658.SH | 邮储银行 | 银行 | 58366196.001 | 6.6413 | 0.5653 | 2.5309 | 2.2249 | N/A | 1.9013 | 94.0819 | 37.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 175334096.7324 | 11.0842 | 1.0793 | 4.9061 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64.7 |
| 600938.SH | 中国海油 | 石油开采 | 145916958.78 | 11.7049 | 1.7431 | 4.1407 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 601998.SH | 中信银行 | 银行 | 40454032.9921 | 5.6812 | 0.5446 | 5.2407 | 2.3976 | N/A | 3.0191 | 91.5368 | 62.5 |
| 600519.SH | 贵州茅台 | 白酒 | 151884914.4 | 18.3624 | 5.6068 | 4.258 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 59.1 |
| 601318.SH | 中国平安 | 保险 | 89415536.196 | 6.7339 | 0.8781 | 5.4678 | 2.479 | N/A | -7.3808 | 89.8779 | 58.8 |
| 601088.SH | 中国神华 | 煤炭开采 | 89490605.9218 | 17.3542 | 1.8609 | 7.0718 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 58.4 |
| 600941.SH | 中国移动 | 电信运营 | 198691836.642 | 14.6306 | 1.3965 | 5.1322 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600028.SH | 中国石化 | 石油加工 | 56955917.1882 | 16.0209 | 0.6836 | 4.2477 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 52.5 |
| 600900.SH | 长江电力 | 水力发电 | 65232268.3882 | 18.0784 | 2.8623 | 3.5371 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 51.2 |
| 601398.SH | 工商银行 | 银行 | 255186880.0836 | 6.8719 | 0.6472 | 4.3338 | 2.0286 | N/A | 3.3093 | 92.1901 | 51.2 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.