# Dividend defensive verification context for 600031.SH as of 2026-08-02

Status: triggered
Defensive Dividend Rating: weak
- Company: 三一重工
- Industry: 工程机械
- Dividend stability: fail
- Dividend coverage: pass
- Industry durability: fail
- Valuation buffer: watch
- Dividend trap risk: high

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 2.3723 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 32 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3334 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260731 | 20.55 | 22.4431 | 2.0862 | 2.3723 | 18895734.042 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.36 | 2 |
| 20250630 | 0.93 | 3 |
| 20241231 | 1.08 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.66 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 89699505000 | 8408057000 | 19975261000 | 2771319000 | 6364740000 | 17203942000 | 0.757 |
| 20241231 | 78383379000 | 5975451000 | 14814278000 | 2938287000 | 2997376000 | 11875991000 | 0.5016 |
| 20231231 | 74018936000 | 4527498000 | 5708220000 | 4525221000 | 2825393000 | 1182999000 | 0.6241 |
| 20221231 | 80822133000 | 4272802000 | 4098763000 | 5665026000 | 4723813000 | -1566263000 | 1.1056 |
| 20211231 | 106873394000 | 12033364000 | 11904233000 | 10299972000 | 5614143000 | 1604261000 | 0.4665 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603298.SH | 杭叉集团 | 工程机械 | 3679261.908 | 16.4919 | 3.0567 | 2.136 | 3.9891 | 2.6424 | 9.1745 | 38.4447 | 65.6 |
| 600031.SH | 三一重工 | 工程机械 | 18895734.042 | 22.4431 | 2.0862 | 2.3723 | 2.7732 | 1.52 | 0.4593 | 47.4353 | 61.9 |
| 000157.SZ | 中联重科 | 工程机械 | 6572886.752 | 15.1713 | 1.127 | 5.2632 | 1.5244 | 0.7169 | -37.3021 | 57.6623 | 58 |
| 000425.SZ | 徐工机械 | 工程机械 | 10493244.5623 | 15.9235 | 1.6746 | 2.2198 | 3.3405 | 1.395 | 0.8624 | 65.041 | 57.2 |
| 603338.SH | 浙江鼎力 | 工程机械 | 2987452.61 | 15.5316 | 2.5224 | 1.9492 | 3.8958 | 2.796 | 5.6616 | 32.0943 | 56.9 |
| 601100.SH | 恒立液压 | 工程机械 | 14541203.745 | 52.5212 | 8.13 | 0.793 | 3.7092 | 3.1411 | 5.5878 | 20.431 | 52.2 |
| 688425.SH | 铁建重工 | 工程机械 | 2293403.71 | 16.3911 | 1.2174 | 1.9767 | 1.3271 | 0.9652 | -25.2415 | 31.034 | 47.5 |
| 601399.SH | 国机重装 | 工程机械 | 2402114.1147 | 50.097 | 1.6146 | N/A | 0.8549 | 0.3751 | 14.3925 | 53.9859 | 46.5 |
| 000811.SZ | 冰轮环境 | 工程机械 | 3503447.34 | 59.5952 | 5.3629 | 0.2833 | 1.8158 | 1.1612 | 25.0619 | 46.825 | 40.6 |
| 601106.SH | 中国一重 | 工程机械 | 2119054.9161 | N/A | 4.1025 | N/A | 0.0376 | 0.2421 | 102.3353 | 83.0515 | 33.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 202787243.4024 | 12.8197 | 1.2483 | 4.2419 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 62.2 |
| 600036.SH | 招商银行 | 银行 | 99921028.2672 | 6.6284 | 0.8824 | 5.0883 | 2.9627 | N/A | 1.518 | 90.4294 | 61.9 |
| 000333.SZ | 美的集团 | 家用电器 | 66693724.764 | 15.0899 | 2.8709 | 4.8056 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 58.9 |
| 600938.SH | 中国海油 | 石油开采 | 153331631.604 | 12.2997 | 1.8317 | 3.5491 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 57.7 |
| 601318.SH | 中国平安 | 保险 | 99410954.58 | 7.4867 | 0.9762 | 4.918 | 2.479 | N/A | -7.3808 | 89.8779 | 55.8 |
| 600519.SH | 贵州茅台 | 白酒 | 168836020.896 | 20.4118 | 6.2325 | 3.8519 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 54.9 |
| 600941.SH | 中国移动 | 电信运营 | 211220885.6583 | 15.5531 | 1.4846 | 4.8288 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.8 |
| 601328.SH | 交通银行 | 银行 | 63445197.0721 | 6.5806 | 0.545 | 4.5223 | 2.044 | N/A | 3.1137 | 92.0004 | 50.2 |
| 600028.SH | 中国石化 | 石油加工 | 63606820.4692 | 17.8917 | 0.7635 | 3.8035 | 2.0481 | 1.2478 | 28.2117 | N/A | 48.1 |
| 601398.SH | 工商银行 | 银行 | 284768599.4229 | 7.6685 | 0.7223 | 3.8836 | 2.0286 | N/A | 3.3093 | 92.1901 | 47.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.