#!/usr/bin/env python3
"""Audit authored triggers against the runtime trigger interpreter."""
from __future__ import annotations
import json, re
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from runtime.catalog import EVENT_OR_RE, NUMERIC_RE, REL_COND_RE, TOKEN_RE, AuthoredCatalog
OUT=ROOT/"docs/MACHINE_RUNTIME_TRIGGER_SEMANTICS_AUDIT_01.json"
def classify(trigger:str)->str:
 low=trigger.lower().strip().rstrip(".")
 if not trigger:return "EMPTY"
 if "first turn" in low:return "FIRST_TURN"
 if low=="severe winter":return "SEVERE_WINTER"
 if NUMERIC_RE.search(trigger) or REL_COND_RE.search(trigger) or TOKEN_RE.search(trigger):
  residue=NUMERIC_RE.sub(" ",trigger); residue=REL_COND_RE.sub(" ",residue); residue=TOKEN_RE.sub(" ",residue); residue=EVENT_OR_RE.sub(" ",residue)
  residue=re.sub(r"\b(?:and|or|after|at least|turns?|later|from|through|with|plus)\b"," ",residue,flags=re.I); residue=re.sub(r"[+<>=`'(),.-]"," ",residue)
  return "PARTIAL_PROSE" if re.search(r"[A-Za-z]{3,}",residue) else "CANONICAL_TOKEN_OR_THRESHOLD"
 if EVENT_OR_RE.search(trigger):return "EVENT_REFERENCE"
 return "OPAQUE_PROSE"
def main()->int:
 catalog=AuthoredCatalog.from_repository(ROOT); rows=[{"event":e.event_id,"trigger":e.trigger,"classification":classify(e.trigger)} for e in catalog.events.values()]
 counts={}
 for row in rows: counts[row["classification"]]=counts.get(row["classification"],0)+1
 opaque=[r for r in rows if r["classification"] in {"OPAQUE_PROSE","PARTIAL_PROSE"}]
 report={"schema_version":"1.0","scope":"E01-E272","audit_only":True,"counts":counts,"opaque_or_partial_count":len(opaque),"opaque_or_partial":opaque,"semantic_boundary":"Opaque prose is not converted into runtime truth. Each such trigger requires an authoritative canonical producer/predicate/route contract before engine implementation."}
 OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8"); print(json.dumps({"status":"PASS",**counts,"opaque_or_partial_count":len(opaque)},sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
