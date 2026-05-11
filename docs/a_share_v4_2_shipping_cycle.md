# TradingAgents v4.2 航运景气模块说明

v4.2 新增航运景气模块，主要服务于招商轮船、中远海能、招商南油、中远海控等航运公司。

新增工具：

```text
get_shipping_context(ticker, curr_date, look_back_days=90)
```

## 1. 模块目标

航运股不能只看财报。油运、成品油运、干散货、集运、LNG 船的盈利都强烈依赖运价周期。

这个模块主要回答：

- 当前油运/干散货/成品油运景气度如何？
- 目标公司的主要航运敞口是什么？
- 哪些航线数据已经有证据，哪些仍然缺失？
- 如果报告里提到 VLCC、TCE、BDTI、BCTI、SCFI 等数据，是否有来源？

## 2. 当前公开指数来源

第一版接入公开 Baltic 指数代理：

| 指数 | 含义 | 适用 |
| --- | --- | --- |
| BDTI | Baltic Dirty Tanker Index | 原油/脏油轮市场代理 |
| BCTI | Baltic Clean Tanker Index | 成品油/清洁油轮市场代理 |
| BDI | Baltic Dry Index | 干散货综合景气代理 |
| BCI | Baltic Capesize Index | 海岬型船，铁矿石/煤炭大船代理 |
| BPI | Baltic Panamax Index | 巴拿马型船，煤炭/粮食代理 |
| BSI | Baltic Supramax Index | 超灵便型船，小宗散货代理 |

这些指数可以作为周期方向证据，但不能替代具体航线 TCE。

## 3. 航线覆盖

模块会列出常见航线和数据状态：

- VLCC：中东湾到中国，常看 TD3C 或中国进口 VLCC 代理。
- VLCC：西非到中国。
- Suezmax：西非到欧洲/美国。
- Aframax：区域原油贸易。
- MR：成品油轮东西向航线。
- LR2：石脑油/成品油航线。
- Capesize：巴西到中国铁矿石、西澳到中国铁矿石。
- Panamax：煤炭、粮食中型散货。
- Container：亚洲到欧洲、跨太平洋集运航线。
- LNG：LNG 船现货市场。

如果路线级别运价没有证据，agent 必须写成“未验证关键变量”，不能编造。

## 4. 当前内置股票映射

| 股票 | 主要板块 | 指数代理 |
| --- | --- | --- |
| 601872.SH 招商轮船 | 原油轮、干散货、LNG | BDTI、BDI、BCI、BPI |
| 600026.SH 中远海能 | 原油轮、成品油轮 | BDTI、BCTI |
| 601975.SH 招商南油 | 成品油轮 | BCTI、BDTI |
| 601919.SH 中远海控 | 集运 | 当前仅提示 SCFI/CCFI 未接入 |

## 5. 使用原则

对于招商轮船这类油运股，BDTI 只能说明原油轮市场的大方向，不能直接等同于 VLCC TD3C 或 TCE。

正确写法：

```text
BDTI 作为原油轮市场代理显示近期油运景气变化，但具体 VLCC TD3C/TCE 尚未接入，需人工核验。
```

错误写法：

```text
VLCC TD3C 今日上涨 20%，招商轮船利润将大增。
```

除非工具证据表里真的有 TD3C 或 TCE 数据。

## 6. 后续可扩展

后续可以继续接入：

- 上海航运交易所 CTFI。
- SCFI、CCFI 集运指数。
- Baltic Exchange 路线级 TCE。
- Clarksons 船队供给、新船订单、拆船数据。
- 港口拥堵和制裁绕航数据。

一句话：v4.2 先让系统具备“航运景气意识”，并且明确哪些运价结论有证据，哪些还需要人工核验。
