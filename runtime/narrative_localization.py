from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .localization import FALLBACK_LOCALE, normalize_locale


@dataclass(frozen=True)
class NarrativeText:
    """One authored narrative string with an explicit locale fallback."""

    key: str
    fallback: str
    translations: Mapping[str, str]

    def resolve(self, locale: str | None) -> str:
        tag = normalize_locale(locale)
        value = self.translations.get(tag)
        if value:
            return value
        return self.fallback


class NarrativeLocalizer:
    """Resolve authored E01-E272 narrative text without changing game rules.

    The catalog remains the source of gameplay semantics. This layer only maps
    presentation text to locale-specific strings and makes fallback observable
    to QA instead of silently pretending English is translated content.
    """

    def __init__(self, texts: Mapping[str, NarrativeText]):
        self._texts = dict(texts)

    def resolve(self, key: str, locale: str | None = None) -> str:
        return self._texts[key].resolve(locale)

    def missing_keys(self, required_keys: set[str], locale: str) -> tuple[str, ...]:
        tag = normalize_locale(locale)
        return tuple(sorted(
            key for key in required_keys
            if key not in self._texts or not self._texts[key].translations.get(tag)
        ))

    def fallback_keys(self, required_keys: set[str], locale: str) -> tuple[str, ...]:
        tag = normalize_locale(locale)
        return tuple(sorted(
            key for key in required_keys
            if key in self._texts and not self._texts[key].translations.get(tag)
        ))

    def keys(self) -> tuple[str, ...]:
        return tuple(sorted(self._texts))
