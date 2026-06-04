from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_a_share_precomputed_context_specs_include_biopharma():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
        encoding="utf-8"
    )

    assert '"biopharma_context",' in source
    assert '"get_biopharma_context",' in source
    assert '"biopharma": biopharma_context' in source


def test_propagator_carries_biopharma_context():
    source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )

    assert 'biopharma_context: str = ""' in source
    assert '"biopharma_context": biopharma_context' in source


def test_biopharma_context_has_coverage_failure_pattern():
    source = (ROOT / "tradingagents" / "dataflows" / "data_coverage.py").read_text(
        encoding="utf-8"
    )

    assert "# biopharma verification context unavailable" in source


def test_a_share_precomputed_context_specs_include_insurance():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
        encoding="utf-8"
    )

    assert '"insurance_context",' in source
    assert '"get_insurance_context",' in source
    assert '"insurance": insurance_context' in source


def test_propagator_carries_insurance_context():
    source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )

    assert 'insurance_context: str = ""' in source
    assert '"insurance_context": insurance_context' in source


def test_insurance_context_has_coverage_failure_pattern():
    source = (ROOT / "tradingagents" / "dataflows" / "data_coverage.py").read_text(
        encoding="utf-8"
    )

    assert "# insurance verification context unavailable" in source


def test_a_share_precomputed_context_specs_include_medical_device():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
        encoding="utf-8"
    )

    assert '"medical_device_context",' in source
    assert '"get_medical_device_context",' in source
    assert '"medical_device": medical_device_context' in source


def test_propagator_carries_medical_device_context():
    source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )

    assert 'medical_device_context: str = ""' in source
    assert '"medical_device_context": medical_device_context' in source


def test_medical_device_context_has_coverage_failure_pattern():
    source = (ROOT / "tradingagents" / "dataflows" / "data_coverage.py").read_text(
        encoding="utf-8"
    )

    assert "# medical-device verification context unavailable" in source


def test_a_share_precomputed_context_specs_include_metals_mining():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
        encoding="utf-8"
    )

    assert '"metals_mining_context",' in source
    assert '"get_metals_mining_context",' in source
    assert '"metals_mining": metals_mining_context' in source


def test_propagator_carries_metals_mining_context():
    source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )

    assert 'metals_mining_context: str = ""' in source
    assert '"metals_mining_context": metals_mining_context' in source


def test_metals_mining_context_has_coverage_failure_pattern():
    source = (ROOT / "tradingagents" / "dataflows" / "data_coverage.py").read_text(
        encoding="utf-8"
    )

    assert "# metals-mining verification context unavailable" in source


def test_a_share_precomputed_context_specs_include_price_move_attribution():
    source = (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
        encoding="utf-8"
    )

    assert '"price_move_attribution_context",' in source
    assert '"get_price_move_attribution_context",' in source
    assert '"price_move_attribution": price_move_attribution_context' in source


def test_propagator_carries_price_move_attribution_context():
    source = (ROOT / "tradingagents" / "graph" / "propagation.py").read_text(
        encoding="utf-8"
    )

    assert 'price_move_attribution_context: str = ""' in source
    assert '"price_move_attribution_context": price_move_attribution_context' in source


def test_price_move_attribution_context_has_coverage_failure_pattern():
    source = (ROOT / "tradingagents" / "dataflows" / "data_coverage.py").read_text(
        encoding="utf-8"
    )

    assert "# price-move attribution context unavailable" in source
