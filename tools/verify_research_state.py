#!/usr/bin/env python3
"""Verify RESEARCH_CONTRIBUTION state scaffolding.

This verifier checks the repo-level evidence that keeps P9-P13 honest. It does
not judge mathematics; it fails missing gates, stale scaffolding, and unwired
research infrastructure before a session can drift into unsupported claims.
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


@dataclass
class ResearchBankStats:
    open_verified: int
    open_verified_areas: set[str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require_file(result: CheckResult, root: Path, relative: str) -> str:
    path = root / relative
    if not path.exists():
        result.add_fail(f"missing {relative}")
        return ""
    result.add_ok(f"{relative} exists")
    return read_text(path)


def table_header_cells(text: str) -> list[str]:
    for line in text.splitlines():
        if line.startswith("|") and "---" not in line:
            return [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
    return []


def markdown_table_rows(text: str) -> list[dict[str, str]]:
    lines = [line for line in text.splitlines() if line.startswith("|")]
    if len(lines) < 2:
        return []
    headers = [cell.strip().lower() for cell in lines[0].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells, strict=True)))
    return rows


def research_bank_stats(index_text: str) -> ResearchBankStats:
    open_verified = 0
    areas: set[str] = set()
    for row in markdown_table_rows(index_text):
        status = row.get("status", "").upper()
        openness = row.get("openness verified date", "").upper()
        if "OPEN-VERIFIED" in status and "OPEN-WEAK" not in status and "OPEN-WEAK" not in openness:
            open_verified += 1
            area = row.get("area", "").strip()
            if area:
                areas.add(area)
    return ResearchBankStats(open_verified=open_verified, open_verified_areas=areas)


def simple_field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def check_phase_state(result: CheckResult, root: Path) -> None:
    roadmap = require_file(result, root, "ROADMAP.md")
    if not roadmap:
        return
    for phase in ("9", "10", "11", "12", "13"):
        if not re.search(rf"\|\s*{phase}\s*\|", roadmap):
            result.add_fail(f"ROADMAP.md missing phase {phase} row")
    for phrase in (
        "Research Contribution Track",
        "RESEARCH_CONTRIBUTION",
        "P9 infra",
        "P10 curation",
        "P11 attempts",
        "P12 verification",
        "P13 notes",
    ):
        if phrase not in roadmap:
            result.add_fail(f"ROADMAP.md missing research phrase: {phrase}")
    if "RESEARCH INFRA" in roadmap and ("IN_PROGRESS" in roadmap or "COMPLETE" in roadmap):
        result.add_ok("ROADMAP.md records research infrastructure phase state")


def check_state_files(result: CheckResult, root: Path) -> None:
    research_log = require_file(result, root, "RESEARCH_LOG.md")
    claims = require_file(result, root, "CLAIMS.md")
    bank_readme = require_file(result, root, "research-bank/README.md")
    bank_index = require_file(result, root, "research-bank/INDEX.md")

    if research_log:
        for phrase in ("RESEARCH_CONTRIBUTION", "formal-check", "openness-verification", "adversarial-novelty"):
            if phrase not in research_log:
                result.add_fail(f"RESEARCH_LOG.md missing phrase: {phrase}")

    if claims:
        expected = [
            "id",
            "date",
            "claim",
            "type",
            "openness trail",
            "adversarial summary",
            "formal/computational evidence",
            "confidence 1-10",
            "status",
        ]
        cells = table_header_cells(claims)
        missing = [cell for cell in expected if cell not in cells]
        if missing:
            result.add_fail("CLAIMS.md missing columns: " + ", ".join(missing))
        for status in (
            "CANDIDATE",
            "PARTIAL-PROGRESS",
            "OBSTRUCTION-FOUND",
            "SOLVED-CLAIM-PENDING-GATES",
            "DOWNGRADED",
            "BLOCKED-EXTERNAL-REVIEW",
        ):
            if status not in claims:
                result.add_fail(f"CLAIMS.md missing status value: {status}")

    for text, name in ((bank_readme, "research-bank/README.md"), (bank_index, "research-bank/INDEX.md")):
        if not text:
            continue
        for column in (
            "id",
            "source",
            "area",
            "openness verified date",
            "tractability rank",
            "why dianoia adds value",
            "status",
        ):
            if column not in table_header_cells(text):
                result.add_fail(f"{name} missing research-bank column: {column}")
    if bank_index:
        stats = research_bank_stats(bank_index)
        result.add_ok(
            f"P10 progress: {stats.open_verified} OPEN-VERIFIED candidates across "
            f"{len(stats.open_verified_areas)} areas"
        )


def check_infra_wiring(result: CheckResult, root: Path) -> None:
    researcher = require_file(result, root, "prompts/subagents/researcher.md")
    arxiv = require_file(result, root, "connectors/arxiv/server.py")
    lean = require_file(result, root, "connectors/lean/server.py")
    openness_skill = require_file(result, root, "skills/openness-verification/SKILL.md")
    novelty_skill = require_file(result, root, "skills/adversarial-novelty-check/SKILL.md")

    if arxiv:
        for phrase in ("openness", "--from-date", "--to-date", "submittedDate"):
            if phrase not in arxiv:
                result.add_fail(f"connectors/arxiv/server.py missing {phrase}")
    if lean:
        for phrase in ("env", "check", "UNVERIFIED"):
            if phrase not in lean:
                result.add_fail(f"connectors/lean/server.py missing {phrase}")
    if researcher:
        for reference in (
            "connectors/arxiv/server.py openness",
            "connectors/lean/server.py",
            "skills/openness-verification/SKILL.md",
            "skills/adversarial-novelty-check/SKILL.md",
        ):
            if reference not in researcher:
                result.add_fail(f"researcher.md missing research wiring: {reference}")
    for skill_text, skill_name in (
        (openness_skill, "skills/openness-verification/SKILL.md"),
        (novelty_skill, "skills/adversarial-novelty-check/SKILL.md"),
    ):
        if skill_text and "## When To Use" in skill_text and "## Procedure" in skill_text:
            result.add_ok(f"{skill_name} has skill structure")
        elif skill_text:
            result.add_fail(f"{skill_name} missing skill structure")


def check_candidate_dirs(result: CheckResult, root: Path) -> None:
    bank = root / "research-bank"
    if not bank.exists():
        result.add_fail("missing research-bank directory")
        return
    candidates = [
        path for path in sorted(bank.iterdir())
        if path.is_dir() and not path.name.startswith(".")
    ]
    if not candidates:
        result.add_warn("research-bank has no promoted candidates yet")
        return
    for candidate in candidates:
        for filename in ("SOURCE.md", "OPENNESS.md", "TRACTABILITY.md", "log.md"):
            if not (candidate / filename).exists():
                result.add_fail(f"research candidate {candidate.name} missing {filename}")

    index_path = bank / "INDEX.md"
    if not index_path.exists():
        return
    for row in markdown_table_rows(read_text(index_path)):
        candidate_id = row.get("id", "").strip()
        if not candidate_id:
            continue
        row_status = row.get("status", "").upper()
        openness_path = bank / candidate_id / "OPENNESS.md"
        if "OPEN-VERIFIED" not in row_status or not openness_path.exists():
            continue
        openness_status = simple_field(read_text(openness_path), "status")
        if openness_status != "OPEN-VERIFIED":
            result.add_fail(
                f"{candidate_id} index says OPEN-VERIFIED but OPENNESS.md status is "
                f"{openness_status or 'MISSING'}"
            )


def check_templates(result: CheckResult, root: Path) -> None:
    template_dir = root / "templates" / "research_candidate"
    required = ("SOURCE.md", "OPENNESS.md", "TRACTABILITY.md", "log.md", "NOVELTY.md", "CLAIM_GATE.md")
    for filename in required:
        path = template_dir / filename
        if not path.exists():
            result.add_fail(f"missing templates/research_candidate/{filename}")
            continue
        text = read_text(path)
        if "candidate_id" not in text and filename != "SOURCE.md":
            result.add_fail(f"templates/research_candidate/{filename} missing candidate_id field")
    if all((template_dir / filename).exists() for filename in required):
        result.add_ok("research candidate templates exist")


def check_research_state(root: Path = ROOT) -> CheckResult:
    result = CheckResult(ok=[], warn=[], fail=[])
    check_phase_state(result, root)
    check_state_files(result, root)
    check_infra_wiring(result, root)
    check_candidate_dirs(result, root)
    check_templates(result, root)
    return result


def main() -> int:
    result = check_research_state(ROOT)
    for message in result.ok:
        print(f"OK {message}")
    for message in result.warn:
        print(f"WARN {message}")
    for message in result.fail:
        print(f"FAIL {message}")
    print(f"SUMMARY ok={len(result.ok)} warn={len(result.warn)} fail={len(result.fail)}")
    return 1 if result.fail else 0


if __name__ == "__main__":
    sys.exit(main())
