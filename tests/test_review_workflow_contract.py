"""Contract tests for dormant, non-invasive security checks."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/archived-security-review.yml"


class OfflineReviewSafetyTests(unittest.TestCase):
    def test_workflow_never_runs_publishers_or_exposes_secrets(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("pull_request:", text)
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("persist-credentials: false", text)
        self.assertIn("--network none", text)
        self.assertIn("--read-only", text)
        self.assertIn("--metrics=off", text)
        for forbidden in (
            "schedule:", "pull_request_target:", "secrets.",
            "contents: write", "id-token: write", "smtp",
            "src/cron.py", "src/main.py", "docker compose up",
        ):
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
