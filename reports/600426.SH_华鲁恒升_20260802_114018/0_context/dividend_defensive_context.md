# Dividend defensive verification context for 600426.SH as of 2026-08-02

Status: triggered
Defensive Dividend Rating: medium
- Company: 华鲁恒升
- Industry: 农药化肥
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: fail
- Valuation buffer: watch
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 1.7857 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 31 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.4614 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260731 | 21.55 | 15.9081 | 1.7344 | 1.7857 | 5926127.165 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.75 | 3 |
| 20250630 | 0.75 | 3 |
| 20241231 | 0.9 | 3 |
| 20240630 | 0.9 | 3 |
| 20231231 | 1.8 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 30968875947.12 | 3315494470.04 | 4197555233.55 | 3649994293.98 | 1505113701.24 | 547560939.57 | 0.454 |
| 20241231 | 34226018627.13 | 3902593305.73 | 4968115816.5 | 5080715840.91 | 2217930893.11 | -112600024.41 | 0.5683 |
| 20231231 | 27259886885.51 | 3575898630.37 | 4715319211.3 | 8710521976.28 | 1934527810.99 | -3995202764.98 | 0.541 |
| 20221231 | 30245283380.3 | 6289374659.11 | 6999469230.44 | 6970135423.48 | 1818351225.99 | 29333806.96 | 0.2891 |
| 20211231 | 26635860726.65 | 7254167060.52 | 4905799644.81 | 3672388955.91 | 613108758.07 | 1233410688.9 | 0.0845 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000408.SZ | 藏格矿业 | 农药化肥 | 12648591.1176 | 27.0336 | 7.1689 | 3.0979 | 9.2881 | 8.8536 | 110.6045 | 7.0627 | 79.4 |
| 000792.SZ | 盐湖股份 | 农药化肥 | 14456576.3432 | 14.0161 | 3.2345 | N/A | 6.7519 | 7.3136 | 154.784 | 15.8486 | 70.5 |
| 600096.SH | 云天化 | 农药化肥 | 5445273.2209 | 10.2932 | 2.09 | 4.687 | 5.6276 | 3.6525 | 10.3918 | 46.6672 | 67.5 |
| 600426.SH | 华鲁恒升 | 农药化肥 | 5926127.165 | 15.9081 | 1.7344 | 1.7857 | 3.3208 | 2.929 | 57.9648 | 28.9562 | 63.1 |
| 002545.SZ | 东方铁塔 | 农药化肥 | 2331372.3754 | 16.6259 | 2.2821 | 1.6009 | 4.0239 | 3.3902 | 95.213 | 29.7791 | 50.2 |
| 600486.SH | 扬农化工 | 农药化肥 | 2290102.1373 | 18.2035 | 1.9298 | 1.6848 | 3.4888 | 2.5455 | -6.4142 | 37.8841 | 40.9 |
| 600141.SH | 兴发集团 | 农药化肥 | 3469423.0913 | 24.1252 | 1.3869 | 1.7239 | 1.0915 | 1.0061 | -17.3743 | 48.4997 | 39.5 |
| 000893.SZ | 亚钾国际 | 农药化肥 | 4792129.5232 | 26.3208 | 3.449 | 0.2097 | 3.9075 | 3.3365 | 38.52 | 32.5255 | 39.1 |
| 600331.SH | 宏达股份 | 农药化肥 | 3315208 | N/A | 10.6435 | N/A | -1.0758 | -0.9895 | 6.19 | 14.7067 | 36.5 |
| 301035.SZ | 润丰股份 | 农药化肥 | 2062370.9874 | 21.6389 | 2.6829 | 2.0963 | 2.1699 | 1.4451 | -35.6141 | 53.8159 | 33.2 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 202787243.4024 | 12.8197 | 1.2483 | 4.2419 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 62.2 |
| 600036.SH | 招商银行 | 银行 | 99921028.2672 | 6.6284 | 0.8824 | 5.0883 | 2.9627 | N/A | 1.518 | 90.4294 | 61.9 |
| 000333.SZ | 美的集团 | 家用电器 | 66693724.764 | 15.0899 | 2.8709 | 4.8056 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 58.9 |
| 600938.SH | 中国海油 | 石油开采 | 153331631.604 | 12.2997 | 1.8317 | 3.5491 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 57.7 |
| 601318.SH | 中国平安 | 保险 | 99410954.58 | 7.4867 | 0.9762 | 4.918 | 2.479 | N/A | -7.3808 | 89.8779 | 55.8 |
| 600519.SH | 贵州茅台 | 白酒 | 168836020.896 | 20.4118 | 6.2325 | 3.8519 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 54.9 |
| 600941.SH | 中国移动 | 电信运营 | 211220885.6583 | 15.5531 | 1.4846 | 4.8288 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.8 |
| 601328.SH | 交通银行 | 银行 | 63445197.0721 | 6.5806 | 0.545 | 4.5223 | 2.044 | N/A | 3.1137 | 92.0004 | 50.2 |
| 600028.SH | 中国石化 | 石油加工 | 63606820.4692 | 17.8917 | 0.7635 | 3.8035 | 2.0481 | 1.2478 | 28.2117 | N/A | 48.1 |
| 601398.SH | 工商银行 | 银行 | 284768599.4229 | 7.6685 | 0.7223 | 3.8836 | 2.0286 | N/A | 3.3093 | 92.1901 | 47.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.