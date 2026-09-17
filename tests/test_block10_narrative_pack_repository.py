import json

import pytest

from runtime.narrative_localization_repository import (
    NarrativePackError,
    load_narrative_localizer,
)


def test_narrative_pack_rejects_missing_file(repo_root):
    with pytest.raises(NarrativePackError):
        load_narrative_localizer(repo_root, "it")


def test_narrative_pack_rejects_locale_mismatch(tmp_path):
    path = tmp_path / "localization" / "narrative"
    path.mkdir(parents=True)
    (path / "it.json").write_text(json.dumps({
        "schema_version": "1.0",
        "locale": "ru",
        "entries": {
            "E01.title": {
                "fallback": "The First Petition",
                "translation": "La Prima Petizione",
            }
        },
    }), encoding="utf-8")
    with pytest.raises(NarrativePackError):
        load_narrative_localizer(tmp_path, "it")
