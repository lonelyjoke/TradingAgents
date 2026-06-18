# Dividend defensive verification context for 600519.SH as of 2026-06-18

Status: triggered
Defensive Dividend Rating: medium
- Company: 贵州茅台
- Industry: 白酒
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
| dv_ttm | 4.1721 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 29 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.2221 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260617 | 1240 | 18.7402 | 5.7222 | 4.1721 | 155010118.4 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 27.993 | 1 |
| 20250930 | 71.871 | 3 |
| 20250630 | 0 | 1 |
| 20241231 | 82.921 | 3 |
| 20240930 | 71.646 | 3 |
| 20240630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 172054171890.91 | 82320067101.68 | 61522204989.35 | 3127594916.41 | 67241733345.45 | 58394610072.94 | 0.8168 |
| 20241231 | 174144069958.25 | 86228146421.62 | 92463692168.43 | 4678712053.56 | 70951027702.94 | 87784980114.87 | 0.8228 |
| 20231231 | 150560330316.45 | 74734071550.75 | 66593247721.09 | 2619755888.79 | 58754786730.01 | 63973491832.3 | 0.7862 |
| 20221231 | 127553959355.97 | 62716443738.27 | 36698595830.03 | 5306546416.54 | 57370196191.46 | 31392049413.49 | 0.9148 |
| 20211231 | 109464278563.89 | 52460144378.16 | 64028676147.37 | 3408784532.01 | 26476019839.37 | 60619891615.36 | 0.5047 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000858.SZ | 五粮液 | 白酒 | 30078580.392 | 23.8705 | 2.35 | 7.4164 | 6.5041 | 5.2115 | 82.5678 | 34.3133 | 69.5 |
| 600519.SH | 贵州茅台 | 白酒 | 155010118.4 | 18.7402 | 5.7222 | 4.1721 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 65 |
| 000568.SZ | 泸州老窖 | 白酒 | 12207950.2116 | 12.2738 | 2.3659 | 7.1741 | 7.316 | 7.4383 | -19.2548 | 21.8137 | 61 |
| 603198.SH | 迎驾贡酒 | 白酒 | 2632800 | 13.2188 | 2.2954 | 4.5579 | 7.551 | 7.7452 | 0.7314 | 21.4057 | 59.5 |
| 002304.SZ | 洋河股份 | 白酒 | 6339120.9808 | 62.423 | 1.2874 | 5.5062 | 5.0949 | 5.4901 | -32.7335 | 18.1694 | 58 |
| 603369.SH | 今世缘 | 白酒 | 3133208.4 | 13.3637 | 1.7458 | 4.7752 | 8.0262 | 6.8452 | -15.7615 | 34.7358 | 57.5 |
| 000596.SZ | 古井贡酒 | 白酒 | 4443411.6 | 15.7226 | 1.7009 | 7.1378 | 6.28 | 5.3163 | -31.0309 | 32.9709 | 55.5 |
| 600809.SH | 山西汾酒 | 白酒 | 14358978.634 | 13.0758 | 3.1892 | 3.0586 | 12.7163 | 12.0063 | -19.0299 | 29.2569 | 49.5 |
| 600779.SH | 水井坊 | 白酒 | 1404496.7192 | 36.3263 | 2.6577 | 3.3471 | 3.2898 | 2.8229 | -10.1183 | 36.9389 | 26.5 |
| 600702.SH | 舍得酒业 | 白酒 | 1264602.1472 | 116.6243 | 1.7684 | 0.8054 | 3.2987 | 2.4793 | -33.102 | 44.1174 | 18 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 149244055.56 | 11.9718 | 1.7829 | 4.0483 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 66.2 |
| 600036.SH | 招商银行 | 银行 | 96415469.7288 | 6.3958 | 0.8515 | 7.8812 | 2.9627 | N/A | 1.518 | 90.4294 | 64.7 |
| 601857.SH | 中国石油 | 石油开采 | 178811495.3106 | 11.304 | 1.1007 | 4.8107 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 64.4 |
| 601998.SH | 中信银行 | 银行 | 42067742.6988 | 5.9078 | 0.5664 | 5.0397 | 2.3976 | N/A | 3.0191 | 91.5368 | 59.4 |
| 601318.SH | 中国平安 | 保险 | 95535919.192 | 7.1948 | 0.9382 | 5.1175 | 2.479 | N/A | -7.3808 | 89.8779 | 57.8 |
| 601088.SH | 中国神华 | 煤炭开采 | 90791971.9798 | 17.6066 | 1.888 | 6.9704 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 56.2 |
| 600941.SH | 中国移动 | 电信运营 | 201575198.8104 | 14.8429 | 1.4168 | 5.0588 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600028.SH | 中国石化 | 石油加工 | 58648874.387 | 16.4971 | 0.704 | 4.1251 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 53.4 |
| 600900.SH | 长江电力 | 水力发电 | 66064187.79 | 18.3089 | 2.8988 | 3.4926 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 52.5 |
| 601398.SH | 工商银行 | 银行 | 262315005.2256 | 7.0639 | 0.6653 | 4.216 | 2.0286 | N/A | 3.3093 | 92.1901 | 49.7 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.