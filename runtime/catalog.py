from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .state import EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST

HEADING_RE = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
CHOICE_PATTERNS = (
    # Canonical legacy form: optional list marker, bold A/B label, closing **.
    re.compile(r"^(?:-\s*)?\*\*([A-Z])\s*[—:]\s*(.+?)\*\*$", re.M),
    # Canonical expansion form: - **A — ...; effects... (no closing ** before effects).
    re.compile(r"^-\s*\*\*([A-Z])\s*[—:]\s*(.+)$", re.M),
    # Canonical bold-label form with explicit colon after the bold text.
    re.compile(r"^(?:-\s*)?\*\*([A-Z])\s*[—:]\s*(.+?)\*\*:\s*(.*)$", re.M),
    # Plain authored list form.
    re.compile(r"^-\s*([A-Z])\s+(.*)$", re.M),
)
DELTA_RE = re.compile(r"([+-]\d+)\s+(gold|trust|security|power|reputation)\b", re.I)
REL_RE = re.compile(r"([+-]\d+)\s+(Mara|Rowan|Seris|Ivo|Amara|Toma)\b", re.I)
TOKEN_RE = re.compile(r"`([^`]+)`")
AFTER_EVENT_RE = re.compile(r"\bafter\s+(E\d{2,3})\b", re.I)
COMPLETED_EVENT_RE = re.compile(r"\b(E\d{2,3})\s+(?:complete|completed|resolved)\b", re.I)
NUMERIC_RE = re.compile(r"\b(gold|trust|security|power|reputation)\s*(<=|>=|<|>)\s*(\d+)\b", re.I)
REL_COND_RE = re.compile(r"\b(Mara|Rowan|Seris|Ivo|Amara|Toma)\s*(<=|>=|<|>)\s*(-?\d+)\b", re.I)

@dataclass(frozen=True)
class Choice:
    choice_id: str
    label: str
    text: str
    body: str
    resource_deltas: dict[str, int]
    relationship_deltas: dict[str, int]
    state_tokens: tuple[str, ...]
    clear_tokens: tuple[str, ...]

@dataclass(frozen=True)
class Event:
    event_id: str
    title: str
    trigger: str
    choices: tuple[Choice, ...]
    source: str

class CatalogError(ValueError):
    pass

