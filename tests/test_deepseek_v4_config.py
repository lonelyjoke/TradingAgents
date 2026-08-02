from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.llm_clients.model_catalog import get_model_options


def _graph_with_config(**overrides):
    graph = object.__new__(TradingAgentsGraph)
    graph.config = {
        "llm_provider": "deepseek",
        "llm_timeout": None,
        "llm_max_retries": None,
        "llm_proxy": None,
        "deepseek_quick_thinking": "enabled",
        "deepseek_quick_reasoning_effort": "high",
        "deepseek_deep_thinking": "enabled",
        "deepseek_deep_reasoning_effort": "max",
        **overrides,
    }
    return graph


def test_deepseek_v4_uses_role_specific_thinking_effort():
    graph = _graph_with_config()

    quick = graph._get_provider_kwargs("quick")
    deep = graph._get_provider_kwargs("deep")

    assert quick["extra_body"] == {"thinking": {"type": "enabled"}}
    assert quick["reasoning_effort"] == "high"
    assert deep["extra_body"] == {"thinking": {"type": "enabled"}}
    assert deep["reasoning_effort"] == "max"


def test_deepseek_disabled_thinking_omits_reasoning_effort():
    graph = _graph_with_config(deepseek_quick_thinking="disabled")

    quick = graph._get_provider_kwargs("quick")

    assert quick["extra_body"] == {"thinking": {"type": "disabled"}}
    assert "reasoning_effort" not in quick


def test_deepseek_catalog_contains_only_current_v4_models():
    quick_ids = [model_id for _label, model_id in get_model_options("deepseek", "quick")]
    deep_ids = [model_id for _label, model_id in get_model_options("deepseek", "deep")]

    assert "deepseek-v4-flash" in quick_ids
    assert "deepseek-v4-pro" in deep_ids
    assert "deepseek-chat" not in quick_ids + deep_ids
    assert "deepseek-reasoner" not in quick_ids + deep_ids
