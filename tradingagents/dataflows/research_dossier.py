"""Reader-led research dossier built from the validated structured bundle.

The raw research contexts are intentionally broad.  Agents should not write a
public report by walking those contexts one by one.  This module converts the
validated underwriting packet, deterministic evidence and Knowledge Planet
ledger into a compact research dossier that routes only decision-useful
objects into the seven reader-facing chapters.

The dossier is deterministic.  It does not invent facts, forecasts or source
credibility.  Its job is to decide *where* an already extracted object may be
used and to make Knowledge Planet transmission explicit: model input,
probability adjustment, verification item, or rejection.
"""

from __future__ import annotations

import json
import re
from typing import Any, Mapping


CHAPTERS: tuple[tuple[str, str, str], ...] = (
    (
        "chapter_1_company",
        "一、公司是谁、如何赚钱",
        "让普通投资者理解产品、客户、定价、收入确认、成本与现金回收。",
    ),
    (
        "chapter_2_industry_chain",
        "二、产业链位置与行业格局",
        "解释上下游、供需与价格形成，并把产业链变化传导到公司经营。",
    ),
    (
        "chapter_3_profit_pools",
        "三、业务拆解与核心利润池",
        "按核心、成长、波动和期权业务拆解收入、利润、现金与资本占用。",
    ),
    (
        "chapter_4_competition",
        "四、竞争优势、护城河与主要短板",
        "用历史或真同行验证规模、品牌、渠道、技术和成本优势。",
    ),
    (
        "chapter_5_growth_forecast",
        "五、增长逻辑、关键分歧与盈利预测",
        "围绕三至五个关键问题，把经营变量传导到三年盈利和现金流。",
    ),
    (
        "chapter_6_expectations",
        "六、市场预期差、风险与验证",
        "区分真实一致预期、单家卖方和反向隐含假设，并给出证伪日历。",
    ),
    (
        "chapter_7_valuation_rating",
        "七、估值、评级与投资结论",
        "在完成公司、产业、模型和预期分析后，最后给出估值、评级与动作。",
    ),
)


SOURCE_POLICY: dict[str, dict[str, str]] = {
    "A_hard_fact": {
        "sources": "公司财报、交易所/公司公告、官方业绩指引",
        "allowed_use": "冻结历史事实和模型基线",
    },
    "B_reproducible": {
        "sources": "Tushare结构化数据、程序计算、官方统计、行业协会",
        "allowed_use": "财务计算、行业比较和可复核代理变量",
    },
    "C_external_expectation": {
        "sources": "具名卖方报告、多机构一致预期",
        "allowed_use": "构建市场预期与预测分歧；单家机构不得冒充一致预期",
    },
    "D_alternative_intelligence": {
        "sources": "知识星球、渠道调研、专家纪要、私域卖方推送",
        "allowed_use": "量化模型变更、情景概率变化、验证日历变化或明确拒绝",
    },
    "E_background": {
        "sources": "普通新闻、政策评论、行业叙事",
        "allowed_use": "解释背景；不得单独改变盈利预测或评级",
    },
}


def _text(value: Any, limit: int = 1200) -> str:
    cleaned = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: max(limit - 1, 0)].rstrip() + "…"


def _list(value: Any, limit: int = 12) -> list[Any]:
    if not isinstance(value, list):
        return []
    return value[:limit]


def _target_aliases(symbol: str, knowledge_planet_context: str) -> list[str]:
    aliases = {
        str(symbol or "").strip(),
        str(symbol or "").replace(".", "").strip(),
        str(symbol or "").split(".", 1)[0].strip(),
    }
    for line in str(knowledge_planet_context or "").splitlines():
        if not re.search(r"(?:Primary query terms|Direct terms)\s*:", line, re.I):
            continue
        _, _, values = line.partition(":")
        for item in re.split(r"[,，、]", values):
            item = item.strip(" -*`\t")
            if len(item) >= 2:
                aliases.add(item)
    return sorted((alias for alias in aliases if alias), key=len, reverse=True)


