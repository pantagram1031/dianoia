import tempfile
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import verify_dianoia_state as verifier  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def source_text(area: str = "algebra") -> str:
    return f"""# Source

## Metadata

- Authors: A
- Year: 2026
- Title: T
- Exact statement reference: Theorem 1

## Source

arXiv:test

## Modification

Controlled modification.

## Area

{area}

## Artifacts

- Raw baseline: raw
- Dianoia run: dianoia
- Run manifest: benchmark-bank/B6/RUN.md
"""


def source_text_missing_exact_statement(area: str = "algebra") -> str:
    return f"""# Source

## Metadata

- Authors: A
- Year: 2026
- Title: T

## Source

arXiv:test

## Modification

Controlled modification.

## Area

{area}

## Artifacts

- Raw baseline: raw
- Dianoia run: dianoia
"""


def comparison_text() -> str:
    return """# Comparison

## Verdict

VALUE_ADDED

## Three Differences

1. exact citation
2. ledgered claim
3. reviewer defect
"""


def structured_comparison_text() -> str:
    return """# Comparison

## Verdict

VALUE_ADDED

## Three Differences

1. artifact: `raw/answer.md`; quote: `raw omitted reviewer evidence`
2. artifact: `problems/example/claim_ledger.md`; quote: `C-001 | ... | PROVED`
3. artifact: `problems/example/review.md`; quote: `Reviewer D blocked overclaim`
"""


def run_text(run_class: str, known_weaknesses: str) -> str:
    return f"""# Run

benchmark_id: B6
run_class: {run_class}

## Problem Statement

P

## Raw Workspace

raw

## Dianoia Workspace

dianoia

## Freshness Protocol

fresh

## Commands Or Manual Steps

steps

## Subagent Fire Audit

| subagent | expected | fired | evidence |
|----------|----------|-------|----------|

## Reviewer Fire Audit

| persona | expected | fired | evidence |
|---------|----------|-------|----------|

## Token Accounting

Method: estimated from logs
Raw tokens: 100
Dianoia tokens: 200
Uncertainty: +/- 25

## Known Weaknesses

{known_weaknesses}
"""


def run_text_unverified_tokens(token_extra: str = "") -> str:
    return f"""# Run

benchmark_id: B6
run_class: full-fresh

## Problem Statement

P

## Raw Workspace

raw

## Dianoia Workspace

dianoia

## Freshness Protocol

fresh

## Commands Or Manual Steps

steps

## Subagent Fire Audit

| subagent | expected | fired | evidence |
|----------|----------|-------|----------|

## Reviewer Fire Audit

| persona | expected | fired | evidence |
|---------|----------|-------|----------|

## Token Accounting

Method: UNVERIFIED
Raw tokens: UNVERIFIED
Dianoia tokens: UNVERIFIED
Uncertainty: UNVERIFIED
{token_extra}

## Known Weaknesses

none
"""


def make_repo(root: Path, b6_run: str) -> None:
    rows = [
        ("B1", "number theory"),
        ("B2", "combinatorics"),
        ("B3", "geometry"),
        ("B4", "probability"),
        ("B5", "algebra"),
        ("B6", "algebra"),
    ]
    table = [
        "# Benchmark",
        "",
        "| ID | area | source | raw verdict | dianoia verdict | head-to-head | tokens | artifact paths |",
        "|----|------|--------|-------------|-----------------|--------------|--------|----------------|",
    ]
    for bid, area in rows:
        table.append(
            f"| {bid} | {area} | source | raw | dianoia | VALUE_ADDED | 123 | `benchmark-bank/{bid}/SOURCE.md`; `benchmark-bank/{bid}/COMPARISON.md` |"
        )
        write(root / "benchmark-bank" / bid / "SOURCE.md", source_text(area))
        write(root / "benchmark-bank" / bid / "COMPARISON.md", comparison_text())
    write(root / "BENCHMARK.md", "\n".join(table) + "\n")
    write(root / "benchmark-bank" / "B6" / "RUN.md", b6_run)
    (root / "raw").mkdir()
    (root / "dianoia").mkdir()


def mark_b6_tokens_unverified(root: Path) -> None:
    text = (root / "BENCHMARK.md").read_text(encoding="utf-8")
    text = text.replace("| B6 | algebra | source | raw | dianoia | VALUE_ADDED | 123 |", "| B6 | algebra | source | raw | dianoia | VALUE_ADDED | UNVERIFIED |")
    write(root / "BENCHMARK.md", text)


