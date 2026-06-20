# Dividend defensive verification context for 605499.SH as of 2026-06-20

Status: triggered
Defensive Dividend Rating: strong
- Company: 东鹏饮料
- Industry: 软饮料
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
| dv_ttm | 3.1892 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 10 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 0.5459 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260618 | 120.6 | 18.8686 | 4.3263 | 3.1892 | 8854443.558 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 7.5 | 3 |
| 20250630 | 7.5 | 3 |
| 20241231 | 7.5 | 3 |
| 20240630 | 7.5 | 3 |
| 20231231 | 7.5 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 20875273117.52 | 4415263147.79 | 6174239867.75 | 2269157969.98 | 2677991860.78 | 3905081897.77 | 0.6065 |
| 20241231 | 15838851828.27 | 3326708852.44 | 5789408508.54 | 1687480710.01 | 2051247908.98 | 4101927798.53 | 0.6166 |
| 20231231 | 11262794083.29 | 2039772803.92 | 3281269652.65 | 917723628.09 | 811027574.58 | 2363546024.56 | 0.3976 |
| 20221231 | 8505389730.5 | 1440520571.36 | 2026105140.73 | 792692471.88 | 603452404.47 | 1233412668.85 | 0.4189 |
| 20211231 | 6977822474.41 | 1192960407.59 | 2076844037.67 | 609483991.45 | 626666079.81 | 1467360046.22 | 0.5253 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603156.SH | 养元饮品 | 软饮料 | 5756948.0768 | 40.3862 | 5.8088 | 3.2837 | 8.5341 | 7.715 | 25.7953 | 23.2556 | 73.4 |
| 000848.SZ | 承德露露 | 软饮料 | 783360.0768 | 11.8675 | 2.1109 | 6.5104 | 6.8995 | 5.9902 | 15.3092 | 31.6502 | 72.2 |
| 605499.SH | 东鹏饮料 | 软饮料 | 8854443.558 | 18.8686 | 4.3263 | 3.1892 | 8.4144 | 4.7439 | 28.3072 | 44.4817 | 65.4 |
| 600300.SH | 维维股份 | 软饮料 | 481908.3756 | 13.8562 | 1.3 | 3.4899 | 2.296 | 2.1653 | 18.6905 | 23.4332 | 60.9 |
| 603711.SH | 香飘飘 | 软饮料 | 509073.7653 | 24.5448 | 1.4218 | 2.0276 | 2.6427 | 2.1921 | 597.4136 | 31.6641 | 57.4 |
| 600189.SH | 泉阳泉 | 软饮料 | 547126.317 | 273.3991 | 4.4253 | N/A | 0.8156 | 0.9887 | 96.5545 | 65.2028 | 40.3 |
| 300997.SZ | 欢乐家 | 软饮料 | 678993.4774 | 144.2151 | 6.2939 | 1.2318 | 3.4987 | 2.7586 | 8.4879 | 42.6314 | 38.3 |
| 605198.SH | 安德利 | 软饮料 | 2730315.96 | 86.1335 | 9.5719 | 0.306 | 2.5819 | 2.7201 | -15.521 | 3.7664 | 36.9 |
| 600962.SH | 国投中鲁 | 软饮料 | 683319.26 | 376.0827 | 7.2156 | N/A | 0.4492 | 0.5439 | -84.2321 | 58.4457 | 25.3 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 175334096.7324 | 11.0842 | 1.0793 | 4.9061 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600938.SH | 中国海油 | 石油开采 | 145916958.78 | 11.7049 | 1.7431 | 4.1407 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 93969144.7056 | 6.2336 | 0.8298 | 8.0864 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅台 | 白酒 | 151884914.4 | 18.3624 | 5.6068 | 4.258 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 59.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 89490605.9218 | 17.3542 | 1.8609 | 7.0718 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 56.2 |
| 601318.SH | 中国平安 | 保险 | 89415536.196 | 6.7339 | 0.8781 | 5.4678 | 2.479 | N/A | -7.3808 | 89.8779 | 55.3 |
| 600941.SH | 中国移动 | 电信运营 | 198691836.642 | 14.6306 | 1.3965 | 5.1322 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600028.SH | 中国石化 | 石油加工 | 56955917.1882 | 16.0209 | 0.6836 | 4.2477 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 52.8 |
| 601398.SH | 工商银行 | 银行 | 255186880.0836 | 6.8719 | 0.6472 | 4.3338 | 2.0286 | N/A | 3.3093 | 92.1901 | 52.2 |
| 600900.SH | 长江电力 | 水力发电 | 65232268.3882 | 18.0784 | 2.8623 | 3.5371 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.