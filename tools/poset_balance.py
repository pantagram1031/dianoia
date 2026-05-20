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


def extension_recurrence_trace(
    poset: Poset,
    labels: Sequence[str],
    first: int,
    second: int,
    max_depth: int = 1,
) -> dict[str, object]:
    if max_depth < 1:
        raise ValueError("recurrence trace depth must be at least 1")
    prerequisites = poset.covers_mask()
    full = (1 << poset.n) - 1

    @cache
    def solve(placed: int, relation_state: int) -> tuple[int, int]:
        if placed == full:
            if relation_state == 1:
                return 1, 0
            if relation_state == 2:
                return 0, 1
            raise ValueError("pair state unresolved at complete extension")
        first_total = 0
        second_total = 0
        for item in range(poset.n):
            bit = 1 << item
            if placed & bit:
                continue
            if prerequisites[item] & ~placed:
                continue
            next_state = relation_state
            if item == first and relation_state == 0:
                next_state = 1
            elif item == second and relation_state == 0:
                next_state = 2
            left, right = solve(placed | bit, next_state)
            first_total += left
            second_total += right
        return first_total, second_total

    @cache
    def build(placed: int, relation_state: int, depth_remaining: int) -> dict[str, object]:
        first_total, second_total = solve(placed, relation_state)
        available = []
        for item in range(poset.n):
            bit = 1 << item
            if placed & bit:
                continue
            if prerequisites[item] & ~placed:
                continue
            next_state = relation_state
            if item == first and relation_state == 0:
                next_state = 1
            elif item == second and relation_state == 0:
                next_state = 2
            child_first, child_second = solve(placed | bit, next_state)
            child_record = {
                "choose": labels[item],
                "remaining_after_choice": [
                    labels[index]
                    for index in range(poset.n)
                    if not (placed | bit) & (1 << index)
                ],
                "pair_state_after_choice": ["unseen", "first_before_second", "second_before_first"][
                    next_state
                ],
                "first_before_second": child_first,
                "second_before_first": child_second,
            }
            if depth_remaining > 1:
                child_record["subtrace"] = build(
                    placed | bit,
                    next_state,
                    depth_remaining - 1,
                )
            available.append(child_record)
        return {
            "placed": [
                labels[index] for index in range(poset.n) if placed & (1 << index)
            ],
            "pair_state": ["unseen", "first_before_second", "second_before_first"][
                relation_state
            ],
            "first_before_second": first_total,
            "second_before_first": second_total,
            "available": available,
        }

    root = build(0, 0, max_depth)
    return root


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


def rank_index_by_item(poset: Poset) -> dict[int, int]:
    return {
        item: rank_index
        for rank_index, layer in enumerate(rank_layers(poset))
        for item in layer
    }


def cover_rank_matrix(poset: Poset) -> list[list[int]]:
    layers = rank_layers(poset)
    rank_index = rank_index_by_item(poset)
    matrix = [[0 for _ in layers] for _ in layers]
    for lower, upper in covers(poset):
        matrix[rank_index[lower]][rank_index[upper]] += 1
    return matrix


def rank_layer_vertex_signatures(poset: Poset) -> list[list[list[object]]]:
    layers = rank_layers(poset)
    rank_index = rank_index_by_item(poset)
    layer_count = len(layers)
    cover_relations = covers(poset)
    signatures_by_layer: list[list[list[object]]] = []
    for layer in layers:
        layer_signatures = []
        for item in layer:
            lower_covers_by_rank = [0] * layer_count
            upper_covers_by_rank = [0] * layer_count
            for lower, upper in cover_relations:
                if upper == item:
                    lower_covers_by_rank[rank_index[lower]] += 1
                if lower == item:
                    upper_covers_by_rank[rank_index[upper]] += 1
            lower_count = sum(1 for lower, upper in poset.less if upper == item)
            upper_count = sum(1 for lower, upper in poset.less if lower == item)
            incomparable_count = poset.n - 1 - lower_count - upper_count
            layer_signatures.append(
                [
                    lower_count,
                    upper_count,
                    incomparable_count,
                    lower_covers_by_rank,
                    upper_covers_by_rank,
                ]
            )
        signatures_by_layer.append(sorted(layer_signatures))
    return signatures_by_layer


def rank_layer_labels(layers: Sequence[Sequence[int]]) -> list[list[str]]:
    names = list("abcdefghijklmnopqrstuvwxyz")
    if sum(len(layer) for layer in layers) > len(names):
        return [
            [f"r{rank_index}_{item_index}" for item_index, _ in enumerate(layer)]
            for rank_index, layer in enumerate(layers)
        ]
    offset = 0
    labels: list[list[str]] = []
    for layer in layers:
        labels.append(names[offset : offset + len(layer)])
        offset += len(layer)
    return labels


def layered_items_from_shape(shape: Sequence[int]) -> list[list[int]]:
    layers: list[list[int]] = []
    offset = 0
    for layer_size in shape:
        layers.append(list(range(offset, offset + layer_size)))
        offset += layer_size
    return layers


def named_edges(edges: Iterable[Relation], label_by_item: dict[int, str]) -> list[str]:
    return sorted(f"{label_by_item[lower]}<{label_by_item[upper]}" for lower, upper in edges)


def rank_normal_form(poset: Poset) -> dict[str, object]:
    layers = rank_layers(poset)
    label_layers = rank_layer_labels(layers)
    best_key: tuple[list[str], list[str]] | None = None
    best_labels: dict[int, str] | None = None
    for layer_permutation in itertools.product(
        *(itertools.permutations(layer) for layer in layers)
    ):
        label_by_item: dict[int, str] = {}
        for rank_index, layer in enumerate(layer_permutation):
            for label, item in zip(label_layers[rank_index], layer):
                label_by_item[item] = label
        cover_key = named_edges(covers(poset), label_by_item)
        relation_key = named_edges(poset.less, label_by_item)
        key = (cover_key, relation_key)
        if best_key is None or key < best_key:
            best_key = key
            best_labels = label_by_item

    if best_labels is None:
        raise ValueError("cannot normalize an empty label assignment")
    report = balance_report(poset)
    best_pair = report["best_pair"]
    named_best_pair: dict[str, object] | None = None
    if isinstance(best_pair, dict):
        x, y = best_pair["pair"]
        named_best_pair = {
            "pair": [best_labels[x], best_labels[y]],
            "x_before_y": best_pair["x_before_y"],
            "lower_orientation_probability": best_pair[
                "lower_orientation_probability"
            ],
            "balanced": best_pair["balanced"],
        }
    return {
        "rank_layers": [
            [best_labels[item] for item in layer]
            for layer in layers
        ],
        "label_by_item": {str(item): best_labels[item] for item in range(poset.n)},
        "cover_relations": named_edges(covers(poset), best_labels),
        "relations": named_edges(poset.less, best_labels),
        "minimal_elements": [best_labels[item] for item in minimal_elements(poset)],
        "maximal_elements": [best_labels[item] for item in maximal_elements(poset)],
        "best_pair": named_best_pair,
    }


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
        "cover_rank_matrix": cover_rank_matrix(poset),
        "vertex_signatures": [
            list(vertex_signature(poset, item)) for item in range(poset.n)
        ],
        "rank_layer_vertex_signatures": rank_layer_vertex_signatures(poset),
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


