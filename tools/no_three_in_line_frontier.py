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


FLAMMENKAMP_ALPHABET = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    "#$%&@?!()[]<>{}=*+|-/~^_:;,."
)
FLAMMENKAMP_SYMMETRIES = {
    ".": "iden",
    ":": "rot2",
    "/": "dia1",
    "-": "ort1",
    "o": "rot4",
    "c": "rct4",
    "x": "dia2",
    "+": "ort2",
    "*": "full",
}
TABLE_ENTRY_RE = re.compile(
    r"\bN\s*=\s*(\d+)\s*:\s*(\[.*?\])(?=\s*N\s*=|\s*Configurations\b|\s*$)",
    re.DOTALL,
)


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


def flammenkamp_certificate_path(output_dir: Path, n: int) -> Path:
    return output_dir / f"flammenkamp-n{n}.json"


def decode_flammenkamp_configuration(line: str, n: int) -> tuple[str, list[nti.Point]]:
    """Decode one Flammenkamp standard-notation configuration line.

    The first character records the symmetry class.  The remaining characters
    are column positions for selected markers, ordered row by row from top to
    bottom and left to right.  A full 2n-point solution therefore has exactly
    two encoded column characters for each row.
    """
    encoded = line.strip()
    expected_length = 1 + 2 * n
    if len(encoded) != expected_length:
        raise ValueError(
            f"Flammenkamp line for n={n} must have length {expected_length}, "
            f"got {len(encoded)}"
        )
    symmetry = encoded[0]
    if symmetry not in FLAMMENKAMP_SYMMETRIES:
        raise ValueError(f"unknown Flammenkamp symmetry marker: {symmetry!r}")

    points: list[nti.Point] = []
    for row in range(n):
        for offset in (0, 1):
            char = encoded[1 + 2 * row + offset]
            try:
                column = FLAMMENKAMP_ALPHABET.index(char)
            except ValueError as exc:
                raise ValueError(f"unknown Flammenkamp coordinate character: {char!r}") from exc
            if column >= n:
                raise ValueError(
                    f"encoded column {column} from {char!r} is outside n={n}"
                )
            points.append((column, row))
    return symmetry, points


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


def flammenkamp_payload(
    n: int,
    points: Sequence[nti.Point],
    *,
    symmetry: str,
    source_url: str,
    source_sha256: str,
    retrieved_date: str,
    line_index: int,
) -> dict[str, object]:
    return {
        "n": n,
        "points": [list(point) for point in points],
        "source": {
            "url": source_url,
            "paper": "Achim Flammenkamp, The No-Three-in-Line Problem",
            "source_sha256": source_sha256,
            "entry": (
                f"line {line_index}; symmetry marker {symmetry!r} "
                f"({FLAMMENKAMP_SYMMETRIES[symmetry]})"
            ),
            "retrieved_date": retrieved_date,
        },
    }


def flammenkamp_command(args: argparse.Namespace) -> int:
    encoded_bytes = args.encoded_file.read_bytes()
    source_sha256 = hashlib.sha256(encoded_bytes).hexdigest()
    lines = [line.strip() for line in encoded_bytes.decode("ascii").splitlines() if line.strip()]
    if args.line_index < 1 or args.line_index > len(lines):
        raise ValueError(
            f"line-index must be in [1, {len(lines)}], got {args.line_index}"
        )

    symmetry, points = decode_flammenkamp_configuration(lines[args.line_index - 1], args.n)
    cert_path = flammenkamp_certificate_path(args.output_dir, args.n)
    write_json(
        cert_path,
        flammenkamp_payload(
            args.n,
            points,
            symmetry=symmetry,
            source_url=args.source_url,
            source_sha256=source_sha256,
            retrieved_date=args.retrieved_date,
            line_index=args.line_index,
        ),
    )
    result = verify_certificate(cert_path)
    verify_path = cert_path.with_suffix(".verify.json")
    write_json(verify_path, nti.result_payload(result))
    payload = {
        "ok": result.ok,
        "certificate": cert_path.as_posix(),
        "verification": verify_path.as_posix(),
        "grid_size": result.grid_size,
        "point_count": result.point_count,
        "source_sha256": source_sha256,
        "line_index": args.line_index,
        "symmetry": FLAMMENKAMP_SYMMETRIES[symmetry],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if result.ok else 1


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

    flammenkamp_parser = subparsers.add_parser("flammenkamp")
    flammenkamp_parser.add_argument("encoded_file", type=Path)
    flammenkamp_parser.add_argument("--n", type=int, required=True)
    flammenkamp_parser.add_argument("--output-dir", type=Path, required=True)
    flammenkamp_parser.add_argument("--source-url", required=True)
    flammenkamp_parser.add_argument("--retrieved-date", required=True)
    flammenkamp_parser.add_argument("--line-index", type=int, default=1)
    flammenkamp_parser.set_defaults(func=flammenkamp_command)

    verify_parser = subparsers.add_parser("verify-dir")
    verify_parser.add_argument("certificate_dir", type=Path)
    verify_parser.add_argument("--pattern", default="*-n*.json")
    verify_parser.set_defaults(func=verify_dir_command)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
