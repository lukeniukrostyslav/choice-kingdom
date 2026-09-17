from runtime.localization import FALLBACK_LOCALE, normalize_locale, supported_locale_tags, is_rtl


def test_block10_declares_at_least_20_release_locales() -> None:
    locales = supported_locale_tags()
    assert len(locales) >= 20
    for required in ("en", "it", "uk", "ru", "ar", "he", "hi", "id", "vi", "th", "ja", "ko", "zh-CN", "zh-TW"):
        assert required in locales


def test_block10_normalizes_region_tags_and_falls_back_to_english() -> None:
    assert normalize_locale("it-IT") == "it"
    assert normalize_locale("zh-CN") == "zh-CN"
    assert normalize_locale("pt-BR") == "pt"
    assert normalize_locale("xx-YY") == FALLBACK_LOCALE


def test_block10_marks_rtl_locales_without_touching_gameplay_data() -> None:
    assert is_rtl("ar")
    assert is_rtl("he")
    assert not is_rtl("en")
