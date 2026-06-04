from tradingagents.dataflows import biopharma_research
from tradingagents.dataflows.biopharma_research import get_biopharma_context


def _empty_reports(*_args, **_kwargs):
    return [], []


def test_biopharma_context_triggers_for_curated_beigene(monkeypatch):
    monkeypatch.setattr(biopharma_research, "_fetch_stock_basic", lambda symbol: None)
    monkeypatch.setattr(biopharma_research, "_load_financial_report_texts", _empty_reports)

    rendered = get_biopharma_context("688235.SH", "2026-06-03")

    assert "Status: triggered" in rendered
    assert "BRUKINSA/zanubrutinib" in rendered
    assert "ClinicalTrials.gov" in rendered
    assert "risk-adjusted NPV" in rendered
    assert "NMPA" in rendered
    assert "FDA" in rendered


def test_biopharma_context_not_applicable_for_unrelated_stock(monkeypatch):
    monkeypatch.setattr(biopharma_research, "_fetch_stock_basic", lambda symbol: None)
    monkeypatch.setattr(biopharma_research, "_load_financial_report_texts", _empty_reports)

    rendered = get_biopharma_context("301396.SZ", "2026-06-03")

    assert "Status: not_applicable" in rendered
    assert "biopharma terms" in rendered


def test_biopharma_context_uses_pharma_services_gate_for_wuxi(monkeypatch):
    monkeypatch.setattr(biopharma_research, "_fetch_stock_basic", lambda symbol: None)
    monkeypatch.setattr(biopharma_research, "_load_financial_report_texts", _empty_reports)

    rendered = get_biopharma_context("603259.SH", "2026-06-03")

    assert "Status: triggered" in rendered
    assert "CRO/CDMO" in rendered
    assert "order backlog" in rendered
    assert "geopolitical" in rendered
    assert "do not value like a drug-owner pipeline" in rendered
