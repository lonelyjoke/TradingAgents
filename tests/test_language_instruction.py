import sys
import types
from pathlib import Path
import importlib.util

from tradingagents.dataflows.config import set_config


messages = types.ModuleType("langchain_core.messages")
messages.HumanMessage = object
messages.RemoveMessage = object
tools = types.ModuleType("langchain_core.tools")
tools.tool = lambda func=None, *args, **kwargs: func if func is not None else (lambda inner: inner)
langchain_core = types.ModuleType("langchain_core")
langchain_core.__path__ = []
sys.modules.setdefault("langchain_core", langchain_core)
sys.modules.setdefault("langchain_core.messages", messages)
sys.modules.setdefault("langchain_core.tools", tools)


def _stub_module(name, symbols):
    module = types.ModuleType(name)
    for symbol in symbols:
        setattr(module, symbol, lambda *args, **kwargs: None)
    sys.modules.setdefault(name, module)


_stub_module(
    "tradingagents.agents.utils.core_stock_tools",
    ["get_stock_data"],
)
_stub_module(
    "tradingagents.agents.utils.technical_indicators_tools",
    ["get_indicators"],
)
_stub_module(
    "tradingagents.agents.utils.fundamental_data_tools",
    [
        "get_fundamentals",
        "get_balance_sheet",
        "get_cashflow",
        "get_baijiu_context",
        "get_biopharma_context",
        "get_building_materials_context",
        "get_commodity_context",
        "get_consumer_staples_context",
        "get_price_move_attribution_context",
        "get_relative_strength_context",
        "get_compute_leasing_context",
        "get_dividend_defensive_context",
        "get_earnings_model_context",
        "get_financial_report_intelligence_context",
        "get_income_statement",
        "get_insurance_context",
        "get_intraday_behavior_context",
        "get_medical_device_context",
        "get_metals_mining_context",
        "get_optical_module_context",
        "get_investor_interaction_context",
        "get_policy_planning_context",
        "get_web_fact_check_context",
        "get_market_sector_risk",
        "get_market_expectation_context",
        "get_market_timing_context",
        "get_management_capital_allocation_context",
        "get_peer_comparison",
        "get_price_earnings_decomposition_context",
        "get_shareholder_structure_context",
        "get_supply_chain_comparison",
        "get_shipping_context",
        "get_software_context",
        "get_thematic_catalyst_context",
        "get_valuation_percentiles",
    ],
)
_stub_module(
    "tradingagents.agents.utils.news_data_tools",
    ["get_company_events", "get_news", "get_insider_transactions", "get_global_news"],
)

_AGENT_UTILS_PATH = (
    Path(__file__).resolve().parents[1]
    / "tradingagents"
    / "agents"
    / "utils"
    / "agent_utils.py"
)
_SPEC = importlib.util.spec_from_file_location("agent_utils_under_test", _AGENT_UTILS_PATH)
agent_utils_under_test = importlib.util.module_from_spec(_SPEC)
assert _SPEC and _SPEC.loader
_SPEC.loader.exec_module(agent_utils_under_test)
get_language_instruction = agent_utils_under_test.get_language_instruction


def test_chinese_language_instruction_uses_investment_thesis_not_paper():
    set_config({"output_language": "Chinese"})

    instruction = get_language_instruction()

    assert "投资论点" in instruction
    assert "核心投资假设" in instruction
    assert "translate by meaning rather than word-for-word" in instruction
    assert "证伪" in instruction
    assert "已持有者" in instruction
    assert "准备建仓者" in instruction
    assert "胜率/赔率" in instruction
    assert "Do not use `论文`" in instruction


def test_buy_side_instruction_contains_chinese_idiomatic_terms():
    instruction = agent_utils_under_test.get_buy_side_thesis_instruction()

    assert "thesis = 投资论点/核心投资假设/投资主线" in instruction
    assert "not 论文" in instruction
    assert "probability/payoff = 胜率/赔率" in instruction
    assert "expectation gap = 预期差" in instruction


def test_resource_valuation_instruction_prioritizes_forward_or_normalized_pe():
    combined = (
        agent_utils_under_test.get_earnings_model_instruction()
        + agent_utils_under_test.get_market_expectation_instruction()
    )

    assert "PE TTM as the primary valuation anchor" in combined
    assert "forward/normalized earnings scenarios" in combined


def test_metals_mining_instruction_requires_nonferrous_rating_layers():
    instruction = agent_utils_under_test.get_metals_mining_instruction()

    assert "Industry Cycle View" in instruction
    assert "Company Expression View" in instruction
    assert "Valuation/Odds View" in instruction
    assert "Tactical Attribution View" in instruction
    assert "PE-low/PB-high" in instruction
    assert "Underweight/Sell" in instruction
    assert "strongest bull case" in instruction
    assert "AI or robotics demand" in instruction
    assert "sell-side-depth metals memo" in instruction
    assert "commodity-price sensitivity table" in instruction
    assert "dated verification calendar" in instruction
    assert "neutral for direction" in instruction
    assert "perfect scenario priced" in instruction


def test_research_gap_instruction_treats_missing_data_as_directionally_neutral():
    instruction = agent_utils_under_test.get_research_gap_instruction()

    assert "neutral for direction" in instruction
    assert "Underweight/Sell" in instruction
    assert "independent verified evidence" in instruction


def test_english_language_instruction_stays_empty():
    set_config({"output_language": "English"})

    assert get_language_instruction() == ""
