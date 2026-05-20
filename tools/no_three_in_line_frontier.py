#!/usr/bin/env python3
"""Extract and replay published no-three-in-line frontier certificates."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Sequence

import no_three_in_line_verify as nti


TABLE_ENTRY_RE = re.compile(r"\bN\s*=\s*(\d+)\s*:\s*(\[.*?\])(?=\s*N\s*=|\s*$)", re.DOTALL)


def extract_table_entries(text: str) -> dict[int, list[nti.Point]]:
    entries: dict[int, list[nti.Point]] = {}
    for match in TABLE_ENTRY_RE.finditer(text):
        n = int(match.group(1))
        points = nti.coerce_points(ast.literal_eval(match.group(2)))
        if n in entries:
            raise ValueError(f"duplicate N={n} entry")
        entries[n] = points
    if not entries:
        raise ValueError("no `N=k: [...]` entries found")
    return dict(sorted(entries.items()))


def certificate_payload(
    n: int,
    points: Sequence[nti.Point],
    *,
    source_url: str,
    source_sha256: str,
    retrieved_date: str,
) -> dict[str, object]:
    return {
        "n": n,
        "points": [list(point) for point in points],
        "source": {
            "url": source_url,
            "paper": (
                "Thomas Prellberg, Constraint Satisfaction Programming for the "
                "No-three-in-line Problem, arXiv:2602.07751"
            ),
            "source_sha256": source_sha256,
            "entry": f"N={n} from Table 1.txt",
            "retrieved_date": retrieved_date,
        },
    }


def certificate_path(output_dir: Path, n: int) -> Path:
    return output_dir / f"prellberg-n{n}.json"


def verify_certificate(path: Path) -> nti.VerificationResult:
    n, points = nti.load_certificate(path, explicit_n=None)
    return nti.verify_points(
        n,
        points,
        require_2n=True,
        require_two_per_row=True,
        require_two_per_column=True,
    )


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def extract_command(args: argparse.Namespace) -> int:
    table_text = args.table.read_text(encoding="utf-8")
    source_sha256 = hashlib.sha256(table_text.encode("utf-8")).hexdigest()
    entries = extract_table_entries(table_text)
    summary: list[dict[str, object]] = []

    for n, points in entries.items():
        cert_path = certificate_path(args.output_dir, n)
        write_json(
            cert_path,
            certificate_payload(
                n,
                points,
                source_url=args.source_url,
                source_sha256=source_sha256,
                retrieved_date=args.retrieved_date,
            ),
        )
        result = verify_certificate(cert_path)
        verify_path = cert_path.with_suffix(".verify.json")
        write_json(verify_path, nti.result_payload(result))
        summary.append(
            {
                "n": n,
                "certificate": cert_path.as_posix(),
                "verification": verify_path.as_posix(),
                "ok": result.ok,
                "point_count": result.point_count,
            }
        )

    summary_path = args.output_dir / "prellberg-frontier-summary.json"
    write_json(
        summary_path,
        {
            "ok": all(item["ok"] for item in summary),
            "source_sha256": source_sha256,
            "certificates": summary,
        },
    )
    print(json.dumps(json.loads(summary_path.read_text(encoding="utf-8")), indent=2, sort_keys=True))
    return 0 if all(item["ok"] for item in summary) else 1


def verify_dir_command(args: argparse.Namespace) -> int:
    certificate_paths = sorted(args.certificate_dir.glob(args.pattern))
    certificate_paths = [path for path in certificate_paths if ".verify" not in path.name]
    if not certificate_paths:
        print(json.dumps({"ok": False, "error": "no certificates found"}, indent=2))
        return 1

    summary: list[dict[str, object]] = []
    for path in certificate_paths:
        result = verify_certificate(path)
        summary.append(
            {
                "certificate": path.as_posix(),
                "ok": result.ok,
                "grid_size": result.grid_size,
                "point_count": result.point_count,
                "errors": result.errors,
            }
        )
    payload = {"ok": all(item["ok"] for item in summary), "certificates": summary}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["ok"] else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract_parser = subparsers.add_parser("extract")
    extract_parser.add_argument("table", type=Path)
    extract_parser.add_argument("--output-dir", type=Path, required=True)
    extract_parser.add_argument("--source-url", required=True)
    extract_parser.add_argument("--retrieved-date", required=True)
    extract_parser.set_defaults(func=extract_command)

    verify_parser = subparsers.add_parser("verify-dir")
    verify_parser.add_argument("certificate_dir", type=Path)
    verify_parser.add_argument("--pattern", default="prellberg-n*.json")
    verify_parser.set_defaults(func=verify_dir_command)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
