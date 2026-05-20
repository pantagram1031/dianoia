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
