#!/usr/bin/env python3
"""Run dianoia local verification commands."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


COMMANDS = [
    [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
    [sys.executable, "tools/verify_dianoia_state.py"],
    [sys.executable, "tools/verify_phase_loop.py"],
    [sys.executable, "tools/verify_routing_guards.py"],
    [sys.executable, "tools/verify_connectors.py"],
    [sys.executable, "tools/verify_research_state.py"],
    [
        sys.executable,
        "tools/no_three_in_line_frontier.py",
        "verify-dir",
        "research-bank/R020/certificates",
    ],
    [sys.executable, "tools/poset_balance.py", "exhaustive-small", "--max-n", "5"],
    [sys.executable, "tools/poset_balance.py", "exhaustive-unlabeled", "--max-n", "5"],
    [
        sys.executable,
        "tools/poset_balance.py",
        "extremal-width",
        "--max-n",
        "5",
        "--width",
        "3",
        "--limit",
        "1",
    ],
    [
        sys.executable,
        "tools/poset_balance.py",
        "shape-classes",
        "--max-n",
        "5",
        "--width",
        "3",
        "--rank-shape",
        "2,2,1",
        "--signature",
        "matrix",
    ],
    [
        sys.executable,
        "tools/poset_balance.py",
        "matrix-feature-partition",
        "research-bank/R013/attempt-20260520/width3-rank2221-matrix-shape-classes-n7.json",
        "--threshold",
        "13/32",
    ],
]


def main() -> int:
    failures = 0
    for command in COMMANDS:
        print("==>", " ".join(command))
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
        if completed.stdout:
            print(completed.stdout, end="")
        if completed.stderr:
            print(completed.stderr, end="")
        if completed.returncode != 0:
            failures += 1
            print(f"FAIL command exited {completed.returncode}: {' '.join(command)}")
    if failures:
        print(f"SUMMARY fail={failures}")
        return 1
    print("SUMMARY all verification commands passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
