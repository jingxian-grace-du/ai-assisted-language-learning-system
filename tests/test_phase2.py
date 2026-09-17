from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "pipeline/eod.py"
FIXTURES = ROOT / "tests/fixtures/synthetic"


class Phase2Tests(unittest.TestCase):
    def run_cli(self, *args: str, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(CLI), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def test_init_and_validate_external_session(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            private_root = Path(temporary) / "private-root"
            result = self.run_cli(
                "init-session",
                "--private-root", str(private_root),
                "--session-id", "EOD-SYN-SESSION-001",
            )
            session_root = Path(result.stdout.strip())
            self.assertTrue((session_root / "session-manifest.json").is_file())
            validation = self.run_cli("validate-session", "--session-root", str(session_root))
            self.assertIn("SESSION_VALIDATION_PASS", validation.stdout)

    def test_rejects_private_root_inside_repository(self) -> None:
        result = self.run_cli(
            "init-session",
            "--private-root", str(ROOT / "private-runtime"),
            "--session-id", "EOD-SYN-SESSION-002",
            expected=1,
        )
        self.assertIn("RM-PRIVATE-PATH-IN-REPOSITORY", result.stderr)

    def test_structural_gold_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "comparison.json"
            self.run_cli(
                "compare",
                "--prediction", str(FIXTURES / "prediction-ledger.json"),
                "--gold", str(FIXTURES / "gold-ledger.json"),
                "--output", str(output),
                "--comparison-id", "CMP-SYN-001",
            )
            comparison = json.loads(output.read_text(encoding="utf-8"))
            outcomes = {item["target_key"]: item["outcome"] for item in comparison["outcomes"]}
            self.assertEqual(outcomes["TARGET-SYN-001"], "true-positive")
            self.assertEqual(outcomes["TARGET-SYN-002"], "partial-target")
            self.assertEqual(outcomes["TARGET-SYN-003"], "false-positive")
            self.assertEqual(outcomes["TARGET-SYN-004"], "false-negative")
            self.assertEqual(comparison["metrics"]["true_positive"], 1)
            self.assertEqual(comparison["metrics"]["false_positive"], 1)
            self.assertEqual(comparison["metrics"]["false_negative"], 1)

    def test_content_free_pilot_bundle_end_to_end(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            private_root = Path(temporary) / "private-root"
            init = self.run_cli(
                "init-session",
                "--private-root", str(private_root),
                "--session-id", "EOD-SYN-SESSION-001",
            )
            session_root = Path(init.stdout.strip())
            imported = self.run_cli(
                "import-bundle",
                "--bundle", str(FIXTURES / "pilot-bundle.json"),
                "--session-root", str(session_root),
            )
            self.assertIn("status=candidate-generated", imported.stdout)

            status = self.run_cli("status", "--session-root", str(session_root), "--json")
            summary = json.loads(status.stdout)
            self.assertTrue(summary["bundle_imported"])
            self.assertEqual(summary["counts"]["source_spans"], 3)
            self.assertEqual(summary["counts"]["rm_gates"], 8)
            self.assertFalse(summary["anki_ready"])

            self.run_cli(
                "import-source-archive",
                "--archive", str(FIXTURES / "private-source-archive.json"),
                "--session-root", str(session_root),
            )
            self.run_cli(
                "import-gold",
                "--gold", str(FIXTURES / "pilot-gold-ledger.json"),
                "--fidelity-report", str(FIXTURES / "source-fidelity-report.json"),
                "--session-root", str(session_root),
            )
            self.run_cli(
                "compare-session",
                "--comparison-id", "CMP-SYN-001",
                "--session-root", str(session_root),
            )
            comparison_path = session_root / "comparisons" / "gold-comparison.json"
            report_path = session_root / "calibration" / "report.json"
            self.run_cli(
                "calibration-report",
                "--comparison", str(comparison_path),
                "--output", str(report_path),
                "--report-id", "CAL-SYN-001",
                "--session-root", str(session_root),
            )
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertTrue(report["next_cycle_required"])
            self.assertEqual(report["difference_counts"], {"true-positive": 1})

            validation = self.run_cli("validate-session", "--session-root", str(session_root))
            self.assertIn("status=comparison-complete", validation.stdout)

            status = self.run_cli("status", "--session-root", str(session_root), "--json")
            completed = json.loads(status.stdout)
            self.assertTrue(completed["source_archive_imported"])
            self.assertTrue(completed["manual_gold_imported"])
            self.assertTrue(completed["rm8_complete"])
            self.assertTrue(completed["rm9_complete"])

    def test_bundle_rejects_source_text_in_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            private_root = Path(temporary) / "private-root"
            init = self.run_cli(
                "init-session",
                "--private-root", str(private_root),
                "--session-id", "EOD-SYN-SESSION-001",
            )
            session_root = Path(init.stdout.strip())
            bundle = json.loads((FIXTURES / "pilot-bundle.json").read_text(encoding="utf-8"))
            bundle["source_span_index"]["spans"][0]["content"] = "SYNTHETIC-PROHIBITED-CONTENT"
            bundle_path = Path(temporary) / "invalid-bundle.json"
            bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            result = self.run_cli(
                "import-bundle",
                "--bundle", str(bundle_path),
                "--session-root", str(session_root),
                expected=1,
            )
            self.assertIn("source text is prohibited", result.stderr)

    def test_state_machine_rejects_skipped_manual_transition(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            init = self.run_cli(
                "init-session",
                "--private-root", str(Path(temporary) / "private-root"),
                "--session-id", "EOD-SYN-SESSION-003",
            )
            session_root = Path(init.stdout.strip())
            rejected = self.run_cli(
                "transition",
                "--session-root", str(session_root),
                "--to", "morning-complete",
                expected=1,
            )
            self.assertIn("invalid state transition", rejected.stderr)
            accepted = self.run_cli(
                "transition",
                "--session-root", str(session_root),
                "--to", "night-open",
            )
            self.assertIn("status=night-open", accepted.stdout)

    def test_gold_handoff_requires_complete_source_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            init = self.run_cli(
                "init-session",
                "--private-root", str(Path(temporary) / "private-root"),
                "--session-id", "EOD-SYN-SESSION-001",
            )
            session_root = Path(init.stdout.strip())
            self.run_cli(
                "import-bundle",
                "--bundle", str(FIXTURES / "pilot-bundle.json"),
                "--session-root", str(session_root),
            )
            archive = json.loads((FIXTURES / "private-source-archive.json").read_text(encoding="utf-8"))
            archive["segments"][0]["complete"] = False
            archive["completeness"]["status"] = "partial"
            archive["completeness"]["missing_ranges"] = ["synthetic missing range"]
            archive_path = Path(temporary) / "partial-archive.json"
            archive_path.write_text(json.dumps(archive), encoding="utf-8")
            result = self.run_cli(
                "import-source-archive",
                "--archive", str(archive_path),
                "--session-root", str(session_root),
                expected=1,
            )
            self.assertIn("RM-SOURCE-ARCHIVE-INVALID", result.stderr)

    def test_gold_ready_cannot_be_set_by_manual_transition(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            init = self.run_cli(
                "init-session",
                "--private-root", str(Path(temporary) / "private-root"),
                "--session-id", "EOD-SYN-SESSION-004",
            )
            session_root = Path(init.stdout.strip())
            result = self.run_cli(
                "transition",
                "--session-root", str(session_root),
                "--to", "gold-ready",
                expected=1,
            )
            self.assertIn("produced only by validated Codex workflow commands", result.stderr)


if __name__ == "__main__":
    unittest.main()
