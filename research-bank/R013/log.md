# Candidate Log

candidate_id: R013

## 2026-05-20 Curation

- Added to P10 bank as `OPEN-VERIFIED`.
- Area: order theory.
- Initial rank: A.
- Initial attack surface: exact linear-extension counting and finite
  small-poset certificate replay.

## 2026-05-20 P11 Attempt 1

- Verdict: `PARTIAL-PROGRESS`.
- Raw route: recorded `NO-PROGRESS` in
  `research-bank/R013/attempt-20260520/RAW.md`; it restated the conjecture but
  produced no exact reusable artifact.
- Dianoia route: added `tools/poset_balance.py`, unit tests, and an exact
  exhaustive labeled-poset check through five elements.
- Replay artifact:
  `research-bank/R013/attempt-20260520/small-posets-n5.json` reports
  `counterexample_count: 0` across all non-chain labeled posets for
  `2 <= n <= 5`.
- Claim discipline: no `CLAIMS.md` row added because this is a small-case
  sanity baseline and verification gate, not a novel result.

## 2026-05-20 P11 Attempt 1B

- Added isomorphism-aware unlabeled poset summaries to avoid overfitting the
  attempt to duplicate labelings.
- Added a poset-native one-point extension generator based on downsets and
  upsets, then used it to enumerate all 318 unlabeled six-element posets.
- Artifact:
  `research-bank/R013/attempt-20260520/unlabeled-posets-n6.json` reports
  `counterexample_count: 0` across 317 non-chain unlabeled six-element posets.
- Structural notes:
  `research-bank/R013/attempt-20260520/STRUCTURAL_NOTES.md` records finite
  search signals: width-2 examples hit the `1/3` boundary, width-3 examples
  remain at least `4/11` in the small data, and width >= 4 examples are loose
  in this range.
- Claim discipline: no `CLAIMS.md` row; these are exact finite observations
  and next-attempt guides, not a new theorem.

## 2026-05-20 P11 Attempt 1C

- Optimized canonical keys with invariant vertex blocks; targeted poset tests
  dropped from roughly 53 seconds to under 4 seconds on the local machine.
- Extended exact canonical replay through all 2045 unlabeled seven-element
  posets:
  `research-bank/R013/attempt-20260520/unlabeled-posets-n7.json`.
- Added width/height filters and a focused width-3 replay:
  `research-bank/R013/attempt-20260520/width3-unlabeled-n7.json`.
- New finite signal: no counterexamples through `n=7`; width 3 worst
  best-pair lower probability is `14/39`, still separated from `1/3`.
- Claim discipline: no `CLAIMS.md` row; the finite data suggests a restricted
  lemma target but does not prove it.

## 2026-05-20 P11 Attempt 1D

- Added an extremal profile command to `tools/poset_balance.py`.
- Generated `research-bank/R013/attempt-20260520/width3-extremals-n7.json`,
  the top 12 width-3 near-boundary profiles through seven elements.
- Added `WIDTH3_EXTREMAL_NOTES.md` with a concrete restricted proof target:
  classify width-3, height-4, rank-layer-shape `2,2,2,1` posets and test
  whether `14/39` is the extremal lower probability in that class.
- Wired a small extremal-profile smoke into `tools/verify_all.py`.
- Claim discipline: no `CLAIMS.md` row; this is a proof target extracted from
  exact finite evidence, not a solved claim.

## 2026-05-20 P11 Attempt 1E

- Added rank-shape filtering to the exact poset tool.
- Classified the restricted target class:
  width 3, height 4, rank-layer-shape `2,2,2,1`.
- Artifact:
  `research-bank/R013/attempt-20260520/width3-rank2221-n7.json` reports
  103 unlabeled profiles, no counterexamples, and worst best-pair lower
  probability `14/39`.
- Artifact:
  `research-bank/R013/attempt-20260520/width3-rank2221-extremals-n7.json`
  records the restricted near-boundary profiles; the next worst lower
  probability after `14/39` is `2/5`.
- Claim discipline: no `CLAIMS.md` row; this sharpens the restricted proof
  target but does not prove novelty or a theorem.

## 2026-05-20 P11 Attempt 1F

- Added a coarse shape-class grouping command.
- Generated
  `research-bank/R013/attempt-20260520/width3-rank2221-shape-classes-n7.json`.
- Result: the 103 restricted profiles split into 12 buckets by rank-layer
  shape, cover-edge count, minimal-element count, and maximal-element count.
- The `14/39` extremal sits in the bucket
  `layers=2,2,2,1|covers=8|mins=2|maxs=2`, which contains 24 profiles.
