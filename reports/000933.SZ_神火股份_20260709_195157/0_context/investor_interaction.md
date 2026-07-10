# Investor interaction context for 000933.SZ as of 2026-07-09

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=gssz0000933&stockcode=000933

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"000933","shortName":"神火股份","pinyin":"SH |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-07-01 | 2026-07-07 | 公司无烟煤和瘦煤销售，是否有长协？如果有，长协占比多少？价格怎么确定？ | 公司煤炭产品销售模式为签量不签价，价格随行就市。 | substantive |
| 2026-07-01 | 2026-07-07 | 请问子公司神火新材未来要上市的条件是什么？今年如果利润达到2亿，是否就具备条件了？ | 交易所针对不同板块设定了差异化的上市门槛，公司将根据神火新材实际经营情况积极推动其上市工作。 | substantive |
| 2026-07-01 | 2026-07-07 | 请问商丘三期铝箔项目的最新进展是怎么样？什么时候开工 | 公司全资子公司神火新材料科技有限公司年产5万吨新能源电池铝箔项目正按照项目建设有关规定有序推进中。 | substantive |
| 2026-07-01 | 2026-07-07 | 很多企业今年铝加工产品出口大增。请问贵司铝箔出口量变化如何？是否出口东南亚和欧洲？ | 公司铝箔业务出口量占铝箔产品总量的20%左右，覆盖亚洲、欧洲、南美洲等多个海外地区。 | substantive |
| 2026-07-01 | 2026-07-07 | 请问贵司目前铝箔加工产能利用率如何？目前订货排产到哪个月份了 | 公司目前铝箔产能处于满产状态，订单充足。 | substantive |
| 2026-07-01 | 2026-07-07 | 不少企业已经出了2026年中报预告，公司计划什么时候出业绩预告或者快报的？ | 公司将根据财务核算情况，按照信息披露的规定及时履行信息披露义务。 | substantive |
| 2026-06-30 | 2026-07-08 | 深交所规定：在减持时间区间内，若减持数量过半或时间过半，需向交易所报告并披露减持完成公告。这次减持的时间是5.14-8.13，时间已经过半，为什么不出公告？ | 谢谢您的关注。“在减持时间区间内，大股东、董监高在减持数量过半或减持时间过半时，应当披露减持进展情况”为《深圳证券交易所上市公司股东及董事、监事、高级管理人员减持股份实施细则》（2017年）第十三条内容，该实施细则已于2024年5月24日废止，现行有效监管规则已删除“减持时间过半、减持数量过半需披露进展公告”的相关规定，不再设置该类事项事中披露义务。公司将严格遵照现行减持监管规定履行相应信息披露义务。 | substantive |
| 2026-06-30 | 2026-07-06 | 请问在当前电力和氧化铝价格情况下，公司每吨电解铝成本大概是多少元？公司在电解铝行业，有哪些优势！ | 谢谢关注，请查阅公司年度报告中关于竞争优势的相关披露事项。电力和氧化铝作为电解铝生产的主要成本，存在一定区域的差异，因此项目的选址对成本构成影响比较大，请关注公司即将于7月28日披露的半年度报告。 | directional-but-unquantified |
| 2026-06-29 | 2026-07-06 | 请问公司配套生产碳素年产能多少吨？满足自身需求的大概多少吨？请问近期石油焦等原材料价格下降，对公司碳素业务影响如何？ | 感谢关注，请查阅公司年度报告相关披露事项，公司子公司新疆神火和云南神火均配套建设有年产40万吨的碳素项目，可以满足其自身生产需求。石油焦作为碳素生产的原材料，其价格下降，有利于降低碳素的生产成本。 | directional-but-unquantified |
| 2026-06-29 | 2026-07-06 | 很多公司已经出了2026年中报预告，请问公司是否已经编制？打算哪一天公布？ | 谢谢关注，公司会根据财务部门对数据的测算情况，按照信息披露的相关规定，在7月15日之前履行信息披露义务。 | directional-but-unquantified |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 9 | 9 | 9 | 2026-06-25 | repeated + substantive |
| compute-power | new-demand adjacency around power + computing infrastructure | needs revenue, order, or project economics before valuation uplift | 1 | 1 | 0 | 2026-06-18 | single-point official signal |

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