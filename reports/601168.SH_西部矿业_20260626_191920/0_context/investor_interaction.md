# Investor interaction context for 601168.SH as of 2026-06-26

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=601168

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 1168 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1658243748000 :西部矿业(601168) 今年氟制冷剂大涨。请问贵司氟化工今年是否盈利会改善？ 2026年06月22日 09:27 来自 网站 ◆ ◆ 西部矿业 今年以来氟制冷剂价格上涨，客观上对同鑫化无水氟化氢生产及销售业务盈利修复有正面作用。具体盈利情况请您关注定期报告。 | 收藏 | 评论 --> 2026年06月23日 18:15 来自 网站 ◆ ◆ 请登录后再点赞！ ◆ ◆ 请登录后再收藏！ 投资者_1629691541000 :西部矿业(60'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-22 | 2026-06-23 | 一季度矿产铅同比下降19.54%，另外还有7种产品也下降，二季度以及后来产量能上来吗？ | 一季度矿产铅及部分产品阶段性下滑，主要与生产组织节奏有关，属于阶段性波动，不会影响公司全年排产计划。公司将严格按年度计划推进，具体产量请以公司即将发布的定期报告为准。 | non-committal |
| 2026-06-22 | 2026-06-23 | 您好，请问公司6月20日的股东人数是多少？谢谢！ | 您好！截止6月18日，公司股东总户数为14.71万户。 | substantive |
| 2026-06-22 | 2026-06-23 | 今年氟制冷剂大涨。请问贵司氟化工今年是否盈利会改善？ | 今年以来氟制冷剂价格上涨，客观上对同鑫化无水氟化氢生产及销售业务盈利修复有正面作用。具体盈利情况请您关注定期报告。 | directional-but-unquantified |
| 2026-06-22 | 2026-06-23 | 请问截止6月20日，贵司的股东人数是多少？ | 您好！截止6月18日，公司股东总户数为14.71万户。 | substantive |
| 2026-06-15 | 2026-06-17 | 玉龙四期规划4500万吨，如果满产的话，对应钼产量一年是不是7500吨？ | 尊敬的投资者您好。目前玉龙铜矿4500万吨项目仍在论证过程中，项目对应的经济指标、金属产出等数据，需待整体论证完成并履行相关流程后，统一依规对外披露。 | substantive |
| 2026-06-15 | 2026-06-17 | 请问贵司1-5月份钼金属产量有多少？ | 尊敬的投资者朋友，您好！非常感谢您关心公司钼金属生产经营情况。截至一季度末，公司矿产钼产量1095吨已在一季报中公开披露。上半年相关数据，敬请各位投资者关注公司后续披露的半年报。 | directional-but-unquantified |
| 2026-06-15 | 2026-06-17 | 请问贵司大股东增持目前进展如何？ | 尊敬的投资者您好。公司控股股东相关增持计划正在实施中，如增持计划完成我们将及时公告。 | substantive |
| 2026-06-10 | 2026-06-11 | 您好，请问公司6月10日的股东人数是多少？谢谢！ | 您好！截止6月10日，公司股东总户数为14.25万户。 | substantive |
| 2026-06-10 | 2026-06-11 | 请问截止6月10日贵司的股东人数是多少？ | 您好！截止6月10日，公司股东总户数为14.25万户。 | substantive |
| 2026-06-01 | 2026-06-01 | 您好，请问公司5月底的股东人数是多少？谢谢！ | 您好！截止5月29日，公司股东总户数为14.74万户。 | substantive |

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