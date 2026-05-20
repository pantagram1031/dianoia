# R013 Near-Boundary Synthesis

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Purpose

This note consolidates the completed near-boundary matrix-bucket work for the
restricted class:

- width `3`
- height `4`
- rank-layer shape `2,2,2,1`
- seven elements

The goal is to stop treating each bucket as an isolated calculation and start
extracting proof obligations for a reusable width-3 lemma.

## Completed Near-Boundary Buckets

| Rank | Profiles | Bucket minimum | Proof artifact |
|------|----------|----------------|----------------|
| 1 | 3 | `14/39` | `BRANCH_ENUMERATION_LEDGER.md` |
| 2 | 1 | `2/5` | `SECOND_MATRIX_BUCKET_NOTES.md` |
| 3 | 6 | `2/5` | `THIRD_MATRIX_BUCKET_NOTES.md` |
| 4 | 4 | `2/5` | `FOURTH_MATRIX_BUCKET_NOTES.md` |
| 5 | 1 | `2/5` | `FIFTH_MATRIX_BUCKET_NOTES.md` |
| 6 | 1 | `2/5` | `SIXTH_MATRIX_BUCKET_NOTES.md` |
| 7 | 2 | `13/32` | `SEVENTH_MATRIX_BUCKET_NOTES.md` |
| 8 | 2 | `13/32` | `EIGHTH_MATRIX_BUCKET_NOTES.md` |

These eight buckets cover the current near-boundary queue in
`MATRIX_BUCKET_ROADMAP.md`: all buckets with minimum at most `13/32`.

## Repeated Counting Pattern

The hand counts repeatedly reduce to a small set of residual posets after one
or two minimal choices.

### Pattern A: Two Lower Bounds Before One Top

Residual form:

```text
x<z ; y<z ; optional free element w
```

Without `w`, the two linear extensions are:

```text
x,y,z
y,x,z
```

With a free element `w`, the count is `8`: the top `z` must appear after
`x,y`, while `w` can be inserted freely. The two orientations of `(x,y)` split
evenly as `4` and `4`.

This pattern appears in:

- `SIXTH_MATRIX_BUCKET_NOTES.md`, prefix `a,d,b`.
- `EIGHTH_MATRIX_BUCKET_NOTES.md`, prefix `a,d,b`.

### Pattern B: One Fork Plus One Chain-to-Top

Residual form:

```text
d<e,f ; e<g
```

The count is `3`: after `d`, the remaining elements are `e,f,g` with `e<g`.

This pattern appears in:

- `FIFTH_MATRIX_BUCKET_NOTES.md`, prefix `a,b,c`.
- `EIGHTH_MATRIX_BUCKET_NOTES.md`, shared residual after choosing `c`.

### Pattern C: Two Independent Top Constraints

Residual form:

```text
c<g ; e<g
```

with one free element `f` has `8` extensions and splits any comparison
between `c` and `e` as `4/4`. With a prior forced lower element `b<c,e`, it
has only the two base orders:

```text
b,c,e,g
b,e,c,g
```

and splits `1/1`.

This pattern appears in:

- `EIGHTH_MATRIX_BUCKET_NOTES.md`, prefix `a,d`.
- `SEVENTH_MATRIX_BUCKET_NOTES.md`, prefix `a,d` after analogous relabeling.

## Lemma Candidate

Candidate restricted lemma:

> In every width-3, height-4, rank-layer-shape `2,2,2,1` poset on seven
> elements, there is an incomparable pair whose lower orientation probability
> is at least `14/39`.

Current evidence:

- Exact enumeration gives 103 unlabeled profiles in the restricted class.
- The global restricted minimum is `14/39`.
- The extremal matrix bucket has a hand enumeration for all three
  rank-normal forms.
- Every matrix bucket with minimum at most `13/32` now has a direct derivation,
  replay artifact, and hand-counted weak form.

This is still not a theorem because the remaining matrix buckets are not yet
covered by a human-readable argument. The exact enumeration proves only the
finite computation, not a satisfying structural proof.

## Proof Obligations

To turn the synthesis into a restricted lemma, dianoia needs one of:

1. A complete table proof: for every remaining matrix bucket, identify a
   balanced pair and reduce its count to a small residual pattern.
2. A dominance proof: show every unprocessed matrix bucket contains, deletes
   to, or otherwise dominates one of the processed safer buckets without
   decreasing the best lower-orientation probability below `14/39`.
3. A rank-layer local lemma: prove that certain degree patterns in the
   `2,2,2,1` cover matrix force a `2/5` or better pair, leaving only the
   already processed extremal matrix for exact enumeration.

The most promising route is (3). The completed buckets suggest that extra
cover density between adjacent middle layers tends to create a `2/5` or
`13/32` pair by forcing shallow residual branch counts. The extremal `14/39`
bucket is therefore likely the sparse exceptional matrix rather than one case
among many.

## Next Concrete Step

Add a command or note that partitions the 67 matrix buckets by simple cover
features:

- row sums from layer 0 to layer 1;
- row sums from layer 1 to layer 2;
- whether a layer-1 element covers both layer-2 elements;
- whether a layer-2 element is covered by both layer-1 elements;
- existence of an immediate `2/5` witness pair.

Then use this feature table to select a structural dominance statement instead
of continuing by rank order alone.

## Claim Discipline

No `CLAIMS.md` row. This is a synthesis of restricted finite subcase work and
a proof-strategy note, not a proof of the published open problem.
