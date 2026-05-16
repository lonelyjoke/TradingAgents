from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Iterable

import pandas as pd

from .config import get_config
from .tushare_a_stock import (
    TushareDataError,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    is_a_share_symbol,
)
from .thematic_research import _compact_text, _load_financial_report_texts


@dataclass(frozen=True)
class FilingEvidence:
    category: str
    signal: str
    evidence: str
    bull_use: str
    bear_use: str


@dataclass(frozen=True)
class FilingQuestion:
    question_id: str
    category: str
    question: str
    keywords: tuple[str, ...]
    preferred_report_types: tuple[str, ...]
    bull_use: str
    bear_use: str


@dataclass(frozen=True)
class FilingQuestionAnswer:
    question_id: str
    category: str
    question: str
    report_type: str
    evidence_strength: str
    evidence: str
    bull_use: str
    bear_use: str


_FILING_SIGNAL_RULES: tuple[tuple[str, tuple[str, ...], str, str], ...] = (
    (
        "demand_visibility",
        ("在手订单", "新增订单", "订单储备", "中标", "合同负债", "预收款项"),
        "Argue revenue visibility, order momentum, or deferred demand already embedded in filings.",
        "Challenge profitability, conversion timing, cancellations, and whether order growth merely masks margin pressure.",
    ),
    (
        "commercialization",
        ("营业收入", "业务收入", "实现收入", "销售收入", "投产", "量产", "客户导入"),
        "Argue that a strategy is becoming monetized rather than remaining narrative.",
        "Test whether the disclosed scale is still too small, one-off, or low margin.",
    ),
    (
        "pricing_and_margin",
        ("毛利率", "价格", "降价", "竞价", "招投标", "成本", "原材料"),
        "Use disclosed pricing or margin language to support an earnings inflection if the trend improves.",
        "Use pressure language to attack profit durability and operating leverage assumptions.",
    ),
    (
        "capacity_and_capex",
        ("产能", "产量", "扩产", "建设项目", "在建工程", "固定资产投资", "资本开支"),
        "Argue future supply, growth runway, or operating leverage from capacity build-out.",
        "Challenge utilization, overcapacity, return on capital, and capex-before-demand risk.",
    ),
    (
        "customer_and_geography",
        ("客户", "海外", "境外", "出口", "区域市场", "市场份额"),
        "Argue market expansion, diversification, or customer validation.",
        "Challenge concentration, collection risk, geopolitical exposure, and lower-quality growth.",
    ),
    (
        "innovation_and_product",
        ("研发", "新产品", "专利", "认证", "技术突破", "迭代"),
        "Argue moat-building, product upgrade, or future mix improvement.",
        "Question commercialization, payback period, and whether R&D is defending rather than expanding moat.",
    ),
    (
        "cash_and_working_capital",
        ("应收账款", "存货", "回款", "经营活动现金流", "合同资产", "减值准备"),
        "Use cash conversion or working-capital improvement to validate earnings quality.",
        "Use receivables, inventory, or weak cash language to challenge revenue quality.",
    ),
    (
        "balance_sheet_and_risk",
        ("担保", "诉讼", "仲裁", "商誉", "资产减值", "关联交易", "重大风险"),
        "Use resilience disclosures only if they directly reduce tail risk.",
        "Surface contingent liabilities, impairments, governance, or off-balance-sheet risk.",
    ),
)

