# Financial-report intelligence for 002202.SZ as of 2026-05-17

- Company: 金风科技
- Vendor industry: 电气设备
- Reading profile: precision_equipment
- Research hygiene: industry-specific playbooks are conservative by design; if identity is ambiguous, generic questions are safer than a wrong template.
- Financial-report look-back: 900 days
- Extraction status: Financial-report text extraction succeeded.

## Financial Reports Considered
- 20260425: 2026年一季度报告
- 20260328: 2025年年度报告
- 20251025: 2025年三季度报告
- 20250823: 半年报董事会决议公告

## Selected Filing Question Playbook
| question_id | category | question | preferred_reports |
| --- | --- | --- | --- |
| generic_revenue_quality | revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | quarterly/semiannual/annual |
| generic_profit_quality | profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | quarterly/semiannual/annual |
| generic_cash_conversion | cash_quality | 利润能否转成现金，还是被应收、存货、预付款拖住？ | quarterly/semiannual/annual |
| generic_capital_allocation | capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | semiannual/annual |
| generic_risk_disclosure | risk | 财报中新增或升级了哪些真正会改变股权价值的风险？ | semiannual/annual |
| equipment_orders | orders | 新增订单、在手订单、合同负债与收入确认是否同向？ | quarterly/semiannual/annual |
| equipment_mix | mix | 高毛利新品类是否已形成可单独验证的收入与毛利贡献？ | semiannual/annual |

## Question-Driven Filing Answers
| question_id | report_type | question | evidence_strength | filing_answer | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| generic_revenue_quality | quarterly | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | quantified disclosure | 2026年一季度报告: 营业收入（元） 15,484,910,567.73 9,472,103,951.62 63.48% | Use matching revenue, cash, and receivable evidence to support quality growth. | Attack any divergence between reported growth and cash realization. |
| generic_profit_quality | quarterly | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | quantified disclosure | 2026年一季度报告: 非经常性损益的净利润 918,870,528.82 555,060,143.33 65.54% | Support durable earnings when the improvement clearly comes from core operations. | Separate operating earnings from accounting or one-off noise. |
| generic_cash_conversion | quarterly | 利润能否转成现金，还是被应收、存货、预付款拖住？ | quantified disclosure | 2026年一季度报告: 3. 预付款项 2026 年 3 月 31 日的余额为人民币 3,056,558,913.19 元，较 2025 年 12 月 31 日余额增加 59.51%，主要原因： | Use improving conversion to validate the thesis. | Use deteriorating working capital to challenge profit quality. |
| generic_capital_allocation | annual | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | quantified disclosure | 2025年年度报告: 4、研发投入 | Argue reinvestment is building future earnings power. | Question return on capital, empire building, or delayed payback. |
| generic_risk_disclosure | annual | 财报中新增或升级了哪些真正会改变股权价值的风险？ | quantified disclosure | 2025年年度报告: 申请仲裁 138,999.83 否 - - - | Use risk relief only when disclosures become visibly safer. | Surface tail risks the market may be underweighting. |
| equipment_orders | quarterly | 新增订单、在手订单、合同负债与收入确认是否同向？ | quantified disclosure | 2026年一季度报告: 外，公司另有内部订单 3,234.46MW。公司在手订单总计 53,934.25MW，同比增长 5.56%。 | Support demand visibility and shipment conversion. | Challenge whether revenue is running ahead of durable order intake. |
| equipment_mix | annual | 高毛利新品类是否已形成可单独验证的收入与毛利贡献？ | quantified disclosure | 2025年年度报告: 营业收入（元） 73,023,477,737.27 56,699,162,790.54 28.79% 50,457,189,147.74 | Show genuine mix upgrade when new lines are separately monetized. | Keep optionality out of core valuation until segment economics are disclosed. |

## Company-Specific Watch Questions
| question_id | question | times_seen | last_seen | last_report_type |
| --- | --- | --- | --- | --- |
| generic_revenue_quality | 收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？ | 5 | 2026-05-17 | quarterly |
| generic_profit_quality | 利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？ | 5 | 2026-05-17 | quarterly |
| generic_cash_conversion | 利润能否转成现金，还是被应收、存货、预付款拖住？ | 5 | 2026-05-17 | quarterly |
| generic_capital_allocation | 管理层把钱投向哪里，资本开支是否正在创造未来收益？ | 5 | 2026-05-17 | annual |
| generic_risk_disclosure | 财报中新增或升级了哪些真正会改变股权价值的风险？ | 5 | 2026-05-17 | annual |
| equipment_orders | 新增订单、在手订单、合同负债与收入确认是否同向？ | 4 | 2026-05-17 | quarterly |
| equipment_mix | 高毛利新品类是否已形成可单独验证的收入与毛利贡献？ | 4 | 2026-05-17 | annual |
| wind_orders | 新增订单、在手订单和合同负债是否同步改善，还是只有收入在冲？ | 1 | 2026-05-15 | quarterly |

