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
    get_earnings_model_context,
    get_financial_report_intelligence_context,
    get_income_statement,
    get_market_sector_risk,
    get_market_expectation_context,
    get_market_timing_context,
    get_management_capital_allocation_context,
    get_peer_comparison,
    get_shareholder_structure_context,
    get_supply_chain_comparison,
    get_shipping_context,
    get_thematic_catalyst_context,
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


def get_material_catalyst_instruction() -> str:
    """Return rules for handling genuine thematic catalysts without chasing noise."""
    return (
        " Material-catalyst discipline: for A-share names, actively check whether "
        "there are company-specific themes that can genuinely affect cash flow, "
        "asset value, or valuation anchors, such as investee IPOs, asset listings, "
        "verified new-business commercialization, policy licenses, major signed "
        "orders, or capacity milestones. A theme may enter valuation only if it "
        "passes all four gates: (1) verifiable evidence from filings, exchange "
        "documents, official disclosures, or equivalent primary sources; "
        "(2) a clear economic transmission path to earnings, NAV, or valuation; "
        "(3) a trackable catalyst timetable or milestone; and (4) materiality "
        "large enough to matter for the listed company. Classify qualifying "
        "themes as asset-revaluation catalysts or business-realization catalysts. "
        "Use filing/news cross-validation rather than one-sided discovery: scan "
        "annual and half-year report text for candidate investees, assets, and "
        "new-business lines, then look for recent news catalysts; for any theme "
        "first discovered in news, require validation from annual or half-year "
        "report text before it may affect valuation. "
        "If a topic is only a market label, media narrative, vague interaction, "
        "or unsupported concept, list it as a rejected theme and do not let it "
        "change valuation or rating."
    )


def get_thematic_valuation_instruction() -> str:
    """Return rules for converting verified themes into valuation arguments."""
    return (
        " Thematic-valuation discipline: do not stop at naming a catalyst. "
        "For every verified theme, state the valuation bridge explicitly. "
        "For asset-revaluation themes, discuss ownership exposure, disclosed "
        "carrying or fair value, listed-company market-cap materiality, catalyst "
        "timing, realizability, dilution/lock-up/liquidity haircuts, and whether "
        "the correct treatment is SOTP/NAV uplift, qualitative optionality, or "
        "exclusion. For business-realization themes, require disclosed revenue, "
        "profit, order, contract, or cash-flow evidence before allowing the theme "
        "into core valuation; otherwise keep it as scenario upside rather than "
        "base-case earnings. Bulls should quantify what the market may be "
        "underpricing; bears should test monetization, ownership, double-counting, "
        "timing, and materiality. Never let an attractive story enter valuation "
        "without saying exactly how much value it could add and what would make "
        "that bridge fail."
    )


def get_peer_selection_instruction() -> str:
    """Return rules for deciding whether a same-industry peer is a better build candidate."""
    return (
        " Peer-selection discipline: every recommendation must answer the cross-sectional "
        "question, not just the single-name question. Compare the target with same-industry "
        "peers on valuation, profitability, growth, leverage, cash quality, shareholder "
        "return, and any industry-specific operating metrics available. State explicitly "
        "whether the target is the best build candidate in the sampled peer set, merely "
        "acceptable, or inferior to one or more alternatives. If another peer is better, "
        "name it, explain the concrete metrics and business reasons, and say whether that "
        "weakens the target to watch/underweight rather than build now. If no peer is clearly "
        "better, say why no superior alternative emerged; never treat a lower PE alone as "
        "proof of superiority."
    )


def get_supply_chain_selection_instruction() -> str:
    """Return rules for comparing different profit pools inside one industrial chain."""
    return (
        " Supply-chain-selection discipline: when a curated industrial-chain map is "
        "available, answer a second cross-sectional question after peer selection: "
        "is the target sitting in the best part of the chain to own now? Compare "
        "different chain positions on economics, scarcity, pricing power, earnings "
        "revision potential, valuation, and balance-sheet quality. State explicitly "
        "whether the better build opportunity lies in the target's own segment or "
        "in another profit pool of the same chain. If another segment is better, "
        "explain why the investor should consider rotating across the chain rather "
        "than merely switching names within one segment. Never force this verdict "
        "for industries whose value-chain map is not yet defined."
    )


