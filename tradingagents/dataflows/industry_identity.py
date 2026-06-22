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


INSURANCE_SYMBOL_HINTS = frozenset(
    {
        "601318.SH",  # Ping An
        "601601.SH",  # CPIC
        "601336.SH",  # New China Life
        "601628.SH",  # China Life
        "601319.SH",  # PICC
    }
)

INSURANCE_TERMS = (
    "\u4fdd\u9669",
    "\u5bff\u9669",
    "\u8d22\u9669",
    "\u4ea7\u9669",
    "\u5065\u5eb7\u9669",
    "\u5185\u542b\u4ef7\u503c",
    "\u65b0\u4e1a\u52a1\u4ef7\u503c",
    "NBV",
    "embedded value",
    "insurance",
    "insurer",
    "solvency",
)


def is_insurance_text(symbol: object = "", *parts: object) -> bool:
    """Return True when the target should use an insurance playbook."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in INSURANCE_SYMBOL_HINTS:
        return True
    text = " ".join(str(part or "") for part in parts)
    lower = text.lower()
    return any(term.lower() in lower for term in INSURANCE_TERMS)


HOG_BREEDING_SYMBOL_HINTS = frozenset(
    {
        "000876.SZ",  # New Hope Liuhe
        "001201.SZ",  # Dongrui Food
        "002100.SZ",  # Tecon Biology
        "002124.SZ",  # Tianbang Food
        "002567.SZ",  # Tangrenshen
        "002714.SZ",  # Muyuan Foods
        "002840.SZ",  # Huatong Meat
        "300498.SZ",  # Wens Foodstuff
        "600975.SH",  # New Wufeng
        "603363.SH",  # Aonong Biology
        "605296.SH",  # Shennong Group
    }
)

HOG_BREEDING_TERMS = (
    "\u751f\u732a",  # live hog
    "\u5546\u54c1\u732a",  # commodity hog
    "\u4ed4\u732a",  # piglet
    "\u79cd\u732a",  # breeding hog
    "\u80fd\u7e41\u6bcd\u732a",  # breeding sow
    "\u6bcd\u732a\u5b58\u680f",  # sow inventory
    "\u732a\u4ef7",  # hog price
    "\u732a\u5468\u671f",  # hog cycle
    "\u51fa\u680f",  # hog output/slaughter
    "\u5c60\u5bb0",  # slaughtering
    "\u517b\u6b96\u5b8c\u5168\u6210\u672c",  # complete breeding cost
    "\u5b8c\u5168\u6210\u672c",  # complete cost
    "\u81ea\u7e41\u81ea\u517b",  # self-breeding/self-raising
    "\u732a\u8089",  # pork
    "\u7267\u539f",  # Muyuan
    "\u6e29\u6c0f",  # Wens
    "\u65b0\u5e0c\u671b",  # New Hope
    "live hog",
    "hog",
    "pig",
    "piglet",
    "sow",
    "breeding sow",
    "slaughter",
    "complete cost",
    "lh futures",
)

HOG_BREEDING_STRONG_TERMS = (
    "\u751f\u732a",
    "\u5546\u54c1\u732a",
    "\u4ed4\u732a",
    "\u79cd\u732a",
    "\u80fd\u7e41\u6bcd\u732a",
    "\u6bcd\u732a\u5b58\u680f",
    "\u732a\u4ef7",
    "\u732a\u5468\u671f",
    "\u81ea\u7e41\u81ea\u517b",
    "\u7267\u539f",
    "\u6e29\u6c0f",
    "\u65b0\u5e0c\u671b",
    "commodity hog",
    "live hog",
    "hog breeding",
    "breeding sow",
    "sow inventory",
    "pork",
    "lh futures",
)


def is_hog_breeding_text(symbol: object = "", *parts: object) -> bool:
    """Return True when the target should use a hog-breeding cycle playbook."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in HOG_BREEDING_SYMBOL_HINTS:
        return True
    text = " ".join(str(part or "") for part in parts)
    lower = text.lower()
    strong_hits = sum(term.lower() in lower for term in HOG_BREEDING_STRONG_TERMS)
    all_hits = sum(term.lower() in lower for term in HOG_BREEDING_TERMS)
    return strong_hits >= 1 and all_hits >= 2


