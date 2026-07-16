"""Shared lightweight industry identity helpers for routing research playbooks."""

from __future__ import annotations

import re


TELECOM_OPERATOR_SYMBOL_HINTS = frozenset(
    {
        "600050.SH",  # China Unicom
        "600941.SH",  # China Mobile
        "601728.SH",  # China Telecom
    }
)


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

TELECOM_OPERATOR_STRONG_TERMS = (
    "电信运营",
    "通信运营",
    "运营商",
    "中国电信",
    "中国移动",
    "中国联通",
    "移动通信服务",
    "宽带接入",
    "天翼云",
    "ARPU",
    "telecom operator",
    "telecommunication operator",
)


LITHIUM_BATTERY_SYMBOL_HINTS = frozenset(
    {
        "300750.SZ",  # CATL
        "300014.SZ",  # EVE Energy
        "002074.SZ",  # Gotion High-Tech
        "300438.SZ",  # Great Power
        "688567.SH",  # Farasis Energy
    }
)

LITHIUM_BATTERY_TERMS = (
    "动力电池",
    "储能电池",
    "锂离子电池",
    "电芯",
    "电池系统",
    "power battery",
    "energy-storage battery",
    "battery cell",
    "catl",
    "宁德时代",
)


SEMICONDUCTOR_FOUNDRY_SYMBOL_HINTS = frozenset(
    {
        "688981.SH",  # SMIC A
        "00981.HK",  # SMIC H
        "01347.HK",  # Hua Hong Semiconductor
        "688347.SH",  # Hua Hong Semiconductor A
    }
)

SEMICONDUCTOR_FOUNDRY_TERMS = (
    "\u6676\u5706\u4ee3\u5de5",
    "\u6676\u5706\u5236\u9020",
    "\u96c6\u6210\u7535\u8def\u5236\u9020",
    "\u534a\u5bfc\u4f53\u5236\u9020",
    "\u6676\u5706",
    "\u5236\u7a0b",
    "\u4ea7\u80fd\u5229\u7528\u7387",
    "\u5149\u523b",
    "\u4e2d\u82af\u56fd\u9645",
    "\u534e\u8679\u534a\u5bfc\u4f53",
    "semiconductor foundry",
    "wafer foundry",
    "pure-play foundry",
    "integrated circuit manufacturing",
    "wafer manufacturing",
    "process node",
    "node mix",
    "fab utilization",
    "wafer starts",
    "smic",
)

SEMICONDUCTOR_FOUNDRY_STRONG_TERMS = (
    "\u6676\u5706\u4ee3\u5de5",
    "\u6676\u5706\u5236\u9020",
    "\u96c6\u6210\u7535\u8def\u5236\u9020",
    "\u534a\u5bfc\u4f53\u5236\u9020",
    "\u4e2d\u82af\u56fd\u9645",
    "\u534e\u8679\u534a\u5bfc\u4f53",
    "semiconductor foundry",
    "wafer foundry",
    "pure-play foundry",
    "integrated circuit manufacturing",
    "wafer manufacturing",
    "smic",
)


SEMICONDUCTOR_DESIGN_SYMBOL_HINTS = frozenset(
    {
        "603501.SH",  # Will Semiconductor
        "603986.SH",  # GigaDevice
        "688008.SH",  # Montage Technology
        "688018.SH",  # Espressif
        "688041.SH",  # Hygon Information
        "688099.SH",  # Amlogic
        "688256.SH",  # Cambricon
        "688385.SH",  # Fudan Microelectronics
        "603893.SH",  # Rockchip
        "002049.SZ",  # Unigroup Guoxin
    }
)

SEMICONDUCTOR_DESIGN_TERMS = (
    "\u82af\u7247\u8bbe\u8ba1",
    "\u96c6\u6210\u7535\u8def\u8bbe\u8ba1",
    "\u65e0\u6676\u5706\u5382",
    "\u65e0\u5382\u534a\u5bfc\u4f53",
    "\u82af\u7247",
    "\u5904\u7406\u5668",
    "\u5b58\u50a8\u82af\u7247",
    "\u6a21\u62df\u82af\u7247",
    "\u5c04\u9891\u82af\u7247",
    "\u7535\u6e90\u7ba1\u7406\u82af\u7247",
    "\u82af\u7247\u4ea7\u54c1",
    "\u82af\u7247\u5e73\u53f0",
    "\u6d41\u7247",
    "fabless",
    "chip design",
    "ic design",
    "semiconductor design",
    "processor",
    "gpu",
    "cpu",
    "soc",
    "asic",
    "fpga",
    "mcu",
    "pmic",
    "rf chip",
)

