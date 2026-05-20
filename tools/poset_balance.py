#!/usr/bin/env python3
"""Exact linear-extension checks for finite poset balancing experiments."""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from pathlib import Path
from typing import Iterable, Sequence


Relation = tuple[int, int]


@dataclass(frozen=True)
class Poset:
    n: int
    less: frozenset[Relation]

    def covers_mask(self) -> tuple[int, ...]:
        prerequisites = [0] * self.n
        for lower, upper in self.less:
            prerequisites[upper] |= 1 << lower
        return tuple(prerequisites)

    def incomparable_pairs(self) -> list[Relation]:
        pairs: list[Relation] = []
        for x in range(self.n):
            for y in range(x + 1, self.n):
                if (x, y) not in self.less and (y, x) not in self.less:
                    pairs.append((x, y))
        return pairs

    def comparable(self, x: int, y: int) -> bool:
        return x == y or (x, y) in self.less or (y, x) in self.less


def transitive_closure(n: int, relations: Iterable[Relation]) -> frozenset[Relation]:
    reach = [[False] * n for _ in range(n)]
    for lower, upper in relations:
        if not (0 <= lower < n and 0 <= upper < n):
            raise ValueError(f"relation outside {n}-element poset: {(lower, upper)}")
        if lower == upper:
            raise ValueError(f"reflexive relation is not allowed: {(lower, upper)}")
        reach[lower][upper] = True

    for mid in range(n):
        for lower in range(n):
            if reach[lower][mid]:
                for upper in range(n):
                    reach[lower][upper] = reach[lower][upper] or reach[mid][upper]

    for item in range(n):
        if reach[item][item]:
            raise ValueError("relations contain a cycle")

    return frozenset(
        (lower, upper)
        for lower in range(n)
        for upper in range(n)
        if reach[lower][upper]
    )


def make_poset(n: int, relations: Iterable[Sequence[int]]) -> Poset:
    return Poset(n=n, less=transitive_closure(n, (tuple(pair) for pair in relations)))


def count_linear_extensions(poset: Poset) -> int:
    prerequisites = poset.covers_mask()
    full = (1 << poset.n) - 1

    @cache
    def count(placed: int) -> int:
        if placed == full:
            return 1
        total = 0
        for item in range(poset.n):
            bit = 1 << item
            if placed & bit:
                continue
            if prerequisites[item] & ~placed:
                continue
            total += count(placed | bit)
        return total

    return count(0)


def count_extensions_with_order(poset: Poset, before: int, after: int) -> int:
    prerequisites = poset.covers_mask()
    full = (1 << poset.n) - 1

    @cache
    def count(placed: int) -> int:
        if placed & (1 << after) and not placed & (1 << before):
            return 0
        if placed == full:
            return 1
        total = 0
        for item in range(poset.n):
            bit = 1 << item
            if placed & bit:
                continue
            if prerequisites[item] & ~placed:
                continue
            total += count(placed | bit)
        return total

    return count(0)


def width(poset: Poset) -> int:
    best = 0
    for mask in range(1, 1 << poset.n):
        items = [index for index in range(poset.n) if mask & (1 << index)]
        if len(items) <= best:
            continue
        if all(not poset.comparable(x, y) for x, y in itertools.combinations(items, 2)):
            best = len(items)
    return best


def height(poset: Poset) -> int:
    memo: dict[int, int] = {}

    def chain_from(item: int) -> int:
        if item not in memo:
            memo[item] = 1 + max(
                (chain_from(upper) for lower, upper in poset.less if lower == item),
                default=0,
            )
        return memo[item]

    return max((chain_from(item) for item in range(poset.n)), default=0)


def covers(poset: Poset) -> frozenset[Relation]:
    cover_relations: set[Relation] = set()
    for lower, upper in poset.less:
        if not any(
            (lower, middle) in poset.less and (middle, upper) in poset.less
            for middle in range(poset.n)
        ):
            cover_relations.add((lower, upper))
    return frozenset(cover_relations)


def minimal_elements(poset: Poset) -> list[int]:
    return [
        item
        for item in range(poset.n)
        if not any(upper == item for _, upper in poset.less)
    ]


def maximal_elements(poset: Poset) -> list[int]:
    return [
        item
        for item in range(poset.n)
        if not any(lower == item for lower, _ in poset.less)
    ]


def rank_layers(poset: Poset) -> list[list[int]]:
    rank_by_item: dict[int, int] = {}

    def rank(item: int) -> int:
        if item not in rank_by_item:
            rank_by_item[item] = max(
                (rank(lower) + 1 for lower, upper in poset.less if upper == item),
                default=0,
            )
        return rank_by_item[item]

    layers: dict[int, list[int]] = {}
    for item in range(poset.n):
        layers.setdefault(rank(item), []).append(item)
    return [sorted(layers[index]) for index in sorted(layers)]