_GENERIC_QUESTIONS: tuple[FilingQuestion, ...] = (
    FilingQuestion(
        "generic_revenue_quality",
        "revenue_quality",
        "收入增长是否有真实业务支撑，而非仅由应收或一次性因素堆出来？",
        ("营业收入", "销售收入", "应收账款", "合同资产", "经营活动现金流"),
        ("quarterly", "semiannual", "annual"),
        "Use matching revenue, cash, and receivable evidence to support quality growth.",
        "Attack any divergence between reported growth and cash realization.",
    ),
    FilingQuestion(
        "generic_profit_quality",
        "profit_quality",
        "利润改善来自主业、价格、成本，还是投资收益/减值/公允价值等非经常因素？",
        ("毛利率", "营业利润", "投资收益", "公允价值", "资产减值", "非经常"),
        ("quarterly", "semiannual", "annual"),
        "Support durable earnings when the improvement clearly comes from core operations.",
        "Separate operating earnings from accounting or one-off noise.",
    ),
    FilingQuestion(
        "generic_cash_conversion",
        "cash_quality",
        "利润能否转成现金，还是被应收、存货、预付款拖住？",
        ("经营活动现金流", "应收账款", "存货", "预付款项", "合同资产", "回款"),
        ("quarterly", "semiannual", "annual"),
        "Use improving conversion to validate the thesis.",
        "Use deteriorating working capital to challenge profit quality.",
    ),
    FilingQuestion(
        "generic_capital_allocation",
        "capital_allocation",
        "管理层把钱投向哪里，资本开支是否正在创造未来收益？",
        ("资本开支", "在建工程", "固定资产", "研发投入", "并购", "分红"),
        ("semiannual", "annual"),
        "Argue reinvestment is building future earnings power.",
        "Question return on capital, empire building, or delayed payback.",
    ),
    FilingQuestion(
        "generic_risk_disclosure",
        "risk",
        "财报中新增或升级了哪些真正会改变股权价值的风险？",
        ("担保", "诉讼", "仲裁", "商誉", "资产减值", "重大风险", "或有事项"),
        ("semiannual", "annual"),
        "Use risk relief only when disclosures become visibly safer.",
        "Surface tail risks the market may be underweighting.",
    ),
)

