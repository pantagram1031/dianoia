import tempfile
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import verify_phase_loop as phase_loop  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class PhaseLoopVerifierTest(unittest.TestCase):
    def test_reviewer_d_missing_gated_phase_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(
                root / "prompts" / "prove.md",
                "00-intake 05-review 01-survey 05-review 02-perspective 05-review "
                "03-hypothesize 05-review 04-develop 05-review 06-consolidate 05-review "
                "prompts/checkpoint.md",
            )
            write(
                root / "prompts" / "05-review.md",
                "Invoke reviewer A. Invoke reviewer B. Invoke reviewer C. "
                "Reviewer D fires at 03-hypothesize, 04-develop, 06-consolidate.",
            )
            for name in (
                "researcher",
                "surveyor",
                "sanity-checker",
                "prover",
                "reviewer",
                "muser",
                "skill-author",
                "specialist-factory",
            ):
                write(root / "prompts" / "subagents" / f"{name}.md", "SUBAGENT CONTRACT")
            write(root / "prompts" / "checkpoint.md", "citation_check ledger_delta")

            result = phase_loop.check_phase_loop(root)

        self.assertTrue(
            any("Reviewer D gated phases missing 00-intake" in item for item in result.fail),
            result.fail,
        )


if __name__ == "__main__":
    unittest.main()
