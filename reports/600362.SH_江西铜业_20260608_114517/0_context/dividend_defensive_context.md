# Dividend defensive verification context for 600362.SH as of 2026-06-08

Status: triggered
Defensive Dividend Rating: medium
- Company: 江西铜业
- Industry: 铜
- Dividend stability: watch
- Dividend coverage: watch
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
| dv_ttm | 2.4672 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 26 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.2183 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 44.36 | 19.2121 | 1.8263 | 2.4672 | 15360667.6406 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 1.2 | 2 |
| 20250630 | 1.2 | 3 |
| 20241231 | 2.1 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 1.8 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 544623484060 | 7130191864 | -6914101315 | 4587268623 | 6223785717 | -11501369938 | 0.8729 |
| 20241231 | 520928245943 | 6962197980 | 2507849798 | 6590553753 | 4933734824 | -4082703955 | 0.7086 |
| 20231231 | 521892512166 | 6505109122 | 10931174473 | 6811373319 | 3796957926 | 4119801154 | 0.5837 |
| 20221231 | 479938045193 | 5993964274 | 10641320122 | 5315447024 | 2520835167 | 5325873098 | 0.4206 |
| 20211231 | 442767670161 | 5635567528 | 9031634346 | 2871469217 | 1612596904 | 6160165129 | 0.2861 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601899.SH | 紫金矿业 | 铜 | 78788287.425 | 12.7717 | 3.9938 | 1.6835 | 10.4049 | 5.9878 | 97.5001 | 51.3712 | 73 |
| 601168.SH | 西部矿业 | 铜 | 7275299 | 16.4565 | 3.6458 | 3.4065 | 8.2604 | 4.8098 | 96.3409 | 58.5159 | 72 |
| 600362.SH | 江西铜业 | 铜 | 15360667.6406 | 19.2121 | 1.8263 | 2.4672 | 3.4073 | 1.8078 | 44.3105 | 62.4705 | 66.5 |
| 000630.SZ | 铜陵有色 | 铜 | 8702747.01 | 33.1583 | 2.3216 | 2.2372 | 3.5947 | 3.1584 | 19.1171 | 54.3423 | 62 |
| 603979.SH | 金诚信 | 铜 | 4463209.6367 | 17.7234 | 3.8987 | 0.6289 | 5.2814 | 3.8512 | 42.5546 | 47.8093 | 49 |
| 000737.SZ | 北方铜业 | 铜 | 2639936.9789 | 25.518 | 3.5504 | 0.7937 | 8.6465 | 4.8696 | 65.7394 | 64.6004 | 48.5 |
| 000878.SZ | 云南铜业 | 铜 | 4200418.7573 | 29.6387 | 2.3505 | 1.3279 | 3.9987 | 1.8822 | 7.9318 | 65.4474 | 43.5 |
| 002203.SZ | 海亮股份 | 铜 | 4363502.0417 | 42.1895 | 2.5579 | 1.299 | 2.5741 | 1.4723 | 26.4155 | 62.2225 | 42 |
| 601212.SH | 白银有色 | 铜 | 4472483.8046 | N/A | 2.8138 | 0.0662 | 0.9864 | 1.5995 | 440.2347 | 69.9131 | 33 |
| 688102.SH | 斯瑞新材 | 铜 | 2922975.1205 | 184.5956 | 14.9691 | 0.2056 | 2.2162 | 1.3 | 33.2412 | 42.7233 | 30.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600036.SH | 招商银行 | 银行 | 97298164.3287 | 6.4544 | 0.8592 | 7.8097 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 000333.SZ | 美的集团 | 家用电器 | 62192502.4029 | 14.0714 | 2.669 | 4.904 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.9 |
| 600028.SH | 中国石化 | 石油加工 | 59132576.4546 | 16.6332 | 0.7098 | 4.6665 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 105237135.243 | 20.4078 | 2.1011 | 6.0136 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 57.4 |
| 600519.SH | 贵州茅台 | 白酒 | 159117886.6649 | 19.2369 | 5.9396 | 4.0644 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 56.6 |
| 600941.SH | 中国移动 | 电信运营 | 211005744.6669 | 15.5373 | 1.5345 | 4.8327 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.3 |
| 601857.SH | 中国石油 | 石油开采 | 194185257.4649 | 12.2262 | 1.1953 | 4.4298 | N/A | N/A | N/A | N/A | 53.1 |
| 600900.SH | 长江电力 | 水力发电 | 67556749.1139 | 18.7226 | 2.9643 | 3.4154 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 53 |
| 601318.SH | 中国平安 | 保险 | 96839669.3893 | 7.293 | 0.951 | 4.8055 | 2.479 | N/A | -7.3808 | 89.8779 | 52.1 |
| 601288.SH | 农业银行 | 银行 | 222589209.5432 | 7.5635 | 0.8004 | 3.923 | 2.3014 | N/A | 4.5238 | 93.5269 | 51.2 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.