_INDUSTRY_PLAYBOOKS: dict[str, tuple[FilingQuestion, ...]] = {
    "wind_power_equipment": (
        FilingQuestion(
            "wind_orders",
            "orders",
            "新增订单、在手订单和合同负债是否同步改善，还是只有收入在冲？",
            ("新增订单", "在手订单", "订单储备", "合同负债"),
            ("quarterly", "semiannual", "annual"),
            "Support demand visibility and delivery backlog.",
            "Ask whether backlog converts into margin or just low-priced volume.",
        ),
        FilingQuestion(
            "wind_pricing",
            "pricing",
            "招投标价格、风机单价和毛利率是否真正止跌？",
            ("招投标", "中标价格", "价格", "毛利率", "风机"),
            ("quarterly", "semiannual"),
            "Argue margin inflection if pricing stabilizes.",
            "Attack any bull thesis that assumes a bottom without disclosed evidence.",
        ),
        FilingQuestion(
            "wind_mix",
            "mix",
            "海上风电、大兆瓦机型、海外业务、风电场运营谁在改善利润结构？",
            ("海上风电", "大兆瓦", "海外", "风电场", "机组容量"),
            ("semiannual", "annual"),
            "Show mix upgrade and higher-value revenue.",
            "Question whether higher-growth segments are still too small or lower quality.",
        ),
        FilingQuestion(
            "wind_overseas_risk",
            "overseas",
            "海外扩张带来的是订单、利润，还是先带来担保和回款风险？",
            ("海外", "境外", "担保", "保函", "应收账款"),
            ("semiannual", "annual"),
            "Support diversification and global optionality.",
            "Stress execution, guarantees, and receivable risk.",
        ),
    ),
    "environmental_services": (
        FilingQuestion(
            "env_order_quality",
            "orders",
            "新增订单是真增长，还是低价抢单、长周期项目堆积？",
            ("新增订单", "在手订单", "中标", "项目"),
            ("quarterly", "semiannual", "annual"),
            "Support future revenue visibility.",
            "Question margin, collection, and project-cycle quality.",
        ),
        FilingQuestion(
            "env_service_mix",
            "mix",
            "设备、服务、运营业务的收入和毛利结构是否优化？",
            ("环卫装备", "环卫服务", "运营", "毛利率", "分部"),
            ("semiannual", "annual"),
            "Support recurring revenue and better business mix.",
            "Expose whether low-margin projects dominate growth.",
        ),
        FilingQuestion(
            "env_receivables",
            "cash_quality",
            "政府客户回款、应收账款和合同资产有没有恶化？",
            ("应收账款", "合同资产", "回款", "政府客户"),
            ("quarterly", "semiannual", "annual"),
            "Use improving collections to validate earnings.",
            "Attack profit quality if cash lags project revenue.",
        ),
        FilingQuestion(
            "env_new_business",
            "new_business",
            "新业务已经贡献收入利润，还是仍停留在战略表述？",
            ("新业务", "算力租赁", "业务收入", "实现收入", "客户导入"),
            ("quarterly", "semiannual", "annual"),
            "Support monetization when filings quantify it.",
            "Keep vague diversification out of base-case valuation.",
        ),
    ),
    "banking": (
        FilingQuestion(
            "bank_asset_quality",
            "asset_quality",
            "不良率、关注类贷款、拨备覆盖和逾期迁徙是否在改善？",
            ("不良贷款率", "关注类贷款", "拨备覆盖率", "逾期贷款", "迁徙率"),
            ("quarterly", "semiannual", "annual"),
            "Support cleaner asset quality and lower credit-cost risk.",
            "Challenge hidden deterioration before it hits profits.",
        ),
        FilingQuestion(
            "bank_nim",
            "profitability",
            "净息差压力是否缓解，还是利润靠规模硬撑？",
            ("净息差", "生息资产", "贷款收益率", "存款成本率"),
            ("quarterly", "semiannual", "annual"),
            "Argue earnings resilience if spread stabilizes.",
            "Attack profitability if volume masks spread compression.",
        ),
        FilingQuestion(
            "bank_fees",
            "mix",
            "中收、零售、财富管理能否抵消传统息差压力？",
            ("手续费", "中间业务", "零售", "财富管理"),
            ("semiannual", "annual"),
            "Support business diversification.",
            "Question whether fee income is cyclical or shrinking.",
        ),
    ),
    "shipping": (
        FilingQuestion(
            "shipping_rates",
            "pricing",
            "运价、TCE、租船价格和运力利用率是否在改善？",
            ("运价", "TCE", "租船", "运力利用率"),
            ("quarterly", "semiannual", "annual"),
            "Support cycle upswing and operating leverage.",
            "Attack if rates remain spot-driven or below replacement economics.",
        ),
        FilingQuestion(
            "shipping_fleet",
            "capacity",
            "船队扩张、订单簿和资本开支是在放大利润，还是把周期顶部资本化？",
            ("船队", "订单簿", "新增运力", "资本开支", "造船"),
            ("semiannual", "annual"),
            "Support growth when capacity enters a favorable cycle.",
            "Challenge oversupply and poor capital timing.",
        ),
        FilingQuestion(
            "shipping_contracts",
            "visibility",
            "长协、现货和区域结构怎样影响利润确定性？",
            ("长协", "现货", "租约", "航线", "区域"),
            ("semiannual", "annual"),
            "Support earnings visibility if contracted coverage improves.",
            "Expose spot exposure and route concentration.",
        ),
    ),
    "software_services": (
        FilingQuestion(
            "software_arr",
            "recurring_revenue",
            "订阅、续费、云收入和合同负债是否显示业务质量改善？",
            ("订阅", "续费", "云收入", "合同负债", "ARR"),
            ("quarterly", "semiannual", "annual"),
            "Support recurring revenue and visibility.",
            "Question growth if bookings fail to convert into durable cash.",
        ),
        FilingQuestion(
            "software_sales_efficiency",
            "efficiency",
            "销售费用率、获客成本和人效是否在改善？",
            ("销售费用率", "销售费用", "人均", "获客", "合同获取成本"),
            ("quarterly", "semiannual", "annual"),
            "Support operating leverage.",
            "Attack if growth depends on ever-higher selling intensity.",
        ),
        FilingQuestion(
            "software_product",
            "product",
            "新产品、AI能力和大客户签约已经商业化，还是仍属概念？",
            ("新产品", "AI", "人工智能", "大客户", "商业化", "客户导入"),
            ("semiannual", "annual"),
            "Support product-led upsell when quantified.",
            "Reject concept-only rerating without monetization.",
        ),
    ),
    "metals_mining": (
        FilingQuestion(
            "metals_resource_volume",
            "resource",
            "资源储量、品位、权益产量和达产节奏有没有继续兑现？",
            ("资源储量", "矿石品位", "权益产量", "金属量", "达产", "采选"),
            ("semiannual", "annual"),
            "Support reserve life, volume growth, and long-cycle earnings visibility.",
            "Challenge reserve quality, dilution, and whether volume growth is value-accretive.",
        ),
        FilingQuestion(
            "metals_price_cost",
            "pricing",
            "金属价格上行能否穿透到利润，还是被冶炼费、能源和单位成本吃掉？",
            ("铜价", "铝价", "金价", "锂价", "冶炼加工费", "单位成本", "完全成本"),
            ("quarterly", "semiannual", "annual"),
            "Support operating leverage when realized prices rise faster than costs.",
            "Attack commodity beta if cost inflation or TC/RC pressure offsets price upside.",
        ),
        FilingQuestion(
            "metals_capex",
            "capital_allocation",
            "扩产、并购和海外矿山投入是在低位锁资源，还是在高位资本开支？",
            ("资本开支", "扩产", "并购", "矿山建设", "海外项目", "在建工程"),
            ("semiannual", "annual"),
            "Support resource replacement and counter-cyclical expansion.",
            "Question project returns, jurisdiction risk, and peak-cycle overinvestment.",
        ),
        FilingQuestion(
            "metals_inventory_hedging",
            "risk",
            "库存、套保和汇率暴露会不会放大利润波动？",
            ("库存商品", "套期保值", "衍生金融工具", "汇率", "存货跌价"),
            ("quarterly", "semiannual", "annual"),
            "Show disciplined risk management and cleaner earnings conversion.",
            "Surface hidden mark-to-market, inventory, and FX risks.",
        ),
    ),
    "lithium_battery": (
        FilingQuestion(
            "battery_capacity_utilization",
            "capacity",
            "产能、产能利用率和出货量是否同步改善，还是行业供给仍然过剩？",
            ("产能", "产能利用率", "出货量", "动力电池", "储能电池", "GWh"),
            ("quarterly", "semiannual", "annual"),
            "Support volume recovery and operating leverage.",
            "Challenge overcapacity and weak utilization beneath revenue growth.",
        ),
        FilingQuestion(
            "battery_price_margin",
            "pricing",
            "产品降价、原材料传导和毛利率之间的关系是否开始改善？",
            ("碳酸锂", "产品价格", "降价", "原材料", "毛利率", "单位售价"),
            ("quarterly", "semiannual"),
            "Argue margin repair if input costs fall faster than ASPs.",
            "Attack the thesis if price war erodes economics faster than cost relief.",
        ),
        FilingQuestion(
            "battery_customer_mix",
            "customer",
            "客户结构、海外订单和储能占比有没有改善收入质量？",
            ("客户结构", "海外客户", "储能", "动力电池", "装机", "客户导入"),
            ("semiannual", "annual"),
            "Support diversification and better mix.",
            "Question customer concentration, certification lag, and lower-quality growth.",
        ),
        FilingQuestion(
            "battery_technology",
            "innovation",
            "新体系、新产品和研发投入已经形成商业化优势，还是仍停留在技术叙事？",
            ("固态电池", "快充", "高镍", "磷酸铁锂", "研发投入", "量产"),
            ("semiannual", "annual"),
            "Support moat and next-cycle product leadership.",
            "Challenge monetization, capex burden, and technology obsolescence.",
        ),
    ),
    "baijiu": (
        FilingQuestion(
            "baijiu_channel_inventory",
            "channel",
            "批价、渠道库存、回款和合同负债是否一起健康，而不是靠压货维持增长？",
            ("批价", "渠道库存", "经销商", "回款", "合同负债", "预收款"),
            ("quarterly", "semiannual", "annual"),
            "Support healthy demand and channel discipline.",
            "Attack hidden inventory, over-shipment, and demand pull-forward.",
        ),
        FilingQuestion(
            "baijiu_product_mix",
            "mix",
            "高端、次高端和大众价位的结构变化，是否真的抬升品牌力和吨价？",
            ("高端", "次高端", "产品结构", "吨价", "系列酒", "核心单品"),
            ("semiannual", "annual"),
            "Support premiumization and mix-driven profit growth.",
            "Question whether mix-up is offset by weak volume or discounting.",
        ),
        FilingQuestion(
            "baijiu_region_expansion",
            "growth",
            "省内、省外和直营网点扩张，是自然渗透还是费用换规模？",
            ("省内", "省外", "直营网点", "直营网店", "全国化", "销售费用"),
            ("semiannual", "annual"),
            "Support geographic expansion and brand replication.",
            "Challenge selling-expense intensity and fragile out-of-province growth.",
        ),
        FilingQuestion(
            "baijiu_cash_quality",
            "cash_quality",
            "现金回款、预收和经营现金流是否仍配得上利润质量？",
            ("销售商品、提供劳务收到的现金", "合同负债", "经营活动现金流", "货币资金"),
            ("quarterly", "semiannual", "annual"),
            "Validate high-quality earnings and channel pull.",
            "Expose profit growth unsupported by real cash collection.",
        ),
    ),
    "airlines": (
        FilingQuestion(
            "airline_traffic_yield",
            "traffic",
            "ASK、RPK、客座率和客公里收益，谁在真正驱动利润修复？",
            ("ASK", "RPK", "客座率", "客公里收益", "旅客周转量", "座公里"),
            ("quarterly", "semiannual", "annual"),
            "Support operating leverage when traffic and yield improve together.",
            "Challenge weak pricing if volume recovers without yield.",
        ),
        FilingQuestion(
            "airline_fuel_fx",
            "cost",
            "航油、汇率和租赁负债对利润的扰动是否在缓和？",
            ("航油", "燃油成本", "汇率", "租赁负债", "美元负债"),
            ("quarterly", "semiannual", "annual"),
            "Support earnings recovery when macro headwinds ease.",
            "Stress exogenous cost sensitivity and balance-sheet fragility.",
        ),
        FilingQuestion(
            "airline_capacity_routes",
            "capacity",
            "国际航线恢复、机队投放和运力结构是否带来更优收益，而非重新打价格战？",
            ("国际航线", "机队", "运力投放", "航线网络", "飞机引进"),
            ("semiannual", "annual"),
            "Support route-mix and capacity normalization upside.",
            "Question supply discipline and route-level profitability.",
        ),
    ),
    "insurance": (
        FilingQuestion(
            "insurance_nbv",
            "growth",
            "新业务价值、新单保费和代理人产能是否同步改善？",
            ("新业务价值", "新单保费", "首年保费", "代理人", "人均产能"),
            ("quarterly", "semiannual", "annual"),
            "Support franchise recovery and future profit emergence.",
            "Challenge superficial premium growth without value growth.",
        ),
        FilingQuestion(
            "insurance_investment",
            "investment",
            "投资收益、净投资收益率和综合投资收益率是否足以支撑利润与内含价值？",
            ("投资收益率", "净投资收益率", "综合投资收益率", "内含价值", "资产配置"),
            ("quarterly", "semiannual", "annual"),
            "Support spread resilience and EV growth.",
            "Stress reinvestment risk, equity-market sensitivity, and yield compression.",
        ),
        FilingQuestion(
            "insurance_quality",
            "quality",
            "继续率、退保率和产品结构是否说明销售质量在改善？",
            ("继续率", "退保率", "产品结构", "保障型", "储蓄型"),
            ("semiannual", "annual"),
            "Support better-quality growth and franchise durability.",
            "Question whether growth is driven by low-quality savings products.",
        ),
        FilingQuestion(
            "insurance_pnc",
            "underwriting",
            "若有财险业务，综合成本率改善来自定价与风控，还是只是赔付暂时偏低？",
            ("综合成本率", "赔付率", "费用率", "财产险", "车险"),
            ("quarterly", "semiannual", "annual"),
            "Support underwriting discipline and earnings quality.",
            "Challenge reserve adequacy and cyclical accident-rate luck.",
        ),
    ),
}


