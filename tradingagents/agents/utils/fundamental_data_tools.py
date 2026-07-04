from langchain_core.tools import tool
from typing import Annotated
from tradingagents.dataflows.interface import route_to_vendor


@tool
def get_fundamentals(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve comprehensive fundamental data for a given ticker symbol.
    Uses the configured fundamental_data vendor.
    Args:
        ticker (str): Ticker symbol of the company
        curr_date (str): Current date you are trading at, yyyy-mm-dd
    Returns:
        str: A formatted report containing comprehensive fundamental data
    """
    return route_to_vendor("get_fundamentals", ticker, curr_date)


@tool
def get_balance_sheet(
    ticker: Annotated[str, "ticker symbol"],
    freq: Annotated[str, "reporting frequency: annual/quarterly"] = "quarterly",
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"] = None,
) -> str:
    """
    Retrieve balance sheet data for a given ticker symbol.
    Uses the configured fundamental_data vendor.
    Args:
        ticker (str): Ticker symbol of the company
        freq (str): Reporting frequency: annual/quarterly (default quarterly)
        curr_date (str): Current date you are trading at, yyyy-mm-dd
    Returns:
        str: A formatted report containing balance sheet data
    """
    return route_to_vendor("get_balance_sheet", ticker, freq, curr_date)


@tool
def get_cashflow(
    ticker: Annotated[str, "ticker symbol"],
    freq: Annotated[str, "reporting frequency: annual/quarterly"] = "quarterly",
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"] = None,
) -> str:
    """
    Retrieve cash flow statement data for a given ticker symbol.
    Uses the configured fundamental_data vendor.
    Args:
        ticker (str): Ticker symbol of the company
        freq (str): Reporting frequency: annual/quarterly (default quarterly)
        curr_date (str): Current date you are trading at, yyyy-mm-dd
    Returns:
        str: A formatted report containing cash flow statement data
    """
    return route_to_vendor("get_cashflow", ticker, freq, curr_date)


@tool
def get_income_statement(
    ticker: Annotated[str, "ticker symbol"],
    freq: Annotated[str, "reporting frequency: annual/quarterly"] = "quarterly",
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"] = None,
) -> str:
    """
    Retrieve income statement data for a given ticker symbol.
    Uses the configured fundamental_data vendor.
    Args:
        ticker (str): Ticker symbol of the company
        freq (str): Reporting frequency: annual/quarterly (default quarterly)
        curr_date (str): Current date you are trading at, yyyy-mm-dd
    Returns:
        str: A formatted report containing income statement data
    """
    return route_to_vendor("get_income_statement", ticker, freq, curr_date)


@tool
def get_commodity_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "commodity/futures look-back window in days"] = 90,
) -> str:
    """
    Retrieve evidence-backed commodity price, futures proxy, inventory/warehouse
    receipt, and product-price context for an A-share company.
    """
    return route_to_vendor("get_commodity_context", ticker, curr_date, look_back_days)


@tool
def get_price_move_attribution_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "short-horizon attribution look-back window in days"] = 60,
) -> str:
    """
    Attribute a recent A-share price move across market indexes, same-metal
    equities, cross-metal equities, mapped commodity futures, company events,
    and valuation/trading diagnostics. Use it for sharp drops or rallies where
    the question is whether the move is commodity-led, sector-led,
    stock-specific, failed-rebound/trend continuation, or possible emotion kill.
    """
    return route_to_vendor("get_price_move_attribution_context", ticker, curr_date, look_back_days)


@tool
def get_intraday_behavior_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "minute K-line look-back window in calendar days"] = 10,
) -> str:
    """
    Retrieve A-share historical minute K-line behavior context for PM validation.
    Use it after fundamental research to assess intraday confirmation, liquidity,
    volume concentration, entry timing, and whether the move looks like company
    alpha, sector beta, or broad risk appetite.
    """
    return route_to_vendor("get_intraday_behavior_context", ticker, curr_date, look_back_days)


@tool
def get_shipping_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "shipping/freight look-back window in days"] = 90,
) -> str:
    """
    Retrieve evidence-backed shipping cycle context, including broad tanker,
    product tanker, dry bulk, and route coverage notes for A-share shipping companies.
    """
    return route_to_vendor("get_shipping_context", ticker, curr_date, look_back_days)


@tool
def get_consumer_staples_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report and consumer context look-back window in days"] = 900,
) -> str:
    """
    Retrieve gated consumer-staples / food-beverage context for A-share companies,
    including category-native demand, channel, inventory, cost, and macro evidence discipline.
    """
    return route_to_vendor("get_consumer_staples_context", ticker, curr_date, look_back_days)


@tool
def get_optical_module_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report and optical-module context look-back window in days"] = 900,
) -> str:
    """
    Retrieve gated AI optical-module / datacom hardware context for A-share
    companies, including supply-chain role, AI capex bridge, high-speed module
    migration, working-capital quality, customer concentration, and technology-route risk.
    """
    return route_to_vendor("get_optical_module_context", ticker, curr_date, look_back_days)


@tool
def get_peer_comparison(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    peer_limit: Annotated[int, "number of same-industry peers to compare"] = 12,
) -> str:
    """
    Retrieve same-industry peer comparison for an A-share ticker.
    Uses valuation, profitability, growth, leverage, and dividend metrics to
    identify whether comparable companies may look stronger than the target.
    """
    return route_to_vendor("get_peer_comparison", ticker, curr_date, peer_limit)


@tool
def get_supply_chain_comparison(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Compare a company with alternative profit pools across different positions
    of the same industrial chain, when a curated chain map exists.
    """
    return route_to_vendor("get_supply_chain_comparison", ticker, curr_date)


@tool
def get_valuation_percentiles(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    years: Annotated[int, "historical look-back years"] = 5,
) -> str:
    """
    Retrieve historical valuation percentile context for an A-share ticker.
    This helps distinguish historically cheap, mid-range, and expensive valuation zones.
    """
    return route_to_vendor("get_valuation_percentiles", ticker, curr_date, years)


@tool
def get_market_sector_risk(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "market trend look-back days"] = 120,
    years: Annotated[int, "index valuation history years"] = 5,
) -> str:
    """
    Retrieve broad-market and same-industry valuation risk for an A-share ticker.
    This flags high market/sector risk and cases where the sector is expensive
    while the target itself looks relatively cheap.
    """
    return route_to_vendor("get_market_sector_risk", ticker, curr_date, look_back_days, years)


