# Forward Forecast Model Scaffold for 600309.SH as of 2026-06-30

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 54052165361.36 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 14.728% / -0.98pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.3776% / +0.04pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.8444 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 6.9575% / -1.27pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 13.2852% / -2.77pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Cathode / material revenue | shipment volume x cathode ASP | LFP/ternary demand, customer order cadence, pass-through clauses |
| Manufacturing spread | cathode ASP - lithium carbonate / precursor / energy / processing cost | raw-material price, inventory-cost lag, processing fee |
| Gross profit | shipment volume x unit spread | capacity utilization, yield, depreciation, product mix |
| Operating profit | gross profit - R&D - SG&A - credit impairment | customer concentration, receivables, scale leverage |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | OCF/NI, inventory, capex, expansion cycle |

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | 产品报价、毛利率、竞品价格、下游接受度、行业价格指数 | numeric assumption delta or explicit rejection |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 54052165361.36 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 14.728% / -0.98pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 6.878% / -0.28pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.3776% / +0.04pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.8444 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 万华化学2026年一季度报告: 稀释每股收益（元/股） 21.43 主要系销售商品收到的现金增加 经营活动产生的现金流量净额 1,079.87 / receivables: 万华化学2026年一季度报告: 交易性金融资产 |
| EV031 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 万华化学2026年一季度报告: 稀释每股收益（元/股） 21.43 主要系销售商品收到的现金增加 经营活动产生的现金流量净额 1,079.87 / receivables: 万华化学2026年一季度报告: 交易性金 |
| EV033 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 万华化学2026年一季度报告: 稀释每股收益（元/股） 21.43 主要系销售商品收到的现金增加 经营活动产生的现金流量净额 1,079.87 / receivables: 万华化学2026年一季度报告: 交易性金... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 万华化学2026年一季度报告: 稀释每股收益（元/股） 21.43 主要系销售商品收到的现金增加 经营活动产生的现金流量净额 1,079.87 / receivables: 万华化学2026年一季度报告: 交... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 万华化学2026年一季度报告: 其他债权投资 长期应收款 1,365,197,292.16 1,393,683,356.10 长期股权投资 12,022,740,3... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 万华化学2026年一季度报告: 59,327,994.40 18,554,815.44 号填列） 信用减值损失（损失以“-”号填 / im... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 万华化学2026年一季度报告: 交易性金融资产 2,502,946,515.31 衍生金融资产 201,799,421.05 215,765,494.47 应收票据 / receivables: 万华化学2026年一季度报告: 衍生金融资产 201,799,421.05 215,765,4... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade partial; reports seen annual/quarterly/semiannual; answered 9/9; core pack thin. Readable filings exist, but either ... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | segment_volume | 2025, 年度 | / product_manufacturer / 产品制造 / 产能出货型 / quantified disclosure / 万华化学2025年年度报告: 报告期内公司新增重要非主营业务的说明 □适用 √不适用 二、报告期内公司所处行业情况 2025 年，国际环境错综复杂，地缘政治冲突多发频发，单边主义、保护主义逆流 涌动，对国际经贸秩序造成严重冲击，全球经济增速继续放缓。受市场需求疲软、贸 易阻碍增多、关税壁垒升级等因素的影响，石化化工行业供过于求的结构性矛盾更加 凸显，市场竞争加剧。 尽管外部环境变化带... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 16.2697 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 0.9997 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=54052165361.36 (CNY); revenue weight=None%; growth=None%; gross margin=14.728%; margin change=-0.98pp; source=earnings_model; mode=llm_semantic |
| 聚氨酯 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| 石化 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=industry_kpi; mode=llm_semantic |
| 精细化学品与新材料 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 化工行业 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=201109817784.79 (filing table unit not explicit in extracted row); revenue weight=100.0%; growth=11.88%; gross margin=13.48%; margin change=-2.61pp; source=filing_intelligence; mode=deterministic_filing_row |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 214155562156 / current equity value / / / PE TTM / 16.2697 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Shared Company Underwriting Packet
- Research readiness: partial
- Readiness reasons: Key segment-level revenue/margin for polyurethane, petrochemical and fine chemicals are not disclosed separately; only a broad 'chemical industry' segment and tiny 'other' segment are reported. Without product-level economics the model cannot fully reflect polyurethane cycle or new-material contr...; Diluted share count is not supplied and cannot be reliably calculated from the evidence; equity per-share values, EPS and per-share valuation closure remain open.; Capex, OCF and FCF data are unavailable for FY2025 or Q1 2026; the reinvestment and cash-flow equations are placeholder.; External industry data for MDI price, capacity, utilization, and new-material ASP/margin are missing; the causal chain from demand to cash flow remains evidence-limited outside of company-level margin and revenue.; Market price is available only as aggregate market cap, and share count missing makes current price and expected return unquantified.; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Three-year values remain missing for consolidated line(s): capex, eps, fcf, gross_margin, ocf, operating_profit, parent_net_profit, revenue
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 营业收入 = Σ(产品销量i × ASPi) ，其中主要产品类别为MDI/TDI聚氨酯、石化产品和精细化学品/新材料；贸易业务亦提供约10%收入
- Profit: 毛利 = 营业收入 – [原材料成本(苯、丙烯、煤等) + 能源 + 折旧 + 其他制造成本]； 营业利润 = 毛利 – 销售管理费用 – 研发费用； 归母净利润 = 营业利润 – 财务费用 – 所得税 ± 非经常性损益
- Cash flow: 经营活动现金流 = 归母净利润 + 折旧摊销 ± 营运资本变动； 自由现金流 = 经营现金流 – 资本开支（含在建工程转固后的新增资本支出）； 由于持续的产能建设，FCF 常常为负或低
- Reinvestment: 固定资产和在建工程规模极大，资本密集度很高；每年研发投入48.65亿元（2025年），大量项目进入建设和爬坡期，回报率取决于新产能的产能利用率、产品价差和下游需求

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q01 | 万华化学在MDI领域的成本优势能否在竞争对手产能扩张和原料成本上升的环境下持续？这直接决定聚氨酯业务的毛利率底线和市场份额。 | unresolved | 化工行业毛利率, 聚氨酯分部毛利率（需拆分）, MDI出口价格指数 | 化工行业收入, 化工行业毛利, 归母净利润, 每股收益 | 公司相对同行的MDI单吨成本比较, 原料成本指数化的具体比例, 出口合同价格证据; 获取第三方MDI行业报告和海关出口数据，并在下一次年报中寻找分部毛利率披露 |
| Q02 | 全球MDI/TDI供需格局何时能从供过于求转为平衡，公司聚氨酯均价何时能迎来拐点？ | unresolved | MDI均价假设, 销售收入增长率, 化工行业毛利率 | 化工行业收入, 毛利, 营业利润, 自由现金流 | MDI行业开工率和库存水平, 海外竞争对手减产消息, 下游冰箱/汽车新订单数据; 跟踪Platts/ICIS MDI价格指数和季度产销公告 |
| Q03 | 公司持续大规模的资本开支（石化、电池材料、新材料）能否带来超过资本成本的回报，还是仅仅是吞噬现金的沉没成本？ | unresolved | 资本开支金额, 新增项目毛利率, 产能利用率, 折旧/摊销对利润的负担 | 自由现金流, 资产负债率, 财务费用, 每股收益（稀释后） | 各重大项目的IRR和回收期, 新增产能的预期产量和成本曲线, 电池材料客户认证进度; 查阅中报或投资者交流记录中关于新项目进展和对财务的影响 |
| Q04 | 公司整体毛利率在2025年大幅下降后，2026年能否触底并温和回升？成本控制和产品结构升级力度是否足以抵消价格压力？ | unresolved | 化工行业毛利率, 营业成本增速, 产品收入结构 | 毛利, 营业利润, 归母净利润, 每股收益 | 分部毛利率趋势, 原材料成本指数走势, 高毛利产品占比; 跟踪Q2 2026季报毛利率并与同期比较 |
| Q05 | 公司电池材料和新材料业务的未来体量能否支撑估值溢价？还是会因为低利润率和激烈竞争成为估值拖累？ | unresolved | 精细化学品/新材料收入占比, 新材料业务毛利率, 资本开支转化率 | 化工行业收入, 毛利, 每股收益, 估值乘数 | 电池材料实际出货量, 客户合同或框架协议, 新材料业务利润率; 等待公司披露新材料业务销售额或关键客户进展 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | CNY mn | 203234.57 | 220000.0 | 240000.0 | 258000.0 | 基于2025年实际203.23bn，假设2026E +8.3%（产能释放和温和需求恢复），2027E +9.1%，2028E +7.5% | 分析师估计 | 每±1%收入变动影响约2.2bn收入;  |
| consolidated | 营业成本 | CNY mn | 175000.0 | 187000.0 | 201600.0 | 215600.0 | 基于2025年毛利率13.48%推算营业成本=收入*(1-毛利率)；2025年收入203.23bn，成本约175.8bn，取175bn；2026E毛利率15%→成本187bn；2027E毛利率16%→成本201.6bn；2028E毛利率16.5%→成本215.6bn | 分析师估计 | 毛利率每+1pp，营业利润增加约2.4bn;  |
| consolidated | 毛利 | CNY mn | 28234.57 | 33000.0 | 38400.0 | 42400.0 | 毛利 = 营业收入 - 营业成本；2025年203.23bn-175bn≈28.23bn | 分析师估计 | ;  |
| consolidated | 毛利率 | % | 13.48 | 15.0 | 16.0 | 16.5 | 保守假定毛利率从2025年低谷逐步修复，2026E 15%（接近Q1实际），2027E 16%，2028E 16.5% | 分析师估计 | 毛利率每+1pp，母净利润增约1.5bn（扣除税费）;  |
| consolidated | 营业利润 | CNY mn | 19000.0 | 23000.0 | 27600.0 | 31000.0 | 营业利润率假设：2025年约9.4% (19bn/203bn)，2026E 10.5%，2027E 11.5%，2028E 12.0%；营业利润 = 营业收入 × 营业利润率 | 分析师估计 | 营业利润率每±0.5pp，营业利润变动约1.2bn;  |
| consolidated | 营业利润率 | % | 9.35 | 10.5 | 11.5 | 12.0 | 基于毛利率恢复和费用控制 | 分析师估计 | ;  |
| consolidated | 归母净利润 | CNY mn | 12527.2 | 15400.0 | 18500.0 | 21000.0 | 净利率假设：2025年6.16% (12.5/203.23)，2026E 7.0%，2027E 7.7%，2028E 8.1%；归母净利润 = 营业收入 × 净利率 | 分析师估计 | 净利率每±0.2pp，归母净利润变动约0.5bn;  |
| consolidated | 净利率 | % | 6.16 | 7.0 | 7.7 | 8.1 | 跟随营业利润率改善，财务费用和税率基本稳定 | 分析师估计 | ;  |
| consolidated | 基本每股收益 | CNY | None | None | None | None | EPS = 归母净利润 / 稀释股本数；因稀释股本数未知，留空 | missing | ; 稀释股本数（百万股） |
| consolidated | 经营活动现金流净额 | CNY mn | None | 28000.0 | 33500.0 | 38000.0 | 参照Q1 OCF/净利润1.84x，假设全年1.8x，2026E OCF = 15400*1.8 ≈ 27720，取28bn；后续保持相似比率 | 分析师估计 | OCF/净利润比率每±0.2，OCF变动约3bn; 折旧摊销及营运资本具体金额 |
| consolidated | 资本支出 | CNY mn | None | None | None | None |  | missing | ; 购建固定资产、无形资产和其他长期资产支付的现金 |
| consolidated | 自由现金流 | CNY mn | None | None | None | None | 自由现金流 = 经营活动现金流净额 - 资本支出；因资本支出缺失，无法计算 | missing | ; 资本支出 |
| consolidated | capex |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | eps |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | fcf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | ocf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | operating_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | parent_net_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | revenue |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | 聚氨酯 | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 产品报价、毛利率、竞品价格、下游接受度、行业价格指数 | 聚氨酯出口需求具体增量, 价格弹性系数, 收入基数 |
| KPE02 | 聚氨酯 | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 具体内容, 量化影响 |
| KPE03 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 万华化学在电容供应链中的角色, 量化影响 |
| KPE04 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 万华化学在电容供应链中的角色, 量化影响 |
| KPE05 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 具体内容, 量化影响 |
| KPE06 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 具体内容, 量化影响 |
| KPE07 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 具体内容, 量化影响 |
| KPE08 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 万华化学在电容供应链中的角色, 量化影响 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

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
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.