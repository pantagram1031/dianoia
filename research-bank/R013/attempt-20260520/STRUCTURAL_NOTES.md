# R013 Structural Notes From Exact Small Posets

date: 2026-05-20
status: OBSERVATION-NOT-CLAIM

## Scope

The exact check in this attempt covers unlabeled finite posets through seven
elements. It is not a novel theorem and it does not affect `CLAIMS.md`.

Artifacts:

- `small-posets-n5.json`: labeled check through five elements.
- `unlabeled-posets-n5.json`: canonical unlabeled check through five elements.
- `unlabeled-posets-n6.json`: canonical unlabeled check through six elements.
- `unlabeled-posets-n7.json`: canonical unlabeled check through seven elements.
- `width3-unlabeled-n7.json`: focused width-3 canonical summary through seven
  elements.
- `width3-extremals-n7.json`: top width-3 near-boundary profiles through seven
  elements.
- `width3-rank2221-n7.json`: restricted width-3, height-4,
  rank-layer-shape `2,2,2,1` summary.
- `width3-rank2221-extremals-n7.json`: restricted extremal list.
- `width3-rank2221-shape-classes-n7.json`: coarse signature buckets for the
  restricted class.
- `width3-rank2221-matrix-shape-classes-n7.json`: inter-rank cover-matrix
  buckets for the restricted class.
- `width3-rank2221-fine-shape-classes-n7.json`: per-layer vertex-signature
  buckets for exact extremal identification.
- `width3-rank2221-extremal-matrix-bucket-n7.json`: full member list for the
  3-profile matrix bucket containing the `14/39` extremal.
- `WIDTH3_EXTREMAL_NOTES.md`: human-readable proof-target notes.
- `MATRIX_BUCKET_NOTES.md`: three-profile matrix-bucket case split for the
  current extremal subcase.
- `RANK_NORMAL_FORM_NOTES.md`: rank-layer normal-form rewrite of the three
  matrix-bucket cases.
- `tools/poset_balance.py`: exact linear-extension and balanced-pair analyzer.

## Exhaustive Small Evidence

The canonical unlabeled run reports:

| n | unlabeled posets | non-chain posets | counterexamples |
|---|------------------|------------------|-----------------|
| 2 | 2 | 1 | 0 |
| 3 | 5 | 4 | 0 |
| 4 | 16 | 15 | 0 |
| 5 | 63 | 62 | 0 |
| 6 | 318 | 317 | 0 |
| 7 | 2045 | 2044 | 0 |

## Structural Signals

These are search signals only:

- Width 2 is the tight small-family source: the worst best-pair probability
  reaches exactly `1/3` in the `n=3` through `n=7` summaries.
- Width 3 remains separated from the boundary in the small data: the worst
  best-pair lower probability is `4/11` for `n=5` and `n=6`, and `14/39` for
  `n=7`.
- Width 4 first shows nontrivial slack at `n=7`: the worst best-pair lower
  probability is `79/197`.
- Width at least 5 is very loose in this small range: the worst best-pair
  lower probability recorded by the canonical run is `1/2`.

## Next Mathematical Moves

1. Try to prove a restricted width-3 separation lemma suggested by the data:
   for small width-3 posets the best balanced pair appears bounded away from
   `1/3` by at least `1/39`.
2. Add cover-graph/level-shape filters and compare the width-3 extremal
   examples at `n=5`, `n=6`, and `n=7`.
3. Start with the specific proof target in `WIDTH3_EXTREMAL_NOTES.md`:
   classify width-3, height-4, rank-layer-shape `2,2,2,1` posets and determine
   whether `14/39` is the extremal lower probability in that restricted class.
   The exact restricted run now confirms this for all 103 unlabeled profiles
   through `n=7`.
4. Turn `MATRIX_BUCKET_NOTES.md` into a coordinate-free sublemma for the
   3-profile matrix bucket: equality only in Case A, with Cases B and C giving
   `14/33` and `5/11`. `RANK_NORMAL_FORM_NOTES.md` now supplies the stable
   rank-layer names for this proof attempt.
5. Scale canonical generation to `n=8` only after further optimizing
   canonical-key speed or adding targeted filters.

## Honesty Boundary

This note is not a proof, counterexample, bound improvement, or new published
connection. It is a finite exact-search baseline and a guide for the next
attempt.
