# Dividend defensive verification context for 601600.SH as of 2026-06-16

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
| dv_ttm | 2.5622 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 17 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3836 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260616 | 10.07 | 11.7791 | 2.1421 | 2.5622 | 17275056.0991 |

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
| 000807.SZ | 云铝股份 | 铝 | 8801675.8812 | 10.14 | 2.4688 | 2.7541 | 10.6372 | 10.6406 | 269.4536 | 17.7381 | 74 |
| 002532.SZ | 天山铝业 | 铝 | 5883125.3625 | 9.8404 | 1.8783 | 4.291 | 7.288 | 5.0744 | 109.6965 | 39.9421 | 67.5 |
| 000933.SZ | 神火股份 | 铝 | 5602269.9604 | 10.0277 | 2.083 | 3.1895 | 8.8986 | 7.1769 | 223.2834 | 40.8811 | 66 |
| 600595.SH | 中孚实业 | 铝 | 2545019.7385 | 11.5244 | 1.419 | 2.7559 | 4.6874 | 4.1747 | 256.6124 | 29.8486 | 65 |
| 600219.SH | 南山铝业 | 铝 | 5385856.0504 | 13.0325 | 1.0571 | 9.2681 | 2.1898 | 1.8234 | -35.3868 | 18.4404 | 59.5 |
| 601677.SH | 明泰铝业 | 铝 | 2051813.94 | 9.2326 | 1.0356 | 1.9088 | 3.6076 | 3.037 | 59.6827 | 31.4242 | 47.5 |
| 601600.SH | 中国铝业 | 铝 | 17275056.0991 | 11.7791 | 2.1421 | 2.5622 | 7.1058 | 5.384 | 56.3465 | 43.2655 | 47 |
| 002379.SZ | 宏桥控股 | 铝 | 21918340.8124 | 11.1211 | 4.1928 | 1.4863 | 13.8129 | 7.9201 | 37.5598 | 52.3604 | 43.5 |
| 603115.SH | 海星股份 | 铝 | 2637572.9216 | 118.1737 | 12.1829 | 0.5441 | 1.8494 | 1.3166 | 74.7373 | 34.494 | 26 |
| 603876.SH | 鼎胜新材 | 铝 | 2483001.9584 | 39.9575 | 3.2498 | 0.1497 | 2.5562 | 1.0844 | 127.2792 | 70.2262 | 24 |

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