CONSUMER_STAPLES_SYMBOL_HINTS = {
    "000568.SZ": ("baijiu",),  # Luzhou Laojiao
    "000596.SZ": ("baijiu",),  # Gujing Gongjiu
    "000858.SZ": ("baijiu",),  # Wuliangye
    "000895.SZ": ("meat_processing",),
    "002216.SZ": ("frozen_prepared_food",),
    "002557.SZ": ("snack_food",),
    "600519.SH": ("baijiu",),
    "600600.SH": ("beer",),
    "600809.SH": ("baijiu",),
    "600872.SH": ("condiment",),
    "600887.SH": ("dairy",),
    "603288.SH": ("condiment",),
    "603345.SH": ("frozen_prepared_food",),
    "603517.SH": ("snack_food",),
    "605089.SH": ("frozen_prepared_food",),
    "605499.SH": ("functional_beverage", "beverage"),  # Eastroc Beverage
}

CONSUMER_STAPLES_TERMS = (
    "\u98df\u54c1",
    "\u996e\u6599",
    "\u8f6f\u996e\u6599",
    "\u529f\u80fd\u996e\u6599",
    "\u80fd\u91cf\u996e\u6599",
    "\u4e73\u5236\u54c1",
    "\u8c03\u5473\u54c1",
    "\u767d\u9152",
    "\u5564\u9152",
    "\u901f\u51bb",
    "\u9884\u5236\u83dc",
    "\u4f11\u95f2\u98df\u54c1",
    "\u8089\u5236\u54c1",
    "food",
    "beverage",
    "consumer staples",
    "functional beverage",
    "energy drink",
    "dairy",
    "condiment",
    "beer",
    "baijiu",
)

FUNCTIONAL_BEVERAGE_TERMS = (
    "\u4e1c\u9e4f\u996e\u6599",
    "\u4e1c\u9e4f\u7279\u996e",
    "\u529f\u80fd\u996e\u6599",
    "\u80fd\u91cf\u996e\u6599",
    "\u7535\u89e3\u8d28\u6c34",
    "\u679c\u6c41\u8336",
    "\u5927\u5496",
    "\u7119\u597d\u8336",
    "\u94fa\u8d27",
    "\u52a8\u9500",
    "eastroc",
    "functional beverage",
    "energy drink",
)


def consumer_staples_subsector_hints(symbol: object = "", *parts: object) -> tuple[str, ...]:
    """Return consumer-staples subsector hints for routing, or an empty tuple."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in CONSUMER_STAPLES_SYMBOL_HINTS:
        return CONSUMER_STAPLES_SYMBOL_HINTS[normalized_symbol]
    text = " ".join(str(part or "") for part in parts)
    lower = text.lower()
    if any(term.lower() in lower for term in FUNCTIONAL_BEVERAGE_TERMS):
        return ("functional_beverage", "beverage")
    if any(term.lower() in lower for term in CONSUMER_STAPLES_TERMS):
        if any(term.lower() in lower for term in ("\u996e\u6599", "\u8f6f\u996e\u6599", "beverage", "energy drink")):
            return ("beverage",)
        if any(term.lower() in lower for term in ("\u767d\u9152", "baijiu")):
            return ("baijiu",)
        if any(term.lower() in lower for term in ("\u4e73\u5236\u54c1", "dairy")):
            return ("dairy",)
        if any(term.lower() in lower for term in ("\u8c03\u5473", "condiment")):
            return ("condiment",)
        return ("general_consumer_staples",)
    return ()


def is_consumer_staples_text(symbol: object = "", *parts: object) -> bool:
    """Return True when the target should use a food/beverage consumer playbook."""
    return bool(consumer_staples_subsector_hints(symbol, *parts))
