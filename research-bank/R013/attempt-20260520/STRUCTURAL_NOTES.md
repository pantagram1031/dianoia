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
- `NORMAL_FORM_COUNT_LEDGER.md`: replayable named-case count certificates for
  the three rank-normal cases.
- `RECURRENCE_LEDGER.md`: depth-2 minimal-element recurrence summaries for
  the three named cases.
- `BRANCH_ENUMERATION_LEDGER.md`: hand enumeration of the residual depth-2
  branch counts for the common matrix subcase.
- `MATRIX_BUCKET_ROADMAP.md`: ranked matrix-bucket proof queue for the
  restricted class.
- `SECOND_MATRIX_BUCKET_NOTES.md`: singleton second-bucket derivation and hand
  count, giving lower orientation probability `2/5`.
- `THIRD_MATRIX_BUCKET_NOTES.md`: six-form third-bucket derivation with exact
  replay counts and a hand count for the equality form.
- `FOURTH_MATRIX_BUCKET_NOTES.md`: four-form fourth-bucket derivation with
  exact replay counts and a hand count for the equality form.
- `FIFTH_MATRIX_BUCKET_NOTES.md`: singleton fifth-bucket derivation with exact
  replay counts and a hand count for the pair `(c,d)`.
- `SIXTH_MATRIX_BUCKET_NOTES.md`: singleton sixth-bucket derivation with exact
  replay counts and a hand count for the pair `(e,c)`.
- `SEVENTH_MATRIX_BUCKET_NOTES.md`: first `13/32` matrix bucket derivation with
  exact replay counts for both forms and a hand count for the weaker form.
- `EIGHTH_MATRIX_BUCKET_NOTES.md`: second `13/32` matrix bucket derivation with
  exact replay counts for both forms and a hand count for the weaker form.
- `NEAR_BOUNDARY_SYNTHESIS.md`: consolidation of the processed near-boundary
  buckets into reusable residual-count patterns and proof obligations for a
  restricted width-3 lemma.
- `FEATURE_PARTITION_NOTES.md`: interpretation of the thresholded matrix
  feature partition that separates the processed near-boundary buckets by
  cover-density and skip-cover features.
- `ALL_FEATURE_PARTITION_NOTES.md`: interpretation of the all-67-bucket
  partition with processed/unprocessed labels and mixed feature classes.
- `VECTOR_FEATURE_PARTITION_NOTES.md`: interpretation of the vector-detail
  partition; exact adjacent/skip vectors separate processed and unprocessed
  feature classes.
- `PROCESSED_VECTOR_CLASSES.md`: compact P1-P8 table of processed vector
  classes and the candidate vector-class dichotomy.
- `VECTOR_FRONTIER_NOTES.md`: componentwise vector-frontier analysis showing
  a unique minimal unprocessed frontier U6 and refuting the naive dominance
  story.
- `VECTOR_DELTA_CLASSIFICATION.md`: all vector classes as nonnegative deltas
  from U6, isolating eight dangerous processed delta groups.
- `U6_DANGEROUS_FORM_LEDGER_NOTES.md`: 22 rank-normal forms for U6 and P1-P8,
  with ledger minima matching source minima.
- `BOUNDARY_RECURRENCE_NOTES.md`: named-case extraction and recurrence
  comparison for the two `13/32` boundary forms P7/P8.
- `COVER_MATRIX_DERIVATION.md`: direct derivation of the three rank-normal
  forms from the common cover matrix.
- `width3-rank2221-cover-matrix-forms-n7.json`: generated direct derivation
  artifact for the common cover matrix.
- `normal-form-cases/`: named case inputs and generated count reports.
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
4. Replace the remaining computational subcase with a hand proof:
   `COVER_MATRIX_DERIVATION.md` derives the three normal forms from the common
   cover matrix, `NORMAL_FORM_COUNT_LEDGER.md` certifies their counts, and
   `RECURRENCE_LEDGER.md` now exposes two recurrence levels for a
   hand-checkable branch proof. `BRANCH_ENUMERATION_LEDGER.md` now
   hand-enumerates those residual branch counts for the common matrix subcase.
5. Continue the matrix-bucket proof queue: `SECOND_MATRIX_BUCKET_NOTES.md`
   handles the singleton `2/5` bucket; `THIRD_MATRIX_BUCKET_NOTES.md` handles
   the next six-profile `2/5` bucket; `FOURTH_MATRIX_BUCKET_NOTES.md` handles
   the next four-profile `2/5` bucket; `FIFTH_MATRIX_BUCKET_NOTES.md` handles
   another singleton `2/5` bucket; `SIXTH_MATRIX_BUCKET_NOTES.md` handles the
   remaining singleton `2/5` bucket; `SEVENTH_MATRIX_BUCKET_NOTES.md` handles
   the first `13/32` bucket; `EIGHTH_MATRIX_BUCKET_NOTES.md` handles the
   second `13/32` bucket. `NEAR_BOUNDARY_SYNTHESIS.md` now extracts common
   residual-count patterns. `FEATURE_PARTITION_NOTES.md` now interprets the
   thresholded feature partition. The next nontrivial target is to partition
   all 67 matrix buckets and mark which feature classes remain unprocessed.
   `ALL_FEATURE_PARTITION_NOTES.md` now records that partition and identifies
   two mixed feature groups; the next step is to refine the feature key using
   exact adjacent/skip vectors or shadowed-skip data.
   `VECTOR_FEATURE_PARTITION_NOTES.md` performs the exact-vector refinement and
   reduces mixed processed/unprocessed groups to zero. The next proof-support
   target is an eight-row processed vector-class table and a dominance argument
   for the vector classes outside that table.
   `PROCESSED_VECTOR_CLASSES.md` now provides the P1-P8 table; the next
   mathematical step is to prove or refute the vector-class dichotomy.
   `VECTOR_FRONTIER_NOTES.md` refines this: prove the no-skip frontier U6, then
   classify skip additions into dangerous P1-P8 placements versus slack
   placements.
   `VECTOR_DELTA_CLASSIFICATION.md` now provides that classification; the next
   step is count/recurrence ledgers for U6 and the dangerous deltas, then a
   uniform proof attempt for the non-dangerous deltas.
   `U6_DANGEROUS_FORM_LEDGER_NOTES.md` now reduces U6 and P1-P8 to 22
   rank-normal forms; next extract named cases or recurrence ledgers for P7/P8.
   `BOUNDARY_RECURRENCE_NOTES.md` now extracts those cases and compares their
   depth-2 recurrences; next seek a shared injection/pairing proof for the
   common `19/13` split.
6. Scale canonical generation to `n=8` only after further optimizing
   canonical-key speed or adding targeted filters.

## Honesty Boundary

This note is not a proof, counterexample, bound improvement, or new published
connection. It is a finite exact-search baseline and a guide for the next
attempt.