@tool
def get_market_timing_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "market mood look-back window in days"] = 120,
    years: Annotated[int, "index valuation history years"] = 5,
) -> str:
    """
    Retrieve market sentiment/regime context and rating-calibration guidance.
    This helps adjust bullish or bearish conclusions based on broad-market
    valuation and mood, while still requiring company-level evidence.
    """
    return route_to_vendor("get_market_timing_context", ticker, curr_date, look_back_days, years)


@tool
def get_relative_strength_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "relative-strength look-back calendar days"] = 380,
    peer_limit: Annotated[int, "same-industry peer count for equal-weight basket"] = 12,
) -> str:
    """
    Retrieve stock-versus-index relative strength, excess return, correlation,
    beta, and same-industry basket context for an A-share ticker. Use it to
    judge whether price action confirms the thesis, is mostly sector beta, or
    reveals a stock-specific divergence.
    """
    return route_to_vendor("get_relative_strength_context", ticker, curr_date, look_back_days, peer_limit)


@tool
def get_thematic_catalyst_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    financial_look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
    news_look_back_days: Annotated[int, "news look-back window in days"] = 180,
) -> str:
    """
    Discover and cross-check A-share thematic catalysts from two directions:
    filing-origin candidates are checked against news, while news-origin
    candidates must be validated against annual/half-year report text.
    """
    return route_to_vendor(
        "get_thematic_catalyst_context",
        ticker,
        curr_date,
        financial_look_back_days,
        news_look_back_days,
    )


