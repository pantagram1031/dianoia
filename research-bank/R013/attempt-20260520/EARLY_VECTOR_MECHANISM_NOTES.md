# R013 Early Vector Mechanism Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note tests whether the P7/P8 boundary mechanisms overfit the two
`13/32` classes, or whether they transfer to the earlier dangerous vector
classes P1/P2/P3.

Generated artifacts:

```text
normal-form-cases/vector-early/summary.json
normal-form-cases/vector-early/p1-form-1-recurrence-depth3.json
normal-form-cases/vector-early/p1-form-1-mechanism-depth3.json
normal-form-cases/vector-early/p2-form-5-recurrence-depth3.json
normal-form-cases/vector-early/p2-form-5-mechanism-depth3.json
normal-form-cases/vector-early/p3-form-3-recurrence-depth3.json
normal-form-cases/vector-early/p3-form-3-mechanism-depth3.json
```

The selected forms are the minimum forms for P1, P2, and P3 in the U6
dangerous-form ledger.

## Reuse Result

| Class | Form | Pair | Root Split | Mechanism | Leaf Split Counts |
|-------|------|------|------------|-----------|-------------------|
| P1 | `p1-form-1` | `(b,c)` | `25/14` out of `39` | `forced-block` | `8:0 x2`, `3:0 x3`, `0:8 x1`, `0:3 x2` |
| P2 | `p2-form-5` | `(a,b)` | `14/21` out of `35` | `forced-block` | `8:0 x1`, `3:0 x2`, `0:8 x2`, `0:3 x1`, `0:2 x1` |
| P3 | `p3-form-3` | `(b,c)` | `21/14` out of `35` | `forced-block` | `6:0 x2`, `3:0 x3`, `0:6 x1`, `0:4 x2` |

P1 and P3 reuse the P7-style forced-block mechanism almost verbatim: five
forced-first leaves and three forced-second leaves, with no unseen residual.
P2 also resolves by forced blocks, but the selected pair is oriented the other
way: the lower orientation is the first-before-second side `14/35`, while the
majority side is forced-second `21/35`.

## Consequence

The recurrence-mechanism abstraction is not limited to P7/P8. Four of the five
tested dangerous minima so far use forced-block certificates:

```text
P1: forced-block, lower 14/39
P2: forced-block, lower 14/35 = 2/5
P3: forced-block, lower 14/35 = 2/5
P7: forced-block, lower 13/32
P8: balanced-core-plus-forced-first, lower 13/32
```

The next mathematical step is to convert the repeated forced-block pattern into
a lemma schema:

```text
If the depth-3 recurrence leaves all force the target pair orientation, then
the lower orientation bound reduces to a finite list of terminal
chain/shuffle counts.
```

This is not a proof of the full width-3 rank-shape class yet. It is a reusable
proof mechanism that can be tested against P4/P5/P6 and then against the U6
frontier.

## Claim Discipline

No `CLAIMS.md` row. This is partial progress toward a restricted finite
subcase, with explicit generated evidence and no publication claim.
