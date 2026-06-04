from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Iterable

import pandas as pd

from .config import get_config
from .industry_classifier import is_banking_entity
from .tushare_a_stock import (
    TushareDataError,
    _derive_financial_metrics,
    _fetch_balance_sheet_data,
    _fetch_cashflow_data,
    _fetch_fina_indicator,
    _fetch_income_statement_data,
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


@dataclass(frozen=True)
class MaterialFilingFinding:
    finding_type: str
    importance: str
    evidence: str
    investment_read: str
    bull_use: str
    bear_use: str


@dataclass(frozen=True)
class BusinessModelFinding:
    lens: str
    report_type: str
    evidence: str
    why_it_matters: str


@dataclass(frozen=True)
class GrowthVectorFinding:
    vector: str
    stage: str
    evidence: str
    valuation_treatment: str
    verification_need: str


@dataclass(frozen=True)
class ReportBridgeFinding:
    topic: str
    long_cycle_evidence: str
    checkpoint_evidence: str
    bridge_status: str
    bridge_read: str
    analyst_read: str


@dataclass(frozen=True)
class FilingExcerpt:
    report_type: str
    section: str
    excerpt: str
    reading_purpose: str


@dataclass(frozen=True)
class FilingParagraphInsight:
    lens: str
    report_type: str
    section: str
    excerpt: str
    reading_question: str
    why_it_matters: str


@dataclass(frozen=True)
class IndustryReadingInsight:
    lens: str
    report_type: str
    section: str
    excerpt: str
    reading_question: str
    why_it_matters: str
    connect_to: str


@dataclass(frozen=True)
class FilingCoverageAudit:
    coverage_grade: str
    report_types_seen: tuple[str, ...]
    missing_report_types: tuple[str, ...]
    answered_question_count: int
    total_question_count: int
    core_pack_status: str
    confidence_read: str


@dataclass(frozen=True)
class CoreDiscussionItem:
    topic: str
    priority: str
    evidence_basis: str
    why_it_matters: str
    valuation_treatment: str
    verification_need: str


@dataclass(frozen=True)
class FilingTableSignal:
    account: str
    report_type: str
    evidence: str
    why_it_matters: str
    bull_use: str
    bear_use: str


@dataclass(frozen=True)
class SegmentEconomicsFinding:
    segment_type: str
    report_type: str
    evidence: str
    analyst_use: str


@dataclass(frozen=True)
class BusinessSegmentValuationFinding:
    business_bucket: str
    report_type: str
    evidence: str
    valuation_anchor: str
    analyst_use: str
    verification_need: str


@dataclass(frozen=True)
class FilingNoteFinding:
    note_type: str
    importance: str
    evidence: str
    why_it_matters: str
    bull_use: str
    bear_use: str


@dataclass(frozen=True)
class FinancialRelationInsight:
    relation_type: str
    importance: str
    evidence: str
    investment_read: str
    bull_use: str
    bear_use: str


@dataclass(frozen=True)
class FilingInsight:
    insight_type: str
    analyst_question: str
    distilled_read: str
    evidence_basis: str
    debate_use: str
    what_would_change_mind: str


@dataclass(frozen=True)
class FilingInternalQualityModule:
    module: str
    purpose: str
    evidence: str
    analyst_use: str
    missing_or_next_check: str


@dataclass(frozen=True)
class FilingTextSignal:
    signal_type: str
    report_type: str
    wording_stage: str
    evidence: str
    investment_read: str
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

_BANKING_SIGNAL_RULES: tuple[tuple[str, tuple[str, ...], str, str], ...] = (
    (
        "bank_spread",
        ("净息差", "净利差", "净利息收益率", "生息资产", "贷款收益率", "存款成本率"),
        "Use spread stabilization, funding advantage, and asset-yield resilience to support bank earnings quality.",
        "Challenge whether volume growth is masking spread compression or higher funding costs.",
    ),
    (
        "bank_asset_quality",
        ("不良贷款率", "不良贷款", "关注类贷款", "逾期贷款", "迁徙率", "拨备覆盖率", "贷款拨备率", "信用成本"),
        "Use clean asset-quality metrics and reserve coverage to support lower credit-cost risk.",
        "Stress early-warning loans, overdue migration, credit cost, and reserve erosion before headline NPLs move.",
    ),
    (
        "bank_capital",
        ("核心一级资本充足率", "一级资本充足率", "资本充足率", "风险加权资产", "内生资本", "分红"),
        "Use capital adequacy and payout discipline to support shareholder-return durability.",
        "Challenge growth or dividend claims if RWA growth consumes capital faster than earnings replenish it.",
    ),
    (
        "bank_retail_wealth",
        ("管理零售客户总资产", "AUM", "财富管理", "手续费", "佣金", "代理基金", "托管规模", "零售客户"),
        "Use wealth-management monetization and retail franchise scale to support fee resilience.",
        "Test whether AUM growth is translating into fee income or being offset by fee-rate compression.",
    ),
    (
        "bank_balance_sheet_mix",
        ("客户贷款", "客户存款", "活期存款", "零售贷款", "公司贷款", "房地产贷款", "信用卡贷款", "消费贷款"),
        "Use loan/deposit mix to connect franchise quality to NIM and asset-quality outcomes.",
        "Challenge retail-bank quality if weak mortgage, credit-card, or consumer-loan data undermine the core engine.",
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
    "smart_grid_automation": (
        FilingQuestion(
            "grid_order_visibility",
            "orders",
            "\u7535\u7f51\u81ea\u52a8\u5316\u3001\u7ee7\u7535\u4fdd\u62a4\u3001\u8c03\u5ea6\u3001\u914d\u7535\u548c\u67d4\u6027\u8f93\u7535\u8ba2\u5355\u662f\u5426\u8f6c\u5316\u4e3a\u6536\u5165\u548c\u5408\u540c\u8d1f\u503a\uff1f",
            ("\u7535\u7f51\u81ea\u52a8\u5316", "\u7ee7\u7535\u4fdd\u62a4", "\u8c03\u5ea6", "\u914d\u7535", "\u67d4\u6027\u8f93\u7535", "\u5408\u540c\u8d1f\u503a", "\u8ba2\u5355", "\u4e2d\u6807"),
            ("quarterly", "semiannual", "annual"),
            "Support demand visibility when grid capex, orders, and revenue conversion are aligned.",
            "Challenge whether policy demand is already priced or delayed by project acceptance and collection.",
        ),
        FilingQuestion(
            "grid_segment_margin",
            "segment_margin",
            "\u7535\u7f51\u4e8c\u6b21\u8bbe\u5907\u3001\u7535\u529b\u4fe1\u606f\u901a\u4fe1\u3001\u65b0\u80fd\u6e90\u53ca\u6d77\u5916\u4e1a\u52a1\u7684\u6536\u5165\u3001\u6bdb\u5229\u7387\u548c\u51c0\u5229\u7387\u6709\u4f55\u5dee\u5f02\uff1f",
            ("\u4e8c\u6b21\u8bbe\u5907", "\u7535\u529b\u4fe1\u606f\u901a\u4fe1", "\u65b0\u80fd\u6e90", "\u6d77\u5916", "\u8425\u4e1a\u6536\u5165", "\u6bdb\u5229\u7387", "\u51c0\u5229\u7387"),
            ("semiannual", "annual"),
            "Build a split valuation around disclosed revenue, margin, and growth by business line.",
            "Avoid giving equal multiple credit to lower-margin or unproven adjacent businesses.",
        ),
        FilingQuestion(
            "grid_cash_conversion",
            "cash_quality",
            "\u56fd\u7f51\u3001\u5357\u7f51\u548c\u884c\u4e1a\u5ba2\u6237\u7684\u56de\u6b3e\u662f\u5426\u652f\u6491\u5229\u6da6\u8d28\u91cf\uff1f",
            ("\u56fd\u5bb6\u7535\u7f51", "\u5357\u65b9\u7535\u7f51", "\u5e94\u6536\u8d26\u6b3e", "\u5408\u540c\u8d44\u4ea7", "\u7ecf\u8425\u6d3b\u52a8\u73b0\u91d1\u6d41", "\u56de\u6b3e"),
            ("quarterly", "semiannual", "annual"),
            "Validate earnings quality when profit converts into cash despite project cycles.",
            "Stress collection, acceptance timing, and working-capital absorption.",
        ),
        FilingQuestion(
            "grid_second_curve",
            "new_business",
            "\u50a8\u80fd\u3001IGBT\u3001\u7535\u529b\u673a\u5668\u4eba\u3001\u6d77\u5916PCS\u7b49\u65b0\u4e1a\u52a1\u662f\u5426\u5df2\u6709\u5206\u90e8\u6536\u5165\u3001\u6bdb\u5229\u7387\u3001\u8ba2\u5355\u6216\u5ba2\u6237\u8bc1\u636e\uff1f",
            ("\u50a8\u80fd", "IGBT", "\u7535\u529b\u673a\u5668\u4eba", "PCS", "\u6d77\u5916", "\u5ba2\u6237", "\u8ba2\u5355", "\u6bdb\u5229\u7387", "\u8425\u4e1a\u6536\u5165"),
            ("semiannual", "annual"),
            "Treat monetized new businesses as scenario or SOTP upside when disclosure is specific.",
            "Keep concept-only second curves out of base valuation until segment economics are disclosed.",
        ),
    ),
    "power_operator": (
        FilingQuestion(
            "power_generation_mix",
            "mix",
            "\u88c5\u673a\u7ed3\u6784\u3001\u53d1\u7535\u91cf\u3001\u7eff\u7535\u4ea4\u6613\u548c\u8f85\u52a9\u670d\u52a1\u6536\u5165\uff0c\u8c01\u5728\u771f\u6b63\u6539\u5584\u5229\u6da6\u7ed3\u6784\uff1f",
            ("\u88c5\u673a", "\u53d1\u7535\u91cf", "\u7eff\u7535", "\u7eff\u8bc1", "\u8f85\u52a9\u670d\u52a1", "\u865a\u62df\u7535\u5382"),
            ("quarterly", "semiannual", "annual"),
            "Support earnings quality when operating mix and monetization both improve.",
            "Question whether narrative growth is outrunning disclosed revenue contribution.",
        ),
        FilingQuestion(
            "power_cash_and_leverage",
            "cash_quality",
            "\u5229\u6da6\u6539\u5584\u662f\u5426\u80fd\u8986\u76d6\u8d44\u672c\u5f00\u652f\u3001\u8d22\u52a1\u8d39\u7528\u548c\u56de\u6b3e\u538b\u529b\uff1f",
            ("\u7ecf\u8425\u6d3b\u52a8\u73b0\u91d1\u6d41", "\u8d44\u672c\u5f00\u652f", "\u8d22\u52a1\u8d39\u7528", "\u5e94\u6536\u8d26\u6b3e", "\u501f\u6b3e"),
            ("quarterly", "semiannual", "annual"),
            "Validate utility-style cash conversion and balance-sheet resilience.",
            "Stress leverage, receivables, and project IRR deterioration.",
        ),
    ),
    "precision_equipment": (
        FilingQuestion(
            "equipment_orders",
            "orders",
            "\u65b0\u589e\u8ba2\u5355\u3001\u5728\u624b\u8ba2\u5355\u3001\u5408\u540c\u8d1f\u503a\u4e0e\u6536\u5165\u786e\u8ba4\u662f\u5426\u540c\u5411\uff1f",
            ("\u65b0\u589e\u8ba2\u5355", "\u5728\u624b\u8ba2\u5355", "\u5408\u540c\u8d1f\u503a", "\u9a8c\u6536", "\u6536\u5165\u786e\u8ba4"),
            ("quarterly", "semiannual", "annual"),
            "Support demand visibility and shipment conversion.",
            "Challenge whether revenue is running ahead of durable order intake.",
        ),
        FilingQuestion(
            "equipment_mix",
            "mix",
            "\u9ad8\u6bdb\u5229\u65b0\u54c1\u7c7b\u662f\u5426\u5df2\u5f62\u6210\u53ef\u5355\u72ec\u9a8c\u8bc1\u7684\u6536\u5165\u4e0e\u6bdb\u5229\u8d21\u732e\uff1f",
            ("\u534a\u5bfc\u4f53", "\u663e\u793a", "\u6bdb\u5229\u7387", "\u5206\u4e1a\u52a1", "\u8425\u4e1a\u6536\u5165"),
            ("semiannual", "annual"),
            "Show genuine mix upgrade when new lines are separately monetized.",
            "Keep optionality out of core valuation until segment economics are disclosed.",
        ),
    ),
    "industrial_components": (
        FilingQuestion(
            "industrial_order_cash",
            "orders",
            "\u8ba2\u5355\u3001\u5408\u540c\u8d1f\u503a\u548c\u7ecf\u8425\u73b0\u91d1\u6d41\u662f\u5426\u540c\u6b65\u6539\u5584\uff0c\u8fd8\u662f\u53ea\u662f\u4ee5\u57ab\u8d44\u6362\u6536\u5165\uff1f",
            ("\u8ba2\u5355", "\u5408\u540c\u8d1f\u503a", "\u7ecf\u8425\u73b0\u91d1\u6d41", "\u5e94\u6536\u8d26\u6b3e", "\u9884\u4ed8\u6b3e\u9879"),
            ("quarterly", "semiannual", "annual"),
            "Support demand visibility only when orders convert into cash.",
            "Challenge apparent order growth if receivables, inventory, or prepayments absorb cash.",
        ),
        FilingQuestion(
            "industrial_margin_mix",
            "pricing",
            "\u4ea7\u54c1\u7ed3\u6784\u3001\u9879\u76ee\u7ed3\u6784\u6216\u6d77\u5916\u8ba2\u5355\u662f\u5426\u771f\u6b63\u63d0\u5347\u6bdb\u5229\u7387\u4e0e\u51c0\u5229\u7387\uff1f",
            ("\u6bdb\u5229\u7387", "\u6d77\u5916", "\u9879\u76ee", "\u4ea7\u54c1\u7ed3\u6784", "\u51c0\u5229\u7387", "\u9500\u552e\u5355\u4ef7"),
            ("quarterly", "semiannual", "annual"),
            "Support operating leverage and mix upgrade.",
            "Expose low-margin growth or one-off project revenue.",
        ),
        FilingQuestion(
            "industrial_capex_returns",
            "capital_allocation",
            "\u5728\u5efa\u5de5\u7a0b\u3001\u65b0\u57fa\u5730\u6216\u5b50\u516c\u53f8\u6269\u5f20\u662f\u5426\u6709\u660e\u786e\u4ea7\u80fd\u91ca\u653e\u4e0e\u56de\u62a5\u8def\u5f84\uff1f",
            ("\u5728\u5efa\u5de5\u7a0b", "\u57fa\u5730", "\u5b50\u516c\u53f8", "\u8fbe\u4ea7", "\u4ea7\u80fd", "\u6295\u8d44"),
            ("semiannual", "annual"),
            "Treat capex as value-accretive only when utilization and returns are visible.",
            "Question whether heavy assets are trapping capital without improving ROIC.",
        ),
        FilingQuestion(
            "industrial_end_market",
            "customer",
            "\u4e0b\u6e38\u5ba2\u6237\u548c\u5e94\u7528\u573a\u666f\u7684\u53d8\u5316\u662f\u7ed3\u6784\u6027\u9700\u6c42\uff0c\u8fd8\u662f\u6982\u5ff5\u6620\u5c04\uff1f",
            ("\u5ba2\u6237", "\u6d77\u6d0b\u5de5\u7a0b", "\u822a\u5929", "\u6e2f\u53e3", "\u9020\u8239", "\u7535\u529b", "\u4f53\u80b2\u573a\u9986"),
            ("semiannual", "annual"),
            "Connect end-market exposure to real orders and margin.",
            "Keep adjacent narratives out of valuation until revenue contribution is disclosed.",
        ),
    ),
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
    "livestock_hog": (
        FilingQuestion(
            "hog_cycle",
            "pricing",
            "生猪价格、仔猪价格、完全成本和猪粮比是否共同指向周期改善？",
            ("生猪价格", "仔猪价格", "完全成本", "猪粮比", "养殖成本"),
            ("quarterly", "semiannual", "annual"),
            "Use realized pricing and cost spread to judge cycle position.",
            "Challenge margin optimism if price recovery is not beating cost.",
        ),
        FilingQuestion(
            "hog_breeding_base",
            "capacity",
            "能繁母猪、PSY、仔猪和出栏量是否显示公司在扩张、收缩还是提效？",
            ("能繁母猪", "PSY", "仔猪", "出栏量", "种猪"),
            ("quarterly", "semiannual", "annual"),
            "Support durable supply advantage when breeding productivity improves.",
            "Test whether volume growth comes from biological efficiency or simple herd expansion.",
        ),
        FilingQuestion(
            "hog_slaughter_mix",
            "mix",
            "屠宰和肉食业务是在抬升利润池，还是仍只是规模补充？",
            ("屠宰", "肉食", "屠宰量", "鲜品", "冻品"),
            ("semiannual", "annual"),
            "Identify whether downstream integration is becoming a real second curve.",
            "Keep adjacent businesses out of core valuation until margins and utilization are disclosed.",
        ),
        FilingQuestion(
            "hog_hedging",
            "risk",
            "期货套保、饲料采购和库存安排是在平滑利润，还是在放大周期判断风险？",
            ("期货", "套期保值", "饲料", "原料采购", "库存"),
            ("quarterly", "semiannual", "annual"),
            "Recognize prudent cycle management when disclosure supports it.",
            "Stress mark-to-market, basis, and procurement timing risk.",
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
        FilingQuestion(
            "bank_capital",
            "capital",
            "资本充足率、核心一级资本和风险加权资产是否支持扩表与分红？",
            ("资本充足率", "核心一级资本充足率", "一级资本充足率", "风险加权资产", "分红"),
            ("quarterly", "semiannual", "annual"),
            "Support growth and payout durability when capital is replenished internally.",
            "Challenge expansion or dividend claims if RWA growth consumes capital.",
        ),
        FilingQuestion(
            "bank_retail_book",
            "loan_deposit_mix",
            "零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？",
            ("零售贷款", "客户存款", "活期存款", "管理零售客户总资产", "AUM", "信用卡"),
            ("quarterly", "semiannual", "annual"),
            "Support the retail-bank moat when deposit and AUM growth remain healthy.",
            "Challenge the moat if retail loan demand or deposit quality deteriorates.",
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
    "medical_device": (
        FilingQuestion(
            "device_installed_base",
            "installed_base",
            "Installed base, replacement cycle, tender cadence, and delivery/acceptance must support equipment-cycle claims.",
            (
                "\u88c5\u673a",
                "\u8bbe\u5907\u66f4\u65b0",
                "\u62db\u6295\u6807",
                "\u91c7\u8d2d",
                "\u4ea4\u4ed8",
                "\u9a8c\u6536",
                "\u76d1\u62a4\u4eea",
                "\u9ebb\u9189\u673a",
                "\u8d85\u58f0",
                "\u5f71\u50cf\u8bbe\u5907",
            ),
            ("quarterly", "semiannual", "annual"),
            "Support the equipment cycle when installed base and tender evidence convert into accepted revenue.",
            "Challenge equipment optimism if procurement, delivery, or acceptance evidence is weak.",
        ),
        FilingQuestion(
            "device_ivd_reagent",
            "recurring_revenue",
            "IVD analyzer installed base should convert into reagent/consumable pull-through, not just one-off equipment sales.",
            (
                "\u4f53\u5916\u8bca\u65ad",
                "\u8bca\u65ad\u8bd5\u5242",
                "\u8bd5\u5242",
                "\u8017\u6750",
                "\u68c0\u9a8c\u8bbe\u5907",
                "\u6d41\u6c34\u7ebf",
                "IVD",
            ),
            ("quarterly", "semiannual", "annual"),
            "Support recurring revenue and margin durability when reagent pull-through is disclosed.",
            "Question recurring-quality claims if analyzer placement lacks reagent volume or menu evidence.",
        ),
        FilingQuestion(
            "device_vbp_policy",
            "policy_pricing",
            "VBP, centralized procurement, and equipment-renewal policy must be translated into price, volume, and margin impact.",
            (
                "\u96c6\u91c7",
                "\u5e26\u91cf\u91c7\u8d2d",
                "\u8bbe\u5907\u66f4\u65b0",
                "\u8d34\u606f\u8d37\u6b3e",
                "\u533b\u7597\u65b0\u57fa\u5efa",
                "\u56fd\u4ea7\u66ff\u4ee3",
            ),
            ("quarterly", "semiannual", "annual"),
            "Support demand or share gains when policy transmission is company-specific.",
            "Challenge if policy only expands the industry while pricing pressure erodes economics.",
        ),
        FilingQuestion(
            "device_overseas_registration",
            "overseas",
            "Overseas growth requires registration, distributor quality, localization, service network, and channel-inventory evidence.",
            (
                "\u6d77\u5916",
                "\u51fa\u6d77",
                "\u6ce8\u518c\u8bc1",
                "\u6e20\u9053",
                "\u7ecf\u9500\u5546",
                "FDA",
                "CE",
                "NMPA",
            ),
            ("semiannual", "annual"),
            "Support overseas optionality when registration and sell-through evidence exist.",
            "Challenge shipment-led growth if channel inventory or local service quality is unclear.",
        ),
        FilingQuestion(
            "device_cash_quality",
            "cash_quality",
            "Receivables, inventory, distributor credit, and operating cash flow must confirm profit quality.",
            (
                "\u5e94\u6536\u8d26\u6b3e",
                "\u5b58\u8d27",
                "\u7ecf\u8425\u6027\u73b0\u91d1\u6d41",
                "\u73b0\u91d1\u6d41",
                "\u7ecf\u9500\u5546",
            ),
            ("quarterly", "semiannual", "annual"),
            "Validate high-quality growth when profit converts into cash.",
            "Expose channel stuffing, collection risk, or inventory pressure.",
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
    "smart_mobility": (
        FilingQuestion(
            "mobility_product_mix",
            "mix",
            "电动两轮车、滑板车、全地形车、割草机器人、服务机器人等产品线，谁在贡献收入和毛利？",
            ("电动两轮车", "电动滑板车", "全地形车", "ATV", "割草机器人", "服务机器人", "分产品", "毛利率"),
            ("semiannual", "annual"),
            "Support a split valuation only when product-line revenue, margin, growth, or cash conversion is disclosed.",
            "Challenge blended valuation if different product lines have different growth, margin, inventory, or channel economics.",
        ),
        FilingQuestion(
            "mobility_channel_inventory",
            "channel_inventory",
            "渠道订单、合同负债、库存和终端动销是否同步，还是存在压货和降价风险？",
            ("合同负债", "预收款项", "库存", "存货", "经销商", "渠道", "动销", "周转"),
            ("quarterly", "semiannual", "annual"),
            "Use synchronized contract liabilities, sell-through, and controlled inventory to validate demand.",
            "Attack the thesis if inventory grows faster than sell-through or contract liabilities become stale channel pressure.",
        ),
        FilingQuestion(
            "mobility_overseas_fx",
            "overseas_fx",
            "海外收入、汇率套保、关税和地区结构是否改善利润质量，还是放大利润波动？",
            ("海外", "境外", "东南亚", "越南", "汇兑", "套期保值", "关税", "Segway"),
            ("quarterly", "semiannual", "annual"),
            "Support global growth when overseas revenue converts into stable margin and cash after FX.",
            "Stress FX losses, tariff exposure, regional execution, and whether overseas growth is lower-quality revenue.",
        ),
        FilingQuestion(
            "mobility_software_services",
            "recurring_revenue",
            "软件服务费、APP服务、订阅或增值服务是否已经形成可单独估值的经常性收入？",
            ("软件服务费", "APP", "增值服务", "订阅", "服务费", "用户", "续费", "毛利率"),
            ("quarterly", "semiannual", "annual"),
            "Upgrade recurring revenue only when filings disclose scale, margin, user base, renewal, or retention.",
            "Keep software optionality out of base-case valuation if it is only an interaction disclosure or below materiality.",
        ),
        FilingQuestion(
            "mobility_new_category",
            "new_business",
            "新品类和第二增长曲线已经商业化，还是仍停留在产品规划和品牌叙事？",
            ("新产品", "新品类", "割草机器人", "全地形车", "E-bike", "电切油", "油转电", "投产", "产能"),
            ("semiannual", "annual"),
            "Use monetized new categories as scenario/SOTP upside with explicit evidence gates.",
            "Challenge new-category optimism when revenue, margin, orders, channels, or cash conversion are missing.",
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
    rules: tuple[tuple[str, tuple[str, ...], str, str], ...] = _FILING_SIGNAL_RULES,
) -> list[FilingEvidence]:
    seen: set[tuple[str, str]] = set()
    evidence_by_category: dict[str, list[FilingEvidence]] = {}

    for title, text in report_texts:
        for raw_line in str(text or "").splitlines():
            line = _compact_text(raw_line, limit=240)
            if not line:
                continue
            for category, keywords, bull_use, bear_use in rules:
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
    for category, *_ in rules:
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


def _repair_mojibake(value: str) -> str:
    text = str(value or "")
    try:
        return text.encode("latin1").decode("utf-8")
    except UnicodeError:
        return text


def _select_industry_profile(
    company_name: str,
    industry: str,
    report_texts: Iterable[tuple[str, str]],
) -> str:
    normalized_parts = [_repair_mojibake(company_name), _repair_mojibake(industry)]
    normalized_parts.extend(_repair_mojibake(text) for _, text in report_texts)
    blob = " ".join(normalized_parts)
    identity_blob = f"{normalized_parts[0]} {normalized_parts[1]}"
    if any(token in identity_blob for token in ("\u4fdd\u9669", "\u5bff\u9669", "\u8d22\u9669", "\u4ea7\u9669")):
        return "insurance"
    medical_device_identity = any(
        token in identity_blob
        for token in (
            "\u8fc8\u745e\u533b\u7597",
            "\u8054\u5f71\u533b\u7597",
            "\u533b\u7597\u5668\u68b0",
            "\u533b\u7597\u8bbe\u5907",
            "\u533b\u7528\u8017\u6750",
            "\u4f53\u5916\u8bca\u65ad",
        )
    )
    medical_device_hits = sum(
        token in blob
        for token in (
            "\u533b\u7597\u5668\u68b0",
            "\u533b\u7597\u8bbe\u5907",
            "\u533b\u7528\u8017\u6750",
            "\u4f53\u5916\u8bca\u65ad",
            "\u8bca\u65ad\u8bd5\u5242",
            "\u76d1\u62a4\u4eea",
            "\u9ebb\u9189\u673a",
            "\u8d85\u58f0",
            "\u5185\u7aa5\u955c",
            "\u5f71\u50cf\u8bbe\u5907",
            "\u88c5\u673a",
            "\u6ce8\u518c\u8bc1",
            "\u96c6\u91c7",
            "\u8bbe\u5907\u66f4\u65b0",
            "IVD",
        )
    )
    if medical_device_identity or medical_device_hits >= 3:
        return "medical_device"
    if any(token in identity_blob for token in ("银行", "商业银行", "股份制银行")):
        return "banking"
    if any(
        token in blob
        for token in (
            "净息差",
            "净利息收益率",
            "不良贷款率",
            "拨备覆盖率",
            "核心一级资本充足率",
        )
    ) and "银行" in blob:
        return "banking"
    smart_grid_identity = any(
        token in identity_blob
        for token in (
            "\u56fd\u7535\u5357\u745e",
            "\u5357\u745e",
            "\u7535\u7f51\u81ea\u52a8\u5316",
            "\u7535\u529b\u81ea\u52a8\u5316",
            "\u7ee7\u7535\u4fdd\u62a4",
            "\u667a\u80fd\u7535\u7f51",
            "\u7535\u529b\u4e8c\u6b21\u8bbe\u5907",
        )
    )
    smart_grid_hits = sum(
        token in blob
        for token in (
            "\u7535\u7f51\u81ea\u52a8\u5316",
            "\u7535\u529b\u81ea\u52a8\u5316",
            "\u8c03\u5ea6\u81ea\u52a8\u5316",
            "\u7535\u7f51\u8c03\u5ea6",
            "\u7ee7\u7535\u4fdd\u62a4",
            "\u53d8\u7535\u7ad9\u81ea\u52a8\u5316",
            "\u914d\u7535\u81ea\u52a8\u5316",
            "\u67d4\u6027\u8f93\u7535",
            "\u7535\u529b\u4fe1\u606f\u901a\u4fe1",
            "\u65b0\u578b\u7535\u529b\u7cfb\u7edf",
            "\u56fd\u5bb6\u7535\u7f51",
            "\u5357\u65b9\u7535\u7f51",
            "\u667a\u80fd\u7535\u7f51",
            "\u7535\u7f51\u5b89\u5168\u7a33\u5b9a\u63a7\u5236",
            "\u7535\u7f51\u6570\u5b57\u5316",
        )
    )
    smart_grid_core_hits = sum(
        token in blob
        for token in (
            "\u7535\u7f51\u81ea\u52a8\u5316",
            "\u7535\u529b\u81ea\u52a8\u5316",
            "\u8c03\u5ea6\u81ea\u52a8\u5316",
            "\u7535\u7f51\u8c03\u5ea6",
            "\u7ee7\u7535\u4fdd\u62a4",
            "\u53d8\u7535\u7ad9\u81ea\u52a8\u5316",
            "\u914d\u7535\u81ea\u52a8\u5316",
            "\u67d4\u6027\u8f93\u7535",
            "\u7535\u529b\u4fe1\u606f\u901a\u4fe1",
            "\u7535\u7f51\u5b89\u5168\u7a33\u5b9a\u63a7\u5236",
            "\u7535\u7f51\u6570\u5b57\u5316",
        )
    )
    if smart_grid_identity or (smart_grid_core_hits >= 1 and smart_grid_hits >= 2):
        return "smart_grid_automation"
    if any(token in identity_blob for token in ("\u65b0\u578b\u7535\u529b", "\u7efc\u5408\u80fd\u6e90", "\u7535\u529b")):
        return "power_operator"
    smart_mobility_identity = any(
        token in identity_blob
        for token in (
            "九号",
            "Ninebot",
            "Segway",
            "摩托车",
            "电动两轮车",
            "两轮车",
            "智能出行",
        )
    )
    smart_mobility_hits = sum(
        token in blob
        for token in (
            "电动两轮车",
            "电动滑板车",
            "电动平衡车",
            "智能短交通",
            "全地形车",
            "ATV",
            "割草机器人",
            "服务机器人",
            "Ninebot",
            "Segway",
            "E-bike",
            "电切油",
            "油转电",
            "软件服务费",
            "APP软件服务费",
        )
    )
    if smart_mobility_identity and smart_mobility_hits >= 2:
        return "smart_mobility"
    industrial_identity = any(
        token in identity_blob
        for token in (
            "\u673a\u68b0\u57fa\u4ef6",
            "\u7d22\u5177",
            "\u540a\u88c5",
            "\u94a2\u4e1d\u7ef3",
            "\u94fe\u6761",
            "\u7d27\u56fa\u4ef6",
            "\u8f74\u627f",
            "\u6db2\u538b",
            "\u5de5\u4e1a\u96f6\u90e8\u4ef6",
        )
    )
    wind_hits = sum(token in blob for token in ("\u98ce\u7535", "\u98ce\u673a", "\u98ce\u7535\u673a\u7ec4", "\u53f6\u7247", "\u6d77\u4e0a\u98ce\u7535", "\u6574\u673a"))
    wind_identity = any(token in identity_blob for token in ("\u98ce\u7535", "\u98ce\u673a", "\u98ce\u7535\u8bbe\u5907"))
    if wind_identity or (not industrial_identity and wind_hits >= 3):
        return "wind_power_equipment"
    if industrial_identity:
        return "industrial_components"
    hog_hits = sum(
        token in blob
        for token in ("生猪", "养猪", "猪肉", "仔猪", "种猪", "能繁母猪", "PSY", "出栏")
    )
    if any(token in identity_blob for token in ("生猪", "养殖", "畜牧")) and hog_hits >= 1:
        return "livestock_hog"
    if hog_hits >= 3:
        return "livestock_hog"
    if any(token in identity_blob for token in ("\u4e13\u7528\u673a\u68b0", "\u8bbe\u5907")) and any(
        token in blob for token in ("\u592a\u9633\u80fd", "\u534a\u5bfc\u4f53", "\u663e\u793a", "\u771f\u7a7a", "\u6fc0\u5149")
    ):
        return "precision_equipment"
    # Resource / battery names often mention environmental compliance,
    # recycling, or ESG in filings. Those incidental words must not route a
    # lithium/mining company into the environmental-services playbook.
    lithium_hits = sum(
        token in blob
        for token in (
            "\u9502",
            "\u9502\u76d0",
            "\u78b3\u9178\u9502",
            "\u6c22\u6c27\u5316\u9502",
            "\u9502\u8f89\u77f3",
            "\u5364\u6c34\u63d0\u9502",
            "\u76d0\u6e56\u63d0\u9502",
            "\u9502\u7535",
            "\u52a8\u529b\u7535\u6c60",
            "\u50a8\u80fd\u7535\u6c60",
            "\u56fa\u6001\u7535\u6c60",
            "\u7535\u89e3\u6db2",
            "\u9694\u819c",
            "\u8d1f\u6781\u6750\u6599",
            "\u6b63\u6781\u6750\u6599",
        )
    )
    if any(
        token in identity_blob
        for token in (
            "\u9502",
            "\u8d63\u950b\u9502\u4e1a",
            "\u5929\u9f50\u9502\u4e1a",
            "\u76d0\u6e56\u80a1\u4efd",
        )
    ) or lithium_hits >= 2:
        return "lithium_battery"
    metals_hits = sum(
        token in blob
        for token in (
            "\u6709\u8272",
            "\u77ff\u4e1a",
            "\u77ff\u5c71",
            "\u77ff\u4ea7",
            "\u91c7\u9009",
            "\u54c1\u4f4d",
            "\u50a8\u91cf",
            "\u91d1\u5c5e\u91cf",
            "\u94dc",
            "\u94dd",
            "\u9ec4\u91d1",
            "\u7a00\u571f",
        )
    )
    if any(token in identity_blob for token in ("\u6709\u8272", "\u77ff\u4e1a", "\u77ff\u5c71", "\u5c0f\u91d1\u5c5e")) or metals_hits >= 2:
        return "metals_mining"
    if any(token in blob for token in ("\u73af\u536b", "\u73af\u4fdd", "\u5783\u573e\u711a\u70e7", "\u73af\u5883\u670d\u52a1")):
        return "environmental_services"
    if any(token in blob for token in ("\u9502\u7535", "\u52a8\u529b\u7535\u6c60", "\u50a8\u80fd\u7535\u6c60", "\u7535\u89e3\u6db2", "\u9694\u819c", "\u8d1f\u6781\u6750\u6599", "\u6b63\u6781\u6750\u6599")):
        return "lithium_battery"
    if any(token in blob for token in ("\u767d\u9152", "\u6279\u4ef7", "\u7ecf\u9500\u5546\u5e93\u5b58", "\u6b21\u9ad8\u7aef", "\u9ad8\u7aef\u9152")):
        return "baijiu"
    if (
        any(token in blob for token in ("\u822a\u7a7a\u8fd0\u8f93", "\u822a\u7a7a\u5ba2\u8fd0", "\u5ba2\u5ea7\u7387", "\u5ba2\u516c\u91cc\u6536\u76ca", "\u65c5\u5ba2\u5468\u8f6c\u91cf"))
        and any(token in blob for token in ("\u822a\u6cb9", "\u673a\u961f", "\u822a\u7ebf", "ASK", "RPK"))
    ):
        return "airlines"
    if any(token in blob for token in ("\u4fdd\u9669", "\u65b0\u4e1a\u52a1\u4ef7\u503c", "\u5185\u542b\u4ef7\u503c", "\u7efc\u5408\u6210\u672c\u7387", "\u7ee7\u7eed\u7387")):
        return "insurance"
    if any(
        token in blob
        for token in (
            "\u533b\u7597\u5668\u68b0",
            "\u533b\u7597\u8bbe\u5907",
            "\u533b\u7528\u8017\u6750",
            "\u4f53\u5916\u8bca\u65ad",
            "\u8bca\u65ad\u8bd5\u5242",
            "\u8bbe\u5907\u66f4\u65b0",
        )
    ):
        return "medical_device"
    if any(token in blob for token in ("\u6709\u8272", "\u77ff\u4e1a", "\u77ff\u5c71", "\u94dc", "\u94dd", "\u9ec4\u91d1", "\u7a00\u571f", "\u91d1\u5c5e\u91cf")):
        return "metals_mining"
    if "\u94f6\u884c" in blob:
        return "banking"
    if any(token in blob for token in ("\u822a\u8fd0", "\u6d77\u8fd0", "\u8239\u961f", "TCE")):
        return "shipping"
    if any(token in blob for token in ("\u8f6f\u4ef6", "SaaS", "\u4e91\u6536\u5165", "\u8ba2\u9605")):
        return "software_services"
    return "generic"


def _extract_material_filing_findings(
    report_texts: Iterable[tuple[str, str]],
) -> list[MaterialFilingFinding]:
    findings: list[MaterialFilingFinding] = []
    seen: set[tuple[str, str]] = set()

    patterns: tuple[
        tuple[str, str, tuple[str, ...], tuple[str, ...], str, str, str],
        ...
    ] = (
        (
            "compute-leasing-monetization",
            "high",
            (
                "\u7b97\u529b\u79df\u8d41",
                "\u667a\u4e91\u8ba1\u7b97",
                "\u667a\u7b97\u4e2d\u5fc3",
                "\u7b97\u529b\u4e2d\u5fc3",
                "\u6570\u636e\u4e2d\u5fc3",
                "AI\u6570\u636e\u670d\u52a1",
                "\u7f51\u7edc\u5de5\u7a0b",
            ),
            (
                "\u6536\u5165",
                "\u8425\u6536",
                "\u5229\u6da6",
                "\u6bdb\u5229",
                "\u8d44\u4ea7",
                "\u79df\u8d41\u4e1a\u52a1\u89c4\u6a21",
                "\u8ba2\u5355",
                "\u5ba2\u6237",
                "\u9879\u76ee",
                "\u5efa\u8bbe",
                "\u65b0\u589e",
            ),
            "Compute leasing or digital infrastructure is disclosed with an economic bridge; it must enter the earnings and asset-quality debate.",
            "Use as filing-grade evidence that the new business may already have operating assets or monetization.",
            "Test ownership boundary, revenue recognition, asset intensity, lease terms, customer quality, margin, and cash conversion before assigning valuation credit.",
        ),
        (
            "contracted-commercialization",
            "high",
            ("长期协议", "长协", "长期销售协议", "长期采购协议"),
            ("甲醇", "绿醇", "绿色甲醇", "氢", "燃料"),
            "A new-business line has progressed beyond concept into contracted demand, improving future revenue visibility and project financeability.",
            "Use as stronger-than-theme evidence that commercialization has begun and future capacity has a demand anchor.",
            "Test customer concentration, contract economics, delivery timing, and whether signed demand is material enough for the listed company.",
        ),
        (
            "named-customer-validation",
            "high",
            ("马士基", "赫伯罗特", "国际航运巨头"),
            ("协议", "订单", "签订"),
            "Named customers or counterparties reduce pure-story risk and improve confidence that a business line has real market pull.",
            "Use named-customer validation to support monetization credibility and downstream acceptance.",
            "Ask whether the disclosed customer relationship is exclusive, material, margin-accretive, and already reflected in valuation.",
        ),
        (
            "capacity-to-demand-bridge",
            "high",
            ("产能", "投产", "在建", "建设"),
            ("长期协议", "长协", "订单", "消纳", "锁定"),
            "Capacity expansion is more investable when filings also disclose a demand sink or offtake path.",
            "Argue that capex is attached to visible demand rather than blind expansion.",
            "Challenge utilization, delivery schedule, and whether economics still work if the market weakens.",
        ),
    )

    strategic_bridge_terms = ("甲醇", "绿醇", "绿色甲醇", "氢", "燃料", "储能", "海外")

    for title, text in report_texts:
        for line in _iter_filing_text_units(text, limit=280):
            if not line:
                continue
            for (
                finding_type,
                importance,
                required_any,
                companion_any,
                investment_read,
                bull_use,
                bear_use,
            ) in patterns:
                if not any(token in line for token in required_any):
                    continue
                if not any(token in line for token in companion_any):
                    continue
                if (
                    finding_type == "capacity-to-demand-bridge"
                    and not any(token in line for token in strategic_bridge_terms)
                ):
                    continue
                key = (finding_type, line)
                if key in seen:
                    continue
                seen.add(key)
                findings.append(
                    MaterialFilingFinding(
                        finding_type=finding_type,
                        importance=importance,
                        evidence=f"{title}: {line}",
                        investment_read=investment_read,
                        bull_use=bull_use,
                        bear_use=bear_use,
                    )
                )
    return findings[:12]


_BUSINESS_MODEL_RULES: tuple[tuple[str, tuple[str, ...], str], ...] = (
    (
        "core_revenue_engine",
        ("主营业务", "营业收入", "主要产品", "主要服务", "销售"),
        "Defines what actually drives the income statement.",
    ),
    (
        "segment_mix",
        ("分业务", "分产品", "收入占比", "主营业务分行业", "主营业务分产品", "主营业务分地区"),
        "Shows whether different profit pools are being mixed together.",
    ),
    (
        "customer_and_channel",
        ("客户", "经销商", "直销", "订单", "协议"),
        "Reveals demand source, concentration, and market validation.",
    ),
    (
        "geography",
        ("境外收入", "海外订单", "海外业务", "国际业务", "出口"),
        "Explains whether growth depends on a specific geography or expansion lane.",
    ),
    (
        "reinvestment_engine",
        ("研发", "资本开支", "在建工程", "产能", "投产"),
        "Shows how today's cash is being converted into tomorrow's earnings power.",
    ),
)

_SEGMENT_SECTION_TERMS: tuple[str, ...] = (
    "分产品",
    "分行业",
    "分地区",
    "分业务",
    "主营业务分产品",
    "主营业务分地区",
    "主营业务分行业",
)

_SEGMENT_VALUE_TERMS: tuple[str, ...] = (
    "营业收入",
    "营业成本",
    "毛利率",
    "收入占比",
    "同比",
    "境外",
    "海外",
    "直销",
    "批发",
    "经销",
    "茅台酒",
    "系列酒",
    "汽车",
    "电池",
    "电子",
)


_SEGMENT_SECTION_TERMS = (
    *_SEGMENT_SECTION_TERMS,
    "\u5206\u4ea7\u54c1",
    "\u5206\u4e1a\u52a1",
    "\u5206\u884c\u4e1a",
    "\u4e3b\u8425\u4e1a\u52a1",
    "\u7b97\u529b\u79df\u8d41",
    "\u667a\u4e91\u8ba1\u7b97",
    "\u667a\u7b97\u4e2d\u5fc3",
    "\u7f51\u7edc\u5de5\u7a0b",
)
_SEGMENT_VALUE_TERMS = (
    *_SEGMENT_VALUE_TERMS,
    "\u6536\u5165",
    "\u8425\u6536",
    "\u8425\u4e1a\u6536\u5165",
    "\u8425\u4e1a\u6210\u672c",
    "\u6bdb\u5229",
    "\u6bdb\u5229\u7387",
    "\u540c\u6bd4",
    "\u8d44\u4ea7",
    "\u7b97\u529b\u79df\u8d41",
    "\u667a\u4e91\u8ba1\u7b97",
    "\u667a\u7b97\u4e2d\u5fc3",
    "\u7f51\u7edc\u5de5\u7a0b",
)

_SEGMENT_EXCLUDE_TERMS: tuple[str, ...] = (
    "银行理财产品",
    "理财产品投资",
    "其他权益工具投资",
    "其他非流动金融资产",
    "交易性金融资产",
    "衍生金融工具",
    "外汇衍生金融工具",
    "金融资产",
    "金融负债",
    "前五名客户",
    "前五大客户",
    "主要销售客户",
    "客户及供应商信息",
    "主要供应商",
    "供应商采购额",
    "第一季度",
    "第二季度",
    "第三季度",
    "第四季度",
    "（1-3 月份）",
    "（4-6 月份）",
    "（7-9 月份）",
    "（10-12 月份）",
)

_STRICT_SEGMENT_CONTEXT_TERMS: tuple[str, ...] = (
    "分产品",
    "分业务",
    "分行业",
    "分地区",
    "分销售模式",
    "主营业务分产品",
    "主营业务分地区",
    "主营业务分行业",
    "营业收入、营业成本的分解信息",
    "算力租赁",
    "智云计算",
    "智算中心",
    "网络工程",
    "电动两轮车",
    "电动滑板车",
    "全地形车",
    "割草机器人",
    "服务机器人",
)


def _is_segment_noise(line: str) -> bool:
    return any(term in line for term in _SEGMENT_EXCLUDE_TERMS)


def _has_strict_segment_context(line: str) -> bool:
    return any(term in line for term in _STRICT_SEGMENT_CONTEXT_TERMS)


def _segment_type(line: str) -> str:
    if any(token in line for token in ("\u7b97\u529b\u79df\u8d41", "\u667a\u4e91\u8ba1\u7b97", "\u667a\u7b97\u4e2d\u5fc3", "\u7f51\u7edc\u5de5\u7a0b")):
        return "business"
    if "产品" in line or any(token in line for token in ("茅台酒", "系列酒", "汽车", "电池", "电子")):
        return "product"
    if "直销" in line or "批发" in line or "经销" in line:
        return "channel"
    if "地区" in line or "境外" in line or "海外" in line:
        return "geography"
    return "business"


def _extract_segment_economics(
    report_texts: Iterable[tuple[str, str]],
    *,
    max_rows: int = 12,
) -> list[SegmentEconomicsFinding]:
    """Extract product/geography/channel economics from annual and half-year reports."""
    rows: list[tuple[int, SegmentEconomicsFinding]] = []
    seen: set[str] = set()
    for report_index, (title, text) in enumerate(report_texts):
        report_type = _detect_report_type(title)
        if report_type not in {"annual", "semiannual"}:
            continue
        lines = [line.strip() for line in str(text or "").splitlines() if line.strip()]
        for idx, raw_line in enumerate(lines):
            window = " ".join(lines[idx : idx + 4])
            compacted = _compact_text(window, limit=360)
            if (
                not compacted
                or compacted in seen
                or _is_low_signal_line(compacted)
                or _is_segment_noise(compacted)
                or not _has_strict_segment_context(compacted)
                or not any(term in compacted for term in _SEGMENT_VALUE_TERMS)
                or len(_TABLE_NUMBER_RE.findall(compacted)) < 2
            ):
                continue
            seen.add(compacted)
            score = len(_TABLE_NUMBER_RE.findall(compacted))
            if any(term in compacted for term in ("营业收入", "营业成本", "毛利率")):
                score += 4
            if any(term in compacted for term in _SEGMENT_SECTION_TERMS):
                score += 3
            score += max(0, 3 - report_index)
            rows.append(
                (
                    score,
                    SegmentEconomicsFinding(
                        segment_type=_segment_type(compacted),
                        report_type=report_type,
                        evidence=f"{title}: {compacted}",
                        analyst_use=(
                            "Use this to explain revenue mix, profit-pool quality, gross-margin dilution/accretion, "
                            "and whether bull/bear claims depend on a specific product, geography, or channel."
                        ),
                    ),
                )
            )
    rows.sort(key=lambda item: item[0], reverse=True)
    return [row for _, row in rows[:max_rows]]


def _segment_valuation_anchor(segment_type: str, evidence: str) -> tuple[str, str, str]:
    """Translate a filing-derived segment clue into a valuation treatment."""
    text = evidence.lower()
    has_margin = any(token in evidence for token in ("毛利", "毛利率", "姣涘埄", "姣涘埄鐜?"))
    has_revenue = any(token in evidence for token in ("收入", "营收", "营业收入", "鏀跺叆", "钀ヤ笟鏀跺叆"))
    has_growth = any(token in evidence for token in ("同比", "增长", "增速", "鍚屾瘮", "澧為暱"))
    has_new_curve = any(
        token in evidence
        for token in (
            "算力租赁",
            "智云计算",
            "智算中心",
            "数据中心",
            "网络工程",
            "新业务",
            "新产品",
            "第二增长",
            "compute",
            "data center",
        )
    )

    if has_new_curve:
        return (
            "emerging_or_second_curve",
            "SOTP or scenario valuation only until segment revenue, margin, capex/utilization, customer quality, and cash conversion are disclosed.",
            "Quantify revenue/profit contribution, asset intensity, utilization, contract terms, recurrence, and cash collection before moving it into base-case valuation.",
        )
    if segment_type == "geography":
        return (
            "geography_or_export_lane",
            "Use as a growth/margin modifier for the core business; only value separately when regional revenue, margin, and regulatory risk are disclosed.",
            "Check regional revenue growth, gross margin, channel inventory, currency/regulatory exposure, and whether the region has different economics.",
        )
    if segment_type == "channel":
        return (
            "channel_mix",
            "Use as a sales-efficiency and working-capital modifier; do not value as a separate business unless channel economics are disclosed.",
            "Check direct/dealer/platform split, take rate or gross margin, receivables, inventory burden, and customer acquisition cost.",
        )
    if segment_type == "product":
        anchor = (
            "Value product lines with normalized earnings or EV/EBIT/PE by segment "
            "when revenue, cost, gross margin, and growth are disclosed; otherwise use as a mix-quality bridge."
        )
        if not (has_revenue and (has_margin or has_growth)):
            anchor = (
                "Use as product-mix context first; upgrade to separate valuation only after revenue, margin, and growth are disclosed."
            )
        return (
            "core_product_line",
            anchor,
            "Check segment revenue scale, gross margin, growth durability, ASP/volume/mix, cash conversion, and peer multiples for that product line.",
        )
    return (
        "core_or_adjacent_business",
        "Start from normalized earnings/FCF for the mature engine; split into SOTP only when filings disclose distinct revenue, margin, assets, or growth profile.",
        "Check whether the evidence identifies a real profit pool rather than a generic business description.",
    )


def _build_business_segment_valuation_map(
    business_model_map: Iterable[BusinessModelFinding],
    segment_economics: Iterable[SegmentEconomicsFinding],
    growth_vectors: Iterable[GrowthVectorFinding],
    *,
    limit: int = 12,
) -> list[BusinessSegmentValuationFinding]:
    """Build a SOTP-oriented map from filing evidence.

    The map is intentionally evidence-led: it does not invent segment values.
    It tells downstream agents which disclosed business buckets can support
    separate valuation and which remain scenario/watch items.
    """
    rows: list[BusinessSegmentValuationFinding] = []
    seen: set[tuple[str, str]] = set()

    def add(
        business_bucket: str,
        report_type: str,
        evidence: str,
        valuation_anchor: str,
        analyst_use: str,
        verification_need: str,
    ) -> None:
        compacted = _compact_text(evidence, 300)
        key = (business_bucket, compacted)
        if not compacted or key in seen:
            return
        seen.add(key)
        rows.append(
            BusinessSegmentValuationFinding(
                business_bucket=business_bucket,
                report_type=report_type,
                evidence=compacted,
                valuation_anchor=valuation_anchor,
                analyst_use=analyst_use,
                verification_need=verification_need,
            )
        )

    for item in business_model_map:
        if item.lens == "core_revenue_engine":
            add(
                "core_revenue_engine",
                item.report_type,
                item.evidence,
                "Anchor the first valuation block on the mature revenue engine: normalized earnings, FCF yield, EV/EBITDA, PE, or peer-relative multiples depending on business model.",
                "Use this as the company introduction before discussing optionality; every later segment should be compared with this core engine.",
                "Confirm the core engine's revenue scale, margin, cash conversion, reinvestment need, and peer multiple range.",
            )
        elif item.lens in {"segment_mix", "geography", "customer_and_channel"}:
            bucket, anchor, verification = _segment_valuation_anchor(item.lens.replace("customer_and_channel", "channel"), item.evidence)
            add(
                bucket,
                item.report_type,
                item.evidence,
                anchor,
                "Use this to decide whether the company needs a split valuation rather than one blended multiple.",
                verification,
            )

    for item in segment_economics:
        bucket, anchor, verification = _segment_valuation_anchor(item.segment_type, item.evidence)
        add(
            bucket,
            item.report_type,
            item.evidence,
            anchor,
            "Build the bull/base/bear case around this segment's own revenue, margin, growth, and cash-quality evidence instead of company-level averages only.",
            verification,
        )

    for item in growth_vectors:
        add(
            "emerging_or_second_curve",
            "filing",
            item.evidence,
            (
                "Treat as SOTP/scenario value when stage is "
                f"{item.stage}; include in base-case valuation only after monetization and economics are disclosed."
            ),
            "Use as the new-business block in a split valuation: size the option separately from the mature core business.",
            item.verification_need,
        )

    priority = {
        "core_revenue_engine": 0,
        "core_product_line": 1,
        "core_or_adjacent_business": 2,
        "emerging_or_second_curve": 3,
        "geography_or_export_lane": 4,
        "channel_mix": 5,
    }
    rows.sort(key=lambda row: (priority.get(row.business_bucket, 9), row.report_type))
    return rows[:limit]


_TABLE_NUMBER_RE = re.compile(r"(?<!\d)\d[\d,]*(?:\.\d+)?(?!\d)")
_TABLE_ACCOUNT_RULES: tuple[
    tuple[str, tuple[str, ...], str, str, str],
    ...
] = (
    (
        "contract_liabilities",
        ("合同负债", "预收款项"),
        "Prepayments from customers are a direct visibility and bargaining-power signal.",
        "Use sustained growth as support for demand visibility if it later converts into revenue and cash.",
        "Challenge whether higher advances reflect true pricing power or merely altered payment terms.",
    ),
    (
        "receivables",
        ("应收账款", "应收票据"),
        "Receivables decide whether reported growth becomes collectible cash.",
        "Use stable receivables relative to sales as proof of healthy conversion.",
        "Use receivable inflation to attack revenue quality and future impairment risk.",
    ),
    (
        "inventory",
        ("存货",),
        "Inventory reveals whether production is ahead of sell-through or preparing for demand.",
        "Use controlled inventory with rising deliveries as evidence of healthy execution.",
        "Use inventory build to test overproduction, price cuts, and future write-down risk.",
    ),
    (
        "prepayments",
        ("预付款项",),
        "Supplier prepayments show whether growth is consuming cash before delivery.",
        "Use disciplined prepayments to support supply assurance for real orders.",
        "Use sharp increases to challenge cash quality and supplier bargaining position.",
    ),
    (
        "construction_in_progress",
        ("在建工程",),
        "Construction in progress turns strategy into capital already committed.",
        "Use when capex is tied to visible demand or higher-return expansion.",
        "Challenge utilization, payback period, and capex-before-demand risk.",
    ),
    (
        "long_term_equity_investments",
        ("长期股权投资", "其他非流动金融资产", "其他权益工具投资"),
        "Investment assets can matter for SOTP/NAV and reveal capital-allocation behavior.",
        "Use named assets and realization history to support hidden value or skill.",
        "Challenge valuation, liquidity, and whether optionality is too small to matter.",
    ),
    (
        "operating_cash_flow",
        ("经营活动产生的现金流量净额",),
        "Operating cash flow is the hard checkpoint for earnings quality.",
        "Use improvement to validate operating leverage and conversion.",
        "Use deterioration to challenge reported profit quality.",
    ),
    (
        "impairment",
        ("信用减值损失", "资产减值损失", "存货跌价准备"),
        "Impairment lines expose the cost of prior weak underwriting or poor sell-through.",
        "Use falling impairment only when it matches healthier assets.",
        "Use rising impairment to attack asset quality and repeatability of profits.",
    ),
)

_NOTE_FINDING_RULES: tuple[
    tuple[str, str, tuple[str, ...], str, str, str],
    ...
] = (
    (
        "customer_concentration",
        "high",
        ("前五名客户", "前五大客户", "客户集中度"),
        "Customer concentration changes the durability and bargaining power of revenue.",
        "Use diversified customers or named blue-chip customers to support demand quality.",
        "Challenge dependence, renewal risk, and negotiating leverage.",
    ),
    (
        "related_party",
        "high",
        ("关联方交易", "关联交易"),
        "Related-party disclosures are a governance and earnings-quality checkpoint.",
        "Use low reliance on related parties as a governance positive.",
        "Use heavy or opaque related-party flows to attack quality and independence.",
    ),
    (
        "guarantees",
        "high",
        ("对外担保", "担保余额", "担保责任"),
        "Guarantees can turn off-balance-sheet obligations into future downside.",
        "Use limited guarantees to support balance-sheet resilience.",
        "Use large or expanding guarantees to surface contingent risk.",
    ),
    (
        "litigation",
        "high",
        ("诉讼", "仲裁"),
        "Litigation and arbitration can change downside tails before they hit earnings.",
        "Use resolved or immaterial cases only as risk relief.",
        "Use unresolved material cases to attack tail-risk underpricing.",
    ),
    (
        "impairment_policy",
        "supporting",
        ("坏账准备", "存货跌价准备", "减值准备"),
        "Provisioning language explains whether accounting conservatism is strengthening or weakening.",
        "Use conservative provisioning only when it lowers future surprise risk.",
        "Use aggressive assumptions or rising provisions to challenge earnings quality.",
    ),
    (
        "capitalized_development",
        "supporting",
        ("开发支出", "资本化", "研发支出资本化"),
        "Capitalized development can shift current profit at the cost of later amortization risk.",
        "Use with commercialization evidence to support platform investment.",
        "Challenge profit quality if capitalization rises ahead of monetization.",
    ),
)


def _first_matching_line(
    report_texts: Iterable[tuple[str, str]],
    keywords: tuple[str, ...],
    preferred_types: tuple[str, ...],
    line_filter=None,
) -> tuple[str, str] | None:
    candidates: list[tuple[int, str, str]] = []
    for report_index, (title, text) in enumerate(report_texts):
        report_type = _detect_report_type(title)
        for raw_line in str(text or "").splitlines():
            line = _compact_text(raw_line, limit=260)
            if (
                not line
                or _is_low_signal_line(line)
                or not any(keyword in line for keyword in keywords)
                or (line_filter is not None and not line_filter(line))
            ):
                continue
            score = 0
            if report_type in preferred_types:
                score += 3
            if _evidence_strength(line) == "quantified disclosure":
                score += 2
            score += max(0, 3 - report_index)
            candidates.append((score, report_type, f"{title}: {line}"))
    if not candidates:
        return None
    _, report_type, evidence = max(candidates, key=lambda item: item[0])
    return report_type, evidence


_BUSINESS_MODEL_COMPANY_TERMS: tuple[str, ...] = (
    "公司",
    "本公司",
    "主营",
    "主要",
    "业务",
    "产品",
    "服务",
    "客户",
)

_BUSINESS_MODEL_SUBSTANCE_TERMS: tuple[str, ...] = (
    "收入",
    "占比",
    "销售",
    "订单",
    "市场",
    "业务",
    "客户",
    "研发",
    "资本开支",
    "在建工程",
    "产能",
)

_BUSINESS_MODEL_HEADER_ONLY_TERMS: tuple[str, ...] = (
    "分产品",
    "分行业",
    "分地区",
    "主营业务分析",
    "公司业务概要",
)

_BUSINESS_MODEL_NOISE_TERMS: tuple[str, ...] = (
    "前五名客户",
    "前五大客户",
    "主要销售客户",
    "主要供应商",
    "客户及供应商信息",
    "贸易业务收入占营业收入比例超过 10%的贸易业务前五名销售客户",
    "银行理财产品",
    "其他权益工具投资",
    "其他非流动金融资产",
    "交易性金融资产",
    "衍生金融工具",
)


def _business_model_line_score(lens: str, line: str) -> int:
    if line.strip() in _BUSINESS_MODEL_HEADER_ONLY_TERMS or len(line.strip()) <= 8:
        return -999
    score = 0
    if any(token in line for token in _BUSINESS_MODEL_COMPANY_TERMS):
        score += 2
    score += min(3, sum(token in line for token in _BUSINESS_MODEL_SUBSTANCE_TERMS))
    if _evidence_strength(line) == "quantified disclosure":
        score += 2
    if len(line) >= 28:
        score += 1
    if lens == "segment_mix" and any(token in line for token in ("占比", "收入", "毛利率")):
        score += 2
    if lens == "customer_and_channel" and any(token in line for token in ("客户", "订单", "协议", "经销", "直销")):
        score += 2
    if lens == "reinvestment_engine" and any(token in line for token in ("研发", "资本开支", "在建工程", "产能", "投产")):
        score += 2
    return score


def _best_business_model_line(
    report_texts: Iterable[tuple[str, str]],
    lens: str,
    keywords: tuple[str, ...],
    preferred_types: tuple[str, ...],
) -> tuple[str, str] | None:
    candidates: list[tuple[int, str, str]] = []
    for report_index, (title, text) in enumerate(report_texts):
        report_type = _detect_report_type(title)
        for raw_line in str(text or "").splitlines():
            line = _compact_text(raw_line, limit=260)
            if (
                not line
                or _is_low_signal_line(line)
                or any(term in line for term in _BUSINESS_MODEL_NOISE_TERMS)
                or not any(keyword in line for keyword in keywords)
            ):
                continue
            if lens == "core_revenue_engine" and not any(
                token in line
                for token in (
                    "主营业务",
                    "主要产品",
                    "主要服务",
                    "产品包括",
                    "业务包括",
                    "覆盖",
                    "从事",
                    "营业收入",
                )
            ):
                continue
            if lens == "segment_mix" and not any(token in line for token in ("占比", "收入", "毛利率")):
                continue
            if lens == "reinvestment_engine" and not any(
                token in line for token in ("投入", "增加", "建设", "投产", "资本开支", "在建工程")
            ):
                continue
            score = _business_model_line_score(lens, line)
            if report_type in preferred_types:
                score += 3
            score += max(0, 3 - report_index)
            candidates.append((score, report_type, f"{title}: {line}"))
    if not candidates:
        return None
    best_score, report_type, evidence = max(candidates, key=lambda item: item[0])
    if best_score <= 0:
        return None
    return report_type, evidence


def _build_business_model_map(
    report_texts: Iterable[tuple[str, str]],
) -> list[BusinessModelFinding]:
    reports = list(report_texts)
    rows: list[BusinessModelFinding] = []
    for lens, keywords, why_it_matters in _BUSINESS_MODEL_RULES:
        match = _best_business_model_line(
            [
                (title, text)
                for title, text in reports
                if _detect_report_type(title) in {"annual", "semiannual"}
            ],
            lens,
            keywords,
            preferred_types=("annual", "semiannual"),
        )
        if match is None:
            match = _best_business_model_line(
                reports,
                lens,
                keywords,
                preferred_types=("annual", "semiannual"),
            )
        if match is None:
            continue
        report_type, evidence = match
        rows.append(
            BusinessModelFinding(
                lens=lens,
                report_type=report_type,
                evidence=evidence,
                why_it_matters=why_it_matters,
            )
        )
    return rows


_GROWTH_VECTOR_RULES: dict[str, tuple[str, ...]] = {
    "green-fuels": ("绿色甲醇", "绿醇", "氢能", "绿色燃料"),
    "energy-storage": ("储能", "电池", "虚拟电厂"),
    "ai-and-digital": ("人工智能", "算力", "数据中心", "数字化"),
    "commercial-space": ("商业航天", "卫星", "火箭"),
    "overseas-expansion": ("海外订单", "海外业务", "国际化", "出口", "境外收入"),
    "new-product-platform": ("新产品", "新业务", "第二增长", "新材料"),
}


def _growth_stage(line: str) -> tuple[str, str, str]:
    if any(token in line for token in ("\u79df\u8d41\u4e1a\u52a1\u89c4\u6a21", "\u6536\u5165", "\u8425\u6536", "\u5229\u6da6", "\u6bdb\u5229")) and any(
        token in line
        for token in (
            "\u7b97\u529b\u79df\u8d41",
            "\u667a\u4e91\u8ba1\u7b97",
            "\u667a\u7b97\u4e2d\u5fc3",
            "\u6570\u636e\u4e2d\u5fc3",
            "\u7f51\u7edc\u5de5\u7a0b",
        )
    ):
        return (
            "monetized",
            "eligible for valuation bridge review",
            "check segment revenue, asset intensity, margin, lease terms, and cash conversion",
        )
    if any(token in line for token in ("\u5efa\u8bbe", "\u8d44\u4ea7", "\u65b0\u589e", "\u6295\u8d44")) and any(
        token in line
        for token in (
            "\u7b97\u529b\u79df\u8d41",
            "\u667a\u4e91\u8ba1\u7b97",
            "\u667a\u7b97\u4e2d\u5fc3",
            "\u6570\u636e\u4e2d\u5fc3",
            "\u7f51\u7edc\u5de5\u7a0b",
        )
    ):
        return (
            "capacity-building",
            "scenario upside, but capital intensity and utilization must be tested",
            "check asset ownership, utilization, customer contracts, and commissioning timetable",
        )
    if any(token in line for token in ("签订长期协议", "签订协议", "中标", "订单", "客户")):
        return (
            "contracted",
            "eligible for core discussion if scale and economics matter",
            "check contract size, delivery schedule, pricing, and concentration",
        )
    if any(token in line for token in ("实现收入", "营业收入", "收入贡献", "利润")):
        return (
            "monetized",
            "eligible for valuation bridge review",
            "check segment revenue, margin, and recurrence",
        )
    if any(token in line for token in ("投产", "产能", "在建", "建设")):
        return (
            "capacity-building",
            "scenario upside, not yet fully valuation-grade",
            "check utilization, offtake, and commissioning timetable",
        )
    return (
        "planned",
        "narrative or early optionality only",
        "check customers, orders, capacity, and revenue evidence",
    )


_LOW_SIGNAL_LINE_TOKENS: tuple[str, ...] = (
    "境外会计准则",
    "境外上市外资",
    "境外法人",
    "会计准则",
    "香港中央结算",
    "价格显失公允",
)


def _is_low_signal_line(line: str) -> bool:
    return any(token in line for token in _LOW_SIGNAL_LINE_TOKENS)


_COMPANY_SUBJECT_TOKENS: tuple[str, ...] = (
    "公司",
    "本公司",
)

_COMPANY_ACTION_TOKENS: tuple[str, ...] = (
    "已开展",
    "开展",
    "布局",
    "建设",
    "投产",
    "产能",
    "生产",
    "签订",
    "订单",
    "客户",
    "实现收入",
    "营业收入",
)

_MACRO_ONLY_TOKENS: tuple[str, ...] = (
    "国家",
    "政策",
    "规划",
    "行业",
    "推动",
    "支持",
    "鼓励",
    "市场空间",
)

_POLICY_REFERENCE_LINE_TOKENS: tuple[str, ...] = (
    "国家发展改革委",
    "国家能源局",
    "印发《",
    "专项行动方案",
    "建设一批",
    "探索建设",
)

_COMPANY_SPECIFIC_COMMERCIAL_TOKENS: tuple[str, ...] = (
    "订单",
    "客户",
    "签订",
    "协议",
    "产能",
    "投产",
    "建设",
    "实现收入",
    "营业收入",
    "销售",
)


_GROWTH_VECTOR_RULES["ai-and-digital"] = (
    *_GROWTH_VECTOR_RULES.get("ai-and-digital", ()),
    "\u7b97\u529b",
    "\u7b97\u529b\u79df\u8d41",
    "\u667a\u4e91\u8ba1\u7b97",
    "\u667a\u7b97\u4e2d\u5fc3",
    "\u7b97\u529b\u4e2d\u5fc3",
    "\u6570\u636e\u4e2d\u5fc3",
    "\u7f51\u7edc\u5de5\u7a0b",
    "AI\u6570\u636e\u670d\u52a1",
)
_COMPANY_SUBJECT_TOKENS = (
    *_COMPANY_SUBJECT_TOKENS,
    "\u516c\u53f8",
    "\u672c\u516c\u53f8",
    "\u5b50\u516c\u53f8",
    "\u5e7f\u4e1c\u76c8\u5cf0",
)
_COMPANY_ACTION_TOKENS = (
    *_COMPANY_ACTION_TOKENS,
    "\u5f00\u5c55",
    "\u5efa\u8bbe",
    "\u6295\u8d44",
    "\u8fd0\u8425",
    "\u5b9e\u73b0",
    "\u5f62\u6210",
    "\u65b0\u589e",
    "\u4ea7\u751f",
)
_COMPANY_SPECIFIC_COMMERCIAL_TOKENS = (
    *_COMPANY_SPECIFIC_COMMERCIAL_TOKENS,
    "\u6536\u5165",
    "\u8425\u6536",
    "\u5229\u6da6",
    "\u6bdb\u5229",
    "\u8d44\u4ea7",
    "\u79df\u8d41\u4e1a\u52a1\u89c4\u6a21",
    "\u8ba2\u5355",
    "\u5ba2\u6237",
    "\u7b97\u529b\u79df\u8d41",
    "\u667a\u4e91\u8ba1\u7b97",
    "\u667a\u7b97\u4e2d\u5fc3",
    "\u6570\u636e\u4e2d\u5fc3",
    "\u7f51\u7edc\u5de5\u7a0b",
)


def _is_company_owned_growth_line(line: str) -> bool:
    has_company_subject = any(token in line for token in _COMPANY_SUBJECT_TOKENS)
    has_company_action = any(token in line for token in _COMPANY_ACTION_TOKENS)
    has_commercial_anchor = any(token in line for token in _COMPANY_SPECIFIC_COMMERCIAL_TOKENS)
    if not has_company_subject and not has_commercial_anchor:
        return False
    if not has_company_action and not has_commercial_anchor:
        return False
    if any(token in line for token in _POLICY_REFERENCE_LINE_TOKENS) and not (
        has_company_subject and has_commercial_anchor
    ):
        return False
    if any(token in line for token in _MACRO_ONLY_TOKENS) and not any(
        token in line for token in _COMPANY_SPECIFIC_COMMERCIAL_TOKENS
    ):
        return False
    return True


def _extract_growth_vectors(
    report_texts: Iterable[tuple[str, str]],
) -> list[GrowthVectorFinding]:
    ranked_rows: list[tuple[int, GrowthVectorFinding]] = []
    seen: set[tuple[str, str]] = set()
    for title, text in report_texts:
        for line in _iter_filing_text_units(text, limit=280):
            if not line or _is_low_signal_line(line) or not _is_company_owned_growth_line(line):
                continue
            for vector, keywords in _GROWTH_VECTOR_RULES.items():
                if not any(keyword in line for keyword in keywords):
                    continue
                key = (vector, line)
                if key in seen:
                    continue
                seen.add(key)
                stage, valuation_treatment, verification_need = _growth_stage(line)
                score = {
                    "contracted": 5,
                    "monetized": 4,
                    "capacity-building": 3,
                    "planned": 1,
                }[stage]
                if _evidence_strength(line) == "quantified disclosure":
                    score += 2
                if any(token in line for token in _COMPANY_SPECIFIC_COMMERCIAL_TOKENS):
                    score += 1
                ranked_rows.append(
                    (
                        score,
                        GrowthVectorFinding(
                            vector=vector,
                            stage=stage,
                            evidence=f"{title}: {line}",
                            valuation_treatment=valuation_treatment,
                            verification_need=verification_need,
                        ),
                    )
                )
    selected: list[GrowthVectorFinding] = []
    per_vector: dict[str, int] = {}
    for _, row in sorted(ranked_rows, key=lambda item: item[0], reverse=True):
        if per_vector.get(row.vector, 0) >= 2:
            continue
        selected.append(row)
        per_vector[row.vector] = per_vector.get(row.vector, 0) + 1
    return selected[:12]


def _iter_filing_text_units(text: str, limit: int = 280) -> Iterable[str]:
    """Yield lines plus short adjacent windows from PDF-extracted filing text."""
    lines = [_compact_text(line, limit=limit) for line in str(text or "").splitlines()]
    lines = [line for line in lines if line]
    seen: set[str] = set()
    for idx, line in enumerate(lines):
        if line not in seen:
            seen.add(line)
            yield line
        for width in (2, 3):
            if idx + width > len(lines):
                continue
            window = _compact_text(" ".join(lines[idx : idx + width]), limit=limit)
            if window and window not in seen:
                seen.add(window)
                yield window


_REPORT_BRIDGE_TOPICS: tuple[
    tuple[str, tuple[str, ...], str],
    ...
] = (
    (
        "orders_and_visibility",
        ("订单", "合同负债", "在手订单", "中标"),
        "Does the short-cycle report confirm the demand visibility described in long-cycle filings?",
    ),
    (
        "pricing_and_margin",
        ("毛利率", "投标均价", "营业成本"),
        "Does the latest checkpoint validate or weaken the prior margin story?",
    ),
    (
        "cash_conversion",
        ("经营活动现金流", "应收账款", "存货", "预付款"),
        "Do newer filings show profits turning into cash?",
    ),
    (
        "growth_vectors",
        ("新业务", "绿色甲醇", "储能", "海外", "商业航天"),
        "Are long-cycle growth vectors gaining real evidence over time?",
    ),
    (
        "capital_intensity",
        ("资本开支", "在建工程", "产能", "投产"),
        "Is reinvestment translating into visible operating progress?",
    ),
)


_DEEP_READING_SECTION_RULES: dict[str, tuple[tuple[str, str], ...]] = {
    "annual": (
        ("公司业务概要", "Read the business model and value chain."),
        ("经营情况讨论与分析", "Read the year's real operating story."),
        ("经营情况讨论及分析", "Read the year's real operating story."),
        ("主营业务分析", "Read segment mix, pricing, and profit pools."),
        ("核心竞争力分析", "Read moat claims and what protects economics."),
        ("公司未来发展的展望", "Read strategy and second-curve ambitions."),
        ("未来发展展望", "Read strategy and second-curve ambitions."),
        ("重大风险提示", "Read long-cycle risks and tail exposures."),
        ("风险管理", "Read long-cycle risks and tail exposures."),
    ),
    "semiannual": (
        ("经营情况讨论与分析", "Check whether the annual thesis is forming into a trend."),
        ("经营情况讨论及分析", "Check whether the annual thesis is forming into a trend."),
        ("主营业务分析", "Check segment and mix evolution."),
        ("风险因素", "Check newly emerging risks."),
    ),
    "quarterly": (
        ("主要会计数据和财务指标发生变动的情况及原因", "Check short-cycle proof or disproof."),
        ("公司订单情况", "Check immediate demand visibility."),
        ("经营活动产生的现金流量净额", "Check cash conversion."),
        ("季度经营分析", "Check short-cycle proof or disproof."),
    ),
}


_PARAGRAPH_READING_LENSES: dict[
    str,
    tuple[tuple[str, tuple[str, ...], tuple[str, ...], str, str], ...],
] = {
    "annual": (
        (
            "business_model",
            ("公司业务概要", "主营业务分析", "经营情况讨论及分析"),
            ("主营业务", "产品", "服务", "收入", "客户", "销售"),
            "What actually earns money today?",
            "Separates the real profit engine from slogans and incidental businesses.",
        ),
        (
            "second_curve",
            ("公司未来发展的展望", "未来发展展望", "主营业务分析", "经营情况讨论及分析", "公司业务概要"),
            ("新业务", "新产品", "布局", "建设", "投产", "订单", "客户", "战略"),
            "What could become the next material earnings engine?",
            "Identifies whether optionality is still a story or already has an economic bridge.",
        ),
        (
            "moat",
            ("核心竞争力分析",),
            ("市场地位", "技术", "研发", "专利", "品牌", "客户", "渠道"),
            "Why might returns persist?",
            "Tests whether claimed advantages protect economics rather than merely decorate the report.",
        ),
        (
            "long_cycle_risk",
            ("重大风险提示", "风险因素", "风险管理"),
            ("风险", "价格", "政策", "减值", "诉讼", "担保", "汇率", "需求"),
            "What could permanently impair equity value?",
            "Keeps long-cycle downside visible instead of overfitting to recent earnings.",
        ),
    ),
    "semiannual": (
        (
            "trend_formation",
            ("经营情况讨论与分析", "经营情况讨论及分析", "主营业务分析"),
            ("收入", "毛利", "订单", "客户", "产能", "出货", "增长"),
            "Is the annual thesis becoming a real trend?",
            "Bridges annual storytelling and quarterly volatility.",
        ),
        (
            "mix_shift",
            ("主营业务分析",),
            ("占比", "毛利率", "分产品", "分业务", "海外", "高端"),
            "Is the profit pool moving toward better businesses?",
            "Shows whether growth quality is improving, not merely volume.",
        ),
        (
            "risk_update",
            ("风险因素", "重大风险提示"),
            ("风险", "减值", "诉讼", "担保", "价格", "需求"),
            "Which risks are newly forming or fading?",
            "Prevents stale annual assumptions from lingering for too long.",
        ),
    ),
    "quarterly": (
        (
            "short_cycle_execution",
            ("主要会计数据和财务指标发生变动的情况及原因", "公司订单情况", "季度经营分析"),
            ("营业收入", "营业成本", "订单", "合同负债", "毛利", "同比", "环比"),
            "Did the last quarter confirm or weaken the thesis?",
            "Turns quarterly reports into proof tests rather than headline snapshots.",
        ),
        (
            "cash_conversion",
            ("主要会计数据和财务指标发生变动的情况及原因", "经营活动产生的现金流量净额", "季度经营分析"),
            ("经营活动现金流", "应收账款", "存货", "预付款", "回款"),
            "Did earnings turn into cash?",
            "Catches revenue quality and working-capital stress early.",
        ),
        (
            "new_signal",
            ("主要会计数据和财务指标发生变动的情况及原因", "公司订单情况", "季度经营分析"),
            ("新业务", "新产品", "客户", "订单", "产能", "投产"),
            "Did a new business line gain or lose evidence this quarter?",
            "Keeps emerging vectors under live surveillance.",
        ),
    ),
}


_INDUSTRY_PARAGRAPH_LENSES: dict[
    str,
    tuple[tuple[str, tuple[str, ...], tuple[str, ...], str, str, str], ...],
] = {
    "smart_grid_automation": (
        (
            "grid_order_and_backlog",
            ("\u4e3b\u8425\u4e1a\u52a1\u5206\u6790", "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u4e0e\u5206\u6790", "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u53ca\u5206\u6790", "\u8ba2\u5355"),
            ("\u7535\u7f51\u81ea\u52a8\u5316", "\u7ee7\u7535\u4fdd\u62a4", "\u8c03\u5ea6", "\u914d\u7535", "\u5408\u540c\u8d1f\u503a", "\u4e2d\u6807", "\u56fd\u5bb6\u7535\u7f51"),
            "Are grid orders and backlog converting into revenue, cash, and accepted projects?",
            "Separates durable grid capex demand from delayed project acceptance or collection.",
            "peer comparison + earnings model + policy planning",
        ),
        (
            "segment_economics",
            ("\u4e3b\u8425\u4e1a\u52a1\u5206\u6790", "\u5206\u4ea7\u54c1", "\u5206\u884c\u4e1a", "\u5206\u5730\u533a", "\u8425\u4e1a\u6536\u5165", "\u6bdb\u5229\u7387"),
            ("\u7535\u7f51\u81ea\u52a8\u5316", "\u7535\u529b\u4fe1\u606f\u901a\u4fe1", "\u67d4\u6027\u8f93\u7535", "\u65b0\u80fd\u6e90", "\u6d77\u5916", "\u6bdb\u5229\u7387", "\u51c0\u5229\u7387"),
            "Which disclosed business lines carry the revenue, growth, margin, and profit pool?",
            "Forces the final memo to explain what the company actually does before assigning valuation credit.",
            "Business Segment Valuation Map + peer comparison",
        ),
        (
            "second_curve_evidence",
            ("\u4e3b\u8425\u4e1a\u52a1\u5206\u6790", "\u672a\u6765\u53d1\u5c55\u5c55\u671b", "\u65b0\u4ea7\u54c1", "\u65b0\u4e1a\u52a1"),
            ("\u50a8\u80fd", "IGBT", "\u7535\u529b\u673a\u5668\u4eba", "PCS", "\u6d77\u5916", "\u8ba2\u5355", "\u5ba2\u6237", "\u8425\u4e1a\u6536\u5165"),
            "Which second curves have crossed from strategy into disclosed monetization?",
            "Keeps optionality visible while preventing concept-only businesses from entering base valuation.",
            "thematic catalysts + investor interaction + SOTP scenario",
        ),
    ),
    "power_operator": (
        (
            "generation_mix",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("装机", "发电量", "利用小时", "绿电", "绿证", "辅助服务"),
            "Which generation mix is really improving earnings quality?",
            "Separates volume growth from cleaner monetization and better asset mix.",
            "policy planning + power-price/green-power catalysts",
        ),
        (
            "project_returns",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("资本开支", "财务费用", "借款", "在建工程", "投产"),
            "Is new capacity earning acceptable returns after financing cost?",
            "Prevents policy-backed capacity from being mistaken for value creation.",
            "earnings model + balance sheet + policy support",
        ),
    ),
    "precision_equipment": (
        (
            "order_conversion",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("新增订单", "在手订单", "合同负债", "验收", "收入确认"),
            "Are orders converting into revenue rather than remaining brochureware?",
            "Tests visibility and execution quality in project businesses.",
            "investor interactions + thematic catalysts",
        ),
        (
            "mix_upgrade",
            ("主营业务分析", "公司未来发展的展望", "未来发展展望"),
            ("半导体", "显示", "毛利率", "新品", "高端", "收入占比"),
            "Is the company moving into a better profit pool?",
            "Distinguishes real mix upgrade from merely attaching hotter labels.",
            "peer comparison + valuation",
        ),
    ),
    "industrial_components": (
        (
            "order_cash_quality",
            ("\u4e3b\u8425\u4e1a\u52a1\u5206\u6790", "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u4e0e\u5206\u6790", "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u53ca\u5206\u6790"),
            ("\u8ba2\u5355", "\u5408\u540c\u8d1f\u503a", "\u7ecf\u8425\u73b0\u91d1\u6d41", "\u5e94\u6536", "\u9884\u4ed8", "\u5b58\u8d27"),
            "Are orders turning into cash, or does growth require working-capital funding?",
            "Industrial component companies often look better on revenue than on cash conversion.",
            "earnings model + investor interaction + receivables/inventory",
        ),
        (
            "project_and_mix_margin",
            ("\u4e3b\u8425\u4e1a\u52a1\u5206\u6790", "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u4e0e\u5206\u6790", "\u7ecf\u8425\u60c5\u51b5\u8ba8\u8bba\u53ca\u5206\u6790"),
            ("\u6bdb\u5229\u7387", "\u6d77\u5916", "\u9879\u76ee", "\u5ba2\u6237", "\u4ea7\u54c1\u7ed3\u6784", "\u9500\u552e\u5355\u4ef7"),
            "Is the company improving mix and project economics, or just chasing low-margin volume?",
            "Separates real operating leverage from concept-driven end-market exposure.",
            "peer comparison + thematic catalysts + market expectation",
        ),
        (
            "capex_and_new_base",
            ("\u4e3b\u8425\u4e1a\u52a1\u5206\u6790", "\u5728\u5efa\u5de5\u7a0b", "\u91cd\u8981\u5b50\u516c\u53f8"),
            ("\u5728\u5efa\u5de5\u7a0b", "\u57fa\u5730", "\u5b50\u516c\u53f8", "\u8fbe\u4ea7", "\u4ea7\u80fd", "\u6295\u8d44"),
            "Does expansion have a clear utilization and return path?",
            "Prevents asset-heavy expansion from being mistaken for value creation.",
            "management capital allocation + cash-flow quality",
        ),
    ),
    "wind_power_equipment": (
        (
            "backlog_quality",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析", "公司订单情况"),
            ("新增订单", "在手订单", "合同负债", "海外订单", "中标"),
            "Is backlog improving in both quantity and quality?",
            "Separates order visibility from low-priced volume accumulation.",
            "policy planning + investor interactions",
        ),
        (
            "pricing_margin",
            ("主营业务分析", "主要会计数据和财务指标发生变动的情况及原因"),
            ("毛利率", "中标价格", "招投标", "营业成本", "风机"),
            "Has pricing really turned into margin improvement?",
            "Keeps the thesis anchored to monetization, not just demand.",
            "earnings model + market expectation",
        ),
        (
            "second_curve_monetization",
            ("主营业务分析", "公司未来发展的展望", "未来发展展望"),
            ("绿色甲醇", "储能", "混塔", "海外", "订单", "投产", "客户"),
            "Which adjacencies have crossed from story into commercial evidence?",
            "Promotes genuine second curves while capping concept-only premium.",
            "thematic catalysts + investor interactions + policy planning",
        ),
    ),
    "livestock_hog": (
        FilingQuestion(
            "hog_cycle",
            "pricing",
            "生猪价格、仔猪价格、完全成本和猪粮比是否共同指向周期改善？",
            ("生猪价格", "仔猪价格", "完全成本", "猪粮比", "养殖成本"),
            ("quarterly", "semiannual", "annual"),
            "Use realized pricing and cost spread to judge cycle position.",
            "Challenge margin optimism if price recovery is not beating cost.",
        ),
        FilingQuestion(
            "hog_breeding_base",
            "capacity",
            "能繁母猪、PSY、仔猪和出栏量是否显示公司在扩张、收缩还是提效？",
            ("能繁母猪", "PSY", "仔猪", "出栏量", "种猪"),
            ("quarterly", "semiannual", "annual"),
            "Support durable supply advantage when breeding productivity improves.",
            "Test whether volume growth comes from biological efficiency or simple herd expansion.",
        ),
        FilingQuestion(
            "hog_slaughter_mix",
            "mix",
            "屠宰和肉食业务是在抬升利润池，还是仍只是规模补充？",
            ("屠宰", "肉食", "屠宰量", "鲜品", "冻品"),
            ("semiannual", "annual"),
            "Identify whether downstream integration is becoming a real second curve.",
            "Keep adjacent businesses out of core valuation until margins and utilization are disclosed.",
        ),
        FilingQuestion(
            "hog_hedging",
            "risk",
            "期货套保、饲料采购和库存安排是在平滑利润，还是在放大周期判断风险？",
            ("期货", "套期保值", "饲料", "原料采购", "库存"),
            ("quarterly", "semiannual", "annual"),
            "Recognize prudent cycle management when disclosure supports it.",
            "Stress mark-to-market, basis, and procurement timing risk.",
        ),
    ),
    "livestock_hog": (
        (
            "cycle_position",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析", "季度经营分析"),
            ("生猪价格", "仔猪价格", "猪粮比", "完全成本", "养殖成本"),
            "Where is the company in the hog cycle after cost?",
            "Livestock equities are priced off price-cost spread, not volume alone.",
            "official livestock data + earnings model",
        ),
        (
            "breeding_productivity",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("能繁母猪", "PSY", "仔猪", "种猪", "出栏量"),
            "Is biological efficiency improving faster than herd size?",
            "Separates enduring operating advantage from simple cyclical beta.",
            "filing evidence + peer comparison",
        ),
        (
            "slaughter_mix",
            ("主营业务分析", "经营情况讨论与分析", "公司未来发展的展望", "未来发展展望"),
            ("屠宰", "肉食", "鲜品", "冻品", "产能利用率"),
            "Has downstream integration become a real profit pool?",
            "Promotes true second curves while keeping adjacency claims disciplined.",
            "thematic catalysts + valuation",
        ),
    ),
    "environmental_services": (
        (
            "order_quality",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("新增订单", "在手订单", "中标", "项目", "毛利率"),
            "Are new projects profitable growth or low-quality backlog?",
            "Separates headline wins from contract economics.",
            "policy planning + investor interactions",
        ),
        (
            "receivable_risk",
            ("主要会计数据和财务指标发生变动的情况及原因", "主营业务分析"),
            ("应收账款", "合同资产", "回款", "政府客户"),
            "Is project revenue turning into cash?",
            "Catches the classic municipal-project trap early.",
            "cash flow + shareholder risk",
        ),
    ),
    "banking": (
        (
            "asset_quality",
            ("经营情况讨论及分析", "经营情况讨论与分析", "季度经营分析"),
            ("不良贷款率", "关注类贷款", "拨备覆盖率", "逾期贷款", "迁徙率"),
            "Is credit quality genuinely improving or merely delayed?",
            "Credit cost often dominates apparent earnings smoothness.",
            "macro risk + investor interactions",
        ),
        (
            "spread_and_mix",
            ("经营情况讨论及分析", "经营情况讨论与分析", "季度经营分析"),
            ("净息差", "贷款收益率", "存款成本率", "手续费", "财富管理", "零售"),
            "Can mix offset spread pressure?",
            "Separates scale growth from quality of earnings.",
            "market expectation + peer comparison",
        ),
    ),
    "shipping": (
        (
            "freight_cycle",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("运价", "TCE", "租船", "航线", "运力利用率"),
            "Is the company positioned for the right part of the freight cycle?",
            "Shipping returns hinge on price, not just tonnage.",
            "shipping context + market timing",
        ),
        (
            "fleet_discipline",
            ("主营业务分析", "公司未来发展的展望", "未来发展展望"),
            ("船队", "订单簿", "新造船", "资本开支", "长协", "现货"),
            "Is management compounding through the cycle or buying the top?",
            "Prevents cycle extrapolation from becoming capital-allocation blindness.",
            "earnings model + capital allocation",
        ),
    ),
    "software_services": (
        (
            "recurring_revenue",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("订阅", "续费", "云收入", "合同负债", "ARR"),
            "Is growth becoming more recurring and visible?",
            "Distinguishes durable software economics from one-off projects.",
            "investor interactions + valuation",
        ),
        (
            "product_monetization",
            ("主营业务分析", "公司未来发展的展望", "未来发展展望"),
            ("AI", "人工智能", "新产品", "大客户", "商业化", "客户导入"),
            "Has product innovation become monetized?",
            "Stops concept rerating from outrunning cash economics.",
            "thematic catalysts + policy planning",
        ),
    ),
    "metals_mining": (
        (
            "reserve_and_volume",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("资源储量", "矿石品位", "权益产量", "金属量", "达产", "采选"),
            "Are reserves and volume extending the earnings runway?",
            "Separates commodity beta from asset quality.",
            "commodity context + policy planning",
        ),
        (
            "price_cost_leverage",
            ("主营业务分析", "主要会计数据和财务指标发生变动的情况及原因"),
            ("铜价", "铝价", "金价", "锂价", "单位成本", "完全成本", "冶炼加工费"),
            "Are realized prices outrunning unit costs?",
            "Determines whether macro upside becomes shareholder earnings.",
            "commodity context + earnings model",
        ),
    ),
    "lithium_battery": (
        (
            "utilization_and_volume",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("产能", "产能利用率", "出货量", "动力电池", "储能电池", "GWh"),
            "Is volume growth repairing utilization or just feeding overcapacity?",
            "Separates revenue rebound from true operating leverage.",
            "commodity context + peer comparison",
        ),
        (
            "technology_and_mix",
            ("主营业务分析", "核心竞争力分析", "公司未来发展的展望", "未来发展展望"),
            ("固态电池", "快充", "高镍", "储能", "客户", "量产"),
            "Which technology bets are commercially real?",
            "Bridges innovation claims with future profit pools.",
            "thematic catalysts + investor interactions",
        ),
    ),
    "baijiu": (
        (
            "channel_health",
            ("主营业务分析", "经营情况讨论与分析", "经营情况讨论及分析"),
            ("批价", "渠道库存", "经销商", "回款", "合同负债", "预收款"),
            "Is demand healthy, or is the channel being stuffed?",
            "The channel is the earliest truth serum in baijiu.",
            "investor interactions + market expectation",
        ),
        (
            "premiumization",
            ("主营业务分析", "公司未来发展的展望", "未来发展展望"),
            ("高端", "次高端", "吨价", "产品结构", "核心单品", "省外"),
            "Is brand strength translating into better mix?",
            "Separates genuine premiumization from price illusion.",
            "peer comparison + valuation",
        ),
    ),
    "airlines": (
        (
            "traffic_and_yield",
            ("经营情况讨论与分析", "经营情况讨论及分析", "季度经营分析"),
            ("ASK", "RPK", "客座率", "客公里收益", "国际航线", "旅客周转量"),
            "Are traffic and yield recovering together?",
            "Airline profits need both volume and price.",
            "shipping context + market timing",
        ),
        (
            "fuel_fx_balance",
            ("经营情况讨论与分析", "经营情况讨论及分析", "季度经营分析"),
            ("航油", "汇率", "租赁负债", "美元负债", "燃油成本"),
            "Are exogenous headwinds easing or merely hidden?",
            "Prevents headline recovery from masking macro fragility.",
            "macro risk + earnings model",
        ),
    ),
    "insurance": (
        (
            "franchise_recovery",
            ("经营情况讨论及分析", "季度经营分析"),
            ("新业务价值", "新单保费", "首年保费", "代理人", "人均产能"),
            "Is franchise recovery visible in value, not just premium?",
            "New-business value is the cleanest bridge to future earnings power.",
            "market expectation + investor interactions",
        ),
        (
            "investment_spread",
            ("经营情况讨论及分析", "季度经营分析"),
            ("投资收益率", "净投资收益率", "综合投资收益率", "内含价值", "资产配置"),
            "Can reinvestment support profit and EV?",
            "Insurance quality depends on spread durability, not premium optics alone.",
            "market timing + portfolio context",
        ),
        (
            "service_ecosystem",
            ("经营情况讨论及分析", "未来发展展望"),
            ("医疗养老", "居家养老", "康养", "医养服务", "第二增长曲线"),
            "Is service attachment strengthening the franchise?",
            "Captures genuine ecosystem economics beyond headline insurance sales.",
            "thematic catalysts + policy planning",
        ),
    ),
}


def _build_report_to_report_bridge(
    report_texts: Iterable[tuple[str, str]],
) -> list[ReportBridgeFinding]:
    reports = list(report_texts)
    rows: list[ReportBridgeFinding] = []
    long_cycle = [(title, text) for title, text in reports if _detect_report_type(title) in {"annual", "semiannual"}]
    checkpoints = [(title, text) for title, text in reports if _detect_report_type(title) == "quarterly"]
    for topic, keywords, analyst_read in _REPORT_BRIDGE_TOPICS:
        line_filter = _is_company_owned_growth_line if topic == "growth_vectors" else None
        long_match = _first_matching_line(
            long_cycle,
            keywords,
            ("annual", "semiannual"),
            line_filter=line_filter,
        )
        checkpoint_match = _first_matching_line(checkpoints, keywords, ("quarterly",))
        if long_match is None and checkpoint_match is None:
            continue
        if long_match is not None and checkpoint_match is not None:
            status = "checkpoint-available"
        elif long_match is not None:
            status = "awaiting-short-cycle-check"
        else:
            status = "short-cycle-signal-without-long-cycle-anchor"
        bridge_read = _interpret_report_bridge(topic, long_match, checkpoint_match)
        rows.append(
            ReportBridgeFinding(
                topic=topic,
                long_cycle_evidence=long_match[1] if long_match else "",
                checkpoint_evidence=checkpoint_match[1] if checkpoint_match else "",
                bridge_status=status,
                bridge_read=bridge_read,
                analyst_read=analyst_read,
            )
        )
    return rows


_WEAKENING_TOKENS: dict[str, tuple[str, ...]] = {
    "pricing_and_margin": ("下降", "承压", "减少", "低于", "恶化"),
    "cash_conversion": ("下降", "减少", "净流出", "增加", "恶化"),
}

_CONFIRMING_TOKENS: dict[str, tuple[str, ...]] = {
    "orders_and_visibility": ("增长", "增加", "在手订单", "合同负债"),
    "pricing_and_margin": ("提升", "增长", "改善", "回升"),
    "cash_conversion": ("改善", "增加", "净流入", "转正"),
    "growth_vectors": ("签订", "投产", "实现收入", "订单", "客户"),
    "capital_intensity": ("投产", "产能", "订单", "实现收入"),
}


def _interpret_report_bridge(
    topic: str,
    long_match: tuple[str, str] | None,
    checkpoint_match: tuple[str, str] | None,
) -> str:
    if long_match is not None and checkpoint_match is None:
        return "awaiting-evidence"
    if long_match is None and checkpoint_match is not None:
        return "new-short-cycle-signal"
    if long_match is None or checkpoint_match is None:
        return "no-bridge"

    checkpoint_text = checkpoint_match[1]
    if any(token in checkpoint_text for token in _WEAKENING_TOKENS.get(topic, ())):
        return "weakened"
    if any(token in checkpoint_text for token in _CONFIRMING_TOKENS.get(topic, ())):
        return "confirmed"
    return "checkpoint-present-but-indeterminate"



_TEXTUAL_PROOF_TOKENS = (
    "\u5df2\u5b9e\u73b0\u6536\u5165",
    "\u5b9e\u73b0\u6536\u5165",
    "\u786e\u8ba4\u6536\u5165",
    "\u5df2\u4ea4\u4ed8",
    "\u5df2\u6295\u4ea7",
    "\u91cf\u4ea7",
    "\u4e2d\u6807",
    "\u7b7e\u8ba2",
    "\u5408\u540c",
    "\u8ba2\u5355",
    "\u5ba2\u6237",
)
_TEXTUAL_EXECUTION_TOKENS = (
    "\u5df2\u5b8c\u6210",
    "\u5b8c\u6210\u5efa\u8bbe",
    "\u8bd5\u751f\u4ea7",
    "\u8bd5\u8fd0\u884c",
    "\u4ea7\u80fd\u91ca\u653e",
    "\u8fbe\u4ea7",
    "\u843d\u5730",
    "\u5b9e\u65bd",
)
_TEXTUAL_SOFT_TOKENS = (
    "\u63a8\u8fdb",
    "\u52a0\u5feb",
    "\u5e03\u5c40",
    "\u89c4\u5212",
    "\u62df",
    "\u5c06",
    "\u529b\u4e89",
    "\u63a2\u7d22",
    "\u50a8\u5907",
    "\u79ef\u6781",
    "\u6301\u7eed",
)
_TEXTUAL_RISK_TOKENS = (
    "\u4e0d\u786e\u5b9a",
    "\u98ce\u9669",
    "\u538b\u529b",
    "\u4e0b\u6ed1",
    "\u4e0b\u964d",
    "\u4e8f\u635f",
    "\u51cf\u503c",
    "\u8bc9\u8bbc",
    "\u5904\u7f5a",
    "\u7acb\u6848",
    "\u91cd\u5927\u4e0d\u5229",
)
_TEXTUAL_STRATEGY_TOKENS = (
    "\u65b0\u4e1a\u52a1",
    "\u65b0\u4ea7\u54c1",
    "\u7b2c\u4e8c\u589e\u957f",
    "\u8f6c\u578b",
    "\u6570\u5b57\u5316",
    "\u667a\u80fd",
    "\u6d77\u5916",
    "\u4ea7\u4e1a\u94fe",
    "\u5546\u4e1a\u5316",
    "\u4ea7\u80fd",
)


def _textual_wording_stage(text: str) -> str:
    if any(token in text for token in _TEXTUAL_RISK_TOKENS):
        return "risk-language"
    if any(token in text for token in _TEXTUAL_PROOF_TOKENS):
        return "proof-backed"
    if any(token in text for token in _TEXTUAL_EXECUTION_TOKENS):
        return "execution-stage"
    if any(token in text for token in _TEXTUAL_SOFT_TOKENS):
        return "soft-intention"
    return "neutral"


def _textual_signal_score(text: str, report_type: str, stage: str) -> int:
    score = {"proof-backed": 5, "risk-language": 5, "execution-stage": 4, "soft-intention": 2}.get(stage, 0)
    if re.search(r"\d", text):
        score += 2
    if report_type == "annual":
        score += 1
    if any(token in text for token in _TEXTUAL_STRATEGY_TOKENS):
        score += 1
    return score


def _extract_textual_filing_signals(
    report_texts: Iterable[tuple[str, str]],
    report_bridge: Iterable[ReportBridgeFinding] = (),
    growth_vectors: Iterable[GrowthVectorFinding] = (),
    limit: int = 10,
) -> list[FilingTextSignal]:
    """Read management language, not just accounting numbers."""

    ranked: list[tuple[int, FilingTextSignal]] = []
    seen: set[tuple[str, str]] = set()
    for title, text in report_texts:
        report_type = _detect_report_type(title)
        for unit in _iter_filing_text_units(text, limit=320):
            repaired = _repair_mojibake(unit)
            stage = _textual_wording_stage(repaired)
            if stage == "neutral":
                continue
            if stage == "soft-intention" and not any(token in repaired for token in _TEXTUAL_STRATEGY_TOKENS):
                continue
            signal_type = {
                "proof-backed": "management_claim_with_evidence",
                "execution-stage": "execution_progress_language",
                "soft-intention": "soft_strategy_language",
                "risk-language": "risk_language_upgrade",
            }[stage]
            if stage == "soft-intention" and not re.search(r"\d", repaired):
                signal_type = "unquantified_strategy_language"
            key = (signal_type, repaired[:160])
            if key in seen:
                continue
            seen.add(key)
            investment_read = {
                "management_claim_with_evidence": "Management language has a harder evidence bridge; debate materiality and economics rather than existence.",
                "execution_progress_language": "The company is describing implementation progress; test whether execution reaches revenue, margin, or cash flow.",
                "soft_strategy_language": "The company is still using intention/planning language; keep it below base-case valuation until proof appears.",
                "unquantified_strategy_language": "Strategic wording is not yet quantified; useful for questions, weak for valuation.",
                "risk_language_upgrade": "Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant.",
            }[signal_type]
            ranked.append(
                (
                    _textual_signal_score(repaired, report_type, stage),
                    FilingTextSignal(
                        signal_type=signal_type,
                        report_type=report_type,
                        wording_stage=stage,
                        evidence=f"{title}: {repaired}",
                        investment_read=investment_read,
                        bull_use="Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion.",
                        bear_use="Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation.",
                    ),
                )
            )

    for vector in growth_vectors:
        if vector.stage in {"planned", "capacity-building"}:
            key = ("watch_missing_monetization", vector.vector)
            if key in seen:
                continue
            seen.add(key)
            ranked.append(
                (
                    3,
                    FilingTextSignal(
                        signal_type="watch_missing_monetization",
                        report_type="annual/semiannual",
                        wording_stage="missing-proof",
                        evidence=vector.evidence,
                        investment_read="The filing describes a possible growth vector, but monetization evidence is still incomplete.",
                        bull_use="Use as a diligence agenda or scenario option, not a base-case valuation driver.",
                        bear_use="Ask why the company has not disclosed revenue, margin, customers, delivery, or cash evidence yet.",
                    ),
                )
            )

    for bridge in report_bridge:
        if bridge.bridge_read == "awaiting-evidence":
            key = ("abnormal_silence_or_missing_update", bridge.topic)
            if key in seen:
                continue
            seen.add(key)
            ranked.append(
                (
                    4,
                    FilingTextSignal(
                        signal_type="abnormal_silence_or_missing_update",
                        report_type="cross-report",
                        wording_stage="missing-update",
                        evidence=f"{bridge.long_cycle_evidence} || {bridge.checkpoint_evidence}",
                        investment_read="A long-cycle narrative lacks short-cycle confirmation; silence or missing update is itself a research signal.",
                        bull_use="Treat as pending proof rather than confirmed progress.",
                        bear_use="Use as evidence that the story has not yet survived the next reporting checkpoint.",
                    ),
                )
            )

    selected: list[FilingTextSignal] = []
    per_type: dict[str, int] = {}
    for _, row in sorted(ranked, key=lambda item: item[0], reverse=True):
        if per_type.get(row.signal_type, 0) >= 2:
            continue
        selected.append(row)
        per_type[row.signal_type] = per_type.get(row.signal_type, 0) + 1
        if len(selected) >= limit:
            break
    return selected

def _extract_deep_reading_excerpts(
    report_texts: Iterable[tuple[str, str]],
    max_sections_per_report_type: int = 4,
    max_chars: int = 900,
) -> list[FilingExcerpt]:
    rows: list[FilingExcerpt] = []
    used_by_type: dict[str, int] = {}
    for title, text in report_texts:
        report_type = _detect_report_type(title)
        rules = _DEEP_READING_SECTION_RULES.get(report_type, ())
        if not rules:
            continue
        lines = [_compact_text(line, limit=260) for line in str(text or "").splitlines()]
        for section, reading_purpose in rules:
            if used_by_type.get(report_type, 0) >= max_sections_per_report_type:
                break
            for idx, line in enumerate(lines):
                if not line or section not in line:
                    continue
                window: list[str] = []
                for candidate in lines[idx : idx + 10]:
                    if candidate:
                        window.append(candidate)
                    if sum(len(item) for item in window) >= max_chars:
                        break
                excerpt = " ".join(window)[:max_chars]
                if not excerpt:
                    continue
                rows.append(
                    FilingExcerpt(
                        report_type=report_type,
                        section=section,
                        excerpt=f"{title}: {excerpt}",
                        reading_purpose=reading_purpose,
                    )
                )
                used_by_type[report_type] = used_by_type.get(report_type, 0) + 1
                break
    return rows


def _section_windows(
    text: str,
    section: str,
    max_chars: int = 1400,
) -> list[str]:
    lines = [_compact_text(line, limit=320) for line in str(text or "").splitlines()]
    known_sections = {
        section
        for rules in _DEEP_READING_SECTION_RULES.values()
        for section, _ in rules
    }
    windows: list[str] = []
    for idx, line in enumerate(lines):
        if not line or section not in line:
            continue
        window: list[str] = []
        for candidate in lines[idx : idx + 18]:
            if (
                candidate
                and candidate != line
                and candidate in known_sections
            ):
                break
            if candidate:
                window.append(candidate)
            if sum(len(item) for item in window) >= max_chars:
                break
        excerpt = " ".join(window)[:max_chars]
        if excerpt:
            windows.append(excerpt)
    return windows


def _section_window(
    text: str,
    section: str,
    max_chars: int = 1400,
) -> str:
    windows = _section_windows(text, section, max_chars=max_chars)
    if not windows:
        return ""
    return max(windows, key=len)


def _paragraph_score(excerpt: str, keywords: tuple[str, ...]) -> int:
    score = sum(1 for keyword in keywords if keyword in excerpt)
    if _evidence_strength(excerpt) == "quantified disclosure":
        score += 2
    if len(excerpt) >= 120:
        score += 1
    return score


def _build_paragraph_reading_pack(
    report_texts: Iterable[tuple[str, str]],
) -> list[FilingParagraphInsight]:
    reports = list(report_texts)
    rows: list[FilingParagraphInsight] = []
    for report_type, rules in _PARAGRAPH_READING_LENSES.items():
        typed_reports = [
            (title, text)
            for title, text in reports
            if _detect_report_type(title) == report_type
        ]
        for lens, sections, keywords, reading_question, why_it_matters in rules:
            candidates: list[tuple[int, FilingParagraphInsight]] = []
            for title, text in typed_reports:
                for section in sections:
                    for excerpt in _section_windows(text, section):
                        if not excerpt or not any(keyword in excerpt for keyword in keywords):
                            continue
                        score = _paragraph_score(excerpt, keywords)
                        candidates.append(
                            (
                                score,
                                FilingParagraphInsight(
                                    lens=lens,
                                    report_type=report_type,
                                    section=section,
                                    excerpt=f"{title}: {excerpt}",
                                    reading_question=reading_question,
                                    why_it_matters=why_it_matters,
                                ),
                            )
                        )
            if candidates:
                rows.append(max(candidates, key=lambda item: item[0])[1])
    return rows


def _build_industry_reading_pack(
    report_texts: Iterable[tuple[str, str]],
    profile: str,
) -> list[IndustryReadingInsight]:
    reports = list(report_texts)
    rules = _INDUSTRY_PARAGRAPH_LENSES.get(profile, ())
    rows: list[IndustryReadingInsight] = []
    for lens, sections, keywords, reading_question, why_it_matters, connect_to in rules:
        candidates: list[tuple[int, IndustryReadingInsight]] = []
        for title, text in reports:
            report_type = _detect_report_type(title)
            for section in sections:
                for excerpt in _section_windows(text, section):
                    if not excerpt or not any(keyword in excerpt for keyword in keywords):
                        continue
                    score = _paragraph_score(excerpt, keywords)
                    if report_type == "annual":
                        score += 2
                    elif report_type == "semiannual":
                        score += 1
                    candidates.append(
                        (
                            score,
                            IndustryReadingInsight(
                                lens=lens,
                                report_type=report_type,
                                section=section,
                                excerpt=f"{title}: {excerpt}",
                                reading_question=reading_question,
                                why_it_matters=why_it_matters,
                                connect_to=connect_to,
                            ),
                        )
                    )
        if candidates:
            rows.append(max(candidates, key=lambda item: item[0])[1])
    return rows

def _question_candidates(profile: str) -> tuple[FilingQuestion, ...]:
    if profile == "banking":
        return _INDUSTRY_PLAYBOOKS.get(profile, ())
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
            for line in _iter_filing_text_units(text, limit=240):
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


_BANKING_KPI_RULES: tuple[tuple[str, tuple[str, ...], str, str], ...] = (
    (
        "spread_profitability",
        ("净息差", "净利差", "净利息收益率", "生息资产收益率", "贷款收益率", "存款成本率"),
        "NIM is the main earnings transmission belt for a bank; do not infer spread stabilization from revenue alone.",
        "Require the actual spread/yield/cost disclosure before calling an earnings inflection.",
    ),
    (
        "asset_quality",
        ("不良贷款率", "不良贷款余额", "关注类贷款", "逾期贷款", "迁徙率", "信用成本", "拨备覆盖率", "贷款拨备率"),
        "Asset-quality direction decides whether low PB is value or a trap.",
        "Look for early deterioration in special-mention, overdue, migration, and reserve metrics before NPLs rise.",
    ),
    (
        "capital_and_payout",
        ("核心一级资本充足率", "一级资本充足率", "资本充足率", "风险加权资产", "分红率", "现金分红"),
        "Capital adequacy links growth, dividends, and downside resilience.",
        "Do not recommend aggressive growth or payout unless CET1/RWA evidence supports it.",
    ),
    (
        "retail_wealth_engine",
        ("管理零售客户总资产", "AUM", "零售客户", "财富管理", "手续费及佣金", "代理基金", "托管规模"),
        "Retail AUM matters only when it converts into durable fee income and deposit stickiness.",
        "Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression.",
    ),
    (
        "loan_deposit_mix",
        ("客户贷款", "客户存款", "活期存款", "零售贷款", "公司贷款", "房地产贷款", "信用卡贷款", "消费贷款"),
        "Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet.",
        "Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking.",
    ),
)


def _extract_banking_kpi_pack(
    report_texts: Iterable[tuple[str, str]],
    max_per_lens: int = 4,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    counts: dict[str, int] = {}
    for title, text in report_texts:
        report_type = _detect_report_type(title)
        for unit in _iter_filing_text_units(text, limit=320):
            if not unit:
                continue
            for lens, keywords, why_it_matters, bear_check in _BANKING_KPI_RULES:
                if counts.get(lens, 0) >= max_per_lens:
                    continue
                if not _line_contains_any(unit, keywords):
                    continue
                strength = _evidence_strength(unit)
                if strength != "quantified disclosure" and counts.get(lens, 0) >= 1:
                    continue
                key = (lens, unit)
                if key in seen:
                    continue
                seen.add(key)
                counts[lens] = counts.get(lens, 0) + 1
                rows.append(
                    {
                        "lens": lens,
                        "report_type": report_type,
                        "evidence_strength": strength,
                        "filing_evidence": f"{title}: {_compact_text(unit, 260)}",
                        "why_it_matters": why_it_matters,
                        "bear_check": bear_check,
                    }
                )
    return rows


def _extract_statement_table_signals(
    report_texts: Iterable[tuple[str, str]],
    max_per_account: int = 2,
) -> list[FilingTableSignal]:
    """Read key balance-sheet / cash-flow rows from layout-preserved filing text."""

    rows: list[FilingTableSignal] = []
    seen_count: dict[str, int] = {}
    for title, text in report_texts:
        report_type = _detect_report_type(title)
        for unit in _iter_filing_text_units(text, limit=260):
            if len(_TABLE_NUMBER_RE.findall(unit)) < 2:
                continue
            for account, aliases, why_it_matters, bull_use, bear_use in _TABLE_ACCOUNT_RULES:
                if seen_count.get(account, 0) >= max_per_account:
                    continue
                if not any(alias in unit for alias in aliases):
                    continue
                rows.append(
                    FilingTableSignal(
                        account=account,
                        report_type=report_type,
                        evidence=f"{title}: {unit}",
                        why_it_matters=why_it_matters,
                        bull_use=bull_use,
                        bear_use=bear_use,
                    )
                )
                seen_count[account] = seen_count.get(account, 0) + 1
    return rows


def _extract_note_findings(
    report_texts: Iterable[tuple[str, str]],
    max_per_type: int = 2,
) -> list[FilingNoteFinding]:
    """Surface decision-relevant filing notes and footnote risks."""

    rows: list[FilingNoteFinding] = []
    seen_count: dict[str, int] = {}
    for title, text in report_texts:
        for unit in _iter_filing_text_units(text, limit=280):
            if not unit:
                continue
            for (
                note_type,
                importance,
                keywords,
                why_it_matters,
                bull_use,
                bear_use,
            ) in _NOTE_FINDING_RULES:
                if seen_count.get(note_type, 0) >= max_per_type:
                    continue
                if not any(keyword in unit for keyword in keywords):
                    continue
                rows.append(
                    FilingNoteFinding(
                        note_type=note_type,
                        importance=importance,
                        evidence=f"{title}: {unit}",
                        why_it_matters=why_it_matters,
                        bull_use=bull_use,
                        bear_use=bear_use,
                    )
                )
                seen_count[note_type] = seen_count.get(note_type, 0) + 1
    return rows


def _metric_value(row: pd.Series, column: str) -> float | None:
    value = pd.to_numeric(pd.Series([row.get(column)]), errors="coerce").iloc[0]
    return None if pd.isna(value) else float(value)


def _pct_change(curr: float | None, prev: float | None) -> float | None:
    if curr is None or prev is None or prev == 0:
        return None
    return (curr / prev - 1.0) * 100.0


def _pp_change(curr: float | None, prev: float | None) -> float | None:
    if curr is None or prev is None:
        return None
    return curr - prev


def _fmt(value: float | None, suffix: str = "") -> str:
    return "N/A" if value is None else f"{value:.2f}{suffix}"


def _infer_financial_relations(
    derived: pd.DataFrame | TushareDataError,
    limit: int = 8,
) -> list[FinancialRelationInsight]:
    """Infer a small set of high-value relationships across the three statements."""

    if isinstance(derived, TushareDataError) or derived is None or len(derived) < 2:
        return []

    ordered = derived.copy()
    ordered["end_date"] = ordered["end_date"].astype(str)
    ordered = ordered.sort_values("end_date", ascending=False)
    latest = ordered.iloc[0]
    prev = ordered.iloc[1]

    revenue_growth = _pct_change(
        _metric_value(latest, "revenue_base"),
        _metric_value(prev, "revenue_base"),
    )
    gross_margin_change = _pp_change(
        _metric_value(latest, "reported_gross_margin"),
        _metric_value(prev, "reported_gross_margin"),
    )
    operating_margin_change = _pp_change(
        _metric_value(latest, "derived_operating_margin"),
        _metric_value(prev, "derived_operating_margin"),
    )
    net_margin_change = _pp_change(
        _metric_value(latest, "derived_net_margin"),
        _metric_value(prev, "derived_net_margin"),
    )
    ocf_to_profit = _metric_value(latest, "ocf_to_net_profit")
    receivables_ratio_change = _pp_change(
        _metric_value(latest, "receivables_to_revenue"),
        _metric_value(prev, "receivables_to_revenue"),
    )
    inventory_ratio_change = _pp_change(
        _metric_value(latest, "inventory_to_revenue"),
        _metric_value(prev, "inventory_to_revenue"),
    )
    prepayment_ratio_change = _pp_change(
        _metric_value(latest, "prepayment_to_revenue"),
        _metric_value(prev, "prepayment_to_revenue"),
    )
    contract_liab_change = _pct_change(
        _metric_value(latest, "contract_like_liab"),
        _metric_value(prev, "contract_like_liab"),
    )
    debt_ratio_change = _pp_change(
        _metric_value(latest, "debt_to_assets_derived"),
        _metric_value(prev, "debt_to_assets_derived"),
    )
    finance_ratio_change = _pp_change(
        _metric_value(latest, "finance_expense_ratio"),
        _metric_value(prev, "finance_expense_ratio"),
    )

    latest_period = str(latest.get("end_date") or "latest")
    prev_period = str(prev.get("end_date") or "prior")
    insights: list[FinancialRelationInsight] = []

    def add(
        relation_type: str,
        importance: str,
        investment_read: str,
        bull_use: str,
        bear_use: str,
    ) -> None:
        evidence = (
            f"{prev_period}->{latest_period}: revenue growth {_fmt(revenue_growth, '%')}, "
            f"gross margin change {_fmt(gross_margin_change, 'pp')}, "
            f"operating margin change {_fmt(operating_margin_change, 'pp')}, "
            f"OCF/net profit {_fmt(ocf_to_profit)}, "
            f"receivables/revenue change {_fmt(receivables_ratio_change, 'pp')}, "
            f"inventory/revenue change {_fmt(inventory_ratio_change, 'pp')}, "
            f"prepayment/revenue change {_fmt(prepayment_ratio_change, 'pp')}, "
            f"contract-like liabilities growth {_fmt(contract_liab_change, '%')}, "
            f"debt/assets change {_fmt(debt_ratio_change, 'pp')}, "
            f"finance-expense ratio change {_fmt(finance_ratio_change, 'pp')}."
        )
        insights.append(
            FinancialRelationInsight(
                relation_type=relation_type,
                importance=importance,
                evidence=evidence,
                investment_read=investment_read,
                bull_use=bull_use,
                bear_use=bear_use,
            )
        )

    # Revenue growth is only valuable if it survives margin and cash tests.
    if (
        revenue_growth is not None
        and revenue_growth > 10
        and gross_margin_change is not None
        and gross_margin_change < -1
    ):
        add(
            "growth_without_margin",
            "high",
            "Top-line growth is not yet translating into better unit economics; volume may be outrunning pricing, mix, or cost absorption.",
            "Argue the thesis only if future filings show the margin drag is temporary and tied to a known mix/timing issue.",
            "Use as evidence that growth quality is weaker than the revenue line suggests.",
        )

    if (
        revenue_growth is not None
        and revenue_growth > 10
        and ocf_to_profit is not None
        and ocf_to_profit < 0.8
        and (
            (receivables_ratio_change is not None and receivables_ratio_change > 3)
            or (inventory_ratio_change is not None and inventory_ratio_change > 3)
            or (prepayment_ratio_change is not None and prepayment_ratio_change > 2)
        )
    ):
        add(
            "cash_absorbing_growth",
            "high",
            "Reported growth is being financed by working capital rather than self-funding cash conversion.",
            "Treat as acceptable only if filings show contracted demand, healthy collections, and a credible release path.",
            "Use to challenge whether earnings are being bought with cash and balance-sheet stretch.",
        )

    if (
        contract_liab_change is not None
        and contract_liab_change > 15
        and gross_margin_change is not None
        and gross_margin_change <= 0
    ):
        add(
            "visibility_not_yet_profitability",
            "high",
            "Demand visibility improved, but the accounts do not yet prove that the backlog is becoming more profitable.",
            "Use contract-liability growth as visibility support, not as proof of better pricing until margins follow.",
            "Attack any attempt to equate prepayments with high-quality earnings before margin confirmation arrives.",
        )

    if (
        gross_margin_change is not None
        and gross_margin_change > 1
        and operating_margin_change is not None
        and operating_margin_change < gross_margin_change - 1
    ):
        add(
            "gross_margin_not_reaching_operating_profit",
            "supporting",
            "Gross-margin improvement is being absorbed below the gross-profit line, so operating leverage is weaker than the headline margin suggests.",
            "Use only if temporary spending can be linked to future monetization.",
            "Use to challenge whether product/mix improvement is truly flowing through to earnings.",
        )

    if (
        debt_ratio_change is not None
        and debt_ratio_change > 2
        and finance_ratio_change is not None
        and finance_ratio_change > 0.3
    ):
        add(
            "leverage_funding_growth",
            "supporting",
            "The balance sheet is taking more of the burden for current growth, and financing cost is beginning to reflect it.",
            "Use only if return on invested capital clearly exceeds the added funding cost.",
            "Use to challenge the durability of growth and the risk of future earnings drag.",
        )

    if (
        revenue_growth is not None
        and revenue_growth > 10
        and gross_margin_change is not None
        and gross_margin_change > 0
        and ocf_to_profit is not None
        and ocf_to_profit >= 1
    ):
        add(
            "quality_growth",
            "high",
            "Revenue, margin, and cash conversion are moving together; this is the cleanest form of operating improvement.",
            "Use as the strongest filing-backed support for an upgrade in thesis confidence.",
            "Ask whether the improvement is cyclical, one-off, or already priced.",
        )

    if (
        net_margin_change is not None
        and gross_margin_change is not None
        and net_margin_change > 1
        and gross_margin_change < 0
    ):
        add(
            "below_gross_profit_help",
            "supporting",
            "Net margin improved despite weaker gross margin, implying the profit story may rely on below-gross-profit items rather than core economics.",
            "Use only after identifying durable operating expense or financing relief.",
            "Use to test whether profit improvement is lower quality than headline EPS suggests.",
        )

    priority_rank = {"high": 0, "supporting": 1}
    return sorted(insights, key=lambda item: (priority_rank.get(item.importance, 9), item.relation_type))[:limit]


def _audit_filing_coverage(
    report_texts: Iterable[tuple[str, str]],
    questions: Iterable[FilingQuestion],
    answers: Iterable[FilingQuestionAnswer],
    business_model_map: Iterable[BusinessModelFinding],
    paragraph_reading_pack: Iterable[FilingParagraphInsight],
    industry_reading_pack: Iterable[IndustryReadingInsight],
) -> FilingCoverageAudit:
    reports = list(report_texts)
    question_rows = list(questions)
    answer_rows = list(answers)
    report_types = tuple(
        sorted(
            {
                _detect_report_type(title)
                for title, _ in reports
                if _detect_report_type(title) != "unknown"
            }
        )
    )
    required_types = ("annual", "semiannual", "quarterly")
    missing_types = tuple(item for item in required_types if item not in report_types)

    business_model_count = len(list(business_model_map))
    paragraph_count = len(list(paragraph_reading_pack))
    industry_count = len(list(industry_reading_pack))
    answered_count = len(answer_rows)
    total_count = len(question_rows)

    if not reports:
        return FilingCoverageAudit(
            coverage_grade="text_unavailable",
            report_types_seen=(),
            missing_report_types=required_types,
            answered_question_count=0,
            total_question_count=total_count,
            core_pack_status="unavailable",
            confidence_read=(
                "Narrative filing text was not readable, so business-model, segment, "
                "and management-discussion evidence is unavailable. This does not by "
                "itself mean structured financial statements, market data, or peer "
                "data failed."
            ),
        )

    answer_ratio = answered_count / total_count if total_count else 0.0
    has_long_cycle = "annual" in report_types
    has_checkpoint = "quarterly" in report_types
    has_structural_bridge = "semiannual" in report_types
    core_pack_ready = (
        business_model_count >= 3
        and paragraph_count >= 3
        and (industry_count >= 2 or not industry_count)
    )

    if has_long_cycle and has_checkpoint and answer_ratio >= 0.6 and core_pack_ready:
        grade = "strong"
        confidence = (
            "Annual base text and quarterly checkpoint are both present, with broad "
            "question coverage; filing read is suitable for thesis formation."
        )
    elif (has_long_cycle or has_structural_bridge) and answer_ratio >= 0.35:
        grade = "partial"
        confidence = (
            "Readable filings exist, but either cross-period coverage or answer density "
            "is incomplete; use findings, but keep verification burden visible."
        )
    else:
        grade = "weak"
        confidence = (
            "Readable text exists but the pack is too thin for a full buy-side read; "
            "avoid strong claims about business model, second curve, or execution trend."
        )

    return FilingCoverageAudit(
        coverage_grade=grade,
        report_types_seen=report_types,
        missing_report_types=missing_types,
        answered_question_count=answered_count,
        total_question_count=total_count,
        core_pack_status="ready" if core_pack_ready else "thin",
        confidence_read=confidence,
    )


def _promote_core_discussion_items(
    material_findings: Iterable[MaterialFilingFinding],
    growth_vectors: Iterable[GrowthVectorFinding],
    answers: Iterable[FilingQuestionAnswer],
    report_bridge: Iterable[ReportBridgeFinding],
    statement_table_signals: Iterable[FilingTableSignal] = (),
    note_findings: Iterable[FilingNoteFinding] = (),
    financial_relations: Iterable[FinancialRelationInsight] = (),
    limit: int = 10,
) -> list[CoreDiscussionItem]:
    """Promote filing discoveries that can genuinely alter an investment thesis."""

    items: list[CoreDiscussionItem] = []
    seen: set[tuple[str, str]] = set()

    for finding in material_findings:
        priority = "core"
        key = ("material", finding.finding_type)
        if key in seen:
            continue
        seen.add(key)
        items.append(
            CoreDiscussionItem(
                topic=finding.finding_type,
                priority=priority,
                evidence_basis=finding.evidence,
                why_it_matters=finding.investment_read,
                valuation_treatment="core debate candidate",
                verification_need=finding.bear_use,
            )
        )

    for vector in growth_vectors:
        if vector.stage in {"monetized", "contracted"}:
            priority = "core"
        elif vector.stage == "capacity-building":
            priority = "scenario"
        else:
            priority = "watch"
        key = ("growth", vector.vector)
        if key in seen:
            continue
        seen.add(key)
        items.append(
            CoreDiscussionItem(
                topic=vector.vector,
                priority=priority,
                evidence_basis=vector.evidence,
                why_it_matters=f"Growth vector currently reads as {vector.stage}.",
                valuation_treatment=vector.valuation_treatment,
                verification_need=vector.verification_need,
            )
        )

    core_categories = {
        "revenue_quality",
        "profit_quality",
        "cash_quality",
        "orders",
        "pricing",
        "mix",
        "asset_quality",
        "profitability",
    }
    for answer in answers:
        if answer.category not in core_categories:
            continue
        if answer.evidence_strength not in {"quantified disclosure", "explicit disclosure"}:
            continue
        key = ("answer", answer.question_id)
        if key in seen:
            continue
        seen.add(key)
        priority = "core" if answer.evidence_strength == "quantified disclosure" else "supporting"
        items.append(
            CoreDiscussionItem(
                topic=answer.question_id,
                priority=priority,
                evidence_basis=answer.evidence,
                why_it_matters=f"Direct filing answer for {answer.category}.",
                valuation_treatment="core debate candidate",
                verification_need=answer.bear_use,
            )
        )

    for bridge in report_bridge:
        if bridge.bridge_read not in {"confirmed", "weakened"}:
            continue
        key = ("bridge", bridge.topic)
        if key in seen:
            continue
        seen.add(key)
        items.append(
            CoreDiscussionItem(
                topic=f"{bridge.topic}:{bridge.bridge_read}",
                priority="core",
                evidence_basis=(
                    f"{bridge.long_cycle_evidence} || {bridge.checkpoint_evidence}"
                ),
                why_it_matters=bridge.analyst_read,
                valuation_treatment="changes thesis confidence",
                verification_need="Check whether the next report continues or reverses this bridge.",
            )
        )

    core_table_accounts = {
        "contract_liabilities",
        "receivables",
        "inventory",
        "operating_cash_flow",
        "impairment",
        "long_term_equity_investments",
    }
    for signal in statement_table_signals:
        key = ("table", signal.account)
        if key in seen:
            continue
        seen.add(key)
        items.append(
            CoreDiscussionItem(
                topic=signal.account,
                priority="core" if signal.account in core_table_accounts else "supporting",
                evidence_basis=signal.evidence,
                why_it_matters=signal.why_it_matters,
                valuation_treatment="core debate candidate",
                verification_need=signal.bear_use,
            )
        )

    for note in note_findings:
        key = ("note", note.note_type)
        if key in seen:
            continue
        seen.add(key)
        items.append(
            CoreDiscussionItem(
                topic=note.note_type,
                priority="core" if note.importance == "high" else "supporting",
                evidence_basis=note.evidence,
                why_it_matters=note.why_it_matters,
                valuation_treatment="risk/governance modifier",
                verification_need=note.bear_use,
            )
        )

    for relation in financial_relations:
        key = ("relation", relation.relation_type)
        if key in seen:
            continue
        seen.add(key)
        items.append(
            CoreDiscussionItem(
                topic=relation.relation_type,
                priority="core" if relation.importance == "high" else "supporting",
                evidence_basis=relation.evidence,
                why_it_matters=relation.investment_read,
                valuation_treatment="financial-relation thesis modifier",
                verification_need=relation.bear_use,
            )
        )

    priority_rank = {"core": 0, "supporting": 1, "scenario": 2, "watch": 3}
    return sorted(items, key=lambda item: (priority_rank.get(item.priority, 9), item.topic))[:limit]


def _distill_filing_insights(
    company_name: str,
    coverage_audit: FilingCoverageAudit,
    business_model_map: Iterable[BusinessModelFinding],
    growth_vectors: Iterable[GrowthVectorFinding],
    answers: Iterable[FilingQuestionAnswer],
    statement_table_signals: Iterable[FilingTableSignal] = (),
    note_findings: Iterable[FilingNoteFinding] = (),
    financial_relations: Iterable[FinancialRelationInsight] = (),
    promoted_items: Iterable[CoreDiscussionItem] = (),
    textual_signals: Iterable[FilingTextSignal] = (),
    limit: int = 8,
) -> list[FilingInsight]:
    """Compress the filing read into buy-side insights instead of raw snippets.

    This layer is deliberately industry-agnostic. Industry playbooks decide which
    operating questions to ask; this layer decides which answers should become a
    research memo's central argument.
    """

    insights: list[FilingInsight] = []
    seen: set[str] = set()

    def add(
        insight_type: str,
        analyst_question: str,
        distilled_read: str,
        evidence_basis: str,
        debate_use: str,
        what_would_change_mind: str,
    ) -> None:
        if insight_type in seen or not evidence_basis:
            return
        seen.add(insight_type)
        insights.append(
            FilingInsight(
                insight_type=insight_type,
                analyst_question=analyst_question,
                distilled_read=distilled_read,
                evidence_basis=evidence_basis,
                debate_use=debate_use,
                what_would_change_mind=what_would_change_mind,
            )
        )

    business_rows = list(business_model_map)
    vector_rows = list(growth_vectors)
    answer_rows = list(answers)
    table_rows = list(statement_table_signals)
    note_rows = list(note_findings)
    relation_rows = list(financial_relations)
    promoted_rows = list(promoted_items)
    text_rows = list(textual_signals)

    core_engine = next((row for row in business_rows if row.lens == "core_revenue_engine"), None)
    if core_engine:
        add(
            "core_business_engine",
            "What actually drives this company's revenue and profit pool?",
            (
                "Start the memo from the operating engine disclosed in filings, "
                "not from market labels, hot themes, or valuation screens."
            ),
            core_engine.evidence,
            "Forces bulls and bears to debate the real business before discussing optionality.",
            "A segment disclosure or order/customer evidence showing a different profit engine has become material.",
        )

    contracted_or_monetized = [
        row for row in vector_rows if row.stage in {"monetized", "contracted", "capacity-building"}
    ]
    if contracted_or_monetized:
        vector = sorted(
            contracted_or_monetized,
            key=lambda row: {"monetized": 0, "contracted": 1, "capacity-building": 2}.get(row.stage, 9),
        )[0]
        if vector.stage == "monetized":
            read = "The filing contains a monetized growth vector; it deserves an earnings-bridge test, not just a narrative mention."
            change = "Segment revenue, margin, recurrence, and cash collection either confirm scale or reveal it is immaterial."
        elif vector.stage == "contracted":
            read = "The filing contains a contracted growth vector; the key is not whether the story exists, but whether contract size and economics matter."
            change = "Disclosed contract value, delivery schedule, gross margin, customer concentration, and cash conversion."
        else:
            read = "The filing contains capacity-building optionality; it should enter scenarios only after utilization and return path become visible."
            change = "Commissioning, utilization, customer offtake, and ROIC evidence."
        add(
            "second_curve_or_inflection_claim",
            "Is there a credible second curve or operating inflection hidden in filings?",
            read,
            vector.evidence,
            "Bulls must quantify the bridge; bears must test scale, timing, margin, and whether it is already priced.",
            change,
        )

    negative_relations = {
        "growth_without_margin",
        "cash_absorbing_growth",
        "visibility_not_yet_profitability",
        "below_gross_profit_help",
        "leverage_funding_growth",
    }
    relation = next((row for row in relation_rows if row.relation_type in negative_relations), None)
    if relation:
        add(
            "quality_of_growth_tension",
            "Does reported growth improve owner economics, or merely consume capital?",
            relation.investment_read,
            relation.evidence,
            "This should become a central bull/bear clash: growth deserves credit only if margin, cash conversion, and balance-sheet burden improve together.",
            "Next report shows revenue growth with stable/rising margin, positive operating cash flow, and no worsening receivables/inventory/prepayments.",
        )

    quality_relation = next((row for row in relation_rows if row.relation_type == "quality_growth"), None)
    if quality_relation:
        add(
            "quality_growth_confirmation",
            "Is the company showing clean, investable operating improvement?",
            quality_relation.investment_read,
            quality_relation.evidence,
            "Bulls can use this as high-quality proof; bears should ask whether it is cyclical, one-off, or already priced.",
            "A reversal in margin, operating cash flow, or working-capital intensity.",
        )

    if vector_rows and not quality_relation:
        vector = vector_rows[0]
        add(
            "monetization_gap",
            "What is the gap between the story and the income statement?",
            (
                "The filing has a growth narrative, but the system has not found enough clean "
                "financial confirmation to treat it as a base-case valuation driver."
            ),
            vector.evidence,
            "Keeps the report from either ignoring the story or overpaying for it; use it as scenario evidence until economics are proven.",
            "Quantified revenue/profit contribution, repeat orders, cash collection, and segment margin evidence.",
        )

    capex_signal = next(
        (
            row
            for row in table_rows
            if row.account
            in {"capex", "construction_in_progress", "long_term_equity_investments", "investment_assets"}
        ),
        None,
    )
    if capex_signal:
        add(
            "capital_allocation_checkpoint",
            "Is management turning reinvestment into future earnings power?",
            capex_signal.why_it_matters,
            capex_signal.evidence,
            "Bulls must show reinvestment creates capacity, orders, or NAV; bears can attack trapped capital and weak ROIC.",
            "Visible utilization, monetization, disposal gains, ROIC uplift, or impairment/disposal losses.",
        )

    tail_note = next(
        (
            row
            for row in note_rows
            if row.note_type in {"litigation", "guarantees", "related_party", "customer_concentration"}
            or row.importance == "high"
        ),
        None,
    )
    if tail_note:
        add(
            "governance_or_tail_risk",
            "Is there a footnote risk that changes the equity story?",
            tail_note.why_it_matters,
            tail_note.evidence,
            "Use as a thesis modifier: it can cap valuation even when operating momentum looks acceptable.",
            "Resolution, quantified liability, customer diversification, related-party cleanup, or explicit non-materiality evidence.",
        )

    strong_text = next(
        (
            row
            for row in text_rows
            if row.signal_type
            in {
                "management_claim_with_evidence",
                "execution_progress_language",
                "risk_language_upgrade",
                "unquantified_strategy_language",
                "abnormal_silence_or_missing_update",
            }
        ),
        None,
    )
    if strong_text:
        add(
            "textual_filing_signal",
            "What is management language trying to prove, soften, or avoid?",
            strong_text.investment_read,
            strong_text.evidence,
            "Use wording as a debate input: hard wording must still clear materiality; soft wording needs proof; risk wording can cap valuation.",
            strong_text.bear_use,
        )

    core_item = next((row for row in promoted_rows if row.priority == "core"), None)
    if core_item:
        add(
            "core_debate_item",
            "Which filing-derived point must enter the bull/bear debate?",
            core_item.why_it_matters,
            core_item.evidence_basis,
            "Do not leave this as background context; make it one of the main debate pillars.",
            core_item.verification_need,
        )

    if coverage_audit.coverage_grade in {"weak", "failed", "text_unavailable"}:
        add(
            "filing_read_confidence_gap",
            "Can we trust a strong conclusion from the available filings?",
            coverage_audit.confidence_read,
            f"Coverage: {coverage_audit.coverage_grade}; reports seen: {'/'.join(coverage_audit.report_types_seen) or 'none'}",
            "Cap conviction and explicitly name missing report types or unanswered thesis-critical questions.",
            "Retrieve annual/semiannual/quarterly text and answer the core playbook with quantified evidence.",
        )

    priority = {
        "core_business_engine": 0,
        "quality_of_growth_tension": 1,
        "quality_growth_confirmation": 1,
        "second_curve_or_inflection_claim": 2,
        "monetization_gap": 3,
        "capital_allocation_checkpoint": 4,
        "governance_or_tail_risk": 5,
        "textual_filing_signal": 6,
        "core_debate_item": 7,
        "filing_read_confidence_gap": 8,
    }
    return sorted(insights, key=lambda row: priority.get(row.insight_type, 99))[:limit]


def _build_internal_filing_quality_modules(
    coverage_audit: FilingCoverageAudit,
    statement_table_signals: Iterable[FilingTableSignal] = (),
    note_findings: Iterable[FilingNoteFinding] = (),
    financial_relations: Iterable[FinancialRelationInsight] = (),
    segment_economics: Iterable[SegmentEconomicsFinding] = (),
    business_segment_valuation_map: Iterable[BusinessSegmentValuationFinding] = (),
    growth_vectors: Iterable[GrowthVectorFinding] = (),
    report_bridge: Iterable[ReportBridgeFinding] = (),
    textual_signals: Iterable[FilingTextSignal] = (),
    answers: Iterable[FilingQuestionAnswer] = (),
    banking_kpi_pack: Iterable[dict[str, str]] = (),
) -> list[FilingInternalQualityModule]:
    """Synthesize ten filing-only review modules from already extracted evidence."""

    table_rows = list(statement_table_signals)
    note_rows = list(note_findings)
    relation_rows = list(financial_relations)
    segment_rows = list(segment_economics)
    valuation_rows = list(business_segment_valuation_map)
    vector_rows = list(growth_vectors)
    bridge_rows = list(report_bridge)
    text_rows = list(textual_signals)
    answer_rows = list(answers)
    bank_rows = list(banking_kpi_pack)

    def evidence_or_gap(evidence: str | None, gap: str) -> tuple[str, str]:
        if evidence:
            return _compact_text(evidence, 260), gap
        return "Not enough direct filing evidence found in the readable report pack.", gap

    def table_evidence(accounts: set[str]) -> str | None:
        parts = [
            f"{row.account}: {row.evidence}"
            for row in table_rows
            if row.account in accounts
        ]
        return " | ".join(parts[:2]) or None

    def note_evidence(types: set[str] | None = None) -> str | None:
        parts = [
            f"{row.note_type}: {row.evidence}"
            for row in note_rows
            if types is None or row.note_type in types
        ]
        return " | ".join(parts[:2]) or None

    def answer_evidence(categories: set[str]) -> str | None:
        parts = [
            f"{row.question_id}: {row.evidence}"
            for row in answer_rows
            if row.category in categories
        ]
        return " | ".join(parts[:2]) or None

    def relation_evidence(types: set[str] | None = None) -> str | None:
        parts = [
            f"{row.relation_type}: {row.evidence}"
            for row in relation_rows
            if types is None or row.relation_type in types
        ]
        return " | ".join(parts[:2]) or None

    modules: list[FilingInternalQualityModule] = []

    def add(
        module: str,
        purpose: str,
        evidence: str | None,
        analyst_use: str,
        missing_or_next_check: str,
    ) -> None:
        evidence_text, next_check = evidence_or_gap(evidence, missing_or_next_check)
        modules.append(
            FilingInternalQualityModule(
                module=module,
                purpose=purpose,
                evidence=evidence_text,
                analyst_use=analyst_use,
                missing_or_next_check=next_check,
            )
        )

    accounting_evidence = (
        relation_evidence()
        or table_evidence(
            {
                "operating_cash_flow",
                "receivables",
                "inventory",
                "prepayments",
                "contract_liabilities",
                "impairment",
            }
        )
        or (" | ".join(str(row) for row in bank_rows[:2]) if bank_rows else None)
    )
    add(
        "accounting_reconciliation",
        "Check signs, units, periods, and cross-statement consistency before a number enters the PM memo.",
        accounting_evidence,
        "Use as the report's source-of-truth layer; flag conflicting cash-flow, profit, leverage, or period claims instead of averaging narratives.",
        "If debate numbers conflict, cite the exact filing period and reconcile revenue, profit, OCF, working capital, and leverage before rating impact.",
    )

    segment_evidence = " | ".join(
        [row.evidence for row in segment_rows[:2]]
        + [row.evidence for row in valuation_rows[:2]]
    )
    add(
        "segment_economics_depth",
        "Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment.",
        segment_evidence or None,
        "Core segments can support base-case value; thin or header-only second curves stay in SOTP/scenario value.",
        "Require revenue, cost/gross margin, profit or cash-quality evidence by product, channel, geography, or business bucket.",
    )

    add(
        "footnote_radar",
        "Surface decision-relevant notes that can hide risk or change confidence.",
        note_evidence(),
        "Use footnotes as valuation modifiers for customer concentration, related parties, guarantees, litigation, impairment, and capitalization choices.",
        "If note evidence is thin, avoid claiming footnote cleanliness; keep guarantees, litigation, impairment assumptions, and related parties on the checklist.",
    )

    cash_evidence = (
        relation_evidence(
            {
                "cash_absorbing_growth",
                "quality_growth",
                "growth_without_margin",
                "visibility_not_yet_profitability",
                "below_gross_profit_help",
            }
        )
        or table_evidence(
            {
                "operating_cash_flow",
                "receivables",
                "inventory",
                "prepayments",
                "contract_liabilities",
            }
        )
        or answer_evidence({"cash_quality", "revenue_quality", "profit_quality"})
    )
    add(
        "cash_flow_quality_decomposition",
        "Separate accounting profit from cash conversion, working-capital drag, and demand visibility.",
        cash_evidence,
        "Upgrade growth only when revenue, margin, OCF, receivables, inventory, and contract liabilities point in the same direction.",
        "Next filing should confirm OCF/net profit, collections, inventory turns, and whether contract liabilities convert at acceptable margin.",
    )

    capex_evidence = (
        table_evidence(
            {
                "capex",
                "construction_in_progress",
                "fixed_assets",
                "long_term_equity_investments",
                "investment_assets",
            }
        )
        or " | ".join(row.evidence for row in vector_rows if row.stage == "capacity-building")[:520]
        or answer_evidence({"capital_allocation"})
    )
    add(
        "capex_cip_return_bridge",
        "Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital.",
        capex_evidence or None,
        "Put projects with unclear utilization, payback, or ROIC in scenario value; require demand and margin evidence before base-case valuation credit.",
        "Track commissioning, utilization or occupancy, capex-to-revenue, payback/ROIC, impairment, and disposal gains or losses.",
    )

    mdna_evidence = (
        " | ".join(f"{row.signal_type}: {row.evidence}" for row in text_rows[:2])
        or " | ".join(
            f"{row.topic}: {row.long_cycle_evidence} -> {row.checkpoint_evidence}"
            for row in bridge_rows[:2]
        )
    )
    add(
        "mdna_text_change",
        "Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports.",
        mdna_evidence or None,
        "Use text changes to decide whether management is proving, softening, or avoiding a theme; do not let soft wording replace hard evidence.",
        "Compare the next quarterly MD&A against annual/semiannual promises, especially on strategy, project ramp, risks, and cash conversion.",
    )

    non_recurring_evidence = (
        table_evidence({"impairment", "investment_assets"})
        or answer_evidence({"profit_quality"})
        or note_evidence({"impairment", "capitalization_policy", "fair_value", "government_subsidy"})
    )
    add(
        "non_recurring_profit_quality",
        "Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items.",
        non_recurring_evidence,
        "Use this to prevent headline EPS from receiving a core multiple when profit quality depends on non-operating or non-recurring items.",
        "Require a bridge from gross profit/operating profit to net profit, and isolate investment income, fair-value gains, subsidies, disposals, and impairments.",
    )

    balance_sheet_evidence = table_evidence(
        {
            "contract_liabilities",
            "receivables",
            "inventory",
            "prepayments",
            "payables",
            "capex",
            "construction_in_progress",
            "debt",
        }
    ) or relation_evidence({"cash_absorbing_growth", "visibility_not_yet_profitability", "leverage_funding_growth"})
    add(
        "balance_sheet_forward_signals",
        "Read balance-sheet leads before income-statement confirmation.",
        balance_sheet_evidence,
        "Contract liabilities and payables can signal demand/funding; receivables, inventory, prepayments, debt, and CIP can signal execution burden.",
        "Track whether leading assets/liabilities convert into revenue, margin, and cash rather than reversals, impairments, or financing drag.",
    )

    shareholder_return_evidence = (
        note_evidence({"dividend", "shareholder_return", "buyback", "capital_allocation"})
        or answer_evidence({"capital_allocation"})
        or (" | ".join(str(row) for row in bank_rows if "payout" in str(row).lower())[:520] or None)
    )
    add(
        "shareholder_return_authenticity",
        "Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales.",
        shareholder_return_evidence,
        "Treat shareholder yield as quality only when payout, FCF/OCF coverage, leverage, capex needs, and dilution risk line up.",
        "Verify dividend payout, buyback execution/cancellation, FCF coverage, leverage movement, and whether capital needs crowd out future returns.",
    )

    disclosure_evidence = (
        f"Coverage grade {coverage_audit.coverage_grade}; reports seen "
        f"{'/'.join(coverage_audit.report_types_seen) or 'none'}; answered "
        f"{coverage_audit.answered_question_count}/{coverage_audit.total_question_count}; "
        f"core pack {coverage_audit.core_pack_status}. {coverage_audit.confidence_read}"
    )
    add(
        "disclosure_quality_score",
        "Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view.",
        disclosure_evidence,
        "High disclosure quality raises conviction; weak or partial coverage should cap sizing and push more assumptions into verification.",
        "Improve confidence by retrieving missing annual/semiannual/quarterly text and answering unanswered thesis-critical filing questions.",
    )

    return modules


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
    try:
        _question_memory_path(symbol).write_text(
            json.dumps(memory, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except PermissionError:
        # A live CLI run or antivirus scanner can briefly lock this tiny memory
        # file on Windows. The filing context itself is still usable, so avoid
        # failing the whole precompute stage just because the learning cache
        # could not be updated.
        pass
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


_RUNTIME_READING_KEYWORDS = (
    "主营",
    "业务",
    "收入",
    "利润",
    "毛利",
    "毛利率",
    "现金流",
    "经营活动",
    "订单",
    "合同",
    "客户",
    "库存",
    "存货",
    "应收",
    "预付款",
    "产能",
    "利用率",
    "研发",
    "费用",
    "减值",
    "商誉",
    "风险",
    "诉讼",
    "担保",
    "关联",
    "分红",
    "回购",
    "净息差",
    "净利差",
    "净利息收益率",
    "生息资产",
    "贷款收益率",
    "存款成本率",
    "不良贷款率",
    "关注类贷款",
    "逾期贷款",
    "迁徙率",
    "拨备覆盖率",
    "贷款拨备率",
    "资本充足率",
    "核心一级资本",
    "风险加权资产",
    "客户存款",
    "客户贷款",
    "零售贷款",
    "财富管理",
    "手续费",
    "AUM",
    "电池",
    "汽车",
    "新能源",
    "海外",
    "出口",
    "market",
    "revenue",
    "profit",
    "margin",
    "cash flow",
    "order",
    "inventory",
    "capacity",
    "customer",
    "risk",
)


def _compact_report_text_for_runtime(
    title: str,
    text: str,
    *,
    max_chars: int,
) -> str:
    """Keep high-signal windows from a large filing text for rule extractors."""
    if len(text) <= max_chars:
        return text

    head_budget = max(30_000, int(max_chars * 0.28))
    tail_budget = max(20_000, int(max_chars * 0.16))
    keyword_budget = max_chars - head_budget - tail_budget - 500
    keyword_lines: list[str] = []
    keyword_chars = 0
    seen: set[str] = set()

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped in seen:
            continue
        lowered = stripped.lower()
        if not any(token in lowered or token in stripped for token in _RUNTIME_READING_KEYWORDS):
            continue
        seen.add(stripped)
        if len(stripped) > 500:
            stripped = stripped[:480].rstrip() + " ... [line trimmed]"
        keyword_lines.append(stripped)
        keyword_chars += len(stripped) + 1
        if keyword_chars >= keyword_budget:
            break

    return "\n".join(
        [
            f"[Runtime-compacted filing text for {title}: original {len(text)} chars, budget {max_chars} chars.]",
            "",
            "[Opening slice]",
            text[:head_budget],
            "",
            "[Keyword evidence lines]",
            "\n".join(keyword_lines) if keyword_lines else "(none detected)",
            "",
            "[Ending slice]",
            text[-tail_budget:],
        ]
    )


def _compact_report_texts_for_runtime(
    report_texts: Iterable[tuple[str, str]],
) -> tuple[list[tuple[str, str]], str]:
    config = get_config()
    per_report_limit = int(config.get("filing_intelligence_max_chars_per_report", 180_000))
    total_limit = int(config.get("filing_intelligence_max_total_chars", 420_000))

    compacted: list[tuple[str, str]] = []
    notes: list[str] = []
    total = 0
    for title, text in report_texts:
        remaining = total_limit - total
        if remaining <= 0:
            notes.append(f"- Skipped {title}: runtime text budget exhausted.")
            break
        budget = min(per_report_limit, remaining)
        new_text = _compact_report_text_for_runtime(title, text or "", max_chars=budget)
        compacted.append((title, new_text))
        total += len(new_text)
        if len(text or "") > len(new_text):
            notes.append(
                f"- Compacted {title}: {len(text or '')} chars -> {len(new_text)} chars."
            )
    return compacted, "\n".join(notes)


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
    report_texts, runtime_compaction_note = _compact_report_texts_for_runtime(report_texts)
    income = _fetch_income_statement_data(symbol, curr_date, freq="quarterly", limit=8)
    balance = _fetch_balance_sheet_data(symbol, curr_date, freq="quarterly", limit=8)
    cashflow = _fetch_cashflow_data(symbol, curr_date, freq="quarterly", limit=8)
    indicators = _fetch_fina_indicator(symbol, curr_date)
    derived_metrics = _derive_financial_metrics(income, balance, cashflow, indicators)
    profile = (
        "banking"
        if is_banking_entity(symbol, basic=basic, company_name=company_name, industry=industry)
        else _select_industry_profile(company_name, industry, report_texts)
    )
    evidence = _extract_filing_evidence(
        report_texts,
        rules=_BANKING_SIGNAL_RULES if profile == "banking" else _FILING_SIGNAL_RULES,
    )
    material_findings = _extract_material_filing_findings(report_texts)
    segment_economics = _extract_segment_economics(report_texts)
    business_model_map = _build_business_model_map(report_texts)
    growth_vectors = _extract_growth_vectors(report_texts)
    business_segment_valuation_map = _build_business_segment_valuation_map(
        business_model_map=business_model_map,
        segment_economics=segment_economics,
        growth_vectors=growth_vectors,
    )
    report_bridge = _build_report_to_report_bridge(report_texts)
    textual_signals = _extract_textual_filing_signals(
        report_texts,
        report_bridge=report_bridge,
        growth_vectors=growth_vectors,
    )
    deep_reading_excerpts = _extract_deep_reading_excerpts(report_texts)
    paragraph_reading_pack = _build_paragraph_reading_pack(report_texts)
    industry_reading_pack = _build_industry_reading_pack(report_texts, profile)
    banking_kpi_pack = _extract_banking_kpi_pack(report_texts) if profile == "banking" else []
    statement_table_signals = [] if profile == "banking" else _extract_statement_table_signals(report_texts)
    note_findings = _extract_note_findings(report_texts)
    financial_relations = [] if profile == "banking" else _infer_financial_relations(derived_metrics)
    questions = _question_candidates(profile)
    answers = _answer_questions(report_texts, questions)
    coverage_audit = _audit_filing_coverage(
        report_texts=report_texts,
        questions=questions,
        answers=answers,
        business_model_map=business_model_map,
        paragraph_reading_pack=paragraph_reading_pack,
        industry_reading_pack=industry_reading_pack,
    )
    promoted_items = _promote_core_discussion_items(
        material_findings=material_findings,
        growth_vectors=growth_vectors,
        answers=answers,
        report_bridge=report_bridge,
        statement_table_signals=statement_table_signals,
        note_findings=note_findings,
        financial_relations=financial_relations,
    )
    distilled_insights = _distill_filing_insights(
        company_name=company_name,
        coverage_audit=coverage_audit,
        business_model_map=business_model_map,
        growth_vectors=growth_vectors,
        answers=answers,
        statement_table_signals=statement_table_signals,
        note_findings=note_findings,
        financial_relations=financial_relations,
        promoted_items=promoted_items,
        textual_signals=textual_signals,
    )
    internal_quality_modules = _build_internal_filing_quality_modules(
        coverage_audit=coverage_audit,
        statement_table_signals=statement_table_signals,
        note_findings=note_findings,
        financial_relations=financial_relations,
        segment_economics=segment_economics,
        business_segment_valuation_map=business_segment_valuation_map,
        growth_vectors=growth_vectors,
        report_bridge=report_bridge,
        textual_signals=textual_signals,
        answers=answers,
        banking_kpi_pack=banking_kpi_pack,
    )
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
    material_rows = [
        {
            "finding_type": item.finding_type,
            "importance": item.importance,
            "filing_evidence": _compact_text(item.evidence, 180),
            "investment_read": item.investment_read,
            "bull_use": item.bull_use,
            "bear_use": item.bear_use,
        }
        for item in material_findings
    ]
    segment_rows = [
        {
            "segment_type": item.segment_type,
            "report_type": item.report_type,
            "filing_evidence": _compact_text(item.evidence, 240),
            "analyst_use": item.analyst_use,
        }
        for item in segment_economics
    ]
    business_model_rows = [
        {
            "lens": item.lens,
            "report_type": item.report_type,
            "filing_evidence": _compact_text(item.evidence, 180),
            "why_it_matters": item.why_it_matters,
        }
        for item in business_model_map
    ]
    growth_vector_rows = [
        {
            "vector": item.vector,
            "stage": item.stage,
            "filing_evidence": _compact_text(item.evidence, 180),
            "valuation_treatment": item.valuation_treatment,
            "verification_need": item.verification_need,
        }
        for item in growth_vectors
    ]
    business_segment_valuation_rows = [
        {
            "business_bucket": item.business_bucket,
            "report_type": item.report_type,
            "filing_evidence": _compact_text(item.evidence, 220),
            "valuation_anchor": item.valuation_anchor,
            "analyst_use": item.analyst_use,
            "verification_need": item.verification_need,
        }
        for item in business_segment_valuation_map
    ]
    report_bridge_rows = [
        {
            "topic": item.topic,
            "long_cycle_evidence": _compact_text(item.long_cycle_evidence, 140),
            "checkpoint_evidence": _compact_text(item.checkpoint_evidence, 140),
            "bridge_status": item.bridge_status,
            "bridge_read": item.bridge_read,
            "analyst_read": item.analyst_read,
        }
        for item in report_bridge
    ]
    excerpt_rows = [
        {
            "report_type": item.report_type,
            "section": item.section,
            "excerpt": _compact_text(item.excerpt, 320),
            "reading_purpose": item.reading_purpose,
        }
        for item in deep_reading_excerpts
    ]
    paragraph_rows = [
        {
            "lens": item.lens,
            "report_type": item.report_type,
            "section": item.section,
            "reading_question": item.reading_question,
            "paragraph_excerpt": _compact_text(item.excerpt, 420),
            "why_it_matters": item.why_it_matters,
        }
        for item in paragraph_reading_pack
    ]
    industry_rows = [
        {
            "lens": item.lens,
            "report_type": item.report_type,
            "section": item.section,
            "reading_question": item.reading_question,
            "paragraph_excerpt": _compact_text(item.excerpt, 420),
            "why_it_matters": item.why_it_matters,
            "connect_to": item.connect_to,
        }
        for item in industry_reading_pack
    ]
    banking_kpi_rows = banking_kpi_pack
    statement_table_rows = [
        {
            "account": item.account,
            "report_type": item.report_type,
            "table_evidence": _compact_text(item.evidence, 180),
            "why_it_matters": item.why_it_matters,
            "bull_use": item.bull_use,
            "bear_use": item.bear_use,
        }
        for item in statement_table_signals
    ]
    note_rows = [
        {
            "note_type": item.note_type,
            "importance": item.importance,
            "note_evidence": _compact_text(item.evidence, 180),
            "why_it_matters": item.why_it_matters,
            "bull_use": item.bull_use,
            "bear_use": item.bear_use,
        }
        for item in note_findings
    ]
    relation_rows = [
        {
            "relation_type": item.relation_type,
            "importance": item.importance,
            "evidence": item.evidence,
            "investment_read": item.investment_read,
            "bull_use": item.bull_use,
            "bear_use": item.bear_use,
        }
        for item in financial_relations
    ]
    textual_rows = [
        {
            "signal_type": item.signal_type,
            "report_type": item.report_type,
            "wording_stage": item.wording_stage,
            "textual_evidence": _compact_text(item.evidence, 240),
            "investment_read": item.investment_read,
            "bull_use": item.bull_use,
            "bear_use": item.bear_use,
        }
        for item in textual_signals
    ]
    coverage_rows = [
        {
            "coverage_grade": coverage_audit.coverage_grade,
            "report_types_seen": "/".join(coverage_audit.report_types_seen) or "none",
            "missing_report_types": "/".join(coverage_audit.missing_report_types) or "none",
            "answered_questions": f"{coverage_audit.answered_question_count}/{coverage_audit.total_question_count}",
            "core_pack_status": coverage_audit.core_pack_status,
            "confidence_read": coverage_audit.confidence_read,
        }
    ]
    promoted_rows = [
        {
            "topic": item.topic,
            "priority": item.priority,
            "evidence_basis": _compact_text(item.evidence_basis, 180),
            "why_it_matters": item.why_it_matters,
            "valuation_treatment": item.valuation_treatment,
            "verification_need": item.verification_need,
        }
        for item in promoted_items
    ]
    distilled_rows = [
        {
            "insight_type": item.insight_type,
            "analyst_question": item.analyst_question,
            "distilled_read": item.distilled_read,
            "evidence_basis": _compact_text(item.evidence_basis, 220),
            "debate_use": item.debate_use,
            "what_would_change_mind": item.what_would_change_mind,
        }
        for item in distilled_insights
    ]
    internal_quality_rows = [
        {
            "module": item.module,
            "purpose": item.purpose,
            "filing_evidence": item.evidence,
            "analyst_use": item.analyst_use,
            "missing_or_next_check": item.missing_or_next_check,
        }
        for item in internal_quality_modules
    ]
    answered_ids = {answer.question_id for answer in answers}
    unanswered_rows = [
        {
            "question_id": question.question_id,
            "category": question.category,
            "question": question.question,
            "why_it_matters": f"Still unresolved in the latest readable filings; {question.bear_use}",
        }
        for question in questions
        if question.question_id not in answered_ids
    ]

    extraction_note = (
        "Financial-report text extraction succeeded."
        if report_texts
        else (
            "Narrative filing text extraction unavailable: no readable annual, "
            "semiannual, or quarterly report body was retrieved. Treat this as a "
            "filing-text/segment-evidence gap, not as proof that structured "
            "financial statements failed."
        )
    )

    lines = [
        f"# Financial-report intelligence for {symbol} as of {curr_date}",
        "",
        f"- Company: {company_name}",
        f"- Vendor industry: {industry}",
        f"- Reading profile: {profile}",
        "- Research hygiene: industry-specific playbooks are conservative by design; if identity is ambiguous, generic questions are safer than a wrong template.",
        f"- Financial-report look-back: {look_back_days} days",
        f"- Extraction status: {extraction_note}",
        *(["- Runtime compaction applied to oversized filing text.", runtime_compaction_note] if runtime_compaction_note else []),
        "",
        "## Financial Reports Considered",
        *report_titles,
        "",
        "## Filing Reading Coverage Audit",
        _build_table(coverage_rows),
        "",
        "## Internal Filing Quality Modules",
        _build_table(internal_quality_rows),
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
        "## Business Model Map",
        _build_table(business_model_rows),
        "",
        "## Segment Economics Pack",
        _build_table(segment_rows),
        "",
        "## Business Segment Valuation Map",
        _build_table(business_segment_valuation_rows),
        "",
        "## Growth Vector Map",
        _build_table(growth_vector_rows),
        "",
        "## Deep Reading Excerpts",
        _build_table(excerpt_rows),
        "",
        "## Paragraph Reading Pack",
        _build_table(paragraph_rows),
        "",
        "## Industry Reading Pack",
        _build_table(industry_rows),
        "",
        "## Banking KPI Pack",
        _build_table(banking_kpi_rows),
        "",
        "## Statement Table Reading Pack",
        _build_table(statement_table_rows),
        "",
        "## Filing Note Reading Pack",
        _build_table(note_rows),
        "",
        "## Financial Relationship Reading Pack",
        _build_table(relation_rows),
        "",
        "## Filing Textual Signals",
        _build_table(textual_rows),
        "",
        "## Filing Insight Distillation Layer",
        _build_table(distilled_rows),
        "",
        "## Core Discussion Promotion Queue",
        _build_table(promoted_rows),
        "",
        "## Unanswered Filing Questions",
        _build_table(unanswered_rows),
        "",
        "## Question-Driven Filing Answers",
        _build_table(question_rows),
        "",
        "## Material Filing Findings",
        _build_table(material_rows),
        "",
        "## Report-to-Report Bridge",
        _build_table(report_bridge_rows),
        "",
        "## Company-Specific Watch Questions",
        _build_table(_memory_rows(memory)),
        "",
        "## Filing-Derived Operating Evidence",
        _build_table(evidence_rows),
        "",
        "## Analyst Instructions",
        "- Start with the filing reading coverage audit. If coverage is partial, weak, or failed, explicitly downgrade confidence before using any filing-derived thesis.",
        "- Use the Internal Filing Quality Modules as a ten-part filing-only review: accounting reconciliation, segment economics, footnote radar, cash-flow quality, capex/CIP return bridge, MD&A text change, non-recurring profit quality, balance-sheet forward signals, shareholder-return authenticity, and disclosure quality. The final PM memo should integrate these into PM Summary, Investment Thesis, Valuation, Risk, and Verification rather than dumping a checklist.",
        "- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.",
        "- Start with the business model map, then use the growth vector map to separate mature engines from emerging second curves.",
        "- For multi-product or multi-region companies, read the Segment Economics Pack before the bull/bear debate. Do not collapse a company into headline revenue or profit when annual/half-year filings disclose product, geography, channel, revenue, cost, gross margin, or growth-rate splits.",
        "- Use the Business Segment Valuation Map to build a split valuation before applying a blended multiple. Value mature/core businesses on normalized earnings, FCF, EV/EBITDA, PE, or peer-relative multiples; value emerging or second-curve businesses with SOTP/scenario treatment until segment revenue, margin, capex/utilization, customers, and cash conversion are proven.",
        "- For unfamiliar companies, first explain the main business from filings, then split the investment case into disclosed business buckets. Do not discuss new businesses as free optionality unless the map shows filing-backed monetization or a clear verification path.",
        "- Use the deep-reading excerpts as source text, not decorative context: annual-report excerpts define the company, semiannual excerpts test trend formation, and quarterly excerpts test short-cycle execution.",
        "- Use the paragraph reading pack for genuine report reading: answer the paragraph-level question first, then decide whether the business model, second curve, moat, trend, or cash-conversion thesis changed.",
        "- Use the industry reading pack as the specialist layer: the same filing should be read through the value drivers that matter for that business model, then linked to the external inputs named in `connect_to` before forming a conclusion.",
        "- Use the statement table reading pack for the hard-accounting layer: contract liabilities, receivables, inventory, prepayments, capex, investment assets, operating cash flow, and impairment rows often decide whether the narrative survives contact with the numbers.",
        "- Use the filing note reading pack for footnote discipline: customer concentration, related parties, guarantees, litigation, impairment assumptions, and capitalization policies often reveal risks that the headline statements hide.",
        "- Use the financial relationship reading pack to connect the statements rather than reading metrics in isolation. Revenue growth only deserves praise if margin, cash conversion, and balance-sheet demands make sense together.",
        "- Use the filing textual signals layer to read management wording strength, risk-language upgrades, abnormal silence, and strategic promises. Hard wording still needs materiality; soft wording belongs in scenarios/watchlist; risk wording can cap valuation. Keep a concise textual-signal module in the manager report when it changes the thesis.",
        "- Use the filing insight distillation layer before writing the final thesis. It converts raw filing snippets into buy-side questions: core engine, second curve, quality of growth, monetization gap, capital allocation, and tail risk. The manager report should read like a company memo, not a list of disconnected data points.",
        "- Start from the selected question playbook, then answer only with evidence actually found in filings.",
        "- For banks, start from the Banking KPI Pack and the banking playbook. Do not use contract liabilities, inventory, gross margin, capex, or generic OCF conversion as core bank-quality evidence unless a bank-specific disclosure explicitly makes them decision-relevant.",
        "- For banks, preserve the exact spread terminology from filings: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. If the filing only supports 净利差 1.77% and 净利息收益率 1.83%, do not invent or substitute a 1.40%/1.50% NIM number. Treat NIM stabilization as conditional until the next filing confirms spread, loan yield, and deposit-cost movement together.",
        "- Use the core discussion promotion queue as the bridge from reading to investing: core items should enter bull/bear debate, supporting items should reinforce or challenge a thesis, scenario items belong in upside/downside cases, and watch items stay out of base-case valuation until upgraded.",
        "- Treat unanswered filing questions as explicit research gaps, not neutral evidence. If a thesis depends on an unanswered question, reduce conviction or state what disclosure would close the gap.",
        "- Promote materially decision-relevant findings such as signed long-term agreements, named customers, take-or-pay/offtake signals, capacity-to-demand bridges, and commercialization milestones into the core debate rather than leaving them buried as generic snippets.",
        "- Use the report-to-report bridge to ask whether annual/semiannual narratives are being confirmed, weakened, or still waiting for quarterly proof.",
        "- Treat annual reports, half-year reports, and quarterly reports as a linked evidence chain: annual reports define the long-cycle thesis, half-year reports test trend formation, and quarterly reports confirm, weaken, or leave unresolved the latest checkpoint.",
        "- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.",
        "- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.",
        "- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.",
    ]
    return "\n".join(lines)
