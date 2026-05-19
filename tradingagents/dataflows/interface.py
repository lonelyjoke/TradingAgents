from typing import Annotated

# Import from vendor-specific modules
from .y_finance import (
    get_YFin_data_online,
    get_stock_stats_indicators_window,
    get_fundamentals as get_yfinance_fundamentals,
    get_balance_sheet as get_yfinance_balance_sheet,
    get_cashflow as get_yfinance_cashflow,
    get_income_statement as get_yfinance_income_statement,
    get_insider_transactions as get_yfinance_insider_transactions,
)
from .yfinance_news import get_news_yfinance, get_global_news_yfinance
from .alpha_vantage import (
    get_stock as get_alpha_vantage_stock,
    get_indicator as get_alpha_vantage_indicator,
    get_fundamentals as get_alpha_vantage_fundamentals,
    get_balance_sheet as get_alpha_vantage_balance_sheet,
    get_cashflow as get_alpha_vantage_cashflow,
    get_income_statement as get_alpha_vantage_income_statement,
    get_insider_transactions as get_alpha_vantage_insider_transactions,
    get_news as get_alpha_vantage_news,
    get_global_news as get_alpha_vantage_global_news,
)
from .alpha_vantage_common import AlphaVantageRateLimitError
from .tushare_a_stock import (
    TushareDataError,
    get_balance_sheet as get_tushare_balance_sheet,
    get_cashflow as get_tushare_cashflow,
    get_fundamentals as get_tushare_fundamentals,
    get_indicator as get_tushare_indicator,
    get_income_statement as get_tushare_income_statement,
    get_stock as get_tushare_stock,
    is_a_share_symbol,
)
from .tushare_research import (
    get_company_events as get_tushare_company_events,
    get_market_sector_risk as get_tushare_market_sector_risk,
    get_market_timing_context as get_tushare_market_timing_context,
    get_peer_comparison as get_tushare_peer_comparison,
    get_tushare_global_news,
    get_tushare_news,
    get_valuation_percentiles as get_tushare_valuation_percentiles,
)
from .commodity_research import get_commodity_context as get_tushare_commodity_context
from .shipping_research import get_shipping_context as get_tushare_shipping_context
from .thematic_research import (
    get_thematic_catalyst_context as get_tushare_thematic_catalyst_context,
)
from .filing_research import (
    get_financial_report_intelligence_context as get_tushare_financial_report_intelligence_context,
)
from .supply_chain_research import (
    get_supply_chain_comparison as get_tushare_supply_chain_comparison,
)
from .earnings_modeling import (
    get_earnings_model_context as get_tushare_earnings_model_context,
)
from .expectation_research import (
    get_market_expectation_context as get_tushare_market_expectation_context,
)
from .price_earnings_decomposition import (
    get_price_earnings_decomposition_context as get_tushare_price_earnings_decomposition_context,
)
from .governance_research import (
    get_management_capital_allocation_context as get_tushare_management_capital_allocation_context,
)
from .shareholder_research import (
    get_shareholder_structure_context as get_tushare_shareholder_structure_context,
)
from .investor_interaction_research import (
    get_investor_interaction_context as get_tushare_investor_interaction_context,
)
from .policy_research import (
    get_policy_planning_context as get_tushare_policy_planning_context,
)

# Configuration and routing logic
from .config import get_config

# Tools organized by category
TOOLS_CATEGORIES = {
    "core_stock_apis": {
        "description": "OHLCV stock price data",
        "tools": [
            "get_stock_data"
        ]
    },
    "technical_indicators": {
        "description": "Technical analysis indicators",
        "tools": [
            "get_indicators"
        ]
    },
    "fundamental_data": {
        "description": "Company fundamentals",
        "tools": [
            "get_fundamentals",
            "get_balance_sheet",
            "get_cashflow",
            "get_income_statement",
            "get_commodity_context",
            "get_shipping_context",
            "get_peer_comparison",
            "get_supply_chain_comparison",
            "get_valuation_percentiles",
            "get_market_sector_risk",
            "get_market_timing_context",
            "get_thematic_catalyst_context",
            "get_financial_report_intelligence_context",
            "get_earnings_model_context",
            "get_market_expectation_context",
            "get_price_earnings_decomposition_context",
            "get_management_capital_allocation_context",
            "get_shareholder_structure_context",
            "get_investor_interaction_context",
            "get_policy_planning_context",
        ]
    },
    "news_data": {
        "description": "News and insider data",
        "tools": [
            "get_news",
            "get_global_news",
            "get_company_events",
            "get_insider_transactions",
        ]
    }
}

VENDOR_LIST = [
    "yfinance",
    "alpha_vantage",
    "tushare",
]

