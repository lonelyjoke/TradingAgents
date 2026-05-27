# Dividend defensive verification context for 600519.SH as of 2026-05-27

Status: triggered
Defensive Dividend Rating: medium
- Company: 贵州茅台
- Industry: 白酒
- Dividend stability: fail
- Dividend coverage: watch
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
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p |
| --- | --- | --- |
| 20251231 | 172054171890.91 | 82320067101.68 |
| 20241231 | 174144069958.25 | 86228146421.62 |
| 20231231 | 150560330316.45 | 74734071550.75 |
| 20221231 | 127553959355.97 | 62716443738.27 |
| 20211231 | 109464278563.89 | 52460144378.16 |

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