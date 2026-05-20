#!/usr/bin/env python3
"""Verify connector wrappers have offline contracts and subagent wiring."""

from __future__ import annotations

import py_compile
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


def connector_dirs(root: Path) -> list[Path]:
    base = root / "connectors"
    if not base.exists():
        return []
    return sorted(path for path in base.iterdir() if path.is_dir())


def check_server_contract(result: CheckResult, relative: str, server: Path) -> None:
    try:
        py_compile.compile(str(server), doraise=True)
    except py_compile.PyCompileError as exc:
        result.add_fail(f"{relative} does not compile: {exc.msg}")
        return

    text = read_text(server)
    required = {
        "argparse": "argparse" in text,
        "json.dumps": "json.dumps" in text,
        "search subcommand": "add_parser(\"search\"" in text or "add_parser('search'" in text,
        "fetch subcommand": "add_parser(\"fetch\"" in text or "add_parser('fetch'" in text,
        "User-Agent": "User-Agent" in text,
    }
    missing = [label for label, present in required.items() if not present]
    if missing:
        result.add_fail(f"{relative} missing server contract phrases: " + "; ".join(missing))
    else:
        result.add_ok(f"{relative} exposes search/fetch JSON CLI contract")


def check_connectors(root: Path = ROOT) -> CheckResult:
    result = CheckResult(ok=[], fail=[])
    dirs = connector_dirs(root)
    if len(dirs) < 2:
        result.add_fail(f"expected at least 2 connector directories, found {len(dirs)}")

    researcher_path = root / "prompts" / "subagents" / "researcher.md"
    if not researcher_path.exists():
        result.add_fail(f"missing prompts/subagents/researcher.md: {researcher_path}")
        researcher = ""
    else:
        researcher = read_text(researcher_path)

    for directory in dirs:
        name = directory.name
        for filename in ("README.md", "example.md", "server.py"):
            path = directory / filename
            relative = f"connectors/{name}/{filename}"
            if path.exists():
                result.add_ok(f"{relative} exists")
            else:
                result.add_fail(f"missing {relative}")

        server = directory / "server.py"
        if server.exists():
            check_server_contract(result, f"connectors/{name}/server.py", server)

        invocation = f"connectors/{name}/server.py"
        if invocation in researcher and "invoke" in researcher.lower():
            result.add_ok(f"researcher.md invokes {invocation}")
        else:
            result.add_fail(f"researcher.md missing {invocation} invocation")

    return result


def main() -> int:
    result = check_connectors(ROOT)
    for message in result.ok:
        print(f"OK {message}")
    for message in result.fail:
        print(f"FAIL {message}")
    print(f"SUMMARY ok={len(result.ok)} fail={len(result.fail)}")
    return 1 if result.fail else 0


if __name__ == "__main__":
    sys.exit(main())
