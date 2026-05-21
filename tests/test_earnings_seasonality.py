import pandas as pd

from tradingagents.dataflows.earnings_modeling import _snapshot_from_income_row


def test_q1_snapshot_uses_historical_seasonality_instead_of_simple_times_four():
    income = pd.DataFrame(
        [
            {"end_date": "20260331", "revenue": 100.0, "n_income_attr_p": 10.0},
            {"end_date": "20251231", "revenue": 500.0, "n_income_attr_p": 50.0},
            {"end_date": "20250331", "revenue": 100.0, "n_income_attr_p": 10.0},
            {"end_date": "20241231", "revenue": 400.0, "n_income_attr_p": 40.0},
            {"end_date": "20240331", "revenue": 80.0, "n_income_attr_p": 8.0},
        ]
    )

    snap = _snapshot_from_income_row(income.iloc[0], income)

    assert snap.annualized_net_profit_parent == 40.0
    assert snap.seasonality_adjusted_net_profit_parent == 50.0
    assert "historical median 0331 share" in snap.seasonality_method

