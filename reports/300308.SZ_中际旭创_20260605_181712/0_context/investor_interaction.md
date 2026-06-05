# Investor interaction context for 300308.SZ as of 2026-06-05

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=9900022016&stockcode=300308

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"300308","shortName":"中际旭创","pinyin":"ZJ |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-05-27 | 2026-05-31 | 同花顺有文章说贵公司收购了FiconTEC，请问是否属实？ | 投资者您好，上述情况不属实。感谢关注！ | directional-but-unquantified |
| 2026-05-27 | 2026-05-31 | 请问公司的投资者热线是不是05358573361？为何长时间无人接听？ | 投资者您好，公司投资者热线：0535-8573360。感谢关注！ | directional-but-unquantified |
| 2026-05-26 | 2026-05-31 | 你好，请问1.6t光模块使用的晶振和800g光模块有什么区别吗？ | 投资者您好，随着产品的持续迭代，对上游原材料的性能和技术指标也会有更高要求。感谢关注！ | directional-but-unquantified |
| 2026-05-26 | 2026-05-31 | 贵公司业绩非常好，得益于二级市场融资以及广大投资者的支持，请问贵公司近期是否会考虑回馈广大投资者，采取以下一些方式：进行分红或股票送转，或者是回购注销呢？ | 投资者您好，公司2025年度分红于2026年4月30日实施完毕；同时，公司已制定《未来三年（2026年-2028年）股东回报规划》，明确重视对投资者的合理投资回报，并保持连续性和稳定性。感谢关注！ | substantive |
| 2026-05-24 | 2026-05-31 | 公司与深南电路有哪些技术和业务合作？ | 投资者您好，公司和哪家厂商有无合作以及具体合作关系，属于商业秘密，不便披露，敬请谅解！ | substantive |
| 2026-05-22 | 2026-05-31 | 请问贵公司5月8日，5月20日股东数量分别是多少？谢谢！ | 投资者您好，公司会在后续定期报告中披露股东人数情况，感谢关注！ | substantive |
| 2026-05-21 | 2026-05-31 | 公司好久没送股，国产光芯片方面有投资建没吗 | 投资者您好，公司目前主营业务不涉及光芯片的生产。感谢关注！ | directional-but-unquantified |
| 2026-05-18 | 2026-05-31 | 公司是否有规划布局太空数据中心相关项目，比如卫星之间激光互联的相关产品研发？ | 投资者您好，公司没有上述业务。感谢关注！ | directional-but-unquantified |
| 2026-05-11 | 2026-05-17 | 索尔思是否为公司的供应商，如果不是未来是否会考虑引入该细分行业的国内优秀公司？ | 投资者您好，公司有没有与哪家企业合作属于商业秘密，不便披露，敬请谅解！ | substantive |
| 2026-05-11 | 2026-05-17 | 基于光芯片的短缺，公司是否会引入国内新晋供应商来保证公司订单的交付？ | 投资者您好，公司有没有与哪家企业合作属于商业秘密，不便披露，敬请谅解！ | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| compute-power | new-demand adjacency around power + computing infrastructure | needs revenue, order, or project economics before valuation uplift | 4 | 3 | 1 | 2026-05-08 | repeated + substantive |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 1 | 1 | 1 | 2026-05-26 | single-point official signal |
| commercial-space | space linkage / investee optionality | ownership, monetization, or investee milestone still needs filing support | 1 | 1 | 0 | 2026-05-18 | single-point official signal |

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