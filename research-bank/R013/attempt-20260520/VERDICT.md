# R013 Attempt Verdict

date: 2026-05-20
verdict: PARTIAL-PROGRESS

## Head-to-Head

- Raw route: `NO-PROGRESS`; located the conjectural target but produced no
  replayable artifact.
- Dianoia route: `PARTIAL-PROGRESS`; produced an exact finite-poset analyzer,
  tests, a replayed exhaustive labeled small-poset check through five elements,
  a canonical unlabeled check through seven elements, and a focused width-3
  frontier summary with extremal profiles.
- The proposed rank-layer target class was classified exactly for `n=7`.

## Exact Evidence

- `tools/poset_balance.py`
- `tests/test_poset_balance.py`
- `research-bank/R013/attempt-20260520/small-posets-n5.json`
- `research-bank/R013/attempt-20260520/unlabeled-posets-n6.json`
- `research-bank/R013/attempt-20260520/unlabeled-posets-n7.json`
- `research-bank/R013/attempt-20260520/width3-unlabeled-n7.json`
- `research-bank/R013/attempt-20260520/width3-extremals-n7.json`
- `research-bank/R013/attempt-20260520/width3-rank2221-n7.json`
- `research-bank/R013/attempt-20260520/width3-rank2221-extremals-n7.json`
- `research-bank/R013/attempt-20260520/width3-rank2221-shape-classes-n7.json`
- `research-bank/R013/attempt-20260520/WIDTH3_EXTREMAL_NOTES.md`
- `research-bank/R013/attempt-20260520/STRUCTURAL_NOTES.md`
- `tools/verify_all.py`

The small-poset artifact reports:

- `n=2`: 3 labeled posets, 1 non-chain.
- `n=3`: 19 labeled posets, 13 non-chains.
- `n=4`: 219 labeled posets, 195 non-chains.
- `n=5`: 4231 labeled posets, 4111 non-chains.
- `counterexample_count: 0`.

The unlabeled seven-element artifact reports:

- `n=7`: 2045 unlabeled posets, 2044 non-chains.
- `counterexample_count: 0`.
- width distribution: 1 chain, 224 width-2, 1060 width-3, 636 width-4,
  112 width-5, 11 width-6, and 1 antichain.
- focused width-3 worst best-pair lower probability at `n=7`: `14/39`.
- extremal profile proof target: width 3, height 4, rank-layer shape
  `2,2,2,1`.
- restricted target class: 103 unlabeled profiles, no counterexamples, worst
  best-pair lower probability `14/39`, next worst `2/5`.
- coarse case split: 12 buckets; the `14/39` extremal is in a 24-profile
  bucket, so a finer invariant is still needed.

## Claim Discipline

No `CLAIMS.md` row is added. The check is useful instrumentation and a sanity
baseline, not a new theorem, counterexample, bound improvement, or publishable
connection.
