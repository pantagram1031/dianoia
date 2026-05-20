#!/usr/bin/env python3
"""Small Lean formal-check wrapper for dianoia research gates."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def lean_path() -> str:
    return shutil.which("lean") or ""


def env(_: argparse.Namespace) -> dict[str, object]:
    path = lean_path()
    if not path:
        return {
            "status": "UNAVAILABLE",
            "lean_path": "",
            "message": "Lean executable not found on PATH.",
        }
    completed = subprocess.run(
        [path, "--version"],
        check=False,
        text=True,
        capture_output=True,
    )
    return {
        "status": "OK" if completed.returncode == 0 else "ERROR",
        "lean_path": path,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def check(args: argparse.Namespace) -> dict[str, object]:
    path = lean_path()
    target = Path(args.file)
    if not target.exists():
        return {
            "status": "ERROR",
            "file": str(target),
            "message": "Lean file does not exist.",
        }
    if not path:
        return {
            "status": "UNVERIFIED",
            "file": str(target),
            "lean_path": "",
            "message": "Lean executable not found on PATH; formal check not run.",
        }
    completed = subprocess.run(
        [path, str(target)],
        check=False,
        text=True,
        capture_output=True,
        timeout=args.timeout,
    )
    return {
        "status": "VERIFIED" if completed.returncode == 0 else "FAILED",
        "file": str(target),
        "lean_path": path,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Run local Lean checks as compact JSON.")
    sub = parser.add_subparsers(dest="command", required=True)

    env_parser = sub.add_parser("env", help="Report Lean executable availability")
    env_parser.set_defaults(func=env)

    check_parser = sub.add_parser("check", help="Check one Lean file")
    check_parser.add_argument("file")
    check_parser.add_argument("--timeout", type=int, default=30)
    check_parser.set_defaults(func=check)

    args = parser.parse_args(argv)
    print(json.dumps(args.func(args), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
