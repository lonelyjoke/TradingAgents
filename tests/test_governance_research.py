import pandas as pd

from tradingagents.dataflows.governance_research import (
    _announcement_category,
)
from tradingagents.dataflows.shareholder_research import (
    _holder_display,
    _holder_concentration,
    _holder_trade_lifecycle,
    _recent_quarter_ends,
    _safe_sort_desc,
)


def test_capital_allocation_announcement_categories():
    assert _announcement_category("关于2025年度利润分配预案的公告") == "dividend"
    assert _announcement_category("关于回购公司股份的进展公告") == "repurchase"
    assert _announcement_category("关于向特定对象发行股票的公告") == "financing"
    assert _announcement_category("关于重大资产重组的提示性公告") == "mna"


def test_recent_quarter_ends_are_stable():
    assert _recent_quarter_ends("2026-05-16", 4) == [
        "20250630",
        "20250930",
        "20251231",
        "20260331",
    ]


def test_holder_concentration_sums_top10_ratio_by_period():
    data = pd.DataFrame(
        [
            {"period": "20251231", "holder_name": "A", "hold_ratio": 20.0},
            {"period": "20251231", "holder_name": "B", "hold_ratio": 10.0},
            {"period": "20250930", "holder_name": "A", "hold_ratio": 18.0},
            {"period": "20250930", "holder_name": "B", "hold_ratio": 9.0},
        ]
    )

    result = _holder_concentration(data)

    assert result.iloc[0]["period"] == "20251231"
    assert result.iloc[0]["top10_hold_ratio_sum"] == 30.0


def test_holder_display_gracefully_handles_missing_period():
    data = pd.DataFrame(
        [
            {"holder_name": "A", "hold_amount": 100, "hold_ratio": 5.0},
            {"holder_name": "B", "hold_amount": 200, "hold_ratio": 8.0},
        ]
    )

    result = _holder_display(data)

    assert list(result["holder_name"]) == ["B", "A"]


def test_holder_concentration_gracefully_handles_missing_period():
    data = pd.DataFrame(
        [
            {"holder_name": "A", "hold_ratio": 5.0},
            {"holder_name": "B", "hold_ratio": 8.0},
        ]
    )

    result = _holder_concentration(data)

    assert list(result.columns) == ["holder_name", "hold_ratio"]
    assert len(result) == 2


def test_safe_sort_desc_returns_unsorted_frame_when_sort_columns_are_missing():
    data = pd.DataFrame(
        [
            {"holder_name": "A", "hold_ratio": 5.0},
            {"holder_name": "B", "hold_ratio": 8.0},
        ]
    )

    result = _safe_sort_desc(data, ["ann_date"])

    assert result.equals(data)



def test_holder_display_keeps_latest_period_only_when_available():
    data = pd.DataFrame(
        [
            {"period": "20250930", "holder_name": "A", "hold_amount": 100, "hold_ratio": 5.0},
            {"period": "20251231", "holder_name": "B", "hold_amount": 200, "hold_ratio": 8.0},
            {"period": "20251231", "holder_name": "C", "hold_amount": 150, "hold_ratio": 6.0},
        ]
    )
    result = _holder_display(data)
    assert set(result["period"]) == {"20251231"}
    assert list(result["holder_name"]) == ["B", "C"]


def test_holder_trade_lifecycle_marks_old_reduction_as_historical_not_live():
    data = pd.DataFrame(
        [
            {
                "holder_name": "Hexie Health",
                "ann_date": "20260407",
                "in_de": "DE",
                "after_ratio": 2.7,
            }
        ]
    )

    result = _holder_trade_lifecycle(data, "2026-05-30")

    assert result.iloc[0]["latest_trade_date"] == "20260407"
    assert result.iloc[0]["lifecycle_read"] == (
        "executed historical reduction; future selling needs separate evidence"
    )
