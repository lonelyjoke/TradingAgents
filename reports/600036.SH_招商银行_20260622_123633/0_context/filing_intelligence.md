# Financial-report intelligence for 600036.SH as of 2026-06-22

- Company: 招商银行
- Vendor industry: 银行
- Reading profile: banking
- Research hygiene: industry-specific playbooks are conservative by design; if identity is ambiguous, generic questions are safer than a wrong template.
- Financial-report look-back: 900 days
- Extraction status: Financial-report text extraction succeeded.

## Financial Reports Considered
- : 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]
- : 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]
- : 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]
- : 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]

## Financial Report Text Acquisition Audit
| stage | status | detail |
| --- | --- | --- |
| runtime_dependency | ready | pdftotext is available for PDF text extraction. |
| announcement_lookup | failed | anns unavailable: anns unavailable: configured_http_url: 请指定正确的接口名; cninfo announcement fallback unavailable: 404 Client Error: Not Found for url: https://www.cninfo.com.cn/new/hisAnnouncement/query; cninfo announcement ... |
| local_text_cache | ready | Recovered 4 readable report text(s) from local disclosure cache. |
| final_text_bundle | ready | Using 4 cached readable report text(s). |

## Filing Reading Coverage Audit
| coverage_grade | report_types_seen | missing_report_types | answered_questions | core_pack_status | confidence_read |
| --- | --- | --- | --- | --- | --- |
| weak | quarterly | annual/semiannual | 2/5 | ready | Readable text exists but the pack is too thin for a full buy-side read; avoid strong claims about business model, second curve, or execution trend. |

