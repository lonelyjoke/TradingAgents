from tradingagents.dataflows.forecast_model_research import build_forecast_model_context


def test_forecast_model_context_promotes_official_earnings_guidance():
    context = build_forecast_model_context(
        "000933.SZ",
        "2026-07-09",
        company_events_context="\n".join(
            [
                "### Official Earnings Guidance / Performance Preannouncements",
                "#### 20260710 河南神火煤电股份有限公司2026年半年度业绩预告",
                "- 业绩预告期间：2026年1月1日至2026年6月30日",
                "- 归属于上市公司股东的净利润：480,000.00万元，同比增长152.04%",
                "- 基本每股收益：2.169元/股",
            ]
        ),
    )

    assert "Official Earnings Guidance Override" in context
    assert "480,000.00万元" in context
    assert "reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS" in context
