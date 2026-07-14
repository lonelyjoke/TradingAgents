# Dividend defensive verification context for 600809.SH as of 2026-07-14

Status: triggered
Defensive Dividend Rating: medium
- Company: 山西汾酒
- Industry: 白酒
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
| dv_ttm | N/A | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 37 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.915 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260713 | 109.56 | 12.1715 | 2.9687 | N/A | 13365927.7752 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 6.56 | 1 |
| 20250630 | 0 | 1 |
| 20241231 | 10.8 | 3 |
| 20240930 | 7.38 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 13.11 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 38718257657.74 | 12246329337.25 | 9013519822.15 | 1194271115.52 | 7392983185.32 | 7819248706.63 | 0.6037 |
| 20241231 | 36010992321.46 | 12242884323.77 | 12172323337.21 | 637684605.31 | 5349153635.82 | 11534638731.9 | 0.4369 |
| 20231231 | 31928483054.02 | 10438114410.47 | 7225083460.39 | 485035030.78 | 4032371231.36 | 6740048429.61 | 0.3863 |
| 20221231 | 26213860718.3 | 8095851303.7 | 10310203977.44 | 825576632.31 | 2196465521.59 | 9484627345.13 | 0.2713 |
| 20211231 | 19970986258.92 | 5313612016.46 | 7645105077.97 | 156277238.19 | 174302053.2 | 7488827839.78 | 0.0328 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000858.SZ | 五粮液 | 白酒 | 28265869.456 | 22.432 | 2.2083 | 7.8921 | 6.5041 | 5.2115 | 82.5678 | 34.3133 | 69.5 |
| 600519.SH | 贵州茅台 | 白酒 | 151383631.6784 | 18.3018 | 5.5883 | 4.2959 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 67.4 |
| 000568.SZ | 泸州老窖 | 白酒 | 11296843.245 | 11.3577 | 2.1894 | 7.7527 | 7.316 | 7.4383 | -19.2548 | 21.8137 | 63.7 |
| 603198.SH | 迎驾贡酒 | 白酒 | 2584000 | 12.9738 | 2.2529 | 4.644 | 7.551 | 7.7452 | 0.7314 | 21.4057 | 60.7 |
| 603369.SH | 今世缘 | 白酒 | 3042192 | 12.9755 | 1.695 | 4.918 | 8.0262 | 6.8452 | -15.7615 | 34.7358 | 58.9 |
| 600809.SH | 山西汾酒 | 白酒 | 13365927.7752 | 12.1715 | 2.9687 | N/A | 12.7163 | 12.0063 | -19.0299 | 29.2569 | 55.5 |
| 002304.SZ | 洋河股份 | 白酒 | 5739555.831 | 56.5189 | 1.1656 | 3.8583 | 5.0949 | 5.4901 | -32.7335 | 18.1694 | 50.1 |
| 000596.SZ | 古井贡酒 | 白酒 | 4174354.2 | 14.7705 | 1.5979 | 1.2663 | 6.28 | 5.3163 | -31.0309 | 32.9709 | 35.3 |
| 000799.SZ | 酒鬼酒 | 白酒 | 1234730.2 | N/A | 3.274 | 1.5789 | 0.8837 | 0.8858 | 4.6274 | 22.0361 | 31.1 |
| 600779.SH | 水井坊 | 白酒 | 1313333.6208 | 33.9684 | 2.4852 | 3.5795 | 3.2898 | 2.8229 | -10.1183 | 36.9389 | 27.8 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 176798264.5548 | 11.1767 | 1.0883 | 4.8654 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 63.1 |
| 600938.SH | 中国海油 | 石油开采 | 136981327.428 | 10.9881 | 1.6364 | 3.9727 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 60.8 |
| 000333.SZ | 美的集团 | 家用电器 | 61212048.756 | 13.8496 | 2.635 | 5.2456 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60.5 |
| 600036.SH | 招商银行 | 银行 | 93943924.86 | 6.2319 | 0.8296 | 5.4121 | 2.9627 | N/A | 1.518 | 90.4294 | 60.4 |
| 601318.SH | 中国平安 | 保险 | 89687150.826 | 6.7544 | 0.8807 | 5.4512 | 2.479 | N/A | -7.3808 | 89.8779 | 56.7 |
| 600519.SH | 贵州茅台 | 白酒 | 151383631.6784 | 18.3018 | 5.5883 | 4.2959 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 56.5 |
| 600941.SH | 中国移动 | 电信运营 | 198254035.2709 | 14.5983 | 1.3934 | 5.1446 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.2 |
| 601328.SH | 交通银行 | 银行 | 59822281.919 | 6.2049 | 0.5138 | 4.7962 | 2.044 | N/A | 3.1137 | 92.0004 | 48.7 |
| 601088.SH | 中国神华 | 煤炭开采 | 92505437.2895 | 17.9389 | 1.9236 | 4.4843 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 47 |
| 601398.SH | 工商银行 | 银行 | 268373911.5963 | 7.227 | 0.6807 | 4.1208 | 2.0286 | N/A | 3.3093 | 92.1901 | 47 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.