class BenchmarkManifestVerifierTest(unittest.TestCase):
    def run_benchmark_check(self, b6_run: str) -> verifier.CheckResult:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(temp_root, b6_run)
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
            return result
        finally:
            verifier.ROOT = original_root

    def test_rejects_unknown_b6_run_class(self) -> None:
        result = self.run_benchmark_check(run_text("quick-pass", "none"))

        self.assertTrue(
            any("run_class must be full-fresh or controlled-comparison" in item for item in result.fail),
            result.fail,
        )

    def test_controlled_comparison_must_name_known_weakness(self) -> None:
        result = self.run_benchmark_check(run_text("controlled-comparison", "none"))

        self.assertTrue(
            any("controlled-comparison must name a concrete known weakness" in item for item in result.fail),
            result.fail,
        )

    def test_b6_source_must_have_four_citation_fields(self) -> None:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(temp_root, run_text("full-fresh", "none"))
                write(temp_root / "benchmark-bank" / "B6" / "SOURCE.md", source_text_missing_exact_statement())
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
        finally:
            verifier.ROOT = original_root

        self.assertTrue(
            any("SOURCE.md Metadata missing Exact statement reference" in item for item in result.fail),
            result.fail,
        )

    def test_b6_source_artifact_paths_must_exist(self) -> None:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(temp_root, run_text("full-fresh", "none"))
                (temp_root / "raw").rmdir()
                write(temp_root / "benchmark-bank" / "B6" / "COMPARISON.md", structured_comparison_text())
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
        finally:
            verifier.ROOT = original_root

        self.assertTrue(
            any("SOURCE.md Artifacts Raw baseline path missing" in item for item in result.fail),
            result.fail,
        )

    def test_b6_value_added_requires_structured_difference_evidence(self) -> None:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(temp_root, run_text("full-fresh", "none"))
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
        finally:
            verifier.ROOT = original_root

        self.assertTrue(
            any("VALUE_ADDED comparison difference 1 missing artifact/quote evidence" in item for item in result.fail),
            result.fail,
        )

    def test_b6_value_added_accepts_structured_difference_evidence(self) -> None:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(temp_root, run_text("full-fresh", "none"))
                write(temp_root / "benchmark-bank" / "B6" / "COMPARISON.md", structured_comparison_text())
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
        finally:
            verifier.ROOT = original_root

        self.assertFalse(
            any("VALUE_ADDED comparison difference" in item for item in result.fail),
            result.fail,
        )

    def test_b6_unverified_tokens_require_blocker_and_plan(self) -> None:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(temp_root, run_text_unverified_tokens())
                write(temp_root / "benchmark-bank" / "B6" / "COMPARISON.md", structured_comparison_text())
                mark_b6_tokens_unverified(temp_root)
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
        finally:
            verifier.ROOT = original_root

        self.assertTrue(
            any("UNVERIFIED token accounting must name Blocker and Removal plan" in item for item in result.fail),
            result.fail,
        )

    def test_b6_unverified_tokens_accept_blocker_and_plan(self) -> None:
        original_root = verifier.ROOT
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                make_repo(
                    temp_root,
                    run_text_unverified_tokens(
                        "Blocker: runtime did not expose token logs\n"
                        "Removal plan: rerun with explicit transcript token counter\n"
                    ),
                )
                write(temp_root / "benchmark-bank" / "B6" / "COMPARISON.md", structured_comparison_text())
                mark_b6_tokens_unverified(temp_root)
                verifier.ROOT = temp_root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_benchmarks(result)
        finally:
            verifier.ROOT = original_root

        self.assertFalse(
            any("UNVERIFIED token accounting must name Blocker and Removal plan" in item for item in result.fail),
            result.fail,
        )


class CapabilityReferenceVerifierTest(unittest.TestCase):
    def test_missing_referenced_capability_artifact_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(root / "README.md", "5 accepted controlled comparisons\nbaseline rather than a terminal\n")
            write(root / "ARCHITECTURE.md", "## Phase Loop\n## Meaningfulness Gate\n## Subagent Flow\n")
            write(root / "ROADMAP.md", "Continuous Improvement Track\ncapability-test/MISSING.md\n")
            write(root / "EXAMPLES.md", "")
            write(root / "CHANGELOG.md", "")
            write(root / "NEXT_SESSION.md", "")
            write(root / "DEVLOG.md", "")
            write(root / "benchmark-bank" / "RUNBOOK.md", "")
            write(root / "templates" / "benchmark_case" / "RUN.md", "")

            original_root = verifier.ROOT
            try:
                verifier.ROOT = root
                result = verifier.CheckResult(ok=[], warn=[], fail=[])
                verifier.check_docs(result)
            finally:
                verifier.ROOT = original_root

        self.assertTrue(
            any("missing referenced capability artifact: capability-test/MISSING.md" in item for item in result.fail),
            result.fail,
        )


if __name__ == "__main__":
    unittest.main()
