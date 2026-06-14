import pandas as pd


def _telecom_basic(symbol: str) -> pd.Series:
    return pd.Series({"ts_code": symbol, "name": "中国电信", "industry": "电信运营"})


def _telecom_reports(*_args, **_kwargs):
    return [], [
        (
            "年报",
            "公司为电信运营商，披露移动用户、宽带用户、天翼云、AI、医疗政务行业客户、光网和软件平台能力。",
        )
    ]


def test_optical_module_context_not_applicable_for_telecom_operator(monkeypatch):
    import tradingagents.dataflows.optical_module_research as optical_module_research

    monkeypatch.setattr(optical_module_research, "_fetch_stock_basic", _telecom_basic)
    monkeypatch.setattr(optical_module_research, "_load_financial_report_texts", _telecom_reports)

    rendered = optical_module_research.get_optical_module_context("601728.SH", "2026-06-12")

    assert "Status: not_applicable" in rendered


def test_software_context_not_applicable_for_telecom_operator(monkeypatch):
    import tradingagents.dataflows.software_research as software_research

    monkeypatch.setattr(software_research, "_fetch_stock_basic", _telecom_basic)
    monkeypatch.setattr(software_research, "_load_financial_report_texts", _telecom_reports)

    rendered = software_research.get_software_context("601728.SH", "2026-06-12")

    assert "Status: not_applicable" in rendered


def test_medical_device_context_not_applicable_for_telecom_operator(monkeypatch):
    import tradingagents.dataflows.medical_device_research as medical_device_research

    monkeypatch.setattr(medical_device_research, "_fetch_stock_basic", _telecom_basic)
    monkeypatch.setattr(medical_device_research, "_load_financial_report_texts", _telecom_reports)

    rendered = medical_device_research.get_medical_device_context("601728.SH", "2026-06-12")

    assert "Status: not_applicable" in rendered


def test_compute_leasing_context_not_applicable_for_telecom_operator(monkeypatch):
    import tradingagents.dataflows.compute_leasing_research as compute_leasing_research

    monkeypatch.setattr(compute_leasing_research, "_company_profile", lambda symbol: ("中国电信", "电信运营"))

    rendered = compute_leasing_research.get_compute_leasing_context("601728.SH", "2026-06-12")

    assert "Status: not_applicable" in rendered
    assert "telecom operator" in rendered

