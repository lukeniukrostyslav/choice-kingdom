from __future__ import annotations

from dataclasses import dataclass

SUPPORTED_LOCALES: tuple[str, ...] = (
    "en", "it", "de", "fr", "es", "pt", "pl", "nl", "sv", "da",
    "no", "fi", "cs", "el", "ro", "hu", "uk", "ru", "ar", "he",
    "hi", "id", "vi", "th", "ja", "ko", "zh-CN", "zh-TW",
)


@dataclass(frozen=True)
class LocaleSpec:
    tag: str
    english_name: str
    rtl: bool = False


LOCALES: tuple[LocaleSpec, ...] = (
    LocaleSpec("en", "English"), LocaleSpec("it", "Italian"),
    LocaleSpec("de", "German"), LocaleSpec("fr", "French"),
    LocaleSpec("es", "Spanish"), LocaleSpec("pt", "Portuguese"),
    LocaleSpec("pl", "Polish"), LocaleSpec("nl", "Dutch"),
    LocaleSpec("sv", "Swedish"), LocaleSpec("da", "Danish"),
    LocaleSpec("no", "Norwegian"), LocaleSpec("fi", "Finnish"),
    LocaleSpec("cs", "Czech"), LocaleSpec("el", "Greek"),
    LocaleSpec("ro", "Romanian"), LocaleSpec("hu", "Hungarian"),
    LocaleSpec("uk", "Ukrainian"), LocaleSpec("ru", "Russian"),
    LocaleSpec("ar", "Arabic", True), LocaleSpec("he", "Hebrew", True),
    LocaleSpec("hi", "Hindi"), LocaleSpec("id", "Indonesian"),
    LocaleSpec("vi", "Vietnamese"), LocaleSpec("th", "Thai"),
    LocaleSpec("ja", "Japanese"), LocaleSpec("ko", "Korean"),
    LocaleSpec("zh-CN", "Simplified Chinese"),
    LocaleSpec("zh-TW", "Traditional Chinese"),
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
