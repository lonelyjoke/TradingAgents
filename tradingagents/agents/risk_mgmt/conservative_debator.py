

from tradingagents.agents.utils.agent_utils import (
    get_buy_side_thesis_instruction,
    get_biopharma_instruction,
    get_compute_leasing_instruction,
    get_consumer_staples_instruction,
    get_dividend_defensive_instruction,
    get_evidence_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_insurance_instruction,
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_optical_module_instruction,
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


def create_conservative_debator(llm):
    def conservative_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        conservative_history = risk_debate_state.get("conservative_history", "")

        current_aggressive_response = risk_debate_state.get("current_aggressive_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

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
                "consumer_staples_context",
                "optical_module_context",
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
        consumer_staples_context = prompt_contexts["consumer_staples_context"]
        optical_module_context = prompt_contexts["optical_module_context"]
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
        prompt_neutral_response = compact_for_prompt(
            current_neutral_response,
            label="risk_history",
            profile="risk",
            max_chars=2500,
        )

        trader_decision = state["trader_investment_plan"]

        prompt = f"""As the Conservative Risk Analyst, your primary objective is to protect assets, minimize volatility, and ensure steady, reliable growth. You prioritize stability, security, and risk mitigation, carefully assessing potential losses, economic downturns, and market volatility. When evaluating the trader's decision or plan, critically examine high-risk elements, pointing out where the decision may expose the firm to undue risk and where more cautious alternatives could secure long-term gains. Here is the trader's decision:

{trader_decision}

Your task is to actively counter the arguments of the Aggressive and Neutral Analysts, highlighting where their views may overlook potential threats or fail to prioritize sustainability. Respond directly to their points, drawing from the following data sources to build a convincing case for a low-risk approach adjustment to the trader's decision:

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
Gated Consumer-Staples Verification Context: {consumer_staples_context}
Gated AI Optical-Module Verification Context: {optical_module_context}
Gated Dividend Defensive Verification Context: {dividend_defensive_context}
Gated Biopharma Verification Context: {biopharma_context}
Gated Software Verification Context: {software_context}
Gated Insurance Verification Context: {insurance_context}
Gated Medical-Device Verification Context: {medical_device_context}
Gated Metals/Mining Verification Context: {metals_mining_context}
Here is the current conversation history: {prompt_history} Here is the last response from the aggressive analyst: {prompt_aggressive_response} Here is the last response from the neutral analyst: {prompt_neutral_response}. If there are no responses from the other viewpoints yet, present your own argument based on the available data.

Engage by questioning their optimism and emphasizing the potential downsides they may have overlooked. Address each of their counterpoints to showcase why a conservative stance is ultimately the safest path for the firm's assets. Focus on debating and critiquing their arguments to demonstrate the strength of a low-risk strategy over their approaches. For commodity/resource/cyclical names, explicitly test whether product-price evidence supports or contradicts the risk stance. For shipping names, use freight-rate context to challenge route-level evidence gaps, but do not treat missing VLCC TD3C/TCE/CTFI as bearish by itself; weigh it against verified company lock-rate, demand, valuation, and Hormuz mechanism evidence. For consumer-staples names, emphasize unverified channel sell-through, distributor inventory, contract liabilities, raw-material cost, promotion intensity, food safety, and Q2/Q3 margin follow-through; missing consumer-native evidence should cap sizing rather than become invented downside proof. For optical-module names, emphasize customer concentration, unverified 800G/1.6T orders, ASP erosion, inventory build, receivable growth, weak OCF conversion, capacity/yield risk, export/tariff exposure, and CPO/LPO/silicon-photonics substitution; missing optical-module evidence should cap sizing rather than become invented downside proof. For biopharma names, emphasize trial design, approval, reimbursement, competition, cash burn, dilution, and CRO/CDMO order-cycle risks; missing clinical evidence should cap sizing rather than become invented downside proof. For software names, emphasize paid-user, ARPU, renewal/churn, contract-liability conversion, project acceptance, receivables, and AI monetization risks; missing software-native evidence should cap sizing rather than become invented downside proof. For insurance names, emphasize weak NBV/EV, channel productivity, solvency, investment-yield spread, P&C COR, dividend coverage, and bank-subsidiary over-blending; missing insurance-native evidence should cap sizing rather than become invented downside proof. For medical-device names, emphasize weak installed-base evidence, tender/procurement slowdown, VBP price pressure, poor reagent pull-through, registration/channel risk, receivables, inventory, and cash-conversion gaps; missing device-native evidence should cap sizing rather than become invented downside proof. For metals/mining names, emphasize weak reserve/grade evidence, high AISC, weak equity output, project delay, smelting/trading dilution, inventory/derivative risk, leverage, capex overrun, jurisdiction risk, and unsupported NAV/SOTP; missing mining-native evidence should cap sizing rather than become invented downside proof. Preserve core discussion items that matter to the thesis even when they do not change the final action today. {get_evidence_instruction()} {get_research_gap_instruction()} {get_supply_demand_fallback_instruction()} {get_buy_side_thesis_instruction()} {get_fair_cycle_valuation_instruction()} {get_thematic_valuation_instruction()} {get_filing_intelligence_instruction()} {get_investor_interaction_instruction()} {get_policy_planning_instruction()} {get_compute_leasing_instruction()} {get_consumer_staples_instruction()} {get_optical_module_instruction()} {get_dividend_defensive_instruction()} {get_biopharma_instruction()} {get_software_instruction()} {get_insurance_instruction()} {get_medical_device_instruction()} {get_metals_mining_instruction()} {get_focused_report_instruction()} Output conversationally as if you are speaking without any special formatting."""

        response = llm.invoke(prompt)

        argument = f"Conservative Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "aggressive_history": risk_debate_state.get("aggressive_history", ""),
            "conservative_history": conservative_history + "\n" + argument,
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Conservative",
            "current_aggressive_response": risk_debate_state.get(
                "current_aggressive_response", ""
            ),
            "current_conservative_response": argument,
            "current_neutral_response": risk_debate_state.get(
                "current_neutral_response", ""
            ),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return conservative_node
