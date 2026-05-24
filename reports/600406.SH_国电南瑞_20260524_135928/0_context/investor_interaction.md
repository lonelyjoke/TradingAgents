# Investor interaction context for 600406.SH as of 2026-05-24

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=600406

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 406 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1776136756323 :国电南瑞(600406) 股价为什么一直掉呢？是不是有公告没披露？？？ 2026年04月14日 11:21 来自 Android ◆ ◆ 国电南瑞 股价受宏观环境、资金流向、市场情绪等多重因素影响。公司严格按照法律法规和交易所规则履行信息披露义务，所有应披露信息均已通过上交所网站及公司指定媒体及时、公平披露，不存在应披露而未披露的重大信息。感谢您对公司的关注。 | 收藏 | 评论 --> 2026年05月11日 16:39 来自 网站 ◆'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-05-06 | 2026-05-11 | 2025年年报显示，比亚迪成为公司前5位客户，双方交易金额达18亿。公司和比亚迪是那方面的合作？比亚迪提供什么服务及产品？是比亚迪闪充站的合作吗？ | 公司与比亚迪的合作主要集中在中东和欧洲的储能业务方面，为比亚迪提供PCS一体机及配套的调试服务。感谢您对公司的关注。 | directional-but-unquantified |
| 2026-04-30 | 2026-05-11 | 2026年一季报中怎么没有股东人数 | 截至2026年3月31日，公司普通股股东总数302,939户，上述信息已在公司2026年一季报中披露，感谢您对公司的关注。 | substantive |
| 2026-04-24 | 2026-05-11 | 为什么在华泰证券的涨乐财富通行情软件里，看不到公司的25年报? | 公司2025年年度报告已按规定在上交所网站及公司指定信息披露媒体发布。感谢您对公司的关注。 | non-committal |
| 2026-04-23 | 2026-05-11 | 您好，公司很长时间未回复投资者提问了，希望能够在百忙之中为投资者架好沟通桥梁！ 我的问题是目前国内电网的更新改造是否像光网通讯线路一样一是线缆及变电设备寿命临近，二是新技术、更智能、更大的用电需求推动电网改造面向智能智慧化及更低损耗的方向更新？ | 当前国内电网更新改造核心驱动来自老旧设备寿命到期与技术及需求双重升级。一方面老旧设备寿命到期，更新换代的刚性需求迫切；另一方面，随着新能源大规模并网、用电负荷增长及新型电力系统建设推进，电网改造正持续向智能化、数字化、低损耗、高可靠方向升级，以更好适应“双碳”目标和新型电力系统建设需求。相比光网通讯线路更新改造，电网是能源基础设施，需兼顾安全、稳定、新能源消纳，投资规模更大、周期更长。公司是以能源电力智能化为核心的能源互联网整体解决方案提供商，将持续服务电网智能化升级相关工作。感谢您对公司的关注。 | directional-but-unquantified |
| 2026-04-16 | 2026-05-11 | 敬的董秘，请问截止4月10日，贵公司的股东户数是多少？ | 根据公司第一季度报告，截至2026年3月31日，公司普通股股东总数302,939户。感谢您对公司的关注。 | substantive |
| 2026-04-14 | 2026-05-11 | 股价为什么一直掉呢？是不是有公告没披露？？？ | 股价受宏观环境、资金流向、市场情绪等多重因素影响。公司严格按照法律法规和交易所规则履行信息披露义务，所有应披露信息均已通过上交所网站及公司指定媒体及时、公平披露，不存在应披露而未披露的重大信息。感谢您对公司的关注。 | substantive |

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