- Interpretation: the restricted target is sharper, but a proof needs a finer
  case split, likely inter-layer cover matrices or rank-layer vertex-signature
  sequences.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-20 P11 Attempt 1G

- Added proof-relevant rank-layer refinements to the exact poset tool:
  inter-rank cover matrices and sorted per-layer vertex signatures.
- Added `shape-classes --signature matrix` and `shape-classes --signature fine`.
- Generated
  `research-bank/R013/attempt-20260520/width3-rank2221-matrix-shape-classes-n7.json`
  and
  `research-bank/R013/attempt-20260520/width3-rank2221-fine-shape-classes-n7.json`.
- Result: matrix signatures split the 103 restricted profiles into 67 buckets;
  the `14/39` extremal bucket has 3 profiles and cover matrix
  `[[0,2,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]`.
- Result: full per-layer vertex signatures split the class into 103 singleton
  buckets, identifying the extremal exactly but too finely for a final proof.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-20 P11 Attempt 1H

- Extracted the actual three profiles in the matrix bucket containing the
  `14/39` extremal.
- Added `research-bank/R013/attempt-20260520/MATRIX_BUCKET_NOTES.md`.
- Result: the three profiles have best lower probabilities `14/39`, `14/33`,
  and `5/11`; the equality candidate is isolated to one profile inside this
  matrix bucket.
- Next proof move: replace the label-dependent extraction with a
  coordinate-free case split on the bottom-layer and rank-1 layer
  vertex-signature patterns.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-20 P11 Attempt 1I

- Added `bucket-members` extraction to the exact poset tool.
- Generated
  `research-bank/R013/attempt-20260520/width3-rank2221-extremal-matrix-bucket-n7.json`.
- The generated artifact records all three members of the extremal matrix
  bucket, sorted by best lower orientation probability.
- Updated `MATRIX_BUCKET_NOTES.md` to cite the exact generation command.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-20 P11 Attempt 1J

- Added rank-layer normal forms to `bucket-members` records.
- Regenerated
  `research-bank/R013/attempt-20260520/width3-rank2221-extremal-matrix-bucket-n7.json`
  with stable rank labels.
- Added `research-bank/R013/attempt-20260520/RANK_NORMAL_FORM_NOTES.md`.
- Result: the extremal matrix bucket is now expressed as three cover patterns
  on layers `{a,b}`, `{c,d}`, `{e,f}`, `{g}` with exact orientation counts.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-21 P11 Attempt 1K

- Added `named-case` analysis to `tools/poset_balance.py`.
- Added named normal-form inputs and generated reports under
  `research-bank/R013/attempt-20260520/normal-form-cases/`.
- Added `NORMAL_FORM_COUNT_LEDGER.md`.
- Result: Case A/B/C orientation counts are now replayable from named
  cover-relation inputs: `14/39`, `14/33`, and `5/11`.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-21 P11 Attempt 1L

- Added `cover-matrix-forms` to derive rank-normal forms directly from a rank
  shape and cover matrix.
- Generated
  `research-bank/R013/attempt-20260520/width3-rank2221-cover-matrix-forms-n7.json`.
- Added `research-bank/R013/attempt-20260520/COVER_MATRIX_DERIVATION.md`.
- Result: the common matrix, width 3, height 4, and rank shape `2,2,2,1`
  produce exactly three rank-normal forms, matching Cases A/B/C.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-21 P11 Attempt 1M

- Added `named-case-recurrence` to expose first-step minimal-element
  recurrences for named normal-form cases.
- Generated recurrence traces for Cases A/B/C in `normal-form-cases/`.
- Added `RECURRENCE_LEDGER.md`.
- Result: the branch recurrences now show how `14/39`, `14/33`, and `5/11`
  arise from root minimal choices.
- Claim discipline: no `CLAIMS.md` row.

## 2026-05-21 P11 Attempt 1N

- Extended `named-case-recurrence` with a bounded `--depth` option while
  preserving the default root-split output.
- Generated depth-2 recurrence traces for Cases A/B/C:
  `case-a-recurrence-depth2.json`, `case-b-recurrence-depth2.json`, and
  `case-c-recurrence-depth2.json`.
- Updated `RECURRENCE_LEDGER.md` and `STRUCTURAL_NOTES.md` to record the
  second-level branch counts.
- Result: the common-matrix subcase is closer to a hand-checkable proof; the
  remaining work is to replace the residual branch totals with terminal
  chain/shuffle counts.
- Claim discipline: no `CLAIMS.md` row.
