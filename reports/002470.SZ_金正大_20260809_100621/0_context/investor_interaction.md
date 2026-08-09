# Investor interaction context for 002470.SZ as of 2026-08-08

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=9900014252&stockcode=002470

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"002470","shortName":"金正大","pinyin":"JZD |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-07-06 | 2026-07-10 | 我注意到公司股票价格从3.82元/股下跌至1.99元/股，跌幅已近50%，二级市场投资者信心受到较大影响。
	1.	针对当前股价大幅波动，公司是否已制定并执行针对性的市值管理方案？具体包含哪些措施，目前实施进度及效果如何？
	2.	请结合公司2025年度及2026年以来的经营数据，说明管理层在战略规划、成本管控、市场拓展、风险防控等核心经营环节的履职情况，是否存在因失职导致公司价值受损的情形？ | 公司始终关注二级市场股价波动，持续通过规范信息披露、夯实经营基本面等常态化方式维护投资者权益；管理层聚焦主业稳健经营，统筹推进战略落地、成本管控、市场拓展与风险防控各项工作，勤勉履职，经营详情可查阅公司定期报告，感谢您的关注。 | substantive |
| 2026-07-04 | 2026-07-10 | 杨秘书，鉴于现在硫磺价格偏高，2024年改造的硫磺制酸项目，是不是应该花一个多亿改成磷石膏制酸呢？众所周知，咱们的阿尔法磷石膏技术不改变现有主流工艺，不增加任何生产成本，建议尽快改造成磷石膏制酸 | 感谢您的建议，公司持续跟进硫磺价格走势，公司将综合考虑市场及生产经营情况推进相应技改。 | non-committal |
| 2026-07-04 | 2026-07-10 | 第13次提问，大股东临沂金正大破产重整投资款第三期和第四期交了没有 | 感谢您的关注，第四期至第七期的重整投资款不涉及上市公司。此次重整是公司控股股东临沂金正大投资控股有限公司重整，非上市公司重整。公司严格按照相关法律法规履行信息披露义务，公司指定信息披露媒体为《证券时报》《中国证券报》《上海证券报》《证券日报》和巨潮资讯网（http://www.cninfo.com.cn）。 | non-committal |
| 2026-07-03 | 2026-07-10 | 尊敬的董秘，请问截止2026年6月30日，公司有多少股东？ | 感谢您的关注。股东人数不属于强制披露内容，为保证信息披露的公平性，公司只在定期报告中披露股东人数，其他时间点的股东人数暂不披露，具体详见未来定期报告。 | substantive |
| 2026-07-01 | 2026-07-10 | 请问董秘，贵公司子公司磷酸铁电池正极前驱体材料建设项目目前进展如何？预计什么时候投产？年产能预计达到多少？是否有目标市场或者客群？谢谢！ | 目前该项目正在建设中，尚未投产，请投资者注意投资风险，感谢您的关注。 | directional-but-unquantified |
| 2026-06-30 | 2026-07-10 | 您好，请问公司是否关注新能源汽车产业链及汽车零部件领域的并购机会？如有关注，公司更倾向于哪些细分方向及标的条件？ | 公司目前暂未有相关计划，感谢您的关注。 | directional-but-unquantified |
| 2026-06-30 | 2026-07-10 | 3亿资金已经还了，中信30亿注资在走流程，银行资金陆续也会来，这是真的吗？ | 公司重大事项请您关注公司在指定媒体发布的公告，感谢您的关注。 | directional-but-unquantified |
| 2026-06-29 | 2026-07-10 | 金丰公社股权信托今天到期，请问公司后续怎么处置？ | 受托人之间正在协商，相关信息请您关注公司在指定信息披露媒体发布的公告，感谢您的关注。 | non-committal |
| 2026-06-29 | 2026-07-10 | 请问兴业银行执行一事进展如何？ | 相关信息请您关注公司在指定信息披露媒体发布的公告，感谢您的关注。 | non-committal |
| 2026-06-29 | 2026-07-10 | 请问兴业银行的执行案现在结果如何？ | 相关信息请您关注公司在指定信息披露媒体发布的公告，感谢您的关注。 | non-committal |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 1 | 1 | 1 | 2026-07-06 | single-point official signal |

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