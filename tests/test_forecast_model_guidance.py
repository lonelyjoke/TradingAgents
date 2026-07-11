from tradingagents.dataflows.forecast_model_research import build_forecast_model_context


def test_forecast_model_context_promotes_official_earnings_guidance():
    context = build_forecast_model_context(
        "000933.SZ",
        "2026-07-09",
        company_events_context="\n".join(
            [
                "### Official Earnings Guidance / Performance Preannouncements",
                "#### 20260710 Shenhuo 2026 half-year performance preview",
                "- Period: 2026H1 cumulative",
                "- Parent net profit: 480,000.00 CNY mn; YoY +52.04%",
                "- EPS: 2.169 CNY/share",
            ]
        ),
    )

    assert "Official Earnings Guidance Override" in context
    assert "480,000.00 CNY mn" in context
    assert "reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS" in context


def test_forecast_model_context_does_not_promote_generic_guidance_rule():
    context = build_forecast_model_context(
        "300750.SZ",
        "2026-07-10",
        company_events_context=(
            "- Analyst rule: official earnings guidance, performance previews and quick "
            "reports are hard public evidence when an actual disclosure exists."
        ),
    )

    assert "Official Earnings Guidance Override" not in context


def test_business_line_agenda_starts_from_financial_report_revenue_mix():
    context = build_forecast_model_context(
        "300750.SZ",
        "2026-07-10",
        structured_research_context={
            "segments": [
                {
                    "segment": "Energy storage battery",
                    "period": "2025A",
                    "revenue_reported_value": 100,
                    "revenue_reported_unit": "CNY bn",
                    "revenue_weight_pct": 12.0,
                    "revenue_growth_pct": 30.0,
                    "gross_margin_pct": 24.0,
                },
                {
                    "segment": "Power battery",
                    "period": "2025A",
                    "revenue_reported_value": 250,
                    "revenue_reported_unit": "CNY bn",
                    "revenue_weight_pct": 72.0,
                    "revenue_growth_pct": 10.0,
                    "gross_margin_pct": 22.0,
                },
            ]
        },
    )

    assert "Business-Line Qualitative And Quantitative Underwriting Agenda" in context
    assert "financial-report revenue composition" in context
    assert "Power battery" in context
    assert "Energy storage battery" in context
    assert context.index("Power battery") < context.index("Energy storage battery")
    assert "Materials / recycling / other" not in context
    assert "Quantitative claims require" in context


def test_forecast_context_requires_sell_side_depth_chain():
    context = build_forecast_model_context(
        "300750.SZ",
        "2026-07-10",
        structured_research_context={
            "segments": [
                {
                    "segment": "Power battery",
                    "period": "2025A",
                    "revenue_reported_value": 250,
                    "revenue_reported_unit": "CNY bn",
                    "revenue_weight_pct": 72.0,
                    "revenue_growth_pct": 10.0,
                    "gross_margin_pct": 22.0,
                }
            ]
        },
    )

    assert "Sell-Side Depth Chain: Revenue Mix To Falsification" in context
    assert "profit-pool priority" in context
    assert "Demand: volume" in context
    assert "Competition: true peers" in context
    assert "market appears to price" in context
    assert "confirm or falsify" in context


def test_forecast_context_exposes_llm_analysis_intervention_map():
    context = build_forecast_model_context(
        "300750.SZ",
        "2026-07-10",
        structured_research_context={
            "underwriting_packet": {
                "llm_analysis_layer": {
                    "business_question_tree": [
                        "Can power battery share stay resilient?"
                    ],
                    "profit_pool_priority": "power battery remains the main profit pool",
                    "competition_and_substitution_analysis": "OEM multi-sourcing is the key substitution risk",
                    "qualitative_to_quantitative_bridge": "shipment data missing; discuss qualitatively",
                    "expectation_gap_analysis": "market prices slower share growth",
                    "red_team_counterarguments": ["customers could self-supply"],
                    "valuation_explanation": "multiple depends on growth durability",
                    "final_editorial_synthesis": "write one clean investor-facing note",
                }
            }
        },
    )

    assert "LLM Analysis Intervention Map" in context
    assert "1. Business question tree" in context
    assert "2. Profit-pool priority" in context
    assert "3. Competition and substitution" in context
    assert "4. Qualitative-to-quantitative bridge" in context
    assert "5. Expectation gap" in context
    assert "6. Red-team counterargument" in context
    assert "7. Valuation explanation" in context
    assert "8. Final editorial synthesis" in context
    assert "Can power battery share stay resilient?" in context
