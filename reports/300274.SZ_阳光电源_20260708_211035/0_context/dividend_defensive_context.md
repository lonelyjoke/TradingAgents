# Dividend defensive verification context for 300274.SZ as of 2026-07-08

Status: triggered
Defensive Dividend Rating: weak
- Company: 阳光电源
- Industry: 电气设备
- Dividend stability: fail
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: fail
- Dividend trap risk: high

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 1.306 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 23 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.7482 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260708 | 124.49 | 21.6406 | 5.304 | 1.306 | 25809409.9635 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 2.07 | 3 |
| 20250630 | 2.85 | 3 |
| 20241231 | 3.24 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 2.895 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 89184357325.77 | 13461279955.37 | 16917778579.11 | 3008018823.6 | 4448237949.52 | 13909759755.51 | 0.3304 |
| 20241231 | 77856966964.63 | 11036278921.36 | 12068326644.66 | 2785952760.93 | 1737973100.43 | 9282373883.73 | 0.1575 |
| 20231231 | 72250674939.46 | 9439561800.25 | 6981838977.28 | 2741238644 | 640318279.02 | 4240600333.28 | 0.0678 |
| 20221231 | 40257239155.34 | 3593410009.26 | 1210498485.89 | 1526766108.85 | 351615275.8 | -316267622.96 | 0.0979 |
| 20211231 | 24136598726.55 | 1582707374.76 | -1638632122.77 | 1665649098.4 | 319225674.3 | -3304281221.17 | 0.2017 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 605117.SH | 德业股份 | 电气设备 | 11404330.067 | 31.2181 | 9.8626 | 2.3154 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 72.4 |
| 300750.SZ | 宁德时代 | 电气设备 | 167022093.88 | 21.1483 | 4.6751 | 2.1903 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 70.8 |
| 600406.SH | 国电南瑞 | 电气设备 | 18079483.2062 | 21.73 | 3.3798 | 2.7478 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 63 |
| 600089.SH | 特变电工 | 电气设备 | 10130849.163 | 16.4231 | 1.4079 | 1.7839 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 55.1 |
| 600875.SH | 东方电气 | 电气设备 | 9583116.3913 | 22.4801 | 2.0441 | 1.4543 | 3.4423 | 1.1117 | 37.4091 | 69.4679 | 49 |
| 300274.SZ | 阳光电源 | 电气设备 | 25809409.9635 | 21.6406 | 5.304 | 1.306 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 46.4 |
| 002028.SZ | 思源电气 | 电气设备 | 12273879.6372 | 37.724 | 7.6152 | 0.4462 | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 45.1 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 12187849.0152 | 27.2081 | 2.7907 | 0.8268 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 44.8 |
| 601727.SH | 上海电气 | 电气设备 | 10520662.3232 | 81.281 | 1.9166 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 40 |
| 601012.SH | 隆基绿能 | 电气设备 | 8896653.1234 | N/A | 1.7627 | N/A | -3.6495 | -1.3384 | -34.1976 | 66.0778 | 33.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 136696147.704 | 10.9653 | 1.633 | 4.42 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 67.2 |
| 601857.SH | 中国石油 | 石油开采 | 169477425.4428 | 10.7139 | 1.0432 | 5.0756 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64 |
| 600036.SH | 招商银行 | 银行 | 95684094.2064 | 6.3473 | 0.845 | 7.9415 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 000333.SZ | 美的集团 | 家用电器 | 60458318.3049 | 13.6791 | 2.6025 | 5.311 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 59.8 |
| 600519.SH | 贵州茅台 | 白酒 | 149922286.288 | 18.1251 | 5.5344 | 4.3378 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.4 |
| 601939.SH | 建设银行 | 银行 | 263431584.1705 | 7.7061 | 0.7426 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 56.2 |
| 601318.SH | 中国平安 | 保险 | 89705258.468 | 6.7557 | 0.8809 | 5.4501 | 2.479 | N/A | -7.3808 | 89.8779 | 55.2 |
| 600941.SH | 中国移动 | 电信运营 | 195044848.2185 | 14.362 | 1.3709 | 5.2292 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.4 |
| 600028.SH | 中国石化 | 石油加工 | 58407023.3586 | 16.4291 | 0.701 | 4.1421 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 51.2 |
| 600900.SH | 长江电力 | 水力发电 | 68095049.8591 | 18.8718 | 2.9879 | 3.3884 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 49.8 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.