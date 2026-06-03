from tradingagents.dataflows.data_coverage import build_data_coverage_context
from tradingagents.dataflows import web_fact_research


def _repo_file(path: str) -> str:
    from pathlib import Path

    return (Path(__file__).resolve().parents[1] / path).read_text(encoding="utf-8")


def test_a_share_precomputed_context_specs_include_shipping():
    source = _repo_file("tradingagents/graph/trading_graph.py")
    assert '"shipping_context", "get_shipping_context"' in source


def test_propagator_carries_shipping_context():
    source = _repo_file("tradingagents/graph/propagation.py")
    assert 'shipping_context: str = ""' in source
    assert '"shipping_context": shipping_context' in source


def test_data_coverage_audits_shipping_cycle():
    audit = build_data_coverage_context(
        {
            "shipping_cycle": (
                "# Shipping cycle context\n\n"
                "| index | value | evidence_status |\n| --- | --- | --- |\n"
                "| BDTI | N/A | Unavailable; do not state freight index level as fact. |\n\n"
                "## Route Coverage And Missing Data\n"
                + "VLCC TD3C/TCE route-level data remains a research gap. " * 12
            ),
        }
    )
    assert "shipping_cycle" in audit
    assert "partial" in audit


def test_shipping_web_fact_queries_use_route_level_terms():
    queries = web_fact_research._fact_queries("601872.SH", "招商轮船", "水运")
    joined = " ".join(queries)

    assert "VLCC" in joined
    assert "TD3C" in joined
    assert "CTFI" in joined
    assert "霍尔木兹" in joined
    assert "产品价格" not in joined
