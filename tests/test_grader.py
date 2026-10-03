import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "demo"))

import grader  # noqa: E402

EXAMPLE_SPEC = ROOT / "examples" / "01-python-data-cli.md"
EXAMPLE_SUB = ROOT / "demo" / "example_submission.py"


class TestSectionParsing(unittest.TestCase):
    def setUp(self):
        self.spec = grader.parse_sections(EXAMPLE_SPEC.read_text(encoding="utf-8"))

    def test_parses_expected_sections(self):
        titles = " ".join(self.spec)
        for keyword in ("Goal", "Context", "Acceptance", "Rubric", "Traps"):
            self.assertIn(keyword, titles)

    def test_acceptance_criteria_extracted(self):
        criteria = grader.acceptance_criteria(self.spec)
        self.assertGreaterEqual(len(criteria), 4)

    def test_rubric_rows_extracted(self):
        dims = [d for d, _ in grader.rubric_rows(self.spec)]
        self.assertIn("Correctness", dims)
        self.assertIn("Streaming", dims)


class TestMockScoring(unittest.TestCase):
    def test_good_submission_scores_full(self):
        code = EXAMPLE_SUB.read_text(encoding="utf-8")
        self.assertTrue(all(grader.mock_checks(code).values()))

    def test_stub_scores_low(self):
        checks = grader.mock_checks("print('hello')\n")
        self.assertFalse(checks["not a stub"])
        self.assertFalse(checks["has an entry point"])
        self.assertFalse(checks["has error handling"])


class TestPromptAndCli(unittest.TestCase):
    def test_build_prompt_contains_criteria_and_rubric(self):
        prompt = grader.build_prompt(EXAMPLE_SPEC, "code = 1\n")
        self.assertIn("Acceptance criteria", prompt)
        self.assertIn("Rubric", prompt)

    def test_cli_mock_mode_returns_zero(self):
        self.assertEqual(
            grader.main([str(EXAMPLE_SPEC), str(EXAMPLE_SUB), "--mock"]), 0
        )


if __name__ == "__main__":
    unittest.main()