## Filing-Derived Operating Evidence
| category | signal | filing_evidence | bull_use | bear_use |
| --- | --- | --- | --- | --- |
| demand_visibility | 中标 | 2026年一季度报告: 4,797.10MW，6MW(含)-10MW 机组 27,644.82MW，10MW 及以上机组 8,750.90MW；公司外部中标未 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| demand_visibility | 在手订单 | 2026年一季度报告: 外，公司另有内部订单 3,234.46MW。公司在手订单总计 53,934.25MW，同比增长 5.56%。 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| demand_visibility | 预收款项 | 2026年一季度报告: 预收款项 8,004,436.27 6,299,420.47 | Argue revenue visibility, order momentum, or deferred demand already embedded in filings. | Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure. |
| commercialization | 营业收入 | 2026年一季度报告: 营业收入（元） 15,484,910,567.73 9,472,103,951.62 63.48% | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| commercialization | 营业收入 | 2026年一季度报告: 7. 营业收入本期为人民币 15,484,910,567.73 元，较上年同期增加 63.48%，主要原因：本期本公司风机及零部件销售规模 | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| commercialization | 营业收入 | 2026年一季度报告: 9. 税金及附加本期为人民币 65,973,922.17 元，较上年同期增加 39.86%，主要原因：本期本公司营业收入增加。 | Argue that a strategy is becoming monetized rather than remaining narrative. | Test whether the disclosed scale is still too small, one-off, or low margin. |
| pricing_and_margin | 成本 | 2026年一季度报告: 业的投资成本小于取得投资时应享有 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| pricing_and_margin | 价格 | 2026年一季度报告: 交易价格显失公允的交易产生的收益 0.00 无 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| pricing_and_margin | 成本 | 2026年一季度报告: 8. 营业成本本期为人民币 12,889,194,475.36 元，较上年同期增加 73.95%，主要原因：本期本公司风机及零部件销售规模 | Use disclosed pricing or margin language to support an earnings inflection if the trend improves. | Use pressure language to attack profit durability and operating leverage assumptions. |
| capacity_and_capex | 在建工程 | 2026年一季度报告: 在建工程 11,455,153,414.60 10,224,265,811.31 | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| capacity_and_capex | 产能 | 2025年年度报告: 术生产绿色甲醇，同时与国际航运巨头等客户签订长期协议，形成产能建设到市场消纳的良性循环。 | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| capacity_and_capex | 产量 | 2025年年度报告: 风机制造销售 生产量 MW 29,356.76 18,835.24 55.86% | Argue future supply, growth runway, or operating leverage from capacity build-out. | Challenge utilization, overcapacity, return on capital, and capex-before-demand risk. |
| customer_and_geography | 境外 | 2026年一季度报告: （代理人）有 境外法人 18.29% 772,620,460 0 不适用 0 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| customer_and_geography | 境外 | 2026年一季度报告: 境外法人 4.50% 190,127,906 0 不适用 0 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| customer_and_geography | 境外 | 2026年一季度报告: 香港中央结算（代理人）有限公 境外上市外资 | Argue market expansion, diversification, or customer validation. | Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth. |
| innovation_and_product | 研发 | 2026年一季度报告: 研发费用 433,809,421.91 338,765,070.35 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| innovation_and_product | 研发 | 2025年年度报告: 储能、能碳等其他业务，为公司提供多元化盈利渠道。金风科技凭借在研发、制造风机及建设风电 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| innovation_and_product | 认证 | 2025年年度报告: 的绿色电力消费机制更加健全，绿色电力消费核算、认证、标识等制度基本建立。到2030年，绿证 | Argue moat-building, product upgrade, or future mix improvement. | Question commercialization, payback period, and whether R&D is defending rather than expanding moat. |
| cash_and_working_capital | 减值准备 | 2026年一季度报告: 资产减值准备的冲销部分） | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| cash_and_working_capital | 合同资产 | 2026年一季度报告: 14. 资产减值利得本期为人民币 162,338.49 元，较上年同期减少 60.73%，主要原因：本期本公司计提的合同资产减值损 | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| cash_and_working_capital | 应收账款 | 2026年一季度报告: 应收账款 33,935,910,065.75 32,344,640,857.74 | Use cash conversion or working-capital improvement to validate earnings quality. | Use receivables, inventory, or weak cash language to challenge revenue quality. |
| balance_sheet_and_risk | 资产减值 | 2026年一季度报告: 资产减值准备的冲销部分） | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |
| balance_sheet_and_risk | 资产减值 | 2026年一季度报告: 14. 资产减值利得本期为人民币 162,338.49 元，较上年同期减少 60.73%，主要原因：本期本公司计提的合同资产减值损 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |
| balance_sheet_and_risk | 担保 | 2026年一季度报告: 易担保证券账户持有公司股份 41,038,700 股，其余 3,961,300 股通过 | Use resilience disclosures only if they directly reduce tail risk. | Surface contingent liabilities, impairments, governance, or off-balance-sheet risk. |

## Analyst Instructions
- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.
- Start from the selected question playbook, then answer only with evidence actually found in filings.
- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.
- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.
- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.