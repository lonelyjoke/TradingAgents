# Investor interaction context for 002460.SZ as of 2026-05-19

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=9900013787&stockcode=002460

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"002460","shortName":"赣锋锂业","pinyin":"GF |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-04-12 | 2026-04-28 | 请问截止4月10日公司股东人数是多少？ | 投资者您好，截至2026年4月10日，公司A股股东人数为298,985户。 | substantive |
| 2026-04-07 | 2026-04-13 | 一季报预告有发布计划吗？有的话求告知 | 尊敬的投资者，您好！非常感谢您对公司的关注。公司将根据相关上市规则进行业绩披露，请以公司后续在指定信息披露媒体发布的正式公告为准。 | substantive |
| 2026-04-02 | 2026-04-13 | 董秘您好，请问截止到2026年3月31日公司股东人数是多少？谢谢！ | 投资者您好，截至2026年3月31日，公司A股股东人数为287,622户。 | substantive |
| 2026-04-01 | 2026-04-13 | 请问如果公司一季报业绩达到预增标准，公司有出一季度业绩预增公告的计划吗？谢谢。 | 尊敬的投资者，您好！非常感谢您对公司的关注。公司将根据相关上市规则进行业绩披露，请以公司后续在指定信息披露媒体发布的正式公告为准。 | substantive |
| 2026-04-01 | 2026-04-13 | 请问公司最新股东人数是多少？ | 投资者您好，截至2026年3月31日，公司A股股东人数为287,622户。 | substantive |
| 2026-03-31 | 2026-04-13 | 根据2025年年报，公司前三季度利润之和为负，而第四季度直接导致全年利润由负转正，请问原因是什么，是否期末突击操纵所致？ | 投资者您好，感谢您对公司2025年年报的关注。公司2025年第四季度业绩的扭转，基于行业基本面回暖及公司经营成果的兑现。 | substantive |
| 2026-03-31 | 2026-04-13 | 根据2025年年报，公司前三季度利润之和为负，而第四季度利润突然大增，难道贵公司觉得合理吗？ | 投资者您好，感谢您对公司2025年年报的关注。公司2025年第四季度业绩的扭转，基于行业基本面回暖及公司经营成果的兑现。 | substantive |
| 2026-03-31 | 2026-04-13 | 尊敬的董秘你好，请问截止至2026年3月31日收盘公司股东人数为多少，谢谢！ | 投资者您好，截至2026年3月31日，公司A股股东人数为287,622户。 | substantive |
| 2026-03-30 | 2026-04-13 | 请教个咱公司财务处理问题。假如公司2月签订储能电池供货协议，2月电池放仓库值100亿，结果3月底还没交付，3月底电池涨价后值200亿。编制一季报时，没交付的电池算存货么？存货价值是交付前的100亿还是200亿。 | 投资者您好，从财务核算角度分析：该批未交付的电池应确认为存货，存货价值为初始价值。具体会计处理需结合公司与客户签订合同等实际情况进行综合判断。 | substantive |
| 2026-03-29 | 2026-04-13 | 一尊敬的董秘您好，请问3月27日股东人数是多少人？谢谢 | 投资者您好，截至2026年3月31日，公司A股股东人数为287,622户。 | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 1 | 0 | 0 | 2026-03-05 | single-point official signal |

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