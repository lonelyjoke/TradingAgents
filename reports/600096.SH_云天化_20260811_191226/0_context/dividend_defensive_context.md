# Dividend defensive verification context for 600096.SH as of 2026-08-11

Status: triggered
Defensive Dividend Rating: medium
- Company: 云天化
- Industry: 农药化肥
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: fail
- Valuation buffer: pass
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 4.6933 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 31 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.7609 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260811 | 29.83 | 10.2794 | 2.0873 | 4.6933 | 5437981.2581 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 3.6 | 3 |
| 20250630 | 0.6 | 3 |
| 20241231 | 4.2 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 3 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 48414923741.78 | 5156043643.98 | 9087217375.51 | 2283814042.51 | 3775796292.29 | 6803403333 | 0.7323 |
| 20241231 | 61536936910.62 | 5332959048.01 | 10752130155.74 | 1758979277.85 | 2947409642.62 | 8993150877.89 | 0.5527 |
| 20231231 | 69060212634.49 | 4522198165.85 | 9437165845.79 | 1942822445.25 | 3321304349.83 | 7494343400.54 | 0.7344 |
| 20221231 | 75313292457.62 | 6021322993.75 | 10550590353.01 | 4216517277.84 | 1676355859.45 | 6334073075.17 | 0.2784 |
| 20211231 | 63249227893.71 | 3641935184.27 | 7748770447.56 | 2124192460.19 | 1679093906.28 | 5624577987.37 | 0.461 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000408.SZ | 藏格矿业 | 农药化肥 | 12924720.1224 | 22.7139 | 7.5158 | 3.0318 | 9.2881 | 8.8536 | 110.6045 | 7.0627 | 79.4 |
| 000792.SZ | 盐湖股份 | 农药化肥 | 15176230.2168 | 14.7138 | 3.3955 | N/A | 6.7519 | 7.3136 | 154.784 | 15.8486 | 69 |
| 600096.SH | 云天化 | 农药化肥 | 5437981.2581 | 10.2794 | 2.0873 | 4.6933 | 5.6276 | 3.6525 | 10.3918 | 46.6672 | 67.5 |
| 600426.SH | 华鲁恒升 | 农药化肥 | 5774880.3 | 15.5021 | 1.6901 | 1.8325 | 3.3208 | 2.929 | 57.9648 | 28.9562 | 63.1 |
| 002545.SZ | 东方铁塔 | 农药化肥 | 2265437.0841 | 16.1557 | 2.2176 | 1.6474 | 4.0239 | 3.3902 | 95.213 | 29.7791 | 53.4 |
| 600486.SH | 扬农化工 | 农药化肥 | 2186245.379 | 17.378 | 1.8423 | 1.7648 | 3.4888 | 2.5455 | -6.4142 | 37.8841 | 44 |
| 000893.SZ | 亚钾国际 | 农药化肥 | 4375382.432 | 24.0319 | 3.1491 | 0.2297 | 3.9075 | 3.3365 | 38.52 | 32.5255 | 40.6 |
| 600331.SH | 宏达股份 | 农药化肥 | 3568801.6 | N/A | 11.4576 | N/A | -1.0758 | -0.9895 | 6.19 | 14.7067 | 36.5 |
| 600141.SH | 兴发集团 | 农药化肥 | 3789085.9047 | 26.3481 | 1.5147 | 1.5784 | 1.0915 | 1.0061 | -17.3743 | 48.4997 | 33.2 |
| 301035.SZ | 润丰股份 | 农药化肥 | 1906362.719 | 20.002 | 2.4799 | 2.2678 | 2.1699 | 1.4451 | -35.6141 | 53.8159 | 33.2 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600036.SH | 招商银行 | 银行 | 98231298.612 | 6.5163 | 0.8675 | 5.1759 | 2.9627 | N/A | 1.518 | 90.4294 | 61.9 |
| 000333.SZ | 美的集团 | 家用电器 | 65186263.8618 | 14.7488 | 2.806 | 4.9152 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.5 |
| 601857.SH | 中国石油 | 石油开采 | 202421201.4468 | 12.7966 | 1.246 | 4.2496 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 59.1 |
| 600938.SH | 中国海油 | 石油开采 | 160175944.98 | 12.8487 | 1.9135 | 3.3974 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 56.1 |
| 601318.SH | 中国平安 | 保险 | 95155658.71 | 7.1662 | 0.9344 | 5.138 | 2.479 | N/A | -7.3808 | 89.8779 | 55.1 |
| 600519.SH | 贵州茅台 | 白酒 | 168323487.44 | 20.3498 | 6.2136 | 3.8636 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 53.4 |
| 600941.SH | 中国移动 | 电信运营 | 209108119.3164 | 15.3976 | 1.4697 | 4.8783 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.2 |
| 601328.SH | 交通银行 | 银行 | 61147738.6823 | 6.3423 | 0.5252 | 4.6922 | 2.044 | N/A | 3.1137 | 92.0004 | 50.2 |
| 600028.SH | 中国石化 | 石油加工 | 61792937.7562 | 17.3815 | 0.7417 | 3.9152 | 2.0481 | 1.2478 | 28.2117 | N/A | 49.7 |
| 601398.SH | 工商银行 | 银行 | 270868755.396 | 7.2942 | 0.687 | 4.0829 | 2.0286 | N/A | 3.3093 | 92.1901 | 48.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.