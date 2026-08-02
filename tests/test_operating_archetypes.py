from tradingagents.dataflows.industry_kpi_research import build_industry_kpi_context
from tradingagents.dataflows.operating_archetypes import (
    detect_operating_archetypes,
    render_operating_archetype_context,
)


def test_consumer_channel_router_uses_business_economics_not_only_industry_label():
    candidates = detect_operating_archetypes(
        "605499.SH",
        "beverage brand with distributors, retail terminals, sell-through and product mix",
    )

    assert candidates[0][0].profile_id == "branded_consumer_channel"
    rendered = render_operating_archetype_context(
        "605499.SH",
        "beverage brand distributor retail terminal sell-through",
    )
    assert "effective outlets x sell-through" in rendered
    assert "competitor promotion response" in rendered


def test_diversified_company_can_receive_multiple_operating_archetypes():
    candidates = detect_operating_archetypes(
        "TEST.SH",
        "subscription cloud software plus project equipment orders, backlog, acceptance and collection",
        limit=3,
    )

    profile_ids = {row.profile_id for row, _score in candidates}
    assert "software_subscription" in profile_ids
    assert "project_order_delivery" in profile_ids


def test_industry_context_embeds_general_router_and_sector_kpis():
    context = build_industry_kpi_context(
        "605499.SH",
        "2026-08-01",
        company_business_model_context=(
            "beverage brand; distributor channel; retail terminal sell-through; product mix"
        ),
    )

    assert "## General Operating-Model Router" in context
    assert "## Required KPI Map" in context
    assert "branded_consumer_channel" in context