SEMICONDUCTOR_DESIGN_STRONG_TERMS = (
    "\u82af\u7247\u8bbe\u8ba1",
    "\u96c6\u6210\u7535\u8def\u8bbe\u8ba1",
    "\u65e0\u6676\u5706\u5382",
    "\u65e0\u5382\u534a\u5bfc\u4f53",
    "fabless",
    "chip design",
    "ic design",
    "semiconductor design",
)

SEMICONDUCTOR_EQUIPMENT_SYMBOL_HINTS = frozenset(
    {
        "002371.SZ",  # NAURA
        "603690.SH",  # PNCS
        "688012.SH",  # AMEC
        "688037.SH",  # Kingsemi
        "688072.SH",  # Piotech
        "688082.SH",  # ACM Research Shanghai
        "688120.SH",  # Hwatsing
    }
)

SEMICONDUCTOR_EQUIPMENT_TERMS = (
    "\u534a\u5bfc\u4f53\u8bbe\u5907",
    "\u6676\u5706\u5236\u9020\u8bbe\u5907",
    "\u523b\u8680\u8bbe\u5907",
    "\u8584\u819c\u6c89\u79ef",
    "\u6c89\u79ef\u8bbe\u5907",
    "\u6e05\u6d17\u8bbe\u5907",
    "\u6d82\u80f6\u663e\u5f71",
    "\u53bb\u80f6",
    "\u79bb\u5b50\u6ce8\u5165",
    "\u91cf\u6d4b\u8bbe\u5907",
    "\u68c0\u6d4b\u8bbe\u5907",
    "\u5316\u5b66\u673a\u68b0\u62cb\u5149",
    "\u5149\u523b\u673a",
    "\u5149\u523b\u8bbe\u5907",
    "semiconductor equipment",
    "wafer fabrication equipment",
    "wafer fab equipment",
    "etch equipment",
    "deposition equipment",
    "cleaning equipment",
    "cmp equipment",
    "metrology",
    "inspection equipment",
    "lithography equipment",
    "photoresist coating",
)

SEMICONDUCTOR_EQUIPMENT_STRONG_TERMS = (
    "\u534a\u5bfc\u4f53\u8bbe\u5907",
    "\u6676\u5706\u5236\u9020\u8bbe\u5907",
    "\u523b\u8680\u8bbe\u5907",
    "\u6e05\u6d17\u8bbe\u5907",
    "\u91cf\u6d4b\u8bbe\u5907",
    "\u68c0\u6d4b\u8bbe\u5907",
    "semiconductor equipment",
    "wafer fabrication equipment",
    "wafer fab equipment",
)


def is_semiconductor_foundry_text(symbol: object = "", *parts: object) -> bool:
    """Return True for wafer foundries before generic tech/cycle routing."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in SEMICONDUCTOR_FOUNDRY_SYMBOL_HINTS:
        return True
    text = " ".join([str(symbol or ""), *(str(part or "") for part in parts)])
    lower = text.lower()
    if any(term.lower() in lower for term in SEMICONDUCTOR_FOUNDRY_STRONG_TERMS):
        return True
    hits = sum(term.lower() in lower for term in SEMICONDUCTOR_FOUNDRY_TERMS)
    return hits >= 3 and any(
        term in lower
        for term in (
            "\u534a\u5bfc\u4f53",
            "\u6676\u5706",
            "\u96c6\u6210\u7535\u8def",
            "semiconductor",
            "foundry",
            "wafer",
            "fab",
        )
    )


def is_semiconductor_design_text(symbol: object = "", *parts: object) -> bool:
    """Return True for fabless/chip-design companies."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in SEMICONDUCTOR_DESIGN_SYMBOL_HINTS:
        return True
    if (
        normalized_symbol in SEMICONDUCTOR_FOUNDRY_SYMBOL_HINTS
        or normalized_symbol in SEMICONDUCTOR_EQUIPMENT_SYMBOL_HINTS
    ):
        return False
    text = " ".join([str(symbol or ""), *(str(part or "") for part in parts)])
    lower = text.lower()
    if any(term.lower() in lower for term in SEMICONDUCTOR_DESIGN_STRONG_TERMS):
        return True
    hits = sum(term.lower() in lower for term in SEMICONDUCTOR_DESIGN_TERMS)
    return hits >= 3 and any(
        term in lower
        for term in (
            "\u82af\u7247",
            "\u96c6\u6210\u7535\u8def",
            "chip",
            "ic",
            "semiconductor",
            "processor",
        )
    )