def _target_excerpt(text: str, aliases: list[str], limit: int = 520) -> tuple[str, str]:
    raw = re.sub(r"\s+", " ", str(text or "")).strip()
    if not raw:
        return "", "missing"
    lowered = raw.lower()
    positions = [
        lowered.find(alias.lower())
        for alias in aliases
        if alias and lowered.find(alias.lower()) >= 0
    ]
    if not positions:
        return _text(raw, min(limit, 300)), "unverified_target_scope"
    position = min(positions)
    start = max(0, position - 80)
    return _text(raw[start : start + limit], limit), "target_mentioned"


def _knowledge_planet_role(row: Mapping[str, Any]) -> str:
    disposition = str(row.get("disposition", "")).lower()
    status = str(row.get("quantification_status", "")).lower()
    outcome = str(row.get("decision_outcome", "")).lower()
    if any(token in disposition for token in ("reject", "拒绝", "不采纳")) or outcome.startswith("rejected"):
        return "rejected"
    if status == "quantified" or disposition == "model_change":
        return "model_input"
    if status == "probability_only" or disposition == "probability_change":
        return "probability_adjustment"
    if disposition in {"verification_change", "watch", "watch_unchanged"}:
        return "verification_item"
    return "verification_item"


def _chapter_for_variable(variable: str, source_module: str = "") -> str:
    value = f"{variable} {source_module}".lower()
    if any(token in value for token in ("valuation", "fair_value", "share_count", "dividend", "capital_allocation")):
        return "chapter_7_valuation_rating"
    if any(token in value for token in ("expectation", "consensus", "sell_side", "price_move", "relative_strength")):
        return "chapter_6_expectations"
    if any(token in value for token in ("forecast", "profit", "eps", "revenue", "margin", "volume", "asp", "cost", "cash", "capex")):
        return "chapter_5_growth_forecast"
    if any(token in value for token in ("peer", "moat", "competition", "market_share")):
        return "chapter_4_competition"
    if any(token in value for token in ("segment", "business_unit", "subsidiary", "product")):
        return "chapter_3_profit_pools"
    if any(token in value for token in ("industry", "commodity", "policy", "supply_chain", "cycle")):
        return "chapter_2_industry_chain"
    return "chapter_1_company"


