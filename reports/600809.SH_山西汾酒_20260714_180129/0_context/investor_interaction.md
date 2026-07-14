# Investor interaction context for 600809.SH as of 2026-07-14

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=600809

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 809 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1778644894190 :山西汾酒(600809) 你好，请问贵公司有考虑出一款混合果汁低度酒吗？比如主打纯果汁无添加，度数低好入口等理念，来迎合年轻消费群体。 2026年06月15日 09:28 来自 Android ◆ ◆ 山西汾酒 感谢您关于果汁低度酒的建议。顺应低度化、天然悦己消费趋势，公司已落地陈皮汾酒，作为 “汾酒 +” 露酒单品，精准覆盖年轻微醺场景,挖掘年轻消费增长空间。 | 收藏 | 评论 --> 2026年06月26日 10:27 来自 网站 '} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-24 | 2026-06-26 | 你好 我是一个爱好喝酒的 也是汾酒的拥护者 小股东 希望汾酒做大做强 汾酒复兴 但是感觉汾酒产品还没有完全下沉市场 既然竹叶青是保健酒那应该对标劲酒那样 小型大型便利店 都应该有对标产品 杏花村也是 做不了高端 做好中低端 汾酒做好 中高低端 高端对标茅台飞天 甚至做到更好 我觉得汾酒做的市场还不够极致 细致 不够大 希望能够超越五粮液 优于五粮液 比肩茅台 产品 做到极致 | 感谢您的建议！ | non-committal |
| 2026-06-15 | 2026-06-26 | 你好，请问贵公司有考虑出一款混合果汁低度酒吗？比如主打纯果汁无添加，度数低好入口等理念，来迎合年轻消费群体。 | 感谢您关于果汁低度酒的建议。顺应低度化、天然悦己消费趋势，公司已落地陈皮汾酒，作为 “汾酒 +” 露酒单品，精准覆盖年轻微醺场景,挖掘年轻消费增长空间。 | substantive |

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