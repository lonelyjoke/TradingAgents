# Dividend defensive verification context for 601600.SH as of 2026-06-04

Status: triggered
Defensive Dividend Rating: medium
- Company: 中国铝业
- Industry: 铝
- Dividend stability: fail
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
| dv_ttm | 2.3671 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3836 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260604 | 10.9 | 12.752 | 2.3187 | 2.3671 | 18698918.7464 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.147 | 1 |
| 20250630 | 0.246 | 2 |
| 20241231 | 0.405 | 3 |
| 20240630 | 0.246 | 3 |
| 20231231 | 0.24 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 241125217000 | 12673918000 | 34092341000 | 9244017000 | 9445151000 | 24848324000 | 0.7452 |
| 20241231 | 237065629000 | 12400160000 | 32807186000 | 10359800000 | 7994528000 | 22447386000 | 0.6447 |
| 20231231 | 225070880000 | 6716945000 | 27040981000 | 6709495000 | 5534701000 | 20331486000 | 0.824 |
| 20221231 | 290987942000 | 4191927000 | 27806188000 | 4751196000 | 6288038000 | 23054992000 | 1.5 |
| 20211231 | 269748232000 | 5079562000 | 28306356000 | 2135552000 | 3966393000 | 26170804000 | 0.7809 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000807.SZ | 云铝股份 | 铝 | 9918358.1783 | 11.4264 | 2.782 | 1.7483 | 10.6372 | 10.6406 | 269.4536 | 17.7381 | 71.5 |
| 002532.SZ | 天山铝业 | 铝 | 6642238.1905 | 11.1101 | 2.2013 | 3.8006 | 7.288 | 5.0744 | 109.6965 | 39.9421 | 67.5 |
| 600595.SH | 中孚实业 | 铝 | 2865652.1565 | 12.9763 | 1.6628 | 2.4476 | 4.6874 | 4.1747 | 256.6124 | 29.8486 | 66 |
| 000933.SZ | 神火股份 | 铝 | 6450144.6163 | 11.5454 | 2.569 | 2.7703 | 8.8986 | 7.1769 | 223.2834 | 40.8811 | 64.5 |
| 600219.SH | 南山铝业 | 铝 | 5730367.0779 | 13.8661 | 1.1602 | 8.7109 | 2.1898 | 1.8234 | -35.3868 | 18.4404 | 61 |
| 601600.SH | 中国铝业 | 铝 | 18698918.7464 | 12.752 | 2.3187 | 2.3671 | 7.1058 | 5.384 | 56.3465 | 43.2655 | 51 |
| 002379.SZ | 宏桥控股 | 铝 | 25332493.7847 | 10.2655 | 5.168 | 1.286 | 13.8129 | 7.9201 | 37.5598 | 52.3604 | 46 |
| 601677.SH | 明泰铝业 | 铝 | 2375130.1276 | 10.6875 | 1.1988 | 1.1466 | 3.6076 | 3.037 | 59.6827 | 31.4242 | 44.5 |
| 603115.SH | 海星股份 | 铝 | 2601531.252 | 116.5589 | 12.0165 | 0.5517 | 1.8494 | 1.3166 | 74.7373 | 34.494 | 25 |
| 603876.SH | 鼎胜新材 | 铝 | 2346399.7128 | 37.7593 | 3.0711 | 0.3965 | 2.5562 | 1.0844 | 127.2792 | 70.2262 | 23 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 168493686.8733 | 13.5159 | 2.0128 | 3.5858 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 601857.SH | 中国石油 | 石油开采 | 194917341.3762 | 12.2723 | 1.1998 | 4.4132 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.9 |
| 600036.SH | 招商银行 | 银行 | 96087611.7398 | 6.3741 | 0.8486 | 7.9081 | 2.9627 | N/A | 1.518 | 90.4294 | 60.3 |
| 000333.SZ | 美的集团 | 家用电器 | 62746640.3878 | 14.1968 | 2.6929 | 4.8607 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60 |
| 600028.SH | 中国石化 | 石油加工 | 58286097.855 | 16.3951 | 0.6996 | 4.7343 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 56.6 |
| 600519.SH | 贵州茅台 | 白酒 | 158510347.0068 | 19.1634 | 5.9169 | 4.08 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 106321606.9582 | 20.6181 | 2.1227 | 5.9523 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 601318.SH | 中国平安 | 保险 | 96386978.3394 | 7.2589 | 0.9465 | 4.8281 | 2.479 | N/A | -7.3808 | 89.8779 | 52.2 |
| 600941.SH | 中国移动 | 电信运营 | 217038851.0698 | 15.9815 | 1.5255 | 4.7864 | 2.084 | 1.759 | -4.2082 | 33.7319 | 51.9 |
| 600900.SH | 长江电力 | 水力发电 | 67825899.5088 | 18.7972 | 2.9761 | 3.4019 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.