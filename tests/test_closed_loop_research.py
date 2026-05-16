import pandas as pd

from tradingagents.dataflows.earnings_modeling import (
    _annualize_cumulative,
    _build_driver_rows,
    _period_label,
)
from tradingagents.dataflows.expectation_research import (
    _implied_snapshot,
)


def test_earnings_model_annualizes_cumulative_reports():
    assert _period_label("20260331") == "Q1"
    assert _period_label("20260630") == "H1"
    assert _period_label("20260930") == "Q3"
    assert _period_label("20261231") == "FY"
    assert _annualize_cumulative(10.0, "20260331") == 40.0
    assert _annualize_cumulative(10.0, "20260630") == 20.0
    assert round(_annualize_cumulative(12.0, "20260930"), 2) == 16.0
    assert _annualize_cumulative(10.0, "20261231") == 10.0


def test_driver_bridge_surfaces_latest_financial_levers():
    derived = pd.DataFrame(
        [
            {
                "end_date": "20260331",
                "revenue_base": 120.0,
                "reported_gross_margin": 22.0,
                "derived_operating_margin": 10.0,
                "derived_net_margin": 8.0,
                "finance_expense_ratio": 1.0,
                "ocf_to_net_profit": 1.2,
                "receivables_to_revenue": 25.0,
                "inventory_to_revenue": 15.0,
            },
            {
                "end_date": "20251231",
                "revenue_base": 100.0,
                "reported_gross_margin": 20.0,
                "derived_operating_margin": 8.0,
                "derived_net_margin": 6.0,
                "finance_expense_ratio": 1.5,
                "ocf_to_net_profit": 0.9,
                "receivables_to_revenue": 22.0,
                "inventory_to_revenue": 12.0,
            },
        ]
    )

    rows = {row["driver"]: row for row in _build_driver_rows(derived)}

    assert rows["Gross margin"]["change_vs_prior_report"] == "+2.00pp"
    assert rows["Finance-expense ratio"]["change_vs_prior_report"] == "-0.50pp"
    assert rows["Receivables / revenue"]["change_vs_prior_report"] == "+3.00pp"


def test_implied_snapshot_reverse_engineers_market_quote():
    daily_basic = pd.Series(
        {
            "total_mv": 100_000.0,  # 1bn CNY because Tushare uses 10k CNY
            "pe_ttm": 20.0,
            "ps_ttm": 2.0,
        }
    )

    snap = _implied_snapshot(daily_basic)

    assert snap.market_cap_cny == 1_000_000_000.0
    assert snap.implied_ttm_earnings_cny == 50_000_000.0
    assert snap.implied_ttm_sales_cny == 500_000_000.0
