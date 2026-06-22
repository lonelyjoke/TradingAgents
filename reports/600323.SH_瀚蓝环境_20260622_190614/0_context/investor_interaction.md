# Investor interaction context for 600323.SH as of 2026-06-22

- Exchange route: sse
- Official source home: https://sns.sseinfo.com/
- Canonical company route: https://sns.sseinfo.com/company.do?stockcode=600323

## Official Endpoint Probe
| source | status | company_page | uid | feed_preview |
| --- | --- | --- | --- | --- |
| cninfo | not_applicable | N/A | N/A | N/A |
| sse | reachable | {'title': '上证e互动', 'has_company_page': True, 'has_qa_section': True} | 323 | {'is_empty_recent_reply': False, 'text_preview': '投资者_1767666763996 :瀚蓝环境(600323) 尊敬的董秘您好，按照公司自身业绩加收购粤丰后，净利润可能会大幅度，对公司长远发展奠定基础，现在披露数据中还有一些不太清楚的问题烦请回答。1、公司只披露了并表的部分粤丰利润，请问2025年粤丰环保净利润？ 2、公司收购粤丰整合效应有哪些对粤丰净利润未来提升空间如何？ 3、按照公司分红规定2026年分红已经快接近50%了，未来还能提升吗？ 4、假设分红未来不提升，公司后续会考虑加大出海力度或者继续并购吗？ 2026年'} |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-06-08 | 2026-06-10 | 尊敬的董秘您好，按照公司自身业绩加收购粤丰后，净利润可能会大幅度，对公司长远发展奠定基础，现在披露数据中还有一些不太清楚的问题烦请回答。1、公司只披露了并表的部分粤丰利润，请问2025年粤丰环保净利润？ 2、公司收购粤丰整合效应有哪些对粤丰净利润未来提升空间如何？ 3、按照公司分红规定2026年分红已经快接近50%了，未来还能提升吗？ 4、假设分红未来不提升，公司后续会考虑加大出海力度或者继续并购吗？ | 尊敬的投资者，感谢您的关注！ 2025年公司归母净利润同比增加3.1亿元，增长18.58%，其中粤丰环保6-12月贡献归母净利润约2.7亿元。2025年6月，公司完成并购粤丰环保重大资产重组，并于年内基本完成财务、人力资源、供应链、信息化、品牌、合规等职能条线的融合，实现平稳过渡和管理初步融合，释放“1+1＞2”的协同效应。具体内容详见公司《2025年年度报告》。 在并购落地的同时，公司积极兑现分红承诺，根据《股东分红回报规划(2024年-2026年)》，公司2026年度每股派发的现金股利将较上一年同比增长不低于10%，即2026年度（含中期分红）每股现金分红不低于1.155元。若2026年度公司总股本增加，公司也将维持上述每股派发现金股利规划不变，体现了公司回报股东的决心和能力。 谢谢！ | substantive |
| 2026-05-25 | 2026-05-26 | 广东证监局官网5月22日公布对多人违规交易瀚蓝环境股票作出行政处罚，请问这些人员是否为公司员工？ | 尊敬的投资者您好，感谢您的关注。 针对您关注的行政处罚事项，公司郑重说明：本次被处罚人员均不是我司员工。谢谢！ | directional-but-unquantified |

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