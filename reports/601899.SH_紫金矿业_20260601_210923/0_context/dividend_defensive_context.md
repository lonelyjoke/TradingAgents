# Dividend defensive verification context for 601899.SH as of 2026-06-01

Status: triggered
Defensive Dividend Rating: medium
- Company: 紫金矿业
- Industry: 铜
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
| dv_ttm | 1.6522 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0233 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260601 | 30.19 | 13.013 | 4.0693 | 1.6522 | 80277367.4438 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.38 | 1 |
| 20250630 | 0.44 | 2 |
| 20241231 | 0.84 | 3 |
| 20240630 | 0.2 | 2 |
| 20231231 | 0.6 | 3 |
| 20230630 | 0.15 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 349079082852 | 51777327785 | 75429516296 | 30982297763 | 22888925189 | 44447218533 | 0.4421 |
| 20241231 | 303639957153 | 32050602437 | 48860346839 | 24797782052 | 16012050922 | 24062564787 | 0.4996 |
| 20231231 | 293403242878 | 21119419571 | 36860066015 | 30428663664 | 15174567428 | 6431402351 | 0.7185 |
| 20221231 | 270328998459 | 20042045977 | 28678502360 | 24794352673 | 11475070934 | 3884149687 | 0.5725 |
| 20211231 | 225102488592 | 15672870591 | 26072237601 | 20148568080 | 7336876536 | 5923669521 | 0.4681 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601899.SH | 紫金矿业 | 铜 | 80277367.4438 | 13.013 | 4.0693 | 1.6522 | 10.4049 | 5.9878 | 97.5001 | 51.3712 | 73 |
| 601168.SH | 西部矿业 | 铜 | 7351555 | 16.629 | 3.684 | 3.3712 | 8.2604 | 4.8098 | 96.3409 | 58.5159 | 72 |
| 600362.SH | 江西铜业 | 铜 | 14945140.112 | 18.6924 | 1.7769 | 2.5358 | 3.4073 | 1.8078 | 44.3105 | 62.4705 | 66.5 |
| 000630.SZ | 铜陵有色 | 铜 | 9145259.5698 | 34.8443 | 2.4397 | 2.1289 | 3.5947 | 3.1584 | 19.1171 | 54.3423 | 60.5 |
| 000737.SZ | 北方铜业 | 铜 | 2660888.8597 | 25.7205 | 3.5786 | 0.7874 | 8.6465 | 4.8696 | 65.7394 | 64.6004 | 48.5 |
| 603979.SH | 金诚信 | 铜 | 4572996.4845 | 18.1594 | 3.9946 | 0.6138 | 5.2814 | 3.8512 | 42.5546 | 47.8093 | 48 |
| 000878.SZ | 云南铜业 | 铜 | 4341079.4316 | 30.6313 | 2.4292 | 1.2849 | 3.9987 | 1.8822 | 7.9318 | 65.4474 | 45 |
| 002203.SZ | 海亮股份 | 铜 | 4597261.0796 | 44.4497 | 2.695 | 1.2329 | 2.5741 | 1.4723 | 26.4155 | 62.2225 | 43 |
| 601212.SH | 白银有色 | 铜 | 4650198.3929 | N/A | 2.9256 | 0.0637 | 0.9864 | 1.5995 | 440.2347 | 69.9131 | 33 |
| 688102.SH | 斯瑞新材 | 铜 | 2691252.166 | 169.9615 | 13.7824 | 0.2233 | 2.2162 | 1.3 | 33.2412 | 42.7233 | 30.5 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600938.SH | 中国海油 | 石油开采 | 165499299.7723 | 13.2757 | 1.9771 | 3.6507 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 63.1 |
| 601857.SH | 中国石油 | 石油开采 | 198028697.9991 | 12.4682 | 1.219 | 4.3438 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 60.9 |
| 600036.SH | 招商银行 | 银行 | 96339810.1958 | 6.3908 | 0.8508 | 7.8874 | 2.9627 | N/A | 1.518 | 90.4294 | 60.3 |
| 000333.SZ | 美的集团 | 家用电器 | 62192863.9932 | 14.0715 | 2.6697 | 4.9041 | 5.5648 | 2.2435 | 2.0312 | 60.0182 | 60 |
| 600028.SH | 中国石化 | 石油加工 | 58890725.4261 | 16.5651 | 0.7069 | 4.6857 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 56.6 |
| 600519.SH | 贵州茅台 | 白酒 | 163710686.467 | 19.7921 | 6.111 | 3.9504 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 106278228.0896 | 20.6097 | 2.1219 | 5.9547 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | 中国移动 | 电信运营 | 214308530.06 | 15.7805 | 1.5063 | 4.8474 | 2.084 | 1.759 | -4.2082 | 33.7319 | 53.4 |
| 601318.SH | 中国平安 | 保险 | 97509652.1431 | 7.3435 | 0.9576 | 4.7725 | 2.479 | N/A | -7.3808 | 89.8779 | 50.6 |
| 600900.SH | 长江电力 | 水力发电 | 67948240.5973 | 18.8311 | 2.9814 | 3.3958 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.3 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.