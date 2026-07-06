# Dividend defensive verification context for 300750.SZ as of 2026-07-06

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
| dv_ttm | 2.1113 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6223 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260706 | 374.51 | 21.9397 | 4.85 | 2.1113 | 173271811.5221 |

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
| 605117.SH | 德业股份 | 电气设备 | 12238296.372 | 33.5009 | 10.5838 | 2.1576 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 72.4 |
| 300750.SZ | 宁德时代 | 电气设备 | 173271811.5221 | 21.9397 | 4.85 | 2.1113 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 69.2 |
| 600406.SH | 国电南瑞 | 电气设备 | 18601547.3592 | 22.3574 | 3.4774 | 2.6707 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 59.5 |
| 600089.SH | 特变电 | 电气设备 | 10787712.201 | 17.488 | 1.4992 | 1.6753 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 54.6 |
| 002028.SZ | 思源电气 | 电气设备 | 13632426.886 | 41.8996 | 8.4581 | N/A | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 53 |
| 600875.SH | 东方电气 | 电气设备 | 10295538.6131 | 24.1513 | 2.196 | 1.3537 | 3.4423 | 1.1117 | 37.4091 | 69.4679 | 50.5 |
| 300274.SZ | 阳光电源 | 电气设备 | 26574425.007 | 22.282 | 5.4612 | 1.2684 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 46.4 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 12902863.6953 | 28.8043 | 2.9544 | 0.781 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 43.2 |
| 601727.SH | 上海电气 | 电气设备 | 10738224.0256 | 82.9618 | 1.9562 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 37 |
| 002202.SZ | 金风科技 | 电气设备 | 10099078.7817 | 32.4385 | 2.5397 | 0.5853 | 2.0584 | 0.8766 | 59.6477 | 71.1004 | 34.1 |

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