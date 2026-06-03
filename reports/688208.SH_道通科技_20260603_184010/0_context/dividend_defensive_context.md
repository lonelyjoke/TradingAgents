# Dividend defensive verification context for 688208.SH as of 2026-06-03

Status: triggered
Defensive Dividend Rating: medium
- Company: 道通科技
- Industry: IT设备
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
| dv_ttm | 3.4742 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260603 | 30.76 | 22.1419 | 5.8541 | 3.4742 | 2061485.2396 |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 4832751860.91 | 935875122.31 | 595597662.21 | 132026059.17 | 613979065.8 | 463571603.04 | 0.656 |
| 20241231 | 3932256447.46 | 640925193.32 | 747517485.85 | 150498028.15 | 359604891.19 | 597019457.7 | 0.5611 |
| 20231231 | 3251152240.25 | 179233332.27 | 434056417.87 | 215789015.52 | 5484271.87 | 218267402.35 | 0.0306 |
| 20221231 | 2265555176.93 | 102033256.64 | -382964140.27 | 133716583.69 | 52693835.93 | -516680723.96 | 0.5164 |
| 20211231 | 2253712738.59 | 438736178.92 | -144829604.97 | 201062114.83 | 233893450.55 | -345891719.8 | 0.5331 |

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
- peer tables need daily_basic market snapshot.