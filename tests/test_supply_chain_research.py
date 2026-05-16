import pandas as pd

from tradingagents.dataflows.supply_chain_research import (
    _find_supply_chain,
    _summarize_segments,
)


def test_supply_chain_lookup_finds_supported_maps():
    assert _find_supply_chain("300750.SZ").key == "lithium_battery_chain"
    assert _find_supply_chain("002202.SZ").key == "wind_power_chain"
    assert _find_supply_chain("600519.SH") is None


def test_segment_summary_ranks_stronger_profit_pool_first():
    scored = pd.DataFrame(
        [
            {
                "segment": "Upstream resources",
                "name": "A",
                "ts_code": "000001.SZ",
                "v4_score": 90,
                "pe_ttm": 10,
                "pb": 1.5,
                "roe": 18,
                "netprofit_yoy": 25,
            },
            {
                "segment": "Upstream resources",
                "name": "B",
                "ts_code": "000002.SZ",
                "v4_score": 80,
                "pe_ttm": 12,
                "pb": 1.8,
                "roe": 16,
                "netprofit_yoy": 20,
            },
            {
                "segment": "Downstream cells",
                "name": "C",
                "ts_code": "000003.SZ",
                "v4_score": 60,
                "pe_ttm": 20,
                "pb": 3.0,
                "roe": 10,
                "netprofit_yoy": 8,
            },
        ]
    )

    summary = _summarize_segments(scored)

    assert summary.iloc[0]["segment"] == "Upstream resources"
    assert summary.iloc[0]["median_v4_score"] == 85.0
    assert summary.iloc[0]["leader"] == "A (000001.SZ)"
