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
5. Wired the small-poset check into `tools/verify_all.py`.

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

## Outcome

`PARTIAL-PROGRESS`. This is not a new mathematical contribution; the small
cases are not novel. It does create a general finite-poset exact-counting
acceptance gate for future R013 attempts, and it broadens dianoia's active
research behavior beyond the R020 no-three-in-line verifier.
