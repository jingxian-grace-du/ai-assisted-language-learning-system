#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
LOCAL_REF = re.compile(r'"\$ref"\s*:\s*"([^"#]+\.json)(?:#[^"]*)?"')


def fail(message: str) -> None:
    raise SystemExit(f"SCHEMA_FAIL: {message}")


def main() -> None:
    catalog = json.loads((SCHEMA_DIR / "catalog.json").read_text(encoding="utf-8"))
    names = catalog.get("schemas")
    if not isinstance(names, list) or not names:
        fail("schema catalogue is empty")
    if len(names) != len(set(names)):
        fail("schema catalogue contains duplicates")

    loaded = {}
    for name in names:
        path = SCHEMA_DIR / name
        if not path.is_file():
            fail(f"missing schema: {name}")
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail(f"unexpected draft for {name}")
        if data.get("$id") != name:
            fail(f"$id must equal filename for {name}")
        loaded[name] = data

        for referenced in LOCAL_REF.findall(path.read_text(encoding="utf-8")):
            if not (SCHEMA_DIR / referenced).is_file():
                fail(f"broken local ref in {name}: {referenced}")

    runtime_private = {
        "source-session.schema.json", "source-span.schema.json", "topic.schema.json",
        "learning-signal.schema.json", "candidate.schema.json", "notebook-unit.schema.json",
        "anki-note.schema.json", "authority-conflict.schema.json",
        "import-reconciliation.schema.json", "session-manifest.schema.json",
        "topic-evidence-packet.schema.json", "candidate-ledger.schema.json",
        "experimental-notebook-manifest.schema.json", "gold-comparison.schema.json",
        "calibration-report.schema.json", "source-span-index.schema.json",
        "private-source-archive.schema.json", "source-fidelity-report.schema.json",
        "checkpoint-link.schema.json", "session-state-transition.schema.json",
        "pilot-bundle.schema.json"
    }
    for name in runtime_private:
        required = set(loaded[name].get("required", []))
        if "privacy" not in required:
            fail(f"private runtime schema must require privacy: {name}")

    print(f"SCHEMA_PASS count={len(names)}")


if __name__ == "__main__":
    main()
