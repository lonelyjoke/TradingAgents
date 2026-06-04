

from tradingagents.agents.utils.agent_utils import (
    get_buy_side_thesis_instruction,
    get_biopharma_instruction,
    get_compute_leasing_instruction,
    get_dividend_defensive_instruction,
    get_evidence_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_insurance_instruction,
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_investor_interaction_instruction,
    get_policy_planning_instruction,
    get_research_gap_instruction,
    get_software_instruction,
    get_supply_demand_fallback_instruction,
    get_thematic_valuation_instruction,
)
from tradingagents.dataflows.prompt_compaction import (
    compact_analyst_report,
    compact_for_prompt,
    compact_risk_history,
    compact_state_fields,
)


def create_neutral_debator(llm):
    def neutral_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        neutral_history = risk_debate_state.get("neutral_history", "")

        current_aggressive_response = risk_debate_state.get("current_aggressive_response", "")
        current_conservative_response = risk_debate_state.get("current_conservative_response", "")

        market_research_report = compact_analyst_report(state["market_report"], profile="risk")
        sentiment_report = compact_analyst_report(state["sentiment_report"], profile="risk")
        news_report = compact_analyst_report(state["news_report"], profile="risk")
        fundamentals_report = compact_analyst_report(state["fundamentals_report"], profile="risk")
        prompt_contexts = compact_state_fields(
            state,
            profile="risk",
            keys={
                "thematic_catalyst_context",
                "commodity_context",
                "filing_intelligence_context",
                "investor_interaction_context",
                "policy_planning_context",
                "shipping_context",
                "compute_leasing_context",
                "dividend_defensive_context",
                "biopharma_context",
                "software_context",
                "insurance_context",
                "medical_device_context",
                "metals_mining_context",
            },
        )
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        shipping_context = prompt_contexts["shipping_context"]
        filing_intelligence_context = prompt_contexts["filing_intelligence_context"]
        investor_interaction_context = prompt_contexts["investor_interaction_context"]
        policy_planning_context = prompt_contexts["policy_planning_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
        biopharma_context = prompt_contexts["biopharma_context"]
        software_context = prompt_contexts["software_context"]
        insurance_context = prompt_contexts["insurance_context"]
        medical_device_context = prompt_contexts["medical_device_context"]
        metals_mining_context = prompt_contexts["metals_mining_context"]
        prompt_history = compact_risk_history(history, profile="risk")
        prompt_aggressive_response = compact_for_prompt(
            current_aggressive_response,
            label="risk_history",
            profile="risk",
            max_chars=2500,
        )
        prompt_conservative_response = compact_for_prompt(
            current_conservative_response,
            label="risk_history",
            profile="risk",
            max_chars=2500,
        )

        trader_decision = state["trader_investment_plan"]

        prompt = f"""As the Neutral Risk Analyst, your role is to provide a balanced perspective, weighing both the potential benefits and risks of the trader's decision or plan. You prioritize a well-rounded approach, evaluating the upsides and downsides while factoring in broader market trends, potential economic shifts, and diversification strategies.Here is the trader's decision:

{trader_decision}

Your task is to challenge both the Aggressive and Conservative Analysts, pointing out where each perspective may be overly optimistic or overly cautious. Use insights from the following data sources to support a moderate, sustainable strategy to adjust the trader's decision:

Market Research Report: {market_research_report}
Social Media Sentiment Report: {sentiment_report}
Latest World Affairs Report: {news_report}
Company Fundamentals Report: {fundamentals_report}
Verified Thematic Catalyst Bridge: {thematic_catalyst_context}
Commodity/Product-Price Context: {commodity_context}
Shipping/Freight-Rate Context: {shipping_context}
Financial-Report Intelligence And Promoted Discussion Items: {filing_intelligence_context}
Official Investor-Interaction Context: {investor_interaction_context}
Official Policy-Planning Context: {policy_planning_context}
Gated Compute-Leasing Verification Context: {compute_leasing_context}
Gated Dividend Defensive Verification Context: {dividend_defensive_context}
Gated Biopharma Verification Context: {biopharma_context}
Gated Software Verification Context: {software_context}
Gated Insurance Verification Context: {insurance_context}
Gated Medical-Device Verification Context: {medical_device_context}
Gated Metals/Mining Verification Context: {metals_mining_context}
Here is the current conversation history: {prompt_history} Here is the last response from the aggressive analyst: {prompt_aggressive_response} Here is the last response from the conservative analyst: {prompt_conservative_response}. If there are no responses from the other viewpoints yet, present your own argument based on the available data.

Engage actively by analyzing both sides critically, addressing weaknesses in the aggressive and conservative arguments to advocate for a more balanced approach. Challenge each of their points to illustrate why a moderate risk strategy might offer the best of both worlds, providing growth potential while safeguarding against extreme volatility. Focus on debating rather than simply presenting data, aiming to show that a balanced view can lead to the most reliable outcomes. For commodity/resource/cyclical names, explicitly test whether product-price evidence supports or contradicts the risk stance. For shipping names, distinguish freight-rate evidence from freight-rate gaps, and evaluate two-sided Hormuz reopening/restocking mechanisms before changing risk posture. For biopharma names, balance pipeline optionality against clinical/regulatory/reimbursement/cash-runway evidence gaps, and keep CRO/CDMO order-cycle risk separate from drug-owner pipeline risk. For software names, balance subscription/AI optionality against paid-user, ARPU, renewal/churn, contract-liability conversion, project acceptance, and cash-collection evidence gaps; translate missing software-native evidence into sizing, verification calendar, and falsification triggers. For insurance names, balance NBV/EV/dividend/SOTP optionality against solvency, investment-yield, channel, P&C COR, and bank-subsidiary evidence gaps; translate missing insurance-native evidence into sizing, verification calendar, and falsification triggers. For medical-device names, balance installed-base, reagent, replacement-cycle, and overseas optionality against VBP, registration, tender, channel inventory, receivable, and cash-conversion evidence gaps; translate missing device-native evidence into sizing, verification calendar, and falsification triggers. For metals/mining names, balance metal-price, reserve, output, and NAV/SOTP optionality against AISC, grade, hedge, inventory, capex, project-ramp, jurisdiction, leverage, and data-source gaps; translate missing mining-native evidence into sizing, verification calendar, and falsification triggers. Preserve core discussion items that matter to the thesis even when they belong in scenario analysis rather than the base case. {get_evidence_instruction()} {get_research_gap_instruction()} {get_supply_demand_fallback_instruction()} {get_buy_side_thesis_instruction()} {get_fair_cycle_valuation_instruction()} {get_thematic_valuation_instruction()} {get_filing_intelligence_instruction()} {get_investor_interaction_instruction()} {get_policy_planning_instruction()} {get_compute_leasing_instruction()} {get_dividend_defensive_instruction()} {get_biopharma_instruction()} {get_software_instruction()} {get_insurance_instruction()} {get_medical_device_instruction()} {get_metals_mining_instruction()} {get_focused_report_instruction()} Output conversationally as if you are speaking without any special formatting."""

        response = llm.invoke(prompt)

        argument = f"Neutral Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "aggressive_history": risk_debate_state.get("aggressive_history", ""),
            "conservative_history": risk_debate_state.get("conservative_history", ""),
            "neutral_history": neutral_history + "\n" + argument,
            "latest_speaker": "Neutral",
            "current_aggressive_response": risk_debate_state.get(
                "current_aggressive_response", ""
            ),
            "current_conservative_response": risk_debate_state.get("current_conservative_response", ""),
            "current_neutral_response": argument,
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return neutral_node