# Mapping of methods to their vendor-specific implementations
VENDOR_METHODS = {
    # core_stock_apis
    "get_stock_data": {
        "alpha_vantage": get_alpha_vantage_stock,
        "tushare": get_tushare_stock,
        "yfinance": get_YFin_data_online,
    },
    # technical_indicators
    "get_indicators": {
        "alpha_vantage": get_alpha_vantage_indicator,
        "tushare": get_tushare_indicator,
        "yfinance": get_stock_stats_indicators_window,
    },
    # fundamental_data
    "get_fundamentals": {
        "alpha_vantage": get_alpha_vantage_fundamentals,
        "tushare": get_tushare_fundamentals,
        "yfinance": get_yfinance_fundamentals,
    },
    "get_balance_sheet": {
        "alpha_vantage": get_alpha_vantage_balance_sheet,
        "tushare": get_tushare_balance_sheet,
        "yfinance": get_yfinance_balance_sheet,
    },
    "get_cashflow": {
        "alpha_vantage": get_alpha_vantage_cashflow,
        "tushare": get_tushare_cashflow,
        "yfinance": get_yfinance_cashflow,
    },
    "get_income_statement": {
        "alpha_vantage": get_alpha_vantage_income_statement,
        "tushare": get_tushare_income_statement,
        "yfinance": get_yfinance_income_statement,
    },
    "get_commodity_context": {
        "tushare": get_tushare_commodity_context,
    },
    "get_shipping_context": {
        "tushare": get_tushare_shipping_context,
    },
    "get_peer_comparison": {
        "tushare": get_tushare_peer_comparison,
    },
    "get_supply_chain_comparison": {
        "tushare": get_tushare_supply_chain_comparison,
    },
    "get_valuation_percentiles": {
        "tushare": get_tushare_valuation_percentiles,
    },
    "get_market_sector_risk": {
        "tushare": get_tushare_market_sector_risk,
    },
    "get_market_timing_context": {
        "tushare": get_tushare_market_timing_context,
    },
    "get_thematic_catalyst_context": {
        "tushare": get_tushare_thematic_catalyst_context,
    },
    "get_financial_report_intelligence_context": {
        "tushare": get_tushare_financial_report_intelligence_context,
    },
    "get_earnings_model_context": {
        "tushare": get_tushare_earnings_model_context,
    },
    "get_market_expectation_context": {
        "tushare": get_tushare_market_expectation_context,
    },
    "get_price_earnings_decomposition_context": {
        "tushare": get_tushare_price_earnings_decomposition_context,
    },
    "get_management_capital_allocation_context": {
        "tushare": get_tushare_management_capital_allocation_context,
    },
    "get_shareholder_structure_context": {
        "tushare": get_tushare_shareholder_structure_context,
    },
    "get_investor_interaction_context": {
        "tushare": get_tushare_investor_interaction_context,
    },
    "get_policy_planning_context": {
        "tushare": get_tushare_policy_planning_context,
    },
    # news_data
    "get_news": {
        "alpha_vantage": get_alpha_vantage_news,
        "tushare": get_tushare_news,
        "yfinance": get_news_yfinance,
    },
    "get_global_news": {
        "yfinance": get_global_news_yfinance,
        "tushare": get_tushare_global_news,
        "alpha_vantage": get_alpha_vantage_global_news,
    },
    "get_company_events": {
        "tushare": get_tushare_company_events,
    },
    "get_insider_transactions": {
        "alpha_vantage": get_alpha_vantage_insider_transactions,
        "yfinance": get_yfinance_insider_transactions,
    },
}

def get_category_for_method(method: str) -> str:
    """Get the category that contains the specified method."""
    for category, info in TOOLS_CATEGORIES.items():
        if method in info["tools"]:
            return category
    raise ValueError(f"Method '{method}' not found in any category")

def get_vendor(category: str, method: str = None) -> str:
    """Get the configured vendor for a data category or specific tool method.
    Tool-level configuration takes precedence over category-level.
    """
    config = get_config()

    # Check tool-level configuration first (if method provided)
    if method:
        tool_vendors = config.get("tool_vendors", {})
        if method in tool_vendors:
            return tool_vendors[method]

    # Fall back to category-level configuration
    return config.get("data_vendors", {}).get(category, "default")

def route_to_vendor(method: str, *args, **kwargs):
    """Route method calls to appropriate vendor implementation with fallback support."""
    category = get_category_for_method(method)
    vendor_config = get_vendor(category, method)
    primary_vendors = [v.strip() for v in vendor_config.split(',')]

    if method not in VENDOR_METHODS:
        raise ValueError(f"Method '{method}' not supported")

    # Build fallback chain: primary vendors first, then remaining available vendors
    all_available_vendors = list(VENDOR_METHODS[method].keys())
    fallback_vendors = primary_vendors.copy()

    # A-share tickers are not handled well by the default yfinance path.
    # Prefer Tushare automatically for common exchange-qualified symbols.
    if method in {
        "get_stock_data",
        "get_indicators",
        "get_fundamentals",
        "get_balance_sheet",
        "get_cashflow",
        "get_income_statement",
        "get_commodity_context",
        "get_shipping_context",
        "get_peer_comparison",
        "get_supply_chain_comparison",
        "get_valuation_percentiles",
        "get_market_sector_risk",
        "get_market_timing_context",
        "get_thematic_catalyst_context",
        "get_financial_report_intelligence_context",
        "get_earnings_model_context",
        "get_market_expectation_context",
        "get_price_earnings_decomposition_context",
        "get_management_capital_allocation_context",
        "get_shareholder_structure_context",
        "get_investor_interaction_context",
        "get_policy_planning_context",
        "get_news",
        "get_company_events",
    } and args:
        symbol = str(args[0])
        if is_a_share_symbol(symbol) and "tushare" in all_available_vendors:
            fallback_vendors = ["tushare"] + [
                vendor for vendor in fallback_vendors if vendor != "tushare"
            ]

    for vendor in all_available_vendors:
        if vendor not in fallback_vendors:
            fallback_vendors.append(vendor)

    for vendor in fallback_vendors:
        if vendor not in VENDOR_METHODS[method]:
            continue

        vendor_impl = VENDOR_METHODS[method][vendor]
        impl_func = vendor_impl[0] if isinstance(vendor_impl, list) else vendor_impl

        try:
            return impl_func(*args, **kwargs)
        except AlphaVantageRateLimitError:
            continue  # Only rate limits trigger fallback
        except TushareDataError:
            if vendor == "tushare":
                raise
            continue

    raise RuntimeError(f"No available vendor for '{method}'")
