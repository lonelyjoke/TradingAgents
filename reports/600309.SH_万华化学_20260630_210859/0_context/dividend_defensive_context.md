# Dividend defensive verification context for 600309.SH as of 2026-06-30

Status: triggered
Defensive Dividend Rating: medium
- Company: 万华化学
- Industry: 化工原料
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
| dv_ttm | 1.8272 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 24 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.2229 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260630 | 68.41 | 16.2697 | 1.9224 | 1.8272 | 21415556.2156 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 3.75 | 3 |
| 20250630 | 0 | 1 |
| 20241231 | 2.19 | 3 |
| 20240630 | 1.04 | 2 |
| 20231231 | 4.875 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 203234573814.42 | 12527201094.15 | 33105189455.82 | 30711201211.89 | 6737836925.98 | 2393988243.93 | 0.5379 |
| 20241231 | 182069119160.94 | 13033066612.84 | 30053435178.33 | 35830124773.82 | 11311953510.64 | -5776689595.49 | 0.8679 |
| 20231231 | 175360935668.36 | 16815755534.31 | 26796752552.51 | 43098415319.53 | 9001793158.27 | -16301662767.02 | 0.5353 |
| 20221231 | 165565484373.69 | 16233626024.32 | 36336824920.33 | 32656552625.92 | 10489947082.1 | 3680272294.41 | 0.6462 |
| 20211231 | 145537817628.55 | 24648748123.08 | 27922292184.74 | 26999582886.59 | 6673634212.28 | 922709298.15 | 0.2707 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002709.SZ | 天赐材料 | 化工原料 | 10484322.8231 | 36.5727 | 5.4945 | 0.6775 | 8.9589 | 7.1376 | 1005.751 | 35.5639 | 76.5 |
| 600989.SH | 宝丰能源 | 化工原料 | 14908720.88 | 11.8565 | 2.8606 | 3.4147 | 7.2844 | 4.8239 | 50.2298 | 44.8554 | 74.5 |
| 002648.SZ | 卫星化学 | 化工原料 | 7912948.7493 | 13.5051 | 2.232 | 2.1247 | 6.1356 | 3.6912 | 34.9726 | 52.4788 | 59 |
| 600160.SH | 巨化股份 | 化工原料 | 14311354.0761 | 34.4652 | 6.6215 | 1.0564 | 5.5796 | 3.9181 | 45.9262 | 38.4052 | 59 |
| 600309.SH | 万华化学 | 化工原料 | 21415556.2156 | 16.2697 | 1.9224 | 1.8272 | 3.3843 | 1.7952 | 20.6239 | 64.3165 | 53 |
| 300037.SZ | 新宙邦 | 化工原料 | 6999835.484 | 51.931 | 6.3825 | 0.5352 | 4.3653 | 2.8032 | 109.0212 | 46.7276 | 47 |
| 600378.SH | 昊华科技 | 化工原料 | 9724017.7386 | 62.0255 | 5.2332 | 0.52 | 1.6744 | 1.5581 | 66.7299 | 40.1982 | 44.5 |
| 300054.SZ | 鼎龙股份 | 化工原料 | 10097429.8678 | 121.6313 | 18.4877 | 0.0944 | 4.6984 | 3.298 | 77.9914 | 40.1705 | 40 |
| 688548.SH | 广钢气体 | 化工原料 | 6874066.185 | 214.1329 | 11.28 | 0.1861 | 1.5178 | 1.2508 | 62.6275 | 31.8489 | 34.5 |
| 601208.SH | 东材科技 | 化工原料 | 7151084.7491 | 187.9912 | 11.7465 | 0.1413 | 3.0805 | 2.0834 | 103.3497 | 44.9036 | 32 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 129043825.11 | 10.3514 | 1.5416 | 4.6821 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 68.8 |
| 601857.SH | 中国石油 | 石油开采 | 158862208.7304 | 10.0429 | 0.9779 | 5.4148 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 61.9 |
| 600036.SH | 招商银行 | 银行 | 89530451.88 | 5.9391 | 0.7906 | 8.4873 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 000333.SZ | 美的集团 | 家用电器 | 57504304.0117 | 13.0107 | 2.4754 | 5.5838 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 57.8 |
| 600519.SH | 贵州茅台 | 白酒 | 148195923.5984 | 17.9164 | 5.4706 | 4.3883 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55 |
| 600028.SH | 中国石化 | 石油加工 | 53932779.3332 | 15.1705 | 0.6473 | 4.4858 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 54.4 |
| 601088.SH | 中国神华 | 煤炭开采 | 84675551.5072 | 16.4205 | 1.7608 | 7.4739 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 54.4 |
| 601318.SH | 中国平安 | 保险 | 86445882.908 | 6.5103 | 0.8489 | 5.6556 | 2.479 | N/A | -7.3808 | 89.8779 | 53.8 |
| 600941.SH | 中国移动 | 电信运营 | 186724799.6724 | 13.7494 | 1.3124 | 5.4612 | 2.084 | 1.759 | -4.2082 | 33.7319 | 51.9 |
| 600900.SH | 长江电力 | 水力发电 | 64767372.2519 | 17.9495 | 2.8419 | 3.5625 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.