from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LocaleSpec:
    tag: str
    english_name: str
    rtl: bool = False


# Release v1 core locales. Additional locales can be added in a later
# localization expansion without blocking the first production release.
SUPPORTED_LOCALES: tuple[str, ...] = (
    "en", "ru", "uk", "it", "de", "fr", "es", "pt",
)

LOCALES: tuple[LocaleSpec, ...] = (
    LocaleSpec("en", "English"),
    LocaleSpec("ru", "Russian"),
    LocaleSpec("uk", "Ukrainian"),
    LocaleSpec("it", "Italian"),
    LocaleSpec("de", "German"),
    LocaleSpec("fr", "French"),
    LocaleSpec("es", "Spanish"),
    LocaleSpec("pt", "Portuguese"),
)

FALLBACK_LOCALE = "en"


def normalize_locale(tag: str | None) -> str:
    if not tag:
        return FALLBACK_LOCALE
    normalized = tag.replace("_", "-")
    for spec in LOCALES:
        if normalized.lower() == spec.tag.lower():
            return spec.tag
    language = normalized.split("-", 1)[0].lower()
    for spec in LOCALES:
        if spec.tag.split("-", 1)[0].lower() == language:
            return spec.tag
    return FALLBACK_LOCALE


def supported_locale_tags() -> tuple[str, ...]:
    return tuple(spec.tag for spec in LOCALES)


def is_rtl(tag: str) -> bool:
    normalized = normalize_locale(tag)
    return next(spec for spec in LOCALES if spec.tag == normalized).rtl
