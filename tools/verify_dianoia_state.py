#!/usr/bin/env python3
"""Verify dianoia continuous-improvement baseline evidence.

The verifier intentionally checks files that future sessions are likely to
drift: benchmark rows and artifacts, skill references, connector wiring, and
current docs. It is a guardrail, not a theorem prover.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CheckResult:
    ok: list[str]
    warn: list[str]
    fail: list[str]

    def add_ok(self, message: str) -> None:
        self.ok.append(message)

    def add_warn(self, message: str) -> None:
        self.warn.append(message)

    def add_fail(self, message: str) -> None:
        self.fail.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def repo_path(path_text: str) -> Path:
    return ROOT / path_text.replace("/", "\\")


def parse_benchmark_rows() -> list[dict[str, str]]:
    benchmark = read_text(ROOT / "BENCHMARK.md")
    rows: list[dict[str, str]] = []
    for line in benchmark.splitlines():
        if not re.match(r"^\| B\d+ \|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 8:
            raise ValueError(f"Malformed BENCHMARK row: {line}")
        rows.append(
            {
                "id": cells[0],
                "area": cells[1],
                "source": cells[2],
                "raw": cells[3],
                "dianoia": cells[4],
                "verdict": cells[5],
                "tokens": cells[6],
                "artifacts": cells[7],
            }
        )
    return rows


def manifest_field(text: str, name: str) -> str:
    pattern = re.compile(rf"^{re.escape(name)}:\s*(.*)$", re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def section_body(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)",
        re.MULTILINE,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def weak_blank(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in {"", "none", "n/a", "na", "no", "unknown", "tbd"}


def check_benchmarks(result: CheckResult) -> None:
    try:
        rows = parse_benchmark_rows()
    except Exception as exc:  # noqa: BLE001 - this is a CLI verifier
        result.add_fail(f"BENCHMARK.md parse failed: {exc}")
        return

    value_added = [row for row in rows if row["verdict"] == "VALUE_ADDED"]
    areas = sorted({row["area"] for row in value_added})
    if len(value_added) >= 5 and len(areas) >= 3:
        result.add_ok(
            f"benchmark rows: {len(value_added)} VALUE_ADDED across {len(areas)} areas"
        )
    else:
        result.add_fail(
            f"benchmark rows insufficient: {len(value_added)} VALUE_ADDED across {len(areas)} areas"
        )

    for row in rows:
        bid = row["id"]
        source = ROOT / "benchmark-bank" / bid / "SOURCE.md"
        comparison = ROOT / "benchmark-bank" / bid / "COMPARISON.md"
        run_manifest = ROOT / "benchmark-bank" / bid / "RUN.md"
        if not source.exists():
            result.add_fail(f"{bid}: missing {source.relative_to(ROOT)}")
            continue
        if not comparison.exists():
            result.add_fail(f"{bid}: missing {comparison.relative_to(ROOT)}")
            continue

        source_text = read_text(source)
        comparison_text = read_text(comparison)
        for required in ("## Metadata", "## Modification", "## Area", "## Artifacts"):
            if required not in source_text:
                result.add_fail(f"{bid}: SOURCE.md missing {required}")
        if "VALUE_ADDED" in row["verdict"] and "## Three Differences" not in comparison_text:
            result.add_fail(f"{bid}: VALUE_ADDED comparison missing Three Differences")
        if int(bid[1:]) >= 6:
            if not run_manifest.exists():
                result.add_fail(f"{bid}: B6+ benchmark missing RUN.md")
            else:
                run_text = read_text(run_manifest)
                for required in (
                    "benchmark_id",
                    "run_class",
                    "## Freshness Protocol",
                    "## Subagent Fire Audit",
                    "## Reviewer Fire Audit",
                    "## Token Accounting",
                ):
                    if required not in run_text:
                        result.add_fail(f"{bid}: RUN.md missing {required}")
                run_class = manifest_field(run_text, "run_class")
                if run_class not in {"full-fresh", "controlled-comparison"}:
                    result.add_fail(
                        f"{bid}: run_class must be full-fresh or controlled-comparison"
                    )
                if run_class == "controlled-comparison":
                    weaknesses = section_body(run_text, "Known Weaknesses")
                    if weak_blank(weaknesses):
                        result.add_fail(
                            f"{bid}: controlled-comparison must name a concrete known weakness"
                        )
                token_section = section_body(run_text, "Token Accounting")
                for label in ("Method:", "Raw tokens:", "Dianoia tokens:", "Uncertainty:"):
                    if label not in token_section:
                        result.add_fail(f"{bid}: RUN.md Token Accounting missing {label}")
        if "UNVERIFIED" in row["tokens"]:
            result.add_warn(f"{bid}: token accounting is UNVERIFIED")


def check_skills(result: CheckResult) -> None:
    skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    subagent_text = "\n".join(
        read_text(path) for path in sorted((ROOT / "prompts" / "subagents").glob("*.md"))
    )
    if len(skill_paths) >= 5:
        result.add_ok(f"skills: {len(skill_paths)} SKILL.md files")
    else:
        result.add_fail(f"skills: only {len(skill_paths)} SKILL.md files")

    for path in skill_paths:
        rel = path.relative_to(ROOT).as_posix()
        if rel in subagent_text:
            result.add_ok(f"skill referenced: {rel}")
        else:
            result.add_fail(f"skill not referenced by subagent prompt: {rel}")


def check_connectors(result: CheckResult) -> None:
    subagent_text = "\n".join(
        read_text(path) for path in sorted((ROOT / "prompts" / "subagents").glob("*.md"))
    )
    connector_dirs = sorted(path for path in (ROOT / "connectors").iterdir() if path.is_dir())
    working = 0
    for directory in connector_dirs:
        rel = directory.relative_to(ROOT).as_posix()
        required = [directory / "README.md", directory / "server.py", directory / "example.md"]
        missing = [path.name for path in required if not path.exists()]
        server_ref = f"{rel}/server.py"
        if missing:
            result.add_fail(f"connector {rel}: missing {', '.join(missing)}")
            continue
        if server_ref not in subagent_text:
            result.add_fail(f"connector {rel}: server not referenced by subagent prompt")
            continue
        working += 1
        result.add_ok(f"connector wired: {rel}")

    if working < 2:
        result.add_fail(f"connectors: only {working} wired connectors")


def check_docs(result: CheckResult) -> None:
    required_files = ["README.md", "ARCHITECTURE.md", "EXAMPLES.md", "CHANGELOG.md", "ROADMAP.md", "NEXT_SESSION.md"]
    for name in required_files:
        if not (ROOT / name).exists():
            result.add_fail(f"missing doc/state file: {name}")
    readme = read_text(ROOT / "README.md")
    architecture = read_text(ROOT / "ARCHITECTURE.md")
    roadmap = read_text(ROOT / "ROADMAP.md")
    for needle in ("5 accepted controlled comparisons", "baseline rather than a terminal"):
        if needle not in readme:
            result.add_fail(f"README.md missing current-state phrase: {needle}")
    for needle in ("Phase Loop", "Meaningfulness Gate", "Subagent Flow"):
        if needle not in architecture:
            result.add_fail(f"ARCHITECTURE.md missing section: {needle}")
    if "Continuous Improvement Track" not in roadmap:
        result.add_fail("ROADMAP.md missing Continuous Improvement Track")
    if not (ROOT / "benchmark-bank" / "RUNBOOK.md").exists():
        result.add_fail("benchmark-bank/RUNBOOK.md missing")
    if not (ROOT / "templates" / "benchmark_case" / "RUN.md").exists():
        result.add_fail("templates/benchmark_case/RUN.md missing")
    if not result.fail:
        result.add_ok("docs/state files contain current continuous-improvement baseline")


def main() -> int:
    result = CheckResult(ok=[], warn=[], fail=[])
    check_benchmarks(result)
    check_skills(result)
    check_connectors(result)
    check_docs(result)

    for message in result.ok:
        print(f"OK {message}")
    for message in result.warn:
        print(f"WARN {message}")
    for message in result.fail:
        print(f"FAIL {message}")

    print(
        f"SUMMARY ok={len(result.ok)} warn={len(result.warn)} fail={len(result.fail)}"
    )
    return 1 if result.fail else 0


if __name__ == "__main__":
    sys.exit(main())