def get_earnings_model_instruction() -> str:
    """Return rules for forcing every thesis through an earnings bridge."""
    return (
        " Earnings-model discipline: every investable thesis must pass through an "
        "earnings bridge. State which operating levers move revenue, which levers "
        "move margin, and how they flow into profit, cash generation, and finally "
        "valuation. Use bull/base/bear scenarios only when each case changes a "
        "specific modeled assumption such as volume, price, mix, utilization, "
        "gross margin, working capital, or financing cost. A catalyst that cannot "
        "be mapped to a modeled lever is not yet a valuation catalyst."
    )


def get_market_expectation_instruction() -> str:
    """Return rules for separating business quality from what is already priced."""
    return (
        " Market-expectation discipline: always distinguish a good company from "
        "a good investment. Read the current quote as an implied bundle of "
        "assumptions about earnings power, sales scale, margin durability, and "
        "growth persistence. State explicitly whether the market appears to price "
        "recovery, stagnation, or deterioration, then identify the precise "
        "assumption where your view differs. Never call a stock cheap or expensive "
        "from PE/PB alone."
    )


def get_three_layer_conclusion_instruction() -> str:
    """Return rules for splitting the final verdict into three different questions."""
    return (
        " Three-layer conclusion discipline: keep three questions separate in the "
        "final verdict. Company quality asks whether the business is good. Current "
        "odds ask whether today's price offers attractive expected value. Relative "
        "allocation asks whether this is the best place to deploy capital versus "
        "same-industry peers and alternative chain positions. A stock may score "
        "well on one layer and poorly on another; do not collapse them into a "
        "single undifferentiated opinion."
    )


def get_management_capital_allocation_instruction() -> str:
    """Return rules for judging stewardship with hard evidence."""
    return (
        " Management-and-capital-allocation discipline: judge stewardship from "
        "hard signals before praise. Use capital returns, buybacks, dividends, "
        "financing, acquisitions, capex, leverage, goodwill, and later ROIC / "
        "cash-flow outcomes to decide whether management compounds value, merely "
        "grows assets, or dilutes owners. Treat management quality as a synthesis "
        "variable: hard evidence can support or weaken the case, but a single "
        "title, speech, or compensation table is never enough by itself."
    )


def get_shareholder_structure_instruction() -> str:
    """Return rules for reading ownership and chip signals without overfitting them."""
    return (
        " Shareholder-structure discipline: use top holders, float holders, holder "
        "count, insider increases/decreases, pledge ratio, repurchases, and unlock "
        "schedule to refine supply-demand and governance risk. Explain whether "
        "ownership is stabilizing, crowded, or becoming a supply overhang, but do "
        "not let chip signals override the business thesis unless size, timing, "
        "and materiality are clear."
    )


def get_filing_intelligence_instruction() -> str:
    """Return rules for using business evidence buried inside filings."""
    return (
        " Filing-intelligence discipline: read quarterly, half-year, and annual "
        "reports as business documents, not only as sources of the three statements. "
        "Actively use filing-derived evidence on orders, backlog, customers, "
        "commercialization, prices, margins, capacity, capex, overseas expansion, "
        "R&D, receivables, inventory, cash collection, guarantees, litigation, "
        "impairment, and related-party risk. Bulls should use quantified filing "
        "evidence to support visibility, moat, monetization, and inflection. Bears "
        "should use the same filings to challenge margin durability, working-capital "
        "quality, capital intensity, customer concentration, governance, and tail "
        "risk. Use quarterly reports to test short-cycle confirmation, half-year "
        "reports to judge trend formation and segment mix, and annual reports to "
        "judge business model, capital allocation, and long-cycle risk. Distinguish "
        "audited or quantified disclosures from management narrative, prefer the "
        "latest report when facts evolve, and explain what changed across reports "
        "when that matters."
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


        
