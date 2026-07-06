"""Research Manager: turns the bull/bear debate into a structured investment plan for the trader."""

from __future__ import annotations

import json
import re
from copy import deepcopy
from typing import Any, Mapping

from tradingagents.agents.schemas import (
    UnderwritingResearchPlan,
    render_underwriting_research_plan,
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
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_optical_module_instruction,
    get_price_move_attribution_instruction,
    get_investor_interaction_instruction,
    get_knowledge_planet_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_material_catalyst_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_instruction,
    get_question_led_debate_instruction,
    get_research_gap_instruction,
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
    compact_state_fields,
    gated_prompt_sections,
)
from tradingagents.dataflows.structured_research import compact_structured_research_for_prompt


def _handoff_metric_key(period: Any, metric: Any) -> tuple[str, str]:
    period_key = re.sub(r"\s+", "", str(period or "")).lower()
    metric_key = re.sub(
        r"[^a-z0-9\u4e00-\u9fff]+", "", str(metric or "").lower()
    )
    aliases = {
        "dilutedsharecount": "dilutedshares",
        "dilutedshares": "dilutedshares",
        "dilutedsharesoutstanding": "dilutedshares",
        "sharecount": "dilutedshares",
        "revenue": "revenue",
        "consolidatedrevenue": "revenue",
        "grossprofit": "grossprofit",
        "consolidatedgrossprofit": "grossprofit",
        "grossmargin": "grossmargin",
        "consolidatedgrossmargin": "grossmargin",
        "operatingprofit": "operatingprofit",
        "consolidatedoperatingprofit": "operatingprofit",
        "netprofitparent": "parentnetprofit",
        "parentnetprofit": "parentnetprofit",
        "consolidatedparentnetprofit": "parentnetprofit",
        "epsbasiccny": "eps",
        "epsbasic": "eps",
        "dilutedeps": "eps",
        "eps": "eps",
        "operatingcashflow": "ocf",
        "ocf": "ocf",
        "capitalexpenditure": "capex",
        "capex": "capex",
        "freecashflow": "fcf",
        "fcf": "fcf",
        "稀释股本": "dilutedshares",
        "总股本": "dilutedshares",
        "营业收入": "revenue",
        "营收": "revenue",
        "毛利润": "grossprofit",
        "毛利率": "grossmargin",
        "营业利润": "operatingprofit",
        "归母净利润": "parentnetprofit",
        "每股收益": "eps",
        "经营活动现金流净额": "ocf",
        "资本开支": "capex",
        "自由现金流": "fcf",
    }
    canonical = aliases.get(metric_key, metric_key)
    if canonical == "dilutedshares":
        period_key = "current"
    return period_key, canonical


def _normalized_unit(value: Any) -> str:
    return re.sub(r"[^a-z0-9%/\u4e00-\u9fff]+", "", str(value or "").lower())


