# Investor interaction context for 002594.SZ as of 2026-05-20

- Exchange route: szse
- Official source home: https://irm.cninfo.com.cn/
- Canonical company route: https://irm.cninfo.com.cn/ircs/company/companyDetail?orgId=gshk0001211&stockcode=002594

## Official Endpoint Probe
| source | status | content_type | body_preview |
| --- | --- | --- | --- |
| cninfo | reachable | application/json;charset=UTF-8 | {"statusCode":200,"title":"","code":"","message":"success","data":[{"stockCode":"002594","shortName":"比亚迪","pinyin":"BYD |
| sse | not_applicable | N/A | N/A |

## Recent Official Q&A
| question_time | answer_time | question | answer | answer_class |
| --- | --- | --- | --- | --- |
| 2026-05-07 | 2026-05-07 | 我是长期坚定看好比亚迪的，但是我觉得比亚迪有些战略还是有必要调整一下，比如轨道交通项目，实在没必要过多的投资 | 尊敬的投资者，您好！衷心感谢您对公司的关注与宝贵建议！公司未来将持续聆听市场声音，审慎吸纳各类有价值的建言，以赋能公司核心能力提升与高质量发展。 | substantive |
| 2026-05-06 | 2026-05-07 | 你们的储能主要是用于闪充，也可以拓展到AI数据中心方面，尤其是技术那么先进 | 尊敬的投资者，您好！公司在储能领域有丰富的业务经验，依托全球领先的电池研发制造技术和强大的创新能力，产品涵盖电源侧、电网侧、工商业、闪充及家庭储能等应用领域。感谢您对公司业务拓展的关注及建议！ | substantive |
| 2026-05-06 | 2026-05-07 | 据传比亚迪固态电池项目已实现小规模量产，公司为何不发布相关公告告知投资者？ | 您好！公司始终秉持用技术创新，满足人们对美好生活的向往，持续深耕消费者核心需求，适时推出兼具市场竞争力与用户价值的产品及技术方案。后续相关动态，敬请关注公司官方发布的权威信息。感谢您对公司的关注与支持！ | substantive |
| 2026-05-06 | 2026-05-07 | 汽车行业近百个品牌竞争激烈带来技术安全售后参差不齐，尤其是某些小厂商出口质量可能会影响到头部企业口碑，公司是否考虑倡导严格行业质量准则？ | 尊敬的投资者，您好！公司始终秉持用技术创新，满足人们对美好生活的向往，持续深耕消费者核心需求，用优秀的产品实现与消费者的双赢。感谢您的建议和勉励！ | substantive |
| 2026-05-05 | 2026-05-07 | 董秘好，请问公司的王朝系列中，有考虑出一款“明”吗？毕竟现在明朝的粉丝数量宠大，建议公司可以出一款，价格在8～10万之间的比亚迪.明，一定会大卖。 | 尊敬的投资者，您好！衷心感谢您对公司的关注与宝贵建议！公司未来将持续聆听市场声音，审慎吸纳各类有价值的建言，以赋能公司核心能力提升与高质量发展。 | substantive |
| 2026-05-03 | 2026-05-07 | 你好，Tesla的semi已经开始量产了，公司的重卡进度如何？什么时候推出好用的高压平台货运卡车？ | 尊敬的投资者，您好！公司多年深耕新能源商用车领域，其中在重卡领域拥有牵引车Q3、搅拌车T25、搅拌车T31、自卸车T25、自卸车T31、环卫底盘T18等多款产品。感谢您对公司的关注！ | substantive |
| 2026-04-29 | 2026-05-07 | 贵公司目前股民总数是多少？ | 尊敬的投资者，您好！截止二零二六年一季度末，公司普通股股东总数为718,724户。感谢您对公司的关注！ | substantive |

## Official Interaction Theme Reads
| theme | story_read | proof_needed | mentions | answered | substantive | latest_question_time | signal_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| compute-power | new-demand adjacency around power + computing infrastructure | needs revenue, order, or project economics before valuation uplift | 4 | 1 | 1 | 2026-05-19 | repeated + substantive |
| buyback-shareholder-return | shareholder-return / valuation-support narrative | needs board approval, execution, and funding visibility | 5 | 0 | 0 | 2026-05-18 | single-point official signal |
| commercial-space | space linkage / investee optionality | ownership, monetization, or investee milestone still needs filing support | 1 | 0 | 0 | 2026-04-20 | single-point official signal |

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