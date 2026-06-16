# Investor interaction context for 601168.SH as of 2026-06-16

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=601168

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 1168 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1658243748000 :西部矿业(601168) 请问截止6月10日贵司的股东人数是多少？ 2026年06月10日 08:58 来自 网站 ◆ ◆ 西部矿业 您好！截止6月10日，公司股东总户数为14.25万户。 | 收藏 | 评论 --> 2026年06月11日 18:17 来自 网站 ◆ ◆ 请登录后再点赞！ ◆ ◆ 请登录后再收藏！ 投资者_1723348400000 :西部矿业(601168) 您好，请问公司6月10日的股东人数是多少？谢谢！ 2026年'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-10 | 2026-06-11 | 您好，请问公司6月10日的股东人数是多少？谢谢！ | 您好！截止6月10日，公司股东总户数为14.25万户。 | substantive |
| 2026-06-10 | 2026-06-11 | 请问截止6月10日贵司的股东人数是多少？ | 您好！截止6月10日，公司股东总户数为14.25万户。 | substantive |
| 2026-06-01 | 2026-06-01 | 您好，请问公司5月底的股东人数是多少？谢谢！ | 您好！截止5月29日，公司股东总户数为14.74万户。 | substantive |
| 2026-05-21 | 2026-05-22 | 请问截止5月20日贵司的股东人数是多少？ | 您好！截止5月20日，公司股东总户数为15.66万户。 | substantive |
| 2026-05-21 | 2026-05-21 | 请问贵司大股东增持计划完成了吗？ | 尊敬的投资者您好。公司控股股东相关增持计划正在实施中，如增持计划完成我们将及时公告。 | substantive |
| 2026-05-21 | 2026-05-21 | 请问茶亭铜多金属矿勘探已经完成，何时能公布初步成果？ | 尊敬的投资者您好，感谢您的关注。目前茶亭铜多金属矿已完成全部钻孔施工工作，后续仍需开展样品测试、选矿试验、工业指标论证等相关工作，预计在2026年年底完成储量核实报告的编制工作，请以公司后续公告为准。 | non-committal |

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