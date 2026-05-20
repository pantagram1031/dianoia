import tempfile
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import verify_routing_guards as routing  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class RoutingGuardVerifierTest(unittest.TestCase):
    def test_wrapped_guard_phrases_count_as_present(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(
                root / "AGENTS.md",
                "malformed zero or multiple slugs missing session_state.md "
                "prompts/prove.md with the message as $1 halt_flag=true "
                "SUCCESS-MEANINGFUL FAILURE-AMBITION-GAP BLOCKED-ITERATE fresh problem statement",
            )
            write(
                root / "prompts" / "prove.md",
                "Malformed stale state MUST NOT receive new problem\n"
                "content. closed problem fresh slug superseded_active "
                "do not append `$1` to that problem",
            )
            write(
                root / "prompts" / "resume.md",
                "Only `BLOCKED-ITERATE` is resume-eligible SUCCESS-MEANINGFUL "
                "FAILURE-AMBITION-GAP halt_flag true without resume-eligible halt reason "
                "fresh problem statements use prompts/prove.md",
            )
            write(
                root / "prompts" / "00-intake.md",
                "session_state.md halt_flag: true active problem is closed "
                "use prompts/prove.md for a fresh problem",
            )

            result = routing.check_routing_guards(root)

        self.assertEqual([], result.fail)

    def test_missing_closed_active_guard_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(root / "AGENTS.md", "malformed active pointer goes to prompts/prove.md")
            write(root / "prompts" / "prove.md", "Malformed stale state MUST NOT receive new problem content.")
            write(root / "prompts" / "resume.md", "Only BLOCKED-ITERATE is resume-eligible.")
            write(root / "prompts" / "00-intake.md", "active problem is closed")

            result = routing.check_routing_guards(root)

        self.assertTrue(
            any("AGENTS.md missing closed active fresh-route guard" in item for item in result.fail),
            result.fail,
        )

    def test_missing_resume_blocked_iterate_guard_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(
                root / "AGENTS.md",
                "malformed active pointer prompts/prove.md halt_flag=true SUCCESS-MEANINGFUL "
                "FAILURE-AMBITION-GAP BLOCKED-ITERATE",
            )
            write(root / "prompts" / "prove.md", "Malformed stale state MUST NOT receive new problem content. superseded_active closed problem fresh slug")
            write(root / "prompts" / "resume.md", "SUCCESS-MEANINGFUL FAILURE-AMBITION-GAP")
            write(root / "prompts" / "00-intake.md", "active problem is closed halt_flag: true prompts/prove.md")

            result = routing.check_routing_guards(root)

        self.assertTrue(
            any("resume.md missing BLOCKED-ITERATE-only guard" in item for item in result.fail),
            result.fail,
        )


if __name__ == "__main__":
    unittest.main()
