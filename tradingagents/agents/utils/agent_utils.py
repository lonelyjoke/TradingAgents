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


def get_derived_financial_metric_instruction() -> str:
    """Return rules for using calculated ratios when reported indicators are missing."""
    return (
        " Derived financial metric discipline: when ready-made indicators such "
        "as gross margin, operating margin, net margin, cash-conversion ratio, "
        "or debt ratio are missing, use explicitly labelled derived metrics "
        "calculated from the income statement, balance sheet, and cash-flow "
        "statement. Do not call derived metrics company-disclosed indicators. "
        "For interim A-share reports, remember that income and cash-flow fields "
        "may be period-to-date rather than standalone single-quarter figures. "
        "Use derived metrics to improve judgment, but explain their accounting "
        "limits when they materially affect the thesis. Also read forward-looking "
        "accounting signals from contract liabilities, advance receipts, contract "
        "assets, receivables, inventories, prepayments, payables, goodwill, net "
        "cash, and working capital. Interpret them by business model: contract "
        "liabilities can indicate order visibility for project or subscription "
        "businesses, but may be less meaningful for spot commodity sales; rising "
        "inventory can be proactive stocking in an upcycle or demand pressure in "
        "a downturn; rising receivables can mean growth or collection risk. Use "
        "these signals as evidence for future revenue/profit inference only when "
        "the accounting item, industry context, and cash-flow quality point in "
        "the same direction."
    )


def get_buy_side_accounting_radar_instruction() -> str:
    """Return a buy-side accounting checklist for forward-looking financial analysis."""
    return (
        " Buy-side accounting radar: read financial statements as reliable but "
        "lagging evidence. Organize accounting analysis around five questions. "
        "First, is revenue real: compare revenue growth with receivables, notes "
        "receivable, contract assets, cash received from customers, and operating "
        "cash flow. Second, is profit quality durable: inspect gross margin, "
        "operating margin, expense ratios, R&D intensity, finance costs, impairment "
        "losses, investment income, fair-value gains, non-operating gains, and "
        "deducted recurring profit if available. Third, are there forward-looking "
        "clues: read contract liabilities, advance receipts, inventories, "
        "prepayments, capex, construction in progress, and order/capacity signals "
        "in the context of the industry cycle. Fourth, can the balance sheet "
        "survive the cycle: check net cash/debt, short-term debt pressure, working "
        "capital, liquidity, goodwill, asset impairment risk, and cash conversion. "
        "Fifth, are shareholder returns aligned: consider dividend sustainability, "
        "buybacks, dilution, minority interests, and whether capital expenditure "
        "is creating future earnings or destroying returns. Do not list every "
        "item mechanically; highlight only the accounting signals that change "
        "the thesis, rating, or falsification conditions."
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


def get_fair_cycle_valuation_instruction() -> str:
    """Return fair calibration rules across valuation and cycle regimes."""
    return (
        " Fair cycle-valuation calibration: evaluate the stock through a neutral "
        "valuation x business-cycle lens. Do not mechanically reward cheapness, "
        "penalize low prosperity, reward high prosperity, or penalize high "
        "valuation. Classify the setup: low valuation/low prosperity, high "
        "valuation/high prosperity, low valuation/high prosperity, or high "
        "valuation/low prosperity. For low valuation/low prosperity names, ask "
        "whether pessimism is fully priced, whether the downturn is cyclical or "
        "structural, whether the company can survive the trough, and whether "
        "there are marginal improvement signals. For high prosperity/high "
        "valuation names, ask whether growth durability and earnings upgrades can "
        "digest valuation, whether crowding is excessive, and what happens if the "
        "cycle rolls over. For low valuation/high prosperity names, test whether "
        "the cheapness reflects overlooked opportunity or unsustainable earnings. "
        "For high valuation/low prosperity names, require clear future inflection "
        "or scarce growth to justify anything above Hold. The rating must follow "
        "expected value: probability, payoff, duration, balance-sheet resilience, "
        "and expectation gap."
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


        
