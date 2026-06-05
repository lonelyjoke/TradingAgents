# Dividend defensive verification context for 300308.SZ as of 2026-06-05

Status: triggered
Defensive Dividend Rating: medium
- Company: 中际旭创
- Industry: 通信设备
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: fail
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 0.1184 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 24 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.4583 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 1179.99 | 88.0054 | 37.9881 | 0.1184 | 131558287.6278 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 1 | 1 |
| 20250630 | 1.2 | 3 |
| 20241231 | 1.5 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 1.35 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 38239935640.67 | 10797254300.45 | 10896126160.03 | 2759994695.91 | 1082737373.75 | 8136131464.12 | 0.1003 |
| 20241231 | 23862159738.37 | 5171485967.85 | 3164582957.85 | 2866157321.96 | 398798831.25 | 298425635.89 | 0.0771 |
| 20231231 | 10717984471.03 | 2173527747.77 | 1897126918.71 | 1704456354.82 | 206588378.41 | 192670563.89 | 0.095 |
| 20221231 | 9641794766.08 | 1223990866.18 | 2448940873.28 | 791834579.12 | 232769127.69 | 1657106294.16 | 0.1902 |
| 20211231 | 7695404805.69 | 876977126.32 | 812760603.14 | 839578498.95 | 167597654.73 | -26817895.81 | 0.1911 |

## Same-Industry Defensive Alternatives
No data returned.

## Cross-Industry Defensive Alternatives
No data returned.

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- daily_basic market snapshot unavailable: daily_basic unavailable: configured_http_url: 您请求速度过快
- peer tables need daily_basic market snapshot.