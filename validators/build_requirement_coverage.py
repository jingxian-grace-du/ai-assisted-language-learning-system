#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    inventory_path = ROOT / "protocol/current/clause-inventory.json"
    requirements_path = ROOT / "protocol/current/requirements.json"
    overrides_path = ROOT / "protocol/current/clause-review-overrides.json"
    output_path = ROOT / "protocol/current/requirement-coverage.json"

    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    catalogue = json.loads(requirements_path.read_text(encoding="utf-8"))
    overrides = json.loads(overrides_path.read_text(encoding="utf-8"))
    operational_profile = set(overrides["operational_profile"])
    non_normative_context = set(overrides["non_normative_context"])
    reviewed_mappings = {
        int(paragraph): requirement_ids
        for paragraph, requirement_ids in overrides["requirement_mappings"].items()
    }

    by_paragraph: dict[int, list[str]] = {}
    for requirement in catalogue["requirements"]:
        for paragraph in requirement["source"]["legacy_paragraphs"]:
            by_paragraph.setdefault(paragraph, []).append(requirement["id"])

    dispositions = []
    counts: dict[str, int] = {}
    for clause in inventory["clauses"]:
        paragraph = clause["legacy_paragraph"]
        linked = sorted(set(by_paragraph.get(paragraph, [])) | set(reviewed_mappings.get(paragraph, [])))
        category = clause["candidate_category"]
        if linked:
            disposition = "mapped-to-baselined-requirement"
        elif paragraph in operational_profile:
            disposition = "reviewed-operational-profile"
        elif paragraph in non_normative_context:
            disposition = "reviewed-non-normative-context"
        elif category == "normative-candidate":
            disposition = "normative-review-backlog"
        elif category == "operational-guidance-candidate":
            disposition = "operational-review-backlog"
        else:
            disposition = "non-normative-retained-context"
        counts[disposition] = counts.get(disposition, 0) + 1
        dispositions.append(
            {
                "clause_id": clause["clause_id"],
                "legacy_paragraph": paragraph,
                "candidate_category": category,
                "disposition": disposition,
                "requirement_ids": linked,
            }
        )

    result = {
        "coverage_version": "0.1.0",
        "protocol_baseline": inventory["protocol_baseline"],
        "catalogue_version": catalogue["catalogue_version"],
        "counts": {"total": len(dispositions), **dict(sorted(counts.items()))},
        "clauses": dispositions,
    }
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("REQUIREMENT_COVERAGE_BUILT", json.dumps(result["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
