# Investor interaction context for 300308.SZ as of 2026-07-18

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
| 2026-06-28 | 2026-07-05 | 近期传闻公司上游物料炫光片被封锁，市场定位公司只是一个中游组装厂，面临上下游挤压的双重风险，公司靠什么核心技术来应对风险？ | 投资者您好，首先，上述市场传言不符合事实。公司在核心物料方面都有正常的采购渠道，供应商也在积极支持，没有被封锁的情形。其次，光模块虽有组装工序（几十道工序之一），但不能简单等同于组装行业。高端光模块涵盖了硅光、相干、光路仿真建模、高频高速电路、精密光学耦合、色散补偿算法、高速误码测试以及温控与散热管理等核心技术，而且还需要长期可靠性测试与大客户严苛的准入认证。总结来说，光模块的系统设计与整合优化以及制造工艺都是核心技术，绝非简单拼装或组装。公司依靠快速高效的研发效率、精密制造和大规模交付能力，能够紧跟大客户技术迭代步伐，巩固核心竞争力和市场份额。感谢关注！ | substantive |
| 2026-06-27 | 2026-07-05 | 董秘先生你好，康宁玻璃桥的推出是否会对公司未来形成利空？ | 投资者您好，上述技术是CPO内部光耦合组件的新方案，不是光模块产品的方案替代；即使未来中长期成为主流，公司多元化的技术布局也能充分适配。感谢关注！ | substantive |
| 2026-06-22 | 2026-06-28 | 请问，未来3年内，公司是否有年利润达到500亿-1000亿的可能性？ | 投资者您好，公司未发布业绩指引，具体业绩情况均以公司披露的公告为准。感谢关注！ | directional-but-unquantified |
| 2026-06-22 | 2026-06-28 | 请问，公司应收账款是否到账及时？ | 投资者您好，公司主要客户账期较短，回款情况良好。感谢关注！ | substantive |
| 2026-06-21 | 2026-06-28 | 受上游原材料涨价传导因素，贵公司800G和1.6T产品是否已经涨价？涨价幅度是多少？ | 投资者您好，公司具体产品价格属于商业秘密不便披露，敬请谅解！ | substantive |
| 2026-06-19 | 2026-06-28 | 最近中际旭创的重大项目进展、时间推进、项目状态 | 投资者您好，公司现有项目都在顺利推进。感谢关注！ | directional-but-unquantified |
| 2026-06-19 | 2026-06-28 | 尊敬的董秘您好，请问贵司截止到6月18日股东人数是多少人？谢谢 | 投资者您好，公司会在后续定期报告中披露股东人数情况，感谢关注！ | substantive |
| 2026-06-14 | 2026-06-21 | 请问公司在验证卓胜微的光电芯片么 | 投资者您好，公司和哪家厂商有无合作以及具体合作关系，属于商业秘密，不便披露，敬请谅解！ | substantive |
| 2026-06-13 | 2026-06-21 | 董秘您好，公司二季度经营状况如何？上游物料（如100/200g eml光芯片）是否备料充足？如外围控货，建议加快国产替代方案，光迅、长光华芯等都是优秀的合作对象。
谢谢 | 投资者您好，1、公司二季度经营情况会在后续半年度报告里进行披露；2、公司会对上游核心物料积极备货以支持订单交付。感谢关注！ | substantive |
| 2026-06-13 | 2026-06-21 | 请教，日本于2月份禁止高端晶振出口，公司如何保障晶振的正常采购？ | 投资者您好，公司核心原材料供应稳定。感谢关注！ | directional-but-unquantified |

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