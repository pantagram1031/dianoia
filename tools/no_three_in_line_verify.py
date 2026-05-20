#!/usr/bin/env python3
"""Verify finite no-three-in-line grid certificates.

The checker is intentionally independent of any search solver.  It accepts a
grid size and a finite set of integer grid points, then verifies bounds,
duplicates, optional 2n cardinality, optional two-per-row/column occupancy, and
the core no-three-collinear condition.
"""

from __future__ import annotations

import argparse
import ast
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence


Point = tuple[int, int]
LineKey = tuple[int, int, int]


@dataclass
class VerificationResult:
    grid_size: int
    point_count: int
    ok: bool = True
    errors: list[str] = field(default_factory=list)
    line_violations: list[tuple[LineKey, list[Point]]] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        self.ok = False
        self.errors.append(message)


def normalize_line(p: Point, q: Point) -> LineKey:
    """Return a canonical integer key for the line through two distinct points."""
    (x1, y1), (x2, y2) = p, q
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    if g:
        a //= g
        b //= g
        c //= g
    for value in (a, b, c):
        if value < 0:
            return (-a, -b, -c)
        if value > 0:
            return (a, b, c)
    return (a, b, c)


def coerce_points(raw_points: Iterable[Sequence[int]]) -> list[Point]:
    points: list[Point] = []
    for index, raw in enumerate(raw_points):
        if len(raw) != 2:
            raise ValueError(f"point {index} is not a pair: {raw!r}")
        x, y = raw
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError(f"point {index} has non-integer coordinate: {raw!r}")
        points.append((x, y))
    return points


def parse_certificate_text(text: str) -> tuple[int | None, list[Point]]:
    """Parse JSON, a Python literal point list, or a single `N=k: [...]` entry."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("empty certificate")

    try:
        data = json.loads(stripped)
    except json.JSONDecodeError:
        data = None
    if isinstance(data, dict):
        n = data.get("n", data.get("grid_size"))
        points = data.get("points")
        if not isinstance(n, int):
            raise ValueError("JSON certificate requires integer `n` or `grid_size`")
        if not isinstance(points, list):
            raise ValueError("JSON certificate requires list `points`")
        return n, coerce_points(points)
    if isinstance(data, list):
        return None, coerce_points(data)

    match = re.search(r"\bN\s*=\s*(\d+)\s*:\s*(\[.*\])\s*$", stripped, re.DOTALL)
    if match:
        n = int(match.group(1))
        return n, coerce_points(ast.literal_eval(match.group(2)))

    literal = ast.literal_eval(stripped)
    if isinstance(literal, list):
        return None, coerce_points(literal)
    raise ValueError("certificate must be JSON, a point list, or `N=k: [...]`")


def verify_points(
    grid_size: int,
    points: Sequence[Point],
    *,
    require_2n: bool = False,
    require_two_per_row: bool = False,
    require_two_per_column: bool = False,
    max_reported_violations: int = 5,
) -> VerificationResult:
    result = VerificationResult(grid_size=grid_size, point_count=len(points))

    if grid_size <= 0:
        result.add_error(f"grid_size must be positive, got {grid_size}")
        return result

    seen: set[Point] = set()
    for point in points:
        x, y = point
        if not (0 <= x < grid_size and 0 <= y < grid_size):
            result.add_error(f"point outside {grid_size}x{grid_size} grid: {point}")
        if point in seen:
            result.add_error(f"duplicate point: {point}")
        seen.add(point)

    if require_2n and len(points) != 2 * grid_size:
        result.add_error(f"expected 2n={2 * grid_size} points, got {len(points)}")

    if require_two_per_row:
        row_counts = [0] * grid_size
        for _, y in points:
            if 0 <= y < grid_size:
                row_counts[y] += 1
        bad_rows = [(row, count) for row, count in enumerate(row_counts) if count != 2]
        if bad_rows:
            result.add_error(f"rows without exactly 2 points: {bad_rows[:10]}")

    if require_two_per_column:
        column_counts = [0] * grid_size
        for x, _ in points:
            if 0 <= x < grid_size:
                column_counts[x] += 1
        bad_columns = [
            (column, count) for column, count in enumerate(column_counts) if count != 2
        ]
        if bad_columns:
            result.add_error(f"columns without exactly 2 points: {bad_columns[:10]}")

    lines: dict[LineKey, set[Point]] = {}
    reported_lines: set[LineKey] = set()
    unique_points = sorted(seen)
    for i, p in enumerate(unique_points):
        for q in unique_points[i + 1 :]:
            key = normalize_line(p, q)
            bucket = lines.setdefault(key, set())
            bucket.add(p)
            bucket.add(q)
            if (
                len(bucket) >= 3
                and key not in reported_lines
                and len(result.line_violations) < max_reported_violations
            ):
                result.line_violations.append((key, sorted(bucket)))
                reported_lines.add(key)

    if result.line_violations:
        result.ok = False
        result.errors.append(
            f"found {sum(1 for pts_on_line in lines.values() if len(pts_on_line) > 2)} "
            "lines containing at least 3 selected points"
        )

    return result


def load_certificate(path: Path, explicit_n: int | None) -> tuple[int, list[Point]]:
    parsed_n, points = parse_certificate_text(path.read_text(encoding="utf-8"))
    n = explicit_n if explicit_n is not None else parsed_n
    if n is None:
        raise ValueError("grid size must be provided by --n or the certificate")
    return n, points


def result_payload(result: VerificationResult) -> dict[str, object]:
    return {
        "ok": result.ok,
        "grid_size": result.grid_size,
        "point_count": result.point_count,
        "errors": result.errors,
        "line_violations": [
            {"line": list(line), "points": [list(point) for point in points]}
            for line, points in result.line_violations
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int, help="grid size, if not stored in the certificate")
    parser.add_argument("--require-2n", action="store_true")
    parser.add_argument("--require-two-per-row", action="store_true")
    parser.add_argument("--require-two-per-column", action="store_true")
    args = parser.parse_args(argv)

    n, points = load_certificate(args.certificate, args.n)
    result = verify_points(
        n,
        points,
        require_2n=args.require_2n,
        require_two_per_row=args.require_two_per_row,
        require_two_per_column=args.require_two_per_column,
    )
    print(json.dumps(result_payload(result), indent=2, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
