# R013 Structural Notes From Exact Small Posets

date: 2026-05-20
status: OBSERVATION-NOT-CLAIM

## Scope

The exact check in this attempt covers unlabeled finite posets through six
elements. It is not a novel theorem and it does not affect `CLAIMS.md`.

Artifacts:

- `small-posets-n5.json`: labeled check through five elements.
- `unlabeled-posets-n5.json`: canonical unlabeled check through five elements.
- `unlabeled-posets-n6.json`: canonical unlabeled check through six elements.
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

## Structural Signals

These are search signals only:

- Width 2 is the tight small-family source: the worst best-pair probability
  reaches exactly `1/3` in the `n=3`, `n=4`, `n=5`, and `n=6` summaries.
- Width 3 remains separated from the boundary in the small data: the worst
  best-pair lower probability is `4/11` for `n=5` and `n=6`.
- Width at least 4 is very loose in this small range: the worst best-pair
  lower probability recorded by the canonical run is `1/2`.

## Next Mathematical Moves

1. Scale canonical generation to `n=7` only if runtime is acceptable or after
   improving canonical-key speed.
2. Add class filters for width, height, and cover graph shape so dianoia can
   ask structural questions rather than merely enumerate.
3. Try to prove the observed high-width looseness for a restricted class, or
   deliberately search for the smallest width-3 family with lower probability
   closer to `1/3` than `4/11`.

## Honesty Boundary

This note is not a proof, counterexample, bound improvement, or new published
connection. It is a finite exact-search baseline and a guide for the next
attempt.
