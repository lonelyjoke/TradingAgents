# Dividend defensive verification context for 300750.SZ as of 2026-06-28

Status: triggered
Defensive Dividend Rating: medium
- Company: 宁德时代
- Industry: 电气设备
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
| dv_ttm | 2.0753 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6223 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260626 | 381 | 22.3199 | 4.934 | 2.0753 | 176274492.51 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 20.871 | 3 |
| 20250630 | 2.014 | 2 |
| 20241231 | 11.346 | 3 |
| 20241211 | 3.69 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 9.05 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 423701834000 | 72201282000 | 133219982000 | 42344558000 | 34923036000 | 90875424000 | 0.4837 |
| 20241231 | 362012554000 | 50744682000 | 96990345000 | 31179943000 | 25807432000 | 65810402000 | 0.5086 |
| 20231231 | 400917044900 | 44121248300 | 92826124400 | 33624896500 | 9481092900 | 59201227900 | 0.2149 |
| 20221231 | 328593987500 | 30729163500 | 61208843300 | 48215268100 | 3551469400 | 12993575200 | 0.1156 |
| 20211231 | 130355796400 | 15931317900 | 42908008700 | 43767770800 | 1568025100 | -859762100 | 0.0984 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 605117.SH | 德业股份 | 电气设备 | 12284167.9523 | 33.6265 | 10.6235 | 2.1495 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 72.7 |
| 300750.SZ | 宁德时代 | 电气设备 | 176274492.51 | 22.3199 | 4.934 | 2.0753 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 69.9 |
| 600406.SH | 国电南瑞 | 电气设备 | 18264213.5988 | 21.952 | 3.4143 | 2.5486 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 59.5 |
| 600875.SH | 东方电气 | 电气设备 | 9845951.7741 | 23.0966 | 2.1001 | 1.4155 | 3.4423 | 1.1117 | 37.4091 | 69.4679 | 53.7 |
| 600089.SH | 特变电工 | 电气设备 | 11343519.387 | 18.389 | 1.5764 | 1.1064 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 52.9 |
| 300274.SZ | 阳光电源 | 电气设备 | 31315859.7075 | 26.2576 | 6.4356 | 1.0763 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 48.1 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 13520080.0149 | 30.1822 | 3.0958 | 0.7453 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 45.3 |
| 002028.SZ | 思源电气 | 电气设备 | 13702285.0992 | 42.1143 | 8.5015 | 0.284 | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 43.3 |
| 002202.SZ | 金风科技 | 电气设备 | 9854099.0371 | 31.6516 | 2.4781 | 0.5998 | 2.0584 | 0.8766 | 59.6477 | 71.1004 | 37.6 |
| 601727.SH | 上海电气 | 电气设备 | 10629443.1744 | 82.1214 | 1.9364 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 37 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 130089484.098 | 10.4353 | 1.554 | 4.6444 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 69.1 |
| 601857.SH | 中国石 | 石油开采 | 163437733.1754 | 10.3321 | 1.0061 | 5.2632 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600036.SH | 招商银行 | 银行 | 90791444.16 | 6.0228 | 0.8018 | 8.3694 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅 | 白酒 | 146088286.0208 | 17.6616 | 5.3928 | 4.4516 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 59.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 85825091.5251 | 16.6434 | 1.7847 | 7.3738 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 56.2 |
| 601318.SH | 中国平安 | 保险 | 85522393.166 | 6.4407 | 0.8398 | 5.7167 | 2.479 | N/A | -7.3808 | 89.8779 | 55.3 |
| 600941.SH | 中国移动 | 电信运营 | 188220679.2936 | 13.8595 | 1.3229 | 5.4178 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600028.SH | 中国石化 | 石油加工 | 54658332.4184 | 15.3746 | 0.6561 | 4.4262 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 53.8 |
| 600900.SH | 长江电力 | 水力发电 | 65207800.1705 | 18.0716 | 2.8612 | 3.5385 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |
| 601288.SH | 农业银行 | 银行 | 216639497.9841 | 7.3613 | 0.7664 | 4.0307 | 2.3014 | N/A | 4.5238 | 93.5269 | 49.7 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.