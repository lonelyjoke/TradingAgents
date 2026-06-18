# Dividend defensive verification context for 300750.SZ as of 2026-06-16

Status: triggered
Defensive Dividend Rating: medium
- Company: 宁德时代
- Industry: 电气设备
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: fail
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 1.9595 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6223 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260616 | 403.53 | 23.6397 | 5.2258 | 1.9595 | 186698283.3663 |

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
| 605117.SH | 德业股份 | 电气设备 | 13039117.8534 | 35.6931 | 11.2764 | 2.0251 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 72.7 |
| 300750.SZ | 宁德时代 | 电气设备 | 186698283.3663 | 23.6397 | 5.2258 | 1.9595 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 71.4 |
| 600406.SH | 国电南瑞 | 电气设备 | 18906754.0948 | 22.7243 | 3.5344 | 2.462 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 61 |
| 600875.SH | 东方电气 | 电气设备 | 10745125.4521 | 25.2059 | 2.2919 | 1.2971 | 3.4423 | 1.1117 | 37.4091 | 69.4679 | 52.7 |
| 300274.SZ | 阳光电源 | 电气设备 | 31614402.1635 | 26.5079 | 6.4969 | 1.0662 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 52.4 |
| 600089.SH | 特变电工 | 电气设备 | 12182282.9586 | 19.7487 | 1.693 | 1.0302 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 48.1 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 14535009.6672 | 32.4479 | 3.3281 | 0.6933 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 45.8 |
| 002028.SZ | 思源电气 | 电气设备 | 13652208.2235 | 41.9604 | 8.4704 | 0.285 | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 44.6 |
| 601727.SH | 上海电气 | 电气设备 | 11437529.4976 | 88.3646 | 2.0836 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 38.5 |
| 301511.SZ | 德福科技 | 电气设备 | 10692152.086 | 442.6503 | 25.7188 | 0.0587 | 3.5669 | 1.288 | 708.9005 | 76.3695 | 32.8 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 182105872.911 | 11.5123 | 1.121 | 4.7236 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600938.SH | 中国海油 | 石油开采 | 148626166.158 | 11.9222 | 1.7755 | 4.0652 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 97272944.4792 | 6.4527 | 0.859 | 7.8118 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅台 | 白酒 | 156968996.2672 | 18.9771 | 5.7945 | 4.12 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.5 |
| 600028.SH | 中国石化 | 石油加工 | 60099980.5574 | 16.9053 | 0.7214 | 4.5914 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.5 |
| 601318.SH | 中国平安 | 保险 | 95952394.958 | 7.2262 | 0.9423 | 5.0953 | 2.479 | N/A | -7.3808 | 89.8779 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 92223474.6436 | 17.8842 | 1.9177 | 6.8622 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | 中国移动 | 电信运营 | 201596878.2252 | 14.8445 | 1.4169 | 5.0583 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600900.SH | 长江电力 | 水力发电 | 66529083.9263 | 18.4378 | 2.9192 | 3.4682 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |
| 601398.SH | 工商银行 | 银行 | 264453442.7682 | 7.1215 | 0.6707 | 4.1819 | 2.0286 | N/A | 3.3093 | 92.1901 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.