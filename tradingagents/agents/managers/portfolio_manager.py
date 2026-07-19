"""Portfolio Manager: synthesises the risk-analyst debate into the final decision.

Uses LangChain's ``with_structured_output`` so the LLM produces a compact typed
``SellSidePMDecision`` directly, in a single call.  The result is rendered
back to markdown for storage in ``final_trade_decision`` so memory log,
CLI display, and saved reports continue to consume the same shape they do
today.  When a provider does not expose structured output, the agent falls
back gracefully to free-text generation.
"""

from __future__ import annotations

import json
import re

from tradingagents.agents.schemas import (
    SellSideEditorialReview,
    SellSidePMDecision,
    normalize_sell_side_pm_decision,
    render_sell_side_pm_decision,
)
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_baijiu_instruction,
    get_biopharma_instruction,
    get_building_materials_instruction,
    get_buy_side_thesis_instruction,
    get_buy_side_underwriting_modules_instruction,
    get_company_depth_contract_instruction,
    get_compute_leasing_instruction,
    get_consumer_staples_instruction,
    get_dividend_defensive_instruction,
    get_evidence_instruction,
    get_earnings_model_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_insurance_instruction,
    get_knowledge_planet_instruction,
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_optical_module_instruction,
    get_price_move_attribution_instruction,
    get_investor_interaction_instruction,
    get_language_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_material_catalyst_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_instruction,
    get_question_led_debate_instruction,
    get_research_gap_instruction,
    get_semiconductor_instruction,
    get_supply_demand_fallback_instruction,
    get_supply_chain_selection_instruction,
    get_shareholder_structure_instruction,
    get_software_instruction,
    get_three_layer_conclusion_instruction,
    get_thematic_valuation_instruction,
    get_web_fact_check_instruction,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)
from tradingagents.dataflows.prompt_compaction import (
    compact_debate_history,
    compact_for_prompt,
    compact_risk_history,
    compact_state_fields,
)
from tradingagents.dataflows.pm_report_compaction import split_pm_public_report
from tradingagents.dataflows.structured_research import compact_structured_research_for_prompt


def _deterministically_owned_pm_line(row: dict) -> bool:
    if str(row.get("status", "")).lower() != "calculated":
        return False
    formula = str(row.get("formula", "")).lower()
    return any(
        marker in formula
        for marker in (
            "parent net profit (cny mn) / diluted shares",
            "ocf = parent net profit x accepted ocf/ni ratio",
            "ocf - abs(capex)",
            "revenue x gross margin",
            "operating profit + finance/other - tax - minority interest",
            "deterministic probability-weighted scenario equity value",
            "deterministic total fair value per share",
        )
    )


def _merge_manager_canonical_snapshot(
    manager_payload: dict,
    pm_payload: dict,
) -> tuple[dict, list[str]]:
    """Deterministically preserve the Research Manager numeric handoff.

    Copying a long canonical snapshot is a data-movement task, not a reasoning
    task.  Providers regularly omit unchanged rows even when prompted to copy
    them.  Restore missing rows here and reject undocumented value/unit changes
    before deterministic PM calculations run.
    """

    payload = json.loads(json.dumps(pm_payload or {}, ensure_ascii=False))
    manager_rows = [
        dict(row) for row in manager_payload.get("canonical_model_snapshot", []) or []
        if str(row.get("line_id", "")).strip()
    ]
    pm_rows = [
        dict(row) for row in payload.get("canonical_model_snapshot", []) or []
        if str(row.get("line_id", "")).strip()
    ]
    if not manager_rows:
        return payload, []

    accepted_changes = {
        str(row.get("line_id", "")).strip().lower()
        for row in payload.get("handoff_change_rows", []) or []
        if str(row.get("disposition", "")).lower() == "accepted"
    }
    pm_by_id = {
        str(row.get("line_id", "")).strip().lower(): row for row in pm_rows
    }
    manager_ids = {
        str(row.get("line_id", "")).strip().lower() for row in manager_rows
    }
    merged: list[dict] = []
    notes: list[str] = []
    for manager_row in manager_rows:
        line_id = str(manager_row.get("line_id", "")).strip().lower()
        pm_row = pm_by_id.get(line_id)
        if pm_row is None:
            merged.append(manager_row)
            notes.append(f"restored omitted canonical line {line_id}")
            continue
        if line_id in accepted_changes:
            merged.append(pm_row)
            continue
        if (
            pm_row.get("value") != manager_row.get("value")
            or str(pm_row.get("unit", "")).strip().lower()
            != str(manager_row.get("unit", "")).strip().lower()
        ):
            notes.append(f"restored undocumented canonical change {line_id}")
        merged.append(manager_row)

    # Retain PM-only dependent lines such as deterministic EPS.  They will be
    # recalculated by normalize_sell_side_pm_decision below.
    merged.extend(
        row
        for row in pm_rows
        if str(row.get("line_id", "")).strip().lower() not in manager_ids
    )
    payload["canonical_model_snapshot"] = merged
    return payload, notes


def _canonical_handoff_issues(
    manager_payload: dict,
    pm_payload: dict,
) -> list[str]:
    """Find silent PM snapshot changes before the saved-report audit."""

    def line_map(payload: dict) -> dict[str, dict]:
        return {
            str(row.get("line_id", "")).strip().lower(): dict(row)
            for row in payload.get("canonical_model_snapshot", []) or []
            if str(row.get("line_id", "")).strip()
        }

    manager_lines = line_map(manager_payload)
    pm_lines = line_map(pm_payload)
    accepted_changes = {
        str(row.get("line_id", "")).strip().lower()
        for row in pm_payload.get("handoff_change_rows", []) or []
        if str(row.get("disposition", "")).lower() == "accepted"
    }
    issues: list[str] = []
    for line_id, manager_line in manager_lines.items():
        pm_line = pm_lines.get(line_id)
        if pm_line is None:
            issues.append(f"dropped canonical line: {line_id}")
            continue
        manager_value = manager_line.get("value")
        pm_value = pm_line.get("value")
        value_changed = manager_value != pm_value
        try:
            left = float(manager_value)
            right = float(pm_value)
            value_changed = abs(left - right) > max(abs(left) * 0.02, 0.01)
        except (TypeError, ValueError):
            pass
        manager_unit = str(manager_line.get("unit", "")).strip().lower()
        pm_unit = str(pm_line.get("unit", "")).strip().lower()
        unit_changed = bool(manager_unit and pm_unit and manager_unit != pm_unit)
        if (
            (value_changed or unit_changed)
            and line_id not in accepted_changes
            and not _deterministically_owned_pm_line(pm_line)
        ):
            issues.append(
                f"silent change {line_id}: {manager_value} {manager_unit} -> "
                f"{pm_value} {pm_unit}"
            )
    return issues


def _analytical_structure_issues(pm_payload: dict) -> list[str]:
    """Advisory repair triggers for the internal analytical workbench."""
    requirements = (
        ("research_questions", 3, "company-specific research questions"),
        ("question_verdicts", 3, "evidence-weighted question verdicts"),
        ("forecast_takeaways", 2, "forecast take-aways"),
        ("forecast_assumptions", 3, "auditable forecast assumptions"),
        ("core_theses", 2, "ranked core theses"),
    )
    issues: list[str] = []
    for field, minimum, label in requirements:
        count = len(pm_payload.get(field, []) or [])
        if count < minimum:
            issues.append(f"analytical structure: {label} count={count}, expected at least {minimum}")
    new_contracts = (
        ("business_model_mechanisms", 4, "business-model mechanism rows"),
        ("segment_economics", 2, "material segment-economics rows"),
        ("industry_driver_matrix", 3, "sector-native driver rows"),
        ("moat_mechanisms", 3, "economic moat mechanism rows"),
        ("accounting_quality_matrix", 3, "accounting/capital-allocation rows"),
    )
    if any(field in pm_payload for field, _, _ in new_contracts):
        for field, minimum, label in new_contracts:
            count = len(pm_payload.get(field, []) or [])
            if count < minimum:
                issues.append(f"deep research matrix: {label} count={count}, expected at least {minimum}")
        scenarios = (
            (pm_payload.get("safe_valuation_assumptions") or {}).get("scenarios", [])
        )
        if len(scenarios) != 3:
            issues.append(
                f"deterministic valuation: bull/base/bear scenario inputs count={len(scenarios)}, expected 3"
            )
    thesis_chapter = str(pm_payload.get("thesis_financial_bridge", "")).lower()
    closure_markers = {
        "strongest counterargument/boundary": ("反证", "反方", "边界", "counter"),
        "market-pricing implication": ("市场定价", "当前价格", "预期差", "market pricing"),
        "falsification condition": ("证伪", "验证条件", "下调信号", "falsification"),
    }
    if thesis_chapter:
        for label, markers in closure_markers.items():
            if not any(marker in thesis_chapter for marker in markers):
                issues.append(f"public thesis chapter missing {label}")
    return issues


def _enforce_forecast_methodology(
    pm_payload: dict,
    structured_research: dict,
) -> tuple[dict, list[str]]:
    """Prevent an un-reconciled segment model from being called bottom-up."""

    payload = json.loads(json.dumps(pm_payload, ensure_ascii=False))
    packet = dict((structured_research or {}).get("underwriting_packet", {}) or {})
    material_units = {
        str(row.get("business_unit", "")).strip().lower()
        for row in payload.get("segment_economics", []) or []
        if str(row.get("business_unit", "")).strip()
        and str(row.get("valuation_treatment", "")).lower() in {"core", "scenario"}
    }
    forecast_rows = list(packet.get("forecast_lines", []) or [])
    revenue_segments: set[str] = set()
    profit_segments: set[str] = set()
    for row in forecast_rows:
        segment = str(row.get("segment", "")).strip().lower()
        if segment in {"consolidated", "group", "合并", "公司整体"}:
            continue
        if not all(
            row.get(field) is not None
            for field in ("year_1_value", "year_2_value", "year_3_value")
        ):
            continue
        metric = str(row.get("metric", "")).strip().lower()
        if "revenue" in metric or "营业收入" in metric or metric == "收入":
            revenue_segments.add(segment)
        if (
            "profit" in metric
            or "利润" in metric
            or "净利" in metric
        ) and "margin" not in metric and "利润率" not in metric:
            profit_segments.add(segment)
    text = str(payload.get("autonomous_forecast_model", "") or "")
    claims_bottom_up = bool(re.search(r"自下而上|bottom[- ]up", text, re.I))
    complete = (
        bool(material_units)
        and len(revenue_segments) >= len(material_units)
        and len(profit_segments) >= len(material_units)
    )
    if not claims_bottom_up or complete:
        return payload, []
    text = re.sub(r"自下而上", "混合", text)
    text = re.sub(r"bottom[- ]up", "hybrid", text, flags=re.I)
    disclosure = (
        "**程序化模型口径判定：混合模型。** 结构化承保包尚未为每个核心业务单元提供"
        "可与集团收入、利润和现金流逐年勾稽的三年数值行；现有分部驱动用于解释集团预测，"
        "不得表述为已完成的全量分部加总模型。"
    )
    payload["autonomous_forecast_model"] = disclosure + "\n\n" + text
    return payload, ["downgraded unsupported bottom-up label to hybrid model"]


