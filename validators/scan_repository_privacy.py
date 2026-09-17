#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".yaml", ".yml", ".toml"}
FORBIDDEN = {
    "absolute-user-path": re.compile("/" + "Users/" + r"[^/\s]+/"),
    "codex-thread-id": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
    "nonportable-citation-token": re.compile(
        "" + "cite" + "|" + "turn" + r"\d+(?:search|fetch|view)\d+", re.I
    ),
}


def main() -> None:
    findings = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path.relative_to(ROOT)}:{line}: {label}")

    if findings:
        print("PRIVACY_SCAN_FAIL")
        print("\n".join(findings))
        raise SystemExit(1)
    print("PRIVACY_SCAN_PASS")


if __name__ == "__main__":
    main()
