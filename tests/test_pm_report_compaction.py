from tradingagents.dataflows.pm_report_compaction import split_pm_public_report


def test_pm_compaction_preserves_depth_contract_and_moves_duplicate_sections():
    report = """# Portfolio Decision

## PM摘要

This repeats the recommendation and target price.

## Company Disaggregation

Product units, channels and reported disclosure limits are reconciled.

## Autonomous Three-Year Forecast Model

2026E through 2028E revenue, profit, EPS, OCF, capex and FCF.

## 核心投资论点

This repeats the thesis already bridged above.

## Thesis-to-Financial Bridge

Volume x ASP x margin reaches EPS and fair value.

## Moat Evidence Scorecard

Every proven item carries an evidence id.

## Valuation Closure

Probability-weighted per-share value and expected return.

## 催化剂与验证日历

Next-quarter evidence gates.

## Shared Underwriting Model Change Audit

No unsupported assumption changes.

## Handoff Integrity Audit

All model fields preserved.

## 报告质量自检

Internal generation QA details.
"""

    public, appendix, moved = split_pm_public_report(report)

    for heading in (
        "Company Disaggregation",
        "Autonomous Three-Year Forecast Model",
        "Thesis-to-Financial Bridge",
        "Moat Evidence Scorecard",
        "Valuation Closure",
        "Shared Underwriting Model Change Audit",
        "Handoff Integrity Audit",
        "催化剂与验证日历",
    ):
        assert f"## {heading}" in public
    assert "## PM摘要" not in public
    assert "## 核心投资论点" not in public
    assert "## 报告质量自检" not in public
    assert "## PM摘要" in appendix
    assert moved == ["PM摘要", "核心投资论点", "报告质量自检"]
