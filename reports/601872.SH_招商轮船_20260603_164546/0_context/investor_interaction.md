# Investor interaction context for 601872.SH as of 2026-06-03

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=601872

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 1872 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1779284481761 :招商轮船(601872) 尊敬的董秘您好，截止2026/5/20公司股东人数是多少？ 2026年05月21日 08:43 来自 网站 ◆ ◆ 招商轮船 您好，公司截止2026年5月20日股东户数为124,560，感谢关注。 | 收藏 | 评论 --> 2026年05月21日 12:52 来自 网站 ◆ ◆ 请登录后再点赞！ ◆ ◆ 请登录后再收藏！ 投资者_1772283808887 :招商轮船(601872) 董秘您好！请问截止到4月3'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-05-21 | 2026-05-21 | 尊敬的董秘您好，截止2026/5/20公司股东人数是多少？ | 您好，公司截止2026年5月20日股东户数为124,560，感谢关注。 | substantive |
| 2026-05-06 | 2026-05-06 | 请问贵公司截至2026年4月30日收盘的股东的户数? | 您好，公司截止2026年4月30日股东户数为126,151，感谢关注。 | substantive |
| 2026-04-30 | 2026-05-06 | 董秘您好！请问截止到4月30日，贵司的股东户数是多少？谢谢！ | 您好，公司截止2026年4月30日股东户数为126,151，感谢关注。 | substantive |

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