# R013 Attempt Verdict

date: 2026-05-20
verdict: PARTIAL-PROGRESS

## Head-to-Head

- Raw route: `NO-PROGRESS`; located the conjectural target but produced no
  replayable artifact.
- Dianoia route: `PARTIAL-PROGRESS`; produced an exact finite-poset analyzer,
  tests, a replayed exhaustive labeled small-poset check through five elements,
  and a canonical unlabeled check through six elements.

## Exact Evidence

- `tools/poset_balance.py`
- `tests/test_poset_balance.py`
- `research-bank/R013/attempt-20260520/small-posets-n5.json`
- `research-bank/R013/attempt-20260520/unlabeled-posets-n6.json`
- `research-bank/R013/attempt-20260520/STRUCTURAL_NOTES.md`
- `tools/verify_all.py`

The small-poset artifact reports:

- `n=2`: 3 labeled posets, 1 non-chain.
- `n=3`: 19 labeled posets, 13 non-chains.
- `n=4`: 219 labeled posets, 195 non-chains.
- `n=5`: 4231 labeled posets, 4111 non-chains.
- `counterexample_count: 0`.

The unlabeled six-element artifact reports:

- `n=6`: 318 unlabeled posets, 317 non-chains.
- `counterexample_count: 0`.
- width distribution: 1 chain, 74 width-2, 170 width-3, 63 width-4, 9 width-5,
  and 1 antichain.

## Claim Discipline

No `CLAIMS.md` row is added. The check is useful instrumentation and a sanity
baseline, not a new theorem, counterexample, bound improvement, or publishable
connection.