def is_semiconductor_equipment_text(symbol: object = "", *parts: object) -> bool:
    """Return True for wafer-fab semiconductor equipment suppliers."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in SEMICONDUCTOR_EQUIPMENT_SYMBOL_HINTS:
        return True
    if normalized_symbol in SEMICONDUCTOR_FOUNDRY_SYMBOL_HINTS:
        return False
    text = " ".join([str(symbol or ""), *(str(part or "") for part in parts)])
    lower = text.lower()
    if any(term.lower() in lower for term in SEMICONDUCTOR_EQUIPMENT_STRONG_TERMS):
        return True
    hits = sum(term.lower() in lower for term in SEMICONDUCTOR_EQUIPMENT_TERMS)
    return hits >= 2 and any(
        term in lower
        for term in (
            "\u8bbe\u5907",
            "\u523b\u8680",
            "\u6c89\u79ef",
            "\u6e05\u6d17",
            "equipment",
            "etch",
            "deposition",
            "metrology",
        )
    )


def is_semiconductor_text(symbol: object = "", *parts: object) -> bool:
    """Return True for the currently supported semiconductor sub-frameworks."""
    return (
        is_semiconductor_foundry_text(symbol, *parts)
        or is_semiconductor_design_text(symbol, *parts)
        or is_semiconductor_equipment_text(symbol, *parts)
    )


CLEAN_ENERGY_POWER_ELECTRONICS_SYMBOL_HINTS = frozenset(
    {
        "300274.SZ",  # Sungrow
    }
)

CLEAN_ENERGY_POWER_ELECTRONICS_TERMS = (
    "光伏逆变器",
    "储能变流器",
    "储能系统集成",
    "储能系统",
    "电力电子",
    "新能源电源",
    "inverter",
    "power conversion system",
    "energy storage system integrator",
)


def is_clean_energy_power_electronics_text(symbol: object = "", *parts: object) -> bool:
    """Identify inverter/PCS/ESS integrators, not battery-cell/material makers."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in CLEAN_ENERGY_POWER_ELECTRONICS_SYMBOL_HINTS:
        return True
    text = " ".join([str(symbol or ""), *(str(part or "") for part in parts)])
    lower = text.lower()
    hits = sum(term.lower() in lower for term in CLEAN_ENERGY_POWER_ELECTRONICS_TERMS)
    return hits >= 2 and any(
        term in lower
        for term in ("光伏逆变器", "储能变流器", "电力电子", "inverter", "power conversion system")
    )


def _standalone_ascii_term(text: str, term: str) -> bool:
    """Match short ASCII identity terms without leaking across numbers/units.

    In particular, ``189.5GWh`` must not be read as evidence that a battery
    company is a 5G telecom operator.
    """
    return bool(
        re.search(
            rf"(?<![A-Za-z0-9.]){re.escape(term)}(?![A-Za-z0-9])",
            text,
            flags=re.IGNORECASE,
        )
    )


