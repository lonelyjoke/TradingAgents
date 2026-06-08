# Investor interaction context for 603345.SH as of 2026-06-07

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=603345

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 84823 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1650011448000 :安井食品(603345) 隔壁恒顺醋业买100股送调料礼包，公司考虑推出买股票送盘饺子的活动吗？我不想天天都关灯吃面了 2026年05月26日 15:59 来自 网站 ◆ ◆ 安井食品 尊敬的投资者，您好：感谢您的关注和建议。 | 收藏 | 评论 --> 2026年06月01日 09:39 来自 网站 ◆ ◆ 请登录后再点赞！ ◆ ◆ 请登录后再收藏！ 投资者_1573610506000 :安井食品(603345) 建议公司推出麻辣烫套装'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-05-26 | 2026-06-01 | 隔壁恒顺醋业买100股送调料礼包，公司考虑推出买股票送盘饺子的活动吗？我不想天天都关灯吃面了 | 尊敬的投资者，您好：感谢您的关注和建议。 | directional-but-unquantified |
| 2026-05-19 | 2026-06-01 | 建议公司推出麻辣烫套装，内容物为一包麻辣烫汤底和一包什锦丸子，单包价格控制在五元以内，顾客买回去后加点菜叶和泡面即可美美地煮一顿麻辣烫。这可能会开辟一块新的市场。 | 尊敬的投资者，您好：感谢您的关注和建议。 | directional-but-unquantified |
| 2026-05-06 | 2026-05-11 | 尊敬的董秘您好请问4月30日股东人数是多少人？谢谢 | 尊敬的投资者，您好：公司按照相关法律法规的规定，会在定期报告（季报、半年报、年报）中披露对应时点的股东户数。根据公司2026年第一季度报告，截至2026年3月31日，我司股东户数为28,646户。感谢您的关注。 | substantive |

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