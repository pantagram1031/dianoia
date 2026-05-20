#!/usr/bin/env python3
"""Verify stale-active and resume routing guard invariants."""

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


def normalize_space(text: str) -> str:
    return " ".join(text.split())


def require_all(result: CheckResult, label: str, text: str, phrases: tuple[str, ...]) -> None:
    normalized = normalize_space(text)
    missing = [phrase for phrase in phrases if normalize_space(phrase) not in normalized]
    if missing:
        result.add_fail(f"{label} missing " + "; ".join(missing))
    else:
        result.add_ok(f"{label} contains required guard phrases")


def check_routing_guards(root: Path = ROOT) -> CheckResult:
    result = CheckResult(ok=[], fail=[])
    paths = {
        "AGENTS.md": root / "AGENTS.md",
        "prove.md": root / "prompts" / "prove.md",
        "resume.md": root / "prompts" / "resume.md",
        "00-intake.md": root / "prompts" / "00-intake.md",
    }
    for label, path in paths.items():
        if not path.exists():
            result.add_fail(f"missing {label}: {path}")
    if result.fail:
        return result

    agents = read_text(paths["AGENTS.md"])
    prove = read_text(paths["prove.md"])
    resume = read_text(paths["resume.md"])
    intake = read_text(paths["00-intake.md"])

    require_all(
        result,
        "AGENTS.md malformed active fresh-route guard",
        agents,
        (
            "malformed",
            "zero or multiple slugs",
            "missing session_state.md",
            "prompts/prove.md with the message as $1",
        ),
    )
    if all(
        phrase in agents
        for phrase in (
            "halt_flag=true",
            "SUCCESS-MEANINGFUL",
            "FAILURE-AMBITION-GAP",
            "BLOCKED-ITERATE",
            "fresh problem statement",
        )
    ):
        result.add_ok("AGENTS.md contains closed active fresh-route guard")
    else:
        result.add_fail("AGENTS.md missing closed active fresh-route guard")

    require_all(
        result,
        "prove.md stale-active guard",
        prove,
        (
            "Malformed stale state MUST NOT receive new problem content.",
            "closed problem",
            "fresh slug",
            "superseded_active",
            "do not append `$1` to that problem",
        ),
    )

    if all(
        phrase in resume
        for phrase in (
            "Only `BLOCKED-ITERATE` is resume-eligible",
            "SUCCESS-MEANINGFUL",
            "FAILURE-AMBITION-GAP",
            "halt_flag true without resume-eligible halt reason",
            "fresh problem statements use prompts/prove.md",
        )
    ):
        result.add_ok("resume.md contains BLOCKED-ITERATE-only guard")
    else:
        result.add_fail("resume.md missing BLOCKED-ITERATE-only guard")

    require_all(
        result,
        "00-intake.md closed active guard",
        intake,
        (
            "session_state.md",
            "halt_flag: true",
            "active problem is closed",
            "use prompts/prove.md for a fresh problem",
        ),
    )

    return result


def main() -> int:
    result = check_routing_guards(ROOT)
    for message in result.ok:
        print(f"OK {message}")
    for message in result.fail:
        print(f"FAIL {message}")
    print(f"SUMMARY ok={len(result.ok)} fail={len(result.fail)}")
    return 1 if result.fail else 0


if __name__ == "__main__":
    sys.exit(main())