def _line_contains_any(line: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in line for keyword in keywords)


def _extract_filing_evidence(
    report_texts: Iterable[tuple[str, str]],
    max_per_category: int = 3,
) -> list[FilingEvidence]:
    seen: set[tuple[str, str]] = set()
    evidence_by_category: dict[str, list[FilingEvidence]] = {}

    for title, text in report_texts:
        for raw_line in str(text or "").splitlines():
            line = _compact_text(raw_line, limit=240)
            if not line:
                continue
            for category, keywords, bull_use, bear_use in _FILING_SIGNAL_RULES:
                if not _line_contains_any(line, keywords):
                    continue
                key = (category, line)
                if key in seen:
                    continue
                seen.add(key)
                evidence_by_category.setdefault(category, []).append(
                    FilingEvidence(
                        category=category,
                        signal="/".join(keyword for keyword in keywords if keyword in line)[:80],
                        evidence=f"{title}: {line}",
                        bull_use=bull_use,
                        bear_use=bear_use,
                    )
                )

    rows: list[FilingEvidence] = []
    for category, *_ in _FILING_SIGNAL_RULES:
        rows.extend(evidence_by_category.get(category, [])[:max_per_category])
    return rows


def _detect_report_type(title: str) -> str:
    if any(token in title for token in ("一季度", "三季度", "季度", "季报")):
        return "quarterly"
    if any(token in title for token in ("半年度", "半年报", "中期")):
        return "semiannual"
    if any(token in title for token in ("年度", "年报")):
        return "annual"
    return "unknown"


