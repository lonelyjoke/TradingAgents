from __future__ import annotations

from typing import Any


BANKING_SYMBOL_HINTS = frozenset(
    {
        "000001.SZ",
        "001227.SZ",
        "002142.SZ",
        "002807.SZ",
        "002839.SZ",
        "002936.SZ",
        "002948.SZ",
        "002958.SZ",
        "002966.SZ",
        "600000.SH",
        "600908.SH",
        "600015.SH",
        "600016.SH",
        "600036.SH",
        "600919.SH",
        "600926.SH",
        "600928.SH",
        "601009.SH",
        "601077.SH",
        "601128.SH",
        "601166.SH",
        "601169.SH",
        "601187.SH",
        "601229.SH",
        "601288.SH",
        "601328.SH",
        "601398.SH",
        "601528.SH",
        "601577.SH",
        "601658.SH",
        "601665.SH",
        "601818.SH",
        "601825.SH",
        "601838.SH",
        "601860.SH",
        "601916.SH",
        "601939.SH",
        "601963.SH",
        "601988.SH",
        "601997.SH",
        "601998.SH",
        "603323.SH",
    }
)

BANKING_NAME_HINTS = {
    "000001.SZ": "\u5e73\u5b89\u94f6\u884c",
    "001227.SZ": "\u5170\u5dde\u94f6\u884c",
    "002142.SZ": "\u5b81\u6ce2\u94f6\u884c",
    "002807.SZ": "\u6c5f\u9634\u94f6\u884c",
    "002839.SZ": "\u5f20\u5bb6\u6e2f\u884c",
    "002936.SZ": "\u90d1\u5dde\u94f6\u884c",
    "002948.SZ": "\u9752\u5c9b\u94f6\u884c",
    "002958.SZ": "\u9752\u519c\u5546\u884c",
    "002966.SZ": "\u82cf\u5dde\u94f6\u884c",
    "600000.SH": "\u6d66\u53d1\u94f6\u884c",
    "600908.SH": "\u65e0\u9521\u94f6\u884c",
    "600015.SH": "\u534e\u590f\u94f6\u884c",
    "600016.SH": "\u6c11\u751f\u94f6\u884c",
    "600036.SH": "\u62db\u5546\u94f6\u884c",
    "600919.SH": "\u6c5f\u82cf\u94f6\u884c",
    "600926.SH": "\u676d\u5dde\u94f6\u884c",
    "600928.SH": "\u897f\u5b89\u94f6\u884c",
    "601009.SH": "\u5357\u4eac\u94f6\u884c",
    "601077.SH": "\u6e1d\u519c\u5546\u884c",
    "601128.SH": "\u5e38\u719f\u94f6\u884c",
    "601166.SH": "\u5174\u4e1a\u94f6\u884c",
    "601169.SH": "\u5317\u4eac\u94f6\u884c",
    "601187.SH": "\u53a6\u95e8\u94f6\u884c",
    "601229.SH": "\u4e0a\u6d77\u94f6\u884c",
    "601288.SH": "\u519c\u4e1a\u94f6\u884c",
    "601328.SH": "\u4ea4\u901a\u94f6\u884c",
    "601398.SH": "\u5de5\u5546\u94f6\u884c",
    "601528.SH": "\u745e\u4e30\u94f6\u884c",
    "601577.SH": "\u957f\u6c99\u94f6\u884c",
    "601665.SH": "\u9f50\u9c81\u94f6\u884c",
    "601658.SH": "\u90ae\u50a8\u94f6\u884c",
    "601818.SH": "\u5149\u5927\u94f6\u884c",
    "601825.SH": "\u6caa\u519c\u5546\u884c",
    "601838.SH": "\u6210\u90fd\u94f6\u884c",
    "601860.SH": "\u7d2b\u91d1\u94f6\u884c",
    "601916.SH": "\u6d59\u5546\u94f6\u884c",
    "601939.SH": "\u5efa\u8bbe\u94f6\u884c",
    "601963.SH": "\u91cd\u5e86\u94f6\u884c",
    "601988.SH": "\u4e2d\u56fd\u94f6\u884c",
    "601997.SH": "\u8d35\u9633\u94f6\u884c",
    "601998.SH": "\u4e2d\u4fe1\u94f6\u884c",
    "603323.SH": "\u82cf\u519c\u94f6\u884c",
}

BANKING_KEYWORDS = (
    "\u94f6\u884c",
    "\u5546\u4e1a\u94f6\u884c",
    "\u80a1\u4efd\u5236\u94f6\u884c",
    "\u57ce\u5546\u884c",
    "\u519c\u5546\u884c",
)


def _safe_get(row: Any, key: str) -> Any:
    if row is None:
        return ""
    if hasattr(row, "get"):
        try:
            return row.get(key, "")
        except Exception:
            return ""
    return ""


def is_banking_entity(
    symbol: str | None = None,
    *,
    basic: Any = None,
    company_name: str | None = None,
    industry: str | None = None,
) -> bool:
    """Return True when the target should use the bank-specific research stack."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in BANKING_SYMBOL_HINTS:
        return True
    text = " ".join(
        str(part or "")
        for part in (
            company_name,
            industry,
            _safe_get(basic, "name"),
            _safe_get(basic, "industry"),
        )
    )
    return any(keyword in text for keyword in BANKING_KEYWORDS)


def banking_profile_hint(symbol: str | None) -> tuple[str, str] | None:
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol not in BANKING_SYMBOL_HINTS:
        return None
    return BANKING_NAME_HINTS.get(normalized_symbol, normalized_symbol), "\u94f6\u884c"