@tool
def get_financial_report_intelligence_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
) -> str:
    """
    Extract non-statement operating evidence from annual and half-year reports:
    orders, commercialization, pricing/margins, capacity/capex, customer/geography,
    R&D/product, working-capital quality, and balance-sheet risk disclosures.
    """
    return route_to_vendor(
        "get_financial_report_intelligence_context",
        ticker,
        curr_date,
        look_back_days,
    )


@tool
def get_earnings_model_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve an evidence-led earnings bridge for an A-share ticker, including
    driver history and scenario-modeling instructions.
    """
    return route_to_vendor("get_earnings_model_context", ticker, curr_date)


@tool
def get_market_expectation_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve a reverse-looking expectation context that translates current
    valuation into the earnings power the market is approximately implying.
    """
    return route_to_vendor("get_market_expectation_context", ticker, curr_date)


@tool
def get_price_earnings_decomposition_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    years: Annotated[int, "historical look-back years"] = 5,
) -> str:
    """
    Decompose historical stock-price moves into EPS-proxy change versus PE-multiple change.
    """
    return route_to_vendor(
        "get_price_earnings_decomposition_context",
        ticker,
        curr_date,
        years,
    )


@tool
def get_management_capital_allocation_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve hard-signal context on management stewardship and capital
    allocation behavior for an A-share company.
    """
    return route_to_vendor("get_management_capital_allocation_context", ticker, curr_date)


@tool
def get_shareholder_structure_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve shareholder concentration, float ownership, holder-count,
    pledge, increase/decrease, and unlock context for an A-share company.
    """
    return route_to_vendor("get_shareholder_structure_context", ticker, curr_date)


@tool
def get_investor_interaction_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve official investor-interaction history for an A-share company,
    including normalized Q&A, theme reads, and narrative-evidence diagnostics.
    """
    return route_to_vendor("get_investor_interaction_context", ticker, curr_date)


@tool
def get_policy_planning_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve official policy-planning context for an A-share company, including
    national-plan and routed industry-plan mapping plus analyst guidance on
    policy-to-demand bridges.
    """
    return route_to_vendor("get_policy_planning_context", ticker, curr_date)


@tool
def get_web_fact_check_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    max_queries: Annotated[int, "maximum search queries to run"] = 3,
    max_results_per_query: Annotated[int, "maximum search results per query"] = 4,
) -> str:
    """
    Search the web for small but thesis-critical high-frequency facts such as
    baijiu wholesale prices, channel inventory, terminal discounts, product
    price changes, or recent sales clues. Results are evidence-ranked and must
    not be treated as filing-grade proof unless the source is official.
    """
    return route_to_vendor(
        "get_web_fact_check_context",
        ticker,
        curr_date,
        max_queries,
        max_results_per_query,
    )


@tool
def get_knowledge_planet_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "local Knowledge Planet look-back window in days"] = 30,
    max_items: Annotated[int, "maximum stream items to return"] = 30,
    max_reports: Annotated[int, "maximum PDF reports to return"] = 12,
) -> str:
    """
    Retrieve locally imported Knowledge Planet topic-text intelligence for a
    ticker. This is alternative intelligence: useful for expectations,
    channel checks, industry data, and sell-side research lenses, but not
    filing-grade proof.
    """
    return route_to_vendor(
        "get_knowledge_planet_context",
        ticker,
        curr_date,
        look_back_days,
        max_items,
        max_reports,
    )


@tool
def get_baijiu_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
) -> str:
    """
    Run a gated baijiu/liquor verification layer for A-share names. It returns
    not_applicable unless the target is a baijiu company, then checks channel
    price, contract-liability seasonality, product mix, cash quality, and
    required peer-basket evidence.
    """
    return route_to_vendor("get_baijiu_context", ticker, curr_date, look_back_days)


@tool
def get_compute_leasing_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    financial_look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
    event_look_back_days: Annotated[int, "announcement look-back window in days"] = 365,
    interaction_look_back_days: Annotated[int, "investor-interaction look-back window in days"] = 365,
    news_look_back_days: Annotated[int, "news look-back window in days"] = 180,
) -> str:
    """
    Run a gated compute-leasing verification layer for A-share names. It returns
    a not_applicable status unless official or semi-official evidence indicates
    a compute-leasing / AI-compute business, avoiding generic AI analysis for
    unrelated stocks.
    """
    return route_to_vendor(
        "get_compute_leasing_context",
        ticker,
        curr_date,
        financial_look_back_days,
        event_look_back_days,
        interaction_look_back_days,
        news_look_back_days,
    )


