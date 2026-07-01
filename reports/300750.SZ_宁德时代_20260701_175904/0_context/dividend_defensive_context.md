# Dividend defensive verification context for 300750.SZ as of 2026-07-01

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
| dv_ttm | 2.06 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.6223 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260701 | 383.84 | 22.4863 | 4.9708 | 2.06 | 177588454.6064 |

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
| 300750.SZ | 宁德时代 | 电气设备 | 177588454.6064 | 22.4863 | 4.9708 | 2.06 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 72.4 |
| 605117.SH | 德业股份 | 电气设备 | 12921992.405 | 35.3725 | 11.1751 | 2.0434 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 69.2 |
| 600406.SH | 国电南瑞 | 电气设备 | 18207991.3054 | 21.8844 | 3.4038 | 2.7284 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 63 |
| 600089.SH | 特变电工 | 电气设备 | 11247516.3276 | 18.2334 | 1.5631 | 1.1159 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 55 |
| 300274.SZ | 阳光电源 | 电气设备 | 28386411.858 | 23.8013 | 5.8335 | 1.1874 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 52.6 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 13746102.8925 | 30.6867 | 3.1475 | 0.7331 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 50.9 |
| 002028.SZ | 思源电气 | 电气设备 | 12972717.5941 | 39.8719 | 8.0488 | 0.2999 | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 44.1 |
| 002202.SZ | 金风科技 | 电气设备 | 10415862.9342 | 33.456 | 2.6193 | 0.5675 | 2.0584 | 0.8766 | 59.6477 | 71.1004 | 40.2 |
| 601727.SH | 上海电气 | 电气设备 | 10893625.2416 | 84.1624 | 1.9846 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 39 |
| 601012.SH | 隆基绿能 | 电气设备 | 9995469.054 | N/A | 1.9804 | N/A | -3.6495 | -1.3384 | -34.1976 | 66.0778 | 33.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 128425935.708 | 10.3018 | 1.5342 | 4.7046 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 68.1 |
| 600036.SH | 招商银行 | 银行 | 90564465.5496 | 6.0077 | 0.7998 | 8.3904 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 601857.SH | 中国石油 | 石油开采 | 159777313.6194 | 10.1007 | 0.9835 | 5.3837 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 61.4 |
| 000333.SZ | 美的集团 | 家用电器 | 58928017.086 | 13.3328 | 2.5366 | 5.4489 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 57.5 |
| 601939.SH | 建设银行 | 银行 | 250351565.0955 | 7.3235 | 0.7057 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 54.4 |
| 601088.SH | 中国神华 | 煤炭开采 | 85629886.6164 | 16.6056 | 1.7806 | 7.3906 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 54.3 |
| 600519.SH | 贵州茅台 | 白酒 | 149135984.9616 | 18.0301 | 5.5053 | 4.3607 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 54.1 |
| 600028.SH | 中国石化 | 石油加工 | 54900183.4468 | 15.4427 | 0.659 | 4.4067 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 53.6 |
| 601318.SH | 中国平安 | 保险 | 89687150.826 | 6.7544 | 0.8807 | 5.4512 | 2.479 | N/A | -7.3808 | 89.8779 | 53.5 |
| 600941.SH | 中国移动 | 电信运营 | 187505258.6052 | 13.8068 | 1.3179 | 5.4384 | 2.084 | 1.759 | -4.2082 | 33.7319 | 51.5 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.