"""Shared lightweight industry identity helpers for routing research playbooks."""

from __future__ import annotations


TELECOM_OPERATOR_TERMS = (
    "电信运营",
    "通信运营",
    "运营商",
    "中国电信",
    "中国移动",
    "中国联通",
    "移动通信服务",
    "宽带接入",
    "天翼云",
    "5G",
    "ARPU",
    "telecom operator",
    "telecommunication operator",
)


def is_telecom_operator_text(*parts: object) -> bool:
    """Return True when the text points to a telecom operator business."""
    text = " ".join(str(part or "") for part in parts)
    lower = text.lower()
    return any(term.lower() in lower for term in TELECOM_OPERATOR_TERMS)

