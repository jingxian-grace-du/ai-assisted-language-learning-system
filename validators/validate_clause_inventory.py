#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANCHOR = re.compile(r'<a id="(legacy-p\d{4})"></a>')
CATEGORIES = {
    "heading", "normative-candidate", "operational-guidance-candidate",
    "explanatory-candidate", "example"
}


def fail(message: str) -> None:
    raise SystemExit(f"CLAUSE_INVENTORY_FAIL: {message}")


def main() -> None:
    protocol = (ROOT / "protocol/current/protocol.md").read_text(encoding="utf-8")
    inventory = json.loads(
        (ROOT / "protocol/current/clause-inventory.json").read_text(encoding="utf-8")
    )
    anchors = set(ANCHOR.findall(protocol))
    clauses = inventory.get("clauses", [])
    if not clauses:
        fail("inventory is empty")

    clause_ids = [clause.get("clause_id") for clause in clauses]
    if len(clause_ids) != len(set(clause_ids)):
        fail("duplicate clause IDs")

    inventory_anchors = {clause.get("anchor") for clause in clauses}
    if inventory_anchors != anchors:
        missing = sorted(anchors - inventory_anchors)
        extra = sorted(inventory_anchors - anchors)
        fail(f"anchor mismatch missing={missing[:5]} extra={extra[:5]}")

    for clause in clauses:
        if clause.get("candidate_category") not in CATEGORIES:
            fail(f"invalid category for {clause.get('clause_id')}")
        if clause.get("review_status") not in {"unreviewed", "confirmed", "reclassified"}:
            fail(f"invalid review status for {clause.get('clause_id')}")
        if not str(clause.get("text", "")).strip():
            fail(f"empty clause text for {clause.get('clause_id')}")

    recorded_total = inventory.get("counts", {}).get("total")
    if recorded_total != len(clauses):
        fail(f"recorded total {recorded_total} != actual {len(clauses)}")

    print(f"CLAUSE_INVENTORY_PASS count={len(clauses)} anchors={len(anchors)}")


if __name__ == "__main__":
    main()
