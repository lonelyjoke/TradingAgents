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
