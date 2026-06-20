# Dividend defensive verification context for 002714.SZ as of 2026-06-20

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
| dv_ttm | 3.9764 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 22 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3213 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260618 | 33.63 | 19.8494 | 2.2506 | 3.9764 | 19414585.548 |

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
| 002299.SZ | 圣农发展 | 农业综合 | 2006382.2838 | 13.5071 | 1.7488 | 3.0867 | 2.2299 | 1.1619 | 71.4079 | 53.4955 | 70.9 |
| 300761.SZ | 立华股份 | 农业综合 | 1454853.8187 | 27.6282 | 1.5324 | 2.0143 | 1.6463 | 1.0426 | -24.8494 | 43.3835 | 67.6 |
| 002714.SZ | 牧原股份 | 农业综合 | 19414585.548 | 19.8494 | 2.2506 | 3.9764 | -1.4728 | -0.3308 | -127.05 | 50.7312 | 67.5 |
| 000061.SZ | 农产品 | 农业综合 | 1163187.2632 | 26.8727 | 1.3458 | N/A | 1.5744 | 1.1031 | 80.891 | 52.0504 | 61.5 |
| 002458.SZ | 益生股份 | 农业综合 | 1173578.342 | 41.6398 | 2.6467 | 1.3864 | 2.3561 | 1.6316 | 884.1125 | 36.2396 | 57.8 |
| 300498.SZ | 温氏股份 | 农业综合 | 8224256.6148 | 37.6724 | 2.0788 | 2.4242 | -2.5963 | -0.97 | -153.1524 | 53.1422 | 53.8 |
| 600201.SH | 生物股份 | 农业综合 | 1308527.1606 | 125.4898 | 2.396 | 0.2526 | 1.4893 | 1.3029 | 5.4418 | 14.8828 | 49.1 |
| 002157.SZ | 正邦科技 | 农业综合 | 2682547.154 | N/A | 2.5681 | N/A | -3.8844 | -2.5878 | -342.8554 | 52.2816 | 38.5 |
| 605296.SH | 神农集团 | 农业综合 | 1347594.9792 | N/A | 3.1491 | 1.5187 | -14.1091 | -9.5377 | -383.6163 | 33.9763 | 29.9 |
| 000048.SZ | 京基智农 | 农业综合 | 999962.4808 | N/A | 2.6625 | 1.9721 | -5.898 | -2.1506 | -306.2703 | 62.3494 | 23.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 175334096.7324 | 11.0842 | 1.0793 | 4.9061 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600938.SH | 中国海油 | 石油开采 | 145916958.78 | 11.7049 | 1.7431 | 4.1407 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 93969144.7056 | 6.2336 | 0.8298 | 8.0864 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅台 | 白酒 | 151884914.4 | 18.3624 | 5.6068 | 4.258 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 59.1 |
| 601088.SH | 中国神华 | 煤炭开采 | 89490605.9218 | 17.3542 | 1.8609 | 7.0718 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 56.2 |
| 601318.SH | 中国平安 | 保险 | 89415536.196 | 6.7339 | 0.8781 | 5.4678 | 2.479 | N/A | -7.3808 | 89.8779 | 55.3 |
| 600941.SH | 中国移动 | 电信运营 | 198691836.642 | 14.6306 | 1.3965 | 5.1322 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600028.SH | 中国石化 | 石油加工 | 56955917.1882 | 16.0209 | 0.6836 | 4.2477 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 52.8 |
| 601398.SH | 工商银行 | 银行 | 255186880.0836 | 6.8719 | 0.6472 | 4.3338 | 2.0286 | N/A | 3.3093 | 92.1901 | 52.2 |
| 600900.SH | 长江电力 | 水力发电 | 65232268.3882 | 18.0784 | 2.8623 | 3.5371 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.