def structural_profile(poset: Poset) -> dict[str, object]:
    cover_relations = covers(poset)
    layers = rank_layers(poset)
    return {
        "width": width(poset),
        "height": height(poset),
        "minimal_elements": minimal_elements(poset),
        "maximal_elements": maximal_elements(poset),
        "rank_layer_sizes": [len(layer) for layer in layers],
        "rank_layers": layers,
        "cover_relations": [list(pair) for pair in sorted(cover_relations)],
        "cover_edge_count": len(cover_relations),
        "vertex_signatures": [
            list(vertex_signature(poset, item)) for item in range(poset.n)
        ],
    }


def parse_rank_shape(raw: str | None) -> tuple[int, ...] | None:
    if raw is None:
        return None
    try:
        shape = tuple(int(part) for part in raw.split(",") if part.strip())
    except ValueError as exc:
        raise ValueError(f"rank shape must be comma-separated integers: {raw!r}") from exc
    if not shape or any(part <= 0 for part in shape):
        raise ValueError(f"rank shape must contain positive integers: {raw!r}")
    return shape


def rank_shape(poset: Poset) -> tuple[int, ...]:
    return tuple(len(layer) for layer in rank_layers(poset))


def vertex_signature(poset: Poset, item: int) -> tuple[int, int, int, int, int]:
    cover_relations = covers(poset)
    lower_count = sum(1 for lower, upper in poset.less if upper == item)
    upper_count = sum(1 for lower, upper in poset.less if lower == item)
    lower_cover_count = sum(1 for lower, upper in cover_relations if upper == item)
    upper_cover_count = sum(1 for lower, upper in cover_relations if lower == item)
    incomparable_count = poset.n - 1 - lower_count - upper_count
    return (
        lower_count,
        upper_count,
        lower_cover_count,
        upper_cover_count,
        incomparable_count,
    )


def relabeled_key(poset: Poset, permutation: Sequence[int]) -> str:
    bits: list[str] = []
    for lower in range(poset.n):
        for upper in range(poset.n):
            if lower == upper:
                continue
            bits.append(
                "1" if (permutation[lower], permutation[upper]) in poset.less else "0"
            )
    return "".join(bits)


def canonical_key(poset: Poset) -> str:
    blocks_by_signature: dict[tuple[int, int, int, int, int], list[int]] = {}
    for item in range(poset.n):
        blocks_by_signature.setdefault(vertex_signature(poset, item), []).append(item)
    blocks = [blocks_by_signature[key] for key in sorted(blocks_by_signature)]
    block_permutations = [itertools.permutations(block) for block in blocks]
    return min(
        relabeled_key(poset, tuple(itertools.chain.from_iterable(permutation_blocks)))
        for permutation_blocks in itertools.product(*block_permutations)
    )


def balance_report(poset: Poset) -> dict[str, object]:
    total = count_linear_extensions(poset)
    pairs: list[dict[str, object]] = []
    balanced_pairs: list[dict[str, object]] = []
    best_pair: dict[str, object] | None = None
    best_distance: Fraction | None = None

    for x, y in poset.incomparable_pairs():
        xy_count = count_extensions_with_order(poset, x, y)
        probability = Fraction(xy_count, total)
        reverse = Fraction(total - xy_count, total)
        lower_probability = min(probability, reverse)
        pair_payload = {
            "pair": [x, y],
            "x_before_y": [probability.numerator, probability.denominator],
            "lower_orientation_probability": [
                lower_probability.numerator,
                lower_probability.denominator,
            ],
            "balanced": Fraction(1, 3) <= probability <= Fraction(2, 3)
            or Fraction(1, 3) <= reverse <= Fraction(2, 3),
        }
        pairs.append(pair_payload)
        if pair_payload["balanced"]:
            balanced_pairs.append(pair_payload)
        distance = abs(probability - Fraction(1, 2))
        if best_distance is None or distance < best_distance:
            best_distance = distance
            best_pair = pair_payload

    return {
        "n": poset.n,
        "relations": [list(pair) for pair in sorted(poset.less)],
        "width": width(poset),
        "height": height(poset),
        "linear_extensions": total,
        "incomparable_pair_count": len(pairs),
        "balanced_pair_count": len(balanced_pairs),
        "has_balanced_pair": bool(balanced_pairs),
        "best_pair": best_pair,
        "pairs": pairs,
    }


