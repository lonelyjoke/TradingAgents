import os
from typing import Annotated

from yfinance.exceptions import YFRateLimitError

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
    looks_like_a_share_query,
    resolve_a_share_symbol,
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
from .web_fact_research import (
    get_web_fact_check_context as get_tushare_web_fact_check_context,
)
from .baijiu_research import get_baijiu_context as get_tushare_baijiu_context
from .compute_leasing_research import (
    get_compute_leasing_context as get_tushare_compute_leasing_context,
)
from .dividend_defensive_research import (
    get_dividend_defensive_context as get_tushare_dividend_defensive_context,
)
from .building_materials_research import (
    get_building_materials_context as get_tushare_building_materials_context,
)
from .biopharma_research import get_biopharma_context as get_tushare_biopharma_context
from .software_research import get_software_context as get_tushare_software_context
from .insurance_research import get_insurance_context as get_tushare_insurance_context
from .medical_device_research import get_medical_device_context as get_tushare_medical_device_context
from .metals_mining_research import get_metals_mining_context as get_tushare_metals_mining_context
from .price_move_attribution_research import get_price_move_attribution_context as get_tushare_price_move_attribution_context

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
            "get_price_move_attribution_context",
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
            "get_web_fact_check_context",
            "get_baijiu_context",
            "get_compute_leasing_context",
            "get_dividend_defensive_context",
            "get_building_materials_context",
            "get_biopharma_context",
            "get_software_context",
            "get_insurance_context",
            "get_medical_device_context",
            "get_metals_mining_context",
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
    "get_price_move_attribution_context": {
        "tushare": get_tushare_price_move_attribution_context,
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
    "get_web_fact_check_context": {
        "tushare": get_tushare_web_fact_check_context,
    },
    "get_baijiu_context": {
        "tushare": get_tushare_baijiu_context,
    },
    "get_compute_leasing_context": {
        "tushare": get_tushare_compute_leasing_context,
    },
    "get_dividend_defensive_context": {
        "tushare": get_tushare_dividend_defensive_context,
    },
    "get_building_materials_context": {
        "tushare": get_tushare_building_materials_context,
    },
    "get_biopharma_context": {
        "tushare": get_tushare_biopharma_context,
    },
    "get_software_context": {
        "tushare": get_tushare_software_context,
    },
    "get_insurance_context": {
        "tushare": get_tushare_insurance_context,
    },
    "get_medical_device_context": {
        "tushare": get_tushare_medical_device_context,
    },
    "get_metals_mining_context": {
        "tushare": get_tushare_metals_mining_context,
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

A_SHARE_TUSHARE_METHODS = {
    "get_stock_data",
    "get_indicators",
    "get_fundamentals",
    "get_balance_sheet",
    "get_cashflow",
    "get_income_statement",
    "get_commodity_context",
    "get_price_move_attribution_context",
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
    "get_web_fact_check_context",
    "get_baijiu_context",
    "get_compute_leasing_context",
    "get_dividend_defensive_context",
    "get_building_materials_context",
    "get_biopharma_context",
    "get_software_context",
    "get_insurance_context",
    "get_medical_device_context",
    "get_metals_mining_context",
    "get_news",
    "get_company_events",
}


def _normalize_a_share_args(method: str, args: tuple, available_vendors: list[str]) -> tuple[tuple, bool]:
    """Normalize the first symbol arg for A-share-capable Tushare tools."""
    if method not in A_SHARE_TUSHARE_METHODS or not args or "tushare" not in available_vendors:
        return args, False

    raw_symbol = str(args[0])
    try:
        resolved_symbol = resolve_a_share_symbol(raw_symbol)
    except TushareDataError:
        if looks_like_a_share_query(raw_symbol):
            raise
        return args, False

    if resolved_symbol:
        return (resolved_symbol, *args[1:]), True

    if looks_like_a_share_query(raw_symbol):
        raise TushareDataError(
            f"Could not resolve A-share symbol/name {raw_symbol!r}. "
            "Use an exchange-qualified Tushare ts_code such as 301396.SZ, "
            "or check TUSHARE_TOKEN/network access for stock_basic."
        )

    return args, False


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


def _default_vendor_for_method(method: str) -> str:
    if "yfinance" in VENDOR_METHODS.get(method, {}):
        return "yfinance"
    if "tushare" in VENDOR_METHODS.get(method, {}):
        return "tushare"
    available = list(VENDOR_METHODS.get(method, {}).keys())
    return available[0] if available else "default"


def _primary_vendors_from_config(vendor_config: str, method: str) -> list[str]:
    vendors = [v.strip() for v in str(vendor_config or "").split(",") if v.strip()]
    expanded: list[str] = []
    for vendor in vendors or ["default"]:
        if vendor == "default":
            vendor = _default_vendor_for_method(method)
        if vendor not in expanded:
            expanded.append(vendor)
    return expanded


def _vendor_is_configured(vendor: str) -> bool:
    if vendor == "alpha_vantage" and not os.getenv("ALPHA_VANTAGE_API_KEY"):
        return False
    return True


def route_to_vendor(method: str, *args, **kwargs):
    """Route method calls to appropriate vendor implementation with fallback support."""
    category = get_category_for_method(method)
    vendor_config = get_vendor(category, method)

    if method not in VENDOR_METHODS:
        raise ValueError(f"Method '{method}' not supported")

    # Build fallback chain: primary vendors first, then remaining available vendors
    all_available_vendors = list(VENDOR_METHODS[method].keys())
    primary_vendors = _primary_vendors_from_config(vendor_config, method)
    fallback_vendors = primary_vendors.copy()

    # A-share symbols and names should stay on Tushare. yfinance often cannot
    # resolve them correctly and may fail the whole run with Yahoo 429s.
    args, force_tushare_for_a_share = _normalize_a_share_args(
        method, args, all_available_vendors
    )
    if force_tushare_for_a_share:
        fallback_vendors = ["tushare"]
    elif args and is_a_share_symbol(str(args[0])) and "tushare" in all_available_vendors:
        fallback_vendors = ["tushare"]

    for vendor in all_available_vendors:
        if force_tushare_for_a_share:
            break
        if vendor not in fallback_vendors:
            fallback_vendors.append(vendor)

    for vendor in fallback_vendors:
        if vendor not in VENDOR_METHODS[method]:
            continue
        if not _vendor_is_configured(vendor):
            continue

        vendor_impl = VENDOR_METHODS[method][vendor]
        impl_func = vendor_impl[0] if isinstance(vendor_impl, list) else vendor_impl

        try:
            return impl_func(*args, **kwargs)
        except AlphaVantageRateLimitError:
            continue  # Only rate limits trigger fallback
        except YFRateLimitError:
            continue  # Yahoo 429s should not abort if another vendor is available
        except ValueError as exc:
            if vendor == "alpha_vantage" and "ALPHA_VANTAGE_API_KEY" in str(exc):
                continue
            raise
        except TushareDataError:
            if vendor == "tushare":
                raise
            continue

    raise RuntimeError(f"No available vendor for '{method}'")
