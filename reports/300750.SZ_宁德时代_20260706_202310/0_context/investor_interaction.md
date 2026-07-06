# Investor interaction context for 300750.SZ as of 2026-07-06

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=GD165627&stockcode=300750

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"300750","shortName":"宁德时代","pinyin":"ND |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-29 | 2026-07-03 | 建议公司收购璞泰来 | 投资者您好，感谢您的关注。 | directional-but-unquantified |
| 2026-06-23 | 2026-07-03 | 请问公司有没有芯片业务或者投资芯片企业？ | 投资者您好，请参考公开信息，感谢您的关注。 | directional-but-unquantified |
| 2026-06-18 | 2026-07-03 | 尊敬的董秘，您好！公司是top1新能源电池供应商，公司目前也有投资需求，不妨根据公司的电池销售数据结合当前使用企业的估值，考虑低价举牌某些心意的企业股权。总好过投一些没有销量的初创企业要好（例如x豆科技）。 | 投资者您好，感谢您的关注。 | directional-but-unquantified |
| 2026-06-11 | 2026-07-03 | 董秘您好，请问公司近期生产经营情况是否正常？谢谢。 | 投资者您好，公司生产经营正常，感谢您的关注。 | directional-but-unquantified |
| 2026-06-09 | 2026-06-22 | 请问公司在AIDC布局情况如何？未来是否考虑给csp厂直接对接交货？ | 投资者您好，全球 AI 数据中心的快速扩张带来了巨大的电力需求，公司已布局相关产品及解决方案，可用于数据中心领域，感谢您的关注。 | directional-but-unquantified |
| 2026-06-09 | 2026-06-18 | 请问公司固态电池什么时候可以量产？目前是在什么阶段 | 投资者您好，公司在全固态电池上持续坚定投入，技术处于行业领先水平，2027年有望实现小批量生产。感谢您的关注。 | directional-but-unquantified |
| 2026-06-08 | 2026-06-18 | 当前股东人数是多少？ | 投资者您好，股东人数信息请参考公司定期报告，感谢您的关注。 | substantive |
| 2026-06-02 | 2026-06-18 | 强制性国家标准《电动汽车安全要求》GB18384—2025在今年7月1日正式实施之后，预计会对具有行业龙头地位的我司带来哪些积极影响？谢谢 | 投资者您好，公司是国内首家通过新国标的企业，通过持续的技术创新，不断提升动力电池热扩散、底部防护、快充安全等方面的安全水平，推动新能源行业高质量发展，感谢您的关注。 | directional-but-unquantified |
| 2026-05-30 | 2026-06-18 | 建议公司收购中国宝安股权，建立完整的电池产业链 | 投资者您好，感谢您的关注。 | directional-but-unquantified |
| 2026-05-27 | 2026-06-18 | 请问贵司何时派发2025年议定的红利？ | 投资者您好，公司2025年度A股权益分派已完成，除息日及现金红利发放日为2026年4月22日，感谢您的关注。 | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 7 | 3 | 1 | 2026-06-23 | repeated + substantive |
| compute-power | new-demand adjacency around power + computing infrastructure | needs revenue, order, or project economics before valuation uplift | 5 | 2 | 0 | 2026-06-09 | single-point official signal |
| capital-allocation | capital-allocation quality narrative | needs realized return history or portfolio evidence | 1 | 0 | 0 | 2026-04-04 | single-point official signal |
| commercial-space | space linkage / investee optionality | ownership, monetization, or investee milestone still needs filing support | 1 | 1 | 0 | 2026-03-20 | single-point official signal |

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