# Financial-report intelligence for 002015.SZ as of 2026-05-16

- Company: 协鑫能科
- Vendor industry: 新型电力
- Reading profile: wind_power_equipment
- Financial-report look-back: 900 days
- Extraction status: Financial-report text extraction succeeded.

## Financial Reports Considered
- 20260428: 2025年年度报告
- 20260428: 2026年一季度报告
- 20251028: 2025年三季度报告
- 20250829: 2025年半年度报告

## Selected Filing Question Playbook
| question_id | category | question | preferred_reports |
| --- | --- | --- | --- |
| generic_revenue_quality | revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | quarterly/semiannual/annual |
| generic_profit_quality | profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | quarterly/semiannual/annual |
| generic_cash_conversion | cash_quality | 利润能否转成现金，还是被应收、存货、预付款拖住？ | quarterly/semiannual/annual |
| generic_capital_allocation | capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | semiannual/annual |
| generic_risk_disclosure | risk | 财报中新增或升级了哪些真正会改变股权价值的风险？ | semiannual/annual |
| wind_orders | orders | 新增订单、在手订单和合同负债是否同步改善，还是只有收入在冲？ | quarterly/semiannual/annual |
| wind_pricing | pricing | 招投标价格、风机单价和毛利率是否真正止跌？ | quarterly/semiannual |
| wind_mix | mix | 海上风电、大兆瓦机型、海外业务、风电场运营谁在改善利润结构？ | semiannual/annual |
| wind_overseas_risk | overseas | 海外扩张带来的是订单、利润，还是先带来担保和回款风险？ | semiannual/annual |

## Question-Driven Filing Answers
| question_id | report_type | question | evidence_strength | filing_answer | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| generic_revenue_quality | annual | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | quantified disclosure | 2025年年度报告: 营业收入（元） 10,325,548,111.80 9,796,410,426.69 5.40% 10,357,772,822.16 | Use matching revenue, cash, and receivable evidence to support quality growth. | Attack any divergence between reported growth and cash realization. |
| generic_profit_quality | annual | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | quantified disclosure | 2025年年度报告: 的扣除非经常性损益 328,669,450.48 293,940,053.32 11.82% 101,070,079.07 | Support durable earnings when the improvement clearly comes from core operations. | Separate operating earnings from accounting or one-off noise. |
| generic_cash_conversion | annual | 利润能否转成现金，还是被应收、存货、预付款拖住？ | quantified disclosure | 2025年年度报告: 经营活动现金流入小计 12,693,762,942.62 11,483,083,031.70 10.54% | Use improving conversion to validate the thesis. | Use deteriorating working capital to challenge profit quality. |
| generic_capital_allocation | annual | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | quantified disclosure | 2025年年度报告: 4、研发投入 | Argue reinvestment is building future earnings power. | Question return on capital, empire building, or delayed payback. |
| generic_risk_disclosure | annual | 财报中新增或升级了哪些真正会改变股权价值的风险？ | quantified disclosure | 2025年年度报告: 资产减值 -422,949,891.94 -38.99% 收益率不达预期的部 不具有。 | Use risk relief only when disclosures become visibly safer. | Surface tail risks the market may be underweighting. |
| wind_orders | annual | 新增订单、在手订单和合同负债是否同步改善，还是只有收入在冲？ | quantified disclosure | 2025年年度报告: 合同负债 122,936,199.53 0.32% 231,597,839.98 0.57% -0.25% | Support demand visibility and delivery backlog. | Ask whether backlog converts into margin or just low-priced volume. |
| wind_pricing | quarterly | 招投标价格、风机单价和毛利率是否真正止跌？ | quantified disclosure | 2026年一季度报告: 营业成本 1,599,888,637.38 2,249,590,186.19 -28.88% 方式优化，运营效率提升，毛利率提高；同时， | Argue margin inflection if pricing stabilizes. | Attack any bull thesis that assumes a bottom without disclosed evidence. |
| wind_mix | annual | 海上风电、大兆瓦机型、海外业务、风电场运营谁在改善利润结构？ | quantified disclosure | 2025年年度报告: 新能源海外发展联盟理事长，南京大学校董会名誉董事长等社会职务。获得“改革开放 40 年中国企业改革奖章”“改革开 | Show mix upgrade and higher-value revenue. | Question whether higher-growth segments are still too small or lower quality. |
| wind_overseas_risk | annual | 海外扩张带来的是订单、利润，还是先带来担保和回款风险？ | quantified disclosure | 2025年年度报告: 2、同时按照境外会计准则与按照中国会计准则披露的财务报告中净利润和净资产差异情况 | Support diversification and global optionality. | Stress execution, guarantees, and receivable risk. |

