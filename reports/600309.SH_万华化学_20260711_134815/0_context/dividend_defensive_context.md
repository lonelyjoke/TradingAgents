# Dividend defensive verification context for 600309.SH as of 2026-07-11

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
| dv_ttm | 1.8192 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 24 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.2229 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260710 | 68.71 | 16.3411 | 1.9308 | 1.8192 | 21509470.3636 |

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
| 002709.SZ | 天赐材料 | 化工原料 | 8166478.1702 | 28.4873 | 4.2798 | 0.8698 | 8.9589 | 7.1376 | 1005.751 | 35.5639 | 75.4 |
| 600989.SH | 宝丰能源 | 化工原料 | 14901387.52 | 11.8507 | 2.8592 | 3.4164 | 7.2844 | 4.8239 | 50.2298 | 44.8554 | 74.5 |
| 600160.SH | 巨化股份 | 化工原料 | 11722297.5662 | 28.2302 | 5.4236 | 1.2897 | 5.5796 | 3.9181 | 45.9262 | 38.4052 | 61.2 |
| 002648.SZ | 卫星化学 | 化工原料 | 7640088.4476 | 13.0394 | 2.155 | 2.2006 | 6.1356 | 3.6912 | 34.9726 | 52.4788 | 60.2 |
| 600309.SH | 万华化学 | 化工原料 | 21509470.3636 | 16.3411 | 1.9308 | 1.8192 | 3.3843 | 1.7952 | 20.6239 | 64.3165 | 55.9 |
| 600378.SH | 昊华科技 | 化工原料 | 7814818.1826 | 49.8475 | 4.2057 | 0.6471 | 1.6744 | 1.5581 | 66.7299 | 40.1982 | 49.1 |
| 300054.SZ | 鼎龙股份 | 化工原料 | 7921579.797 | 95.4215 | 14.5039 | 0.1203 | 4.6984 | 3.298 | 77.9914 | 40.1705 | 43.3 |
| 688548.SH | 广钢气体 | 化工原料 | 5752577.46 | 179.1976 | 9.4397 | 0.2224 | 1.5178 | 1.2508 | 62.6275 | 31.8489 | 39.8 |
| 601208.SH | 东材科技 | 化工原料 | 5516608.8169 | 145.0233 | 9.0617 | 0.1831 | 3.0805 | 2.0834 | 103.3497 | 44.9036 | 35.6 |
| 688585.SH | 上纬新材 | 化工原料 | 5768072.31 | N/A | 44.3505 | N/A | -3.1028 | -1.5986 | -282.1176 | 41.7856 | 25 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 169660446.4206 | 10.7255 | 1.0444 | 5.0701 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64 |
| 600036.SH | 招商银 | 银行 | 93010790.5728 | 6.17 | 0.8214 | 5.4664 | 2.9627 | N/A | 1.518 | 90.4294 | 61.6 |
| 600938.SH | 中国海 | 石油开采 | 133796820.51 | 10.7327 | 1.5983 | 4.0672 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 60.5 |
| 000333.SZ | 美的集团 | 家用电器 | 60138553.8711 | 13.6067 | 2.5887 | 5.3392 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 59.8 |
| 600519.SH | 贵州茅台 | 白酒 | 150632332.6368 | 18.211 | 5.5606 | 4.3173 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.4 |
| 601939.SH | 建设银行 | 银行 | 262385182.6445 | 7.6755 | 0.7397 | N/A | 2.3288 | N/A | 3.5273 | 92.0007 | 56.2 |
| 601318.SH | 中国平安 | 保险 | 89596612.616 | 6.7475 | 0.8799 | 5.4568 | 2.479 | N/A | -7.3808 | 89.8779 | 55.2 |
| 600941.SH | 中国移动 | 电信运营 | 195109899.3074 | 14.3668 | 1.3713 | 5.2275 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.4 |
| 600028.SH | 中国石化 | 石油加工 | 57560544.7592 | 16.191 | 0.6909 | 4.2031 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 51.2 |
| 601328.SH | 交通银 | 银行 | 58408461.3714 | 6.0582 | 0.5017 | 4.9123 | 2.044 | N/A | 3.1137 | 92.0004 | 49.8 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.