def _evidence_strength(text: str) -> str:
    if re.search(r"\d", text):
        return "quantified disclosure"
    if any(token in text for token in ("预计", "计划", "力争", "将", "拟")):
        return "management narrative"
    return "explicit disclosure"


def _select_industry_profile(
    company_name: str,
    industry: str,
    report_texts: Iterable[tuple[str, str]],
) -> str:
    blob = " ".join([company_name or "", industry or ""] + [text for _, text in report_texts])
    if any(token in blob for token in ("风电", "风机", "叶片", "海上风电")):
        return "wind_power_equipment"
    if any(token in blob for token in ("环卫", "环保", "垃圾焚烧", "环境服务")):
        return "environmental_services"
    if any(token in blob for token in ("锂电", "动力电池", "储能电池", "电解液", "隔膜", "负极材料", "正极材料")):
        return "lithium_battery"
    if any(token in blob for token in ("白酒", "批价", "经销商库存", "次高端", "高端酒")):
        return "baijiu"
    if (
        any(token in blob for token in ("航空运输", "航空客运", "客座率", "客公里收益", "旅客周转量"))
        and any(token in blob for token in ("航油", "机队", "航线", "ASK", "RPK"))
    ):
        return "airlines"
    if any(token in blob for token in ("保险", "新业务价值", "内含价值", "综合成本率", "继续率")):
        return "insurance"
    if any(token in blob for token in ("有色", "矿业", "矿山", "铜", "铝", "黄金", "稀土", "金属量")):
        return "metals_mining"
    if "银行" in blob:
        return "banking"
    if any(token in blob for token in ("航运", "海运", "船队", "TCE")):
        return "shipping"
    if any(token in blob for token in ("软件", "SaaS", "云收入", "订阅")):
        return "software_services"
    return "generic"


