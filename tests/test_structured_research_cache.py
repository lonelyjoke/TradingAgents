from types import SimpleNamespace

from tradingagents.graph import trading_graph
from tradingagents.graph.trading_graph import TradingAgentsGraph


def _graph(tmp_path):
    graph = object.__new__(TradingAgentsGraph)
    graph.quick_thinking_llm = SimpleNamespace(model_name="quick-model")
    graph.deep_thinking_llm = SimpleNamespace(model_name="deep-model")
    graph.config = {
        "data_cache_dir": str(tmp_path),
        "structured_research_preprocess_enabled": True,
        "structured_research_cache_enabled": True,
        "structured_research_llm_enabled": True,
        "company_underwriting_packet_enabled": True,
        "structured_research_prompt_max_chars": 42000,
        "company_underwriting_prompt_max_chars": 60000,
    }
    return graph


def test_structured_research_cache_reuses_identical_source_payload(monkeypatch, tmp_path):
    calls = []

    def fake_builder(symbol, as_of_date, **kwargs):
        calls.append((symbol, as_of_date, kwargs["contexts"]))
        return {
            "symbol": symbol,
            "as_of_date": as_of_date,
            "preprocessing_mode": "llm_semantic_plus_deterministic_validation",
            "preprocessing_notes": [],
            "underwriting_packet": {"readiness_reasons": []},
        }

    monkeypatch.setattr(trading_graph, "build_structured_research_bundle", fake_builder)
    graph = _graph(tmp_path)
    contexts = {"filing_intelligence": "same filing", "knowledge_planet": "same note"}

    first = graph._build_structured_research_context("300274.SZ", "2026-07-05", contexts)
    second = graph._build_structured_research_context("300274.SZ", "2026-07-05", contexts)

    assert first == second
    assert len(calls) == 1


def test_structured_research_cache_invalidates_when_source_changes(monkeypatch, tmp_path):
    calls = []

    def fake_builder(symbol, as_of_date, **kwargs):
        calls.append(kwargs["contexts"])
        return {
            "symbol": symbol,
            "as_of_date": as_of_date,
            "preprocessing_mode": "llm_semantic_plus_deterministic_validation",
            "preprocessing_notes": [],
            "underwriting_packet": {"readiness_reasons": []},
        }

    monkeypatch.setattr(trading_graph, "build_structured_research_bundle", fake_builder)
    graph = _graph(tmp_path)

    graph._build_structured_research_context(
        "300274.SZ", "2026-07-05", {"filing_intelligence": "version one"}
    )
    graph._build_structured_research_context(
        "300274.SZ", "2026-07-05", {"filing_intelligence": "version two"}
    )

    assert len(calls) == 2


def test_transient_llm_failure_is_not_cacheable():
    assert not TradingAgentsGraph._structured_research_cacheable(
        {
            "preprocessing_notes": ["semantic LLM failed: timeout"],
            "underwriting_packet": {"readiness_reasons": []},
        }
    )
    assert not TradingAgentsGraph._structured_research_cacheable(
        {
            "preprocessing_notes": [],
            "underwriting_packet": {
                "readiness_reasons": [
                    "LLM company underwriting failed; only deterministic skeleton is available."
                ]
            },
        }
    )