## Company-Specific Watch Questions
| question_id | question | times_seen | last_seen | last_report_type |
| --- | --- | --- | --- | --- |
| generic_revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | 1 | 2026-05-16 | annual |
| generic_profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | 1 | 2026-05-16 | annual |
| generic_cash_conversion | 利润能否转成现金，还是被应收、存货、预付款拖住？ | 1 | 2026-05-16 | annual |
| generic_capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | 1 | 2026-05-16 | annual |
| generic_risk_disclosure | 财报中新增或升级了哪些真正会改变股权价值的风险？ | 1 | 2026-05-16 | annual |
| wind_orders | 新增订单、在手订单和合同负债是否同步改善，还是只有收入在冲？ | 1 | 2026-05-16 | annual |
| wind_pricing | 招投标价格、风机单价和毛利率是否真正止跌？ | 1 | 2026-05-16 | quarterly |
| wind_mix | 海上风电、大兆瓦机型、海外业务、风电场运营谁在改善利润结构？ | 1 | 2026-05-16 | annual |

## Filing-Derived Operating Evidence
| category | signal | filing_evidence | bull_use | bear_use |
| --- | --- | --- | --- | --- |
| demand_visibility | 合同负债 | 2025年年度报告: 合同负债 122,936,199.53 0.32% 231,597,839.98 0.57% -0.25% | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| demand_visibility | 预收款项 | 2025年年度报告: 预收款项 20,330,888.63 15,820,000.00 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| demand_visibility | 合同负债 | 2025年年度报告: 合同负债 122,936,199.53 231,597,839.98 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| commercialization | 营业收入 | 2025年年度报告: 营业收入（元） 10,325,548,111.80 9,796,410,426.69 5.40% 10,357,772,822.16 | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| commercialization | 营业收入 | 2025年年度报告: 营业收入 2,932,925,080.10 2,489,463,885.02 2,512,547,184.15 2,390,611,962.53 | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| commercialization | 投产 | 2025年年度报告: 新投产机组的装机容量（万千瓦） 88.27 301.72 | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| pricing_and_margin | 成本 | 2025年年度报告: 本报告中如有涉及未来计划等前瞻性陈述，均不构成本公司对投资者的 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| pricing_and_margin | 成本 | 2025年年度报告: 异地重建，提质降本增效，保持成本领先优势，夯实发展基础；针对集中式新能源资产，公司全面引入能源+AI 一体化 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| pricing_and_margin | 成本 | 2025年年度报告: 管理模式，通过提升市场化交易能力提高项目收益，并通过自主运维，减少限电与电网考核，以降低运维成本。另一方 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| capacity_and_capex | 产能 | 2025年年度报告: 上述“资产推动服务客户导入，服务驱动资产增值”的模式，既可扩大轻资产能源服务规模，亦可盘活存量能源资产 | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| capacity_and_capex | 产量 | 2025年年度报告: 生产量 万 kWh 1,082,928.8 966,549.02 12.04% | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| capacity_and_capex | 产量 | 2025年年度报告: 生产量 吨 10,518,597.49 11,056,282.58 -4.86% | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| customer_and_geography | 境外 | 2025年年度报告: 2、同时按照境外会计准则与按照中国会计准则披露的财务报告中净利润和净资产差异情况 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| customer_and_geography | 境外 | 2025年年度报告: 公司报告期不存在按照境外会计准则与按照中国会计准则披露的财务报告中净利润和净资产差异情况。 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| customer_and_geography | 客户 | 2025年年度报告: 质客户群，聚焦工商业场景进行定制化开发，创新“分布式+绿电+智慧运维”等商业模式；同时结合政策走向，探索零碳 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| innovation_and_product | 研发 | 2025年年度报告: 维护；能源信息智能化服务；能源技术的科技研发和咨询 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| innovation_and_product | 研发 | 2025年年度报告: 技术研发；技术服务、技术开发、技术咨询、技术交流、 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| innovation_and_product | 研发 | 2025年年度报告: 能技术研发；技术服务、技术开发、技术咨询、技术交 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| cash_and_working_capital | 减值准备 | 2025年年度报告: 减值准备的冲销部 | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| cash_and_working_capital | 减值准备 | 2025年年度报告: 应收款项减值准备转 15,775,981.00 158,451.62 | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| cash_and_working_capital | 减值准备 | 2025年年度报告: ②公司持续动态优化调整资产结构，对预计收益率不达预期的部分项目相关资产进行了处置或减值准备计提，导致 | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| balance_sheet_and_risk | 资产减值 | 2025年年度报告: 资产减值 -422,949,891.94 -38.99% 收益率不达预期的部 不具有。 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |
| balance_sheet_and_risk | 担保/关联交易 | 2025年年度报告: 此外，公司每月初定期对最新资本市场法规及案例等进行合规专题分享，以及日常针对关联交易、财务资助、对外担保 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |
| balance_sheet_and_risk | 关联交易 | 2025年年度报告: 人及其控制的其他企业，不存在显失公平的关联交易。公司的主营业务不依赖于控股股东、实际控制人及其控制的其他 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |

## Analyst Instructions
- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.
- Start from the selected question playbook, then answer only with evidence actually found in filings.
- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.
- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.
- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.