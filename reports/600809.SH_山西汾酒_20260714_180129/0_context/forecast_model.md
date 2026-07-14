# Forward Forecast Model Scaffold for 600809.SH as of 2026-07-14

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 14923228703.48 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 75.0468% / -3.75pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / -0.0283% / +0.00pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.5334 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 0.0002% / -0.00pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 22.8675% / +3.99pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 汾酒 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 青花系列 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 玻汾系列 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 老白汾系列 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Hog-Breeding Sensitivity Requirement
| item | Formula / requirement |
| --- | --- |
| Sales kg | commodity-hog output x average sale weight |
| Unit spread | realized commodity-hog ASP - complete hog-breeding cost |
| Breeding profit | sales kg x unit spread |
| Sensitivity | show at least bear/base/bull hog ASP cases and each 1 CNY/kg move where data permits |
| Implied cycle | reverse-engineer the hog ASP implied by current market cap under normalized PE/PB bands |
| Valuation floor | stress-case book value / NAV after losses and impairment, cross-checked with trough PB |
- No Buy/Overweight or Underweight/Sell conclusion is complete without linking rating triggers to hog ASP, complete cost, breeding-sow inventory, OCF, leverage, and current-market-cap implied hog price.
- The scenario table must be monotonic in economic logic: a positive-spread recovery case cannot have a selected fair-value range below a worse loss-making stress case unless the report explicitly explains why PB support disappears.
- Use PE only on normalized cycle earnings. Do not use TTM PE or a one-year trough/peak EPS as the primary hog-breeder valuation anchor.

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 汾酒 | period=annual filing; revenue=37441361212.24 filing table unit not explicit in extracted row; revenue_weight=100.0%; growth=7.72%; gross_margin=75.67% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 青花系列 | period=unspecified; revenue=None 亿元（回款口径）; revenue_weight=47.4%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 玻汾系列 | period=unspecified; revenue=None 亿元（回款口径）; revenue_weight=26.3%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 老白汾系列 | period=unspecified; revenue=None 亿元（回款口径）; revenue_weight=13.2%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 汾酒 | revenue_weight=100.0%; growth=7.72%; gross_margin=75.67%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 青花系列 | revenue_weight=47.4%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 玻汾系列 | revenue_weight=26.3%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 老白汾系列 | revenue_weight=13.2%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | What is the realistic pace of out-of-province market penetration for Qinghua 20 and Laobaifen?; How will the channel inventory cycle play out over the next 3 quarters given the management's destocking pledge?; Can the operating margin recover to 45%+ levels if gross margin stabilises and selling expenses decline as promised?; What is the exact effect of C-terminal red-packet incentives on sell-through volumes? |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | The core Fenjiu segment (97% of revenue) is the overwhelming profit engine. Within it, Qinghua series (especially Qinghua 20) contributes the highest absolute gross profit given its weight and superior margin. Bofen provides volume and cash conversion but dilutes margins. Laobaifen is a transition story. Priority for analysis: Qinghua volume/mix, consolidated gross margin, selling expense control. |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | Direct competitors: national brands (Moutai, Wuliangye, Luzhou Laojiao) and strong regional players (Yingjia, Gujing, Jinshiyuan). Fenjiu competes mainly in the light-aroma niche, which faces less direct taste substitution but still competes for consumer wallet share. The rise of health-conscious alternatives and imported spirits could be a long-term threat. Customer switching is low due to brand loyalty in Shanxi but higher outside. |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | Qualitative claims around out-of-province growth and C-end red-packet efficiency are partially supported by channel checks showing H1 out-of-province slight growth and scan-rate data (30% opening rate for Qinghua 20). However, precise revenue elasticity cannot be quantified without regional sales data. The qualitative narrative needs to be bridged with regional revenue splits and C-end conversion-to-sales metrics, which are currently missing. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | Market capitalisation of 133.7 bn CNY implies a TTM P/E of 12.2x. This suggests the market is already pricing a decrease in earnings (TTM implied profit 10,981 mn vs FY2025 12,246 mn). The base-case 2026E profit of 11,062 mn is very close to implied TTM profit, meaning the market is already pricing flat/down earnings. If the bear case (8,500 mn) materialises, further downside remains. Bull case (12,920 mn) would likely cause a re-rating, but share count missing prevents per-share target. The expectation gap is therefore on timing of recovery and out-of-province success, not on the existence of a profit decline. |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Even if out-of-province expansion succeeds, Fenjiu's low brand awareness outside Shanxi could limit premiumisation and keep margins in check.; The real destocking may take longer than 2 quarters; CFO's 'market benign' language may be optimistic, and a second wave of price cuts could follow.; If the industry downturn extends to 2028, the stock could de-rate to 8x P/E (bear case profit) giving market cap ~68 bn CNY, a substantial downside from current levels. |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | Without a share count, we can only value the firm at equity level. Base case uses P/E 12.0x, near current market P/E, reflecting no re-rating. Bull case applies 15x, consistent with historical mid-cycle valuations. The method does not require DCF as there is insufficient capex data and the baijiu business is asset-light and cash-generative. Risk premium is embedded in the low multiple, justified by industry headwinds. Sensitivity: a 1% permanent shift in net margin could move equity value by ~7-8%. Recovery or further decline of the baijiu cycle is the key variable. |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | As of mid-July 2026, Fenjiu is navigating a baijiu industry correction with product transition. Q1 results showed margin compression but very strong cash generation. The market appears to be pricing a flat to slightly down profit year. The investment case hinges on two turnarounds: out-of-province growth recovery and gross margin stabilization. Given the lack of share count data, we cannot give a per-share valuation, but the equity value (132.7 bn in base) offers limited premium to current market cap (133.7 bn), suggesting full pricing. Downside protection is provided by the current low P/E and strong balance sheet, but catalysts are still developing. The underwriting packet should be update |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE02 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE03 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 14923228703.48 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 75.0468% / -3.75pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 36.0683% / -4.16pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / -0.0283% / +0.00pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.5334 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年第一季度报告: 衍生金融资产 应收票据 应收账款 93,685.45 96,807.50 / receivables: 2026年第一季度报告: 应收票据 应收账款 93,685.45 96,807.50 / Use a... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年第一季度报告: 衍生金融资产 应收票据 应收账款 93,685.45 96,807.50 / receivables: 2026年第一季度报告: 应收票据 应收账款 93,685.45 96,807.50 / Up... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年第一季度报告: 其他债权投资 长期应收款 长期股权投资 121,799,888.28 118,769,623.60 / long_term_equity_... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2025, 年度, 2030 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 2025年年度报告: 艺全方位提升。产能建设全速推进，2030 技改项目、汾青基地项目稳步实施。品质标准全面升级， 科技成果通过鉴定，获 4 项科技奖励、6 项授权专利、2 项软件著作权，成功... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年第一季度报告: 公允价值变动收益（损失以“-”号 填列） 信用减值损失（损失以“-”号填列） -160,825.96 -4,02... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年第一季度报告: 衍生金融资产 应收票据 应收账款 93,685.45 96,807.50 / receivables: 2026年第一季度报告: 应收票据 应收账款 93,685.45 96,807.50 / Contract liabilities and payables c... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 营业外收入 6,889,151.48 3,959,234.86 74.00 营业外支出 18,371,... |
| EV052 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 12.1715 / earnings multiple the market is paying now / |
| EV053 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.6008 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 0.0002% / -0.00pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |
| EV010 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Inventory / revenue / 22.8675% / +3.99pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 汾酒 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=37441361212.24 (filing table unit not explicit in extracted row); revenue weight=100.0%; growth=7.72%; gross margin=75.67%; margin change=-1.4pp; source=filing_intelligence; mode=deterministic_filing_row |
| 青花系列 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (亿元（回款口径）); revenue weight=47.4%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| 玻汾系列 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (亿元（回款口径）); revenue weight=26.3%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| 老白汾系列 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (亿元（回款口径）); revenue weight=13.2%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 133659277752 / current equity value / / / PE TTM / 12.1715 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
| / 2026-07-12 20:08:00 / 新浪财经 / 大降超60%！白酒业首份半年度业绩预告来了，舍得酒业预计上半年业绩同比下降超60% / N/A / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - Treat official earnings guidance, performance previews, and quick reports as harder evidence than run-rate extrapolation; reconcile stated H1/Q1/Q2/EPS ranges before writing forecast, valuation, rating, or next-verification language. | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
- If official guidance conflicts with the prior run-rate or sell-side/proxy assumption, update the forecast or state the exact reason it cannot be used. Do not ignore the guidance.
- After guidance is available, the next verification point is the formal report's segment mix, cost bridge, cash conversion and balance-sheet quality, not whether the guided profit strength exists.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Shared Company Underwriting Packet
- Research readiness: partial
- Readiness reasons: Diluted share count not available from Tushare or market price; EPS and per-share valuation cannot be calculated.; Detailed capex and FCF data not supplied; cannot complete cash-flow forecast.; Product-level revenue and margin only from channel checks (回款口径) and not from filings.; Forecast still functional for revenue, gross/operating margin, and parent profit; bull/base/bear scenarios can be built on these variables.; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 玻汾系列, 老白汾系列, 青花系列; Bull/base/bear per-share valuation is incomplete.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Sum over products (Sales volume × ex-factory ASP) + other sales.  Volume is mainly a function of brand acceptance, channel inventory dynamics, and promotional intensity.  ASP reflects product mix (premiumisation) and pricing power.
- Profit: Gross profit = Revenue – cost of goods (mainly grain, packaging, labour, depreciation).  Operating profit = Gross profit – selling (incl. channel incentives, advertising, C-terminal red-packet scanning) – administrative expenses – R&D.  Net profit parent = Operating profit + net financial income (low leverage) – income tax (~25%).  Working capital is very light (receivables ≈ 0).
- Cash flow: OCF ≈ Net profit + depreciation – change in working capital (mostly inventory).  Since receivables are negligible and payables are moderate, pre-payments to suppliers grow with capacity build.  Inventory build can be a cash drag.  Investing cash outflow = capex for capacity expansion (e.g., 2030 project) and maintenance.  Financing outflow = dividend payments.
- Reinvestment: Light-asset nature but requiring long-ageing storage and brand-building.  Major capex underway (2030 technical upgrade project) to expand base-liquor capacity.  Maintenance capex is modest relative to operating cash flow.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | Can out-of-province growth accelerate in 2027-2028, offsetting Shanxi saturation and driving a return to >5% revenue growth? | Out-of-province growth slightly positive in 2026H1, with company targeting 'third brand' status. Momentum moderate. | Consolidated revenue growth rate, Revenue share from out-of-province regions | Consolidated revenue, Gross margin (if Qinghua mix improves) | Out-of-province sales data by region from company, Channel inventory and sell-through data beyond Shanxi; Obtain company revenue split by province/region in 2026 annual report. |
| Q2 | Will the product mix shift towards mid-price Qinghua 20 and Laobaifen permanently lower the blended gross margin, or can margin recovery occur with scale and premiumisation re-acceleration? | Q1 2026 gross margin fell 3.75pp YoY to 75%, driven by higher share of Qinghua 20 and Bofen, and lower Qinghua 30 volume. | Blended gross margin, Product mix (share of Qinghua 20/30, Bofen) | Gross profit, Operating profit, EPS | Product-level gross margin from filings, Volumes by SKU; Request segmented gross margin data from company IR. |
| Q3 | Is the current channel inventory level (2-3 months) truly healthy, or are we seeing hidden inventory accumulation that will delay a return to sell-in growth? | Channel checks report 2-3 months inventory (Jul 2026), Q2 destocking is underway. Management aims for benign market development. | Channel inventory months, Revenue growth (sell-in) vs. sell-through growth | Revenue, Working capital | Actual sell-through volumes from company, Detailed distributor inventory by region; Track sell-through data and company commentary on inventory at H1 2026 results. |
| Q4 | What is the future trajectory of selling expenses and the 'cost-to-sales ratio', given the shift towards C-terminal red packets and brand-building? | Management claims a slow decreasing trend in cost-to-sales ratio (费销比), focusing more on C-end incentives. Q1 operating margin fell sharply due to lower gross margin, not necessarily higher SG&A. | SG&A ratio, Operating margin | Operating profit, Net profit | Exact selling expense ratio history and forecast, Breakdown between C-end and channel spending; Analyse H1 2026 income statement for selling expense trends. |
| Q5 | Will capex for the 2030 technical upgrade project cause a significant drag on free cash flow and returns in 2026-2028, or will it be well-covered by operating cash flow? | Evidence shows 2030 project is ongoing; prepayments for capacity projects increased significantly in 2025. No recent capex numbers available. | Capex, FCF, ROIC | FCF, DPS, ROIC | Detailed capex schedule and budget for 2030 project, Current capitalised assets and depreciation; Review 2025 annual report cash flow statement for capex and CIP details. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 38718.3 | 36062.3 | 37144.2 | 38629.9 | Year 1 = seasonality-adjusted Q1 2026 (Q1 rev / 48.7% median share).  Year 2 +3%, Year 3 +4% as destocking ends and out-of-province expansion resumes. | calculated | +1% revenue = ~387 mn CNY;  |
| consolidated | Gross margin | % | 75.0 | 74.5 | 74.8 | 75.0 | Year 1 reflects mix shift and margin pressure from product transition.  Gradual recovery as premiumisation resumes. | analytical | 1pp gross margin = ~387 mn gross profit; Product-level gross margin |
| consolidated | Operating margin | % | 45.0 | 41.0 | 42.5 | 43.5 | Operating margin = gross margin – SG&A ratio – R&D ratio.  SG&A ratio assumed ~33% in 2026E, gradually declining. | analytical | 1pp operating margin = ~360 mn operating profit on 2026E revenue; Detailed SG&A breakdown, Management's cost-to-sales target |
| consolidated | Operating profit | CNY mn | 17423.2 | 14785.5 | 15786.3 | 16804.0 | Revenue × operating margin | calculated | ;  |
| consolidated | Net profit parent | CNY mn | 12246.3 | 11061.7 | 11355.8 | 11820.4 | Operating profit + net financial income (immaterial) – tax ~25% | calculated | 1% revenue change = ~110 mn net profit impact in 2026E;  |
| consolidated | EPS (diluted) | CNY | None | None | None | None | Not calculable; diluted share count missing. | missing | ; Total diluted share count |
| consolidated | OCF | CNY mn | 16995.0 | 16592.5 | 17033.7 | 17730.6 | Assumes OCF/NI ratio ~1.5 (Q1 2026 observed).  Applied to net profit parent.  Base year assumed 1.5 ratio. | analytical | 10% change in ratio swings OCF by ~1.6 bn; Cash flow statement details |
| consolidated | Capex | CNY mn | None | None | None | None | Missing; major 2030 project expenditure unknown. | missing | If capex = 3,000 mn p.a., FCF would be 13,592 mn in 2026E; Capital expenditure schedule, Cash paid for construction/fixed assets |
| consolidated | FCF | CNY mn | None | None | None | None | OCF - capex | missing | ; Capex |
| 汾酒 | Revenue | CNY mn | 37441.4 | 34800.0 | 35844.0 | 37277.8 | Proportional to consolidated revenue (segment weight ~96.7%).  Year 1 reduction mirrors total revenue drop. | analytical | ; Segment-level official forecast |
| 其他酒类 | Revenue | CNY mn | 1151.4 | 1262.3 | 1300.2 | 1352.1 | Slight growth as health liqueur gains traction; assumes ~10% growth in 2026E, slowing. | analytical | ;  |
| consolidated | eps |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 无直接关联于汾酒的具体假设 |
| KPE02 | consolidated | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 无直接关联于汾酒的具体假设 |
| KPE03 | 青花系列 | revenue_growth | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 基数 |
| KPE03 | consolidated | channel_inventory | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 绝对库存水平 |
| KPE03 | consolidated | sg&a_ratio | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 费销比数值 |
| KPE04 | consolidated | revenue_growth | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | Q1实际值 |
| KPE04 | consolidated | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 省外增速绝对值 |
| KPE05 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | none |
| KPE06 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | none |
| KPE07 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | none |
| KPE08 | 青花系列 | wholesale_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 批价变动趋势 |
| KPE09 | consolidated | revenue_growth | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | Q1绝对数值 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-13T08:13 | 高时效/1天 | 未披露 | [玫瑰]山西汾酒：预计Q2业绩表现或与Q1接近，全年不追求硬性高增，26年1-5月省内动销同比下滑约10%，省外略有增长 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 国泰海通/2026-06-30T18:58 | 有效窗口/14天 | 未披露 | 未提取到带期间的明确盈利预测 | （6）白酒基本面及估值探底，推荐率先出清标的：迎驾贡酒、今世缘、金徽酒、古井贡酒、珍酒李渡、舍得酒业及价格弹性标的：贵州茅台、五粮液、泸州老窖、山西汾酒 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-06-28T20:10 | 有效窗口/16天 | 未披露 | 未提取到带期间的明确盈利预测 | 推荐格局清晰、率先改善且估值&筹码结构有优势的地产酒板块，推荐今世缘、迎驾贡酒、金徽酒、古井贡酒，中长期推荐竞争力强标的，如贵州茅台、山西汾酒、泸州老窖等，弹性品种关注珍酒李渡、酒鬼酒等 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 机构未识别/2026-06-16T18:12 | 有效窗口/28天 | 未披露 | 山西汾酒股东大会调研更新：青2... 山西汾酒股东大会调研更新：青2... 山西汾酒股东大会调研更新：青20&玻汾动销优异，预计Q2业绩延续Q1表现（20260616） 业绩展望：预计Q2业绩表现或与Q1接近，仍处调整出清阶段 / 周期展望：预计26-27年行业见底 / 库存情况：Q2继续去库存&当前库存相对合理，预计报表增速慢于实际动销 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
- Do not average incompatible forecast years, valuation dates or methods.
- A range or median may be called consensus only when a named multi-broker sample and statistical basis are supplied.

## Mandatory Three-Year Table
| item | 2026E | 2027E | 2028E | evidence / assumption status |
| --- | --- | --- | --- | --- |
| Revenue | to be estimated | to be estimated | to be estimated | reconcile segment volume, ASP, mix, and eliminations |
| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |
| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |
| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |
| Operating cash flow / capex / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and reinvestment |

## Analyst Instructions
- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.
- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.
- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.
- If an official earnings preview, guidance or quick report is available, it overrides run-rate extrapolation for the covered period until the formal report supplies segment, cash-flow and balance-sheet detail.
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.