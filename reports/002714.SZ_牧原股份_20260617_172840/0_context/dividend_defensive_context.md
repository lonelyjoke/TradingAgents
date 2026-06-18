# Dividend defensive verification context for 002714.SZ as of 2026-06-17

Status: triggered
Defensive Dividend Rating: medium
- Company: 牧原股份
- Industry: 农业综合
- Dividend stability: fail
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: pass
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 3.8153 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 22 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3213 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260616 | 35.05 | 20.6875 | 2.3457 | 3.8153 | 20234350.98 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 1.281 | 3 |
| 20250630 | 1.8595 | 2 |
| 20241231 | 1.7183 | 3 |
| 20240930 | 2.4968 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0 | 2 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 144144965371.68 | 15486891254.04 | 30056186914.47 | 9528929651.93 | 10344664907.19 | 20527257262.54 | 0.668 |
| 20241231 | 137946892076.87 | 17881260485.27 | 37543066214.49 | 12380725812 | 8255880276.03 | 25162340402.49 | 0.4617 |
| 20231231 | 110860727714.4 | -4263280820.31 | 9892816863.72 | 17015725403.56 | 7747123200.88 | -7122908539.84 | 1.8172 |
| 20221231 | 124826212177.74 | 13266156512.39 | 23010550801.93 | 15738918946.02 | 4190777891.87 | 7271631855.91 | 0.3159 |
| 20211231 | 78889870566.4 | 6903777691.92 | 16295026813.82 | 35852334356.78 | 8966972376.87 | -19557307542.96 | 1.2989 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002299.SZ | 圣农发展 | 农业综合 | 2000166.7253 | 13.4653 | 1.7433 | 3.0963 | 2.2299 | 1.1619 | 71.4079 | 53.4955 | 70.9 |
| 300761.SZ | 立华股份 | 农业综合 | 1501402.3702 | 28.5121 | 1.5814 | 1.9518 | 1.6463 | 1.0426 | -24.8494 | 43.3835 | 67.6 |
| 002714.SZ | 牧原股份 | 农业综合 | 20234350.98 | 20.6875 | 2.3457 | 3.8153 | -1.4728 | -0.3308 | -127.05 | 50.7312 | 67.5 |
| 000061.SZ | 农产品 | 农业综合 | 1202886.4872 | 27.7899 | 1.3917 | N/A | 1.5744 | 1.1031 | 80.891 | 52.0504 | 62.5 |
| 002458.SZ | 益生股份 | 农业综合 | 1182165.5006 | 41.9445 | 2.6661 | 1.3764 | 2.3561 | 1.6316 | 884.1125 | 36.2396 | 58.2 |
| 300498.SZ | 温氏股份 | 农业综合 | 8583568.668 | 39.3183 | 2.1696 | 2.3227 | -2.5963 | -0.97 | -153.1524 | 53.1422 | 53.8 |
| 600201.SH | 生物股份 | 农业综合 | 1376343.7764 | 131.9935 | 2.5202 | 0.2401 | 1.4893 | 1.3029 | 5.4418 | 14.8828 | 50.1 |
| 002157.SZ | 正邦科技 | 农业综合 | 2830549.7556 | N/A | 2.7097 | N/A | -3.8844 | -2.5878 | -342.8554 | 52.2816 | 35.5 |
| 605296.SH | 神农集团 | 农业综合 | 1374882.728 | N/A | 3.2128 | 1.4885 | -14.1091 | -9.5377 | -383.6163 | 33.9763 | 28.9 |
| 000048.SZ | 京基智农 | 农业综合 | 1013217.5508 | N/A | 2.6978 | 1.9463 | -5.898 | -2.1506 | -306.2703 | 62.3494 | 25 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 182105872.911 | 11.5123 | 1.121 | 4.7236 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600938.SH | 中国海油 | 石油开采 | 148626166.158 | 11.9222 | 1.7755 | 4.0652 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 97272944.4792 | 6.4527 | 0.859 | 7.8118 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅台 | 白酒 | 156968996.2672 | 18.9771 | 5.7945 | 4.12 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.5 |
| 600028.SH | 中国石 | 石油加工 | 60099980.5574 | 16.9053 | 0.7214 | 4.5914 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.5 |
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