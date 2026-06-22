"""Shared 5-tier rating vocabulary and a deterministic heuristic parser.

The same five-tier scale (Buy, Overweight, Hold, Underweight, Sell) is used by:
- The Research Manager (investment plan recommendation)
- The Portfolio Manager (final position decision)
- The signal processor (rating extracted for downstream consumers)
- The memory log (rating tag stored alongside each decision entry)

Centralising it here avoids drift between those call sites.
"""

from __future__ import annotations

import re
from typing import Tuple


# Canonical, ordered 5-tier scale (most bullish to most bearish).
RATINGS_5_TIER: Tuple[str, ...] = (
    "Buy", "Overweight", "Hold", "Underweight", "Sell",
)

_RATING_SET = {r.lower() for r in RATINGS_5_TIER}
_CHINESE_RATING_MAP = (
    ("强烈买入", "Buy"),
    ("买入", "Buy"),
    ("超配", "Overweight"),
    ("高配", "Overweight"),
    ("增持", "Overweight"),
    ("持有", "Hold"),
    ("中性", "Hold"),
    ("观望", "Hold"),
    ("低配", "Underweight"),
    ("减持", "Underweight"),
    ("卖出", "Sell"),
    ("回避", "Sell"),
    ("清仓", "Sell"),
)
_CHINESE_LABEL_RE = re.compile(
    r"(?:最终评级|当前评级|投资评级|最终裁决|最终决策|交易决策|评级|推荐|建议)\s*[：:：]?\s*([^\n，,。；;]*)",
    re.IGNORECASE,
)

# Matches "Rating: X" / "rating - X" / "Rating: **X**" — tolerates markdown
# bold wrappers and either a colon or hyphen separator.
_RATING_LABEL_RE = re.compile(r"rating.*?[:\-][\s*]*(\w+)", re.IGNORECASE)


def parse_rating(text: str, default: str = "Hold") -> str:
    """Heuristically extract a 5-tier rating from prose text.

    Two-pass strategy:
    1. Look for an explicit "Rating: X" label (tolerant of markdown bold).
    2. Fall back to the first 5-tier rating word found anywhere in the text.

    Returns a Title-cased rating string, or ``default`` if no rating word appears.
    """
    for line in text.splitlines():
        m = _RATING_LABEL_RE.search(line)
        if m and m.group(1).lower() in _RATING_SET:
            return m.group(1).capitalize()
        chinese_match = _CHINESE_LABEL_RE.search(line)
        if chinese_match:
            label_value = chinese_match.group(1)
            for token, rating in _CHINESE_RATING_MAP:
                if token in label_value:
                    return rating

    for line in text.splitlines():
        for word in line.lower().split():
            clean = word.strip("*:.,")
            if clean in _RATING_SET:
                return clean.capitalize()

    return default
