from pathlib import Path
import re

ROOT = Path(__file__).parents[1] / "androidApp/app/src/main/res"
STRING_RE = re.compile(r'<string name="([^"]+)">(.*?)</string>', re.DOTALL)


def strings(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return {name: value for name, value in STRING_RE.findall(text)}


def test_release_locale_ui_copy_has_no_silent_english_fallback():
    default = strings(ROOT / "values/strings.xml")
    critical = {
        "turn_format", "event_subtitle", "realm_subtitle", "history_subtitle",
        "people_subtitle", "investigation_subtitle", "ending_subtitle",
        "settings_subtitle", "starting_runtime", "journey_safe",
        "journey_continues", "known", "unknown", "thread_title",
        "thread_detail", "journey_ended", "ending_ahead", "ending_state",
        "settings_description", "accessibility_ready", "gold", "trust",
        "security", "power", "your_decision", "available", "selected",
        "resolving", "blocked", "preparing_journey", "offline_journey",
        "presentation_preferences",
    }
    failures = []
    for path in sorted(ROOT.glob("values-*/strings.xml")):
        locale = path.parent.name
        current = strings(path)
        for key in critical:
            if key in default and current.get(key) == default[key]:
                failures.append(f"{locale}:{key}")
    assert not failures, (
        "Silent English/default fallback remains in release UI resources: "
        + ", ".join(failures)
    )
