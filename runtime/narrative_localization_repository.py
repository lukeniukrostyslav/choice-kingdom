from __future__ import annotations

import json
from pathlib import Path

from .localization import normalize_locale
from .narrative_localization import NarrativeLocalizer, NarrativeText


class NarrativePackError(ValueError):
    pass


def load_narrative_localizer(root: Path, locale: str) -> NarrativeLocalizer:
    """Load one authored narrative translation pack.

    Translation packs are data-only. Gameplay semantics stay in the canonical
    event catalog and every key is resolved through NarrativeLocalizer so
    missing translations remain observable to QA.
    """
    tag = normalize_locale(locale)
    path = root / "localization" / "narrative" / f"{tag}.json"
    if not path.exists():
        raise NarrativePackError(f"missing narrative translation pack: {path}")

    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "1.0":
        raise NarrativePackError(f"unsupported narrative pack schema: {path}")
    if payload.get("locale") != tag:
        raise NarrativePackError(f"locale mismatch in {path}")

    entries = payload.get("entries")
    if not isinstance(entries, dict):
        raise NarrativePackError(f"entries must be an object in {path}")

    texts: dict[str, NarrativeText] = {}
    for key, entry in entries.items():
        if not isinstance(entry, dict):
            raise NarrativePackError(f"invalid entry {key!r} in {path}")
        fallback = entry.get("fallback")
        translation = entry.get("translation")
        if not isinstance(fallback, str) or not fallback.strip():
            raise NarrativePackError(f"missing fallback for {key!r} in {path}")
        if not isinstance(translation, str) or not translation.strip():
            raise NarrativePackError(f"missing translation for {key!r} in {path}")
        texts[key] = NarrativeText(key, fallback, {tag: translation})

    return NarrativeLocalizer(texts)