def is_telecom_operator_text(symbol: object = "", *parts: object) -> bool:
    """Return True when the text points to a telecom operator business."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in TELECOM_OPERATOR_SYMBOL_HINTS:
        return True
    text = " ".join([str(symbol or ""), *(str(part or "") for part in parts)])
    lower = text.lower()
    if any(term.lower() in lower for term in TELECOM_OPERATOR_STRONG_TERMS):
        return True
    # 5G is useful only as a standalone token and is too weak on its own.
    # Require a second operator-native feature before selecting the playbook.
    return _standalone_ascii_term(text, "5G") and any(
        term in lower for term in ("subscriber", "broadband", "mobile arpu", "cloud revenue")
    )


def is_lithium_battery_text(symbol: object = "", *parts: object) -> bool:
    """Return True for battery-cell/system companies, not incidental demand mentions."""
    normalized_symbol = str(symbol or "").strip().upper()
    if is_clean_energy_power_electronics_text(symbol, *parts):
        return False
    if normalized_symbol in LITHIUM_BATTERY_SYMBOL_HINTS:
        return True
    text = " ".join([str(symbol or ""), *(str(part or "") for part in parts)])
    lower = text.lower()
    hits = sum(term.lower() in lower for term in LITHIUM_BATTERY_TERMS)
    return hits >= 2


def has_lithium_battery_symbol_hint(symbol: object = "") -> bool:
    """Return whether structured symbol identity proves a cell/system maker."""
    return str(symbol or "").strip().upper() in LITHIUM_BATTERY_SYMBOL_HINTS


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

INSURANCE_IDENTITY_TERMS = (
    "保险公司",
    "保险集团",
    "寿险公司",
    "财险公司",
    "再保险公司",
    "综合金融保险集团",
    "integrated insurer",
    "insurance company",
    "insurance group",
    "life insurer",
    "p&c insurer",
)


def is_insurance_text(symbol: object = "", *parts: object) -> bool:
    """Return True when the target should use an insurance playbook."""
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in INSURANCE_SYMBOL_HINTS:
        return True
    text = " ".join(str(part or "") for part in parts)
    lower = text.lower()
    if any(term.lower() in lower for term in INSURANCE_IDENTITY_TERMS):
        return True
    # Generic research documents often mention NBV, solvency, or insurance as
    # examples of *other* industry templates.  One incidental token must not
    # re-route a non-insurer into the insurance model.
    hits = sum(term.lower() in lower for term in INSURANCE_TERMS)
    return hits >= 3 and any(
        term in lower
        for term in ("underwriting", "保费", "保险服务收入", "赔付", "代理人")
    )


AUTOMOTIVE_COMPONENT_SYMBOL_HINTS = frozenset(
    {
        "601689.SH",  # Tuopu Group
        "600660.SH",  # Fuyao Glass
        "600741.SH",  # HASCO
        "002920.SZ",  # Desay SV
    }
)

AUTOMOTIVE_COMPONENT_IDENTITY_TERMS = (
    "汽车零部件",
    "汽车配件",
    "汽车部件",
    "汽配供应商",
    "整车配套供应商",
    "tier 0.5",
    "tier0.5",
    "tier-0.5",
    "tier 1 automotive supplier",
    "automotive component",
    "auto parts supplier",
)

AUTOMOTIVE_COMPONENT_PRODUCT_TERMS = (
    "底盘系统",
    "减震系统",
    "内外饰",
    "热管理系统",
    "空气悬架",
    "线控制动",
    "智能座舱",
    "车身轻量化",
    "汽车电子",
    "执行器",
)


def is_automotive_components_text(symbol: object = "", *parts: object) -> bool:
    """Return True for automotive-component suppliers, not vehicle OEMs.

    The explicit identity layer takes precedence over incidental downstream
    words such as battery, insurance, metals, AI, or robotics that commonly
    occur in diversified supplier filings.
    """
    normalized_symbol = str(symbol or "").strip().upper()
    if normalized_symbol in AUTOMOTIVE_COMPONENT_SYMBOL_HINTS:
        return True
    text = " ".join(str(part or "") for part in parts)
    lower = text.lower()
    if any(term.lower() in lower for term in AUTOMOTIVE_COMPONENT_IDENTITY_TERMS):
        return True
    product_hits = sum(term.lower() in lower for term in AUTOMOTIVE_COMPONENT_PRODUCT_TERMS)
    return product_hits >= 3 and any(
        term in lower
        for term in ("整车厂", "主机厂", "车型", "单车配套", "客户定点", "ppap")
    )


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
