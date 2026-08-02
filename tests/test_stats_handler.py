from types import SimpleNamespace

from langchain_core.messages import AIMessage

from cli.stats_handler import StatsCallbackHandler


def test_stats_handler_attributes_tokens_and_cache_to_graph_node():
    handler = StatsCallbackHandler()
    run_id = "research-manager-call"
    metadata = {"langgraph_node": "Research Manager"}

    handler.on_chat_model_start(
        {"name": "deepseek"},
        [[]],
        run_id=run_id,
        metadata=metadata,
        invocation_params={"model": "deepseek-v4-pro"},
    )
    response = SimpleNamespace(
        generations=[
            [
                SimpleNamespace(
                    message=AIMessage(
                        content="done",
                        usage_metadata={
                            "input_tokens": 100,
                            "output_tokens": 20,
                            "total_tokens": 120,
                            "input_token_details": {"cache_read": 60},
                        },
                    )
                )
            ]
        ]
    )
    handler.on_llm_end(response, run_id=run_id)

    stats = handler.get_stats()

    assert stats["llm_calls"] == 1
    assert stats["tokens_in"] == 100
    assert stats["uncached_tokens_in"] == 40
    assert stats["cache_hit_ratio"] == 0.6
    assert stats["node_breakdown"]["Research Manager"] == {
        "llm_calls": 1,
        "tool_calls": 0,
        "tokens_in": 100,
        "tokens_out": 20,
        "cached_tokens_in": 60,
        "llm_errors": 0,
    }
    assert stats["model_breakdown"]["deepseek-v4-pro"] == {
        "llm_calls": 1,
        "tokens_in": 100,
        "tokens_out": 20,
        "cached_tokens_in": 60,
        "llm_errors": 0,
    }
    assert stats["estimated_model_costs_cny"]["deepseek-v4-pro"] == 0.000242
    assert stats["estimated_llm_cost_cny"] == 0.0002
    assert stats["cost_estimate_priced_tokens"] == 120


def test_stats_handler_tracks_errors_and_tools_by_node():
    handler = StatsCallbackHandler()
    handler.on_llm_start(
        {"name": "deepseek"},
        ["prompt"],
        run_id="pm-call",
        metadata={"langgraph_node": "Portfolio Manager"},
    )
    handler.on_llm_error(RuntimeError("timeout"), run_id="pm-call")
    handler.on_tool_start(
        {"name": "get_stock_data"},
        "600000",
        metadata={"langgraph_node": "Market Analyst"},
    )

    stats = handler.get_stats()

    assert stats["llm_errors"] == 1
    assert stats["tool_calls"] == 1
    assert stats["node_breakdown"]["Portfolio Manager"]["llm_errors"] == 1
    assert stats["node_breakdown"]["Market Analyst"]["tool_calls"] == 1