def _normalize_sell_side_lineage(
    pm_payload: dict,
    structured_research: dict,
) -> tuple[dict, list[str]]:
    """Replace invented broker aliases with exact KSI/KPE ledger ids."""

    payload = json.loads(json.dumps(pm_payload, ensure_ascii=False))
    ledger = list((structured_research or {}).get("sell_side_intelligence", []) or [])
    valid = {
        str(row.get("intelligence_id", "")).strip().upper(): row
        for row in ledger
        if str(row.get("intelligence_id", "")).strip()
    }
    notes: list[str] = []
    for row in payload.get("sell_side_expectation_matrix", []) or []:
        source_ids = [str(value).strip() for value in row.get("source_ids", []) or []]
        exact = [value.upper() for value in source_ids if value.upper() in valid]
        matched_id = exact[0] if exact else ""
        if not matched_id and valid:
            blob = " ".join(
                str(row.get(field, ""))
                for field in (
                    "institution",
                    "published_at",
                    "forecast_and_valuation",
                    "comparison_with_our_model",
                )
            ).lower()
            blob_numbers = set(re.findall(r"\d+(?:\.\d+)?", blob))
            scored: list[tuple[int, str]] = []
            for ksi_id, candidate in valid.items():
                candidate_blob = " ".join(str(value) for value in candidate.values()).lower()
                candidate_numbers = set(re.findall(r"\d+(?:\.\d+)?", candidate_blob))
                score = 4 * len(blob_numbers & candidate_numbers)
                institution = str(row.get("institution", "")).strip().lower()
                if institution and institution in candidate_blob:
                    score += 8
                if str(row.get("published_at", ""))[:10] in candidate_blob:
                    score += 2
                scored.append((score, ksi_id))
            scored.sort(reverse=True)
            if scored and scored[0][0] >= 6:
                matched_id = scored[0][1]
        if not matched_id:
            row["source_ids"] = [value for value in source_ids if not value.upper().startswith("KSI")]
            continue
        candidate = valid[matched_id]
        linked = candidate.get("kpe_ids", candidate.get("evidence_ids", [])) or []
        if isinstance(linked, str):
            linked = re.findall(r"KPE\d+", linked, re.I)
        row["source_ids"] = list(
            dict.fromkeys(
                [matched_id]
                + [str(value).upper() for value in linked if str(value).strip()]
                + [
                    value
                    for value in source_ids
                    if not value.upper().startswith(("KSI", "KPE"))
                ]
            )
        )
        if source_ids != row["source_ids"]:
            notes.append(
                f"normalized sell-side lineage {source_ids or ['missing']} -> {row['source_ids']}"
            )

    kpe_ledger = dict((structured_research or {}).get("known_kpe_ledger", {}) or {})
    sell_side_linked_kpe_ids: set[str] = set()
    for item in ledger:
        linked = item.get("kpe_ids", item.get("evidence_ids", [])) or []
        if isinstance(linked, str):
            linked = re.findall(r"KPE\d+", linked, re.I)
        sell_side_linked_kpe_ids.update(str(value).upper() for value in linked)
    for decision in payload.get("alternative_intelligence_decisions", []) or []:
        decision_kpe_ids = {
            str(kpe_id).upper() for kpe_id in decision.get("kpe_ids", []) or []
        }
        types = {
            str((kpe_ledger.get(str(kpe_id).upper()) or {}).get("source_type", "")).lower()
            for kpe_id in decision.get("kpe_ids", []) or []
        }
        if (
            types & {"sell_side_push", "strategy_view", "broker_report_summary"}
            or decision_kpe_ids & sell_side_linked_kpe_ids
        ):
            decision["source_type"] = "sell_side_view"
            if decision.get("evidence_grade") == "B_private_edge":
                decision["evidence_grade"] = "C_market_narrative"
            decision["public_crosscheck"] = (
                str(decision.get("public_crosscheck", "")).rstrip("。")
                + "；该KPE与对应KSI属于同一卖方原始帖子，不构成独立交叉验证。"
            )
    return payload, notes


def _editorial_review_prompt(
    *,
    decision_payload: dict,
    manager_payload: dict,
    structured_research_context: str,
    fundamentals_context: str,
    handoff_issues: list[str],
) -> str:
    return f"""You are the senior sell-side research editor for an A-share deep-dive memo.

Judge analytical depth, not writing length or keyword coverage. Missing unavailable data is
not itself a defect when it is disclosed and handled conditionally. Require revision only
where the memo can improve using evidence already supplied, where logic/financial
transmission is shallow, where counterevidence is missing, where valuation does not answer
the expectation gap, where company economics are generic, or where sections contradict.

Treat an empty or superficial question_verdicts, forecast_takeaways, forecast_assumptions, or core_theses array
as a substantive defect in the internal workbench. The research questions and verdict ledger must not be
rendered as a public Q&A chapter; verify instead that their accepted conclusions are synthesized once into
the relevant company, industry, thesis, forecast or valuation narrative. Check that assumptions have historical/evidence anchors rather than
being arbitrary bull/bear midpoints; that the three-year table reconciles earnings and cash;
and that every ranked thesis has one clear takeaway, strongest counterevidence, auditable
financial transmission, market-pricing implication and falsification gate. Recalculate any
claimed sensitivity before accepting it. Do not reward a long machine table or a long moat list.
The public `thesis_financial_bridge` chapter must preserve those same elements in connected analyst prose;
the internal `core_theses` cards do not compensate for a thin public chapter.
Require `business_model_mechanisms`, `segment_economics`, `industry_driver_matrix`, `moat_mechanisms`, and
`accounting_quality_matrix` to carry the evidence and
causal depth; prose cannot compensate for empty structured rows. Recalculate the deterministic valuation output
from the supplied assumptions and reject any prose number that differs from it. If relevant KPE rows exist in the
source bundle, require at least one `alternative_intelligence_decisions` row per deduplicated material claim, with
an actual model/probability/verification change or an explicit rejection reason.
If KSI sell-side rows exist, require `sell_side_expectation_matrix` to preserve institution, date, forecast period,
valuation method/multiple/target, revision history and the exact difference versus the independent model. Never
allow one institution, one repost or one industry note to be described as market consensus.
When a foreign broker forecast affects base earnings, valuation, or scenario probability, require the row to mark
`institution_origin`, `adoption_level`, `forecast_posture`, and `key_assumptions_and_scenario`. The public valuation
chapter must tell readers that the forecast is foreign-sell-side-anchored, what demand/ASP/share/margin/valuation
case it assumes, whether that case is optimistic or conservative, and exactly how it changed the TradingAgents model.
Treat repeated substance as a revision defect: the same assumption, threshold, valuation conclusion or causal
paragraph must not be fully restated across the executive summary, thesis, forecast, valuation and risk chapters.
Keep detail in the owning chapter and use a short cross-reference elsewhere.
Treat workflow language as a revision defect in public prose: KPE/KSI disposition logs, evidence-grade audits,
question-by-question deliberation and repeated `结论/证据/反证/传导/定价/证伪` labels belong to the structured
workbench. Require section 2 to explain business mechanics and section 3 to explain moat economics before the
memo discusses detailed valuation. Exact PE/target/safe-price/scenario values should be concentrated in section 7.

Do not change the rating and do not rewrite the report in this call. Return only the
SellSideEditorialReview JSON object. Make revision instructions section-specific and
actionable. A complex company may need more detail; a simple company may be concise.

Deterministic handoff issues detected before review:
{json.dumps(handoff_issues, ensure_ascii=False)}

Research Manager canonical plan:
{json.dumps(manager_payload, ensure_ascii=False, separators=(',', ':'))[:30000]}

Structured research source of record:
{structured_research_context}

Fundamental reconciliation excerpt:
{fundamentals_context}

PM decision draft JSON:
{json.dumps(decision_payload, ensure_ascii=False, separators=(',', ':'))}
"""


def _editorial_revision_prompt(
    *,
    decision_payload: dict,
    review_payload: dict,
    handoff_issues: list[str],
    manager_payload: dict,
    structured_research_context: str,
    fundamentals_context: str,
    lessons_line: str,
    recent_decision_line: str,
) -> str:
    """Ask the same selected deep model for one bounded, evidence-preserving revision."""

    return f"""SENIOR SELL-SIDE EDITOR REVISION PASS
The draft below was already generated under the complete Portfolio Manager mandate and
validated as a SellSidePMDecision object. Revise that existing object; do not restart the
research process and do not recreate unaffected sections from raw module dumps.

Revise the PM draft once using the editorial findings below. Return the complete
SellSidePMDecision object, including fields that are unchanged.

Hard preservation rules:
- Keep the original rating exactly unchanged.
- Do not invent facts, estimates, sources, segment allocations, or unavailable data.
- Preserve the Research Manager canonical snapshot exactly unless an explicit accepted
  handoff change row states old value, new value, evidence, and recalculated impact.
- Resolve deterministic handoff issues by restoring the manager value or documenting a
  valid accepted change; do not hide the discrepancy in prose.
- Revise only sections named by the editor or needed for cross-section consistency.
- Improve causal and financial transmission, counterevidence, and valuation closure using
  the supplied record. Depth is judged by analytical closure, not word count.
- Treat the existing draft as the source for every unaffected field. The compact source
  records below exist only to support the editor's named corrections.
- Preserve the Portfolio Manager mandate: the output remains a self-contained public research note,
  not a checklist of upstream modules or an internal analysis transcript.
- Preserve the compact public-writing contract: begin with a short Company Snapshot; retain the
  Business Model & Industry Chain Primer and its upstream-midstream-downstream chain; use the
  required Debate & Decision Logic, Catalysts & Optionality, Evidence Gaps & Data Coverage, and
  Verification & Falsification content in their owning chapters. Use this narrative order and
  treat source modules as materiality gates, not a checklist. Avoid repeating the same fact;
  prefer less fragmentation, more synthesis. There is no hard word-count or section-count target.
  Close each decisive argument as claim -> evidence -> causal transmission -> valuation/position implication.
  Preserve the Bank Buy-Side Memo Overlay rule, including: If the target is not a bank, do not
  force bank-specific metrics. Route non-bank companies through their own industry-native drivers.
  For banks, retain PB/ROE/COE and earning assets x NIM logic. Preserve the Decision-Continuity Rules
  and Material-catalyst discipline. Do not invent A-share/H-share/U.S.-listed companies.

Prior-decision context that must remain reflected when relevant:
{lessons_line}{recent_decision_line}

Original PM draft JSON:
{json.dumps(decision_payload, ensure_ascii=False, separators=(',', ':'))}

Editorial review JSON:
{json.dumps(review_payload, ensure_ascii=False, separators=(',', ':'))}

Deterministic handoff issues:
{json.dumps(handoff_issues, ensure_ascii=False)}

Research Manager canonical plan (compact):
{json.dumps(manager_payload, ensure_ascii=False, separators=(',', ':'))[:30000]}

Structured research source of record (compact):
{structured_research_context}

Fundamental reconciliation excerpt:
{fundamentals_context}
"""


