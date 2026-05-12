from langchain_core.messages import HumanMessage, RemoveMessage

# Import tools from separate utility files
from tradingagents.agents.utils.core_stock_tools import (
    get_stock_data
)
from tradingagents.agents.utils.technical_indicators_tools import (
    get_indicators
)
from tradingagents.agents.utils.fundamental_data_tools import (
    get_fundamentals,
    get_balance_sheet,
    get_cashflow,
    get_commodity_context,
    get_income_statement,
    get_market_sector_risk,
    get_market_timing_context,
    get_peer_comparison,
    get_shipping_context,
    get_valuation_percentiles,
)
from tradingagents.agents.utils.news_data_tools import (
    get_company_events,
    get_news,
    get_insider_transactions,
    get_global_news
)


def get_language_instruction() -> str:
    """Return a prompt instruction for the configured output language.

    Returns empty string when English (default), so no extra tokens are used.
    Only applied to user-facing agents (analysts, portfolio manager).
    Internal debate agents stay in English for reasoning quality.
    """
    from tradingagents.dataflows.config import get_config
    lang = get_config().get("output_language", "English")
    if lang.strip().lower() == "english":
        return ""
    return f" Write your entire response in {lang}."


def get_evidence_instruction() -> str:
    """Return anti-hallucination rules for numeric investment claims."""
    return (
        " Evidence discipline: any concrete number, percentage, price, inventory, "
        "capacity, production quota, product spread, or date-specific market claim "
        "must be grounded in the supplied tool outputs or analyst reports. If the "
        "supporting evidence is absent, explicitly label it as an unverified key "
        "assumption and do not present it as fact. Never invent commodity prices, "
        "inventory levels, product-price changes, or policy details."
    )


def get_research_gap_instruction() -> str:
    """Return rules for handling missing but thesis-critical evidence."""
    return (
        " Research-gap discipline: when a thesis-critical driver is missing "
        "(for example product prices, product spreads, inventory, freight rates, "
        "policy details, capacity, order backlog, or utilization), do not let the "
        "analysis collapse into technical indicators or static PE/PB alone. Treat "
        "the missing driver as a critical research gap, explain why it matters, "
        "and build conditional scenarios from the evidence that is available. "
        "If the missing driver is essential to a bullish or bearish claim, cap "
        "conviction, label the conclusion as evidence-limited, and list the exact "
        "data that should be checked next. Hold is appropriate only when the "
        "verified bull and bear evidence is genuinely balanced, not merely because "
        "important operating evidence is unavailable."
    )


def get_supply_demand_fallback_instruction() -> str:
    """Return rules for macro supply-demand analysis when micro data is unavailable."""
    return (
        " Supply-demand fallback: if micro data for a key product or route is "
        "unavailable, use macro supply-demand evidence instead, but keep it "
        "product-specific rather than generic. Discuss the product's traits "
        "(standardized vs non-standardized, storability, import/export exposure, "
        "policy sensitivity, substitution risk), upstream cost drivers, downstream "
        "demand industries, inventory or operating-rate proxies, capacity additions "
        "or shutdowns, and whether margins/spreads can be inferred from verified "
        "inputs. Clearly separate verified macro proxies from unverified micro "
        "prices. Do not say 'demand is improving' or 'supply is tight' unless you "
        "name the concrete channel, affected upstream/downstream link, and evidence "
        "strength."
    )


def get_buy_side_thesis_instruction() -> str:
    """Return rules that make the framework more like a buy-side thesis memo."""
    return (
        " Buy-side thesis discipline: do not behave like a static fact checker. "
        "For every directional view, first state the core bet: what future variable "
        "the investor is actually underwriting. Then judge whether the boom-bust "
        "or business-cycle expectation can plausibly happen using verified data, "
        "proxy data, and bounded inference. Separate facts from inference, but do "
        "not default to Hold just because some data is missing. A direction can be "
        "valid when the probability/payoff is attractive and the thesis is "
        "falsifiable. Always discuss expectation gap: whether the market may have "
        "already priced the thesis, or whether there is a plausible mispricing. "
        "State catalyst path, falsification signals, conviction level, and position "
        "implication. Use Hold only when there is no clear tradable thesis, the "
        "expectation gap is weak, or probability/payoff is not attractive."
    )


def get_focused_report_instruction() -> str:
    """Return rules for keeping reports concise and decision-relevant."""
    return (
        " Focus discipline: prioritize decision-relevant evidence over exhaustive "
        "data listing. Do not restate every financial line, every indicator, or "
        "every tool output. Keep the memo organized around thesis, key evidence, "
        "missing evidence, expectation gap, risk/reward, and next verification "
        "signals. Compress routine background unless it changes the rating."
    )


def build_instrument_context(ticker: str) -> str:
    """Describe the exact instrument so agents preserve exchange-qualified tickers."""
    return (
        f"The instrument to analyze is `{ticker}`. "
        "Use this exact ticker in every tool call, report, and recommendation, "
        "preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`)."
    )

def create_msg_delete():
    def delete_messages(state):
        """Clear messages and add placeholder for Anthropic compatibility"""
        messages = state["messages"]

        # Remove all messages
        removal_operations = [RemoveMessage(id=m.id) for m in messages]

        # Add a minimal placeholder message
        placeholder = HumanMessage(content="Continue")

        return {"messages": removal_operations + [placeholder]}

    return delete_messages


        
