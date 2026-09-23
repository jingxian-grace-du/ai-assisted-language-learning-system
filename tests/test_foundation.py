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

    def test_vocabulary_answers_use_context_independent_citation_forms(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("context-independent", text)
                self.assertIn("citation form", text)
        specification = paths[0].read_text(encoding="utf-8")
        self.assertIn("`connect`, `hold back`", specification)
        self.assertIn("inflected form in the example", specification)

    def test_manual_gold_is_a_coverage_floor_not_an_exclusive_whitelist(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("coverage floor", text)
                self.assertIn("exclusive whitelist", text)
                self.assertIn("AI Supplementary", text)
                self.assertIn("Manual silence", text)

    def test_reciprocal_omission_scan_is_approval_gated(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            normalised = " ".join(text.split())
            with self.subTest(path=path.name):
                self.assertIn("reciprocal omission scan", normalised)
                self.assertIn("semantic inversion", normalised)
                self.assertIn("later", normalised)
                self.assertIn("reuse", normalised)
                self.assertIn("Manual-Gold Review Alert", normalised)
                self.assertIn("does not enter", normalised)

    def test_synonym_contrast_and_single_card_cloze_rules_are_consistent(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("Type::SynonymContrast", text)
                self.assertIn("c1", text)
                self.assertIn("intentionally separate", text)

    def test_false_positive_requires_more_than_manual_silence(self) -> None:
        catalogue = json.loads(
            (ROOT / "protocol/experimental/error-codes.json").read_text(encoding="utf-8")
        )
        code = next(
            item for item in catalogue["codes"]
            if item["code"] == "RM-TARGET-FALSE-POSITIVE"
        )
        self.assertIn("explicitly rejected", code["meaning"])
        self.assertIn("absence from manual marks alone is insufficient", code["meaning"])

    def test_context_cloze_chinese_prompt_remains_fully_visible(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("Chinese Prompt", text)
                self.assertIn("fully visible", text)
                self.assertIn("numbered blanks", text)
                self.assertIn("approved English targets", text)

    def test_topic_retell_preserves_sequence_and_causality(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("chronology", text)
                self.assertIn("causality", text)
                self.assertIn("event identity", text)
                self.assertIn("intervening event", text)

    def test_topic_retell_does_not_force_a_paired_phrase_card(self) -> None:
        paths = [
            ROOT / "protocol/experimental/raw-material-processing-spec-v0.1.md",
            ROOT
            / "protocol/experimental/english-oral-diary-protocol-v3.6-draft-shadow-mode-profile.md",
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt",
        ]
        for path in paths:
            normalised = " ".join(path.read_text(encoding="utf-8").split())
            with self.subTest(path=path.name):
                self.assertIn("Feynman-style", normalised)
                self.assertIn("Do not", normalised)
                self.assertIn("paired note", normalised)
                self.assertIn("distinct approved function", normalised)
                self.assertIn("contextual Cloze", normalised)

    def test_chatgpt_handoff_excludes_post_bundle_gold_processing(self) -> None:
        path = (
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt"
        )
        normalised = " ".join(path.read_text(encoding="utf-8").split())
        self.assertIn("perform the reciprocal omission scan", normalised)
        self.assertIn("Those are Codex post-handoff steps", normalised)
        self.assertIn("stop the ChatGPT Shadow Mode processing stage", normalised)

    def test_chatgpt_project_instructions_fit_character_limit(self) -> None:
        path = (
            ROOT
            / "protocol/experimental/chatgpt-project-instructions-phase-2-replacement.txt"
        )
        text = path.read_text(encoding="utf-8")
        self.assertLessEqual(len(text), 8000)


if __name__ == "__main__":
    unittest.main()
