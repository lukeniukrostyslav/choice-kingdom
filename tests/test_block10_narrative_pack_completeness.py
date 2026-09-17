from __future__ import annotations

from pathlib import Path
import json

from runtime.localization import SUPPORTED_LOCALES
from runtime.localization_contract import build_locale_contract
from runtime.narrative_localization_repository import NarrativePackError, load_narrative_localizer


def test_every_declared_locale_has_a_complete_narrative_pack(repo_root: Path):
    contract = build_locale_contract(repo_root)
    required = {
        key
        for event in contract["events"]
        for key in event["keys"]
    }
    failures = []
    for locale in SUPPORTED_LOCALES:
        path = repo_root / "localization" / "narrative" / f"{locale}.json"
        if not path.exists():
            failures.append(f"{locale}:missing-pack")
            continue
        try:
            localizer = load_narrative_localizer(repo_root, locale)
        except NarrativePackError as exc:
            failures.append(f"{locale}:invalid-pack:{exc}")
            continue
        missing = localizer.missing_keys(required, locale)
        fallback = localizer.fallback_keys(required, locale)
        if missing:
            failures.append(f"{locale}:missing={len(missing)}")
        if fallback:
            failures.append(f"{locale}:fallback={len(fallback)}")
        if locale != "en":
            payload_entries = json.loads(path.read_text(encoding="utf-8")).get("entries", {})
            identical = tuple(
                sorted(
                    key for key in required
                    if payload_entries.get(key, {}).get("translation")
                    == payload_entries.get(key, {}).get("fallback")
                )
            )
            if identical:
                failures.append(f"{locale}:identical-to-fallback={len(identical)}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if len(payload.get("entries", {})) != len(required):
            failures.append(f"{locale}:count={len(payload.get('entries', {}))}/{len(required)}")
    assert not failures, "Incomplete narrative localization packs: " + "; ".join(failures)