def _line_changed(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    try:
        left_value = float(left.get("value"))
        right_value = float(right.get("value"))
        value_changed = abs(left_value - right_value) > max(
            abs(left_value) * 0.02, 0.01
        )
    except (TypeError, ValueError):
        value_changed = left.get("value") != right.get("value")
    return value_changed or (
        _normalized_unit(left.get("unit"))
        and _normalized_unit(right.get("unit"))
        and _normalized_unit(left.get("unit"))
        != _normalized_unit(right.get("unit"))
    )


def _underwriting_line_map(packet: Mapping[str, Any]) -> dict[tuple[str, str], dict]:
    lines: dict[tuple[str, str], dict] = {}
    company = dict(packet.get("company_model", {}))
    shares = company.get("diluted_share_count_mn")
    if shares is not None:
        lines[("current", "dilutedshares")] = {
            "line_id": "shares",
            "period": company.get("share_count_period", "current"),
            "metric": "diluted_shares",
            "value": shares,
            "unit": "mn shares",
            "status": (
                "reported"
                if company.get("share_count_source_type") == "reported"
                else "calculated"
            ),
            "evidence_ids": [company.get("share_count_evidence_id")]
            if company.get("share_count_evidence_id")
            else [],
            "formula": company.get("share_count_formula", ""),
        }
    years = list(packet.get("forecast_years", []))
    for row in packet.get("forecast_lines", []) or []:
        if str(row.get("segment", "")).strip().lower() not in {
            "consolidated", "group", "合并", "公司整体"
        }:
            continue
        for index, value_field in enumerate(
            ("year_1_value", "year_2_value", "year_3_value")
        ):
            if index >= len(years) or row.get(value_field) is None:
                continue
            key = _handoff_metric_key(years[index], row.get("metric"))
            lines[key] = {
                "line_id": f"{years[index]}_{key[1]}",
                "period": years[index],
                "metric": key[1],
                "value": row.get(value_field),
                "unit": row.get("unit", ""),
                "status": (
                    "reported"
                    if row.get("assumption_status") == "reported"
                    else "calculated"
                    if row.get("assumption_status") == "calculated"
                    else "estimated"
                ),
                "evidence_ids": list(row.get("evidence_ids", []) or []),
                "formula": row.get("formula", ""),
            }
    return lines


def _complete_unchanged_handoff_lines(
    packet: Mapping[str, Any], payload: Mapping[str, Any]
) -> tuple[dict[str, Any], list[str]]:
    """Copy omitted unchanged underwriting lines without another LLM call.

    The Research Manager is allowed to revise a line only through an accepted
    ``model_change_rows`` entry.  Therefore a source line that is absent from
    the snapshot and has no accepted change is bookkeeping, not analysis.  It
    can be restored deterministically while substantive changes remain routed
    to the existing repair/audit path.
    """

    completed = deepcopy(dict(payload))
    snapshot = [dict(row) for row in completed.get("canonical_model_snapshot", []) or []]
    accepted_keys = {
        _handoff_metric_key(row.get("period"), row.get("metric"))
        for row in snapshot
        if row.get("value") is not None
    }
    changed_ids = {
        str(row.get("line_id", "")).strip().lower()
        for row in completed.get("model_change_rows", []) or []
        if str(row.get("disposition", "")).lower() == "accepted"
    }
    copied_ids: list[str] = []
    for key, source in _underwriting_line_map(packet).items():
        line_id = str(source.get("line_id", "")).strip()
        if key in accepted_keys or line_id.lower() in changed_ids:
            continue
        snapshot.append(dict(source))
        accepted_keys.add(key)
        copied_ids.append(line_id)
    completed["canonical_model_snapshot"] = snapshot
    return completed, copied_ids


def _research_manager_handoff_issues(
    packet: Mapping[str, Any], payload: Mapping[str, Any]
) -> list[str]:
    """Return machine-actionable underwriting -> Research Manager gaps."""

    initial = _underwriting_line_map(packet)
    accepted = {
        _handoff_metric_key(row.get("period"), row.get("metric")): dict(row)
        for row in payload.get("canonical_model_snapshot", []) or []
        if row.get("value") is not None
    }
    change_ids = {
        str(row.get("line_id", "")).strip().lower()
        for row in payload.get("model_change_rows", []) or []
        if str(row.get("line_id", "")).strip()
        and str(row.get("disposition", "")).lower() == "accepted"
    }
    issues: list[str] = []
    for key, original in initial.items():
        final = accepted.get(key)
        if final is None:
            issues.append(
                f"missing canonical line {original['line_id']}: "
                f"{original['value']} {original['unit']}"
            )
            continue
        if _line_changed(original, final) and str(
            final.get("line_id", "")
        ).lower() not in change_ids:
            issues.append(
                f"undocumented change {final.get('line_id')}: "
                f"{original['value']} {original['unit']} -> "
                f"{final.get('value')} {final.get('unit')}"
            )
    return issues


def _handoff_repair_prompt(
    *, packet: Mapping[str, Any], payload: Mapping[str, Any], issues: list[str]
) -> str:
    source_lines = list(_underwriting_line_map(packet).values())
    return f"""CANONICAL UNDERWRITING HANDOFF REPAIR
Your first Research Manager object is analytically usable but its machine-readable
handoff is incomplete. Return one complete UnderwritingResearchPlan object.

Do not change the recommendation merely to repair bookkeeping. Preserve the substantive
debate ruling. For every populated consolidated underwriting line, do exactly one of:
1. copy its value and unit into canonical_model_snapshot; or
2. use the debated replacement value and add an accepted model_change_rows entry with the
   same line_id, old value, new value, evidence ids, reason, and EPS/FCF/valuation impact.
Never drop a populated line. Spaces versus underscores are the same unit and do not require
a change row. Keep missing source cells missing rather than inventing precision.

Detected issues:
{json.dumps(issues, ensure_ascii=False)}

Canonical populated lines from the original underwriting packet:
{json.dumps(source_lines, ensure_ascii=False, separators=(',', ':'))}

First Research Manager JSON:
{json.dumps(payload, ensure_ascii=False, separators=(',', ':'))}
"""


def create_research_manager(llm):
    structured_llm = bind_structured(
        llm,
        UnderwritingResearchPlan,
        "Research Manager",
    )

    def research_manager_node(state) -> dict:
        instrument_context = build_instrument_context(state["company_of_interest"])
        history = state["investment_debate_state"].get("history", "")
        recent_decision_context = compact_for_prompt(
            state.get("recent_decision_context", ""),
            label="recent_decision_context",
            profile="research",
        )
        prompt_contexts = compact_state_fields(state, profile="research")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        price_move_attribution_context = prompt_contexts["price_move_attribution_context"]
        relative_strength_context = prompt_contexts["relative_strength_context"]
        shipping_context = prompt_contexts["shipping_context"]
        filing_intelligence_context = prompt_contexts["filing_intelligence_context"]
        peer_comparison_context = prompt_contexts["peer_comparison_context"]
        supply_chain_comparison_context = prompt_contexts["supply_chain_comparison_context"]
        earnings_model_context = prompt_contexts["earnings_model_context"]
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
        gated_sector_context, gated_sector_instructions = gated_prompt_sections(
            [
                ("Baijiu", baijiu_context, get_baijiu_instruction),
                ("Compute leasing", compute_leasing_context, get_compute_leasing_instruction),
                ("Defensive dividend", dividend_defensive_context, get_dividend_defensive_instruction),
                ("Building materials", building_materials_context, get_building_materials_instruction),
                (
                    "Consumer staples",
                    consumer_staples_context,
                    lambda: get_consumer_staples_instruction(),
                ),
                ("Optical module", optical_module_context, get_optical_module_instruction),
                ("Biopharma", biopharma_context, get_biopharma_instruction),
                ("Software", software_context, get_software_instruction),
                ("Insurance", insurance_context, get_insurance_instruction),
                ("Medical device", medical_device_context, get_medical_device_instruction),
                ("Metals/mining", metals_mining_context, get_metals_mining_instruction),
            ]
        )
        industry_cycle_context = prompt_contexts["industry_cycle_context"]
        company_business_model_context = prompt_contexts["company_business_model_context"]
        industry_kpi_context = prompt_contexts["industry_kpi_context"]
        forecast_model_context = prompt_contexts["forecast_model_context"]
        quality_audit_context = prompt_contexts["quality_audit_context"]
        thesis_question_context = prompt_contexts["thesis_question_context"]
        data_coverage_context = prompt_contexts["data_coverage_context"]
        structured_research_context = compact_structured_research_for_prompt(
            state.get("structured_research_context", {}),
        )
        # The shared packet is built before analysts finish. Feed later analyst
        # work directly to the model referee so reproducible corrections are
        # not lost inside debate summaries.
        fundamentals_reconciliation_context = compact_for_prompt(
            state.get("fundamentals_report", ""),
            label="analyst_report",
            profile="research",
            max_chars=12000,
        )
        market_reconciliation_context = compact_for_prompt(
            state.get("market_report", ""),
            label="analyst_report",
            profile="research",
            max_chars=5000,
        )
        prompt_history = compact_debate_history(history, profile="research")
        continuity_context = (
            f"""
**Most Recent Same-Ticker Decision (may still be pending outcome):**
{recent_decision_context}
"""
            if recent_decision_context
            else ""
        )

        investment_debate_state = state["investment_debate_state"]

        prompt = f"""As the Research Manager and debate facilitator, your role is to critically evaluate this round of debate and deliver a clear, actionable investment plan for the trader.

{instrument_context}

---

**Rating Scale** (use exactly one):
- **Buy**: Strong conviction in the bull thesis; recommend taking or growing the position
- **Overweight**: Constructive view; recommend gradually increasing exposure
- **Hold**: Balanced view; recommend maintaining the current position
- **Underweight**: Cautious view; recommend trimming exposure
- **Sell**: Strong conviction in the bear thesis; recommend exiting or avoiding the position

Commit to a clear stance whenever the core bet has attractive probability/payoff. Reserve Hold for cases where there is no clear tradable thesis, the expectation gap is weak, or the risk/reward is not attractive. Do not use Hold merely because the evidence set is imperfect, but also do not treat Hold as a low-information or useless conclusion: a high-quality Hold must be a thesis-rich transition rating with valuation bands, verification gates, upgrade/downgrade triggers, and position-size guidance.

**Hold Posture Discipline:**
- Do not let every unfinished but interesting idea collapse into plain neutral Hold. If the recommendation is Hold, explicitly classify the posture as one of: `Hold / Positive Watch`, `Hold / Defensive Starter`, `Hold / Neutral Wait`, or `Hold / Negative Watch`.
- `Hold / Positive Watch` means the thesis has improving evidence or an expectation gap, but the price, catalyst, or decisive disclosure is not good enough for Overweight yet.
- `Hold / Defensive Starter` means downside appears bounded enough for a small trial position, but full sizing still needs verification.
- `Hold / Neutral Wait` means evidence and odds are genuinely balanced.
- `Hold / Negative Watch` means existing holders may wait for exit/repair evidence, but new money should avoid unless the setup changes.
- When the upside evidence, valuation gap, catalyst path, and downside containment already create positive expected value, use Overweight with staged sizing rather than hiding the view inside Hold merely because one data point is still pending.

**Buy-Side Thesis Framework:**
- First answer: if we are bullish, what exactly are we betting on?
- Judge whether that boom-bust or business-cycle expectation can plausibly realize using verified evidence, proxy evidence, and bounded inference.
- Separate facts, proxy evidence, inference, and unverified assumptions.
- A thesis can be investable before every data point is proven if the probability/payoff is attractive and the falsification path is clear.
- Do not infer a positive rating from the failure of the negative case, or a negative rating from the failure of the positive case. `Not Underweight` is not `Overweight`; `not Overweight` is not `Underweight`.
- Rate from the company's full fundamental chain first: business quality, segment economics, key operating drivers, cash-flow and balance-sheet quality, management/capital allocation, valuation-implied expectations, catalysts, downside case, peer opportunity cost, and falsification path.
- Use Overweight only when verified or high-quality proxy evidence supports positive expected value after the main company-specific risks are explicitly underwritten; the report must show why current price underestimates normalized earnings/ROE/cash flow or asset value and why the catalyst path can unlock that gap.
- Use Underweight only when verified company-specific deterioration, overvaluation, poor payoff, or a truly verified superior substitute makes the expected value unattractive; a partial peer screen or one unresolved risk is not enough.
- Use Hold when the company has an investable possibility but the decisive variable remains unresolved. This is not a weak conclusion: it should say what position is justified now, what evidence would upgrade to Overweight/Buy, what evidence would downgrade to Underweight/Sell, and what price would change the odds.
- For every direction, specify expectation gap, probability/payoff, catalyst path, falsification signals, and conviction level.

**Fair Cycle-Valuation Calibration:**
- Judge every stock through the same valuation x prosperity lens.
- Low valuation/low prosperity is not automatically bearish; ask whether pessimism is priced and whether an inflection is plausible.
- High prosperity/high valuation is not automatically bullish; ask whether growth durability and earnings upgrades can digest valuation.
- Low valuation/high prosperity can be attractive, but test whether earnings are sustainable or temporarily inflated.
- High valuation/low prosperity normally requires a clear future inflection, scarce growth, or other special evidence to avoid Underweight.
- The rating should reflect expected value, not style preference.

**Market-Regime Calibration:**
- Start from company evidence, then adjust for market/sector mood.
- In a normal bull market, a high-quality stock with reasonable valuation can receive a slightly more constructive rating, but an expensive/crowded stock should not be upgraded mechanically.
- In a normal bear market, keep ratings more conservative unless valuation, balance sheet, and catalysts are strong.
- In extreme pessimism with depressed valuations, allow contrarian watch or staged-entry logic for resilient companies, but avoid upgrading fragile balance sheets simply because prices are low.
- In extreme optimism with high valuations, require stronger evidence for Buy/Overweight and emphasize trimming discipline.
- For cyclical, commodity, shipping, high-beta, or event-driven stocks, calibrate the rating using the stock's own cycle drivers, not only broad-market mood.

**Evidence-Gap Calibration:**
- Missing core operating data is neutral evidence for direction, but not neutral for conviction. It is a research gap that should reduce confidence in the affected thesis.
- Missing data is also not adverse evidence by itself. Do not convert an unavailable data point into Underweight/Sell unless verified negative evidence independently supports the downside case.
- Do not let PE/PB and technical indicators replace missing product-price, spread, inventory, freight-rate, policy, capacity, or order-book evidence.
- Missing-data neutrality overrides narrower sector rules: unavailable data is neutral non-evidence and must not mechanically downgrade or upgrade the recommendation, conviction tier, sizing, valuation multiple, or publication status.
- If unavailable data is central to either thesis, keep the recommendation based only on verified evidence, leave unsupported model cells null, and state the retrieval task and conditional scenario. Do not default to Hold merely because the field is missing.
- For aluminum names, missing alumina, power, or anode cost evidence cannot by itself support Underweight/Sell, margin-collapse claims, or "perfect scenario priced" language. Require independent verified cost squeeze, segment-margin compression, cash-flow deterioration, inventory loss, peer opportunity cost, or valuation stress.
- For hog breeders such as Muyuan, Wens Foodstuff, and New Hope, force a livestock-cycle valuation frame: hog ASP x complete-cost spread, sales kilograms, breeding-sow supply, OCF/leverage survival, PB/NAV floor, normalized cycle earnings, and current-market-cap implied hog price. PE TTM is context only, not the target-price anchor.
- For hog breeders, reject any scenario table whose selected fair-value range is economically lower in a mild recovery than in a bottom/stress case unless the memo explicitly proves why PB/NAV support disappears. Show earnings value and PB/NAV floor side by side before choosing the final range.
- Hold should mean balanced verified evidence, not "we could not fetch the important data."

**Supply-Demand Fallback:**
- If micro product price, spread, inventory, or freight data is missing, ask whether macro supply-demand evidence can still say something useful.
- This fallback must be specific to the product or route: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Treat macro proxies as lower-confidence evidence than verified micro prices. They can shape scenarios and watch ranges, but should not be presented as exact product-price conclusions.
- If macro supply-demand evidence points clearly one way, do not default to Hold purely because product quotes are missing; instead state an evidence-limited directional view and what data would confirm or refute it.
- Do not let a bull or bear case use unverified exact wholesale prices, product prices, spreads, inventories, or date-specific market statistics as decisive facts. Keep them in an evidence-gap/watchlist bucket unless the source context labels them verified.

**Decision-Continuity Rules:**
- Reassess the company fully, but do not silently reverse a recent same-ticker stance.
- If the recommendation differs from the most recent same-ticker decision, explicitly identify the new decisive evidence, the core facts that remain unchanged, and why the prior stance is no longer preferred.
- A lower share price by itself is not a new fundamental fact. It may change valuation or trading posture, but it cannot alone justify a reversal across the neutral line.
- If there is no new decisive evidence, prefer preserving the prior directional stance while adjusting conviction, sizing, or watch levels.
- If a recent same-ticker decision is present and you are writing free text rather than structured fields, include explicit sections titled **Prior Rating**, **New Evidence Since Prior**, **Unchanged Core Facts**, and **Rating Change Audit**.
- If any verified theme matters to the thesis and you are writing free text rather than structured fields, include an explicit section titled **Thematic Valuation Bridge** that explains whether the theme belongs in core valuation, scenario valuation, SOTP/NAV, or only qualitative optionality.
- If you are writing free text rather than structured fields, include explicit sections titled **Company Quality Verdict**, **Current Odds Verdict**, and **Relative Allocation Verdict** so that business quality, today's risk/reward, and best deployment choice are not collapsed into one view.
- If you are writing free text rather than structured fields, also include **Management & Capital Allocation Verdict** and **Shareholder Structure Verdict** whenever the hard-signal contexts are available.
- If official investor-interaction context is available, keep an **Investor Communication Verdict** explicit enough for the downstream trader and risk team to understand the live concern map and disclosure quality.
- Keep an **Industry Cycle Verdict** explicit enough to state the current cycle stage before valuation: downturn, bottom-testing, bottom-right validation, early upcycle, mid-cycle expansion, peak/rollover, or evidence insufficient. Do not let company PE or one-quarter profit alone establish the cycle stage.
- Keep a **Business Model / Segment Economics Verdict** explicit enough to teach how the company makes money, which segments are mature core value, which are second-curve/scenario value, what moat is actually evidenced, and which segment disclosures are still missing.
- Keep an **Industry KPI Verdict** explicit enough to say which sector-native KPI layers are verified, partial, or missing. Verified KPI evidence may change the model; unavailable KPI fields remain neutral and go to the retrieval/verification calendar.
- Keep a **Forward Forecast Model Verdict** with three explicit forward years (or four forward quarters), segment drivers and the shared packet's model-profile-appropriate earnings, cash/capital, asset-quality and per-share lines. Ordinary companies use revenue/margin/parent profit/EPS/OCF/capex/FCF; banks, insurers, securities firms and REITs use their native driver sets. Missing inputs must appear as `missing/not disclosed` with a research task; a one-year range is incomplete and cannot support a target or safety price.
- Keep a **Key Number Audit Verdict** explicit enough to police decisive PE/PB/EV multiples, target price, safety price, dividend yield, margins, ASP, shipments, utilization, backlog, and contract-liability claims. Require formula, period, source, and evidence status when those numbers drive the rating.
- Keep a **Question-Led Thesis Verdict** explicit enough to say which Thesis Question Context IDs were answered by the bull, which were successfully attacked by the bear, which remain unanswered, and how that changes rating, valuation, sizing, and next verification.
- If official policy context is available, keep a **Policy Direction Verdict** explicit enough to distinguish industry support from company-specific monetization.
- If historical price/EPS/PE decomposition context is available, keep the valuation-cycle verdict explicit enough to say whether the current price is supported by earnings improvement, multiple expansion, both, or neither.
- Preserve a concise standalone **Safety Price / Defensive Build Anchor** when financial state supports it; when writing Chinese, title it `## 安全价格区间 / 防御性建仓锚`. For value stocks, blue chips, banks, defensive dividend names, and mature cash-flow compounders, anchor it in normalized low-cycle EPS or FCF, sustainable dividend yield, book value/PB and ROE, cash conversion, leverage or net cash, asset quality, payout capacity, and peer/historical valuation floors. For commodity/resource/cyclical names, anchor it in cycle-trough or stress-case earnings, conservative product prices, unit-cost resilience, balance-sheet survival, maintenance capex, and normalized PE/PB floors. Include only the practical anchor: price band, valuation bridge, business conditions that must remain true, slow-build plan, and deterioration that invalidates it. Prefer one short paragraph or a compact 3-4 row table, not a second valuation essay. If the company is structurally impaired, highly leveraged, deeply cyclical without survivable trough economics, or evidence-thin, still keep the section and say no reliable safety price can be assigned.
- If industry-specific filing context is available, keep an **Industry Driver Verdict** explicit enough to preserve the real sector-native variables that decide the thesis.
- If the filing context contains **Growth Sustainability & Ramp Conditions**, keep a **Growth Sustainability Verdict** explicit enough to judge whether revenue/profit growth can continue or ramp further. Require the debate to separate verified drivers, inferred drivers, needed ramp conditions, and falsification signals before accepting any Buy/Underweight conclusion.
- Fill the compact `UnderwritingResearchPlan` schema. Put the reconciled operating/forecast/scenario model in `accepted_underwriting_model`, all assumption changes in `model_change_ledger`, unresolved company-specific questions in `unresolved_questions_and_gaps`, and a concise constraint set in `handoff_to_pm_and_trader`. Do not recreate the legacy optional-field checklist.
- Populate `research_questions` with only the 3-5 company-specific questions that can change earnings, cash/capital, valuation or rating. Use them as the organizing agenda rather than adding more generic modules.
- Populate `question_verdicts` for those same questions. Do not summarize modules one by one. For each question select the strongest dated evidence already supplied, reconcile the strongest conflicting observation, state the exact forecast/probability/valuation effect or an explicit unchanged result, and name the next verification. Evidence that does not affect a question, model line, probability or verification task stays out of the decision spine.
- Populate `forecast_takeaways` with 2-3 conclusions that interpret the forecast. Each needs a dated evidence anchor, financial implication, confidence and invalidation risk; never restate a row without explaining why it matters.
- Populate `forecast_assumptions` with the few parameters responsible for most model variance. Every parameter needs a historical anchor, evidence status, bear/base/bull values, sensitivity and verification gate. A bull/bear midpoint is not an independent estimate. If shipment, ASP, utilization or another industry-native driver is missing, label the affected assumption top-down/low-confidence and use a range; do not reverse-engineer a precise value and present it as bottom-up evidence.
- Populate `core_theses` with 2-4 ranked investment conclusions. Each must close takeaway -> evidence -> strongest counterevidence -> revenue/profit/EPS/FCF-or-capital/value transmission -> current market pricing -> falsification. Integrate moat evidence into the relevant thesis instead of creating an unprioritized moat list.
- Fill `canonical_model_snapshot` with the deterministic diluted-share line and every populated consolidated forecast/scenario line from the underwriting packet. Use stable line ids such as `shares`, `2026E_revenue`, `2026E_parent_net_profit`, `2026E_eps`, `base_fair_value`. Copy unchanged values and units exactly. Every changed value or unit must have a matching accepted `model_change_rows` entry with old/new values, evidence ids and recalculated impact; otherwise keep the packet value or mark the line unresolved.
- For a standard operating company, the accepted three-year snapshot must carry enough lines to cross-foot the income statement and cash flow: revenue, gross margin, gross profit, operating profit, finance/other items (signed), income tax, minority interest, parent net profit, diluted shares, EPS, OCF, capex and FCF. Select driver assumptions; application code recalculates gross profit, parent profit, EPS and FCF. If a bridge input is unavailable, leave it null and mark the model partial instead of inserting a plug.
- If the filing context or shared packet contains **Pre-Debate Underwriting Questions**, use them as the judging agenda. Reconcile initial assumption, bull evidence, bear attack, accepted model value, EPS/FCF/valuation impact and next verification inside `model_change_ledger`. Do not let the final plan ignore an unanswered question that is central to the recommendation.
- If the filing context contains a Business Segment Valuation Map or Segment Economics Pack, keep a **Business Segment Valuation Verdict** explicit enough to split mature core businesses from emerging second curves, geographies, and channels. Do not allow the debate to collapse a multi-business company into one blended PE unless the filings do not support a meaningful split.
- Keep a **Segment Prosperity Verdict** for multi-business companies. Judge each material segment on both current prosperity level and marginal direction using dated demand, supply/capacity, price/volume/share, utilization/mix, margin, working-capital and cash evidence. Require written causal analysis, strongest counterevidence, confidence, EPS/FCF transmission, and profit-weighted company aggregation; do not let one commodity proxy or a small fashionable segment determine the whole-company verdict.
- Enforce same-period segment ranking: compare every disclosed material segment's revenue growth and margin change before accepting `fastest-growing`, `highest-margin`, or `dominant profit pool`. A consolidated prosperity label is invalid until the segment matrix is complete or its missing links are explicitly disclosed.
- If the filing context contains Internal Filing Quality Modules, keep a **Filing Internal Quality Verdict** explicit enough to summarize accounting reconciliation, segment economics, footnotes, cash-flow quality, capex/CIP returns, MD&A text changes, non-recurring profit quality, balance-sheet leading signals, shareholder-return authenticity, and disclosure quality. Synthesize the material points; do not mechanically repeat all ten if some are immaterial.
- If commodity/product-price context is available, keep a **Commodity Cycle Verdict** explicit enough to say whether the product-price evidence supports or contradicts the margin/EPS/inventory part of the thesis.
- If price-move attribution context is available, keep a **Sharp Move Attribution Verdict** explicit enough to say whether a recent move is market-led, same-metal sector-led, cross-metal residual, mapped-commodity-led, stock-specific, failed-rebound/trend continuation, or possible emotion kill. Do not call a drop mispriced until valuation/NAV support and event checks pass.
- If relative-strength/index-linkage context is available, keep a **Relative Strength Verdict** explicit enough to decide whether the stock is stronger or weaker than its style index and same-industry basket, whether correlation/Beta suggest benchmark beta or company alpha, and how that changes timing, sizing, and thesis validation.
- If Knowledge Planet context is available, keep a **Knowledge Planet Intelligence Verdict** explicit enough to use the Single-Stock Knowledge Fusion Pack first, separate information-rich industry data/channel checks/research feedback from sell-side promotion, and reconcile private/proxy clues with filings, Tushare data, peer evidence, price/volume behavior, and official announcements. Decide whether it upgrades the catalyst/expectation gap, only creates a watch item, or raises pump/crowding risk.
- In text-only Knowledge Planet mode, a PDF/audio filename or report-list post proves only that a document exists. It cannot support an institution view, operating assumption, forecast, probability change or valuation input. Use only substantive topic text that survives the company-identity and deduplication gates.
- Use the Structured Research Bundle as the machine-readable source of record for segment identities, grounded metrics, source conflicts, and KPE financial transmission. Do not promote semantic rows marked unverified or missing-period into decisive evidence. When KPE quantification lacks a revenue base, margin, share count, cash conversion, or valid probability triplet, make the missing input an explicit research task instead of filling it narratively.
- Treat `underwriting_packet` inside that bundle as the single shared company model. Act as a model referee: reconcile the fundamental analyst's Shared Model Update Ledger with the Bull and Bear Model Change Ledgers question by question and forecast line by forecast line. Produce one **Accepted Underwriting Model** covering the company operating equations, all material segments, three forward years, the appropriate consolidated earnings/cash/capital/per-share model, and bull/base/bear probability/value. For each disputed line record old assumption, bull proposal, bear proposal, accepted assumption, evidence ids, financial impact, and next verification. Do not resolve disagreement by prose compromise or by choosing a rating first.
- Apply source precedence when reconciling: deterministic filing/Tushare facts first; reproducible calculations from those facts second; clearly labeled analyst estimates third; channel/proxy evidence fourth. A pre-debate packet cell marked missing must be replaced when a later analyst supplies a reproducible formula and source. Never repeat `missing` after accepting a valid update, and never let an unsupported analyst narrative overwrite a filing fact.
- The research plan handed to Trader and PM must state the packet's `research_readiness`, the accepted model changes, unresolved model cells and reconciliation failures. A missing model cell is neutral non-evidence: keep it explicit and unresolved, never convert it into either a convenient middle rating or a directional signal.
- Read and disclose the bundle's `preprocessing_mode` and `preprocessing_notes`. If semantic preprocessing failed, use deterministic filing-row segments only as a controlled fallback and cap confidence in semantic conflict/KPE mapping. For each company-specific KPE item, preserve one explicit downstream outcome: numeric old->new, probability before->after, unchanged/watch with verification gate, or rejected with reason.
- Do not call a forecast bottom-up unless numeric three-year rows exist for every material business unit and reconcile to consolidated revenue, profit and cash. When shipments, ASP or segment margin are missing, label the model hybrid/top-down and leave the unsupported segment cell unresolved.
- Reject period or per-share bridges that do not reconcile. H1 equals Q1 plus Q2 single-quarter profit and cannot reuse Q2 labels; BVPS=current price/PB, EPS=parent profit/diluted shares, and safety/target price must equal the stated EPSxPE or BVPSxPB formula with consistent units. If a required denominator is missing, require `no reliable safety price can be assigned` rather than an approximate range.
- Do not dismiss Knowledge Planet merely because it is unofficial. If a clue is company-specific, industry-KPI-like, channel-check-like, or broker research feedback, translate it into a thesis variable: driver, expected earnings/cash-flow effect, probability shift, catalyst clock, objective anchor, and falsification signal. If the clue is ignored, state the precise reason: stale, promotional, not company-specific, contradicted by objective data, already priced, or lacking a product-to-profit bridge.
- Treat relative strength and technical weakness as market-confirmation/timing evidence, not as a standalone proof that the thesis is false. It can reduce sizing or require staged execution; it should not override verified fundamentals without a linked fundamental explanation.
- If shipping/freight-rate context is available, keep a **Shipping Cycle Verdict** explicit enough to separate broad proxies (BDTI/BCTI/BDI/BCI/BPI) from route-level economics (VLCC TD3C/TCE/CTFI), and explicitly test two-sided Hormuz mechanisms: reopening can reduce risk premium and improve vessel turnover, while restocking, queue normalization, and renewed cargo flows can support near-term cargo demand. Missing route-level freight is a conviction cap, not automatically bearish evidence.
- If gated baijiu context says `Status: triggered`, keep a **Baijiu Channel Verification Verdict** explicit enough to separate product wholesale price evidence, channel inventory/payment quality, contract-liability seasonality, product mix, peer-basket comparison, and missing data. If it says `Status: not_applicable`, do not force baijiu analysis into the stock.
- If gated compute-leasing context says `Status: triggered`, keep a **Compute-Leasing Verification Verdict** explicit enough to separate legacy value, verified compute-leasing value, unverified compute optionality, unit-economics gaps, capex/funding risk, and transition credibility. If it says `Status: not_applicable`, do not force compute-leasing analysis into the stock.
- If gated dividend-defensive context says `Status: triggered`, keep a **Dividend Defensive Verdict** explicit enough to say whether this is a true defensive dividend candidate, a dividend-trap risk, or inferior to peer alternatives. If it says `Status: not_applicable`, do not force a high-dividend thesis into the stock.
- If gated building-materials context says `Status: triggered`, use it as a discipline layer: anchor first on company filings and management wording, then classify the industry stage and likely evolution path, and then cover product price/ASP, regional demand, property-completion/infrastructure/renovation exposure, capacity/utilization, upstream costs, inventory, receivables, cash collection, payout safety, and whether low PB/high dividend is real safety or a value trap. Add a dedicated **Building Materials Operating Cycle Verdict** only when it changes the rating, valuation, sizing, or action plan; otherwise integrate the relevant points into the main business/valuation/risk discussion. Treat repurchases and dividends as shareholder-return, safety-margin, and controlling-shareholder-attitude evidence, not as the whole thesis. If it says `Status: not_applicable`, do not force building-materials logic into the stock.
- If gated consumer-staples context says `Status: triggered`, keep a **Consumer Staples Verification Verdict** explicit enough to decide whether the thesis is category demand, channel restocking, cost pass-through, product-mix upgrade, prepared-dish optionality, dividend defensiveness, or merely valuation mean reversion. For frozen-food names such as Anjoy, explicitly test Spring Festival seasonality, distributor inventory, contract liabilities/advance receipts, inventory-to-revenue, raw-material cost proxies, promotion intensity, and Q2/Q3 margin follow-through. If it says `Status: not_applicable`, do not force food/beverage logic into the stock.
- If gated optical-module context says `Status: triggered`, keep an **AI Optical-Module Verification Verdict** explicit enough to decide whether the thesis is 800G share gain, 1.6T ramp, overseas cloud customer orders, product price/mix, exchange-rate tailwind, capacity/yield, AI capex durability, or merely valuation momentum. For Zhongji Innolight, Eoptolink, and similar names, explicitly test customer qualification, shipment mix, inventory/revenue, receivables/revenue, operating cash flow, gross margin, customer concentration, export/tariff risk, and CPO/LPO/silicon-photonics route risk. If it says `Status: not_applicable`, do not force optical-module or AI datacom logic into the stock.
- If gated biopharma context says `Status: triggered`, keep a **Biopharma Verification Verdict** explicit enough to separate commercialized products, label expansion, late-stage pipeline, early pipeline, regulatory review, reimbursement/pricing, BD economics, R&D spend, cash runway, and dilution risk. For CRO/CDMO/pharma-services names, separate order visibility, customer funding cycle, project conversion, capacity utilization, capex returns, geopolitical risk, and FCF durability from drug-owner pipeline logic. Clinical or regulatory missing data is a neutral research task; it is not proof of either approval or failure and does not mechanically alter the rating.
- If gated software context says `Status: triggered`, keep a **Software Verification Verdict** explicit enough to classify the software model and separate subscription/ARR quality, paid users, ARPU, renewal/churn, contract-liability conversion, project acceptance, receivables/cash collection, AI paid adoption, and model-labeled peer valuation. Missing metrics remain neutral model gaps; do not replace them with AI narratives or mechanically alter the rating.
- If gated insurance context says `Status: triggered`, keep an **Insurance Verification Verdict** explicit enough to separate life/health NBV and EV, channel quality, solvency, investment-yield spread, P&C COR, bank-subsidiary contribution, dividends, and SOTP optionality. If current EV is missing, say whether the latest annual EV can be used only as a stale-base cross-check. If it says `Status: not_applicable`, do not force insurance analysis into the stock.
- For insurance/high-dividend defensive candidates, separate absolute downside from sector-relative low-weighting and defensive-basket suitability. Treat one-quarter net profit, non-recurring profit, and operating cash flow as warning signals only; a sharp OCF decline is a hard negative cash-flow signal with unresolved attribution, not a soft concern and not standalone proof of franchise deterioration. Missing NBV, EV/P-EV, OPAT/core operating profit, CSM/NCSM, solvency, investment-yield spread, dividend coverage, or P&C COR remains neutral non-evidence; use verified indicators for the recommendation and do not mechanically force Hold/Underweight.
- For constructive insurance calls, calibrate rating strength before handing the plan downstream. If sizing should remain 1/3-1/2 target weight or below normal allocation until H1/annual validation, the default recommendation should be Hold/positive watch unless the insurance-native evidence already proves positive expected value on a standalone basis. Use staged/cautious Overweight only when the plan proves all three: verified NBV/OPAT/COR or EV evidence outweighs unresolved OCF/channel risks, valuation-implied expectations are explicitly too pessimistic, and downside is bounded by capital, payout, and solvency evidence.
- For insurance valuation and defensive-dividend claims, force a clean audit trail: reconcile interim dividend, final dividend, full-year DPS, payout ratio, yield-price base, and disclosure period; build SOTP from visible segment formulas, ownership stakes, per-share conversion, holding-company discount, and double-counting checks; label scenario probabilities as subjective PM/research underwriting weights. Compare the target with true insurer alternatives and decide whether it is a higher-beta NBV/SOTP recovery expression, a cleaner insurance-quality compounder, a dividend sleeve, or inferior to peers.
- Insurance peer-substitution rating gate: do not let a same-industry peer screen based only on PE/PB/ROE/dividend yield/one-quarter profit growth become the decisive reason for Underweight/Sell. Before recommending a peer switch, require comparable peer evidence on NBV growth, NBV margin, EV or P/EV, OCF/cash-quality trend, solvency, investment spread, payout coverage, channel mix, and P&C COR where applicable. Missing peer-native metrics are neutral and invalidate the peer-switch inference; they do not mechanically cap the target-company recommendation.
- If gated medical-device context says `Status: triggered`, keep a **Medical Device Verification Verdict** explicit enough to separate equipment installed base/replacement cycle, IVD analyzer plus reagent pull-through, consumables/procedure volume, VBP/procurement price pressure, registration/overseas channel quality, receivables/cash conversion, and product-mix/gross-margin durability. If it says `Status: not_applicable`, do not force medical-device analysis into the stock.
- If gated metals/mining context says `Status: triggered`, keep a **Metals / Mining Verification Verdict** explicit enough to separate exchange price proxies, realized selling price, reserve/resource quality, grade, equity production, AISC/unit cost, smelting/trading split, hedging/inventory, project capex/ramp, jurisdiction risk, balance-sheet survival, and NAV/SOTP. If it says `Status: not_applicable`, do not force metals/mining analysis into the stock.
- If verified but non-base-case optionality matters, keep a **Strategic Optionality Verdict** explicit enough that downstream agents do not erase a second growth curve, investee holding, asset revaluation path, or live thematic catalyst merely because it does not flip today's rating.
- If the thematic valuation bridge contains material `asset-revaluation` or primary-investment holdings, build an explicit **Primary Investment NAV Verdict**. Separate operating earnings from investee/NAV value; use conservative/base/upside values with liquidity, lock-up, exit-probability, and double-counting haircuts. Do not collapse verified non-listed equity holdings into a vague "small imagination premium" when ownership value, materiality, and an IPO/exit path are disclosed.
- Always read the Data Coverage Audit before ruling. If a module is failed, missing, or partial and touches the core bet, explicitly state the neutral gap and retrieval task. Preserve the recommendation derived from verified evidence; do not mechanically alter it because a channel failed.
- If financial-report intelligence says narrative filing text or readable report body was unavailable, do not write that the system failed to retrieve all financial data. First check whether structured statements, market data, peer comparison, valuation, and earnings-model contexts are present. Describe the gap narrowly as missing report-body/segment/management-discussion evidence unless those other modules also failed.

---

{continuity_context}
**Thematic Catalyst Cross-Check And Valuation Bridge:**
{thematic_catalyst_context}

**Industry Cycle Scan:**
{industry_cycle_context}

**Company Business Model Primer:**
{company_business_model_context}

**Structured Research Bundle (JSON source of record):**
{structured_research_context}

**Post-Analyst Fundamental Reconciliation Pack:**
{fundamentals_reconciliation_context}

**Post-Analyst Market Reconciliation Pack:**
{market_reconciliation_context}

**Industry KPI Checklist:**
{industry_kpi_context}

**Forward Forecast Model Scaffold:**
{forecast_model_context}

**Sell-Side Depth And Key-Number Audit:**
{quality_audit_context}

**Thesis Question Context:**
{thesis_question_context}

**Commodity/Product-Price Context:**
{commodity_context}

**Price-Move Attribution Context:**
{price_move_attribution_context}

**Relative-Strength / Index-Linkage Context:**
{relative_strength_context}

**Shipping/Freight-Rate Context:**
{shipping_context}

**Financial-Report Intelligence:**
{filing_intelligence_context}

**Same-Industry Peer Comparison:**
{peer_comparison_context}

**Cross-Position Supply-Chain Comparison:**
{supply_chain_comparison_context}

**Earnings-Model Context:**
{earnings_model_context}

**Market-Expectation Context:**
{market_expectation_context}

**Historical Price-EPS-PE Decomposition Context:**
{price_earnings_decomposition_context}

**Management/Capital-Allocation Context:**
{management_capital_allocation_context}

**Shareholder-Structure Context:**
{shareholder_structure_context}

**Official Investor-Interaction Context:**
{investor_interaction_context}

**Official Policy-Planning Context:**
{policy_planning_context}

**Web Fact-Check Context:**
{web_fact_check_context}

**Knowledge Planet Stream/PDF Intelligence:**
{knowledge_planet_context}

**Triggered Sector-Specific Research Layers:**
{gated_sector_context}

**Data Coverage Audit:**
{data_coverage_context}

**Debate History:**
{prompt_history}

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
{gated_sector_instructions}
{get_fair_cycle_valuation_instruction()}
{get_focused_report_instruction()}
If a bull or bear argument contains an exact product price, inventory figure, product spread, percentage change, or date-specific market claim that is not supported by the analyst reports or corroborated web fact-check context, downgrade that argument and list it as an unverified key assumption."""

        investment_plan, research_manager_generation_status = invoke_structured_or_freetext(
            structured_llm,
            llm,
            prompt,
            render_underwriting_research_plan,
            "Research Manager",
            return_metadata=True,
            fallback_schema=UnderwritingResearchPlan,
        )
        research_manager_plan_payload = research_manager_generation_status.pop(
            "validated_payload",
            {},
        )
        research_manager_generation_status["schema"] = "UnderwritingResearchPlan"

        underwriting_packet = dict(
            state.get("structured_research_context", {}).get(
                "underwriting_packet", {}
            )
        )
        initial_handoff_issues = _research_manager_handoff_issues(
            underwriting_packet,
            research_manager_plan_payload,
        ) if underwriting_packet and research_manager_plan_payload else []
        deterministic_copied_lines: list[str] = []
        if initial_handoff_issues:
            completed_payload, deterministic_copied_lines = (
                _complete_unchanged_handoff_lines(
                    underwriting_packet,
                    research_manager_plan_payload,
                )
            )
            if deterministic_copied_lines:
                try:
                    completed_plan = UnderwritingResearchPlan.model_validate(
                        completed_payload
                    )
                except (TypeError, ValueError):
                    deterministic_copied_lines = []
                else:
                    research_manager_plan_payload = completed_plan.model_dump(
                        mode="json"
                    )
                    investment_plan = render_underwriting_research_plan(completed_plan)
        repair_status: dict = {"mode": "not_run"}
        repair_applied = False
        remaining_handoff_issues = _research_manager_handoff_issues(
            underwriting_packet,
            research_manager_plan_payload,
        ) if underwriting_packet and research_manager_plan_payload else []
        llm_repair_issues = list(remaining_handoff_issues)
        if remaining_handoff_issues:
            repaired_plan, repair_status = invoke_structured_or_freetext(
                structured_llm,
                llm,
                _handoff_repair_prompt(
                    packet=underwriting_packet,
                    payload=research_manager_plan_payload,
                    issues=remaining_handoff_issues,
                ),
                render_underwriting_research_plan,
                "Research Manager Handoff Repair",
                return_metadata=True,
                fallback_schema=UnderwritingResearchPlan,
            )
            repaired_payload = repair_status.pop("validated_payload", {})
            if repaired_payload:
                repaired_issues = _research_manager_handoff_issues(
                    underwriting_packet,
                    repaired_payload,
                )
                if not repaired_issues:
                    investment_plan = repaired_plan
                    research_manager_plan_payload = repaired_payload
                    remaining_handoff_issues = []
                    repair_applied = True
        research_manager_generation_status.update(
            {
                "handoff_repair_requested": bool(llm_repair_issues),
                "handoff_repair_applied": repair_applied,
                "handoff_repair_mode": repair_status.get("mode", "not_run"),
                "handoff_deterministic_completion_applied": bool(
                    deterministic_copied_lines
                ),
                "handoff_deterministic_copied_lines": deterministic_copied_lines,
                "initial_handoff_issues": initial_handoff_issues,
                "remaining_handoff_issues": remaining_handoff_issues,
            }
        )

        new_investment_debate_state = {
            "judge_decision": investment_plan,
            "history": investment_debate_state.get("history", ""),
            "bear_history": investment_debate_state.get("bear_history", ""),
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": investment_plan,
            "count": investment_debate_state["count"],
        }

        return {
            "investment_debate_state": new_investment_debate_state,
            "investment_plan": investment_plan,
            "research_manager_generation_status": research_manager_generation_status,
            "research_manager_plan_payload": research_manager_plan_payload,
        }

    return research_manager_node
