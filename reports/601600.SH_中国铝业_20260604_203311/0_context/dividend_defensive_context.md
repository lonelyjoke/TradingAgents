# Dividend defensive verification context for 601600.SH as of 2026-06-04

Status: triggered
Defensive Dividend Rating: medium
- Company: 中国铝业
- Industry: 铝
- Dividend stability: fail
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
| dv_ttm | 2.3671 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260604 | 10.9 | 12.752 | 2.3187 | 2.3671 | 18698918.7464 |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 241125217000 | 12673918000 | 34092341000 | 9244017000 | 9445151000 | 24848324000 | 0.7452 |
| 20241231 | 237065629000 | 12400160000 | 32807186000 | 10359800000 | 7994528000 | 22447386000 | 0.6447 |
| 20231231 | 225070880000 | 6716945000 | 27040981000 | 6709495000 | 5534701000 | 20331486000 | 0.824 |
| 20221231 | 290987942000 | 4191927000 | 27806188000 | 4751196000 | 6288038000 | 23054992000 | 1.5 |
| 20211231 | 269748232000 | 5079562000 | 28306356000 | 2135552000 | 3966393000 | 26170804000 | 0.7809 |

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