def parse_cover_matrix(raw: str) -> tuple[tuple[int, ...], ...]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"cover matrix must be JSON: {raw!r}") from exc
    if not isinstance(payload, list) or not payload:
        raise ValueError("cover matrix must be a nonempty JSON list")
    rows: list[tuple[int, ...]] = []
    width_value: int | None = None
    for row in payload:
        if not isinstance(row, list) or not row:
            raise ValueError("cover matrix rows must be nonempty lists")
        if not all(isinstance(item, int) and item >= 0 for item in row):
            raise ValueError("cover matrix entries must be nonnegative integers")
        if width_value is None:
            width_value = len(row)
        elif len(row) != width_value:
            raise ValueError("cover matrix rows must have equal length")
        rows.append(tuple(row))
    if len(rows) != width_value:
        raise ValueError("cover matrix must be square")
    return tuple(rows)


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


def parse_named_relation(raw: str, index_by_label: dict[str, int]) -> Relation:
    if "<" not in raw:
        raise ValueError(f"named relation must use '<': {raw!r}")
    lower, upper = (part.strip() for part in raw.split("<", 1))
    if lower not in index_by_label or upper not in index_by_label:
        raise ValueError(f"named relation has unknown label: {raw!r}")
    return index_by_label[lower], index_by_label[upper]


