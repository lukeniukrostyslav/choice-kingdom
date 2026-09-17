from pathlib import Path
import re

ROOT = Path(__file__).parents[1] / "androidApp/app/src/main/res"
STRING_RE = re.compile(r'<string name="([^"]+)"')


def keys(path: Path) -> set[str]:
    return set(STRING_RE.findall(path.read_text(encoding="utf-8")))


def test_all_declared_locale_resources_have_default_key_coverage() -> None:
    default = keys(ROOT / "values/strings.xml")
    localized = sorted(ROOT.glob("values-*/strings.xml"))
    assert len(localized) == 27
    assert len(default) >= 45
    for path in localized:
        missing = default - keys(path)
        assert not missing, f"{path}: missing {sorted(missing)}"


def test_required_rtl_and_cjk_resource_sets_exist() -> None:
    for qualifier in ("values-ar", "values-he", "values-ja", "values-ko", "values-zh-rCN", "values-zh-rTW"):
        assert (ROOT / qualifier / "strings.xml").is_file()
