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
