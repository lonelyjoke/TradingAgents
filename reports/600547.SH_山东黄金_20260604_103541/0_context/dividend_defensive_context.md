# Dividend defensive verification context for 600547.SH as of 2026-06-04

Status: triggered
Defensive Dividend Rating: weak
- Company: 山东黄金
- Industry: 黄金
- Dividend stability: fail
- Dividend coverage: watch
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
| dv_ttm | 1.0979 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 26 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 0.8801 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260603 | 29.39 | 26.2628 | 4.2333 | 1.0979 | 13548582.874 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.18 | 1 |
| 20250630 | 0.3547 | 2 |
| 20241231 | 0.444 | 3 |
| 20240630 | 0.24 | 3 |
| 20231231 | 0.42 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 104287391583.12 | 4739393120.72 | 21492754843.56 | 12928502009.1 | 4884773968.89 | 8564252834.46 | 1.0307 |
| 20241231 | 82517993538.3 | 2951551189.32 | 13339797529.06 | 20102968313.79 | 4191121094.68 | -6763170784.73 | 1.42 |
| 20231231 | 59275274514.67 | 2327750542.04 | 6848761658.51 | 9181251886.67 | 2508518210.17 | -2332490228.16 | 1.0777 |
| 20221231 | 50305754258.45 | 1245858630.24 | 2971775379.32 | 4214148974.24 | 1901175239.81 | -1242373594.92 | 1.526 |
| 20211231 | 33934960452.94 | -193687290.91 | 1822242735.09 | 3555902588.2 | 1352546474.93 | -1733659853.11 | 6.9831 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000975.SZ | 山金国际 | 黄金 | 6326907.609 | 17.2317 | 4.2733 | 2.1052 | 8.9473 | 9.2482 | 100.8885 | 22.6432 | 71.5 |
| 600489.SH | 中金黄金 | 黄金 | 11211833.9605 | 17.8657 | 3.4185 | 1.6775 | 7.5424 | 5.499 | 129.2346 | 43.013 | 67.9 |
| 000506.SZ | 招金黄金 | 黄金 | 1317347.1851 | 37.7065 | 14.8167 | N/A | 23.6036 | 14.1635 | 6136.2107 | 37.0877 | 57 |
| 001337.SZ | 四川黄金 | 黄金 | 2079000 | 32.7168 | 10.9857 | 1.0101 | 13.5072 | 9.7768 | 176.9309 | 38.3295 | 54.3 |
| 601069.SH | 西部黄金 | 黄金 | 2498870.5944 | 26.0633 | 4.7537 | N/A | 10.4621 | 4.5047 | 2102.762 | 65.5555 | 53 |
| 600988.SH | 赤峰黄金 | 黄金 | 6356875.3904 | 17.721 | 4.6465 | 0.9567 | 7.1342 | 6.7568 | 104.4289 | 29.3577 | 51.2 |
| 600547.SH | 山东黄金 | 黄金 | 13548582.874 | 26.2628 | 4.2333 | 1.0979 | 3.1815 | 2.3103 | 40.8737 | 62.5682 | 48.4 |
| 300139.SZ | 晓程科技 | 黄金 | 1191078 | 64.2707 | 9.9962 | N/A | 3.8001 | 4.0054 | 307.9568 | 19.9835 | 46.5 |
| 002155.SZ | 湖南黄金 | 黄金 | 3981635.5532 | 22.7364 | 4.5702 | 0.6944 | 7.0777 | 7.1826 | 79.2052 | 12.8256 | 43.1 |
| 002237.SZ | 恒邦股份 | 黄金 | 1987658.8671 | 29.9475 | 1.4751 | 0.8144 | 1.3629 | 0.878 | 14.5583 | 65.8274 | 27.1 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 172438673.054 | 13.8324 | 2.0599 | 3.5038 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 601857.SH | 中国石油 | 石油开采 | 198577760.9325 | 12.5028 | 1.2224 | 4.3318 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.9 |
| 600036.SH | 招商银行 | 银行 | 97096405.5639 | 6.441 | 0.8575 | 7.826 | 2.9627 | N/A | 1.518 | 90.4294 | 60.3 |
| 000333.SZ | 美的集团 | 家用电器 | 62889821.9619 | 14.2292 | 2.6992 | 4.8497 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60 |
| 600028.SH | 中国石化 | 石油加工 | 58769799.9119 | 16.5311 | 0.7054 | 4.6954 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 56.6 |
| 600519.SH | 贵州茅台 | 白酒 | 160249210.5138 | 19.3736 | 5.9818 | 4.0357 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 105952886.575 | 20.5466 | 2.1154 | 5.973 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | 中国移动 | 电信运营 | 217038851.0698 | 15.9815 | 1.5255 | 4.7864 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.4 |
| 601318.SH | 中国平安 | 保险 | 97238037.5132 | 7.323 | 0.9549 | 4.7858 | 2.479 | N/A | -7.3808 | 89.8779 | 50.6 |
| 600900.SH | 长江电力 | 水力发电 | 68241859.2099 | 18.9125 | 2.9943 | 3.3811 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.