#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ID_PATTERN = re.compile(r"^EOD-[A-Z]+-[0-9]{3}$")
LEVELS = {"must", "should", "may"}
METHODS = {"deterministic", "semantic", "operational", "human-decision"}
STATUSES = {"baselined", "draft", "deprecated"}


def fail(message: str) -> None:
    raise SystemExit(f"REQUIREMENTS_FAIL: {message}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalogue_path = root / "protocol/current/requirements.json"
    protocol_path = root / "protocol/current/protocol.md"
    catalogue = json.loads(catalogue_path.read_text(encoding="utf-8"))
    protocol = protocol_path.read_text(encoding="utf-8")

    requirements = catalogue.get("requirements")
    if not isinstance(requirements, list) or not requirements:
        fail("requirements must be a non-empty list")

    seen = set()
    for index, requirement in enumerate(requirements):
        rid = requirement.get("id")
        if not isinstance(rid, str) or not ID_PATTERN.fullmatch(rid):
            fail(f"invalid id at index {index}: {rid!r}")
        if rid in seen:
            fail(f"duplicate id: {rid}")
        seen.add(rid)

        if requirement.get("level") not in LEVELS:
            fail(f"invalid level for {rid}")
        if requirement.get("status") not in STATUSES:
            fail(f"invalid status for {rid}")

        statement = requirement.get("statement")
        if not isinstance(statement, str) or len(statement.strip()) < 10:
            fail(f"missing statement for {rid}")

        source = requirement.get("source", {})
        if source.get("protocol_version") != "3.5":
            fail(f"unsupported source version for {rid}")
        paragraphs = source.get("legacy_paragraphs")
        if not isinstance(paragraphs, list) or not paragraphs:
            fail(f"missing legacy paragraph references for {rid}")
        for paragraph in paragraphs:
            if not isinstance(paragraph, int) or paragraph < 1:
                fail(f"invalid legacy paragraph for {rid}: {paragraph!r}")
            if f'id="legacy-p{paragraph:04d}"' not in protocol:
                fail(f"missing protocol anchor for {rid}: legacy-p{paragraph:04d}")

        verification = requirement.get("verification", {})
        if verification.get("method") not in METHODS:
            fail(f"invalid verification method for {rid}")
        if not str(verification.get("evidence", "")).strip():
            fail(f"missing verification evidence for {rid}")

    print(f"REQUIREMENTS_PASS count={len(requirements)} unique_ids={len(seen)}")


if __name__ == "__main__":
    main()
