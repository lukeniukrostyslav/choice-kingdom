from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

from runtime.catalog import AuthoredCatalog
from runtime.localization import SUPPORTED_LOCALES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "localization" / "narrative"
TARGETS = tuple(locale for locale in SUPPORTED_LOCALES if locale != "en")
TOKEN_RE = re.compile(r"(E\d{2,3}|\x60[^\x60]+\x60)")


def protect(text: str) -> tuple[str, list[str]]:
    tokens: list[str] = []

    def repl(match: re.Match[str]) -> str:
        token = f"__CKTOKEN_{len(tokens)}__"
        tokens.append(match.group(0))
        return token

    return TOKEN_RE.sub(repl, text), tokens


def restore(text: str, tokens: list[str]) -> str:
    for index, token in enumerate(tokens):
        text = text.replace(f"__CKTOKEN_{index}__", token)
    return text


def build_source(root: Path) -> dict[str, str]:
    catalog = AuthoredCatalog.from_repository(root)
    result: dict[str, str] = {}
    for event in catalog.events.values():
        result[f"{event.event_id}.title"] = event.title
        result[f"{event.event_id}.trigger"] = event.trigger
        for choice in event.choices:
            result[f"{choice.choice_id}.text"] = choice.text
    return result


def translate_batch(translator: GoogleTranslator, texts: list[str]) -> list[str]:
    protected: list[list[str]] = []
    prepared: list[str] = []
    for text in texts:
        value, tokens = protect(text)
        prepared.append(value)
        protected.append(tokens)

    for attempt in range(5):
        try:
            translated = translator.translate_batch(prepared)
            if len(translated) == len(prepared):
                return [
                    restore(str(value), tokens)
                    for value, tokens in zip(translated, protected, strict=True)
                ]
        except Exception:
            pass
        time.sleep(2 ** attempt)

    output: list[str] = []
    for value, tokens in zip(prepared, protected, strict=True):
        for attempt in range(5):
            try:
                output.append(restore(translator.translate(value), tokens))
                break
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(2 ** attempt)
        time.sleep(0.35)
    return output


def _load_partial(path: Path, source: dict[str, str]) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        entries = payload.get("entries", {})
        if not isinstance(entries, dict):
            return {}
        return {
            key: str(entry["translation"]).strip()
            for key, entry in entries.items()
            if key in source
            and isinstance(entry, dict)
            and isinstance(entry.get("translation"), str)
            and entry["translation"].strip()
        }
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        return {}


def _write_partial(path: Path, locale: str, source: dict[str, str], translations: dict[str, str]) -> None:
    payload = {
        "schema_version": "1.0-partial",
        "locale": locale,
        "source_locale": "en",
        "translation_provider": "Google Translate via deep-translator",
        "machine_translated": True,
        "entries": {
            key: {"fallback": source[key], "translation": translations[key]}
            for key in source
            if key in translations
        },
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_pack(locale: str, source: dict[str, str]) -> None:
    path = OUT / f"{locale}.json"
    partial = OUT / f".{locale}.json.partial"
    keys = list(source)
    translations = _load_partial(partial, source)

    if path.exists():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            entries = payload.get("entries", {})
            if set(entries) == set(keys):
                print(f"{locale}: already complete")
                return
        except (OSError, json.JSONDecodeError, TypeError):
            pass

    translator = GoogleTranslator(source="en", target=locale)
    for start in range(0, len(keys), 25):
        batch_keys = keys[start:start + 25]
        pending = [key for key in batch_keys if key not in translations]
        if pending:
            values = translate_batch(translator, [source[key] for key in pending])
            for key, value in zip(pending, values, strict=True):
                if not value.strip():
                    raise RuntimeError(f"empty translation: {locale}:{key}")
                translations[key] = value.strip()
            _write_partial(partial, locale, source, translations)
        print(f"{locale}: {len(translations)}/{len(keys)}")

    if set(translations) != set(keys):
        raise RuntimeError(f"incomplete translation pack: {locale}")

    payload = {
        "schema_version": "1.0",
        "locale": locale,
        "source_locale": "en",
        "translation_provider": "Google Translate via deep-translator",
        "machine_translated": True,
        "entries": {
            key: {"fallback": source[key], "translation": translations[key]}
            for key in keys
        },
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    partial.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=TARGETS)
    args = parser.parse_args()

    source = build_source(ROOT)
    if len(source) != 1064:
        raise RuntimeError(f"unexpected source key count: {len(source)}")
    OUT.mkdir(parents=True, exist_ok=True)

    en_payload = {
        "schema_version": "1.0",
        "locale": "en",
        "source_locale": "en",
        "translation_provider": "canonical source",
        "machine_translated": False,
        "entries": {
            key: {"fallback": value, "translation": value}
            for key, value in source.items()
        },
    }
    (OUT / "en.json").write_text(
        json.dumps(en_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    locales = (args.locale,) if args.locale else TARGETS
    for locale in locales:
        write_pack(locale, source)


if __name__ == "__main__":
    main()
