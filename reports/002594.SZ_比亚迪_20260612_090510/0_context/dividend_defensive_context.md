# Dividend defensive verification context for 002594.SZ as of 2026-06-12

Status: triggered
Defensive Dividend Rating: medium
- Company: 比亚迪
- Industry: 汽车整车
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
| dv_ttm | 1.4751 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 20 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 2.3411 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260611 | 89.8 | 29.7193 | 3.5303 | 1.4751 | 81872434.1337 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.358 | 1 |
| 20250630 | 0 | 1 |
| 20241231 | 11.922 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 9.2898 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 803964958000 | 32619022000 | 59135544000 | 156807853000 | 14125279000 | -97672309000 | 0.433 |
| 20241231 | 777102455000 | 40254346000 | 133453873000 | 97359768000 | 10051081000 | 36094105000 | 0.2497 |
| 20231231 | 602315354000 | 30040811000 | 169725025000 | 122093509000 | 4101617000 | 47631516000 | 0.1365 |
| 20221231 | 424060635000 | 16622448000 | 140837657000 | 97456862000 | 1632852000 | 43380795000 | 0.0982 |
| 20211231 | 216142395000 | 3045188000 | 65466682000 | 37343609000 | 2619303000 | 28123073000 | 0.8601 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600066.SH | 宇通客车 | 汽车整车 | 6531120.7079 | 11.9646 | 5.5362 | 8.4746 | 4.1424 | 2.1005 | -12.6885 | 51.3262 | 73 |
| 601633.SH | 长城汽车 | 汽车整车 | 14985586.0076 | 16.5412 | 1.7001 | 2.5706 | 1.0718 | 0.506 | -46.0102 | 59.8529 | 64.2 |
| 601127.SH | 赛力斯 | 汽车整车 | 11794981.0173 | 19.7788 | 2.9548 | 1.6382 | 1.835 | 0.4701 | 0.8921 | 65.9226 | 63.1 |
| 000625.SZ | 长安汽车 | 汽车整车 | 7375215.5393 | 23.9997 | 0.9553 | 4.6377 | 0.4536 | 0.2756 | -74.0874 | 57.1494 | 61.9 |
| 600104.SH | 上汽集团 | 汽车整车 | 12495366.6468 | 12.3611 | 0.4158 | 0.8046 | 1.0098 | 0.6084 | 0.0934 | 61.102 | 56.2 |
| 002594.SZ | 比亚迪 | 汽车整车 | 81872434.1337 | 29.7193 | 3.5303 | 1.4751 | 1.6464 | 0.5355 | -55.3844 | 70.9426 | 50.5 |
| 601238.SH | 广汽集团 | 汽车整车 | 5863312.8925 | N/A | 0.5625 | 0.3471 | -0.6266 | -0.4251 | 10.292 | 51.671 | 49.6 |
| 000800.SZ | 一汽解放 | 汽车整车 | 2962611.147 | 37.2749 | 1.1186 | 0.8306 | 0.3751 | -0.0109 | 241.8173 | 67.5543 | 46.9 |
| 600733.SH | 北汽蓝谷 | 汽车整车 | 3629277.7583 | N/A | 6.0265 | N/A | -24.97 | -3.6499 | 8.704 | 76.9582 | 28.5 |
| 600418.SH | 江淮汽车 | 汽车整车 | 7051069.394 | N/A | 5.6032 | N/A | -5.4412 | -1.1165 | -171.7415 | 73.7769 | 26 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 160746304.3739 | 12.8945 | 1.9203 | 3.7587 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.7 |
| 600036.SH | 招商银行 | 银行 | 97676462.0127 | 6.4795 | 0.8626 | 7.7795 | 2.9627 | N/A | 1.518 | 90.4294 | 60.9 |
| 601857.SH | 中国石油 | 石油开采 | 189792753.9973 | 11.9497 | 1.1683 | 4.5323 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.3 |
| 600028.SH | 中国石化 | 石油加工 | 57923321.3123 | 16.293 | 0.6952 | 4.764 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 60 |
| 600519.SH | 贵州茅台 | 白酒 | 159885436.7679 | 19.3297 | 5.9682 | 4.0449 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 102569334.8236 | 19.8905 | 2.0478 | 6.1701 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 000333.SZ | 美的集团 | 家用电器 | 64980701.0712 | 14.7023 | 2.7898 | 4.6936 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 55.3 |
| 600941.SH | 中国移动 | 电信运营 | 208057344.2483 | 15.3202 | 1.5131 | 4.9012 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.4 |
| 601318.SH | 中国平安 | 保险 | 95318627.4617 | 7.1785 | 0.9661 | 5.1292 | 2.479 | N/A | -7.3808 | 89.8779 | 53.1 |
| 600900.SH | 长江电力 | 水力发电 | 68241859.2099 | 18.9125 | 2.9943 | 3.3811 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.