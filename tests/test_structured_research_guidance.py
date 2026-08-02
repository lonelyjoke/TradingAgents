from tradingagents.dataflows.structured_research import (
    SemanticConflict,
    _apply_official_guidance_control,
)


def test_deterministic_guidance_rejects_semantic_prior_period_column_shift():
    metrics = [
        {
            "segment": "consolidated",
            "variable": "net_profit_parent",
            "value": 1_904_456_800.0,
            "value_text": "190,445.68 (万元)",
            "unit": "CNY",
            "period": "2026H1 forecast",
            "comparison_basis": "同比上升",
            "source_module": "company_events",
            "source_quote": "归属于上市公司股东的净利润 190,445.68",
            "evidence_status": "reported",
            "model_role": "earnings guidance",
            "control_flags": [],
        }
    ]
    conflicts = [
        SemanticConflict(
            topic="H1 2026 net profit forecast vs Q1 reported net profit",
            claim_a="Q1 2026 parent profit is 2289.7 CNY mn",
            source_a="earnings_model",
            claim_b="H1 preview is 1904.5 CNY mn",
            source_b="company_events",
            conflict_type="inconsistency",
            required_resolution="check the report",
        )
    ]
    contexts = {
        "company_events": (
            "2026年半年度业绩预告\n"
            "Parsed official guidance metrics: period=2026H1; "
            "parent_net_profit_cny_mn=4800; "
            "parent_net_profit_prior_cny_mn=1904.4568; unit=CNY mn"
        )
    }
    errors: list[str] = []

    controlled, retained_conflicts = _apply_official_guidance_control(
        metrics, conflicts, contexts, errors
    )

    rejected = controlled[0]
    canonical = next(
        row
        for row in controlled
        if "official_current_period_source_of_truth" in row["control_flags"]
    )
    assert rejected["value"] is None
    assert rejected["evidence_status"] == "unverified"
    assert "matched_official_prior_period_value" in rejected["control_flags"]
    assert canonical["value"] == 4800.0
    assert canonical["period"] == "2026H1"
    assert retained_conflicts == []
    assert any("rejected 2026H1" in error for error in errors)
    assert any("resolved semantic guidance conflict" in error for error in errors)


def test_broad_peer_news_is_not_reparsed_as_target_official_guidance():
    metrics = [
        {
            "segment": "consolidated",
            "variable": "net_profit_parent",
            "value": 1_680.0,
            "value_text": "1680 CNY mn",
            "unit": "CNY mn",
            "period": "2026E",
            "source_module": "earnings_model",
            "evidence_status": "estimated",
            "model_role": "forecast",
            "control_flags": [],
        }
    ]
    contexts = {
        "company_events": (
            "# Tushare A-share event research for 603345.SH\n"
            "- Company: 安井食品\n"
            "## Company And Industry News\n"
            "洽洽食品2026年半年度业绩预告：预计归母净利润为90,000万元。"
        )
    }
    errors: list[str] = []

    controlled, retained_conflicts = _apply_official_guidance_control(
        metrics,
        [],
        contexts,
        errors,
    )

    assert controlled == metrics
    assert retained_conflicts == []
    assert errors == []
    assert not any(
        "official_current_period_source_of_truth" in row.get("control_flags", [])
        for row in controlled
    )
