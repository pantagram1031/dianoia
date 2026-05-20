#!/usr/bin/env python3
"""Verify core dianoia phase-loop prompt invariants."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CheckResult:
    ok: list[str]
    fail: list[str]

    def add_ok(self, message: str) -> None:
        self.ok.append(message)

    def add_fail(self, message: str) -> None:
        self.fail.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_in_order(text: str, needles: list[str]) -> bool:
    cursor = 0
    for needle in needles:
        position = text.find(needle, cursor)
        if position == -1:
            return False
        cursor = position + len(needle)
    return True


def reviewer_d_window(review_text: str) -> str:
    marker = "Reviewer D fires"
    start = review_text.find(marker)
    if start == -1:
        return ""
    end_marker = "Reviewer D answers"
    end = review_text.find(end_marker, start)
    return review_text[start:end if end != -1 else len(review_text)]


def check_phase_loop(root: Path = ROOT) -> CheckResult:
    result = CheckResult(ok=[], fail=[])
    prompts = root / "prompts"
    prove = prompts / "prove.md"
    review = prompts / "05-review.md"
    checkpoint = prompts / "checkpoint.md"

    for path in (prove, review, checkpoint):
        if not path.exists():
            result.add_fail(f"missing prompt: {path.relative_to(root)}")
    if result.fail:
        return result

    prove_text = read_text(prove)
    review_text = read_text(review)
    checkpoint_text = read_text(checkpoint)

    sequence = [
        "00-intake",
        "05-review",
        "01-survey",
        "05-review",
        "02-perspective",
        "05-review",
        "03-hypothesize",
        "05-review",
        "04-develop",
        "05-review",
        "06-consolidate",
        "05-review",
    ]
    if find_in_order(prove_text, sequence):
        result.add_ok("prove.md contains the expected phase/review order")
    else:
        result.add_fail("prove.md missing expected phase/review order")

    for phrase in (
        "After each atomic unit",
        "prompts/checkpoint.md",
        "BATCHING PROHIBITED",
    ):
        if phrase in prove_text:
            result.add_ok(f"prove.md contains {phrase}")
        else:
            result.add_fail(f"prove.md missing {phrase}")

    for persona in ("persona `A`", "persona `B`", "persona `C`"):
        if persona in review_text:
            result.add_ok(f"05-review.md invokes {persona}")
        else:
            result.add_fail(f"05-review.md missing invocation for {persona}")

    d_window = reviewer_d_window(review_text)
    if not d_window:
        result.add_fail("05-review.md missing Reviewer D gated-phase rule")
    else:
        missing = [
            phase
            for phase in ("00-intake", "03-hypothesize", "04-develop", "06-consolidate")
            if phase not in d_window
        ]
        if missing:
            result.add_fail(
                "Reviewer D gated phases missing " + ", ".join(missing)
            )
        else:
            result.add_ok("Reviewer D gated phases present")

    required_subagents = (
        "researcher",
        "surveyor",
        "sanity-checker",
        "prover",
        "reviewer",
        "muser",
        "skill-author",
        "specialist-factory",
    )
    for name in required_subagents:
        path = prompts / "subagents" / f"{name}.md"
        if not path.exists():
            result.add_fail(f"missing subagent prompt: {path.relative_to(root)}")
            continue
        text = read_text(path)
        if "SUBAGENT CONTRACT" not in text:
            result.add_fail(f"{path.relative_to(root)} missing SUBAGENT CONTRACT")
        elif "forbidden_writes" not in text:
            result.add_fail(f"{path.relative_to(root)} missing forbidden_writes")
        else:
            result.add_ok(f"subagent contract present: {name}")

    for phrase in ("citation_check", "ledger_delta"):
        if phrase in checkpoint_text:
            result.add_ok(f"checkpoint.md contains {phrase}")
        else:
            result.add_fail(f"checkpoint.md missing {phrase}")

    return result


def main() -> int:
    result = check_phase_loop(ROOT)
    for message in result.ok:
        print(f"OK {message}")
    for message in result.fail:
        print(f"FAIL {message}")
    print(f"SUMMARY ok={len(result.ok)} fail={len(result.fail)}")
    return 1 if result.fail else 0


if __name__ == "__main__":
    sys.exit(main())
