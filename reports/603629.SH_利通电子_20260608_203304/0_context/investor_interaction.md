# Investor interaction context for 603629.SH as of 2026-06-08

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=603629

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 128241 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1780885525437 :利通电子(603629) 近期贵公司股票连续跌停，网上多篇小作文肆意传播，是否有重大利空？请董秘及时澄清 9小时前 来自 Android ◆ ◆ 利通电子 您好！针对公司近期舆情，公司澄清如下： 1、公司董事、高级管理人员等均正常履职，不存在被留置的情况。 2、公司董事、董事会秘书丁阿静女士，其任职资格及股权激励的股票授予，程序合法合规。 3、公司算力、制造业经营一切正常，在手订单都在按计划有序交付中。 4、有关公司情况请以公司公开发布的'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| N/A | N/A | Interaction retrieval unavailable: Invalid comparison between dtype=datetime64[s] and date |  | unavailable |

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