def _question_candidates(profile: str) -> tuple[FilingQuestion, ...]:
    return _GENERIC_QUESTIONS + _INDUSTRY_PLAYBOOKS.get(profile, ())


def _answer_questions(
    report_texts: Iterable[tuple[str, str]],
    questions: Iterable[FilingQuestion],
) -> list[FilingQuestionAnswer]:
    indexed_reports = list(report_texts)
    answers: list[FilingQuestionAnswer] = []

    for question in questions:
        best: tuple[int, FilingQuestionAnswer] | None = None
        for report_index, (title, text) in enumerate(indexed_reports):
            report_type = _detect_report_type(title)
            for raw_line in str(text or "").splitlines():
                line = _compact_text(raw_line, limit=240)
                if not line or not _line_contains_any(line, question.keywords):
                    continue
                strength = _evidence_strength(line)
                score = 0
                if report_type in question.preferred_report_types:
                    score += 3
                if strength == "quantified disclosure":
                    score += 2
                elif strength == "explicit disclosure":
                    score += 1
                score += max(0, 2 - report_index)
                answer = FilingQuestionAnswer(
                    question_id=question.question_id,
                    category=question.category,
                    question=question.question,
                    report_type=report_type,
                    evidence_strength=strength,
                    evidence=f"{title}: {line}",
                    bull_use=question.bull_use,
                    bear_use=question.bear_use,
                )
                if best is None or score > best[0]:
                    best = (score, answer)
        if best is not None:
            answers.append(best[1])
    return answers


def _question_memory_path(symbol: str) -> Path:
    root = Path(get_config()["data_cache_dir"]).expanduser()
    path = root / "filing_question_memory"
    path.mkdir(parents=True, exist_ok=True)
    return path / f"{symbol}.json"


