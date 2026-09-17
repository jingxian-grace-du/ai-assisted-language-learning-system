from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(script: str) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "validators" / script)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


class FoundationTests(unittest.TestCase):
    def test_requirements_catalogue(self) -> None:
        run("validate_requirements.py")

    def test_clause_inventory(self) -> None:
        run("validate_clause_inventory.py")

    def test_repository_privacy_scan(self) -> None:
        run("scan_repository_privacy.py")

    def test_schema_catalogue(self) -> None:
        run("validate_schemas.py")

    def test_requirement_coverage(self) -> None:
        run("validate_requirement_coverage.py")

    def test_error_code_catalogue(self) -> None:
        run("validate_error_codes.py")

    def test_catalogue_has_no_duplicate_ids(self) -> None:
        catalogue = json.loads((ROOT / "protocol/current/requirements.json").read_text())
        ids = [item["id"] for item in catalogue["requirements"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_topic_retell_front_enforcement_is_consistent(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
            ROOT / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("→", text)
                self.assertIn("；", text)
                self.assertIn("复述", text)
                self.assertIn("same-class scan", text)


if __name__ == "__main__":
    unittest.main()