## Internal Filing Quality Modules
| module | purpose | filing_evidence | analyst_use | missing_or_next_check |
| --- | --- | --- | --- | --- |
| accounting_reconciliation | Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. | {'lens': 'retail_wealth_engine', 'report_type': 'quarterly', 'evidence_strength': 'quantified disclosure', 'filing_evidence': '广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 - - 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - -', 'why_it_matters': 'Reta... | Use as the report's source-of-truth layer; flag conflicting cash-flow, profit, leverage, or period claims instead of averaging narratives. | If debate numbers conflict, cite the exact filing period and reconcile revenue, profit, OCF, working capital, and leverage before rating impact. |
| segment_economics_depth | Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | Core segments can support base-case value; thin or header-only second curves stay in SOTP/scenario value. | Require revenue, cost/gross margin, profit or cash-quality evidence by product, channel, geography, or business bucket. |
| footnote_radar | Surface decision-relevant notes that can hide risk or change confidence. | impairment_policy: 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | impairment_policy: 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Use footnotes as valuation modifiers for customer concentration, related parties, guarantees, litigation, impairment, and capitalization choices. | If note evidence is thin, avoid claiming footnote cleanliness; keep guarantees, litigation, impairment assumptions, and related parties on the checklist. |
| cash_flow_quality_decomposition | Separate accounting profit from cash conversion, working-capital drag, and demand visibility. | Not enough direct filing evidence found in the readable report pack. | Upgrade growth only when revenue, margin, OCF, receivables, inventory, and contract liabilities point in the same direction. | Next filing should confirm OCF/net profit, collections, inventory turns, and whether contract liabilities convert at acceptable margin. |
| capex_cip_return_bridge | Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. | Not enough direct filing evidence found in the readable report pack. | Put projects with unclear utilization, payback, or ROIC in scenario value; require demand and margin evidence before base-case valuation credit. | Track commissioning, utilization or occupancy, capex-to-revenue, payback/ROIC, impairment, and disposal gains or losses. |
| mdna_text_change | Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. | risk_language_upgrade: 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | risk_language_upgrade: 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,... | Use text changes to decide whether management is proving, softening, or avoiding a theme; do not let soft wording replace hard evidence. | Compare the next quarterly MD&A against annual/semiannual promises, especially on strategy, project ramp, risks, and cash conversion. |
| non_recurring_profit_quality | Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. | Not enough direct filing evidence found in the readable report pack. | Use this to prevent headline EPS from receiving a core multiple when profit quality depends on non-operating or non-recurring items. | Require a bridge from gross profit/operating profit to net profit, and isolate investment income, fair-value gains, subsidies, disposals, and impairments. |
| balance_sheet_forward_signals | Read balance-sheet leads before income-statement confirmation. | Not enough direct filing evidence found in the readable report pack. | Contract liabilities and payables can signal demand/funding; receivables, inventory, prepayments, debt, and CIP can signal execution burden. | Track whether leading assets/liabilities convert into revenue, margin, and cash rather than reversals, impairments, or financing drag. |
| shareholder_return_authenticity | Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. | Not enough direct filing evidence found in the readable report pack. | Treat shareholder yield as quality only when payout, FCF/OCF coverage, leverage, capex needs, and dilution risk line up. | Verify dividend payout, buyback execution/cancellation, FCF coverage, leverage movement, and whether capital needs crowd out future returns. |
| disclosure_quality_score | Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. | Coverage grade weak; reports seen quarterly; answered 2/5; core pack ready. Readable text exists but the pack is too thin for a full buy-side read; avoid strong claims about business model, second curve, or execution trend. | High disclosure quality raises conviction; weak or partial coverage should cap sizing and push more assumptions into verification. | Improve confidence by retrieving missing annual/semiannual/quarterly text and answering unanswered thesis-critical filing questions. |

## Company-Specific Business Archetype
| archetype_id | archetype_name | evidence_strength | evidence_basis | underwriting_focus |
| --- | --- | --- | --- | --- |
| project_delivery | 项目订单 / 交付回款型 | quantified disclosure | 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股... | 验证订单质量、交付节奏、验收确认、毛利率、应收/合同资产和现金回款。 |
| financial_intermediary | 金融中介 / 资产负债表型 | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三）主要会计数据和财务指标发生变动的情况及原因 ☑适用□不适用 报表项目 本报告期 上年同期/年初数 同比增减 披露原因 财务费用 192,357,034.98 -21,449,464.49 不适用 主要是本期汇兑损失增加 其他收益 36,636,192.52 59,294,316.91 -38.21% 主要是本期政府补助减少 主要... | 验证息差、资产质量、资本充足、负债成本、费用率、投资收益和分红能力。 |
| platform_ecosystem | 平台生态 / 交易服务型 | quantified disclosure | 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股... | 验证用户/商户留存、交易额、变现率、服务收入、获客成本和利润率。 |

## Growth Sustainability & Ramp Conditions
| growth_source | sustainability_read | evidence_strength | evidence_basis | ramp_conditions | falsification_signals | pm_use |
| --- | --- | --- | --- | --- | --- | --- |
| core_revenue_and_profit_engine | growth durability is not proven by the current readable filings; treat it as a verification item. | quantified disclosure | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Revenue and profit can keep expanding only if the disclosed core engine keeps volume/price/utilization/customer growth while margins and cash conversion do not deteriorate. | Revenue growth decouples from gross margin, operating cash flow, receivables, inventory, contract liabilities, utilization, or disclosed customer/order evidence. | Use as the first growth paragraph in the PM memo: what has to remain true for consolidated revenue and profit growth to be sustainable. |
| segment_mix_and_profit_pool | segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. | quantified disclosure | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Track segment revenue scale, growth rate, margin/profit contribution, cash conversion, and valuation treatment separately instead of relying on consolidated growth. | High-growth segments remain too small, undisclosed, margin-dilutive, capital-intensive, or valued like the best segment without proof. | Use this as the bridge between Business Segment Breakdown and valuation/SOTP evidence gates. |
| growth_vector_overseas-expansion | requires more filing confirmation before assigning core valuation credit. | quantified disclosure | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | check customers, orders, capacity, and revenue evidence | The next annual/half-year/quarterly report would falsify the vector if it fails to show revenue, customers/orders, utilization, margin, cash conversion, or management wording progress. | Classify this vector as core value, scenario/SOTP value, watch item, or narrative only. |
| archetype_ramp_project_delivery | the primary business archetype sets the company-specific ramp variables; growth is only durable when those variables improve together. | quantified disclosure | 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股 报告期末普通股股东总数 127,680... | 验证订单质量、交付节奏、验收确认、毛利率、应收/合同资产和现金回款。 | The next evidence pack fails on the archetype's own value drivers, even if headline revenue still grows. | Use as the company-specific final check before the bull/bear debate and PM rating. |

## Pre-Debate Underwriting Questions
| question_id | theme | underwriting_question | preliminary_answer | evidence_strength | evidence_basis | bull_debate_use | bear_debate_use | pm_integration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pre_debate_business_model | business_model | 招商银行到底靠什么赚钱，收入、利润和资产之间如何形成经营闭环？ | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | quantified disclosure | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Use disclosed core engine and segment mix to prove the thesis is tied to real economics, not a slogan. | Attack any rating that relies on an undefined or over-blended business model. | Put a concise business-model explanation before valuation and avoid using one blended multiple if segments differ. |
| pre_debate_moat | moat | 这家公司的护城河来自哪里，它能否保护价格、份额、租金、毛利率或客户粘性？ | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一、经营活动产生的现金流量： 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一、经营活动产生的现金流量： 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | Support durable valuation only when filings show customer stickiness, network effect, cost advantage, brand, license, technology, or location advantage. | Challenge generic competitive-advantage language when it lacks numbers or transmission into returns. | Use this question to decide business quality and deserved valuation premium/discount. |
| pre_debate_archetype_project_delivery | company_archetype | 订单和项目储备能否转化为收入、毛利和现金？交付、验收、回款周期是否会吞噬利润质量？ | 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股 报告期末普通股股东总数 127,680 报告期末表决权恢复的优先股股东总数（如... | quantified disclosure | 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股... | 当在手订单高质量且交付回款顺畅时，支持收入可见度和盈利兑现。 | 若订单不等于利润，或应收/合同资产扩张快于收入，应下调确定性。 | PM报告应把订单、收入确认和现金流三者串联起来。 |
| pre_debate_archetype_financial_intermediary | company_archetype | 这家公司真正的利润驱动来自息差、资产质量、资本约束、保费/手续费，还是投资收益？资产负债表风险是否被低估？ | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三）主要会计数据和财务指标发生变动的情况及原因 ☑适用□不适用 报表项目 本报告期 上年同期/年初数 同比增减 披露原因 财务费用 192,357,034.98 -21,449,464.49 不适用 主要是本期汇兑损失增加 其他收益 36,636,192.52 59,294,316.91 -38.21% 主要是本期政府补助减少 主要是本期衍生金融资产处置收益增加及对 投资收益 33,566,661.52 -6,... | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三）主要会计数据和财务指标发生变动的情况及原因 ☑适用□不适用 报表项目 本报告期 上年同期/年初数 同比增减 披露原因 财务费用 192,357,034.98 -21,449,464.49 不适用 主要是本期汇兑损失增加 其他收益 36,636,192.52 59,294,316.91 -38.21% 主要是本期政府补助减少 主要... | 当资产质量稳定、资本充足且核心收入改善时，支持估值修复。 | 若利润依赖投资收益或拨备调节，且资产质量承压，应降低信心。 | PM报告应从资产负债表和资本回报出发，而不是用一般制造业框架。 |
| pre_debate_growth_driver | growth_driver | 未来增长主要来自价格、销量/客流、利用率/出租率、产能、客户、区域扩张，还是产品/服务结构升级？ | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一、经营活动产生的现金流量： 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一、经营活动产生的现金流量： 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | Use this to show which value driver can still beat market expectations. | Use this to expose where growth depends on unverified volume, price, utilization, or mix assumptions. | Tie valuation and rating to 3-6 named value drivers rather than generic growth. |
| pre_debate_second_curve | second_curve | 是否存在第二增长曲线？它已经变成收入、利润、订单、客户或现金流，还是仍停留在战略叙事？ | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | quantified disclosure | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | Promote second curves only when filings show monetization, contracted demand, users, capacity, customers, or cash conversion. | Challenge concept-only optionality, especially when capex or working capital rises before revenue proof. | Classify each second curve as core valuation, scenario/SOTP value, watch item, or narrative only. |
| pre_debate_cash_quality | cash_quality | 利润和收入能否转化为现金？应收、存货、预付款、合同负债或资本开支是否改变了增长质量？ | No direct cash-quality answer was found; structured statements may still be needed before conviction rises. | unanswered | No direct filing evidence found. | Use cash conversion and disciplined working capital to validate earnings quality. | Use working-capital absorption, weak OCF, or capex-before-proof to attack reported growth. | Let cash quality affect conviction, sizing, and safety-price work. |
| pre_debate_segment_valuation | valuation | 不同业务、地区、渠道或第二曲线应如何分开估值，而不是简单套一个合并PE/PB？ | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | quantified disclosure | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Give premium credit only to segments with proven growth, margin, cash conversion, or scarcity. | Attack over-blending when low-quality or unproven businesses are valued like the best segment. | Use split valuation when segment evidence exists; otherwise state why a blended multiple is only a rough cross-check. |
| pre_debate_key_risks | risk | 哪些风险会真正改变股权价值，而不只是年报里的常规风险披露？ | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | quantified disclosure | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Use absence of material negative notes cautiously; it is not proof of safety unless coverage is strong. | Prioritize risks with direct financial transmission: impairment, litigation, guarantees, customer concentration, margin pressure, leverage, or policy exposure. | Put only decision-relevant risks into verification/falsification and avoid padding with boilerplate. |

## Selected Filing Question Playbook
| question_id | category | question | preferred_reports |
| --- | --- | --- | --- |
| bank_asset_quality | asset_quality | 不良率、关注类贷款、拨备覆盖和逾期迁徙是否在改善？ | quarterly/semiannual/annual |
| bank_nim | profitability | 净息差压力是否缓解，还是利润靠规模硬撑？ | quarterly/semiannual/annual |
| bank_fees | mix | 中收、零售、财富管理能否抵消传统息差压力？ | semiannual/annual |
| bank_capital | capital | 资本充足率、核心一级资本和风险加权资产是否支持扩表与分红？ | quarterly/semiannual/annual |
| bank_retail_book | loan_deposit_mix | 零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？ | quarterly/semiannual/annual |

## Business Model Map
| lens | report_type | filing_evidence | why_it_matters |
| --- | --- | --- | --- |
| core_revenue_engine | quarterly | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Defines what actually drives the income statement. |
| customer_and_channel | quarterly | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 123,837,190 股，通过中信建投证券股份有限公司客户信用交易担 | Reveals demand source, concentration, and market validation. |
| geography | quarterly | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 量净额 加及出口退税增加所致。 | Explains whether growth depends on a specific geography or expansion lane. |
| reinvestment_engine | quarterly | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 在建工程 2,886,925,929 2,376,645,906 | Shows how today's cash is being converted into tomorrow's earnings power. |

## Segment Economics Pack
No filing-derived evidence snippets found.

## Business Segment Valuation Map
| business_bucket | report_type | filing_evidence | valuation_anchor | analyst_use | verification_need |
| --- | --- | --- | --- | --- | --- |
| core_revenue_engine | quarterly | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Anchor the first valuation block on the mature revenue engine: normalized earnings, FCF yield, EV/EBITDA, PE, or peer-relative multiples depending on business model. | Use this as the company introduction before discussing optionality; every later segment should be compared with this core engine. | Confirm the core engine's revenue scale, margin, cash conversion, reinvestment need, and peer multiple range. |
| emerging_or_second_curve | filing | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | Treat as SOTP/scenario value when stage is planned; include in base-case valuation only after monetization and economics are disclosed. | Use as the new-business block in a split valuation: size the option separately from the mature core business. | check customers, orders, capacity, and revenue evidence |
| geography_or_export_lane | quarterly | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 量净额 加及出口退税增加所致。 | Use as a growth/margin modifier for the core business; only value separately when regional revenue, margin, and regulatory risk are disclosed. | Use this to decide whether the company needs a split valuation rather than one blended multiple. | Check regional revenue growth, gross margin, channel inventory, currency/regulatory exposure, and whether the region has different economics. |
| channel_mix | quarterly | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 123,837,190 股，通过中信建投证券股份有限公司客户信用交易担 | Use as a sales-efficiency and working-capital modifier; do not value as a separate business unless channel economics are disclosed. | Use this to decide whether the company needs a split valuation rather than one blended multiple. | Check direct/dealer/platform split, take rate or gross margin, receivables, inventory burden, and customer acquisition cost. |

## Growth Vector Map
| vector | stage | filing_evidence | valuation_treatment | verification_need |
| --- | --- | --- | --- | --- |
| overseas-expansion | planned | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | narrative or early optionality only | check customers, orders, capacity, and revenue evidence |

## Deep Reading Excerpts
| report_type | section | excerpt | reading_purpose |
| --- | --- | --- | --- |
| quarterly | 经营活动产生的现金流量净额 | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 4,103,164,771 2,615,211,547 56.90 基本每股收益（元/股） 0.67 0.34 97.06 加权平均净资产收益率（%） 8.26 4.61 增加 3.65 个百分点 1 / 10 西部矿业股份有限公司2026 年第一季度报告 | Check cash conversion. |
| quarterly | 主要会计数据和财务指标发生变动的情况及原因 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三）主要会计数据和财务指标发生变动的情况及原因 ☑适用□不适用 报表项目 本报告期 上年同期/年初数 同比增减 披露原因 财务费用 192,357,034.98 -21,449,464.49 不适用 主要是本期汇兑损失增加 其他收益 36,636,192.52 59,294,316.91 -38.21% 主要是本期政府补助减少 主要是本期衍生金融资产处置收益增加及对 投资收益 33,566,661.52 -6,851,264.43 不适用 联营合营企业投资收益增加 公允价值变动 -12,746,217.46 8,394,208.... | Check short-cycle proof or disproof. |
| quarterly | 经营活动产生的现金流量净额 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 -548,303,437.22 -137,741,351.36 二、投资活动产生的现金流量： 收回投资收到的现金 199,598,500.00 170,240,860.22 取得投资收益收到的现金 580,325.00 5,755,084.04 处置固定资产、无形资产和其他长 6,209,195.16 69,964,425.02 期资产收回的现金净额 处置子公司及其他营业单位收到的 - - 现金净额 | Check cash conversion. |
| quarterly | 主要会计数据和财务指标发生变动的情况及原因 | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 单位：元 资产负债表项目 期末余额 期初余额 变动幅度 变动说明 报告期内，主要系配售持有股 交易性金融资产 500,243,118.17 137,000,000.00 265.14% 票增加所致。 | Check short-cycle proof or disproof. |

## Paragraph Reading Pack
| lens | report_type | section | reading_question | paragraph_excerpt | why_it_matters |
| --- | --- | --- | --- | --- | --- |
| short_cycle_execution | quarterly | 主要会计数据和财务指标发生变动的情况及原因 | Did the last quarter confirm or weaken the thesis? | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三）主要会计数据和财务指标发生变动的情况及原因 ☑适用□不适用 报表项目 本报告期 上年同期/年初数 同比增减 披露原因 财务费用 192,357,034.98 -21,449,464.49 不适用 主要是本期汇兑损失增加 其他收益 36,636,192.52 59,294,316.91 -38.21% 主要是本期政府补助减少 主要是本期衍生金融资产处置收益增加及对 投资收益 33,566,661.52 -6,851,264.43 不适用 联营合营企业投资收益增加 公允价值变动 -12,746,217.46 8,394,208.52 -251.85% 主要是本期衍生金融工具公允价值变动 收益 资产处置收益 2,540,078.57 1,255,460.13 102.32% 主要是本期固定资产处置收益 营业外支出 1,165,... | Turns quarterly reports into proof tests rather than headline snapshots. |
| cash_conversion | quarterly | 经营活动产生的现金流量净额 | Did earnings turn into cash? | 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的优先股股东数量及前十名股东持股情况表 单位：股 报告期末普通股股东总数 127,680 报告期末表决权恢复的优先股股东总数（如有） 0 前 10 名股东持股情况（不含通过转融通出借股份） 持股比例 持有有限售条 质押、标记或冻结情况 股东名称 股东性质 持股数量 （%） 件的股份数量 股份状态 数量 徐州工程机械 国有法人 21.02% 2,469,739,335 2,376,104,688 不适用 0 集团有限公司 | Catches revenue quality and working-capital stress early. |
| new_signal | quarterly | 主要会计数据和财务指标发生变动的情况及原因 | Did a new business line gain or lose evidence this quarter? | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 单位：元 资产负债表项目 期末余额 期初余额 变动幅度 变动说明 报告期内，主要系配售持有股 交易性金融资产 500,243,118.17 137,000,000.00 265.14% 票增加所致。 报告期内，主要系收到的票据 应收款项融资 130,318,687.89 69,600,183.61 87.24% 增加所致。 报告期内，主要系扩大产能资 在建工程 5,169,689,299.24 3,609,874,903.28 43.21% 产投入增加所致。 报告期内，主要系借款增加所 短期借款 3,046,670,304.20 1,499,705,005.98 103.15% | Keeps emerging vectors under live surveillance. |

## Industry Reading Pack
No filing-derived evidence snippets found.

## Banking KPI Pack
| lens | report_type | evidence_strength | filing_evidence | why_it_matters | bear_check |
| --- | --- | --- | --- | --- | --- |
| retail_wealth_engine | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 - - 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - - | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| retail_wealth_engine | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - - | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| retail_wealth_engine | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - - 应付分保账款 - - | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| retail_wealth_engine | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 已赚保费 - - 手续费及佣金收入 - - 二、营业总成本 9,304,577,384.76 8,274,057,259.75 | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| loan_deposit_mix | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一、经营活动产生的现金流量： 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |
| loan_deposit_mix | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |
| loan_deposit_mix | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - 向中央银行借款净增加额 - - | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |
| loan_deposit_mix | quarterly | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动现金流入小计 8,524,439,432.72 7,929,656,174.66 购买商品、接受劳务支付的现金 7,010,045,297.64 6,173,852,447.76 客户贷款及垫款净增加额 - - | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |

## Structured Balance-Sheet History
| end_date | ann_date | contract_liab | adv_receipts | contract_plus_adv | qoq_change | yoy_change | inventories | receivables | money_cap | liab_to_assets | analyst_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260331 | 20260429 | 33.86亿元 | N/A | 33.86亿元 | -1.62亿元 (-4.6%) | -6.72亿元 (-16.6%) | N/A | N/A | N/A | 90.4% | forward demand/liability signal available |
| 20251231 | 20260328 | 35.48亿元 | N/A | 35.48亿元 | -1.77亿元 (-4.8%) | -6.45亿元 (-15.4%) | N/A | N/A | N/A | 90.2% | forward demand/liability signal available |
| 20250930 | 20251030 | 37.25亿元 | N/A | 37.25亿元 | -1.91亿元 (-4.9%) | -9.89亿元 (-21.0%) | N/A | N/A | N/A | 89.9% | forward demand/liability signal available |
| 20250630 | 20250830 | 39.16亿元 | N/A | 39.16亿元 | -1.42亿元 (-3.5%) | -10.95亿元 (-21.9%) | N/A | N/A | N/A | 89.8% | forward demand/liability signal available |
| 20250331 | 20250430 | 40.58亿元 | N/A | 40.58亿元 | -1.35亿元 (-3.2%) | N/A | N/A | N/A | N/A | 90.0% | forward demand/liability signal available |
| 20241231 | 20250326 | 41.93亿元 | N/A | 41.93亿元 | -5.21亿元 (-11.1%) | N/A | N/A | N/A | N/A | 89.8% | forward demand/liability signal available |
| 20240930 | 20241030 | 47.14亿元 | N/A | 47.14亿元 | -2.97亿元 (-5.9%) | N/A | N/A | N/A | N/A | 90.1% | forward demand/liability signal available |
| 20240630 | 20240830 | 50.11亿元 | N/A | 50.11亿元 | N/A | N/A | N/A | N/A | N/A | 90.3% | forward demand/liability signal available |

## Statement Table Reading Pack
No filing-derived evidence snippets found.

## Filing Note Reading Pack
| note_type | importance | note_evidence | why_it_matters | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- |
| impairment_policy | supporting | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Provisioning language explains whether accounting conservatism is strengthening or weakening. | Use conservative provisioning only when it lowers future surprise risk. | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| impairment_policy | supporting | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Provisioning language explains whether accounting conservatism is strengthening or weakening. | Use conservative provisioning only when it lowers future surprise risk. | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| capitalized_development | supporting | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 无形资产 1,545,729,551.58 1,561,353,193.96 其中：数据资源 开发支出 - - | Capitalized development can shift current profit at the cost of later amortization risk. | Use with commercialization evidence to support platform investment. | Challenge profit quality if capitalization rises ahead of monetization. |
| capitalized_development | supporting | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：数据资源 开发支出 - - | Capitalized development can shift current profit at the cost of later amortization risk. | Use with commercialization evidence to support platform investment. | Challenge profit quality if capitalization rises ahead of monetization. |

## Financial Relationship Reading Pack
No filing-derived evidence snippets found.

## Filing Textual Signals
| signal_type | report_type | wording_stage | textual_evidence | investment_read | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| risk_language_upgrade | quarterly | risk-language | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| risk_language_upgrade | quarterly | risk-language | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| management_claim_with_evidence | quarterly | proof-backed | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 应付票据 700,528,095 636,636,197 应付账款 2,380,194,008 2,509,189,467 合同负债 2,180,099,838 796,418,224 | Management language has a harder evidence bridge; debate materiality and economics rather than existence. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| management_claim_with_evidence | quarterly | proof-backed | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 应付账款 2,380,194,008 2,509,189,467 合同负债 2,180,099,838 796,418,224 | Management language has a harder evidence bridge; debate materiality and economics rather than existence. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| watch_missing_monetization | annual/semiannual | missing-proof | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | The filing describes a possible growth vector, but monetization evidence is still incomplete. | Use as a diligence agenda or scenario option, not a base-case valuation driver. | Ask why the company has not disclosed revenue, margin, customers, delivery, or cash evidence yet. |

## Filing Insight Distillation Layer
| insight_type | analyst_question | distilled_read | evidence_basis | debate_use | what_would_change_mind |
| --- | --- | --- | --- | --- | --- |
| core_business_engine | What actually drives this company's revenue and profit pool? | Start the memo from the operating engine disclosed in filings, not from market labels, hot themes, or valuation screens. | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 | Forces bulls and bears to debate the real business before discussing optionality. | A segment disclosure or order/customer evidence showing a different profit engine has become material. |
| monetization_gap | What is the gap between the story and the income statement? | The filing has a growth narrative, but the system has not found enough clean financial confirmation to treat it as a base-case valuation driver. | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | Keeps the report from either ignoring the story or overpaying for it; use it as scenario evidence until economics are proven. | Quantified revenue/profit contribution, repeat orders, cash collection, and segment margin evidence. |
| textual_filing_signal | What is management language trying to prove, soften, or avoid? | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Use wording as a debate input: hard wording must still clear materiality; soft wording needs proof; risk wording can cap valuation. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| core_debate_item | Which filing-derived point must enter the bull/bear debate? | Direct filing answer for mix. | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 - - 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - - | Do not leave this as background context; make it one of the main debate pillars. | Question whether fee income is cyclical or shrinking. |
| filing_read_confidence_gap | Can we trust a strong conclusion from the available filings? | Readable text exists but the pack is too thin for a full buy-side read; avoid strong claims about business model, second curve, or execution trend. | Coverage: weak; reports seen: quarterly | Cap conviction and explicitly name missing report types or unanswered thesis-critical questions. | Retrieve annual/semiannual/quarterly text and answer the core playbook with quantified evidence. |

## Core Discussion Promotion Queue
| topic | priority | evidence_basis | why_it_matters | valuation_treatment | verification_need |
| --- | --- | --- | --- | --- | --- |
| bank_fees | core | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 - - 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - - | Direct filing answer for mix. | core debate candidate | Question whether fee income is cyclical or shrinking. |
| capitalized_development | supporting | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 无形资产 1,545,729,551.58 1,561,353,193.96 其中：数据资源 开发支出 - - | Capitalized development can shift current profit at the cost of later amortization risk. | risk/governance modifier | Challenge profit quality if capitalization rises ahead of monetization. |
| impairment_policy | supporting | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 单位:元 币种:人民币 非经常性损益项目 本期金额 说明 非流动性资产处置损益，包括已计提资产减值准备的冲销部分 1,355,779 | Provisioning language explains whether accounting conservatism is strengthening or weakening. | risk/governance modifier | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| overseas-expansion | watch | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 | Growth vector currently reads as planned. | narrative or early optionality only | check customers, orders, capacity, and revenue evidence |

## Unanswered Filing Questions
| question_id | category | question | why_it_matters |
| --- | --- | --- | --- |
| bank_asset_quality | asset_quality | 不良率、关注类贷款、拨备覆盖和逾期迁徙是否在改善？ | Still unresolved in the latest readable filings; Challenge hidden deterioration before it hits profits. |
| bank_nim | profitability | 净息差压力是否缓解，还是利润靠规模硬撑？ | Still unresolved in the latest readable filings; Attack profitability if volume masks spread compression. |
| bank_capital | capital | 资本充足率、核心一级资本和风险加权资产是否支持扩表与分红？ | Still unresolved in the latest readable filings; Challenge expansion or dividend claims if RWA growth consumes capital. |

## Question-Driven Filing Answers
| question_id | report_type | question | evidence_strength | filing_answer | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| bank_fees | quarterly | 中收、零售、财富管理能否抵消传统息差压力？ | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 - - 应付股利 3,211,179.07 3,211,179.07 应付手续费及佣金 - - | Support business diversification. | Question whether fee income is cyclical or shrinking. |
| bank_retail_book | quarterly | 零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？ | quantified disclosure | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一、经营活动产生的现金流量： 销售商品、提供劳务收到的现金 7,892,788,643.48 7,268,766,582.70 客户存款和同业存放款项净增加额 - - | Support the retail-bank moat when deposit and AUM growth remain healthy. | Challenge the moat if retail loan demand or deposit quality deteriorates. |

## Material Filing Findings
No filing-derived evidence snippets found.

## Report-to-Report Bridge
| topic | long_cycle_evidence | checkpoint_evidence | bridge_status | bridge_read | analyst_read |
| --- | --- | --- | --- | --- | --- |
| orders_and_visibility |  | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 合同负债 2,180,099,838 796,418,224 | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Does the short-cycle report confirm the demand visibility described in long-cycle filings? |
| pricing_and_margin |  | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 其中：营业成本 14,491,966,770 13,663,232,064 | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Does the latest checkpoint validate or weaken the prior margin story? |
| cash_conversion |  | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 应收账款 326,183,465 103,857,896 | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Do newer filings show profits turning into cash? |
| capital_intensity |  | 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 在建工程 2,886,925,929 2,376,645,906 | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Is reinvestment translating into visible operating progress? |

## Company-Specific Watch Questions
| question_id | question | times_seen | last_seen | last_report_type |
| --- | --- | --- | --- | --- |
| bank_fees | 中收、零售、财富管理能否抵消传统息差压力？ | 2 | 2026-06-22 | quarterly |
| bank_retail_book | 零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？ | 2 | 2026-06-22 | quarterly |
| generic_revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | 1 | 2026-05-22 | quarterly |
| generic_profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | 1 | 2026-05-22 | quarterly |
| generic_cash_conversion | 利润能否转成现金，还是被应收、存货、预付款拖住？ | 1 | 2026-05-22 | quarterly |
| generic_capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | 1 | 2026-05-22 | annual |
| generic_risk_disclosure | 财报中新增或升级了哪些真正会改变股权价值的风险？ | 1 | 2026-05-22 | annual |
| bank_asset_quality | 不良率、关注类贷款、拨备覆盖和逾期迁徙是否在改善？ | 1 | 2026-05-22 | quarterly |

## Filing-Derived Operating Evidence
| category | signal | filing_evidence | bull_use | bear_use |
| --- | --- | --- | --- | --- |
| bank_retail_wealth | 手续费/佣金 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 应付手续费及佣金 - - | Use wealth-management monetization and retail franchise scale to support fee resilience. | Test whether AUM growth is translating into fee income or being offset by fee-rate compression. |
| bank_retail_wealth | 手续费/佣金 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 手续费及佣金收入 - - | Use wealth-management monetization and retail franchise scale to support fee resilience. | Test whether AUM growth is translating into fee income or being offset by fee-rate compression. |
| bank_retail_wealth | 手续费/佣金 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 手续费及佣金支出 - - | Use wealth-management monetization and retail franchise scale to support fee resilience. | Test whether AUM growth is translating into fee income or being offset by fee-rate compression. |
| bank_balance_sheet_mix | 客户存款 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 客户存款和同业存放款项净增加额 - - | Use loan/deposit mix to connect franchise quality to NIM and asset-quality outcomes. | Challenge retail-bank quality if weak mortgage, credit-card, or consumer-loan data undermine the core engine. |
| bank_balance_sheet_mix | 客户贷款 | 广西柳工机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 客户贷款及垫款净增加额 - - | Use loan/deposit mix to connect franchise quality to NIM and asset-quality outcomes. | Challenge retail-bank quality if weak mortgage, credit-card, or consumer-loan data undermine the core engine. |
| bank_balance_sheet_mix | 客户存款 | 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 客户存款和同业存放款项净增加额 | Use loan/deposit mix to connect franchise quality to NIM and asset-quality outcomes. | Challenge retail-bank quality if weak mortgage, credit-card, or consumer-loan data undermine the core engine. |

## Analyst Instructions
- Start with the filing reading coverage audit. If coverage is partial, weak, or failed, explicitly downgrade confidence before using any filing-derived thesis.
- Use the Internal Filing Quality Modules as a ten-part filing-only review: accounting reconciliation, segment economics, footnote radar, cash-flow quality, capex/CIP return bridge, MD&A text change, non-recurring profit quality, balance-sheet forward signals, shareholder-return authenticity, and disclosure quality. The final PM memo should integrate these into PM Summary, Investment Thesis, Valuation, Risk, and Verification rather than dumping a checklist.
- Use the Growth Sustainability & Ramp Conditions table before assigning upside or downside. For each company, explain whether revenue and profit growth are sustainable, what must happen for growth to keep ramping, which evidence is already verified, and what would falsify the growth thesis.
- Use the Pre-Debate Underwriting Questions before the bull/bear debate. These are the company-specific buy-side questions that should frame the debate: business model, moat, growth driver, second curve, cash quality, segment valuation, and decision-relevant risks. Bulls and bears should answer or attack these questions directly rather than debating generic sector slogans.
- Use Structured Balance-Sheet History as the second-layer financial-statement proof for contract liabilities/advance receipts, inventory, receivables, cash, and leverage. If this table is ready, do not call contract liabilities or working-capital history missing merely because the PDF narrative excerpt did not mention it.
- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.
- Start with the business model map, then use the growth vector map to separate mature engines from emerging second curves.
- For multi-product or multi-region companies, read the Segment Economics Pack before the bull/bear debate. Do not collapse a company into headline revenue or profit when annual/half-year filings disclose product, geography, channel, revenue, cost, gross margin, or growth-rate splits.
- Use the Business Segment Valuation Map to build a split valuation before applying a blended multiple. Value mature/core businesses on normalized earnings, FCF, EV/EBITDA, PE, or peer-relative multiples; value emerging or second-curve businesses with SOTP/scenario treatment until segment revenue, margin, capex/utilization, customers, and cash conversion are proven.
- For unfamiliar companies, first explain the main business from filings, then split the investment case into disclosed business buckets. Do not discuss new businesses as free optionality unless the map shows filing-backed monetization or a clear verification path.
- Use the deep-reading excerpts as source text, not decorative context: annual-report excerpts define the company, semiannual excerpts test trend formation, and quarterly excerpts test short-cycle execution.
- Use the paragraph reading pack for genuine report reading: answer the paragraph-level question first, then decide whether the business model, second curve, moat, trend, or cash-conversion thesis changed.
- Use the industry reading pack as the specialist layer: the same filing should be read through the value drivers that matter for that business model, then linked to the external inputs named in `connect_to` before forming a conclusion.
- Use the statement table reading pack for the hard-accounting layer: contract liabilities, receivables, inventory, prepayments, capex, investment assets, operating cash flow, and impairment rows often decide whether the narrative survives contact with the numbers.
- Use the filing note reading pack for footnote discipline: customer concentration, related parties, guarantees, litigation, impairment assumptions, and capitalization policies often reveal risks that the headline statements hide.
- Use the financial relationship reading pack to connect the statements rather than reading metrics in isolation. Revenue growth only deserves praise if margin, cash conversion, and balance-sheet demands make sense together.
- Use the filing textual signals layer to read management wording strength, risk-language upgrades, abnormal silence, and strategic promises. Hard wording still needs materiality; soft wording belongs in scenarios/watchlist; risk wording can cap valuation. Keep a concise textual-signal module in the manager report when it changes the thesis.
- Use the filing insight distillation layer before writing the final thesis. It converts raw filing snippets into buy-side questions: core engine, second curve, quality of growth, monetization gap, capital allocation, and tail risk. The manager report should read like a company memo, not a list of disconnected data points.
- Start from the selected question playbook, then answer only with evidence actually found in filings.
- For banks, start from the Banking KPI Pack and the banking playbook. Do not use contract liabilities, inventory, gross margin, capex, or generic OCF conversion as core bank-quality evidence unless a bank-specific disclosure explicitly makes them decision-relevant.
- For banks, preserve the exact spread terminology from filings: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. If the filing only supports 净利差 1.77% and 净利息收益率 1.83%, do not invent or substitute a 1.40%/1.50% NIM number. Treat NIM stabilization as conditional until the next filing confirms spread, loan yield, and deposit-cost movement together.
- Use the core discussion promotion queue as the bridge from reading to investing: core items should enter bull/bear debate, supporting items should reinforce or challenge a thesis, scenario items belong in upside/downside cases, and watch items stay out of base-case valuation until upgraded.
- Treat unanswered filing questions as explicit research gaps, not neutral evidence. If a thesis depends on an unanswered question, reduce conviction or state what disclosure would close the gap.
- Promote materially decision-relevant findings such as signed long-term agreements, named customers, take-or-pay/offtake signals, capacity-to-demand bridges, and commercialization milestones into the core debate rather than leaving them buried as generic snippets.
- Use the report-to-report bridge to ask whether annual/semiannual narratives are being confirmed, weakened, or still waiting for quarterly proof.
- Treat annual reports, half-year reports, and quarterly reports as a linked evidence chain: annual reports define the long-cycle thesis, half-year reports test trend formation, and quarterly reports confirm, weaken, or leave unresolved the latest checkpoint.
- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.
- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.
- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.