def load_named_case(path: Path) -> tuple[Poset, list[str], list[list[str]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("named case file must be a JSON object")
    labels = payload.get("labels")
    if not isinstance(labels, list) or not all(
        isinstance(label, str) for label in labels
    ):
        raise ValueError("named case file requires string labels")
    if len(set(labels)) != len(labels):
        raise ValueError("named case labels must be unique")
    index_by_label = {label: index for index, label in enumerate(labels)}
    raw_relations = payload.get("cover_relations", payload.get("relations", []))
    if not isinstance(raw_relations, list) or not all(
        isinstance(relation, str) for relation in raw_relations
    ):
        raise ValueError("named case file requires string cover_relations")
    raw_pairs = payload.get("check_pairs", [])
    if not isinstance(raw_pairs, list):
        raise ValueError("named case file check_pairs must be a list")
    check_pairs: list[list[str]] = []
    for pair in raw_pairs:
        if (
            not isinstance(pair, list)
            or len(pair) != 2
            or not all(isinstance(item, str) for item in pair)
        ):
            raise ValueError(f"invalid named check pair: {pair!r}")
        if pair[0] not in index_by_label or pair[1] not in index_by_label:
            raise ValueError(f"named check pair has unknown label: {pair!r}")
        check_pairs.append(pair)
    relations = [
        parse_named_relation(relation, index_by_label) for relation in raw_relations
    ]
    return make_poset(len(labels), relations), labels, check_pairs


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


def named_case_command(args: argparse.Namespace) -> int:
    poset, labels, check_pairs = load_named_case(args.case)
    index_by_label = {label: index for index, label in enumerate(labels)}
    total = count_linear_extensions(poset)
    pair_reports: list[dict[str, object]] = []
    for first, second in check_pairs:
        first_index = index_by_label[first]
        second_index = index_by_label[second]
        first_before_second = count_extensions_with_order(
            poset,
            first_index,
            second_index,
        )
        second_before_first = total - first_before_second
        lower = min(first_before_second, second_before_first)
        lower_probability = Fraction(lower, total)
        pair_reports.append(
            {
                "pair": [first, second],
                "first_before_second": [
                    first_before_second,
                    total,
                ],
                "second_before_first": [
                    second_before_first,
                    total,
                ],
                "lower_orientation_probability": [
                    lower_probability.numerator,
                    lower_probability.denominator,
                ],
                "balanced": 3 * first_before_second <= 2 * total
                and 3 * first_before_second >= total
                or 3 * second_before_first <= 2 * total
                and 3 * second_before_first >= total,
            }
        )
    payload = {
        "labels": labels,
        "linear_extensions": total,
        "width": width(poset),
        "height": height(poset),
        "cover_relations": named_edges(covers(poset), dict(enumerate(labels))),
        "relations": named_edges(poset.less, dict(enumerate(labels))),
        "check_pairs": pair_reports,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def named_case_recurrence_command(args: argparse.Namespace) -> int:
    poset, labels, check_pairs = load_named_case(args.case)
    if len(check_pairs) != 1:
        raise ValueError("named-case-recurrence requires exactly one check_pair")
    payload = named_case_recurrence_payload(
        poset,
        labels,
        check_pairs[0],
        args.depth,
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def named_case_recurrence_payload(
    poset: Poset,
    labels: Sequence[str],
    check_pair: Sequence[str],
    depth: int,
) -> dict[str, object]:
    index_by_label = {label: index for index, label in enumerate(labels)}
    first, second = check_pair
    trace = extension_recurrence_trace(
        poset,
        list(labels),
        index_by_label[first],
        index_by_label[second],
        max_depth=depth,
    )
    return {
        "labels": list(labels),
        "pair": [first, second],
        "depth": depth,
        "linear_extensions": trace["first_before_second"]
        + trace["second_before_first"],
        "cover_relations": named_edges(covers(poset), dict(enumerate(list(labels)))),
        "trace": trace,
    }


def named_case_mechanism_search(case: Path, max_depth: int) -> dict[str, object]:
    poset, labels, check_pairs = load_named_case(case)
    if len(check_pairs) != 1:
        raise ValueError("named-case-mechanism-search requires exactly one check_pair")
    depth_records: list[dict[str, object]] = []
    found: dict[str, object] | None = None
    for depth in range(1, max_depth + 1):
        recurrence = named_case_recurrence_payload(poset, labels, check_pairs[0], depth)
        mechanism = recurrence_mechanism_summary(recurrence, str(case))
        record = {
            "depth": depth,
            "mechanism_type": mechanism["mechanism_type"],
            "root_first_before_second": mechanism["root_first_before_second"],
            "root_second_before_first": mechanism["root_second_before_first"],
            "root_total": mechanism["root_total"],
            "leaf_count": mechanism["leaf_count"],
            "state_counts": mechanism["state_counts"],
            "split_counts": mechanism["split_counts"],
            "balanced_unseen_leaf_count": mechanism["balanced_unseen_leaf_count"],
            "unbalanced_unseen_leaf_count": mechanism["unbalanced_unseen_leaf_count"],
        }
        depth_records.append(record)
        if mechanism["mechanism_type"] in {
            "forced-block",
            "balanced-core-plus-forced-first",
            "balanced-core-plus-forced-second",
            "balanced-core-with-forced-blocks",
        }:
            found = record
            break

    first = int(depth_records[-1]["root_first_before_second"])
    second = int(depth_records[-1]["root_second_before_first"])
    total = int(depth_records[-1]["root_total"])
    lower = min(first, second)
    out = {
        "case": str(case),
        "labels": labels,
        "pair": list(check_pairs[0]),
        "max_depth": max_depth,
        "found": found is not None,
        "found_depth": found["depth"] if found else None,
        "mechanism_type": found["mechanism_type"] if found else depth_records[-1]["mechanism_type"],
        "lower_probability": [lower, total],
        "depth_records": depth_records,
    }
    if found and found["mechanism_type"] == "forced-block":
        recurrence = named_case_recurrence_payload(
            poset,
            labels,
            check_pairs[0],
            int(found["depth"]),
        )
        out["forced_block_obligations"] = recurrence_forced_block_obligations(
            recurrence,
            str(case),
        )
    return out


def named_case_mechanism_search_command(args: argparse.Namespace) -> int:
    out = named_case_mechanism_search(args.case, args.max_depth)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def is_named_case_file(path: Path) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return isinstance(payload, dict) and "cover_relations" in payload and "check_pairs" in payload


def named_case_mechanism_batch_command(args: argparse.Namespace) -> int:
    case_paths: list[Path] = []
    for case_dir in args.case_dirs:
        case_paths.extend(
            path
            for path in sorted(case_dir.glob("*.json"))
            if is_named_case_file(path)
        )
    seen: set[str] = set()
    records: list[dict[str, object]] = []
    for case in case_paths:
        key = str(case)
        if key in seen:
            continue
        seen.add(key)
        records.append(named_case_mechanism_search(case, args.max_depth))

    by_mechanism: dict[str, int] = {}
    unresolved: list[str] = []
    for record in records:
        mechanism = str(record["mechanism_type"])
        by_mechanism[mechanism] = by_mechanism.get(mechanism, 0) + 1
        if not record["found"]:
            unresolved.append(str(record["case"]))
    out = {
        "case_dirs": [str(path) for path in args.case_dirs],
        "case_count": len(records),
        "max_depth": args.max_depth,
        "found_count": len(records) - len(unresolved),
        "unresolved": unresolved,
        "by_mechanism": by_mechanism,
        "cases": records,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def recurrence_leaves(trace: dict[str, object]) -> list[dict[str, object]]:
    leaves: list[dict[str, object]] = []

    def walk(node: dict[str, object], path: list[str]) -> None:
        available = node.get("available", [])
        if not isinstance(available, list):
            raise ValueError("recurrence trace available field must be a list")
        if not available:
            leaves.append(
                {
                    "path": path,
                    "pair_state": node["pair_state"],
                    "first_before_second": node["first_before_second"],
                    "second_before_first": node["second_before_first"],
                    "total": int(node["first_before_second"])
                    + int(node["second_before_first"]),
                }
            )
            return
        for child in available:
            if not isinstance(child, dict):
                raise ValueError("recurrence trace child must be a dictionary")
            choose = str(child["choose"])
            child_path = path + [choose]
            if "subtrace" in child:
                subtrace = child["subtrace"]
                if not isinstance(subtrace, dict):
                    raise ValueError("recurrence subtrace must be a dictionary")
                walk(subtrace, child_path)
            else:
                leaves.append(
                    {
                        "path": child_path,
                        "pair_state": child["pair_state_after_choice"],
                        "first_before_second": child["first_before_second"],
                        "second_before_first": child["second_before_first"],
                        "total": int(child["first_before_second"])
                        + int(child["second_before_first"]),
                        "remaining_after_choice": child.get(
                            "remaining_after_choice",
                            [],
                        ),
                    }
                )

    walk(trace, [])
    return leaves


def recurrence_leaf_summary_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.recurrence.read_text(encoding="utf-8"))
    leaves = recurrence_leaves(payload["trace"])
    state_totals: dict[str, dict[str, int]] = {}
    for leaf in leaves:
        state = str(leaf["pair_state"])
        state_total = state_totals.setdefault(
            state,
            {"first_before_second": 0, "second_before_first": 0, "total": 0},
        )
        state_total["first_before_second"] += int(leaf["first_before_second"])
        state_total["second_before_first"] += int(leaf["second_before_first"])
        state_total["total"] += int(leaf["total"])
    out = {
        "source": str(args.recurrence),
        "labels": payload.get("labels"),
        "pair": payload.get("pair"),
        "depth": payload.get("depth"),
        "leaf_count": len(leaves),
        "first_before_second": payload["trace"]["first_before_second"],
        "second_before_first": payload["trace"]["second_before_first"],
        "state_totals": state_totals,
        "leaves": leaves,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def recurrence_mechanism_summary(recurrence: dict[str, object], source: str) -> dict[str, object]:
    leaves = recurrence_leaves(recurrence["trace"])
    forced_first_total = 0
    forced_second_total = 0
    unseen_first_total = 0
    unseen_second_total = 0
    unseen_total = 0
    balanced_unseen_count = 0
    unbalanced_unseen_count = 0
    split_counts: dict[str, int] = {}
    state_counts: dict[str, int] = {}

    for leaf in leaves:
        first = int(leaf["first_before_second"])
        second = int(leaf["second_before_first"])
        total = int(leaf["total"])
        state = str(leaf["pair_state"])
        state_counts[state] = state_counts.get(state, 0) + 1
        split_key = f"{first}:{second}"
        split_counts[split_key] = split_counts.get(split_key, 0) + 1

        if state == "first_before_second":
            forced_first_total += total
        elif state == "second_before_first":
            forced_second_total += total
        elif state == "unseen":
            unseen_first_total += first
            unseen_second_total += second
            unseen_total += total
            if first == second:
                balanced_unseen_count += 1
            else:
                unbalanced_unseen_count += 1

    if unseen_total == 0:
        mechanism_type = "forced-block"
    elif unbalanced_unseen_count == 0 and forced_second_total == 0:
        mechanism_type = "balanced-core-plus-forced-first"
    elif unbalanced_unseen_count == 0 and forced_first_total == 0:
        mechanism_type = "balanced-core-plus-forced-second"
    elif unbalanced_unseen_count == 0:
        mechanism_type = "balanced-core-with-forced-blocks"
    else:
        mechanism_type = "mixed"

    trace = recurrence["trace"]
    return {
        "source": source,
        "labels": recurrence.get("labels"),
        "pair": recurrence.get("pair"),
        "depth": recurrence.get("depth"),
        "leaf_count": len(leaves),
        "root_first_before_second": trace["first_before_second"],
        "root_second_before_first": trace["second_before_first"],
        "root_total": int(trace["first_before_second"]) + int(trace["second_before_first"]),
        "mechanism_type": mechanism_type,
        "forced_first_total": forced_first_total,
        "forced_second_total": forced_second_total,
        "unseen_first_total": unseen_first_total,
        "unseen_second_total": unseen_second_total,
        "unseen_total": unseen_total,
        "balanced_unseen_leaf_count": balanced_unseen_count,
        "unbalanced_unseen_leaf_count": unbalanced_unseen_count,
        "state_counts": state_counts,
        "split_counts": split_counts,
        "leaves": leaves,
    }


def recurrence_mechanism_summary_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.recurrence.read_text(encoding="utf-8"))
    out = recurrence_mechanism_summary(payload, str(args.recurrence))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def recurrence_forced_block_obligations(
    recurrence: dict[str, object],
    source: str,
) -> dict[str, object]:
    mechanism = recurrence_mechanism_summary(recurrence, source)
    if mechanism["mechanism_type"] != "forced-block":
        return {
            "source": source,
            "applies": False,
            "reason": f"mechanism_type is {mechanism['mechanism_type']}, not forced-block",
            "mechanism_type": mechanism["mechanism_type"],
            "pair": mechanism["pair"],
            "depth": mechanism["depth"],
        }

    first = int(mechanism["root_first_before_second"])
    second = int(mechanism["root_second_before_first"])
    total = int(mechanism["root_total"])
    if first <= second:
        lower_orientation = "first_before_second"
        lower_total = first
        upper_total = second
    else:
        lower_orientation = "second_before_first"
        lower_total = second
        upper_total = first

    obligations = []
    for leaf in mechanism["leaves"]:
        state = str(leaf["pair_state"])
        count = int(leaf["total"])
        obligations.append(
            {
                "path": leaf["path"],
                "orientation": state,
                "count": count,
                "counts_toward_lower_orientation": state == lower_orientation,
                "remaining_after_choice": leaf.get("remaining_after_choice", []),
            }
        )

    return {
        "source": source,
        "applies": True,
        "mechanism_type": "forced-block",
        "pair": mechanism["pair"],
        "depth": mechanism["depth"],
        "root_split": {
            "first_before_second": first,
            "second_before_first": second,
            "total": total,
        },
        "lower_orientation": lower_orientation,
        "lower_total": lower_total,
        "upper_total": upper_total,
        "lower_probability": [lower_total, total],
        "forced_first_total": mechanism["forced_first_total"],
        "forced_second_total": mechanism["forced_second_total"],
        "split_counts": mechanism["split_counts"],
        "obligations": obligations,
        "lemma_schema": [
            "Partition linear extensions by the listed initial paths.",
            "For each path, prove the terminal count by a direct residual-poset count.",
            "Sum the terminal counts by forced orientation.",
            "Use the lower orientation total as the certified probability lower bound.",
        ],
    }


def recurrence_forced_block_obligations_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.recurrence.read_text(encoding="utf-8"))
    out = recurrence_forced_block_obligations(payload, str(args.recurrence))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def recurrence_leaf_compare_command(args: argparse.Namespace) -> int:
    left = json.loads(args.left.read_text(encoding="utf-8"))
    right = json.loads(args.right.read_text(encoding="utf-8"))
    left_leaves = recurrence_leaves(left["trace"])
    right_leaves = recurrence_leaves(right["trace"])

    def split_key(leaf: dict[str, object]) -> str:
        return f"{leaf['first_before_second']}:{leaf['second_before_first']}"

    def split_counts(leaves: list[dict[str, object]]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for leaf in leaves:
            counts[split_key(leaf)] = counts.get(split_key(leaf), 0) + 1
        return counts

    left_counts = split_counts(left_leaves)
    right_counts = split_counts(right_leaves)
    split_comparison = [
        {
            "split": split,
            "left_count": left_counts.get(split, 0),
            "right_count": right_counts.get(split, 0),
        }
        for split in sorted(set(left_counts) | set(right_counts))
    ]
    out = {
        "left": str(args.left),
        "right": str(args.right),
        "left_pair": left.get("pair"),
        "right_pair": right.get("pair"),
        "left_leaf_count": len(left_leaves),
        "right_leaf_count": len(right_leaves),
        "left_total_split": [
            left["trace"]["first_before_second"],
            left["trace"]["second_before_first"],
        ],
        "right_total_split": [
            right["trace"]["first_before_second"],
            right["trace"]["second_before_first"],
        ],
        "matching_total_split": (
            left["trace"]["first_before_second"] == right["trace"]["first_before_second"]
            and left["trace"]["second_before_first"] == right["trace"]["second_before_first"]
        ),
        "split_comparison": split_comparison,
        "left_leaves": left_leaves,
        "right_leaves": right_leaves,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
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


def fine_signature_bucket(profile: dict[str, object]) -> str:
    return "|".join(
        [
            matrix_signature_bucket(profile),
            "layer_vertex_signatures="
            + json.dumps(
                profile["rank_layer_vertex_signatures"],
                separators=(",", ":"),
            ),
        ]
    )


def matrix_signature_bucket(profile: dict[str, object]) -> str:
    return "|".join(
        [
            signature_bucket(profile),
            "cover_matrix=" + json.dumps(profile["cover_rank_matrix"], separators=(",", ":")),
        ]
    )


def profile_signature(profile: dict[str, object], mode: str) -> str:
    if mode == "fine":
        return fine_signature_bucket(profile)
    if mode == "matrix":
        return matrix_signature_bucket(profile)
    if mode == "coarse":
        return signature_bucket(profile)
    raise ValueError(f"unknown signature mode: {mode}")


def parse_fraction(raw: str) -> Fraction:
    if "/" in raw:
        numerator, denominator = raw.split("/", 1)
        return Fraction(int(numerator), int(denominator))
    return Fraction(int(raw), 1)


def matrix_from_bucket_signature(signature: str) -> tuple[tuple[int, ...], ...]:
    fields: dict[str, str] = {}
    for part in signature.split("|"):
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        fields[key] = value
    if "cover_matrix" not in fields:
        raise ValueError(f"signature has no cover_matrix field: {signature!r}")
    return parse_cover_matrix(fields["cover_matrix"])


def matrix_feature_record(
    bucket: dict[str, object],
    *,
    key_detail: str = "coarse",
) -> dict[str, object]:
    signature = str(bucket["signature"])
    matrix = matrix_from_bucket_signature(signature)
    size = len(matrix)

    def entry(row: int, column: int) -> int:
        if row >= size or column >= size:
            return 0
        return matrix[row][column]

    adjacent_edges = sum(entry(rank, rank + 1) for rank in range(size - 1))
    adjacent_vector = tuple(entry(rank, rank + 1) for rank in range(size - 1))
    skip_edges = sum(
        entry(row, column)
        for row in range(size)
        for column in range(row + 2, size)
    )
    skip_vector = tuple(
        entry(row, column)
        for row in range(size)
        for column in range(row + 2, size)
    )
    layer_features = {
        f"r{row}_to_r{column}": entry(row, column)
        for row in range(size)
        for column in range(row + 1, size)
    }
    flags = {
        "bottom_dense": entry(0, 1) >= 3,
        "middle_dense": entry(1, 2) >= 3,
        "has_bottom_skip": entry(0, 2) > 0,
        "has_middle_to_top_skip": entry(1, 3) > 0,
        "top_fed_by_two": entry(2, 3) >= 2,
        "has_skip_cover": skip_edges > 0,
    }
    key_parts = [
        f"covers={sum(sum(row) for row in matrix)}",
        f"adjacent={adjacent_edges}",
        f"skip={skip_edges}",
    ]
    if key_detail == "vector":
        key_parts.extend(
            [
                "adjacent_vector=" + ",".join(str(value) for value in adjacent_vector),
                "skip_vector=" + ",".join(str(value) for value in skip_vector),
            ]
        )
    key_parts.extend(f"{key}={int(value)}" for key, value in sorted(flags.items()))
    return {
        "signature": signature,
        "count": bucket["count"],
        "min_lower_orientation_probability": bucket[
            "min_lower_orientation_probability"
        ],
        "cover_matrix": [list(row) for row in matrix],
        "features": {
            "adjacent_edges": adjacent_edges,
            "adjacent_vector": list(adjacent_vector),
            "skip_edges": skip_edges,
            "skip_vector": list(skip_vector),
            **layer_features,
            **flags,
        },
        "feature_key": "|".join(key_parts),
    }


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
            key = profile_signature(profile, args.signature)
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
        "signature_mode": args.signature,
        "bucket_count": len(bucket_list),
        "total_posets": sum(int(bucket["count"]) for bucket in bucket_list),
        "buckets": bucket_list,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def matrix_feature_partition_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.classes.read_text(encoding="utf-8"))
    threshold = parse_fraction(args.threshold) if args.threshold else None
    processed_threshold = (
        parse_fraction(args.processed_threshold)
        if args.processed_threshold
        else None
    )
    groups: dict[str, dict[str, object]] = {}
    for bucket in payload["buckets"]:
        record = matrix_feature_record(bucket, key_detail=args.key_detail)
        lower = Fraction(*record["min_lower_orientation_probability"])
        if threshold is not None and lower > threshold:
            continue
        if processed_threshold is not None:
            record["processed"] = lower <= processed_threshold
        group = groups.setdefault(
            str(record["feature_key"]),
            {
                "feature_key": record["feature_key"],
                "bucket_count": 0,
                "profile_count": 0,
                "processed_bucket_count": 0,
                "unprocessed_bucket_count": 0,
                "processed_profile_count": 0,
                "unprocessed_profile_count": 0,
                "min_lower_orientation_probability": record[
                    "min_lower_orientation_probability"
                ],
                "features": record["features"],
                "buckets": [],
            },
        )
        group["bucket_count"] = int(group["bucket_count"]) + 1
        group["profile_count"] = int(group["profile_count"]) + int(record["count"])
        if processed_threshold is not None:
            if record["processed"]:
                group["processed_bucket_count"] = int(group["processed_bucket_count"]) + 1
                group["processed_profile_count"] = (
                    int(group["processed_profile_count"]) + int(record["count"])
                )
            else:
                group["unprocessed_bucket_count"] = int(group["unprocessed_bucket_count"]) + 1
                group["unprocessed_profile_count"] = (
                    int(group["unprocessed_profile_count"]) + int(record["count"])
                )
        if lower < Fraction(*group["min_lower_orientation_probability"]):
            group["min_lower_orientation_probability"] = record[
                "min_lower_orientation_probability"
            ]
        group["buckets"].append(record)

    group_list = sorted(
        groups.values(),
        key=lambda group: (
            Fraction(*group["min_lower_orientation_probability"]),
            group["feature_key"],
        ),
    )
    out = {
        "source": str(args.classes),
        "threshold": args.threshold,
        "processed_threshold": args.processed_threshold,
        "key_detail": args.key_detail,
        "source_bucket_count": payload["bucket_count"],
        "included_bucket_count": sum(int(group["bucket_count"]) for group in group_list),
        "processed_bucket_count": sum(
            int(group["processed_bucket_count"]) for group in group_list
        ),
        "unprocessed_bucket_count": sum(
            int(group["unprocessed_bucket_count"]) for group in group_list
        ),
        "group_count": len(group_list),
        "groups": group_list,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def vector_from_feature_group(group: dict[str, object]) -> tuple[int, ...]:
    features = group["features"]
    if not isinstance(features, dict):
        raise ValueError("feature group has no feature dictionary")
    adjacent = features.get("adjacent_vector")
    skip = features.get("skip_vector")
    if not isinstance(adjacent, list) or not isinstance(skip, list):
        raise ValueError("feature group has no adjacent_vector/skip_vector")
    return tuple(int(value) for value in adjacent + skip)


def vector_leq(left: Sequence[int], right: Sequence[int]) -> bool:
    return all(a <= b for a, b in zip(left, right))


def vector_l1_distance(left: Sequence[int], right: Sequence[int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def matrix_vector_frontier_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.partition.read_text(encoding="utf-8"))
    processed: list[dict[str, object]] = []
    unprocessed: list[dict[str, object]] = []
    mixed: list[dict[str, object]] = []
    for group in payload["groups"]:
        vector = vector_from_feature_group(group)
        record = {
            "feature_key": group["feature_key"],
            "vector": list(vector),
            "adjacent_vector": group["features"]["adjacent_vector"],
            "skip_vector": group["features"]["skip_vector"],
            "bucket_count": group["bucket_count"],
            "profile_count": group["profile_count"],
            "processed_bucket_count": group.get("processed_bucket_count", 0),
            "unprocessed_bucket_count": group.get("unprocessed_bucket_count", 0),
            "min_lower_orientation_probability": group[
                "min_lower_orientation_probability"
            ],
        }
        processed_count = int(record["processed_bucket_count"])
        unprocessed_count = int(record["unprocessed_bucket_count"])
        if processed_count and unprocessed_count:
            mixed.append(record)
        elif processed_count:
            processed.append(record)
        elif unprocessed_count:
            unprocessed.append(record)

    def sort_key(record: dict[str, object]) -> tuple[Fraction, list[int], str]:
        return (
            Fraction(*record["min_lower_orientation_probability"]),
            list(record["vector"]),
            str(record["feature_key"]),
        )

    processed.sort(key=sort_key)
    unprocessed.sort(key=sort_key)
    for index, record in enumerate(processed, start=1):
        record["id"] = f"P{index}"
    for index, record in enumerate(unprocessed, start=1):
        record["id"] = f"U{index}"

    analyzed_unprocessed: list[dict[str, object]] = []
    for record in unprocessed:
        vector = tuple(record["vector"])
        dominated_by_unprocessed = [
            other["id"]
            for other in unprocessed
            if other is not record
            and vector_leq(tuple(other["vector"]), vector)
            and tuple(other["vector"]) != vector
        ]
        dominates_processed = [
            other["id"]
            for other in processed
            if vector_leq(tuple(other["vector"]), vector)
        ]
        dominated_by_processed = [
            other["id"]
            for other in processed
            if vector_leq(vector, tuple(other["vector"]))
        ]
        nearest_processed: list[dict[str, object]] = []
        if processed:
            distances = [
                (vector_l1_distance(vector, tuple(other["vector"])), other["id"])
                for other in processed
            ]
            min_distance = min(distance for distance, _ in distances)
            nearest_processed = [
                {"id": item_id, "l1_distance": distance}
                for distance, item_id in distances
                if distance == min_distance
            ]
        enriched = dict(record)
        enriched["dominated_by_unprocessed"] = dominated_by_unprocessed
        enriched["is_unprocessed_frontier"] = not dominated_by_unprocessed
        enriched["dominates_processed"] = dominates_processed
        enriched["dominated_by_processed"] = dominated_by_processed
        enriched["nearest_processed"] = nearest_processed
        analyzed_unprocessed.append(enriched)

    frontier = [
        record
        for record in analyzed_unprocessed
        if record["is_unprocessed_frontier"]
    ]
    out = {
        "source": str(args.partition),
        "key_detail": payload.get("key_detail"),
        "processed_class_count": len(processed),
        "unprocessed_class_count": len(unprocessed),
        "mixed_class_count": len(mixed),
        "unprocessed_frontier_count": len(frontier),
        "unprocessed_with_processed_below_count": sum(
            1 for record in analyzed_unprocessed if record["dominates_processed"]
        ),
        "frontier_with_processed_below_count": sum(
            1 for record in frontier if record["dominates_processed"]
        ),
        "processed_classes": processed,
        "unprocessed_frontier": frontier,
        "unprocessed_classes": analyzed_unprocessed,
        "mixed_classes": mixed,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def matrix_vector_deltas_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.frontier.read_text(encoding="utf-8"))
    records = list(payload["processed_classes"]) + list(payload["unprocessed_classes"])
    by_id = {str(record["id"]): record for record in records}
    if args.base_id not in by_id:
        raise ValueError(f"base id {args.base_id!r} is not in frontier artifact")
    base = by_id[args.base_id]
    base_vector = tuple(int(value) for value in base["vector"])

    groups: dict[str, dict[str, object]] = {}
    class_records: list[dict[str, object]] = []
    for record in records:
        vector = tuple(int(value) for value in record["vector"])
        delta = tuple(value - base_value for value, base_value in zip(vector, base_vector))
        state = (
            "processed"
            if int(record.get("processed_bucket_count", 0)) > 0
            else "unprocessed"
        )
        class_record = {
            "id": record["id"],
            "state": state,
            "delta": list(delta),
            "nonnegative_from_base": all(value >= 0 for value in delta),
            "adjacent_delta": list(delta[:3]),
            "skip_delta": list(delta[3:]),
            "vector": record["vector"],
            "adjacent_vector": record["adjacent_vector"],
            "skip_vector": record["skip_vector"],
            "min_lower_orientation_probability": record[
                "min_lower_orientation_probability"
            ],
            "feature_key": record["feature_key"],
        }
        class_records.append(class_record)
        group = groups.setdefault(
            ",".join(str(value) for value in delta),
            {
                "delta": list(delta),
                "adjacent_delta": list(delta[:3]),
                "skip_delta": list(delta[3:]),
                "processed_ids": [],
                "unprocessed_ids": [],
                "min_lower_orientation_probability": record[
                    "min_lower_orientation_probability"
                ],
            },
        )
        group[f"{state}_ids"].append(record["id"])
        if Fraction(*record["min_lower_orientation_probability"]) < Fraction(
            *group["min_lower_orientation_probability"]
        ):
            group["min_lower_orientation_probability"] = record[
                "min_lower_orientation_probability"
            ]

    delta_groups = sorted(
        groups.values(),
        key=lambda group: (
            Fraction(*group["min_lower_orientation_probability"]),
            group["delta"],
        ),
    )
    out = {
        "source": str(args.frontier),
        "base_id": args.base_id,
        "base_vector": list(base_vector),
        "class_count": len(class_records),
        "delta_group_count": len(delta_groups),
        "processed_delta_group_count": sum(
            1 for group in delta_groups if group["processed_ids"]
        ),
        "unprocessed_delta_group_count": sum(
            1 for group in delta_groups if group["unprocessed_ids"]
        ),
        "mixed_delta_group_count": sum(
            1
            for group in delta_groups
            if group["processed_ids"] and group["unprocessed_ids"]
        ),
        "nonnegative_from_base_count": sum(
            1 for record in class_records if record["nonnegative_from_base"]
        ),
        "delta_groups": delta_groups,
        "classes": sorted(
            class_records,
            key=lambda record: (
                Fraction(*record["min_lower_orientation_probability"]),
                record["state"],
                record["id"],
            ),
        ),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def bucket_members_command(args: argparse.Namespace) -> int:
    shape_filter = parse_rank_shape(args.rank_shape)
    records: list[dict[str, object]] = []
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
            profile = structural_profile(poset)
            signature = profile_signature(profile, args.signature)
            if signature != args.bucket:
                continue
            lower = Fraction(*best_pair["lower_orientation_probability"])
            records.append(
                {
                    "n": n,
                    "lower_orientation_probability": [
                        lower.numerator,
                        lower.denominator,
                    ],
                    "best_pair": best_pair,
                    "relations": report["relations"],
                    "linear_extensions": report["linear_extensions"],
                    "profile": profile,
                    "rank_normal_form": rank_normal_form(poset),
                    "signature": signature,
                }
            )
    records.sort(
        key=lambda item: (
            Fraction(*item["lower_orientation_probability"]),
            item["linear_extensions"],
            len(item["relations"]),
        )
    )
    payload = {
        "max_n": args.max_n,
        "width": args.width,
        "height": args.height,
        "rank_shape": list(shape_filter) if shape_filter else None,
        "signature_mode": args.signature,
        "bucket": args.bucket,
        "record_count": len(records),
        "records": records,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def cover_matrix_form_records(
    shape: tuple[int, ...],
    matrix: tuple[tuple[int, ...], ...],
    *,
    only_width: int | None = None,
    only_height: int | None = None,
) -> list[dict[str, object]]:
    if len(matrix) != len(shape):
        raise ValueError("cover matrix dimensions must match rank shape")
    layers = layered_items_from_shape(shape)
    edge_choices: list[list[tuple[Relation, ...]]] = []
    for lower_rank, row in enumerate(matrix):
        for upper_rank, count in enumerate(row):
            if count == 0:
                continue
            if lower_rank >= upper_rank:
                raise ValueError("cover matrix may only use upward rank entries")
            possible_edges = [
                (lower, upper)
                for lower in layers[lower_rank]
                for upper in layers[upper_rank]
            ]
            if count > len(possible_edges):
                raise ValueError(
                    f"cover matrix entry {lower_rank},{upper_rank} exceeds possible edges"
                )
            edge_choices.append(list(itertools.combinations(possible_edges, count)))

    forms: dict[tuple[str, ...], dict[str, object]] = {}
    for choice in itertools.product(*edge_choices):
        relation_seed = list(itertools.chain.from_iterable(choice))
        try:
            poset = make_poset(sum(shape), relation_seed)
        except ValueError:
            continue
        profile = structural_profile(poset)
        if tuple(profile["rank_layer_sizes"]) != shape:
            continue
        if cover_rank_matrix(poset) != [list(row) for row in matrix]:
            continue
        actual_covers = set(covers(poset))
        if actual_covers != set(relation_seed):
            continue
        if only_width is not None and width(poset) != only_width:
            continue
        if only_height is not None and height(poset) != only_height:
            continue
        normal = rank_normal_form(poset)
        key = tuple(normal["cover_relations"])
        report = balance_report(poset)
        forms.setdefault(
            key,
            {
                "cover_relations": normal["cover_relations"],
                "relations": normal["relations"],
                "rank_layers": normal["rank_layers"],
                "linear_extensions": count_linear_extensions(poset),
                "width": width(poset),
                "height": height(poset),
                "best_pair": report["best_pair"],
                "rank_normal_form": normal,
            },
        )
    return [forms[key] for key in sorted(forms)]


def cover_matrix_forms_command(args: argparse.Namespace) -> int:
    shape = parse_rank_shape(args.rank_shape)
    if shape is None:
        raise ValueError("cover-matrix-forms requires --rank-shape")
    matrix = parse_cover_matrix(args.cover_matrix)
    records = cover_matrix_form_records(
        shape,
        matrix,
        only_width=args.width,
        only_height=args.height,
    )
    payload = {
        "rank_shape": list(shape),
        "cover_matrix": [list(row) for row in matrix],
        "width": args.width,
        "height": args.height,
        "form_count": len(records),
        "forms": records,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def cover_matrix_from_vectors(
    rank_count: int,
    adjacent: Sequence[int],
    skip: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    if len(adjacent) != rank_count - 1:
        raise ValueError("adjacent vector length must be rank_count - 1")
    expected_skip = (rank_count - 1) * (rank_count - 2) // 2
    if len(skip) != expected_skip:
        raise ValueError("skip vector has wrong length for rank_count")
    matrix = [[0] * rank_count for _ in range(rank_count)]
    for rank, value in enumerate(adjacent):
        matrix[rank][rank + 1] = int(value)
    skip_index = 0
    for lower in range(rank_count):
        for upper in range(lower + 2, rank_count):
            matrix[lower][upper] = int(skip[skip_index])
            skip_index += 1
    return tuple(tuple(row) for row in matrix)


def matrix_vector_form_ledger_command(args: argparse.Namespace) -> int:
    shape = parse_rank_shape(args.rank_shape)
    if shape is None:
        raise ValueError("matrix-vector-form-ledger requires --rank-shape")
    payload = json.loads(args.frontier.read_text(encoding="utf-8"))
    records = list(payload["processed_classes"]) + list(payload["unprocessed_classes"])
    by_id = {str(record["id"]): record for record in records}
    requested_ids = [item.strip() for item in args.ids.split(",") if item.strip()]
    class_ledgers: list[dict[str, object]] = []
    for item_id in requested_ids:
        if item_id not in by_id:
            raise ValueError(f"class id {item_id!r} is not in frontier artifact")
        record = by_id[item_id]
        adjacent = [int(value) for value in record["adjacent_vector"]]
        skip = [int(value) for value in record["skip_vector"]]
        matrix = cover_matrix_from_vectors(len(shape), adjacent, skip)
        forms = cover_matrix_form_records(
            shape,
            matrix,
            only_width=args.width,
            only_height=args.height,
        )
        min_lower: list[int] | None = None
        for form in forms:
            best_pair = form.get("best_pair")
            if not isinstance(best_pair, dict):
                continue
            lower = best_pair.get("lower_orientation_probability")
            if not isinstance(lower, list):
                continue
            if min_lower is None or Fraction(*lower) < Fraction(*min_lower):
                min_lower = [int(lower[0]), int(lower[1])]
        state = (
            "processed"
            if int(record.get("processed_bucket_count", 0)) > 0
            else "unprocessed"
        )
        class_ledgers.append(
            {
                "id": item_id,
                "state": state,
                "adjacent_vector": adjacent,
                "skip_vector": skip,
                "cover_matrix": [list(row) for row in matrix],
                "source_min_lower_orientation_probability": record[
                    "min_lower_orientation_probability"
                ],
                "ledger_min_lower_orientation_probability": min_lower,
                "form_count": len(forms),
                "forms": forms,
            }
        )
    out = {
        "source": str(args.frontier),
        "rank_shape": list(shape),
        "width": args.width,
        "height": args.height,
        "ids": requested_ids,
        "class_count": len(class_ledgers),
        "total_form_count": sum(int(item["form_count"]) for item in class_ledgers),
        "classes": class_ledgers,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def matrix_vector_named_cases_command(args: argparse.Namespace) -> int:
    payload = json.loads(args.ledger.read_text(encoding="utf-8"))
    requested_ids = {item.strip() for item in args.ids.split(",") if item.strip()}
    if not requested_ids:
        raise ValueError("matrix-vector-named-cases requires at least one id")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    summary: list[dict[str, object]] = []
    for class_record in payload["classes"]:
        class_id = str(class_record["id"])
        if class_id not in requested_ids:
            continue
        for index, form in enumerate(class_record["forms"], start=1):
            normal = form["rank_normal_form"]
            best_pair = normal.get("best_pair")
            if not isinstance(best_pair, dict) or not isinstance(best_pair.get("pair"), list):
                raise ValueError(f"class {class_id} form {index} has no named best pair")
            case_name = f"{class_id.lower()}-form-{index}"
            case_payload = {
                "case": case_name,
                "source_class": class_id,
                "source_form_index": index,
                "labels": list(normal["label_by_item"].values()),
                "cover_relations": normal["cover_relations"],
                "check_pairs": [best_pair["pair"]],
            }
            output = args.output_dir / f"{case_name}.json"
            output.write_text(json.dumps(case_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            written.append(str(output))
            summary.append(
                {
                    "case": case_name,
                    "class": class_id,
                    "form_index": index,
                    "check_pair": best_pair["pair"],
                    "lower_orientation_probability": best_pair[
                        "lower_orientation_probability"
                    ],
                    "path": str(output),
                }
            )
    missing = sorted(requested_ids - {item["class"] for item in summary})
    if missing:
        raise ValueError(f"requested ids not found in ledger: {', '.join(missing)}")
    out = {
        "source": str(args.ledger),
        "ids": sorted(requested_ids),
        "case_count": len(summary),
        "cases": summary,
        "written": written,
    }
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("poset", type=Path)
    analyze_parser.set_defaults(func=analyze_command)

    named_case_parser = subparsers.add_parser("named-case")
    named_case_parser.add_argument("case", type=Path)
    named_case_parser.add_argument("--output", type=Path)
    named_case_parser.set_defaults(func=named_case_command)

    named_case_recurrence_parser = subparsers.add_parser("named-case-recurrence")
    named_case_recurrence_parser.add_argument("case", type=Path)
    named_case_recurrence_parser.add_argument("--depth", type=int, default=1)
    named_case_recurrence_parser.add_argument("--output", type=Path)
    named_case_recurrence_parser.set_defaults(func=named_case_recurrence_command)

    mechanism_search_parser = subparsers.add_parser("named-case-mechanism-search")
    mechanism_search_parser.add_argument("case", type=Path)
    mechanism_search_parser.add_argument("--max-depth", type=int, default=5)
    mechanism_search_parser.add_argument("--output", type=Path)
    mechanism_search_parser.set_defaults(func=named_case_mechanism_search_command)

    mechanism_batch_parser = subparsers.add_parser("named-case-mechanism-batch")
    mechanism_batch_parser.add_argument("case_dirs", nargs="+", type=Path)
    mechanism_batch_parser.add_argument("--max-depth", type=int, default=5)
    mechanism_batch_parser.add_argument("--output", type=Path)
    mechanism_batch_parser.set_defaults(func=named_case_mechanism_batch_command)

    leaf_summary_parser = subparsers.add_parser("recurrence-leaf-summary")
    leaf_summary_parser.add_argument("recurrence", type=Path)
    leaf_summary_parser.add_argument("--output", type=Path)
    leaf_summary_parser.set_defaults(func=recurrence_leaf_summary_command)

    mechanism_parser = subparsers.add_parser("recurrence-mechanism-summary")
    mechanism_parser.add_argument("recurrence", type=Path)
    mechanism_parser.add_argument("--output", type=Path)
    mechanism_parser.set_defaults(func=recurrence_mechanism_summary_command)

    forced_block_parser = subparsers.add_parser("recurrence-forced-block-obligations")
    forced_block_parser.add_argument("recurrence", type=Path)
    forced_block_parser.add_argument("--output", type=Path)
    forced_block_parser.set_defaults(func=recurrence_forced_block_obligations_command)

    leaf_compare_parser = subparsers.add_parser("recurrence-leaf-compare")
    leaf_compare_parser.add_argument("left", type=Path)
    leaf_compare_parser.add_argument("right", type=Path)
    leaf_compare_parser.add_argument("--output", type=Path)
    leaf_compare_parser.set_defaults(func=recurrence_leaf_compare_command)

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
    classes_parser.add_argument(
        "--signature",
        choices=["coarse", "matrix", "fine"],
        default="coarse",
    )
    classes_parser.add_argument("--examples-per-bucket", type=int, default=2)
    classes_parser.add_argument("--output", type=Path)
    classes_parser.set_defaults(func=shape_classes_command)

    feature_parser = subparsers.add_parser("matrix-feature-partition")
    feature_parser.add_argument("classes", type=Path)
    feature_parser.add_argument("--threshold")
    feature_parser.add_argument("--processed-threshold")
    feature_parser.add_argument(
        "--key-detail",
        choices=["coarse", "vector"],
        default="coarse",
    )
    feature_parser.add_argument("--output", type=Path)
    feature_parser.set_defaults(func=matrix_feature_partition_command)

    frontier_parser = subparsers.add_parser("matrix-vector-frontier")
    frontier_parser.add_argument("partition", type=Path)
    frontier_parser.add_argument("--output", type=Path)
    frontier_parser.set_defaults(func=matrix_vector_frontier_command)

    deltas_parser = subparsers.add_parser("matrix-vector-deltas")
    deltas_parser.add_argument("frontier", type=Path)
    deltas_parser.add_argument("--base-id", required=True)
    deltas_parser.add_argument("--output", type=Path)
    deltas_parser.set_defaults(func=matrix_vector_deltas_command)

    bucket_parser = subparsers.add_parser("bucket-members")
    bucket_parser.add_argument("--max-n", type=int, default=7)
    bucket_parser.add_argument("--width", type=int, required=True)
    bucket_parser.add_argument("--height", type=int)
    bucket_parser.add_argument("--rank-shape")
    bucket_parser.add_argument(
        "--signature",
        choices=["coarse", "matrix", "fine"],
        default="matrix",
    )
    bucket_parser.add_argument("--bucket", required=True)
    bucket_parser.add_argument("--output", type=Path)
    bucket_parser.set_defaults(func=bucket_members_command)

    matrix_forms_parser = subparsers.add_parser("cover-matrix-forms")
    matrix_forms_parser.add_argument("--rank-shape", required=True)
    matrix_forms_parser.add_argument("--cover-matrix", required=True)
    matrix_forms_parser.add_argument("--width", type=int)
    matrix_forms_parser.add_argument("--height", type=int)
    matrix_forms_parser.add_argument("--output", type=Path)
    matrix_forms_parser.set_defaults(func=cover_matrix_forms_command)

    vector_forms_parser = subparsers.add_parser("matrix-vector-form-ledger")
    vector_forms_parser.add_argument("frontier", type=Path)
    vector_forms_parser.add_argument("--ids", required=True)
    vector_forms_parser.add_argument("--rank-shape", required=True)
    vector_forms_parser.add_argument("--width", type=int)
    vector_forms_parser.add_argument("--height", type=int)
    vector_forms_parser.add_argument("--output", type=Path)
    vector_forms_parser.set_defaults(func=matrix_vector_form_ledger_command)

    vector_cases_parser = subparsers.add_parser("matrix-vector-named-cases")
    vector_cases_parser.add_argument("ledger", type=Path)
    vector_cases_parser.add_argument("--ids", required=True)
    vector_cases_parser.add_argument("--output-dir", type=Path, required=True)
    vector_cases_parser.add_argument("--summary", type=Path)
    vector_cases_parser.set_defaults(func=matrix_vector_named_cases_command)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
