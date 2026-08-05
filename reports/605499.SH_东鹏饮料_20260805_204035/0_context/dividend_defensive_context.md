# Dividend defensive verification context for 605499.SH as of 2026-08-05

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
| dv_ttm | 3.1387 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 10 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 0.5459 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260805 | 122.54 | 18.3336 | 4.6196 | 3.1387 | 8996878.3447 |

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
| 603156.SH | 养元饮品 | 软饮料 | 5680071.1432 | 39.8469 | 5.7312 | 3.3282 | 8.5341 | 7.715 | 25.7953 | 23.2556 | 77 |
| 000848.SZ | 承德露露 | 软饮料 | 916980.0899 | 13.8918 | 2.4709 | 5.5617 | 6.8995 | 5.9902 | 15.3092 | 31.6502 | 72.2 |
| 605499.SH | 东鹏饮料 | 软饮料 | 8996878.3447 | 18.3336 | 4.6196 | 3.1387 | 8.4144 | 4.7439 | 28.3072 | 44.4817 | 63.7 |
| 600300.SH | 维维股份 | 软饮料 | 514251.2196 | 14.7861 | 1.3872 | 3.2704 | 2.296 | 2.1653 | 18.6905 | 23.4332 | 56.7 |
| 603711.SH | 香飘飘 | 软饮料 | 463244.7402 | 22.3352 | 1.2938 | 0.6239 | 2.6427 | 2.1921 | 597.4136 | 31.6641 | 54.4 |
| 600189.SH | 泉阳泉 | 软饮料 | 526385.5808 | 263.0349 | 4.2576 | N/A | 0.8156 | 0.9887 | 96.5545 | 65.2028 | 41.9 |
| 300997.SZ | 欢乐家 | 软饮料 | 782082.1732 | 166.1107 | 7.2495 | 1.0695 | 3.4987 | 2.7586 | 8.4879 | 42.6314 | 41.3 |
| 605198.SH | 安德利 | 软饮料 | 2052248.508 | 64.7425 | 7.1947 | 0.4885 | 2.5819 | 2.7201 | -15.521 | 3.7664 | 40.2 |
| 600962.SH | 国投中鲁 | 软饮料 | 757000.27 | 416.635 | 7.9937 | N/A | 0.4492 | 0.5439 | -84.2321 | 58.4457 | 22.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600036.SH | 招商银行 | 银行 | 98206078.7664 | 6.5146 | 0.8673 | 5.1772 | 2.9627 | N/A | 1.518 | 90.4294 | 61.9 |
| 601857.SH | 中国石油 | 石油开采 | 194551299.4014 | 12.2991 | 1.1976 | 4.4215 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.6 |
| 000333.SZ | 美的集团 | 家用电器 | 65072062.2783 | 14.7229 | 2.8011 | 4.9241 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.5 |
| 600938.SH | 中国海油 | 石油开采 | 145869428.826 | 11.7011 | 1.7426 | 3.7306 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 57.7 |
| 601318.SH | 中国平安 | 保险 | 97817482.084 | 7.3667 | 0.9606 | 4.9981 | 2.479 | N/A | -7.3808 | 89.8779 | 55.8 |
| 600519.SH | 贵州茅台 | 白酒 | 163316910.632 | 19.7445 | 6.0288 | 3.982 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 53.4 |
| 600941.SH | 中国移动 | 电信运营 | 208175569.1058 | 15.3289 | 1.4632 | 4.9002 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.2 |
| 601328.SH | 交通银行 | 银行 | 61236102.4665 | 6.3515 | 0.526 | 4.6855 | 2.044 | N/A | 3.1137 | 92.0004 | 50.9 |
| 600028.SH | 中国石化 | 石油加工 | 60220906.0716 | 16.9393 | 0.7228 | 4.0174 | 2.0481 | 1.2478 | 28.2117 | N/A | 49.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 93264567.49 | 18.0861 | 1.9394 | 4.4478 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 47.9 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.