def create_portfolio_manager(llm):
    structured_llm = bind_structured(llm, SellSidePMDecision, "Portfolio Manager")
    editorial_review_llm = bind_structured(
        llm,
        SellSideEditorialReview,
        "Sell-Side Research Editor",
    )

    def portfolio_manager_node(state) -> dict:
        instrument_context = build_instrument_context(state["company_of_interest"])

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        research_plan = compact_for_prompt(
            state["investment_plan"],
            label="investment_plan",
            profile="portfolio",
            max_chars=30000,
        )
        trader_plan = compact_for_prompt(
            state["trader_investment_plan"],
            label="trader_plan",
            profile="portfolio",
        )
        prompt_contexts = compact_state_fields(state, profile="portfolio")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        price_move_attribution_context = prompt_contexts["price_move_attribution_context"]
        intraday_behavior_context = prompt_contexts["intraday_behavior_context"]
        relative_strength_context = prompt_contexts["relative_strength_context"]
        shipping_context = prompt_contexts["shipping_context"]
        filing_intelligence_context = prompt_contexts["filing_intelligence_context"]
        peer_comparison_context = prompt_contexts["peer_comparison_context"]
        supply_chain_comparison_context = prompt_contexts["supply_chain_comparison_context"]
        earnings_model_context = prompt_contexts["earnings_model_context"]
        company_events_context = prompt_contexts["company_events_context"]
        market_expectation_context = prompt_contexts["market_expectation_context"]
        price_earnings_decomposition_context = prompt_contexts["price_earnings_decomposition_context"]
        management_capital_allocation_context = prompt_contexts["management_capital_allocation_context"]
        shareholder_structure_context = prompt_contexts["shareholder_structure_context"]
        investor_interaction_context = prompt_contexts["investor_interaction_context"]
        policy_planning_context = prompt_contexts["policy_planning_context"]
        web_fact_check_context = prompt_contexts["web_fact_check_context"]
        knowledge_planet_context = prompt_contexts["knowledge_planet_context"]
        baijiu_context = prompt_contexts["baijiu_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
        building_materials_context = prompt_contexts["building_materials_context"]
        consumer_staples_context = prompt_contexts["consumer_staples_context"]
        optical_module_context = prompt_contexts["optical_module_context"]
        biopharma_context = prompt_contexts["biopharma_context"]
        software_context = prompt_contexts["software_context"]
        insurance_context = prompt_contexts["insurance_context"]
        medical_device_context = prompt_contexts["medical_device_context"]
        metals_mining_context = prompt_contexts["metals_mining_context"]
        industry_cycle_context = prompt_contexts["industry_cycle_context"]
        company_business_model_context = prompt_contexts["company_business_model_context"]
        industry_kpi_context = prompt_contexts["industry_kpi_context"]
        forecast_model_context = prompt_contexts["forecast_model_context"]
        quality_audit_context = prompt_contexts["quality_audit_context"]
        thesis_question_context = prompt_contexts["thesis_question_context"]
        data_coverage_context = prompt_contexts["data_coverage_context"]

        # Sector playbooks are intentionally large. Inject only those whose
        # deterministic gate fired; sending every bank, mining, software,
        # biopharma, baijiu, and optical-module rule to an automotive supplier
        # diluted company-specific evidence and made structured PM output less
        # reliable.
        gated_playbooks = [
            ("Baijiu", baijiu_context, get_baijiu_instruction),
            ("Compute leasing", compute_leasing_context, get_compute_leasing_instruction),
            ("Defensive dividend", dividend_defensive_context, get_dividend_defensive_instruction),
            ("Building materials", building_materials_context, get_building_materials_instruction),
            ("Consumer staples", consumer_staples_context, get_consumer_staples_instruction),
            ("Optical module", optical_module_context, get_optical_module_instruction),
            ("Biopharma", biopharma_context, get_biopharma_instruction),
            ("Software", software_context, get_software_instruction),
            ("Insurance", insurance_context, get_insurance_instruction),
            ("Medical device", medical_device_context, get_medical_device_instruction),
            ("Metals/mining", metals_mining_context, get_metals_mining_instruction),
        ]

        def _gate_triggered(context: str) -> bool:
            lowered = str(context or "").lower()
            return "status: triggered" in lowered or "status：triggered" in lowered

        active_playbooks = [
            (label, context, instruction())
            for label, context, instruction in gated_playbooks
            if _gate_triggered(context)
        ]
        gated_sector_context = "\n".join(
            f"- {label} context: **{context}**"
            for label, context, _ in active_playbooks
        ) or "- No gated sector playbook was triggered for this company."
        gated_sector_instructions = "".join(
            instruction for _, _, instruction in active_playbooks
        )
        gated_sector_instructions += get_semiconductor_instruction()
        structured_research_context = compact_structured_research_for_prompt(
            state.get("structured_research_context", {}),
            max_chars=32000,
        )
        fundamentals_reconciliation_context = compact_for_prompt(
            state.get("fundamentals_report", ""),
            label="analyst_report",
            profile="portfolio",
            max_chars=9000,
        )
        research_manager_payload_context = json.dumps(
            state.get("research_manager_plan_payload", {}),
            ensure_ascii=False,
            separators=(",", ":"),
        )[:30000]
        investment_debate_state = state.get("investment_debate_state", {})
        bull_bear_context = ""
        if investment_debate_state:
            bull_history = compact_debate_history(
                investment_debate_state.get("bull_history", ""),
                profile="portfolio",
            )
            bear_history = compact_debate_history(
                investment_debate_state.get("bear_history", ""),
                profile="portfolio",
            )
            judge_decision = compact_for_prompt(
                investment_debate_state.get("judge_decision", research_plan),
                label="investment_plan",
                profile="portfolio",
                max_chars=10000,
            )
            bull_bear_context = f"""
**Research Team Bull-Bear Debate Context:**
- Bull case history:
{bull_history}
- Bear case history:
{bear_history}
- Research Manager ruling:
{judge_decision}
"""

        past_context = compact_for_prompt(
            state.get("past_context", ""),
            label="past_context",
            profile="portfolio",
        )
        recent_decision_context = compact_for_prompt(
            state.get("recent_decision_context", ""),
            label="recent_decision_context",
            profile="portfolio",
        )
        prompt_risk_history = compact_risk_history(history, profile="portfolio")
        lessons_line = (
            f"- Lessons from prior decisions and outcomes:\n{past_context}\n"
            if past_context
            else ""
        )
        recent_decision_line = (
            f"- Most recent same-ticker decision (may still be pending outcome):\n"
            f"{recent_decision_context}\n"
            if recent_decision_context
            else ""
        )

        prompt = f"""As the Portfolio Manager, synthesize the risk analysts' debate and deliver the final trading decision.

{instrument_context}

---

**Rating Scale** (use exactly one):
- **Buy**: Clear core bet, strong evidence/proxy support, attractive probability/payoff, and identifiable catalysts
- **Overweight**: Positive expected value but some evidence gaps remain; suitable for gradual or partial exposure
- **Hold**: Balanced or transition setup where the company may be investable, but the decisive variable is unresolved or the justified position is only an observation/starter weight pending validation
- **Underweight**: Negative expected value or unattractive payoff, but not enough evidence for a full exit call
- **Sell**: Core thesis deteriorated or downside probability/payoff is clearly unfavorable

**Final-Rating Consistency Rules:**
- The structured `rating` field is the final Portfolio Manager rating. Every PM summary, one-line thesis, holder/builder action, position posture, and execution paragraph must be consistent with that final rating.
- Research Manager, Trader, and risk-analyst ratings are upstream, non-final inputs. If you discuss a different upstream rating, label it explicitly as `upstream Research Manager view`, `upstream Trader view`, or `prior non-final view`; never call it the current, final, or PM rating.
- Before finalizing, check that no sentence says `current rating`, `final rating`, `本次评级`, `当前评级`, or `最终评级` equals a tier different from the structured final rating.
- If the final PM rating differs from the Research Manager or Trader rating, explain the change in Debate & Decision Logic or Rating Change Audit, then make the action guidance follow the final PM rating only.
- For Buy / Overweight, do not tell holders to reduce to Underweight or avoid new positions unless you clearly mark that as a rejected upstream view. For Underweight / Sell, do not tell builders to add or overweight unless it is a lower-price re-entry watch condition.
- The final rating must be derived from the company's full fundamental chain, not from the failure of the opposite rating. `The Underweight case is not proven` is not a reason to choose Overweight; `the Overweight case is not proven` is not a reason to choose Underweight. First prove the positive or negative expected-value chain on its own merits.
- Before choosing Buy/Overweight/Underweight/Sell, complete a rating-strength ladder: company quality, segment economics, key operating drivers, cash-flow and balance-sheet quality, management/capital allocation, valuation-implied expectations, catalyst path, downside case, peer opportunity cost, and falsification path.
- Do not map uncertainty, a starter position, or waiting for one disclosure mechanically to Hold. Derive the rating, conviction and sizing from verified evidence and the reconciled expected-value/downside distribution. Put source unavailability only in `research_readiness` and retrieval tasks; Hold is valid only when the available verified model supports roughly balanced risk/reward.
- Always fill the `rating_posture` field. Keep the clean `rating` field as exactly Buy / Overweight / Hold / Underweight / Sell, but use `rating_posture` to make the action readable.
- If the final rating is Hold, choose exactly one posture: `Hold / Positive Watch`, `Hold / Defensive Starter`, `Hold / Neutral Wait`, or `Hold / Negative Watch`. Then state whether new capital should wait, open only a starter, or avoid, and state what upgrades or downgrades the posture.
- If the final rating is Overweight with unresolved evidence, label the posture `Staged/Cautious Overweight` and prove why positive expected value is already strong enough despite the unresolved gate. If that proof is missing, use Hold with a positive-watch or defensive-starter posture instead.
- Do not let valuation support, technical strength, or Knowledge Planet sell-side evidence become a separate side comment. Translate them into the posture: current allocation, starter size, wait zone, upgrade trigger, downgrade trigger, and next verification date.
- Hold must not be a vague neutral label. A high-quality Hold should be useful: state the live thesis, justified current position, valuation band, exact upgrade triggers, exact downgrade triggers, and the next verification date.

**Non-Negotiable Research Release Contract:**
- The Structured Research Bundle contains a shared `underwriting_packet`. Treat it as the common analytical workbench, not optional background. Start from its company model, material segment driver chains, underwriting questions, three-year forecast lines, scenarios and evidence-change rules. The final report must explain and reconcile this model; it must not create a separate set of unsupported PM assumptions.
- Treat the Research Manager's Accepted Underwriting Model as the canonical post-analyst version. It supersedes earlier `missing` markers only where the manager records a reproducible filing/Tushare calculation or a clearly labeled estimate. Do not resurrect a resolved gap, and do not silently change an accepted assumption without showing old value, new value, evidence, formula and EPS/FCF/value impact.
- The Research Manager's `Accepted Underwriting Model` and `Model Change Ledger` are the authoritative debated revisions to the initial packet. Apply those revisions line by line. When the accepted model conflicts with the initial packet, disclose the change and use the accepted value only when its evidence and arithmetic reconcile; otherwise keep the line unresolved rather than choosing whichever supports the desired rating.
- The PM is a report synthesizer and final allocator, not the first analyst to understand the company. Do not summarize upstream prose sequentially. Reconstruct the investment case from the shared operating equations and accepted model changes, then use debate excerpts only to explain why an assumption changed or stayed unchanged.
- Fill every required field in `SellSidePMDecision`. The renderer, not the model, owns all H1/H2 headings and produces exactly eight public Chinese sections. Do not put H2 headings in any field. `report_markdown` is ignored legacy compatibility state and must be empty.
- Fill `research_questions`, `question_verdicts`, `forecast_takeaways`, `forecast_assumptions`, and `core_theses` from the accepted model. Do not leave them empty when the source record supports analysis. Questions, verdicts and thesis cards are the internal analytical workbench; they must improve the reasoning but must not appear as a public question list, Q&A ledger or repeated checklist.
- Fill `segment_economics` with every material economic unit, using reported/calculated/analyst-estimate/missing labels and explicit core/scenario/optionality/excluded valuation treatment. Fill `industry_driver_matrix` with dated demand, supply/capacity, price/cost and policy variables. Fill `accounting_quality_matrix` with working-capital, cash-conversion, capex/ROIC, leverage/impairment and shareholder-return checks. The adjacent prose interprets these tables and must not repeat every cell.
- Business-line question discipline is mandatory and starts from financial-report revenue composition. Identify high-revenue-weight and thesis-critical segments from the filing before deciding what to analyze. For every selected segment or business bucket, answer what it sells, who buys, why customers choose or switch, what substitutes or true peers threaten it, the qualitative investment judgment when data are missing, the quantitative bridge when data are available, the financial/valuation implication and the next verification gate. Missing data must lead to a qualitative discussion plus a retrieval task, not omission of the issue.
- Do not impose a fixed industry checklist. Use industry knowledge and the LLM to generate segment-specific questions from the actual business attributes: customer procurement behavior, supplier diversification, self-supply/substitution risk, price formation, unit economics, order/delivery cycle, capacity/utilization, regulatory or technology change, cash collection and peer opportunity cost. For a battery company these may include OEM multi-sourcing or storage tender economics only if the relevant disclosed segment and evidence context make them material; for another industry, generate different questions suited to its own revenue mix and economics.
- The research depth chain must be explicit in the reasoning even if not shown as a table: financial-report revenue mix -> profit-pool priority -> segment-specific question tree -> qualitative/quantitative answer -> market expectation gap -> valuation transmission -> falsification gate. Revenue weight alone is insufficient; rank business importance by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
- Every core thesis must identify the specific business-line assumption that differs from market expectations, the direction and mechanism of the difference, the revenue/profit/EPS/FCF or multiple impact, the strongest counter-mechanism, and the earliest observable KPI or disclosure that would confirm or overturn it.
- Use the LLM analysis layer in eight places before writing the final decision: (1) generate business-line question trees from filing revenue mix, (2) judge profit-pool priority beyond revenue share, (3) analyze competition/substitution/customer switching, (4) bridge qualitative judgment to quantitative evidence or retrieval tasks, (5) infer market/consensus expectation gap, (6) red-team the thesis and define falsification, (7) explain valuation as operating-variable transmission while application code owns arithmetic, and (8) act as final sell-side editor. These are analytical judgments; do not invent historical facts or unsupported numbers.
- The public memo must show the result of these eight LLM interventions as a single investment argument. Do not create eight visible sub-sections, paste the LLM intervention map, or expose raw question trees. The reader should see a clean sell-side note: conclusion first, business economics, industry/competition, thesis with counter-case, forecast, valuation, risks/catalysts, verification and action.
- Fill `business_model_mechanisms` with four to seven links covering customer/value proposition, purchase or tender decision, pricing, delivery/revenue recognition, cost stack/service, and cash collection/capital intensity. Fill `moat_mechanisms` with at least three mechanisms tested through observable share, win rate, ASP, margin, turnover, cash or ROIC outcomes. Awards, R&D spending and market-share labels are not moat proof by themselves.
- Fill `safe_valuation_assumptions` with exactly bull/base/bear inputs plus required return, holding period, margin of safety and maximum acceptable bear loss. Use the risk parameters as underwriting discipline, not as a second punishment after already conservative base/bear scenarios. For mature blue chips or conservative base cases, start from required annual return 18-20%, one-year holding period unless the thesis needs a longer verification clock, 15-20% margin of safety, and 15-20% maximum acceptable bear loss. Use 25%+ required return or 25%+ bear-loss tolerance only for genuinely high-beta, highly leveraged, evidence-thin, or speculative names, and explain why in `valuation_closure`. Put each genuinely independent second curve in `optionality_inputs` with one metric value, multiple, probability, ownership and a separate execution haircut. Never add a bull-versus-base incremental value as optionality when the same volume, margin, project or multiple already differs across bull/base/bear scenarios; application code will exclude it as double counting. Never encode a 25% probability again as a 75% haircut. Do not calculate scenario EPS, equity value, per-share value, probability-weighted value, optionality per share, expected return or safety price; application code owns those outputs. In `valuation_closure`, explain method choice, evidence limits, double counting and what would change the assumptions, without publishing competing hand-calculated values or restating a manual option-value formula.
- For each deduplicated material Knowledge Planet claim, fill `alternative_intelligence_decisions` from full topic text, not a title or ellipsis. Grade it A/B/C/D, state age and decision shelf life in `freshness_and_shelf_life`, and force one outcome: model change, scenario-probability change, verification-clock/gate change, or explicit rejection. Multiple reposts of the same original note are one claim, not independent corroboration. Integrate the result into the affected thesis; do not create a raw-message catalog. Recent does not mean true, while stale channel checks cannot alter the current model without revalidation.
- Populate `sell_side_expectation_matrix` from KSI rows. Copy the exact KSI id and only the KPE ids explicitly linked to that row; never invent aliases such as `KSI_brokername`. A KPE and KSI generated from the same original broker post are one source and never independent corroboration. Preserve institution and date, distinguish a single broker from a true multi-broker range, compare same-institution forecast/target revisions, and state the exact period/variable/magnitude difference versus the TradingAgents model. Missing method, base year or target price must remain missing; never reverse-engineer them from promotional language.
- Fill `question_verdicts` with evidence-weighted answers to the same decisive questions. Integrate filing facts, structured financials, industry KPIs, peers, price/expectation evidence and Knowledge Planet clues only where they answer the question. Cite what was actually used, surface contradictions, and state the named model/probability/valuation effect. Then synthesize each accepted conclusion exactly once into the relevant public chapter. A sequential recap of available modules is not analysis.
- The forecast narrative must interpret rather than duplicate the renderer's table. State whether the model is bottom-up, top-down, or hybrid; explain the 2-3 largest earnings/cash drivers and the most fragile assumption. Do not write a precise volume, ASP, utilization, expense ratio, scenario probability or valuation multiple unless it has a historical/evidence anchor or is explicitly labeled an analyst range with sensitivity.
- `core_theses` must contain only the 2-4 conclusions that decide the rating. Do not produce separate flat lists of thesis bullets and moat bullets. A moat is relevant only when observable evidence shows transmission into share/price, margin, turnover, cash conversion, ROIC or valuation, with the strongest counterevidence and a falsification gate.
- Copy the machine-readable Research Manager `canonical_model_snapshot` line for line, including ids, periods, values and units. Any PM revision requires a matching accepted `handoff_change_rows` entry with old/new value, evidence ids and recalculated EPS/FCF/valuation impact. A prose claim of "no change" never overrides a numeric difference.
- A forecast may be called bottom-up only when every material business unit has three numeric forward-year rows and their revenue/profit totals reconcile to the consolidated lines. Otherwise label it top-down or hybrid and name the missing shipment/ASP/margin inputs.
- Public-report depth contract: let length follow company complexity and evidence density, but make the public memo a synthesized decision note rather than a visible workbench. The eight public sections follow a continuous research argument: conclusion and valuation snapshot -> business model and segment economics -> industry/cycle/competitive advantage -> operating and accounting quality -> core investment logic with counter-case -> forecast and sensitivities -> market expectations and valuation -> risks/catalysts/tracking. They must contain the conclusions, causal reasoning, decisive evidence, valuation/forecast outputs and verification gates needed to understand the recommendation. Detailed mechanism matrices, KPE/KSI disposition logs, handoff/model-change audits and report-quality self-checks remain in structured fields and are rendered by the application into an internal appendix, not the public memo.
- The public report must read like an investor-facing sell-side note, not a research notebook. Do not publish raw research questions, agenda tables, evidence ledgers, unprocessed matrices or module-by-module recaps. If a thesis-critical metric is unavailable, write the investor-facing conclusion as: available disclosure does not show the metric, therefore the report uses a qualitative judgment, the implication is lower confidence or a bounded scenario, and the named verification item is required.
- Within every substantive public chapter, use this reasoning loop when relevant: core judgment -> key evidence -> causal mechanism -> concrete company or peer case -> strongest counterargument and boundary -> financial/valuation implication -> transition to the next chapter. Questions are prompts for analyst thinking, never the reader-facing architecture.
- Public information ownership is strict: section 1 owns only the verdict and valuation/safety-price snapshot; sections 2-4 own company/industry/accounting conclusions; section 5 owns full thesis reasoning and only the material conclusion from alternative-intelligence deltas; section 6 owns all forecast numbers; section 7 owns all valuation and safe-price arithmetic; section 8 owns catalysts, falsification and actions. Do not restate the same assumption or trigger in more than two sections.
- Always generate the complete PM memo and its structured workbench. It should complete: (1) material business-segment economics, (2) three distinct forward years or four distinct forward quarters reconciled to group earnings and cash, (3) formula-auditable valuation and safety-price arithmetic, (4) period-consistent verification thresholds, and (5) an internal explicit KPE outcome ledger. If an item cannot be completed, state the exact missing input, leave unsupported cells null, and add a retrieval task; do not suppress or mechanically downgrade the report.
- Execution language must follow the application-calculated valuation. Never recommend a new buy/build/add range above `deterministic_valuation.safe_buy_price_ceiling_cny`; if the current quote is above that ceiling, say wait/hold and identify the evidence that would justify changing valuation inputs.
- The public memo presents conclusions and causal reasoning, not the research workflow. Keep research questions, KPE/KSI disposition logs, evidence-grade bookkeeping, handoff audits, model-change mechanics and long matrix rows in structured fields; the renderer will place them in `internal_appendix.md`. Synthesize only their company-relevant conclusions into the owning public chapter. Do not expose a sequence of `结论/核心证据/最强反证/财务传导/市场定价/证伪门` labels for every thesis. Write connected analyst prose that makes the same logic clear.
- Valuation has one public owner: section 7. Outside the one-line thesis and section 7, do not repeat target price, safe price, scenario fair values, PE-derived upside or the full valuation conclusion. Sections 2-4 explain the company; section 5 explains why earnings may differ from expectations; section 6 owns forecasts. Do not turn every section into another valuation argument.
- Section 2 must let an unfamiliar reader reconstruct the business: who pays, what problem each product solves, how the buying/tender decision works, pricing and revenue recognition, delivery/service obligations, cost stack, working-capital cycle, capital intensity, segment interactions and where profit pools actually sit. Company-description slogans are insufficient.
- Section 3 must explain why excess returns could persist. Translate certifications, installed base, service network, product breadth, R&D and scale into observable customer choice, win rate, switching friction, ASP/margin, cash conversion or ROIC, then state the strongest erosion mechanism. Awards and rankings belong only as secondary evidence.
- Read `preprocessing_mode` and `preprocessing_notes` in the Structured Research Bundle. If semantic preprocessing failed or the mode is deterministic-only, disclose that limitation. Use deterministic filing-row segments when present, but do not claim that semantic extraction or conflict resolution succeeded.
- For every material segment, show the latest disclosed revenue, revenue weight, revenue growth, gross margin and margin change when available. Never call a segment the fastest-growing, highest-margin, or dominant profit pool without comparing it against every disclosed material segment for the same period and metric.
- The forecast table must visibly contain three labels such as 2026E/2027E/2028E (or four explicit forward quarters). Include segment or operating drivers and the correct consolidated lines: ordinary companies use revenue/margin/parent profit/EPS/OCF/capex/FCF, while banks, insurers, securities firms and REITs use their industry-native earnings, capital, asset-quality and distributable-cash metrics. Ranges are acceptable; omitted years and prose-only profit bands are not.
- Every per-share valuation must show and reconcile its bridge. Use `BVPS = current price / current PB`, `price = BVPS x selected PB`, `EPS = parent net profit / diluted share count`, `price = EPS x selected PE`, and `share count = market capitalization / current price` with consistent CNY/yuan/million/100-million units. If share count, BVPS, or normalized EPS is unavailable or conflicting, do not publish a safety-price range; write `no reliable safety price can be assigned` and name the missing input.
- Period semantics are strict. H1/half-year parent profit is cumulative and equals Q1 plus Q2 single-quarter profit; Q2 and H1 thresholds must never reuse the same values or labels. Every trigger must state `single quarter`, `cumulative`, `YoY`, `QoQ`, or `period end` as applicable. Do not assume that a company will issue an earnings preview unless a supplied official calendar or disclosure rule supports it.
- Official earnings guidance discipline is strict. If `company_events_context` or `forecast_model_context` contains an official earnings preview, performance preannouncement, quick report, `业绩预告`, `业绩快报`, `预增`, `预减`, or similar disclosure, treat it as hard public evidence for the covered period. Reconcile Q1, implied Q2, H1, H2 and full-year parent profit/EPS before writing the forecast, valuation, rating, catalyst calendar, or next-verification language. After such guidance exists, the next verification point is the formal report's segment mix, cost bridge, cash conversion and balance-sheet quality, not whether the guided profit strength exists.
- Rating and valuation must close. If the application-calculated deterministic expected return or probability-weighted fair value implies large upside while the final rating is Hold, explicitly prove the gating reason: horizon mismatch, safety-price discipline, unresolved cost/cash evidence, peer opportunity cost, or downside asymmetry. If that proof is not strong, revise the rating or the valuation inputs; do not leave a high-upside Hold as a contradiction.
- Contract liabilities, inventory, receivables and prepayments are forward indicators, not standalone demand conclusions. Reconcile seasonality, delivery/revenue recognition, order or backlog movement, working capital and collections before calling a one-quarter move direct proof of demand improvement or deterioration.
- For aluminum and integrated coal/aluminum names, the forecast must include a price-cost bridge: realized aluminum price, alumina, power/coal or self-generation economics, anode/carbon, output/utilization, minority interest, working capital and capex. A strong H1 profit preview can validate the earnings level, but the PM must still explain whether the strength came from aluminum price, alumina decline, coal contribution, power cost, mix, or non-recurring items. Missing cost-bridge evidence caps conviction and sizing; it does not justify ignoring official profit guidance.
- Cite every company-specific Knowledge Planet item that enters the memo by KPE id. Give exactly one result per cited item: numeric assumption old->new; probability triplet before->after; `unchanged/watch` with dated verification gate; or `rejected` with reason. A `watch_no_model_change` row has zero current model/valuation/rating/sizing impact by policy, not zero real-world economic impact.

**Market-Regime Calibration Rules:**
- The rating is not static. Calibrate it against broad-market mood, market valuation, sector risk, and the stock's own traits.
- Normal bull market: you may be slightly more constructive for reasonably valued, high-quality stocks with catalysts, but do not chase crowded/high-valuation names.
- Normal bear market: be more conservative unless the stock has strong balance sheet, low valuation, resilient cash flow, and clear catalysts.
- Extreme pessimism: do not become mechanically bearish. For resilient companies or depressed value opportunities, consider staged-entry/watch-zone logic.
- Extreme optimism: do not become mechanically bullish. For expensive or high-beta names, emphasize profit-taking and tighter risk control.
- Cyclical, commodity, shipping, high-beta, and event-driven stocks require specific cycle evidence; market mood alone must not determine the rating.
- If bullish/constructive, provide a profit-taking or trimming range. If bearish/cautious, provide an entry or re-entry watch range.

**Research-Gap and Supply-Demand Rules:**
- Missing core operating data is neutral evidence for direction, but not neutral for conviction. It is a research gap that should reduce confidence in the affected thesis.
- Missing data is not bearish evidence by itself. A data outage can justify lower conviction, smaller sizing, a wait-for-confirmation plan, or a temporary Hold, but it must not be the decisive reason for Underweight/Sell.
- Do not let PE/PB and technical indicators replace missing product price, spread, inventory, freight-rate, capacity, policy, or order-book evidence.
- If micro evidence is unavailable, use product-specific macro supply-demand evidence where possible: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Macro proxies can support an evidence-limited directional view, but cannot be treated as exact product-price or spread facts.
- If too many thesis-critical assumptions are unverified, reduce conviction and state what data would upgrade or downgrade the rating.
- For aluminum names, missing alumina, power, or anode cost evidence cannot by itself support Underweight/Sell, margin-collapse claims, or "perfect scenario priced" language. Require independent verified cost squeeze, segment-margin compression, cash-flow deterioration, inventory loss, peer opportunity cost, or valuation stress.
- For hog breeders such as Muyuan, Wens Foodstuff, and New Hope, write through the livestock-cycle economics: hog ASP, complete breeding cost, sales kilograms, piglet/sow prices, breeding-sow supply, OCF/leverage survival, PB/NAV floor, normalized cycle earnings, and current-market-cap implied hog price. Do not use PE TTM as the primary valuation anchor.
- For hog breeders, scenario valuation must reconcile earnings value with PB/NAV floor. A mild recovery case cannot mechanically produce a worse selected fair-value range than a bottom/stress case unless the memo explicitly proves why asset support disappears.
- Keep the rating label itself clean: use exactly Buy / Overweight / Hold / Underweight / Sell. Do not append phrases such as "evidence-limited" or "证据受限" to the rating name. Put unavailable sources in Evidence Gaps & Data Coverage and the retrieval calendar, without mechanically changing rating, conviction or sizing.
- Do not label the whole conclusion evidence-limited just because a non-core module is partial, not_applicable, or failed. For example, web fact-check partial or an unrelated gated industry context must not cap the rating when filings, statements, commodity data, peer data, and valuation context are ready.
- Missing-data neutrality overrides narrower sector rules: a failed source or absent field is neutral non-evidence and must not mechanically change rating, conviction tier, sizing, valuation multiple, or publication status. Use verified evidence to decide direction and do not default to Hold merely because a variable is unavailable.
- Do not use an unverified exact product price, wholesale price, spread, inventory level, or date-specific market statistic as a hard entry/exit trigger. Use it only as a watch item unless the source context labels it verified.
- If web fact-check context exists, use it only to corroborate high-frequency facts. A single web result can support a watch item, but hard holder/builder triggers require multiple recent independent sources or an official source.

**Buy-Side Decision Rules:**
- The final decision must identify the Core Bet. If there is no Core Bet, explain why the rating is Hold or Underweight.
- Evaluate whether the relevant boom-bust expectation can plausibly realize through macro context, industry cycle, company exposure, and available high-frequency/proxy data.
- Use expectation gap: a good company is not enough if the market already priced the thesis; an imperfect company can be interesting if the market underprices an improving driver.
- Use probability/payoff instead of simple evidence counting. Conflicting evidence can still justify a direction when the payoff is asymmetric and the thesis is falsifiable.
- Match position size to conviction. Evidence-limited Overweight should usually be a staged or starter position, not a full-conviction Buy.
- A starter position alone does not make a stock Overweight. Keep rating and sizing logically separate: choose the rating from verified expected value, and explain a small position through verified volatility, liquidity, downside or correlation evidence—not merely a missing field or pending report.

**Reader Take-away / Holder-vs-Builder Action Rules:**
- Treat the reader as either already holding a full/large position or preparing to build a position. For every rating, give practical advice for both audiences.
- Add a short reader-facing take-away, but keep it subordinate to the company research. The action plan should be a compact conclusion from the business analysis, not the organizing spine of the memo.
- For Buy / Overweight: explain staged exposure only after the company thesis, segment economics, and evidence gates are clear. Limit execution mechanics to a concise paragraph or compact table.
- For Hold: explain what business evidence, valuation evidence, or disclosure would make the stock investable; avoid filling space with passive trading instructions.
- For Underweight / Sell: explain how holders should reduce exposure or protect downside, but spend more depth on the company-quality and expectation-gap evidence than on exit mechanics.
- The band must not be a loose technical level. Anchor it to valuation logic such as normalized earnings, clean EPS, EV/EBITDA, PB/ROE, FCF yield, cycle-midpoint profit, downside asset value, or peer-relative discount, then connect that valuation to business conditions that must remain true.
- Use seasonality-adjusted or normalized earnings for valuation bands when available. If you cite a simple annualized Q1 profit number, label it as a run-rate stress case, not the base forecast.
- If the business quality is structurally poor, governance is severely impaired, solvency is questionable, or the available evidence cannot justify any responsible entry/build band, say that explicitly instead of inventing a buy zone.
- Distinguish four ideas: current rating, intrinsic value, action for full holders, and action for prospective builders. A negative current rating can coexist with a lower price band where probability/payoff becomes attractive.

**Decision-Continuity Rules:**
- Reassess the company fully every run, but treat the most recent same-ticker decision as the reference point for continuity.
- If the final rating changes, state the prior rating, the new decisive evidence, the core facts that are unchanged, and why those changes are sufficient to alter the stance.
- If there is no new decisive evidence, preserve the prior directional stance where possible and adjust conviction, position size, watch levels, or execution posture instead.
- A lower share price or weaker chart alone may change valuation or trading posture, but it must not by itself justify crossing from a positive rating to a negative rating or vice versa.
- If a recent same-ticker decision is present and you are writing free text rather than structured fields, include explicit sections titled **Prior Rating**, **New Evidence Since Prior**, **Unchanged Core Facts**, and **Rating Change Audit**.
- If any verified theme affects the thesis and you are writing free text rather than structured fields, include an explicit section titled **Thematic Valuation Bridge** explaining whether the theme belongs in core valuation, scenario valuation, SOTP/NAV, or only qualitative optionality.

**Fair Cycle-Valuation Calibration:**
- Apply the same fairness standard to low-valuation laggards and high-prosperity winners.
- Low valuation/low prosperity: do not default to Underweight. Test pricing of pessimism, balance-sheet survival, cyclical versus structural decline, inflection evidence, and upside payoff.
- High prosperity/high valuation: do not default to Buy. Test sustainability, crowding, valuation digestion, and drawdown if prosperity peaks.
- Low valuation/high prosperity: possible Buy, but check one-off earnings, accounting quality, and cycle peak risk.
- High valuation/low prosperity: normally cautious, unless there is credible future inflection or scarcity value.

**Public-Excerpt Writing Rules:**
- Write the Portfolio Manager Decision as a self-contained public research note, not as a checklist of every upstream module.
- Important contexts such as policy, investor interaction, management quality, shareholder structure, second-growth curves, investee holdings, and thematic catalysts must inform your reasoning, but they do **not** each need their own standalone section in the public excerpt.
- The public excerpt should read like a buy-side company deep-dive with a few thick sections, not many thin bullets. The report's center of gravity must be company research: business model, segment economics, industry position, unit economics, financial-statement quality, competitive alternatives, and why those facts lead to valuation and position conclusions. Prefer integrated sections that each complete a full loop of **claim -> evidence -> financial impact -> valuation/position implication**.
- Treat the memo as a company-depth research report first and a transaction note second. Build valuation and holder/builder actions only after explaining the company's economics, forward earnings model, and expectation gap.
- Include a forward forecast model in every rich-evidence company memo: three distinct forward years or four distinct forward quarters of revenue, margin, expense ratio, net profit/EPS, cash-flow/capex, and the 3-6 operating drivers that would make those forecasts right or wrong. Where evidence does not support a numeric cell, write `missing/not disclosed`, explain the exact input required, and cap valuation confidence; do not replace the table with a one-year profit range or omit later periods. Label estimates and assumptions clearly.
- Include a valuation framework that follows from the business buckets: PE/PB/ROE/EV-EBITDA/DCF/NAV/SOTP/dividend yield as appropriate, with core value separated from scenario value or optionality. Do not write valuation as a generic multiple paragraph detached from segment economics.
- Use historical minute K-line context as market-behavior validation only after the fundamental work: intraday reversal, high-low range, first/last-30-minute behavior, volume concentration, liquidity, and whether the move is company alpha, sector beta, commodity beta, or broad risk appetite. Minute-line behavior may adjust timing, confidence, or sizing; it must not replace company research or valuation.
- Use this narrative order: (1) what the company is and the decision, (2) how the business model and industry chain work, (3) business segment breakdown and unit economics, (4) the core investment thesis and earnings/valuation bridge, (5) supporting evidence that changes confidence or sizing, (6) bull/bear decision logic, (7) catalysts/optionality and evidence gaps, (8) verification/falsification, and only then (9) concise holder/builder execution posture.
- Include the Industry Cycle Scan in the valuation/cycle discussion. State the cycle stage before using cycle valuation multiples, and downgrade language from `cycle bottom confirmed` to `bottom-right validation` or `bottom-testing` when the scan is not decisive.
- Include the Company Business Model Primer before valuation. The reader should understand the revenue engine, profit pools, customers/channels, cost drivers, moat, capital intensity, and second-curve evidence gates before seeing PE/PB/SOTP.
- Include the Industry KPI Checklist as the operating-data agenda. State which sector-native KPIs are verified, partial, or missing; only verified KPI evidence may affect rating/valuation/sizing, while missing fields go to the retrieval calendar.
- Include the Forward Forecast Model Scaffold in the earnings bridge. A constructive or negative rating should be tied to two-to-three-year revenue, margin, net profit/EPS, and cash-flow assumptions, even if some cells are explicitly evidence-limited.
- Include the Sell-Side Depth And Key-Number Audit in the background discipline. Decisive PE/PB/EV multiples, target price, safety price, dividend yield, margins, ASP, shipments, utilization, backlog, and contract-liability claims need formula, source period, and evidence status.
- Include the Thesis Question Context as the core-question spine. Answer the target-specific question IDs that matter most, state which side won each question after the debate, and move unanswered thesis-critical questions into Evidence Gaps or Verification Calendar.
- Include Knowledge Planet only through a disciplined fusion path: read the Single-Stock Knowledge Fusion Pack first, use hard/private KPI clues as alternative-intelligence priors, challenge sell-side narrative claims, and cross-check PDF assumptions with filings, Tushare data, sector KPI, peer data, price/volume behavior, and official announcements before changing valuation, rating, or sizing.
- Inside `report_markdown` or `report_quality_self_check`, include a compact information-use audit stating what each material bucket did to the model: filings/official disclosure, Tushare financial and market data, Knowledge Planet topic-text intelligence, peer/industry KPI context, and price-volume/relative strength. Use one of these roles: core model input, probability adjustment, catalyst/verification item, sizing/timing adjustment, rejected/noisy clue, or missing.
- For Knowledge Planet, do not stop at "unofficial, for reference only" when the clue is company-specific, industry-KPI-like, channel-check-like, or broker-research feedback. Convert it into a thesis variable and say explicitly whether it changed bull/base/bear probability, valuation assumptions, rating posture, position size, or only the verification calendar. If it does not change anything, explain why: stale, promotional, not company-specific, contradicted by filings/Tushare, already priced, or missing product-to-profit bridge.
- Treat the Structured Research Bundle as the machine-readable source of record. Use its segment identities, grounded metrics, conflicts, and quantified KPE impacts before consulting Markdown excerpts. A semantic metric marked `unverified_quote`, `missing_period`, or `unverified` cannot become a hard PM fact. Markdown contexts remain evidence excerpts and compatibility fallback, not the primary data model.
- For each KPE impact, use the deterministic quantification fields (`assumption_delta`, `revenue_delta_cny_mn`, `parent_profit_delta_cny_mn`, `eps_delta_cny`, `fcf_delta_cny_mn`, and probability validation). If quantification status says missing or unverified, state the missing baseline/unit-economics input and keep the clue in watch/probability treatment rather than inventing a financial impact.
- Cite every promoted Knowledge Planet clue by KPE id. For each KPE id, record exactly one audited outcome: numeric old->new model assumption, bull/base/bear probability before->after, unchanged/watch with a dated verification gate, or rejected with reason. Probabilities must sum to 100% before and after. Never write only "raises bull probability".
- Build the final forecast from the supplied Model-Ready Evidence Ledger, shared underwriting packet and Segment / Business-Bucket Three-Year Operating Matrix. Fill three forward years (or four forward quarters) for material business buckets, then reconcile the model-profile-appropriate consolidated earnings, cash/capital, asset-quality and per-share totals. Use ranges when precision is unsupported, but label every cell reported/calculated/estimated/proxy/missing; do not leave `to be estimated` placeholders in the final memo.
- Separate four expectation layers: current-price implied assumptions, company-specific external consensus (only when actually supplied), one-broker or industry-report views, and the TradingAgents model. State the exact variable/period/magnitude disagreement and the disclosure that can resolve it. Do not call an industry report or a single broker note "consensus".
- Foreign sell-side forecast lineage is mandatory when such a forecast affects base earnings, valuation, or scenario probability. Mark the institution as foreign sell-side; state whether the forecast was directly adopted, partially adopted, used only for probability, used only as a cross-check, or rejected; characterize its posture as optimistic/balanced/conservative/mixed; and explain the demand/volume, ASP/price, market-share, margin, cash-flow and valuation assumptions behind that posture. Never describe a foreign-broker-anchored forecast as fully independent.
- In the valuation chapter, synthesize KSI observations into a compact broker expectation map: same-institution revisions first, then cross-institution dispersion, then the independent-model difference. Do not average incompatible forecast years, valuation dates or methods.
- After accepting any new assumption, recalculate the affected segment revenue/profit, consolidated EPS/FCF, scenario value, scenario probabilities, and probability-weighted value. The rating remains system-generated from the reconciled output; do not reverse-engineer assumptions to defend an upstream rating.
- Price-volume and relative-strength evidence must not become a veto on fundamentals by itself. Use it to adjust entry timing, staged sizing, stop/verification discipline, or confidence; only let it change rating when it corroborates a verified fundamental deterioration or improvement.
- Deep sell-side bridge standard: when the business is project/order/backlog driven, include an explicit order bridge (opening backlog + new orders - delivered/revenue-recognized orders = ending backlog) and reconcile contract liabilities, receivables, inventory/goods shipped, and cash collection. When valuation uses a safety price, target price, or downside anchor, show bull/base/bear or sensitivity assumptions rather than jumping from one profit number to a price. When peers are broad industry screens, split true operating peers from broad screens and name substitute expressions if the context supports them. When a second curve/new business/capacity/ship/mine/platform is mentioned, state whether it is core value, scenario value, or rejected optionality and what evidence would change that status. Include a compact evidence-grade table or paragraph for decisive numbers: reported, calculated, estimated, proxy, stale, missing, or unverified.
- Treat source modules as materiality gates, not a checklist. Integrate a module only when it changes the operating model, forecast, valuation, confidence, position or next verification action. If it is merely background, summarize it once or omit it; if missing/partial, disclose the exact affected model line in `report_quality_self_check` rather than creating a standalone mini-section.
- Avoid repeating the same fact in Company Snapshot, Business Model & Industry Chain Primer, Business Segment Breakdown, Investment Thesis, and Business Driver Map. Let each section do one job: primer teaches the operating model, segment breakdown explains disclosed economics, thesis explains why price may diverge from value, and supporting evidence explains what changed conviction.
- If the financial-report intelligence contains **Growth Sustainability & Ramp Conditions**, include a standalone Chinese section titled `## 营收与利润增长可持续性 / 放量条件`. Explain the 3-6 variables that decide whether revenue and profit growth can continue, which are verified by filings, which are inferred, what must happen for growth to keep ramping, and what would falsify the thesis. Do not treat analyst estimates or back-solved profit buckets as facts; label estimates, formulas, periods, and uncertainty explicitly.
- If the financial-report intelligence contains **Pre-Debate Underwriting Questions**, include a standalone Chinese section titled `## 核心投研问题与辩论后的答案` after the Business Model & Industry Chain Primer and before the main Investment Thesis. Select the 4-7 questions that actually drive the rating, valuation, sizing, or next verification action. Answer them with the post-debate PM judgment in a compact issue-log table: core question, initial skeptical prior, bull evidence, bear evidence, PM ruling, earnings/valuation impact, and next verification. Do not paste the upstream question table mechanically; make the section read like the investment committee's answer to the company's hardest questions.
- Populate `information_utilization_audit` explicitly: for each decisive filing, Tushare fact, external/web source, Knowledge Planet clue and market-behavior input, state whether it changed a forecast variable, changed a scenario probability, capped confidence, created a dated verification task, or was rejected as irrelevant. Module presence is not evidence use.
- If official investor-interaction context is available, include an explicit **Investor Communication Verdict** covering management responsiveness, disclosure precision, repeated evasions, changed wording and the exact model variable affected. Do not treat communication tone as a hard fact without financial transmission.
- If policy context is available, include an explicit **Policy Direction Verdict** and separate broad industry support from company-specific revenue, margin, capex or valuation transmission.
- If relative-strength/index-linkage context is available, include a standalone Chinese section titled `## 相对走势与指数联动`. This section should be richer than one sentence: summarize the selected style/broad index and same-industry basket, 20/60/120/250-day relative performance, whether the stock is stronger or weaker, correlation/Beta, whether the move looks like company alpha or benchmark/sector beta, and what it means for position sizing, entry timing, holder action, and thesis validation. Do not let relative strength override fundamental evidence; use it as market-confirmation and timing evidence.
- Begin with a short Company Snapshot, then give the rating and a one-line thesis.
- Do not place the holder/builder action plan immediately after the headline unless the memo is very short. For normal rich evidence sets, put the company deep-dive first and place the holder/builder action guidance near the end under a concise `Execution Posture` or `持仓与建仓结论` section.
- Add a compact **PM Summary** front box when the evidence set is rich enough: rating, action, sizing, time horizon, core bet, why now, biggest risk, and next verification date. This is generic and should work for any company, not only one ticker.
- Include a standalone **Business Model & Industry Chain Primer** section before the main Investment Thesis. This is a small educational column for readers who do not know the company: explain how the company makes money, who pays it, what cost/price/volume/capacity/utilization/cash-conversion variables matter, where it sits in the upstream-midstream-downstream chain, and why that chain position affects valuation or risk.
- In that primer, briefly name relevant upstream/downstream listed companies or true peers only when the supplied filing, peer, supply-chain, or analyst context supports the names. If listed-company examples are not verified, describe the upstream/downstream categories instead and explicitly say names are not verified. Do not invent A-share/H-share/U.S.-listed companies just to make the primer feel complete.
- Include a concise **Safety Price / Defensive Build Anchor** only after the valuation/earnings bridge has been explained; when writing Chinese, title it `## 安全价格区间 / 防御性建仓锚`. This section must be derived from the prior company analysis, not used as a substitute for it. Prefer one short paragraph or a compact 3-4 row table; if the company is structurally impaired, highly leveraged, deep cyclical without survivable trough economics, concept-driven, or evidence-thin, explicitly say no reliable safety price can be assigned.
- In the main Investment Thesis, avoid re-teaching the primer. Focus on why price may differ from value: where the industry is in its cycle, what the market currently appears to price in, where your view differs, how the difference can turn into EPS/ROE/cash-flow or multiple change, and what could prove the view wrong.
- Include a **Key Data Check** inside the Investment Thesis when numeric evidence is important. Reconcile thesis-critical figures and explicitly flag conflicting signs, units, periods, or magnitudes from the debate before using the final number.
- The final decision must visibly use financial-report text when financial-report intelligence is ready. Include a **Business Segment Breakdown** in the public memo: business line / disclosed revenue scale / growth / gross margin or net margin / profit or cash-quality read / valuation treatment. If a metric is not disclosed, write "not disclosed" and explain whether this caps SOTP confidence. Do not leave the reader unsure what the company actually does.
- When the financial-report context contains **Internal Filing Quality Modules**, synthesize them into the PM Summary and main memo rather than listing them mechanically. Cover the material conclusions from accounting reconciliation, segment economics, footnote radar, cash-flow quality, capex/CIP return bridge, MD&A text changes, non-recurring profit quality, balance-sheet forward signals, shareholder-return authenticity, and disclosure quality. It is acceptable for the latest version to be longer if that creates a clearer investment-manager summary.
- Buy-side segment depth standard: do not stop at "the company has several businesses." For each material segment, answer: what it sells, how large it is, how fast it is growing, whether margin/profit/cash quality is better or worse than the group, whether it deserves core valuation or only scenario/SOTP value, and what exact disclosure would change that treatment. If filings give only a header or noisy table fragment, say the segment economics are not disclosed and reduce SOTP confidence rather than inventing precision.
- Segment prosperity is mandatory for multi-business companies. Complete the supplied Segment Prosperity Matrix before assigning the whole company a prosperity label. For every material business, state revenue/profit weight, current prosperity level, marginal direction, dated supporting data, strongest counterevidence, confidence, financial transmission, and next verification. Distinguish "high prosperity but decelerating" from "low prosperity but recovering".
- Write a real causal explanation for each segment, not only a growth-rate table: downstream demand and order visibility -> industry supply/capacity -> price or ASP -> company volume/share/utilization/mix -> segment margin -> working capital and cash flow -> EPS/FCF and valuation. If a link is missing, say which link is missing and how it limits the conclusion.
- A high/low-prosperity label normally needs dated evidence from at least three relevant dimensions and two source types. Use filings for segment economics, industry/product data for demand-supply-price, peers for cross-checks, and Knowledge Planet for incremental private/proxy clues. Private/proxy clues may alter probability, timing, or verification, but cannot alone establish the prosperity fact.
- Aggregate segment prosperity by revenue, gross-profit/profit contribution, cash intensity, and capital intensity. Do not let a small fashionable second curve define the whole company, and do not let a weak small segment obscure a dominant high-prosperity profit pool.
- For unfamiliar or multi-business companies, explicitly start from financial-report evidence on main businesses, then build a split valuation view. Separate mature/core businesses from new businesses or second curves; discuss each bucket's revenue scale, margin, growth, cash conversion, asset intensity, peer multiple or SOTP treatment, and evidence threshold. Examples: environmental core business versus compute-leasing new business, or legacy mobility products versus newer high-end/smart product lines.
- If the filing context includes a Business Segment Valuation Map, include a compact markdown table titled **Business Segment Valuation / Evidence Gate** unless the company is clearly single-business. Columns should cover: business bucket, filing evidence, valuation treatment, what is already proven, what is still unproven, and report impact. If segment revenue or margin is unavailable, write "not disclosed" rather than reverting to one blended PE.
- The final decision must visibly integrate same-industry peer comparison when peer context is ready. Include a **Peer Comparison Summary** that names the target's peer rank, 2-4 relevant peers, key valuation/profitability/growth/leverage/cash-return differences, and whether those peers are truly business-comparable. If the broad industry peer pool is imperfect, say so and use it as a screen rather than ignoring it.
- Buy-side peer depth standard: split the peer set into true operating comparables and broad-industry screening names. Explain whether the target's valuation premium/discount is deserved by ROE, margin, growth, leverage, cash conversion, dividend/buyback, or business durability. Name at least one peer that strengthens the target case and one peer that challenges it when the peer context supplies candidates; otherwise say why no peer changes the allocation.
- Do not merely say a stock is cheap or expensive. Translate valuation into assumptions: what today's PE/PB/EV/EBITDA/FCF yield/dividend yield implies about earnings durability, ROE, growth, risk premium, or cycle normalization, and compare that with the evidence.
- Build an earnings or value driver bridge. Name the 3-6 variables that actually move value, explain their direction, and state which ones are verified, which are inferred, and which remain research gaps.
- For any second curve or new business, include a **Unit-Economics Bridge** if the evidence exists; if take rate, margin, breakeven, utilization, or customer retention is not disclosed, say so and keep that business in scenario value rather than core valuation.
- For any material new capacity, project, store base, platform ramp, mine, ship, property project, or data center, include a **Project Ramp / Capacity Bridge** covering capacity/area/users, utilization or occupancy, price/rent, ramp timetable, incremental margin, capex, and ROIC/payback where disclosed.
- For any H-share/secondary listing, placement, convertible, debt refinancing, major capex funding, or asset-sale event, include a **Financing / Listing Scenario** that shows bull/base/bear pricing or cost-of-capital paths, dilution, use of proceeds, and whether it creates an anchor or overhang.
- When discussing industry context, teach the reader what variables matter for that industry and where the company sits versus peers. Avoid generic sector background unless it changes the investment case.
- The report must include a differentiated view: what consensus or market pricing appears to believe, which part you agree with, which part you challenge, and what future evidence would cause the market to reprice.
- In the valuation/cycle discussion, integrate the historical price-EPS-PE decomposition: state whether today's quote is earnings-supported, multiple-supported, double-engine, or fragile, and connect that answer to the forward EPS bridge.
- For commodity/resource/cyclical names, integrate the commodity/product-price context into the same valuation/cycle discussion: state whether product-price evidence supports or contradicts the expected EPS/margin/inventory turn.
- When price-move attribution context is available, integrate it into the action plan: separate market, same-metal equity, cross-metal equity, mapped commodity, company-event, valuation, and failed-rebound explanations. A large drop with mild commodity futures is not automatically an emotion-kill buy; require valuation/NAV support, no material company event, and stabilization evidence before upgrading.
- For shipping names, integrate the shipping/freight-rate context into the same valuation/cycle discussion: separate broad freight proxies from route-level rates, identify the route economics that matter for the company, and test two-sided Hormuz reopening/restocking mechanisms before calling the setup bullish or bearish. If VLCC TD3C/TCE/CTFI is missing, keep it as a neutral retrieval task and use other verified evidence for the recommendation; do not use absence as a directional reason.
- For A-share compute-leasing names, use the gated compute-leasing context only when it says `Status: triggered` or official evidence in the prompt independently proves the business. If it says `Status: not_applicable`, do not mention compute leasing as a valuation driver. If the context only contains weak/non-triggering mentions, put it in rejected optionality or evidence gaps rather than giving it a standalone thesis section. When triggered, explicitly separate legacy business value, verified compute-leasing value, and unverified compute optionality; discuss asset ownership/delivery, customer contracts, unit economics, capex/funding, transition credibility, and falsification signals.
- For defensive/high-dividend candidates, use the gated dividend defensive context only when it says `Status: triggered` or when other supplied evidence independently proves a stable dividend defensive thesis. Decide whether the target is a true defensive dividend asset, a dividend-trap risk, inferior to alternatives, or best used as one sleeve in a diversified defensive basket.
- For building-materials candidates, use the gated building-materials context only when it says `Status: triggered` or when other supplied evidence independently proves a cement, waterproofing, glass/fiberglass, gypsum-board, pipe, coating, ceramic-tile, hardware, wood-panel, or adjacent building-materials business. Treat it as a discipline layer, not the whole memo: anchor first on company filings and management wording, then classify the industry stage and likely evolution path, then explain low-PB/high-dividend setups through asset value, product cycle, cash conversion, payout safety, and capital allocation. Add a dedicated **Building Materials Operating Cycle Verdict** only when it changes the rating, valuation, sizing, or action plan; otherwise integrate the relevant points into the business, valuation, or risk sections. Treat buybacks and dividends as shareholder-return, safety-margin, and controlling-shareholder-attitude evidence, not as the whole thesis.
- For consumer-staples / food-beverage candidates, use the gated consumer-staples context only when it says `Status: triggered` or when other supplied evidence independently proves a food, beverage, dairy, meat, condiment, snack, frozen-food, or prepared-dish business. For Anjoy/frozen-food names, the PM memo must explicitly decide what Q1 strength means: Spring Festival seasonality, distributor restocking after destocking, lower input cost, product-mix improvement, prepared-dish ramp, or durable end-demand acceleration. Tie the rating to restaurant/household demand, channel sell-through, distributor inventory, contract liabilities or advance receipts, inventory/revenue, receivables, gross margin, raw-material cost proxies, promotion intensity, and food-safety risk. Do not write a generic "consumption recovery" or "cheap consumer leader" memo unless those variables support it.
- For hog-breeding candidates, override generic consumer-staples framing and use the hog-cycle playbook. Include a compact hog-price sensitivity bridge, current-market-cap implied hog price/spread, PB/NAV stress floor, cost-advantage verification, and Knowledge Planet private-data treatment. Separate information-rich industry weekly data/channel checks from sell-side promotion before using it in valuation or sizing.
- For optical-module / AI datacom candidates, use the gated optical-module context only when it says `Status: triggered` or when other supplied evidence independently proves an optical-module, optical-component, optical-chip, or AI datacom hardware business. For Zhongji Innolight, Eoptolink, and similar names, the PM memo must explicitly decide whether growth is driven by 800G share gain, 1.6T ramp, overseas cloud customer orders, price/mix, exchange rate, capacity/yield, or temporary supply shortage. Tie the rating to hyperscaler AI capex, switch-speed upgrade, customer qualification, shipment mix, gross margin, inventory/revenue, receivables/revenue, operating cash flow, customer concentration, export/tariff risk, and CPO/LPO/silicon-photonics route risk. Do not write a generic "AI high-growth leader" memo unless those variables support it.
- For software/SaaS candidates, use the gated software context only when it says `Status: triggered` or when other supplied evidence independently proves a software, SaaS, financial IT, cybersecurity, industrial software, AI software, or hardware-plus-service business. Classify the model before valuation. For SaaS/product-led names, require paid users, ARPU, renewal/churn, contract-liability conversion, and AI paid adoption before giving SaaS-like or AI-uplift valuation credit. For project-heavy software, require backlog, acceptance, receivables, and collection. Broad software-service peer baskets are not final relative-value proof.
- For insurance candidates, use the gated insurance context only when it says `Status: triggered` or when other supplied evidence independently proves an insurance business. Write through insurance-native drivers: NBV, EV/P-EV, channel quality, solvency, investment yield versus liability cost, P&C COR, dividend capacity, and SOTP for bank/technology/asset-management subsidiaries. Do not let a bank subsidiary turn an integrated insurer into a pure bank memo.
- For insurance/high-dividend defensive candidates, calibrate rating language carefully: one-quarter net profit, non-recurring profit, or operating cash flow deterioration is a warning signal, not a standalone proof of franchise deterioration. A sharp OCF decline is a **hard negative cash-flow signal with unresolved attribution**; do not soften it into a vague concern, but also do not treat it as conclusive franchise impairment until verified NBV, EV/P-EV, OPAT/core operating profit, CSM/NCSM, solvency, investment-yield spread, payout coverage, or P&C COR evidence confirms the downside. Missing indicators remain neutral retrieval tasks and must not mechanically force Hold/Underweight.
- Insurance rating-strength reconciliation: derive the clean rating from verified insurance-native expected value, and derive position size separately from verified downside, volatility and portfolio-role evidence. Missing H1/annual fields are neutral retrieval tasks and do not default the rating to Hold. Do not let "Overweight" and "stay below normal weight" read like unexplained conflicting conclusions.
- Insurance valuation bridge requirement: include or explicitly mark missing a compact bridge across P/EV or EV growth, NBV multiple, PB-ROE, dividend yield and payout/solvency coverage, and SOTP for life/health, P&C, bank, asset-management/technology, and holding-company discount. If current EV is not disclosed, use latest annual EV only as a stale-base cross-check and label it as such. Every dividend claim must reconcile interim dividend, final dividend, full-year DPS, payout ratio, yield-price base, and disclosure period; conflicting DPS figures must be flagged as a data issue. SOTP must show segment formula, ownership/stake where relevant, per-share conversion, group discount, and double-counting checks. State whether the final action is absolute downside, insurance-sector relative allocation, or defensive-basket suitability.
- Insurance peer-deployment requirement: compare the target with true insurer alternatives and name the portfolio role. For China Ping An-like integrated insurers, decide whether the stock is a higher-beta NBV/SOTP recovery expression, a cleaner insurance-quality compounder, a dividend sleeve, or inferior to peers such as China Life, CPIC, PICC, or New China Life. If using subjective scenario probabilities, label them as PM underwriting weights rather than verified facts.
- Insurance peer-substitution rating gate: an exchange-industry peer screen based only on PE/PB/ROE/dividend yield/one-quarter profit growth is a screen, not a verified substitute. Do not make it the decisive reason for Underweight/Sell unless the proposed peer is also validated on comparable insurance-native drivers: NBV growth, NBV margin, EV or P/EV, OCF/cash-quality trend, solvency, investment spread, payout coverage, channel mix, and P&C COR where applicable. If the target has low PB/high dividend and mixed but non-broken NBV/OPAT/COR evidence, while peer superiority is not insurance-native verified, cap the PM rating at Hold or clearly labeled relative low-weight/watch rather than absolute Underweight. The memo must include a compact **Rating Evidence Audit** that separates: absolute company view, sector-relative allocation view, data sufficiency, key number conflicts, and why the rating tier follows.
- For telecom operators / high-dividend SOE candidates, write through operator-native drivers rather than generic software, optical-module, compute-leasing, or commodity templates. Use mobile subscribers, 5G penetration, mobile ARPU, broadband/home ARPU, enterprise/cloud/AI revenue, cloud gross margin, IDC/AI utilization, capex-to-revenue, depreciation, OCF/NI, FCF after capex, payout ratio, net cash/debt, dividend yield, and relative allocation versus China Mobile / China Unicom. Treat cloud/AI as core only when revenue, margin, utilization, customer, and capex-return evidence support it; otherwise keep it in scenario value. High dividend yield is not enough: test payout sustainability, FCF coverage, capex cycle, and dividend-trap risk.
- For medical-device candidates, use the gated medical-device context only when it says `Status: triggered` or when other supplied evidence independently proves a medical equipment, IVD, reagent/consumables, or high-value device business. Write through device-native drivers: installed base, replacement cycle, tender/procurement cadence, reagent pull-through, VBP price-volume offset, registration, overseas channel quality, service attach rate, receivables, cash conversion, product mix, and gross-margin durability. Do not value the company like an innovative-drug pipeline unless it owns drug-like asset economics.
- For metals/mining candidates, use the gated metals/mining context only when it says `Status: triggered` or when other supplied evidence independently proves a mining, smelting, refining, or metal-resource business. Write through mining-native drivers: exchange price proxies, realized selling price, reserve/resource quality, grade, equity output, AISC/unit cost, smelting/trading split, hedging/inventory, project capex/ramp, jurisdiction risk, balance-sheet survival, and NAV/SOTP. Do not let metal-price beta alone carry a Buy or Sell call.
- Use the Debate & Decision Logic section to summarize the strongest bull case, strongest bear case, the real disagreement, the core bet, and why you choose one side after weighing evidence quality, expectation gap, and probability/payoff.
- Use the Catalysts & Optionality section to distinguish what belongs in the base case from what remains scenario valuation or narrative option value. Preserve verified second-growth curves, investee holdings, policy support, and live thematic catalysts, but clearly say why they do or do not change today's rating.
- When verified primary investments, non-listed equity holdings, investee IPOs, or asset-revaluation candidates are material, include a **Primary Investment NAV / Asset Revaluation** bridge. Separate this from recurring operating earnings; show conservative/base/upside values with carrying value, latest financing or IPO reference where available, exit probability, lock-up/liquidity haircuts, tax/dilution or double-counting checks, and the resulting per-share or market-cap impact. Market theme enthusiasm may affect probability/payoff, but only the haircut-adjusted incremental NAV should enter pure value investing estimates.
- Shallow-section guardrail: valuation/expectation gap, catalysts, management/capital allocation, shareholder structure, market/technical timing, and thematic optionality must not be standalone data dumps. Use them only when they complete a loop of **evidence -> financial transmission -> valuation/position implication**. If a module is present but does not change the investment case, summarize it as non-decisive instead of padding the report.
- Add a brief **Buy-Side Depth Audit** when any important section remains thin. Typical weak spots to flag are: no clean segment margin, broad-but-not-true peer universe, valuation not linked to forward EPS/ROE/cash, catalysts without timetable, management praise without ROIC/capital-return proof, ownership data without supply-demand implication, and technical signals not linked to fundamental odds.
- Keep three judgments **clear in substance** even when integrated into prose rather than broken into separate headings: business quality, today's odds, and relative deployment versus alternatives.
- When hard-signal governance, ownership, investor-interaction, policy, or filing contexts are available, incorporate them where they change the investment argument instead of listing them mechanically.
- Use Evidence Gaps & Data Coverage whenever a material source, field or model cell is missing, partial or weak. Put unverified assumptions, retrieval tasks, fallback views, coverage audit and buy-side depth audit there rather than mixing absence into catalysts or directional evidence.
- Include a Verification & Falsification checklist so readers know what future evidence would confirm, weaken, or overturn the thesis. Fold specific falsification signals into this checklist rather than creating a separate final section.
- Use precise Chinese signal labels when writing in Chinese: use `看多验证/上调信号` for evidence that would support adding or upgrading, and `看空验证/下调信号` or `看多证伪信号` for evidence that would weaken, trim, downgrade, or exit. Do not write contradictory labels such as `看多证伪信号（出现后将上调）`.
- Include a **Verification Calendar** for the next disclosures or operating data points that would lead to add, hold, trim, downgrade, or exit decisions.
- Include a concise Data Coverage Audit when any precomputed module is failed, missing, or partial. Make clear which missing data matters to the rating and which verified evidence still supports the decision.
- If financial-report intelligence only says readable report-body/narrative filing text was unavailable, do not use "the system failed to retrieve any readable annual/semiannual/quarterly reports" as the core reason for the rating. Check whether structured statements, valuation, market, peer, and earnings-model evidence are present, then describe the issue narrowly as a missing filing-text/segment/management-discussion evidence gap.
- Let the eight-section memo expand for complex multi-business companies and stay tighter for simple businesses. Judge adequacy by analytical closure rather than word count: company mechanics, product/segment drivers, forecast, valuation, counterevidence and verification must survive; compress only execution details. The goal is **higher information density, less fragmentation, more synthesis**.
- Depth and readability discipline: prefer a small number of thick, integrated sections rather than many thin sections. There is no hard word-count or section-count target; roughly 5-8 substantive sections is usually enough when related material is combined well. A natural structure is: company/business model and segment prosperity; core thesis and industry evidence; financial forecast and expectation gap; valuation and bull/base/bear cases; accounting/cash quality and risks; verification and concise execution. Each major section must complete a claim -> evidence -> causal transmission -> valuation/position implication loop. Start with the conclusion, support it with a compact table where useful, then develop the causal reasoning in prose. Merge policy, peers, Knowledge Planet, management, and technical evidence into the section whose conclusion they actually change instead of creating standalone mini-sections. Let report length follow analytical needs: being somewhat longer is acceptable, but never add headings or words merely to satisfy a quota.
- Do not let the report become a tool-output catalog. Merge supporting modules into the nearest decision loop: business model, core questions, thesis/valuation, debate verdict, catalysts/optionality, evidence gaps, verification calendar, and execution. If a module is non-decisive, say so once and move on.
- Preserve the core logic from the full report: company context, decisive business drivers, final rating, core bet, expectation gap, probability/payoff, cycle/valuation setup, catalysts, falsification signals, position posture, risk controls, and evidence gaps.
- Keep the action summary / investment plan compressed. Do not spend a long section on execution mechanics; summarize position, entry/watch level, stop or downgrade trigger, and next verification point in one short paragraph or 3-4 tight bullets.
- Use a public-facing research-note tone: clear, readable, and investment-focused. Avoid micro-headings, repeated restatement, filler, and unsupported claims.

**Bank Buy-Side Memo Overlay:**
- If the target is a bank, a financial institution, or the filing context says `Reading profile: banking`, write the final decision through a bank-specific buy-side framework. Do not use orders, contract liabilities, gross margin, inventory, commodity cycles, or manufacturing-style cash conversion as core evidence.
- If the target is not a bank and the filing context does not say `Reading profile: banking`, do **not** use bank-specific KPI language such as NIM, deposit cost, credit cost, NPL, provision coverage, CET1, RWA, PB/ROE/COE bank framing, or payout-capital regulatory analysis unless those terms are directly relevant to the company's disclosed business. Route non-bank companies through their own industry-native drivers instead.
- Make the reader understand the bank's economic engine: earning assets, deposit franchise, NIM/net interest yield, fee income/AUM, credit cost, asset quality, capital/RWA, payout capacity, and regulatory constraints.
- Include a compact bank KPI decision table in prose or markdown: NIM/net interest yield and deposit cost; loan/deposit mix; fee income and wealth-management/AUM; NPL/special-mention/overdue or provision coverage; CET1/capital adequacy/RWA growth; dividend or payout safety. For each item, state latest evidence, direction, thesis implication, and next verification point.
- Build the bank earnings bridge through earning assets x NIM, fee income, credit cost/provisioning, operating efficiency, tax/minority items, capital consumption, and payout. If a driver is missing, say it is missing and do not substitute generic revenue, margin, OCF, orders, or contract-liability evidence.
- Build the bank valuation bridge through PB/ROE/COE, PE as a cross-check, dividend yield, and peer-relative quality. Explain what today's PB/PE implies about sustainable ROE or risk premium, then compare it with the bank's actual ROE, asset quality, deposit franchise, and capital position.
- Explain why this bank rather than another bank: compare quality paid for versus quality received, including PB/ROE, asset quality, deposit franchise, fee resilience, capital, payout, and whether the quality premium is justified.
- Scenario analysis for banks must attach probabilities to explicit banking variables: NIM bps, credit cost/provision coverage, fee-income growth, NPL movement, ROE, PB or dividend yield, and position action. Do not use generic bull/base/bear labels without these variables.
- Keep NIM terminology precise: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. Never invent a NIM number that is not supported by the supplied filing or KPI context.

**Context:**
- Research Manager's investment plan: **{research_plan}**
- Machine-readable Research Manager canonical model (authoritative numeric handoff): **{research_manager_payload_context or '{}'}**
- Trader's transaction proposal: **{trader_plan}**
- Thematic catalyst cross-check and valuation bridge: **{thematic_catalyst_context}**
- Industry cycle scan: **{industry_cycle_context}**
- Company business-model primer: **{company_business_model_context}**
- Structured research bundle (JSON source of record; prefer this over re-parsing Markdown): **{structured_research_context}**
- Post-analyst fundamentals reconciliation pack (use to verify accepted model updates): **{fundamentals_reconciliation_context}**
- Industry KPI checklist: **{industry_kpi_context}**
- Forward forecast-model scaffold: **{forecast_model_context}**
- Sell-side depth and key-number audit: **{quality_audit_context}**
- Thesis-question context: **{thesis_question_context}**
- Commodity/product-price context: **{commodity_context}**
- Price-move attribution context: **{price_move_attribution_context}**
- Historical minute K-line / intraday behavior context: **{intraday_behavior_context}**
- Relative-strength / index-linkage context: **{relative_strength_context}**
- Shipping/freight-rate context: **{shipping_context}**
- Financial-report intelligence: **{filing_intelligence_context}**
- Same-industry peer comparison: **{peer_comparison_context}**
- Cross-position supply-chain comparison: **{supply_chain_comparison_context}**
- Earnings-model context: **{earnings_model_context}**
- Company announcement/event context: **{company_events_context}**
- Market-expectation context: **{market_expectation_context}**
- Historical price-EPS-PE decomposition context: **{price_earnings_decomposition_context}**
- Management/capital-allocation context: **{management_capital_allocation_context}**
- Shareholder-structure context: **{shareholder_structure_context}**
- Official investor-interaction context: **{investor_interaction_context}**
- Official policy-planning context: **{policy_planning_context}**
- Web fact-check context: **{web_fact_check_context}**
- Knowledge Planet topic-text intelligence: **{knowledge_planet_context}**
- Active gated sector contexts:
{gated_sector_context}
- Data coverage audit: **{data_coverage_context}**
{lessons_line}
{recent_decision_line}
{bull_bear_context}
**Risk Analysts Debate History:**
{prompt_risk_history}

---

Be decisive and ground every conclusion in specific evidence from the analysts.
{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_buy_side_underwriting_modules_instruction()}
{get_company_depth_contract_instruction()}
{get_material_catalyst_instruction()}
{get_thematic_valuation_instruction()}
{get_filing_intelligence_instruction()}
{get_question_led_debate_instruction()}
{gated_sector_instructions}
{get_price_move_attribution_instruction()}
{get_peer_selection_instruction()}
{get_supply_chain_selection_instruction()}
{get_earnings_model_instruction()}
{get_market_expectation_instruction()}
{get_price_earnings_decomposition_instruction()}
{get_investor_interaction_instruction()}
{get_policy_planning_instruction()}
{get_three_layer_conclusion_instruction()}
{get_management_capital_allocation_instruction()}
{get_shareholder_structure_instruction()}
{get_web_fact_check_instruction()}
{get_knowledge_planet_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_focused_report_instruction()}
If an important investment claim depends on an unverified commodity price, product spread, inventory, policy detail, wholesale price, or exact percentage, list it under an "Unverified Key Assumptions" paragraph instead of treating it as fact. Do not place unverified exact prices in the holder/builder action plan as hard triggers; turn them into verification items.{get_language_instruction()}"""

        final_trade_decision, pm_generation_status = invoke_structured_or_freetext(
            structured_llm,
            llm,
            prompt,
            render_sell_side_pm_decision,
            "Portfolio Manager",
            return_metadata=True,
            fallback_schema=SellSidePMDecision,
        )
        pm_decision_payload = pm_generation_status.pop("validated_payload", {})
        pm_generation_status["schema"] = "SellSidePMDecision"
        manager_payload = state.get("research_manager_plan_payload", {}) or {}
        deterministic_model_notes: list[str] = []
        if pm_decision_payload:
            pm_decision_payload, restored_handoff_notes = (
                _merge_manager_canonical_snapshot(
                    manager_payload,
                    pm_decision_payload,
                )
            )
            deterministic_model_notes.extend(restored_handoff_notes)
            try:
                normalized_decision, normalization_notes = normalize_sell_side_pm_decision(
                    pm_decision_payload
                )
            except (TypeError, ValueError) as exc:
                # Compatibility/fallback providers can return an older partial
                # payload. Preserve their already-rendered report instead of
                # crashing; deterministic valuation remains visibly unclosed.
                deterministic_model_notes = [
                    "deterministic normalization skipped for incomplete PM payload: "
                    + str(exc).splitlines()[0]
                ]
            else:
                deterministic_model_notes.extend(normalization_notes)
                pm_decision_payload = normalized_decision.model_dump(mode="json")
                pm_decision_payload, lineage_notes = _normalize_sell_side_lineage(
                    pm_decision_payload,
                    state.get("structured_research_context", {}),
                )
                pm_decision_payload, methodology_notes = _enforce_forecast_methodology(
                    pm_decision_payload,
                    state.get("structured_research_context", {}),
                )
                deterministic_model_notes.extend(lineage_notes)
                deterministic_model_notes.extend(methodology_notes)
                normalized_decision = SellSidePMDecision.model_validate(
                    pm_decision_payload
                )
                final_trade_decision = render_sell_side_pm_decision(normalized_decision)

        initial_handoff_issues = _canonical_handoff_issues(
            manager_payload,
            pm_decision_payload,
        )
        initial_analytical_issues = _analytical_structure_issues(pm_decision_payload)
        editorial_review_payload: dict = {}
        editorial_review_status: dict = {
            "mode": "not_run",
            "agent": "Sell-Side Research Editor",
            "structured_error": "initial PM output was not schema-validated",
        }
        revision_requested = False
        revision_applied = False
        revision_rejection_reasons: list[str] = []
        revision_status: dict = {"mode": "not_run"}
        remaining_handoff_issues = list(initial_handoff_issues)
        remaining_analytical_issues = list(initial_analytical_issues)

        # The editor is advisory: a provider failure never fragments or blocks the
        # report. A valid review can request one bounded revision from the same
        # user-selected deep model.
        if pm_decision_payload:
            _review_text, editorial_review_status = invoke_structured_or_freetext(
                editorial_review_llm,
                llm,
                _editorial_review_prompt(
                    decision_payload=pm_decision_payload,
                    manager_payload=manager_payload,
                    structured_research_context=structured_research_context,
                    fundamentals_context=fundamentals_reconciliation_context,
                    handoff_issues=[*initial_handoff_issues, *initial_analytical_issues],
                ),
                lambda value: value.model_dump_json(),
                "Sell-Side Research Editor",
                return_metadata=True,
                fallback_schema=SellSideEditorialReview,
            )
            editorial_review_payload = editorial_review_status.pop(
                "validated_payload", {}
            )
            revision_requested = bool(initial_handoff_issues) or bool(initial_analytical_issues) or bool(
                editorial_review_payload.get("revision_required")
            )

        if revision_requested:
            revised_decision, revision_status = invoke_structured_or_freetext(
                structured_llm,
                llm,
                _editorial_revision_prompt(
                    decision_payload=pm_decision_payload,
                    review_payload=editorial_review_payload,
                    handoff_issues=[*initial_handoff_issues, *initial_analytical_issues],
                    manager_payload=manager_payload,
                    structured_research_context=structured_research_context,
                    fundamentals_context=fundamentals_reconciliation_context,
                    lessons_line=lessons_line,
                    recent_decision_line=recent_decision_line,
                ),
                render_sell_side_pm_decision,
                "Portfolio Manager Editorial Revision",
                return_metadata=True,
                fallback_schema=SellSidePMDecision,
            )
            revised_payload = revision_status.pop("validated_payload", {})
            if revised_payload:
                revised_payload, restored_revision_notes = (
                    _merge_manager_canonical_snapshot(
                        manager_payload,
                        revised_payload,
                    )
                )
                try:
                    normalized_revision, revision_model_notes = normalize_sell_side_pm_decision(
                        revised_payload
                    )
                    revision_model_notes = [
                        *restored_revision_notes,
                        *revision_model_notes,
                    ]
                except (TypeError, ValueError) as exc:
                    normalized_revision = None
                    revision_model_notes = []
                    revision_rejection_reasons.append(
                        "revision normalization failed: " + str(exc).splitlines()[0]
                    )
            if revised_payload and normalized_revision is not None:
                revised_payload = normalized_revision.model_dump(mode="json")
                revised_payload, revision_lineage_notes = _normalize_sell_side_lineage(
                    revised_payload,
                    state.get("structured_research_context", {}),
                )
                revised_payload, revision_methodology_notes = _enforce_forecast_methodology(
                    revised_payload,
                    state.get("structured_research_context", {}),
                )
                revision_model_notes.extend(revision_lineage_notes)
                revision_model_notes.extend(revision_methodology_notes)
                normalized_revision = SellSidePMDecision.model_validate(revised_payload)
                revised_handoff_issues = _canonical_handoff_issues(
                    manager_payload,
                    revised_payload,
                )
                revised_analytical_issues = _analytical_structure_issues(
                    revised_payload
                )
                rating_preserved = revised_payload.get("rating") == pm_decision_payload.get(
                    "rating"
                )
                handoff_not_worsened = len(revised_handoff_issues) <= len(
                    initial_handoff_issues
                )
                analytical_not_worsened = len(revised_analytical_issues) <= len(
                    initial_analytical_issues
                )
                if rating_preserved and handoff_not_worsened and analytical_not_worsened:
                    final_trade_decision = render_sell_side_pm_decision(normalized_revision)
                    pm_decision_payload = revised_payload
                    remaining_handoff_issues = revised_handoff_issues
                    remaining_analytical_issues = revised_analytical_issues
                    deterministic_model_notes = revision_model_notes
                    revision_applied = True
                else:
                    if not rating_preserved:
                        revision_rejection_reasons.append("revision changed the protected rating")
                    if not handoff_not_worsened:
                        revision_rejection_reasons.append(
                            "revision increased canonical handoff issues "
                            f"from {len(initial_handoff_issues)} to {len(revised_handoff_issues)}"
                        )
                    if not analytical_not_worsened:
                        revision_rejection_reasons.append(
                            "revision increased analytical structure issues "
                            f"from {len(initial_analytical_issues)} to {len(revised_analytical_issues)}"
                        )

        initial_mode = pm_generation_status.get("mode", "unknown")
        if revision_applied:
            pm_generation_status["mode"] = revision_status.get("mode", initial_mode)
        pm_generation_status.update(
            {
                "initial_mode": initial_mode,
                "editorial_review_mode": editorial_review_status.get("mode", "not_run"),
                "editorial_revision_requested": revision_requested,
                "editorial_revision_applied": revision_applied,
                "editorial_revision_mode": revision_status.get("mode", "not_run"),
                "remaining_handoff_issues": remaining_handoff_issues,
                "remaining_analytical_issues": remaining_analytical_issues,
                "editorial_revision_rejection_reasons": revision_rejection_reasons,
                "deterministic_model_notes": deterministic_model_notes,
            }
        )
        pm_editorial_review = {
            "review": editorial_review_payload,
            "review_status": editorial_review_status,
            "revision_requested": revision_requested,
            "revision_applied": revision_applied,
            "revision_status": revision_status,
            "initial_handoff_issues": initial_handoff_issues,
            "initial_analytical_issues": initial_analytical_issues,
            "remaining_handoff_issues": remaining_handoff_issues,
            "remaining_analytical_issues": remaining_analytical_issues,
            "revision_rejection_reasons": revision_rejection_reasons,
        }
        full_pm_decision = final_trade_decision
        final_trade_decision, internal_overflow, removed_sections = (
            split_pm_public_report(full_pm_decision)
        )
        pm_generation_status.update(
            {
                "full_report_chars": str(len(full_pm_decision)),
                "public_report_chars": str(len(final_trade_decision)),
                "internal_overflow_chars": str(len(internal_overflow)),
                "internal_sections_removed_from_public_report": ", ".join(removed_sections),
                "public_h2_count": str(
                    sum(
                        1
                        for line in final_trade_decision.splitlines()
                        if line.startswith("## ")
                    )
                ),
            }
        )

        new_risk_debate_state = {
            "judge_decision": final_trade_decision,
            "history": risk_debate_state["history"],
            "aggressive_history": risk_debate_state["aggressive_history"],
            "conservative_history": risk_debate_state["conservative_history"],
            "neutral_history": risk_debate_state["neutral_history"],
            "latest_speaker": "Judge",
            "current_aggressive_response": risk_debate_state["current_aggressive_response"],
            "current_conservative_response": risk_debate_state["current_conservative_response"],
            "current_neutral_response": risk_debate_state["current_neutral_response"],
            "count": risk_debate_state["count"],
        }

        return {
            "risk_debate_state": new_risk_debate_state,
            "final_trade_decision": final_trade_decision,
            "pm_internal_overflow": internal_overflow,
            "pm_full_decision": full_pm_decision,
            "pm_generation_status": pm_generation_status,
            "pm_decision_payload": pm_decision_payload,
            "pm_editorial_review": pm_editorial_review,
        }

    return portfolio_manager_node
