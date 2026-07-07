# Dividend defensive verification context for 000528.SZ as of 2026-07-07

Status: triggered
Defensive Dividend Rating: strong
- Company: 柳工
- Industry: 工程机械
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
| dv_ttm | 3.8224 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 26 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0635 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260706 | 8.27 | 10.8137 | 0.8855 | 3.8224 | 1684867.1961 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.975 | 3 |
| 20250630 | 0 | 1 |
| 20241231 | 0.819 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.5987 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 33143878244.37 | 1609225714.3 | 1005334550.87 | 715058347.74 | 874703212.96 | 290276203.13 | 0.5436 |
| 20241231 | 30062709198.12 | 1327039490.08 | 1322006265.24 | 664177690.37 | 732746454.44 | 657828574.87 | 0.5522 |
| 20231231 | 27519122309.99 | 867811519.99 | 1628961753.49 | 793842165.65 | 502470951.53 | 835119587.84 | 0.579 |
| 20221231 | 26479736961.83 | 599326029.8 | 958769895.05 | 714786732.76 | 517482562.83 | 243983162.29 | 0.8634 |
| 20211231 | 28700729485.25 | 995312780.88 | 846491366.35 | 912361270.17 | 663335831.29 | -65869903.82 | 0.6665 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603298.SH | 杭叉集团 | 工程机械 | 3471001.8 | 15.5584 | 2.8837 | 2.2642 | 3.9891 | 2.6424 | 9.1745 | 38.4447 | 67.8 |
| 603338.SH | 浙江鼎力 | 工程机械 | 2683137.5221 | 13.9495 | 2.2654 | 2.1702 | 3.8958 | 2.796 | 5.6616 | 32.0943 | 63.1 |
| 000425.SZ | 徐工机械 | 工程机械 | 9907684.0399 | 15.0349 | 1.5811 | 2.351 | 3.3405 | 1.395 | 0.8624 | 65.041 | 61.9 |
| 000157.SZ | 中联重科 | 工程机械 | 6304782.1608 | 14.5525 | 1.081 | 6.8587 | 1.5244 | 0.7169 | -37.3021 | 57.6623 | 58 |
| 601100.SH | 恒立液压 | 工程机械 | 15754646.75 | 56.904 | 8.8084 | 0.2553 | 3.7092 | 3.1411 | 5.5878 | 20.431 | 52.2 |
| 600031.SH | 三一重工 | 工程机械 | 17369363.3116 | 20.6302 | 1.9177 | 1.6328 | 2.7732 | 1.52 | 0.4593 | 47.4353 | 49.4 |
| 688425.SH | 铁建重工 | 工程机械 | 2218734.752 | 15.8575 | 1.1778 | 2.0433 | 1.3271 | 0.9652 | -25.2415 | 31.034 | 47.5 |
| 601399.SH | 国机重装 | 工程机械 | 2409327.6706 | 50.2474 | 1.6194 | N/A | 0.8549 | 0.3751 | 14.3925 | 53.9859 | 45 |
| 000811.SZ | 冰轮环境 | 工程机械 | 5322659.514 | 90.5407 | 8.1476 | 0.1865 | 1.8158 | 1.1612 | 25.0619 | 46.825 | 41.6 |
| 601106.SH | 中国一重 | 工程机械 | 2146486.0477 | N/A | 4.1557 | N/A | 0.0376 | 0.2421 | 102.3353 | 83.0515 | 33.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 134367179.958 | 10.7784 | 1.6051 | 4.4966 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 68.1 |
| 600036.SH | 招商银行 | 银行 | 95154477.4488 | 6.3122 | 0.8403 | 7.9857 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 601857.SH | 中国石油 | 石油开采 | 166366068.8202 | 10.5173 | 1.0241 | 5.1705 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 61.4 |
| 000333.SZ | 美的集团 | 家用电器 | 60907511.2 | 13.7807 | 2.6218 | 5.2718 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 56.5 |
| 600519.SH | 贵州茅台 | 白酒 | 150873598.3856 | 18.2402 | 5.5695 | 4.3104 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.7 |
| 601088.SH | 中国神华 | 煤炭开采 | 90900419.1513 | 17.6276 | 1.8902 | 6.9621 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 54.9 |
| 601939.SH | 建设银行 | 银行 | 252967568.9105 | 7.4 | 0.7131 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 54.4 |
| 600941.SH | 中国移动 | 电信运营 | 190816527.44 | 14.0507 | 1.3412 | 5.3451 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.1 |
| 601318.SH | 中国平安 | 保险 | 90719286.42 | 6.8321 | 0.8909 | 5.3892 | 2.479 | N/A | -7.3808 | 89.8779 | 52.9 |
| 601398.SH | 工商银行 | 银行 | 253761255.0552 | 6.8335 | 0.6436 | 4.3581 | 2.0286 | N/A | 3.3093 | 92.1901 | 49.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.