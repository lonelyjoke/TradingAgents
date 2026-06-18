# Dividend defensive verification context for 601318.SH as of 2026-06-18

Status: triggered
Defensive Dividend Rating: strong
- Company: 中国平安
- Industry: 保险
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: pass
- Dividend trap risk: low

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 5.1175 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 34 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0509 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260617 | 52.76 | 7.1948 | 0.9382 | 5.1175 | 95535919.192 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 5.25 | 3 |
| 20250630 | 1.9 | 2 |
| 20241231 | 4.86 | 3 |
| 20240630 | 1.86 | 2 |
| 20231231 | 4.5 | 3 |
| 20230630 | 1.86 | 2 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 1050506000000 | 134778000000 | 658632000000 | 8355000000 | 77146000000 | 650277000000 | 0.5724 |
| 20241231 | 1028925000000 | 126607000000 | 382474000000 | 6678000000 | 74669000000 | 375796000000 | 0.5898 |
| 20231231 | 913789000000 | 85665000000 | 360403000000 | 7810000000 | 73087000000 | 352593000000 | 0.8532 |
| 20221231 | 1110568000000 | 83774000000 | 485905000000 | 8871000000 | 77791000000 | 477034000000 | 0.9286 |
| 20211231 | 1180444000000 | 101618000000 | 90116000000 | 12186000000 | 92829000000 | 77930000000 | 0.9135 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601318.SH | 中国平安 | 保险 | 95535919.192 | 7.1948 | 0.9382 | 5.1175 | 2.479 | N/A | -7.3808 | 89.8779 | 64 |
| 601601.SH | 中国太保 | 保险 | 30967879.2885 | 5.7434 | 0.969 | 3.3551 | 3.2299 | N/A | 4.3004 | 89.0876 | 63 |
| 601336.SH | 新华保险 | 保险 | 19263200.255 | 5.22 | 1.5591 | 4.3077 | 5.5304 | N/A | 10.5236 | 93.3325 | 60 |
| 601319.SH | 中国人保 | 保险 | 30956793.42 | 7.265 | 0.9694 | 2.7426 | 2.8055 | N/A | -31.4032 | 78.5414 | 46 |
| 601628.SH | 中国人寿 | 保险 | 101215908.605 | 6.991 | 1.6918 | 1.9213 | 3.2686 | N/A | -32.279 | 92.0676 | 37 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 178811495.3106 | 11.304 | 1.1007 | 4.8107 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64.7 |
| 600938.SH | 中国海油 | 石油开采 | 149244055.56 | 11.9718 | 1.7829 | 4.0483 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 96415469.7288 | 6.3958 | 0.8515 | 7.8812 | 2.9627 | N/A | 1.518 | 90.4294 | 62.8 |
| 601998.SH | 中信银行 | 银行 | 42067742.6988 | 5.9078 | 0.5664 | 5.0397 | 2.3976 | N/A | 3.0191 | 91.5368 | 60.9 |
| 600519.SH | 贵州茅台 | 白酒 | 155010118.4 | 18.7402 | 5.7222 | 4.1721 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 58.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 90791971.9798 | 17.6066 | 1.888 | 6.9704 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 56.2 |
| 600941.SH | 中国移动 | 电信运营 | 201575198.8104 | 14.8429 | 1.4168 | 5.0588 | 2.084 | 1.759 | -4.2082 | 33.7319 | 55.3 |
| 600028.SH | 中国石化 | 石油加工 | 58648874.387 | 16.4971 | 0.704 | 4.1251 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 52.5 |
| 600900.SH | 长江电力 | 水力发电 | 66064187.79 | 18.3089 | 2.8988 | 3.4926 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 51.2 |
| 601398.SH | 工商银行 | 银行 | 262315005.2256 | 7.0639 | 0.6653 | 4.216 | 2.0286 | N/A | 3.3093 | 92.1901 | 51.2 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.