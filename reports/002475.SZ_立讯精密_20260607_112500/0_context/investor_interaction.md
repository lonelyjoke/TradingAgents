# Investor interaction context for 002475.SZ as of 2026-06-07

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=9900014448&stockcode=002475

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"002475","shortName":"立讯精密","pinyin":"LX |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-05-20 | 2026-05-22 | 你好，请问截至2026年5月20日，贵公司股东户数是多少？ | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-15 | 2026-05-22 | 请问贵公司最新股东户数是多少 | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-11 | 2026-05-22 | 尊敬的董秘你好，请问截止至2026年5月10日收盘公司股东人数为多少，谢谢！ | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-11 | 2026-05-22 | 尊敬的董秘你好，请问截止至2026年4月10日收盘公司股东人数为多少，谢谢！ | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-11 | 2026-05-22 | 你好，贵司截至2026年5月10日股东户数是多少？ | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-10 | 2026-05-22 | 董秘您好，我是公司在册股东，本着价值投资长期持有，麻烦告知：
截至5月10日最新股东户数，辛苦依规予以披露，谢谢！ | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-06 | 2026-05-22 | 董秘您好！请问贵公司截至2026年4月30，股东户数有多少？谢谢 | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-05 | 2026-05-22 | 请问贵司截止到4月30日股东人数是多少人？谢谢 | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-02 | 2026-05-22 | 请问截至2026年4月30日公司的股东总数是多少？谢谢 | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |
| 2026-05-01 | 2026-05-22 | 你好，请问贵公司截至4月30日股东户数是多少？谢谢 | 您好，截止5月20日，公司股东户数为414,971户，谢谢！ | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 13 | 12 | 12 | 2026-04-03 | repeated + substantive |
| compute-power | new-demand adjacency around power + computing infrastructure | needs revenue, order, or project economics before valuation uplift | 9 | 6 | 4 | 2026-06-03 | repeated + substantive |
| commercial-space | space linkage / investee optionality | ownership, monetization, or investee milestone still needs filing support | 2 | 1 | 1 | 2026-04-19 | repeated + substantive |
| capital-allocation | capital-allocation quality narrative | needs realized return history or portfolio evidence | 1 | 1 | 1 | 2026-05-10 | single-point official signal |

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