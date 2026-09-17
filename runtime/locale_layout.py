from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TextDirection(str, Enum):
    LTR = "ltr"
    RTL = "rtl"


class TextDensity(str, Enum):
    NORMAL = "normal"
    EXPANDED = "expanded"


@dataclass(frozen=True)
class LocaleLayoutPolicy:
    locale: str
    direction: TextDirection
    text_scale: float = 1.0
    density: TextDensity = TextDensity.NORMAL
    allow_wrap: bool = True
    mirror_navigation: bool = False


def locale_layout_policy(
    locale: str,
    *,
    large_text: bool = False,
) -> LocaleLayoutPolicy:
    """Return presentation-only locale constraints; never changes gameplay data."""
    normalized = locale.replace("_", "-").lower()
    rtl = normalized.split("-")[0] in {"ar", "fa", "he", "ur"}
    return LocaleLayoutPolicy(
        locale=locale,
        direction=TextDirection.RTL if rtl else TextDirection.LTR,
        text_scale=1.25 if large_text else 1.0,
        density=TextDensity.EXPANDED if large_text else TextDensity.NORMAL,
        allow_wrap=True,
        mirror_navigation=rtl,
    )