def _load_question_memory(symbol: str) -> dict:
    path = _question_memory_path(symbol)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _update_question_memory(
    symbol: str,
    curr_date: str,
    profile: str,
    answers: Iterable[FilingQuestionAnswer],
) -> dict:
    memory = _load_question_memory(symbol)
    memory.setdefault("profile", profile)
    memory.setdefault("questions", {})
    for answer in answers:
        item = memory["questions"].setdefault(
            answer.question_id,
            {
                "question": answer.question,
                "category": answer.category,
                "times_seen": 0,
            },
        )
        item["times_seen"] += 1
        item["last_seen_date"] = curr_date
        item["last_report_type"] = answer.report_type
        item["last_evidence"] = answer.evidence
    _question_memory_path(symbol).write_text(
        json.dumps(memory, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return memory


def _memory_rows(memory: dict, limit: int = 8) -> list[dict[str, str]]:
    questions = list(memory.get("questions", {}).items())
    questions.sort(
        key=lambda item: (
            item[1].get("times_seen", 0),
            item[1].get("last_seen_date", ""),
        ),
        reverse=True,
    )
    rows = []
    for question_id, payload in questions[:limit]:
        rows.append(
            {
                "question_id": question_id,
                "question": payload.get("question", ""),
                "times_seen": str(payload.get("times_seen", 0)),
                "last_seen": payload.get("last_seen_date", ""),
                "last_report_type": payload.get("last_report_type", ""),
            }
        )
    return rows


def _build_table(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "No filing-derived evidence snippets found."
    return _markdown_table(pd.DataFrame(rows))


def get_financial_report_intelligence_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 900,
) -> str:
    """Extract question-driven operating evidence from A-share financial reports."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Financial-report intelligence expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    basic = _fetch_stock_basic(symbol)
    company_name = _format_value(basic.get("name")) if basic is not None else symbol
    industry = _format_value(basic.get("industry")) if basic is not None else ""
    reports, report_texts = _load_financial_report_texts(symbol, curr_date, look_back_days)
    evidence = _extract_filing_evidence(report_texts)
    profile = _select_industry_profile(company_name, industry, report_texts)
    questions = _question_candidates(profile)
    answers = _answer_questions(report_texts, questions)
    memory = _update_question_memory(symbol, curr_date, profile, answers)

    report_titles = []
    if isinstance(reports, TushareDataError):
        report_titles.append(f"Financial report lookup unavailable: {reports}")
    elif reports is None or reports.empty:
        report_titles.append("No recent quarterly/half-year/annual report announcements found.")
    else:
        for _, row in reports.iterrows():
            report_titles.append(
                f"- {row.get('ann_date', 'N/A')}: {row.get('title', 'N/A')}"
            )

    question_rows = [
        {
            "question_id": answer.question_id,
            "report_type": answer.report_type,
            "question": answer.question,
            "evidence_strength": answer.evidence_strength,
            "filing_answer": _compact_text(answer.evidence, 160),
            "bull_use": answer.bull_use,
            "bear_use": answer.bear_use,
        }
        for answer in answers
    ]
    evidence_rows = [
        {
            "category": item.category,
            "signal": item.signal,
            "filing_evidence": _compact_text(item.evidence, 150),
            "bull_use": item.bull_use,
            "bear_use": item.bear_use,
        }
        for item in evidence
    ]

    extraction_note = (
        "Financial-report text extraction succeeded."
        if report_texts
        else "Financial-report text extraction unavailable or no readable report text was retrieved."
    )

    lines = [
        f"# Financial-report intelligence for {symbol} as of {curr_date}",
        "",
        f"- Company: {company_name}",
        f"- Vendor industry: {industry}",
        f"- Reading profile: {profile}",
        f"- Financial-report look-back: {look_back_days} days",
        f"- Extraction status: {extraction_note}",
        "",
        "## Financial Reports Considered",
        *report_titles,
        "",
        "## Selected Filing Question Playbook",
        _build_table(
            [
                {
                    "question_id": question.question_id,
                    "category": question.category,
                    "question": question.question,
                    "preferred_reports": "/".join(question.preferred_report_types),
                }
                for question in questions
            ]
        ),
        "",
        "## Question-Driven Filing Answers",
        _build_table(question_rows),
        "",
        "## Company-Specific Watch Questions",
        _build_table(_memory_rows(memory)),
        "",
        "## Filing-Derived Operating Evidence",
        _build_table(evidence_rows),
        "",
        "## Analyst Instructions",
        "- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.",
        "- Start from the selected question playbook, then answer only with evidence actually found in filings.",
        "- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.",
        "- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.",
        "- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.",
    ]
    return "\n".join(lines)
