# Investor interaction context for 600096.SH as of 2026-08-11

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=600096

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 96 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1779420309277 :云天化(600096) 您好！请问截至2026年7月20日公司的股东总数是多少？谢谢！ 2026年07月22日 13:42 来自 网站 ◆ ◆ 云天化 感谢您的关注。截至2026年7月20日，公司股东人数为16.78万名。 (1) | 收藏 | 评论 --> 2026年07月23日 09:46 来自 网站 ◆ ◆ 请登录后再点赞！ ◆ ◆ 请登录后再收藏！ 投资者_1583388055000 :云天化(600096) 请问董秘，为什么最近'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-07-22 | 2026-07-23 | 您好！请问截至2026年7月20日公司的股东总数是多少？谢谢！ | 感谢您的关注。截至2026年7月20日，公司股东人数为16.78万名。 | substantive |
| 2026-07-21 | 2026-07-23 | 请问董秘，为什么最近不回答股东提问？截止7月20日股东人数是多少？之前每10天都回答的问题，我问怎么就不回答了？ | 感谢您的关注。截至2026年7月20日，公司股东人数为16.78万名。 | substantive |

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