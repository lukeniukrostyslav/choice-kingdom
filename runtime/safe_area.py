from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SafeInsets:
    """Logical safe-zone contract supplied by the platform UI layer."""

    top_dp: int = 0
    end_dp: int = 0
    bottom_dp: int = 0
    start_dp: int = 0


@dataclass(frozen=True)
class SafeContentBounds:
    width_dp: int
    height_dp: int
    insets: SafeInsets

    @property
    def content_width_dp(self) -> int:
        return max(0, self.width_dp - self.insets.start_dp - self.insets.end_dp)

    @property
    def content_height_dp(self) -> int:
        return max(0, self.height_dp - self.insets.top_dp - self.insets.bottom_dp)


def safe_content_bounds(width_dp: int, height_dp: int, insets: SafeInsets) -> SafeContentBounds:
    """Keep interactive content inside system/cutout/gesture safe zones."""
    if width_dp < 0 or height_dp < 0:
        raise ValueError("window dimensions must be non-negative")
    return SafeContentBounds(width_dp, height_dp, insets)
