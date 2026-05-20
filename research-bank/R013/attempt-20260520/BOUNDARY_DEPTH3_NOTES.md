# R013 Boundary Depth-3 Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note interprets:

```text
normal-form-cases/vector-boundary/p7-form-2-recurrence-depth3.json
normal-form-cases/vector-boundary/p8-form-1-recurrence-depth3.json
normal-form-cases/vector-boundary/p7-form-2-leaves-depth3.json
normal-form-cases/vector-boundary/p8-form-1-leaves-depth3.json
normal-form-cases/vector-boundary/p7-p8-leaf-comparison-depth3.json
```

## Depth-3 Pattern

P7 form 2 resolves completely into forced pair-state leaves:

```text
first_before_second leaves: 5, 3, 3, 5, 3  total 19
second_before_first leaves: 5, 4, 4        total 13
```

P8 form 1 does not fully resolve at depth 3:

```text
forced first leaves: 3, 3                  total 6
unseen leaves: 4/4, 4/4, 1/1, 4/4          total 13/13
```

Thus P8's `19/13` split decomposes as:

```text
6 forced-first + 13 balanced-unseen first
0 forced-second + 13 balanced-unseen second
```

## Interpretation

Depth 3 makes a symmetric P7/P8 leaf pairing less plausible. P7 resolves its
orientation at depth 3, while P8 still has balanced unseen subproblems. The
shared `19/13` boundary value is better explained by two different mechanisms:

- P7: forced majority blocks dominate forced minority blocks by `19-13`.
- P8: a balanced `13/13` residual core plus two forced-first blocks of size `3`
  each.

This is good news for proof search. Instead of requiring a mysterious
P7/P8 bijection, each boundary case may admit a short recurrence proof with a
different local explanation.

## Next Proof Move

Write two separate boundary lemmas:

1. P7 form 2: prove the depth-3 forced block identity
   `5+3+3+5+3` versus `5+4+4`.
2. P8 form 1: prove the depth-3 decomposition into two forced-first blocks of
   size `3` plus four balanced unseen blocks summing to `13/13`.

Then check whether P1/P2/P3 reduce to the same P7-style forced-block identity
or the same P8-style balanced-core identity.

## Claim Discipline

No `CLAIMS.md` row. This is recurrence evidence for a restricted finite
subcase, not a proof of the published open problem.
