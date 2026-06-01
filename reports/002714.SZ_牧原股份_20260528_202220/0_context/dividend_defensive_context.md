# Dividend defensive verification context for 002714.SZ as of 2026-05-28

Status: triggered
Defensive Dividend Rating: medium
- Company: 牧原股份
- Industry: 农业综合
- Dividend stability: fail
- Dividend coverage: watch
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
| dv_ttm | 3.6094 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 22 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3838 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260528 | 37.05 | 21.868 | 2.5516 | 3.6094 | 21388947.6495 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.427 | 1 |
| 20250630 | 1.8595 | 2 |
| 20241231 | 1.7183 | 3 |
| 20240930 | 2.4968 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0 | 2 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p |
| --- | --- | --- |
| 20251231 | 144144965371.68 | 15486891254.04 |
| 20241231 | 137946892076.87 | 17881260485.27 |
| 20231231 | 110860727714.4 | -4263280820.31 |
| 20221231 | 124826212177.74 | 13266156512.39 |
| 20211231 | 78889870566.4 | 6903777691.92 |

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