def load_poset(path: Path) -> Poset:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("poset file must be a JSON object")
    n = payload.get("n")
    relations = payload.get("relations", [])
    if not isinstance(n, int):
        raise ValueError("poset file requires integer n")
    if not isinstance(relations, list):
        raise ValueError("poset file requires list relations")
    return make_poset(n, relations)


def all_labeled_posets(n: int) -> list[Poset]:
    """Enumerate labeled posets by orienting each unordered pair or leaving it free.

    This simple generator is intentionally bounded to small n; it canonicalizes
    by transitive closure so duplicate relation presentations collapse.
    """
    unordered_pairs = list(itertools.combinations(range(n), 2))
    seen: set[frozenset[Relation]] = set()
    posets: list[Poset] = []
    for states in itertools.product((-1, 0, 1), repeat=len(unordered_pairs)):
        relations: list[Relation] = []
        for state, (x, y) in zip(states, unordered_pairs):
            if state == -1:
                relations.append((y, x))
            elif state == 1:
                relations.append((x, y))
        try:
            closure = transitive_closure(n, relations)
        except ValueError:
            continue
        if closure in seen:
            continue
        seen.add(closure)
        posets.append(Poset(n=n, less=closure))
    return posets


def is_downset(poset: Poset, mask: int) -> bool:
    for lower, upper in poset.less:
        if mask & (1 << upper) and not mask & (1 << lower):
            return False
    return True


def is_upset(poset: Poset, mask: int) -> bool:
    for lower, upper in poset.less:
        if mask & (1 << lower) and not mask & (1 << upper):
            return False
    return True


def one_point_extensions(poset: Poset) -> list[Poset]:
    new_item = poset.n
    old_mask_limit = 1 << poset.n
    extensions: dict[str, Poset] = {}
    downsets = [mask for mask in range(old_mask_limit) if is_downset(poset, mask)]
    upsets = [mask for mask in range(old_mask_limit) if is_upset(poset, mask)]

    for down_mask in downsets:
        for up_mask in upsets:
            if down_mask & up_mask:
                continue
            relations = list(poset.less)
            for item in range(poset.n):
                if down_mask & (1 << item):
                    relations.append((item, new_item))
                if up_mask & (1 << item):
                    relations.append((new_item, item))
            try:
                candidate = make_poset(poset.n + 1, relations)
            except ValueError:
                continue
            extensions.setdefault(canonical_key(candidate), candidate)
    return [extensions[key] for key in sorted(extensions)]


def all_unlabeled_posets_by_extension(max_n: int) -> dict[int, list[Poset]]:
    if max_n < 1:
        return {}
    levels: dict[int, list[Poset]] = {1: [Poset(n=1, less=frozenset())]}
    for n in range(2, max_n + 1):
        representatives: dict[str, Poset] = {}
        for poset in levels[n - 1]:
            for extension in one_point_extensions(poset):
                representatives.setdefault(canonical_key(extension), extension)
        levels[n] = [representatives[key] for key in sorted(representatives)]
    return levels


def all_unlabeled_posets(n: int) -> list[Poset]:
    return all_unlabeled_posets_by_extension(n).get(n, [])


def analyze_command(args: argparse.Namespace) -> int:
    print(json.dumps(balance_report(load_poset(args.poset)), indent=2, sort_keys=True))
    return 0


