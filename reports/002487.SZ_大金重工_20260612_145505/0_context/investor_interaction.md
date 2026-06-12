# Investor interaction context for 002487.SZ as of 2026-06-12

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=9900014996&stockcode=002487

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"002487","shortName":"大金重工","pinyin":"DJ |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-03 | 2026-06-08 | 请问5月30日的股东人数是多少？ | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-05-20 | 2026-06-08 | 您好，最新股东户数多少？ | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-05-20 | 2026-06-08 | 请问！最新股东户数是多少！谢谢！ | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-05-08 | 2026-06-08 | 请问截止5月10日股东户数是多少，麻烦抽空查下，谢谢！ | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-05-06 | 2026-06-08 | 董秘您好！我想查询截至2026年4月30日公司最新股东人数? | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-05-04 | 2026-06-08 | 请问截至止2026年4月30日公司的股东总数是多少？谢谢 | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-04-21 | 2026-06-08 | 董秘您好！我想查询截至2026年4月20日公司最新股东人数？ | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-04-17 | 2026-06-08 | 请问最新股东户数是多少，谢谢 | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-04-12 | 2026-06-08 | 董秘您好！我想查询截至2026年4月10日公司最新股东人数？谢谢 | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |
| 2026-04-09 | 2026-06-08 | 请问4月10日股东户数是多少？谢谢 | 尊敬的投资者，您好！截至2026年5月29日，公司股东户数54,457户。谢谢！ | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| compute-power | new-demand adjacency around power + computing infrastructure | needs revenue, order, or project economics before valuation uplift | 2 | 0 | 0 | 2026-05-18 | single-point official signal |
| commercial-space | space linkage / investee optionality | ownership, monetization, or investee milestone still needs filing support | 1 | 0 | 0 | 2026-05-09 | single-point official signal |

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