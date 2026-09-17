from runtime.narrative_localization import NarrativeLocalizer, NarrativeText


def test_narrative_localizer_resolves_requested_locale() -> None:
    localizer = NarrativeLocalizer({
        "E01.title": NarrativeText("E01.title", "The Crown", {"it": "La Corona"}),
    })
    assert localizer.resolve("E01.title", "it") == "La Corona"
    assert localizer.resolve("E01.title", "de") == "The Crown"


def test_narrative_localizer_reports_untranslated_fallbacks() -> None:
    localizer = NarrativeLocalizer({
        "E01.title": NarrativeText("E01.title", "The Crown", {"it": "La Corona"}),
    })
    assert localizer.missing_keys({"E01.title"}, "it") == ()
    assert localizer.fallback_keys({"E01.title"}, "de") == ("E01.title",)
