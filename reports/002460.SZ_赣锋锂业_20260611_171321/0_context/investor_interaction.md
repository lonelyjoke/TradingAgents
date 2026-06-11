# Investor interaction context for 002460.SZ as of 2026-06-11

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
| 2026-06-01 | 2026-06-04 | 尊敬的董秘，您好！请问截止2026年5月31日公司的股东人数是多少？谢谢！ | 投资者您好，截至2026年5月29日，公司A股股东人数为331,994户。 | substantive |
| 2026-05-29 | 2026-06-04 | 您好，贵公司截止到5月29日的股东人数是多少？谢谢！ | 投资者您好，截至2026年5月29日，公司A股股东人数为331,994户。 | substantive |
| 2026-05-20 | 2026-05-22 | 请问，2026年5月10日和5月20日股东数分别为多少？谢谢！ | 投资者您好，截至2026年5月8日，公司A股股东人数为333,631户；截至2026年5月20日，公司A股股东人数为341,075户 | substantive |
| 2026-05-19 | 2026-05-29 | 近日SMM新增库存数据将增加贸易商样本覆盖率,根据您的了解,贸易商那边的库存量一般都是多少?是否有传言那种大量未被统计的表外库存?谢谢 | 投资者您好，第三方机构调整库存数据统计口径，并不会改变行业实际库存基本面。当前，行业及公司锂矿石、锂产品库存天数均处于历史低位水平。从供需基本面角度看，行业去库趋势并未根本性逆转，下游需求仍然保持强劲韧性。 | directional-but-unquantified |
| 2026-05-19 | 2026-05-22 | 尊敬的董秘您好！请问截止2026年5月20日，公司的股东人数是多少，其中机构户数有多少？谢谢 | 投资者您好，截至2026年5月20日，公司A股股东人数为341,075户。 | substantive |
| 2026-05-18 | 2026-05-22 | 请问截止5月20日的股东人数和机构数量是多少？谢谢！ | 投资者您好，截至2026年5月20日，公司A股股东人数为341,075户。 | substantive |
| 2026-05-15 | 2026-06-04 | 你好懂秘，赣锋最新股东人数是多少 | 投资者您好，截至2026年5月29日，公司A股股东人数为331,994户。 | substantive |
| 2026-05-12 | 2026-05-22 | 请问贵公司4月10日股东人数和机构数量各是多少？ | 投资者您好，截至2026年4月10日，公司A股股东人数为298,985户。 | substantive |
| 2026-05-11 | 2026-06-04 | 董秘你好，天齐锂业最近股东数下降了3万，到25万了，我公司作为碳酸锂行业绝对龙头，目前股东数多少？ | 投资者您好，截至2026年5月29日，公司A股股东人数为331,994户。 | substantive |
| 2026-05-08 | 2026-05-29 | 请问董秘，公司二季度碳酸锂和电池订单情况如何？ | 投资者您好，目前公司在手订单较为充裕。 | substantive |

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