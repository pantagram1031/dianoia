import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import verify_research_state as research_state  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_valid_research_state(root: Path) -> None:
    write(
        root / "ROADMAP.md",
        """# Roadmap

| Phase | Name | Status | Evidence |
|-------|------|--------|----------|
| 9 | RESEARCH INFRA | IN_PROGRESS | P9 infra |
| 10 | CURATION | PENDING | P10 curation |
| 11 | ATTEMPTS | PENDING | P11 attempts |
| 12 | VERIFICATION GATE | PENDING | P12 verification |
| 13 | INTERMEDIATE WINS | PENDING | P13 notes |

## Research Contribution Track

RESEARCH_CONTRIBUTION
""",
    )
    write(
        root / "RESEARCH_LOG.md",
        "RESEARCH_CONTRIBUTION formal-check openness-verification adversarial-novelty\n",
    )
    write(
        root / "CLAIMS.md",
        """# Claims

| id | date | claim | type | openness trail | adversarial summary | formal/computational evidence | confidence 1-10 | status |
|----|------|-------|------|----------------|---------------------|-------------------------------|-----------------|--------|

CANDIDATE
PARTIAL-PROGRESS
OBSTRUCTION-FOUND
SOLVED-CLAIM-PENDING-GATES
DOWNGRADED
BLOCKED-EXTERNAL-REVIEW
""",
    )
    bank_table = """| id | source | area | openness verified date | tractability rank | why dianoia adds value | status |
|----|--------|------|------------------------|-------------------|------------------------|--------|
"""
    write(root / "research-bank" / "README.md", bank_table)
    write(root / "research-bank" / "INDEX.md", bank_table)
    write(
        root / "prompts" / "subagents" / "researcher.md",
        "connectors/arxiv/server.py openness\n"
        "connectors/lean/server.py\n"
        "skills/openness-verification/SKILL.md\n"
        "skills/adversarial-novelty-check/SKILL.md\n",
    )
    write(root / "connectors" / "arxiv" / "server.py", "openness --from-date --to-date submittedDate\n")
    write(root / "connectors" / "lean" / "server.py", "env check UNVERIFIED\n")
    write(root / "skills" / "openness-verification" / "SKILL.md", "## When To Use\n## Procedure\n")
    write(root / "skills" / "adversarial-novelty-check" / "SKILL.md", "## When To Use\n## Procedure\n")
    write(root / "templates" / "research_candidate" / "SOURCE.md", "id:\n")
    for filename in ("OPENNESS.md", "TRACTABILITY.md", "log.md", "NOVELTY.md", "CLAIM_GATE.md"):
        write(root / "templates" / "research_candidate" / filename, "candidate_id:\n")


class ResearchStateVerifierTest(unittest.TestCase):
    def test_valid_research_state_passes_with_empty_bank_warning(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_valid_research_state(root)

            result = research_state.check_research_state(root)

        self.assertEqual([], result.fail)
        self.assertTrue(any("no promoted candidates" in warning for warning in result.warn), result.warn)

    def test_missing_researcher_wiring_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_valid_research_state(root)
            write(root / "prompts" / "subagents" / "researcher.md", "connectors/lean/server.py\n")

            result = research_state.check_research_state(root)

        self.assertTrue(any("connectors/arxiv/server.py openness" in failure for failure in result.fail), result.fail)
        self.assertTrue(any("skills/openness-verification/SKILL.md" in failure for failure in result.fail), result.fail)

    def test_candidate_directory_requires_four_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_valid_research_state(root)
            write(root / "research-bank" / "R001" / "SOURCE.md", "# Source\n")

            result = research_state.check_research_state(root)

        self.assertTrue(any("R001 missing OPENNESS.md" in failure for failure in result.fail), result.fail)
        self.assertTrue(any("R001 missing TRACTABILITY.md" in failure for failure in result.fail), result.fail)
        self.assertTrue(any("R001 missing log.md" in failure for failure in result.fail), result.fail)

    def test_research_bank_stats_count_only_open_verified_rows(self) -> None:
        index_text = """# Research Bank Index

| id | source | area | openness verified date | tractability rank | why dianoia adds value | status |
|----|--------|------|------------------------|-------------------|------------------------|--------|
| R001 | source | combinatorics | 2026-05-20 (OPEN-WEAK) | A | warm-up | CURATED-OPEN-WEAK |
| R002 | source | number theory | 2026-05-20 | B | useful | OPEN-VERIFIED |
| R003 | source | algebra | 2026-05-20 | B | useful | CURATED-OPEN-VERIFIED |
"""

        stats = research_state.research_bank_stats(index_text)

        self.assertEqual(2, stats.open_verified)
        self.assertEqual({"number theory", "algebra"}, stats.open_verified_areas)

    def test_p10_gate_reports_pending_until_20_candidates_and_4_areas(self) -> None:
        stats = research_state.ResearchBankStats(
            open_verified=19,
            open_verified_areas={"number theory", "algebra", "geometry", "probability"},
        )

        self.assertEqual(
            "P10 gate PENDING: need 1 more OPEN-VERIFIED candidates and 0 more areas",
            research_state.p10_gate_message(stats),
        )

    def test_p10_gate_reports_ready_at_20_candidates_and_4_areas(self) -> None:
        stats = research_state.ResearchBankStats(
            open_verified=20,
            open_verified_areas={"number theory", "algebra", "geometry", "probability"},
        )

        self.assertEqual(
            "P10 gate READY: 20 OPEN-VERIFIED candidates across 4 areas",
            research_state.p10_gate_message(stats),
        )

    def test_p10_progress_message_reports_verified_count_and_areas(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_valid_research_state(root)
            write(
                root / "research-bank" / "INDEX.md",
                """| id | source | area | openness verified date | tractability rank | why dianoia adds value | status |
|----|--------|------|------------------------|-------------------|------------------------|--------|
| R002 | source | number theory | 2026-05-20 | B | useful | OPEN-VERIFIED |
""",
            )

            result = research_state.check_research_state(root)

        self.assertTrue(any("P10 progress: 1 OPEN-VERIFIED candidates across 1 areas" in item for item in result.ok), result.ok)

    def test_index_open_verified_requires_matching_openness_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_valid_research_state(root)
            write(
                root / "research-bank" / "INDEX.md",
                """| id | source | area | openness verified date | tractability rank | why dianoia adds value | status |
|----|--------|------|------------------------|-------------------|------------------------|--------|
| R002 | source | number theory | 2026-05-20 (OPEN-VERIFIED) | B | useful | CURATED-OPEN-VERIFIED |
""",
            )
            write(root / "research-bank" / "R002" / "SOURCE.md", "status: OPEN-VERIFIED\n")
            write(root / "research-bank" / "R002" / "OPENNESS.md", "status: OPEN-WEAK\n")
            write(root / "research-bank" / "R002" / "TRACTABILITY.md", "rank: B\n")
            write(root / "research-bank" / "R002" / "log.md", "current_status: CURATED-OPEN-WEAK\n")

            result = research_state.check_research_state(root)

        self.assertTrue(any("R002 index says OPEN-VERIFIED but OPENNESS.md status is OPEN-WEAK" in failure for failure in result.fail), result.fail)


if __name__ == "__main__":
    unittest.main()