class AuthoredCatalog:
    def __init__(self, root: Path, events: dict[str, Event]):
        self.root = root
        self.events = events

    @classmethod
    def from_repository(cls, root: Path) -> "AuthoredCatalog":
        import json
        manifest = json.loads((root / "docs" / "MACHINE_CANONICAL_GRAPH_01.json").read_text(encoding="utf-8"))
        first = int(manifest["scope"]["first_event"])
        last = int(manifest["scope"]["last_event"])
        excluded = set(manifest["scope"].get("excluded_events", [])) | set(EXCLUDED_EVENTS)
        expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded
        events: dict[str, Event] = {}
        for source in manifest["source_of_truth"]["catalog_sources"]:
            path = root / source
            if not path.exists():
                raise CatalogError(f"missing catalog source: {source}")
            text = path.read_text(encoding="utf-8")
            headings = list(HEADING_RE.finditer(text))
            for index, heading in enumerate(headings):
                event_id, title = heading.group(1), heading.group(2).strip()
                if event_id not in expected:
                    if event_id in excluded:
                        continue
                    raise CatalogError(f"event outside frozen scope: {event_id}")
                end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
                parsed = cls._parse_event(event_id, title, text[heading.start():end], source)
                existing = events.get(event_id)
                if existing is not None:
                    if event_id != "E271" or existing != parsed:
                        raise CatalogError(f"conflicting duplicate event block: {event_id}")
                    continue
                events[event_id] = parsed
        missing = expected - set(events)
        if missing:
            raise CatalogError("missing authored events: " + ", ".join(sorted(missing)))
        return cls(root, dict(sorted(events.items(), key=lambda item: int(item[0][1:]))))

    @staticmethod
    def _parse_event(event_id: str, title: str, block: str, source: str) -> Event:
        trigger_match = re.search(r"^\*\*Trigger:\*\* (.+)$", block, re.M)
        trigger = trigger_match.group(1).strip() if trigger_match else ""
        rows = []
        for pattern in CHOICE_PATTERNS:
            rows.extend(pattern.finditer(block))
        rows.sort(key=lambda match: match.start())
        choices: list[Choice] = []
        seen_labels: set[str] = set()
        for index, row in enumerate(rows):
            end = rows[index + 1].start() if index + 1 < len(rows) else len(block)
            body = block[row.start():end]
            label, text = row.group(1), row.group(2).strip()
            if label in seen_labels:
                continue
            seen_labels.add(label)
            resource_deltas = {resource.lower(): int(delta) for delta, resource in DELTA_RE.findall(body)}
            relationship_deltas = {name.lower(): int(delta) for delta, name in REL_RE.findall(body)}
            tokens: list[str] = []
            clears: list[str] = []
            for line in body.splitlines():
                for token in TOKEN_RE.findall(line):
                    low = line.lower()
                    if any(word in low for word in ("clear", "remove", "reset", "invalidate", "revoke", "cancel")):
                        clears.append(token)
                    else:
                        tokens.append(token)
            choices.append(Choice(
                choice_id=f"{event_id}-{label}", label=label, text=text, body=body,
                resource_deltas=resource_deltas, relationship_deltas=relationship_deltas,
                state_tokens=tuple(dict.fromkeys(tokens)), clear_tokens=tuple(dict.fromkeys(clears)),
            ))
        return Event(event_id, title, trigger, tuple(choices), source)

    def get(self, event_id: str) -> Event:
        if event_id in EXCLUDED_EVENTS:
            raise CatalogError(f"excluded event: {event_id}")
        return self.events[event_id]

    def validate(self) -> None:
        expected = {f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)} - set(EXCLUDED_EVENTS)
        if set(self.events) != expected:
            raise CatalogError("runtime catalog scope is not exactly E01-E272 excluding E273-E277")
        for event in self.events.values():
            labels = {choice.label for choice in event.choices}
            if labels and not {"A", "B"}.issubset(labels):
                raise CatalogError(f"incomplete authored choice set in {event.event_id}: {sorted(labels)}")

    def authored_prerequisites(self, event_id: str) -> tuple[str, ...]:
        """Return only event prerequisites explicitly authored in the trigger text."""
        event = self.get(event_id)
        refs = list(AFTER_EVENT_RE.findall(event.trigger)) + list(COMPLETED_EVENT_RE.findall(event.trigger))
        return tuple(dict.fromkeys(ref.upper() for ref in refs))

    def trigger_satisfied(self, event_id: str, state) -> bool:
        event = self.get(event_id)
        if event_id in state.history:
            return False
        trigger = event.trigger
        low = trigger.lower().strip().rstrip(".")
        if not trigger:
            return True
        matched_condition = False
        for name, op, raw in NUMERIC_RE.findall(trigger):
            matched_condition = True
            if not _compare(state.resources[name.lower()], op, int(raw)):
                return False
        for required in self.authored_prerequisites(event_id):
            matched_condition = True
            if required not in state.history:
                return False
        for name, op, raw in REL_COND_RE.findall(trigger):
            matched_condition = True
            if not _compare(state.relationships[name.lower()], op, int(raw)):
                return False
        for token in TOKEN_RE.findall(trigger):
            matched_condition = True
            if token not in state.flags and token not in state.history and token not in state.threads:
                return False
        if "first turn" in low:
            matched_condition = True
            if state.turn != 1:
                return False
        # Canonical derived-predicate binding: E160's authored "severe winter"
        # trigger consumes the current-cycle predicate produced by E29-A/B.
        if low == "severe winter":
            matched_condition = True
            if "pred.winter_severe" not in state.flags and "pred.winter_severe" not in state.history and "pred.winter_severe" not in state.threads:
                return False
        return matched_condition

def _compare(value: int, op: str, target: int) -> bool:
    return {"<": value < target, "<=": value <= target, ">": value > target, ">=": value >= target}[op]
