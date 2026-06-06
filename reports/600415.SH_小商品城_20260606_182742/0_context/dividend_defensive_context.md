# Dividend defensive verification context for 600415.SH as of 2026-06-06

Status: triggered
Defensive Dividend Rating: medium
- Company: 小商品城
- Industry: 商品城
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
| dv_ttm | 2.7943 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.5522 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 11.81 | 14.7497 | 2.7132 | 2.7943 | 6476083.4459 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.5 | 1 |
| 20250630 | 0 | 1 |
| 20241231 | 0.99 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.6 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 19927252694.51 | 4203546946.97 | 10529211443 | 2182072518.33 | 1993385493.06 | 8347138924.67 | 0.4742 |
| 20241231 | 15737383922.24 | 3073677494.86 | 4491339090.33 | 1500262163.77 | 1402224958.9 | 2991076926.56 | 0.4562 |
| 20231231 | 11299686665.89 | 2676182133.26 | 1845059849.92 | 2627630588.71 | 594916647.3 | -782570738.79 | 0.2223 |
| 20221231 | 7619693742.6 | 1104719091.71 | 1400090713.77 | 4114901826.31 | 652035197.63 | -2714811112.54 | 0.5902 |
| 20211231 | 6033842972.95 | 1334095906.95 | 2033082507.76 | 2042626824.44 | 650819017.71 | -9544316.68 | 0.4878 |

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