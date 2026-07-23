# Investor interaction context for 000933.SZ as of 2026-07-21

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
| 2026-07-16 | 2026-07-20 | 公司旗下有1100Y合金中强高延伸电池铝箔、8μm超薄电池铝箔、高达因电池铝箔、7μm高强度双面光电池铝箔等多款高性能电池铝箔产品，请问目前是销售是怎么定价？是电解铝加加工费定价模式吗？ | 除出口产品中少量实行一口价结算外，公司铝箔产品主要采用“铝锭价格+加工费”的定价模式。 | substantive |
| 2026-07-16 | 2026-07-20 | 请问公司目前电解铝箔产能有多少？分别是什么产品？听说在高端铝箔一块，公司有很多突破。有哪些技术优势的？是国内领先，还是国际领先 | 请查阅公司2025年年度报告。 | substantive |
| 2026-07-16 | 2026-07-20 | 请问神火新材的最新上市进展是怎么样？目前是否有委托中介机构开始上市辅导了 | 请关注公司2026年半年度报告。 | directional-but-unquantified |
| 2026-07-16 | 2026-07-20 | 公司聚焦电解铝及加工业，新疆参股的煤矿股份，是否考虑转让？公司目前参股的煤矿有哪一些？分别产能多少 | 公司暂未考虑转让所持新疆神兴能源有限责任公司的股权；公司目前仅参股新郑煤电赵家寨煤矿，产能300万吨/年。 | substantive |
| 2026-07-16 | 2026-07-20 | 公司新疆的风电项目，是否已完全并网使用？请问目前运转，是否有达到预期目标？目前发电情况如何。 | 公司新疆风电项目已实现全容量并网，运营正常。 | substantive |
| 2026-07-16 | 2026-07-20 | 公司无烟煤和瘦煤，目前核定产能是多少吨？目前产能利用率如何 | 公司无烟煤、贫瘦煤在产矿井核定产能为795万吨/年，具体产量情况请关注公司半年度报告。 | directional-but-unquantified |
| 2026-07-16 | 2026-07-20 | 公司披露定于什么时候发布2026年中期报告？是否有可能提前发布。 | 公司将于7月28日披露2026年半年度报告。 | substantive |
| 2026-07-15 | 2026-07-17 | 请问贵公司今年会有中期分红吗？ | 上市公司分红需履行董事会、股东会审议程序，公司目前尚未研究相关事项。 | substantive |
| 2026-07-13 | 2026-07-16 | 董秘你好，请问截止目前，公司股东数有多少？ | 截止7月10日。公司股东户数11.20万户。 | substantive |
| 2026-07-09 | 2026-07-14 | 请转达管理层，现在公司盈利好现金流强劲外加资本开支有限，在估值如此低估情况下，希望公司考虑每年拿50%的利润回购股份注销。 | 谢谢您的关注。 | non-committal |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 10 | 10 | 9 | 2026-07-09 | repeated + substantive |
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