def _evidence_index(bundle: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for collection in ("deterministic_evidence", "semantic_metrics"):
        for row in _list(bundle.get(collection), 100):
            if not isinstance(row, Mapping):
                continue
            evidence_id = str(row.get("evidence_id") or row.get("metric_id") or "").strip()
            if not evidence_id:
                continue
            source_module = str(row.get("source_module") or row.get("source") or "")
            variable = str(row.get("model_variable") or row.get("variable") or "unmapped")
            rows[evidence_id] = {
                "evidence_id": evidence_id,
                "source_module": source_module,
                "variable": variable,
                "period": row.get("period", "unspecified"),
                "status": row.get("status") or row.get("evidence_status") or "unverified",
                "text": _text(row.get("text") or row.get("source_quote") or row.get("value_text"), 420),
                "chapter_id": _chapter_for_variable(variable, source_module),
            }
    return rows


def build_reader_research_dossier(
    symbol: str,
    as_of_date: str,
    *,
    structured_research: Mapping[str, Any],
    contexts: Mapping[str, str],
) -> dict[str, Any]:
    """Build the deterministic seven-chapter research dossier."""

    packet = dict(structured_research.get("underwriting_packet") or {})
    company_model = dict(packet.get("company_model") or {})
    segments = [dict(row) for row in _list(packet.get("segment_models"), 12) if isinstance(row, Mapping)]
    business_units = [dict(row) for row in _list(packet.get("business_unit_map"), 16) if isinstance(row, Mapping)]
    questions = [dict(row) for row in _list(packet.get("underwriting_questions"), 7) if isinstance(row, Mapping)]
    moat_tests = [dict(row) for row in _list(packet.get("moat_evidence_tests"), 8) if isinstance(row, Mapping)]
    competition_landscapes = [
        dict(row)
        for row in _list(packet.get("competition_landscapes"), 12)
        if isinstance(row, Mapping)
    ]
    material_transactions = [
        dict(row)
        for row in _list(packet.get("transaction_rights_map"), 8)
        if isinstance(row, Mapping)
    ]
    llm_analysis = dict(packet.get("llm_analysis_layer") or {})
    evidence = _evidence_index(structured_research)
    aliases = _target_aliases(symbol, contexts.get("knowledge_planet", ""))

    knowledge_planet: list[dict[str, Any]] = []
    for row in _list(structured_research.get("kpe_impacts"), 20):
        if not isinstance(row, Mapping):
            continue
        known = row.get("known_kpe") if isinstance(row.get("known_kpe"), Mapping) else {}
        evidence_id = str(row.get("evidence_id") or known.get("evidence_id") or "").upper()
        excerpt, entity_scope = _target_excerpt(str(known.get("evidence") or ""), aliases)
        role = _knowledge_planet_role(row)
        variable = str(row.get("variable") or known.get("affected_variable") or "unmapped")
        knowledge_planet.append(
            {
                "evidence_id": evidence_id,
                "source_type": known.get("source_type", "alternative_intelligence"),
                "published_at": known.get("date", ""),
                "source_reliability": known.get("source_reliability", "C_private_unverified"),
                "bias_profile": known.get("bias_profile", "unknown"),
                "adoption_ceiling": known.get("adoption_ceiling", "scenario_or_verification_only"),
                "target_excerpt": excerpt,
                "entity_scope": entity_scope,
                "affected_variable": variable,
                "allowed_role": role,
                "decision_outcome": _text(row.get("decision_outcome"), 380),
                "verification_gate": _text(row.get("verification_gate") or known.get("verification"), 260),
                "grounding_status": row.get("grounding_status", "unverified"),
                "chapter_id": (
                    "chapter_6_expectations"
                    if role in {"probability_adjustment", "verification_item", "rejected"}
                    else _chapter_for_variable(variable, "knowledge_planet")
                ),
            }
        )

    chapter_packets: list[dict[str, Any]] = []
    for chapter_id, title, reader_goal in CHAPTERS:
        selected_evidence = [
            evidence_id
            for evidence_id, row in evidence.items()
            if row.get("chapter_id") == chapter_id
        ][:12]
        selected_kpe = [
            row["evidence_id"]
            for row in knowledge_planet
            if row.get("chapter_id") == chapter_id
            and row.get("allowed_role") != "rejected"
            and row.get("evidence_id")
        ][:6]
        chapter_packets.append(
            {
                "chapter_id": chapter_id,
                "title": title,
                "reader_goal": reader_goal,
                "selected_evidence_ids": selected_evidence,
                "knowledge_planet_ids": selected_kpe,
                "writing_contract": (
                    "核心问题→清晰判断→产业/商业机制→少量决定性证据→"
                    "最强反证与边界→财务或估值含义→自然过渡。"
                    "不得按数据源逐项复述。"
                ),
            }
        )

    forecast_lines = [dict(row) for row in _list(packet.get("forecast_lines"), 36) if isinstance(row, Mapping)]
    scenarios = [dict(row) for row in _list(packet.get("scenarios"), 3) if isinstance(row, Mapping)]
    sell_side = [dict(row) for row in _list(structured_research.get("sell_side_intelligence"), 12) if isinstance(row, Mapping)]

    return {
        "schema_version": 1,
        "symbol": symbol,
        "as_of_date": str(as_of_date),
        "reader_contract": {
            "audience": "普通投资者",
            "principle": "数据用于权威佐证，不能替代公司、产业链与投资逻辑。",
            "formal_rating_position": "开篇投资摘要，并在第七章末尾重申",
            "chapter_count": 7,
        },
        "source_policy": SOURCE_POLICY,
        "company_introduction": {
            "business_archetype": company_model.get("business_archetype", ""),
            "value_proposition_and_customers": company_model.get("value_proposition_and_customers", ""),
            "revenue_equation": company_model.get("revenue_equation", ""),
            "profit_equation": company_model.get("profit_equation", ""),
            "cash_flow_equation": company_model.get("cash_flow_equation", ""),
            "capital_intensity_and_reinvestment": company_model.get("capital_intensity_and_reinvestment", ""),
            "key_unknowns": _list(company_model.get("key_unknowns"), 8),
        },
        "industry_chain": {
            "operating_model_family": company_model.get("operating_model_family", "other"),
            "upstream_cost_and_supply": [
                {
                    "segment": row.get("segment"),
                    "supply_capacity": _text(row.get("industry_supply_and_capacity"), 500),
                    "unit_cost_inputs": _text(row.get("unit_cost_and_input_prices"), 500),
                }
                for row in segments
            ],
            "downstream_demand_and_pricing": [
                {
                    "segment": row.get("segment"),
                    "customers_channel": _text(row.get("customers_and_channel"), 400),
                    "demand": _list(row.get("demand_and_order_drivers"), 5),
                    "price_asp": _text(row.get("price_asp_take_rate"), 400),
                }
                for row in segments
            ],
        },
        "profit_pools": {
            "reported_or_analytical_units": business_units,
            "segment_models": segments,
        },
        "material_transactions": {
            "rights_and_cash_waterfalls": material_transactions,
            "rule": (
                "Reconcile ownership before/after, attributable cash and retained/disposed rights "
                "before forecast, cash-flow classification or valuation."
            ),
        },
        "competition_and_moat": {
            "landscapes": competition_landscapes,
            "competition_and_substitution_analysis": _text(
                llm_analysis.get("competition_and_substitution_analysis"), 1800
            ),
            "claimed_mechanisms": _list(company_model.get("moat_mechanisms"), 7),
            "tests": moat_tests,
            "structural_risks": _list(company_model.get("structural_risks"), 8),
            "interpretation_rule": (
                "Chapter 2 owns market boundary, structure, direct competitors, substitutes and likely response; "
                "Chapter 4 owns relative advantage, observable proof and financial persistence."
            ),
        },
        "key_underwriting_questions": questions,
        "forecast_spine": {
            "forecast_years": _list(packet.get("forecast_years"), 4),
            "forecast_lines": forecast_lines,
            "scenarios": scenarios,
            "readiness": packet.get("research_readiness", "partial"),
            "readiness_reasons": _list(packet.get("readiness_reasons"), 10),
        },
        "market_expectations": {
            "sell_side_observations": sell_side,
            "valuation_closure": packet.get("valuation_closure", {}),
            "rule": "单家机构是观察值；只有具备样本和口径的多机构数据才可称为一致预期。",
        },
        "knowledge_planet": {
            "importance": "material_alternative_intelligence",
            "use_rule": "每条线索必须落到模型变化、概率变化、验证变化或拒绝之一。",
            "items": knowledge_planet,
        },
        "evidence_index": list(evidence.values())[:50],
        "chapter_packets": chapter_packets,
        "preprocessing_notes": [
            "原始上下文不直接成为公共报告结构。",
            "知识星球线索已按目标实体、变量、允许用途和验证门槛重新路由。",
            "所有章节必须围绕读者问题展开，数据只作为决定性证据进入正文。",
        ],
    }


def compact_reader_research_dossier(
    dossier: Mapping[str, Any] | None,
    *,
    max_chars: int = 15000,
) -> dict[str, Any]:
    """Return a prompt-sized dossier while retaining the seven-chapter spine."""

    if not dossier:
        return {}
    compact = {
        "schema_version": dossier.get("schema_version"),
        "symbol": dossier.get("symbol"),
        "as_of_date": dossier.get("as_of_date"),
        "reader_contract": dossier.get("reader_contract", {}),
        "source_policy": dossier.get("source_policy", {}),
        "company_introduction": dossier.get("company_introduction", {}),
        "industry_chain": dossier.get("industry_chain", {}),
        "profit_pools": dossier.get("profit_pools", {}),
        "material_transactions": dossier.get("material_transactions", {}),
        "competition_and_moat": dossier.get("competition_and_moat", {}),
        "key_underwriting_questions": _list(dossier.get("key_underwriting_questions"), 5),
        "forecast_spine": dossier.get("forecast_spine", {}),
        "market_expectations": dossier.get("market_expectations", {}),
        "knowledge_planet": {
            "importance": (dossier.get("knowledge_planet") or {}).get("importance"),
            "use_rule": (dossier.get("knowledge_planet") or {}).get("use_rule"),
            "items": _list((dossier.get("knowledge_planet") or {}).get("items"), 10),
        },
        "chapter_packets": dossier.get("chapter_packets", []),
    }
    rendered = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
    if len(rendered) <= max_chars:
        return compact
    compact.pop("source_policy", None)
    for key in ("profit_pools", "industry_chain", "forecast_spine", "market_expectations"):
        value = compact.get(key)
        if not isinstance(value, dict):
            continue
        for list_key, rows in list(value.items()):
            if isinstance(rows, list) and len(rows) > 5:
                value[list_key] = rows[:5]
    kp = compact.get("knowledge_planet", {})
    if isinstance(kp, dict):
        kp["items"] = _list(kp.get("items"), 6)
    return compact


def render_reader_research_dossier(dossier: Mapping[str, Any]) -> str:
    """Render a concise human-auditable view of the preprocessing result."""

    company = dossier.get("company_introduction") or {}
    kp = dossier.get("knowledge_planet") or {}
    parts = [
        f"# 七章研究档案：{dossier.get('symbol', '')}",
        "",
        f"- 截止日期：{dossier.get('as_of_date', '')}",
        "- 写作原则：数据用于权威佐证，不能替代公司、产业链与投资逻辑。",
        "- 正式评级位置：开篇投资摘要，并在第七章末尾重申。",
        "",
        "## 公司与商业模式",
        "",
        f"- 公司类型：{company.get('business_archetype') or '待确认'}",
        f"- 客户与价值：{company.get('value_proposition_and_customers') or '待确认'}",
        f"- 收入方程：{company.get('revenue_equation') or '待确认'}",
        f"- 利润方程：{company.get('profit_equation') or '待确认'}",
        f"- 现金方程：{company.get('cash_flow_equation') or '待确认'}",
        "",
        "## 七章路由",
        "",
    ]
    for chapter in dossier.get("chapter_packets", []):
        parts.append(
            f"- **{chapter.get('title', '')}**：{chapter.get('reader_goal', '')} "
            f"（EV {len(chapter.get('selected_evidence_ids', []))} 条；"
            f"KPE {len(chapter.get('knowledge_planet_ids', []))} 条）"
        )
    parts.extend(["", "## 知识星球利用结果", ""])
    items = kp.get("items", []) if isinstance(kp, Mapping) else []
    if not items:
        parts.append("- 本次没有可路由的知识星球线索。")
    for row in items[:12]:
        parts.append(
            f"- {row.get('evidence_id', 'KPE')}｜{row.get('allowed_role', 'verification_item')}｜"
            f"{row.get('target_excerpt') or '无目标公司摘录'}｜"
            f"下一验证：{row.get('verification_gate') or '待定义'}"
        )
    return "\n".join(parts).strip() + "\n"
