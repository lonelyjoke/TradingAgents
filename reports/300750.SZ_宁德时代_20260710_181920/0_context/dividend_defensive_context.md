# Dividend defensive verification context for 300750.SZ as of 2026-07-10

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
| dv_ttm | 2.2672 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6223 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260710 | 348.76 | 20.4313 | 4.5165 | 2.2672 | 161359073.3008 |

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
| 605117.SH | 德业股份 | 电气设备 | 10695140.4 | 29.2767 | 9.2493 | 2.4689 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 72.7 |
| 300750.SZ | 宁德时代 | 电气设备 | 161359073.3008 | 20.4313 | 4.5165 | 2.2672 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 69.9 |
| 600406.SH | 国电南瑞 | 电气设备 | 17701990.6648 | 21.2762 | 3.3092 | 2.8064 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 59.5 |
| 600089.SH | 特变电工 | 电气设备 | 10135901.9556 | 16.4313 | 1.4086 | 1.7831 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 54.7 |
| 600875.SH | 东方电气 | 电气设备 | 9731825.8842 | 22.8289 | 2.0758 | 1.4321 | 3.4423 | 1.1117 | 37.4091 | 69.4679 | 51.9 |
| 300274.SZ | 阳光电源 | 电气设备 | 23798394.8085 | 19.9544 | 4.8907 | 1.4163 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 48.1 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 11940093.1686 | 26.655 | 2.734 | 0.8439 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 46.3 |
| 002028.SZ | 思源电气 | 电气设备 | 11873984.6809 | 36.495 | 7.3671 | 0.4613 | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 42.3 |
| 601727.SH | 上海电气 | 电气设备 | 10598362.9312 | 81.8813 | 1.9308 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 38 |
| 002202.SZ | 金风科技 | 电气设备 | 9444391.5332 | 30.3356 | 2.375 | 0.6258 | 2.0584 | 0.8766 | 59.6477 | 71.1004 | 36.6 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 169660446.4206 | 10.7255 | 1.0444 | 5.0701 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64 |
| 600036.SH | 招商银 | 银行 | 93010790.5728 | 6.17 | 0.8214 | 5.4664 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 600938.SH | 中国海 | 石油开采 | 133796820.51 | 10.7327 | 1.5983 | 4.0672 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 60.5 |
| 000333.SZ | 美的集团 | 家用电器 | 60138553.8711 | 13.6067 | 2.5887 | 5.3392 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 59.8 |
| 600519.SH | 贵州茅台 | 白酒 | 150632332.6368 | 18.211 | 5.5606 | 4.3173 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.4 |
| 601939.SH | 建设银行 | 银行 | 262385182.6445 | 7.6755 | 0.7397 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 56.2 |
| 601318.SH | 中国平安 | 保险 | 89596612.616 | 6.7475 | 0.8799 | 5.4568 | 2.479 | N/A | -7.3808 | 89.8779 | 55.2 |
| 600941.SH | 中国移动 | 电信运营 | 195109899.3074 | 14.3668 | 1.3713 | 5.2275 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.4 |
| 600028.SH | 中国石化 | 石油加工 | 57560544.7592 | 16.191 | 0.6909 | 4.2031 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 51.2 |
| 601328.SH | 交通银 | 银行 | 58408461.3714 | 6.0582 | 0.5017 | 4.9123 | 2.044 | N/A | 3.1137 | 92.0004 | 49.8 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.