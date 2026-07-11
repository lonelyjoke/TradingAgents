import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_signature(path: Path, func_name: str):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            args = node.args
            positional = [arg.arg for arg in args.posonlyargs + args.args]
            keyword_only = [arg.arg for arg in args.kwonlyargs]
            required_keyword_only = {
                name
                for name, default in zip(keyword_only, args.kw_defaults)
                if default is None
            }
            return set(positional + keyword_only), required_keyword_only, args.kwarg is not None
    raise AssertionError(f"Could not find function {func_name} in {path}")


def test_trading_graph_context_call_signatures_are_in_sync():
    signatures = {
        "_build_precomputed_data_coverage": _load_signature(
            ROOT / "tradingagents" / "graph" / "trading_graph.py",
            "_build_precomputed_data_coverage",
        ),
        "build_forecast_model_context": _load_signature(
            ROOT / "tradingagents" / "dataflows" / "forecast_model_research.py",
            "build_forecast_model_context",
        ),
        "build_quality_audit_context": _load_signature(
            ROOT / "tradingagents" / "dataflows" / "quality_audit_research.py",
            "build_quality_audit_context",
        ),
        "build_thesis_question_context": _load_signature(
            ROOT / "tradingagents" / "dataflows" / "thesis_question_research.py",
            "build_thesis_question_context",
        ),
    }

    allowed, required, has_varkw = _load_signature(
        ROOT / "tradingagents" / "graph" / "propagation.py",
        "create_initial_state",
    )
    signatures["create_initial_state"] = (allowed - {"self"}, required, has_varkw)

    tree = ast.parse(
        (ROOT / "tradingagents" / "graph" / "trading_graph.py").read_text(
            encoding="utf-8"
        )
    )
    errors = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = None
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = node.func.attr
        if name not in signatures:
            continue
        allowed, required_keyword_only, has_varkw = signatures[name]
        provided = {kw.arg for kw in node.keywords if kw.arg is not None}
        if not has_varkw:
            unexpected = provided - allowed
            if unexpected:
                errors.append((node.lineno, name, "unexpected", sorted(unexpected)))
        missing = required_keyword_only - provided
        if missing:
            errors.append((node.lineno, name, "missing", sorted(missing)))

    assert errors == []
