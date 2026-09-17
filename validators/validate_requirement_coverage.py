#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"REQUIREMENT_COVERAGE_FAIL: {message}")


def main() -> None:
    inventory = json.loads(
        (ROOT / "protocol/current/clause-inventory.json").read_text(encoding="utf-8")
    )
    catalogue = json.loads(
        (ROOT / "protocol/current/requirements.json").read_text(encoding="utf-8")
    )
    overrides = json.loads(
        (ROOT / "protocol/current/clause-review-overrides.json").read_text(encoding="utf-8")
    )
    coverage = json.loads(
        (ROOT / "protocol/current/requirement-coverage.json").read_text(encoding="utf-8")
    )

    inventory_ids = {item["clause_id"] for item in inventory["clauses"]}
    coverage_ids = [item["clause_id"] for item in coverage["clauses"]]
    if len(coverage_ids) != len(set(coverage_ids)):
        fail("duplicate clause coverage records")
    if set(coverage_ids) != inventory_ids:
        fail("coverage does not match complete clause inventory")

    requirement_ids = {item["id"] for item in catalogue["requirements"]}
    override_paragraphs = (
        set(overrides["operational_profile"])
        | set(overrides["non_normative_context"])
        | {int(value) for value in overrides["requirement_mappings"]}
    )
    if len(override_paragraphs) != (
        len(overrides["operational_profile"])
        + len(overrides["non_normative_context"])
        + len(overrides["requirement_mappings"])
    ):
        fail("a clause appears in more than one review override disposition")
    unknown_override_ids = {
        requirement_id
        for values in overrides["requirement_mappings"].values()
        for requirement_id in values
        if requirement_id not in requirement_ids
    }
    if unknown_override_ids:
        fail(f"unknown requirement IDs in review overrides: {sorted(unknown_override_ids)}")
    linked_ids = {
        requirement_id
        for item in coverage["clauses"]
        for requirement_id in item["requirement_ids"]
    }
    if not requirement_ids.issubset(linked_ids):
        fail(f"unlinked requirements: {sorted(requirement_ids - linked_ids)}")

    actual_counts: dict[str, int] = {}
    for item in coverage["clauses"]:
        disposition = item["disposition"]
        actual_counts[disposition] = actual_counts.get(disposition, 0) + 1
    if coverage["counts"].get("total") != len(coverage["clauses"]):
        fail("incorrect total")
    for key, value in actual_counts.items():
        if coverage["counts"].get(key) != value:
            fail(f"incorrect count for {key}")

    print(
        "REQUIREMENT_COVERAGE_PASS",
        f"clauses={len(coverage_ids)}",
        f"requirements={len(requirement_ids)}",
        f"normative_backlog={actual_counts.get('normative-review-backlog', 0)}",
        f"operational_backlog={actual_counts.get('operational-review-backlog', 0)}",
    )


if __name__ == "__main__":
    main()