@tool
def get_dividend_defensive_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_years: Annotated[int, "dividend and financial look-back window in years"] = 6,
    peer_limit: Annotated[int, "maximum peer alternatives to return"] = 10,
) -> str:
    """
    Run a gated defensive-dividend verification layer for A-share names. It
    tests whether dividend yield is supported by stable profits, cash-flow
    coverage, non-declining industry logic, valuation buffer, and better peer
    alternatives.
    """
    return route_to_vendor(
        "get_dividend_defensive_context",
        ticker,
        curr_date,
        look_back_years,
        peer_limit,
    )


@tool
def get_building_materials_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
) -> str:
    """
    Run a gated building-materials verification layer for A-share names. It
    returns not_applicable unless the target is a cement, waterproofing, glass,
    fiberglass, gypsum-board, pipe, coating, ceramic, hardware, or wood-panel
    company, then frames sector-native cycle, price/cost, channel, working
    capital, low-PB, and dividend-trap checks.
    """
    return route_to_vendor("get_building_materials_context", ticker, curr_date, look_back_days)


@tool
def get_biopharma_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
) -> str:
    """
    Run a gated biopharma/pharma-services verification layer for A-share names.
    It returns not_applicable unless the target is an innovative-drug,
    biotech, or pharma-services company, then frames official clinical,
    regulatory, reimbursement, pipeline, commercialization, cash-runway, and
    CRO/CDMO order-cycle checks.
    """
    return route_to_vendor("get_biopharma_context", ticker, curr_date, look_back_days)


@tool
def get_software_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
) -> str:
    """
    Run a gated software/SaaS verification layer for A-share names. It returns
    not_applicable unless the target is a software, SaaS, financial IT,
    cybersecurity, industrial software, AI software, or hardware-plus-service
    company, then frames ARR/ARPU/paid-user/renewal, project-delivery,
    contract-liability, AI-monetization, and peer-model checks.
    """
    return route_to_vendor("get_software_context", ticker, curr_date, look_back_days)


@tool
def get_insurance_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
    peer_limit: Annotated[int, "maximum same-industry insurance peers to return"] = 8,
) -> str:
    """
    Run a gated insurance verification layer for A-share insurers. It returns
    not_applicable unless the target is an insurer, then frames NBV, EV/P-EV,
    channel quality, solvency, investment yield, P&C COR, dividend safety, and
    insurance peer-comparison checks.
    """
    return route_to_vendor("get_insurance_context", ticker, curr_date, look_back_days, peer_limit)


@tool
def get_medical_device_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report look-back window in days"] = 900,
    peer_limit: Annotated[int, "maximum same-industry medical-device peers to return"] = 8,
) -> str:
    """
    Run a gated medical-device verification layer for A-share companies. It
    returns not_applicable unless the target is a medical equipment, IVD,
    reagent/consumables, or high-value device company, then frames installed
    base, tender cadence, VBP, registration, overseas channel, reagent
    pull-through, gross-margin durability, and cash-conversion checks.
    """
    return route_to_vendor("get_medical_device_context", ticker, curr_date, look_back_days, peer_limit)


@tool
def get_metals_mining_context(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    look_back_days: Annotated[int, "financial report and price look-back window in days"] = 900,
    peer_limit: Annotated[int, "maximum same-industry metals/mining peers to return"] = 8,
) -> str:
    """
    Run a gated metals/mining verification layer for A-share companies. It
    returns not_applicable unless the target is a miner, smelter, or metal
    resource company, then frames reserve/grade/equity output, AISC/unit cost,
    commodity-price source chains, hedging, capex, mine NAV/SOTP, and
    cycle-trough valuation checks.
    """
    return route_to_vendor("get_metals_mining_context", ticker, curr_date, look_back_days, peer_limit)
