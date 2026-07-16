# Investor interaction context for 688981.SH as of 2026-07-15

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=688981

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 173884 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1677316020000 :中芯国际(688981) 请问截止5月15日，公司的股东人数是多少？ 2026年05月18日 08:28 来自 IOS ◆ ◆ 中芯国际 尊敬的投资者，您好！如要查询定期报告时点以外的股东户数，您可携带本人身份证、证券账户证明、截止查询日的持股证明至公司或发送公司投资者关系邮箱 IR@smics.com ，公司将在核实股东身份后予以提供相关信息。感谢您的关注！ | 收藏 | 评论 --> 2026年06月18日 17:19 来自 网站 ◆'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-16 | 2026-06-18 | 公司目前的月产能是多少，到今年年末还会新增吗？谢谢！ | 尊敬的投资者，您好！截至2026年第一季度末，公司的月产能为1,078,250 片（折合 8 英寸标准逻辑）。在产能规划方面，公司预计今年年底较去年年底，月产能增量折合12英寸增加约4 万片（折合 8 英寸标准逻辑约增加9万片）。感谢您的关注！ | directional-but-unquantified |
| 2026-06-16 | 2026-06-18 | 董秘您好，请问如何查询公司的产能利用率数据？请提供公司一季度的产能利用率数据。 | 尊敬的投资者，您好！公司在季度报告中披露产能利用率数据。公司2026年第一季度平均产能利用率为93.1%。感谢您的关注！ | substantive |
| 2026-06-01 | 2026-06-18 | 鉴于近期内存价格上涨，公司是否有转产nor,slc等内存代工的规划？如有，请问规划进度如何？谢谢。 | 尊敬的投资者，您好！公司在特殊存储领域（包括NOR、NAND等）已具备多年量产经验和技术积累。当前存储行业景气上行、产能整体供不应求，公司已着手布局更多产能，增加灵活性。感谢您的关注！ | directional-but-unquantified |
| 2026-05-19 | 2026-06-18 | 高资本开支的晶圆代工厂往往因为折旧金额高导致净利润比较低，因此专业投资者往往会看EBITDA利润率，请问贵公司EBITDA利润率多少？和同业相比高还是低 | 尊敬的投资者，您好！公司在季度报告中披露息税折旧摊销前利润率（EBITDA margin）。公司2026年第一季度国际会计准则下的息税折旧摊销前利润率为57.3%。感谢您的关注！ | substantive |
| 2026-05-18 | 2026-06-18 | 请问截止5月15日，公司的股东人数是多少？ | 尊敬的投资者，您好！如要查询定期报告时点以外的股东户数，您可携带本人身份证、证券账户证明、截止查询日的持股证明至公司或发送公司投资者关系邮箱 IR@smics.com ，公司将在核实股东身份后予以提供相关信息。感谢您的关注！ | substantive |
| 2026-05-14 | 2026-06-18 | 請問把带有时间和姓名的股票交易软件持仓截图和身份证一并扫描发送至公司邮箱，可以获知 非定期报告相关时点的股东人数吗？盼你们具体，明确答复。顺祝健康，快乐 【比如截至到2026年5月10日贵公司的股东人数是多少? | 尊敬的投资者，您好！如要查询定期报告时点以外的股东户数，您可携带本人身份证、证券账户证明、截止查询日的持股证明至公司或发送公司投资者关系邮箱 IR@smics.com ，公司将在核实股东身份后予以提供相关信息。感谢您的关注！ | substantive |

## Official Interaction Theme Reads
No data returned.

## Normalized Record Schema
| field | meaning |
| --- | --- |
| ts_code | A-share ticker |
| question_time / answer_time | official timestamps when exposed |
| question / answer | verbatim official interaction text |
| answer_class | substantive, directional-but-unquantified, non-committal, or unanswered |
| theme / story_read / proof_needed | mapped narrative, interpretation, and what still needs verification |
| source_type | cninfo_irm or sse_e_interaction |

## Analyst Instructions
- Treat official company answers as stronger narrative evidence than media association, but weaker than filings or announcements.
- Before feeding interaction content into valuation, classify answers as substantive, directional-but-unquantified, non-committal, or unanswered.
- Non-committal answers such as '感谢您的关注' or '请以公司公告为准' may remain narrative options, but they should not raise conviction.
- Use substantive interaction answers as tier-3 narrative options unless filings or announcements independently verify the same claim.