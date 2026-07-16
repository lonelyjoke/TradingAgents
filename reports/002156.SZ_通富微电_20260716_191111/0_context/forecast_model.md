# Forward Forecast Model Scaffold for 002156.SZ as of 2026-07-16

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 7481674677.05 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 13.3247% / +0.13pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 2.2446% / +0.23pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 2.8615 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 18.1068% / -2.00pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 16.0769% / +2.69pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 半导体封测 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: semiconductor equipment / wafer-fab tools. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
| control | Mandatory treatment |
| --- | --- |
| Business buckets | split mature/core products from product-cycle, technology-node, customer, or tool-category optionality; do not bury optionality inside the base multiple |
| Operating bridge | start from sector-native volume x ASP x mix, then explicitly bridge gross margin, R&D, working capital, capex and share count |
| Foundry / manufacturing | use wafer capacity, utilization, wafer ASP, node mix, yield, depreciation, capex, construction-in-progress transfer, and equipment access |
| Chip design | use shipments, ASP, design wins, tape-out/mass-production milestones, customer concentration, foundry/package cost, inventory and R&D/IP moat |
| Semiconductor equipment | use new orders, backlog, delivery/acceptance, tool-category mix, localization rate, installed base/service, inventory, advances and receivables |
| Valuation triangulation | PE is only one cross-check. Also show EV/EBITDA, DCF/FCF, ROIC/PB or SOTP/NAV depending on asset intensity and disclosure |
| Optionality discipline | AI, advanced node, localization or strategic-scarcity value must have explicit probability, payoff, verification gate and overlap key; unverified optionality cannot enter base value |
| Market-implied check | reverse current market cap into required revenue, gross margin, net profit, ROIC, backlog conversion or node/product contribution; compare with the model |
- A semiconductor Buy/Underweight call is incomplete if it relies only on static PE/PB or valuation percentiles without the operating bridge above.

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 半导体封测 | period=2025年度/2026Q1; revenue=27921424656.15 CNY; revenue_weight=100.0%; growth=16.92%; gross_margin=13.3247% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 半导体封测 | revenue_weight=100.0%; growth=16.92%; gross_margin=13.3247%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | What percentage of total packaging revenue is from advanced vs. legacy packaging, and what is the margin differential?; Is AMD's CoWoS-L outsourcing a realistic probability, and what is the capex and timeline?; How sticky are AMD's orders beyond 2027, given competition from TSMC and other OSATs?; Can TFMC sustain >20% revenue growth without dilutive equity issuance? |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | The integrated circuit packaging and testing segment accounts for ~98% of revenue and virtually all profit. Within this, the most important profit pool is advanced packaging (Chiplet, 2.5D, CoWoS) because it carries 2-3x the ASP and higher margin than traditional packaging. However, without segment disclosure, we estimate advanced packaging contributes maybe 20-25% of 2025 revenue but a disproportionate share of gross profit. The second pool is traditional packaging for AMD's CPU/GPU, which is volume-driven with lower margins but steady cash generation. The mold/material sales pool is negligible. Therefore, the model's sensitivity is entirely driven by the advanced packaging ramp and the CoW |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | True peers are JCET, ASE Group, and Amkor for OSAT advanced packaging; TSMC for CoWoS in-house. TFMC's differentiator is its exclusive AMD JV relationship and growing domestic customer base. However, switching risk remains: AMD could bring more backend in-house or use TSMC's integrated service for high-end chips. Substitution risk from chiplets moving to hybrid bonding or direct copper interconnects could alter packaging requirements. Domestic OSATs like JCET also investing heavily in advanced packaging, posing competitive threat for domestic AI chip orders. Supplier diversification is moderate: TFMC depends on substrates and gold wire suppliers, but can source from multiple regions. New ent |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | Qualitatively, the market narrative is that TFMC is the purest AMD AI leap play, with upside from CoWoS. Quantitatively, we have an H1 2026 profit range of CNY 16-18 bn, which annualizes to ~32-36 bn. But that includes one-off items; normalized core profit is lower. Without capex and tax data, we cannot build a full DCF. Our bridge takes the H1 run-rate, applies a full-year multiplier of 1.85x (considering H2 is stronger), yields CNY 29-33 bn revenue. We then apply an improving net margin (from 4.4% in Q1 to ~5.5% for the year) to arrive at a parent profit of ~CNY 1.6-1.8 bn for 2026E. The model's gap is the lack of segment-level margins and cash flow inputs. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | At current market cap ~CNY 119 bn and PE TTM 82.6x, the market appears to be pricing in the bull scenario (rapid advanced packaging growth and CoWoS win). Our base-case equity value of CNY 105 bn (25x 2027E) suggests the stock is approximately fair, while the probability-weighted value (using only the base/bear/bull scenarios we built) is ~CNY 98 bn, implying slight overvaluation unless bull case materializes. The gap is timing and magnitude: the market is assigning high probability to CoWoS that the company has not yet confirmed. The bear scenario (CNY 36 bn) shows significant downside if AMD relationship disappoints. |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Counter to bullish AMD thesis: 'AMD's current CoWoS demand is only a fraction of NVIDIA's, and the spike in 2027 is based on analyst estimates. If AMD's Venice or MI455 ramp disappoints, demand could be cut 30-40%, and TSMC will keep the high-end CoWoS in-house, leaving TFMC with legacy packaging only.'; Counter to bearish single-customer risk: 'AMD's roadmap and market share gain in server CPU is durable; even a 20% downside in 2027 CoWoS would still leave TFMC with high-double-digit revenue growth, and the company could easily fill capacity with domestic AI chip customers at better margins than legacy packaging.' |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | Valuation is a function of the earnings bridge: we use scenarios to map the operating assumptions to net profit, applying a PE multiple that reflects the growth and risk profile. For the base case, a 25x PE on 2027E net profit of CNY 4.2 bn yields CNY 105 bn. The bull case uses a higher multiple (30x) and adds CoWoS option value, while bear uses a depressed 15x. Multiples are subjective but consistent with historical trading range and peer comparison. The key risk premium variable is the probability of AMD CoWoS; without that, the stock should trade closer to peers like JCET (15-20x). Sensitivity: 1% change in operating margin translates to ~CNY 300 mn in operating profit, around CNY 0.15 EP |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | TFMC is a pure-play bet on AMD's AI silicon boom and the structural shift to advanced packaging. While the company's H1 2026 profit explosion supports a strong operational momentum, the thesis hinges on two unconfirmed variables: AMD's outsourcing of CoWoS-L and the sustainability of margin improvement. Our scenario analysis shows that at the current valuation, the market is giving credit to the bull case, leaving limited margin of safety. A cautious PM would demand official confirmation of CoWoS plans and evidence of expanding non-AMD customer base before adding. The investment boils down to whether you believe the sell-side narrative that AMD is desperate for alternative CoWoS capacity and |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | net profit / EPS | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 7481674677.05 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 13.3247% / +0.13pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 4.3982% / +2.73pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 2.2446% / +0.23pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 2.8615 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | valuation | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / prepayments: 2026年一季度报告: 交易性金融资产 92,633,474.32 0.00 不适用 融资产所致。 预付款项 92,589,379.46 69,942,264.47 32.38% 主要系预付材料款余额增加所致。 / prepaym... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction_in_progress: 2026年一季度报告: 预付款项 92,589,379.46 69,942,264.47 32.38% 主要系预付材料款余额增加所致。 主要系公司业务量增长，增加中高 在建... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 2025年年度报告: 术、新工艺、新产品无法如期产业化风险，主要原材料供应及价格变动风险， 汇率风险，国际贸易风险，敬请广大投资者注意投资风险。 公司经本次董事会审议通过的利润分配预案为：以公... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 通富微电子股份有限公司 2026 年第一季度报告 主要系本期计提坏账准备，而去年同 信用减值损失 -4,375,6... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 华特、纳芯微、汇顶科技、思瑞浦、杰理科技等近 40 家客户的嘉奖。此外，客户还针对产品线、销售、工程、... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 7/9; core pack ready. Annual base text and quarterly chec... |
| EV043 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV044 | company_events | research_context | reported | valuation | 20260715, 2026, 半年 | / 20260715 / earnings guidance / performance preview / 002156.SZ / 通富微电 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002156&announcementId=1225423192&orgId=9900003427&announcementTime=2026-07-15 / |
| EV053 | company_events | research_context | reported | segment_margin | unspecified | <!DOCTYPE html> <html lang="zh-CN"> <!-- 公共头部样式 --> <head> <meta charset="utf-8"> <meta name="format-detection" content="telephone=no"> <meta name="author" content="深圳证券信息有限公司"> <meta name="renderer" content="webkit"> <meta name="X-UA-Compatible" content="IE=e |
| EV055 | company_events | research_context | reported | revenue | 2026-07-15 | / 2026-07-15 20:16:57 / 财联社 / 美国半导体设备公司盘前急涨30% 预计下一财年营收最高翻3倍 / N/A / |
| EV058 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 82.5857 / earnings multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 半导体封测 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年度/2026Q1; reported revenue=27921424656.15 (CNY); revenue weight=100.0%; growth=16.92%; gross margin=13.3247%; margin change=0.13pp; source=filing_intelligence; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 119450051999 / current equity value / / / PE TTM / 82.5857 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
| / earnings guidance / performance preview / 1 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260715 / earnings guidance / performance preview / 002156.SZ / 通富微电 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002156&announcementId=1225423192&orgId=9900003427&announcementTime=2026-07-15 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260715 / 002156.SZ / 通富微电 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002156&announcementId=1225423192&orgId=9900003427&announcementTime=2026-07-15 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260714 / sina / N/A / N/A / 【赛伍技术：预计2026年上半年亏损300万元-600万元，同比减亏92%-96%】赛伍技术公告，预计2026年半年度实现归属于上市公司股东的净利润为-300万元至-600万元，与上年同期亏损7209.61万元相比减亏92%-96%；预计扣除非经常性损益后的净利润为-500万元至-900万元，同比减亏88%-93%。业绩减亏主要因传统光伏材料业务毛利率提升、海外胶膜业务营收占比增长，叠加新兴业务板块（锂电PACK、电子电力材料、半导体材料）营收显著增长，以及收购今蓝纳米后协同效应逐步显... | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: Diluted share count not reported or derivable from supplied evidence; EPS and per-share valuation remain unresolved.; No segment-level revenue or margin disclosure for advanced packaging vs. legacy packaging; product mix assumptions are analytical only.; Cash flow statements not included in evidence; OCF, capex, and FCF derived from indirect indicators (OCF/net profit ratio, CIP growth) remain provisional.; KPE evidence (H1 2026 profit guidance) is unverified private proxy; baseline consensus missing, so model uses midpoint 17 bn CNY.; CoWoS capacity plan (KPE10) is unconfirmed by the company; placed in optionality bucket, not base case.; One or more filing-reported segments required deterministic restoration.; Material segment three-year driver lines are missing: 半导体封测; Bull/base/bear per-share valuation is incomplete.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ (Packaging volume_k x ASP_k) + testing service revenue + minor mold/material sales. ASP increases with higher-end packaging (advanced vs. traditional), and volume is gated by capacity and utilization.
- Profit: Gross profit = Revenue - (direct materials, labor, depreciation, electricity, subcontracting). Operating profit = Gross profit - R&D - SG&A. Recent operating leverage driven by utilization improvement, mix shift to advanced packaging, and cost control. Net profit includes investment income, government grants, and forex gains/losses.
- Cash flow: OCF = Net income + depreciation/amortization ± working capital changes. Historically OCF/Net profit >2.5x, indicating strong depreciation add-back and moderate working-capital management. FCF = OCF - capex (primarily facility expansion in Penang and domestic advanced lines).
- Reinvestment: Capex intensive: requires continuous investment in cleanrooms, equipment (bumping, wafer-level, flip-chip, testers). Construction in progress rose 31.95% YoY in Q1 2026 to CNY 4.1 bn, signaling major capacity expansion. ROIC will improve if new capacity ramps with high utilization.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | What is the exact advanced packaging revenue contribution and margin profile vs. legacy packaging? | Unresolved; company does not disclose packaging type split. | segment_volume, asp_or_price, segment_margin | Revenue mix, Gross margin, Operating profit, EPS | Advanced packaging revenue % and gross margin, Traditional packaging margin; 2026 semi-annual report; direct inquiry with IR. |
| Q2 | Will AMD allocate CoWoS-L volume to TFMC, and at what scale? | Unconfirmed; company declined to comment on specific CoWoS plans. | utilization_or_backlog | Revenue (new line item), CapEx, FCF, EPS | Official company statement or signed customer agreement., Equipment order data.; AMD upcoming product launch (July 22); TFMC announcements or analyst day. |
| Q3 | What is the post-2026 normalized operating margin run-rate, and how much of the H1 2026 margin surge is sustainable? | Partially resolved: Q1 margin improvement is partly mix/shift and cost control, not purely one-off. But sustainability depends on advanced packaging ramp. | segment_margin, operating_margin_pct | Gross margin, Operating margin, Net margin, EPS | Normalized depreciation schedule, Mix-adjusted margin sensitivity; 2026 semi-annual report; management commentary on margin outlook. |
| Q4 | Can the company maintain cash conversion above 2x OCF/Net profit while capex is still accelerating? | Uncertain: Q1 OCF/NP 2.86x but capex likely high. Private placement approval suggests capital needs. | capex_or_roic, cash_conversion_ratio | Operating cash flow, Capex, Free cash flow, EPS (dilution) | Statement of cash flows, Capital expenditure 2025 actual and 2026 plan; 2026 semi-annual report cash flow statements; company capex guidance. |
| Q5 | What is the impact of the private placement on share count and EPS? | Unresolved: size and pricing not disclosed. | diluted_share_count_mn | EPS, FCF per share, Valuation | Placement size, number of shares, issue price; Announcement of placement details. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 27921.4 | None | None | None | Base 2025 revenue × (1 + growth rate); growth driven by capacity expansion and mix. | missing | Varies with advanced packaging ramp, CoWoS optionality, and forex.; Assumed growth percentages for 2026E-2028E |
| consolidated | Gross Margin | % | 13.3247 | None | None | None | Blended margin improves if advanced packaging share rises; partially offset by depreciation. | missing | Advanced packaging penetration, pricing power, gold/substrate costs.; Gross margin by product type |
| consolidated | Operating Margin | % | 6.2765 | None | None | None | GM - (SG&A+R&D)/Rev. Leverage effect from revenue growth. | missing | Revenue scale, cost control, R&D intensity.; Fixed vs variable SG&A structure |
| consolidated | Operating Profit | CNY mn | None | None | None | None | Revenue × Operating Margin | missing | Tied to revenue and margin assumptions.; Revenue and margin forecasts |
| consolidated | Parent Net Profit | CNY mn | 1218.7 | None | None | None | (Operating Profit + non-operating items - tax - minority) ≈ Operating Profit × (1 - tax) adjusted for non-recurring items. | missing | Operating margin, tax rate, non-recurring items (investment income, government grants).; Effective tax rate, Non-operating income projection |
| consolidated | EPS | CNY | None | None | None | None | Parent Net Profit / Diluted Share Count | missing | Profit and share count both uncertain.; Parent net profit forecast, Diluted share count |
| consolidated | Operating Cash Flow | CNY mn | None | None | None | None | Parent Net Profit × OCF/NI ratio (historical ~2.5-2.9x), but depends on working capital. | missing | Net profit, working capital movements.; Full cash flow projection |
| consolidated | CapEx | CNY mn | None | None | None | None | Capex/revenue ratio historically ~15-20%, potentially rising with Penang expansion. | missing | CoWoS or advanced packaging capacity plans.; Actual capex outflows |
| consolidated | Free Cash Flow | CNY mn | None | None | None | None | OCF - CapEx | missing | OCF and CapEx paths.; OCF and CapEx forecasts |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | 半导体封测 | profit_or_eps | None CNY 亿 | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 市场对该股2026H1净利润的一致预期, Q1实际净利润作为基数 |
| KPE02 | 半导体封测 | profit_or_eps | None CNY 亿 | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 市场一致预期基数, 扣非净利拆分 |
| KPE03 | 半导体封测 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 先进封装收入占比, 产能利用率具体数据 |
| KPE04 | 半导体封测 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 国产算力对先进封装的需求弹性, 通富微电在先进封装市场的份额 |
| KPE06 | 半导体封测 | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 先进封装ASP趋势, 毛利率与ASP相关性 |
| KPE07 | 半导体封测 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 先进封装业务量增长数据 |
| KPE08 | 半导体封测 | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 行业供需平衡表 |
| KPE09 | 半导体封测 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 超节点对封测订单的具体拉动量 |
| KPE10 | 半导体封测 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | CoWoS-L产能规划官方确认, 海外产能建设资本开支计划, AMD CoWoS需求分配细节 |
| KPE05 | 半导体封测 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-15T08:09 | 高时效/1天 | 未披露 | 全志科技披露半年预告，扣非净利4.35-4.65亿元，yoy+222.46%-244.70%，公司通过产品调价对冲上游原材料成本压力，AI硬件、平板产品线持续放量 📍板块内AIoT与传统消费电子业务景气度分化，下半年端侧芯片企业有望延续高增态势，重点跟踪终端爆款落地节奏，板块或存在整体性行情机会 🔥先进封装：算力Chiplet、2.5D/3D先进封装需求维持高景气，行业企业扩产规划积极，板块上半年量利同步向好 📌通富微电26H1归母净利润16-18亿元，yoy+288.26%-336.8%，业绩落地符合前期乐观预判 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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