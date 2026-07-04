# Dividend defensive verification context for 300274.SZ as of 2026-07-04

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
| dv_ttm | 1.2887 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 23 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.7482 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260703 | 126.16 | 21.9309 | 5.3751 | 1.2887 | 26155636.284 |

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
| 605117.SH | 德业股份 | 电气设备 | 12279039.764 | 33.6125 | 10.6191 | 2.1504 | 10.8612 | 6.4643 | 68.3658 | 47.1349 | 72.7 |
| 300750.SZ | 宁德时代 | 电气设备 | 175811829.8 | 22.2613 | 4.9211 | 2.0808 | 5.9731 | 2.4673 | 48.5237 | 62.3223 | 69.9 |
| 600406.SH | 国电南瑞 | 电气设备 | 18384689.9418 | 22.0968 | 3.4368 | 2.7022 | 1.3591 | 0.8753 | 6.0424 | 40.195 | 59.5 |
| 600875.SH | 东方电气 | 电气设备 | 9991202.9067 | 23.4374 | 2.1311 | 1.3949 | 3.4423 | 1.1117 | 37.4091 | 69.4679 | 53.7 |
| 300274.SZ | 阳光电源 | 电气设备 | 26155636.284 | 21.9309 | 5.3751 | 1.2887 | 4.81 | 2.1505 | -40.1157 | 57.5148 | 50.9 |
| 600089.SH | 特变电工 | 电气设备 | 11121196.5126 | 18.0286 | 1.5456 | 1.1285 | 2.4026 | 1.2267 | 13.3952 | 56.5765 | 50.1 |
| 300014.SZ | 亿纬锂能 | 电气设备 | 13291883.8404 | 29.6728 | 3.0435 | 0.7581 | 3.3523 | 1.3373 | 31.3489 | 64.8881 | 46.3 |
| 002028.SZ | 思源电气 | 电气设备 | 13119841.3745 | 40.3241 | 8.1401 | 0.2966 | 3.4795 | 2.1281 | 23.1699 | 45.8498 | 42.3 |
| 002202.SZ | 金风科技 | 电气设备 | 10386296.4133 | 33.361 | 2.6119 | 0.5691 | 2.0584 | 0.8766 | 59.6477 | 71.1004 | 37.6 |
| 601727.SH | 上海电气 | 电气设备 | 10815924.6336 | 83.5621 | 1.9704 | N/A | 0.6943 | 0.3477 | 30.1534 | 75.4984 | 37 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 131610442.626 | 10.5573 | 1.5722 | 4.5908 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 68.1 |
| 600036.SH | 招商银行 | 银行 | 92884691.3448 | 6.1616 | 0.8203 | 8.1808 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 601857.SH | 中国石油 | 石油开采 | 164169817.0866 | 10.3784 | 1.0106 | 5.2397 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 61.4 |
| 000333.SZ | 美的集团 | 家用电器 | 59354369.6644 | 13.4293 | 2.555 | 5.4098 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 58.1 |
| 600519.SH | 贵州茅台 | 白酒 | 149315996.712 | 18.0518 | 5.512 | 4.3554 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.7 |
| 601939.SH | 建设银行 | 银行 | 248258762.0435 | 7.2623 | 0.6998 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 54.4 |
| 601088.SH | 中国神华 | 煤炭开采 | 88275997.601 | 17.1187 | 1.8356 | 7.1691 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 54.3 |
| 601318.SH | 中国平安 | 保险 | 88890414.578 | 6.6944 | 0.8729 | 5.5001 | 2.479 | N/A | -7.3808 | 89.8779 | 53.5 |
| 600941.SH | 中国移动 | 电信运营 | 189651520.6704 | 13.9649 | 1.333 | 5.3769 | 2.084 | 1.759 | -4.2082 | 33.7319 | 51.5 |
| 600028.SH | 中国石化 | 石油加工 | 56834991.674 | 15.9869 | 0.6822 | 4.2567 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 49.4 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.