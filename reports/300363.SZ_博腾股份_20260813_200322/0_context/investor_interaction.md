# Investor interaction context for 300363.SZ as of 2026-08-13

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=9900022740&stockcode=300363

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"300363","shortName":"博腾股份","pinyin":"BT |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-07-22 | 2026-07-28 | 董秘好。目前市场紧缺高端合规OEB5高活Payload合成产能，请问公司市场竞争力如何？ | 您好，Payload-linker相关服务是公司新分子业务的服务内容之一，公司已在中国上海及美国新泽西建立了高活设施和能力，可承接临床前到商业化阶段的研发生产服务。新分子业务属于公司新兴业务之一，整体收入占公司营业收入比例较小。2025年实现收入0.68亿元，同比增长224%，占公司整体营业收入约2%。 | substantive |
| 2026-07-22 | 2026-07-28 | 董秘好，目前创新药Payload需求旺盛，请问对于公司有何影响？ | 您好，Payload-linker相关服务是公司新分子业务的服务内容之一，公司已在中国上海及美国新泽西建立了高活设施和能力，可承接临床前到商业化阶段的研发生产服务。新分子业务属于公司新兴业务之一，整体收入占公司营业收入比例较小。2025年实现收入0.68亿元，同比增长224%，占公司整体营业收入约2%。 | substantive |
| 2026-07-22 | 2026-07-27 | 董秘好，剔除减值影响，二季度利润环比大增，请问受益于什么产品？ | 您好，关于2026年半年度业绩具体情况，公司将在2026年半年度报告中进行披露，相关信息请以法定信息披露为准。 | non-committal |
| 2026-07-21 | 2026-07-27 | 贵公司新成立子公司，主营健康消费品市场，请问具体是什么产品？减肥药相关还是口含烟相关呢？ | 您好，公司设立全资子公司曜初生物主要是探索大健康消费品领域，目前处于成立初期，后续将根据相关业务开展进展履行相应的信息披露义务。 | directional-but-unquantified |
| 2026-07-21 | 2026-07-27 | 领导您好！国外瑞拓龄是一种定位在“延缓衰老”领域的膳食补充剂，在针对中年小鼠的实验中，据称能将剩余寿命延长34.4%，产品供不应求，国外很多顶尖富豪包括巴菲特也在服用。请问公司成立曜初生物科技有限公司会不会向这领域延伸？谢谢 | 您好，公司设立全资子公司曜初生物主要是探索大健康消费品领域，目前处于成立初期，后续将根据相关业务开展进展履行相应的信息披露义务。 | directional-but-unquantified |
| 2026-07-16 | 2026-07-17 | 请问公司7月10日股东人数，谢谢！ | 截至2026年7月10日收盘，公司股东总户数（合并普通账户和融资融券信用账户）为48,036户。 | substantive |
| 2026-07-14 | 2026-07-17 | 请问截止7月10日公司股东户数是多少？谢谢 | 截至2026年7月10日收盘，公司股东总户数（合并普通账户和融资融券信用账户）为48,036户。 | substantive |
| 2026-07-06 | 2026-07-13 | 您好！请问截至6月底股东人数是多少，谢谢！ | 您好，公司将在2026年半年度报告中披露截至2026年6月30日的股东户数。 | substantive |
| 2026-06-30 | 2026-07-07 | 请问贵司公告回购股票进展情况如何了？什么时候注销？谢谢 | 您好，截至2026年6月30日，公司累计通过股票回购专用证券账户以集中竞价交易方式回购公司股份5,907,619股，占公司当前总股本的1.09%，最高成交价为16.49元/股，最低成交价为13.32元/股，成交总金额为83,776,250.93元（不含手续费）。后续公司将根据回购进展持续履行信息披露义务。 | substantive |
| 2026-06-04 | 2026-07-06 | 请问三位股东的股票质押价是多少，目前已临近平仓线，公司有提升股价防止平仓的打算吗？ | 您好，截至目前，公司未收到实际控制人关于质押股份触及平仓线或需强制平仓的通知，不存在应披露而未披露的重大事项。 | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 2 | 1 | 1 | 2026-06-30 | repeated + substantive |

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