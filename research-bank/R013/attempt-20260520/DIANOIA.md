# R013 Dianoia Attempt

date: 2026-05-20
mode: exact finite-poset counting attempt
verdict: PARTIAL-PROGRESS

## Problem

Build a replayable finite certificate path for the 1/3-2/3 conjecture and use
it to test small posets exactly.

## Work Performed

1. Added `tools/poset_balance.py`, an exact finite-poset analyzer.
2. Implemented transitive-closure validation, cycle rejection, linear-extension
   counting by subset dynamic programming, and exact balanced-pair probabilities
   using rational arithmetic.
3. Added `tests/test_poset_balance.py` for antichains, chains, cycle rejection,
   small labeled-poset counts, and exhaustive checking through four elements.
4. Ran the exact labeled-poset enumeration through five elements and wrote:
   `research-bank/R013/attempt-20260520/small-posets-n5.json`.
5. Added canonical unlabeled-family summaries through six elements using a
   poset-native one-point extension generator.
6. Optimized canonical keys using invariant vertex blocks, making the exact
   unlabeled replay fast enough to reach seven elements.
7. Added width/height filters and focused the width-3 frontier through seven
   elements.
8. Added an extremal width profiler and recorded the top width-3 near-boundary
   profiles through seven elements.
9. Added rank-shape filtering and classified the width-3, height-4,
   rank-layer-shape `2,2,2,1` target class.
10. Wired the small-poset and extremal-profile checks into `tools/verify_all.py`.

## Verification

Targeted test:

```powershell
python tests\test_poset_balance.py
```

Result: `Ran 5 tests ... OK`.

Exhaustive check:

```powershell
python tools\poset_balance.py exhaustive-small `
  --max-n 5 `
  --output research-bank\R013\attempt-20260520\small-posets-n5.json
```

Result: `counterexample_count: 0` across all labeled non-chain posets through
five elements.

Canonical unlabeled check:

```powershell
python tools\poset_balance.py exhaustive-unlabeled `
  --max-n 6 `
  --output research-bank\R013\attempt-20260520\unlabeled-posets-n6.json
```

Result: `counterexample_count: 0` across all unlabeled non-chain posets through
six elements.

Extended canonical unlabeled check:

```powershell
python tools\poset_balance.py exhaustive-unlabeled `
  --max-n 7 `
  --output research-bank\R013\attempt-20260520\unlabeled-posets-n7.json
```

Result: `counterexample_count: 0` across all 2044 non-chain unlabeled posets
through seven elements.

Focused width-3 check:

```powershell
python tools\poset_balance.py exhaustive-unlabeled `
  --max-n 7 `
  --width 3 `
  --output research-bank\R013\attempt-20260520\width3-unlabeled-n7.json
```

Result: `counterexample_count: 0`; the worst best-pair lower probability at
`n=7` is `14/39`.

Extremal profile command:

```powershell
python tools\poset_balance.py extremal-width `
  --max-n 7 `
  --width 3 `
  --limit 12 `
  --output research-bank\R013\attempt-20260520\width3-extremals-n7.json
```

Result: the top profile is a seven-element width-3, height-4 poset with
rank-layer sizes `2,2,2,1`, 39 linear extensions, and best-pair lower
probability `14/39`.

Restricted rank-shape command:

```powershell
python tools\poset_balance.py exhaustive-unlabeled `
  --max-n 7 `
  --width 3 `
  --height 4 `
  --rank-shape 2,2,2,1 `
  --output research-bank\R013\attempt-20260520\width3-rank2221-n7.json
```

Result: 103 unlabeled profiles, no counterexamples, and worst best-pair lower
probability `14/39`.

Restricted shape-class command:

```powershell
python tools\poset_balance.py shape-classes `
  --max-n 7 `
  --width 3 `
  --height 4 `
  --rank-shape 2,2,2,1 `
  --examples-per-bucket 3 `
  --output research-bank\R013\attempt-20260520\width3-rank2221-shape-classes-n7.json
```

Result: 12 coarse buckets. The `14/39` extremal lies in the
`layers=2,2,2,1|covers=8|mins=2|maxs=2` bucket, which still contains 24
profiles.

Restricted matrix-signature command:

```powershell
python tools\poset_balance.py shape-classes `
  --max-n 7 `
  --width 3 `
  --height 4 `
  --rank-shape 2,2,2,1 `
  --signature matrix `
  --examples-per-bucket 3 `
  --output research-bank\R013\attempt-20260520\width3-rank2221-matrix-shape-classes-n7.json
```

Result: 67 matrix buckets. The `14/39` extremal lies in the bucket with cover
matrix `[[0,2,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]`, which contains 3 profiles.

Restricted fine-signature command:

```powershell
python tools\poset_balance.py shape-classes `
  --max-n 7 `
  --width 3 `
  --height 4 `
  --rank-shape 2,2,2,1 `
  --signature fine `
  --examples-per-bucket 3 `
  --output research-bank\R013\attempt-20260520\width3-rank2221-fine-shape-classes-n7.json
```

Result: 103 fine buckets over 103 profiles. The `14/39` extremal bucket is a
singleton.

## Outcome

`PARTIAL-PROGRESS`. This is not a new mathematical contribution; the small
cases are not novel. It does create a general finite-poset exact-counting
acceptance gate for future R013 attempts, and it broadens dianoia's active
research behavior beyond the R020 no-three-in-line verifier.
