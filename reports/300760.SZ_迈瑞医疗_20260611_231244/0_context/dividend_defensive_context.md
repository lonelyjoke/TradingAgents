# Dividend defensive verification context for 300760.SZ as of 2026-06-11

Status: triggered
Defensive Dividend Rating: medium
- Company: 迈瑞医疗
- Industry: 医疗保健
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: watch
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 2.8731 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 21 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0185 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260611 | 146.88 | 22.7238 | 4.6596 | 2.8731 | 17808339.1951 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20260331 | 3.75 | 3 |
| 20251231 | 0.93 | 3 |
| 20250930 | 2.7 | 2 |
| 20250630 | 2.62 | 2 |
| 20250331 | 2.82 | 2 |
| 20241231 | 1.68 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 33282159404 | 8135775409 | 10144968535 | 2037744137 | 5743047401 | 8107224398 | 0.7059 |
| 20241231 | 36725749548 | 11668487164 | 12432041281 | 1959448254 | 8843406846 | 10472593027 | 0.7579 |
| 20231231 | 34931900884 | 11582226085 | 11062025295 | 2688667990 | 10669617132 | 8373357305 | 0.9212 |
| 20221231 | 30365643811 | 9607174094 | 12141147876 | 1915528356 | 4233373015 | 10225619520 | 0.4406 |
| 20211231 | 25269580818 | 8001553606 | 8998649175 | 1402493907 | 3039228165 | 7596155268 | 0.3798 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300760.SZ | 迈瑞医疗 | 医疗保健 | 17808339.1951 | 22.7238 | 4.6596 | 2.8731 | 5.9579 | 4.0936 | -11.372 | 24.7744 | 69.5 |
| 300832.SZ | 新产业 | 医疗保健 | 3437519.6844 | 21.1575 | 4.0223 | 2.7362 | 4.7445 | 4.9519 | 1.0238 | 7.1408 | 69.5 |
| 300015.SZ | 爱尔眼科 | 医疗保健 | 7842658.5995 | 23.2645 | 3.4032 | 0.948 | 5.2448 | 4.4329 | 12.4619 | 32.7198 | 64.5 |
| 002432.SZ | 九安医疗 | 医疗保健 | 2876428.8213 | 12.5389 | 1.3745 | 2.4059 | 1.3511 | 1.3238 | 10.2339 | 27.0243 | 59 |
| 688617.SH | 惠泰医疗 | 医疗保健 | 2825771.2485 | 32.5954 | 9.8412 | 0.4925 | 7.575 | 7.4343 | 25.2725 | 12.3422 | 57.5 |
| 300896.SZ | 爱美客 | 医疗保健 | 2800186.9325 | 24.4444 | 3.6702 | 2.1529 | 3.8597 | 3.9177 | -32.7864 | 7.4337 | 54.5 |
| 300347.SZ | 泰格医药 | 医疗保健 | 3418273.4185 | 44.3089 | 1.6343 | 0.7496 | 0.2342 | 1.4979 | -70.3611 | 14.7066 | 45.5 |
| 688301.SH | 奕瑞科技 | 医疗保健 | 3511966.4894 | 51.2206 | 5.6445 | 0.4069 | 2.8203 | 1.63 | 24.9063 | 47.7679 | 41 |
| 688271.SH | 联影医疗 | 医疗保健 | 9248700.9413 | 48.7264 | 4.2112 | 0.1862 | 1.8325 | 1.5275 | 7.7786 | 33.9651 | 36 |
| 300677.SZ | 英科医疗 | 医疗保健 | 3028233.8414 | 45.3322 | 1.6653 | 0.3227 | 0.055 | 0.2342 | -97.1562 | 53.9218 | 23 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 160746304.3739 | 12.8945 | 1.9203 | 3.7587 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.7 |
| 600036.SH | 招商银行 | 银行 | 97676462.0127 | 6.4795 | 0.8626 | 7.7795 | 2.9627 | N/A | 1.518 | 90.4294 | 60.9 |
| 601857.SH | 中国石油 | 石油开采 | 189792753.9973 | 11.9497 | 1.1683 | 4.5323 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.3 |
| 600028.SH | 中国石化 | 石油加工 | 57923321.3123 | 16.293 | 0.6952 | 4.764 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 60 |
| 600519.SH | 贵州茅台 | 白酒 | 159885436.7679 | 19.3297 | 5.9682 | 4.0449 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 102569334.8236 | 19.8905 | 2.0478 | 6.1701 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 000333.SZ | 美的集团 | 家用电器 | 64980701.0712 | 14.7023 | 2.7898 | 4.6936 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 55.3 |
| 600941.SH | 中国移动 | 电信运营 | 208057344.2483 | 15.3202 | 1.5131 | 4.9012 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.4 |
| 601318.SH | 中国平安 | 保险 | 95318627.4617 | 7.1785 | 0.9661 | 5.1292 | 2.479 | N/A | -7.3808 | 89.8779 | 53.1 |
| 600900.SH | 长江电力 | 水力发电 | 68241859.2099 | 18.9125 | 2.9943 | 3.3811 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.