def exhaustive_command(args: argparse.Namespace) -> int:
    summary: list[dict[str, object]] = []
    counterexamples: list[dict[str, object]] = []
    worst: dict[str, object] | None = None
    for n in range(2, args.max_n + 1):
        posets = all_labeled_posets(n)
        non_chains = 0
        for poset in posets:
            if not poset.incomparable_pairs():
                continue
            non_chains += 1
            report = balance_report(poset)
            if not report["has_balanced_pair"]:
                counterexamples.append(report)
            best_pair = report["best_pair"]
            if isinstance(best_pair, dict):
                lower = Fraction(*best_pair["lower_orientation_probability"])
                if worst is None or lower < Fraction(*worst["lower_orientation_probability"]):
                    worst = {
                        "n": n,
                        "relations": report["relations"],
                        "pair": best_pair["pair"],
                        "lower_orientation_probability": best_pair[
                            "lower_orientation_probability"
                        ],
                    }
        summary.append(
            {
                "n": n,
                "labeled_posets": len(posets),
                "non_chain_posets": non_chains,
            }
        )
    payload = {
        "max_n": args.max_n,
        "summary": summary,
        "counterexample_count": len(counterexamples),
        "counterexamples": counterexamples[: args.max_counterexamples],
        "worst_best_pair": worst,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not counterexamples else 1


def summarize_posets(posets: Iterable[Poset]) -> dict[str, object]:
    counterexamples: list[dict[str, object]] = []
    width_distribution: dict[int, int] = {}
    height_distribution: dict[int, int] = {}
    worst_by_width: dict[int, dict[str, object]] = {}
    non_chains = 0
    total = 0

    for poset in posets:
        total += 1
        poset_width = width(poset)
        poset_height = height(poset)
        width_distribution[poset_width] = width_distribution.get(poset_width, 0) + 1
        height_distribution[poset_height] = height_distribution.get(poset_height, 0) + 1
        if not poset.incomparable_pairs():
            continue
        non_chains += 1
        report = balance_report(poset)
        if not report["has_balanced_pair"]:
            counterexamples.append(report)
        best_pair = report["best_pair"]
        if isinstance(best_pair, dict):
            lower = Fraction(*best_pair["lower_orientation_probability"])
            prior = worst_by_width.get(poset_width)
            if prior is None or lower < Fraction(*prior["lower_orientation_probability"]):
                worst_by_width[poset_width] = {
                    "relations": report["relations"],
                    "pair": best_pair["pair"],
                    "lower_orientation_probability": best_pair[
                        "lower_orientation_probability"
                    ],
                    "height": poset_height,
                }

    return {
        "total_posets": total,
        "non_chain_posets": non_chains,
        "counterexample_count": len(counterexamples),
        "counterexamples": counterexamples,
        "width_distribution": {
            str(key): width_distribution[key] for key in sorted(width_distribution)
        },
        "height_distribution": {
            str(key): height_distribution[key] for key in sorted(height_distribution)
        },
        "worst_by_width": {
            str(key): worst_by_width[key] for key in sorted(worst_by_width)
        },
    }


def filtered_posets(
    posets: Iterable[Poset],
    *,
    only_width: int | None = None,
    only_height: int | None = None,
    only_rank_shape: tuple[int, ...] | None = None,
) -> list[Poset]:
    filtered: list[Poset] = []
    for poset in posets:
        if only_width is not None and width(poset) != only_width:
            continue
        if only_height is not None and height(poset) != only_height:
            continue
        if only_rank_shape is not None and rank_shape(poset) != only_rank_shape:
            continue
        filtered.append(poset)
    return filtered


def exhaustive_unlabeled_command(args: argparse.Namespace) -> int:
    summary: list[dict[str, object]] = []
    counterexample_count = 0
    shape_filter = parse_rank_shape(args.rank_shape)
    for n in range(2, args.max_n + 1):
        posets = filtered_posets(
            all_unlabeled_posets(n),
            only_width=args.width,
            only_height=args.height,
            only_rank_shape=shape_filter,
        )
        item = {"n": n, **summarize_posets(posets)}
        counterexample_count += int(item["counterexample_count"])
        if args.max_counterexamples >= 0:
            item["counterexamples"] = item["counterexamples"][: args.max_counterexamples]
        summary.append(item)

    payload = {
        "max_n": args.max_n,
        "mode": "unlabeled-canonical",
        "filters": {
            "width": args.width,
            "height": args.height,
            "rank_shape": list(shape_filter) if shape_filter else None,
        },
        "summary": summary,
        "counterexample_count": counterexample_count,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if counterexample_count == 0 else 1


def extremal_width_command(args: argparse.Namespace) -> int:
    records: list[dict[str, object]] = []
    shape_filter = parse_rank_shape(args.rank_shape)
    for n in range(2, args.max_n + 1):
        posets = filtered_posets(
            all_unlabeled_posets(n),
            only_width=args.width,
            only_height=args.height,
            only_rank_shape=shape_filter,
        )
        for poset in posets:
            if not poset.incomparable_pairs():
                continue
            report = balance_report(poset)
            best_pair = report["best_pair"]
            if not isinstance(best_pair, dict):
                continue
            lower = Fraction(*best_pair["lower_orientation_probability"])
            gap = lower - Fraction(1, 3)
            records.append(
                {
                    "n": n,
                    "lower_orientation_probability": [lower.numerator, lower.denominator],
                    "gap_above_one_third": [gap.numerator, gap.denominator],
                    "best_pair": best_pair,
                    "relations": report["relations"],
                    "linear_extensions": report["linear_extensions"],
                    "profile": structural_profile(poset),
                }
            )
    records.sort(
        key=lambda item: (
            Fraction(*item["lower_orientation_probability"]),
            item["n"],
            len(item["relations"]),
        )
    )
    payload = {
        "max_n": args.max_n,
        "width": args.width,
        "height": args.height,
        "rank_shape": list(shape_filter) if shape_filter else None,
        "record_count": len(records),
        "limit": args.limit,
        "records": records[: args.limit],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def signature_bucket(profile: dict[str, object]) -> str:
    return "|".join(
        [
            "layers=" + ",".join(str(item) for item in profile["rank_layer_sizes"]),
            f"covers={profile['cover_edge_count']}",
            f"mins={len(profile['minimal_elements'])}",
            f"maxs={len(profile['maximal_elements'])}",
        ]
    )


def shape_classes_command(args: argparse.Namespace) -> int:
    shape_filter = parse_rank_shape(args.rank_shape)
    buckets: dict[str, dict[str, object]] = {}
    for n in range(2, args.max_n + 1):
        posets = filtered_posets(
            all_unlabeled_posets(n),
            only_width=args.width,
            only_height=args.height,
            only_rank_shape=shape_filter,
        )
        for poset in posets:
            report = balance_report(poset)
            best_pair = report["best_pair"]
            if not isinstance(best_pair, dict):
                continue
            lower = Fraction(*best_pair["lower_orientation_probability"])
            profile = structural_profile(poset)
            key = signature_bucket(profile)
            bucket = buckets.setdefault(
                key,
                {
                    "signature": key,
                    "count": 0,
                    "min_lower_orientation_probability": [
                        lower.numerator,
                        lower.denominator,
                    ],
                    "examples": [],
                },
            )
            bucket["count"] = int(bucket["count"]) + 1
            current_min = Fraction(*bucket["min_lower_orientation_probability"])
            if lower < current_min:
                bucket["min_lower_orientation_probability"] = [
                    lower.numerator,
                    lower.denominator,
                ]
                bucket["examples"] = []
            if (
                lower == Fraction(*bucket["min_lower_orientation_probability"])
                and len(bucket["examples"]) < args.examples_per_bucket
            ):
                bucket["examples"].append(
                    {
                        "n": n,
                        "lower_orientation_probability": [
                            lower.numerator,
                            lower.denominator,
                        ],
                        "best_pair": best_pair,
                        "relations": report["relations"],
                        "profile": profile,
                    }
                )
    bucket_list = sorted(
        buckets.values(),
        key=lambda bucket: (
            Fraction(*bucket["min_lower_orientation_probability"]),
            bucket["signature"],
        ),
    )
    payload = {
        "max_n": args.max_n,
        "width": args.width,
        "height": args.height,
        "rank_shape": list(shape_filter) if shape_filter else None,
        "bucket_count": len(bucket_list),
        "total_posets": sum(int(bucket["count"]) for bucket in bucket_list),
        "buckets": bucket_list,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("poset", type=Path)
    analyze_parser.set_defaults(func=analyze_command)

    exhaustive_parser = subparsers.add_parser("exhaustive-small")
    exhaustive_parser.add_argument("--max-n", type=int, default=5)
    exhaustive_parser.add_argument("--max-counterexamples", type=int, default=3)
    exhaustive_parser.add_argument("--output", type=Path)
    exhaustive_parser.set_defaults(func=exhaustive_command)

    unlabeled_parser = subparsers.add_parser("exhaustive-unlabeled")
    unlabeled_parser.add_argument("--max-n", type=int, default=5)
    unlabeled_parser.add_argument("--max-counterexamples", type=int, default=3)
    unlabeled_parser.add_argument("--output", type=Path)
    unlabeled_parser.add_argument("--width", type=int)
    unlabeled_parser.add_argument("--height", type=int)
    unlabeled_parser.add_argument("--rank-shape")
    unlabeled_parser.set_defaults(func=exhaustive_unlabeled_command)

    extremal_parser = subparsers.add_parser("extremal-width")
    extremal_parser.add_argument("--max-n", type=int, default=7)
    extremal_parser.add_argument("--width", type=int, required=True)
    extremal_parser.add_argument("--height", type=int)
    extremal_parser.add_argument("--rank-shape")
    extremal_parser.add_argument("--limit", type=int, default=10)
    extremal_parser.add_argument("--output", type=Path)
    extremal_parser.set_defaults(func=extremal_width_command)

    classes_parser = subparsers.add_parser("shape-classes")
    classes_parser.add_argument("--max-n", type=int, default=7)
    classes_parser.add_argument("--width", type=int, required=True)
    classes_parser.add_argument("--height", type=int)
    classes_parser.add_argument("--rank-shape")
    classes_parser.add_argument("--examples-per-bucket", type=int, default=2)
    classes_parser.add_argument("--output", type=Path)
    classes_parser.set_defaults(func=shape_classes_command)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
