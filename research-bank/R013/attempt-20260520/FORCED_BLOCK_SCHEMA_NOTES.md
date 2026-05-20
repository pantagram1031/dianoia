# R013 Forced-Block Schema Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note synthesizes the forced-block recurrence evidence for U6 and P1-P8 in
the width-3, height-4, rank-layer-shape `2,2,2,1` finite subcase.

Primary artifacts:

```text
normal-form-cases/vector-early/
normal-form-cases/vector-boundary/
normal-form-cases/vector-forced-block-check/
```

## Lemma Schema

Forced-block schema:

```text
Given a finite poset P and an incomparable pair (x,y), expand the linear
extension recurrence to depth d. If every depth-d leaf has already forced either
x before y or y before x, then the pair split is certified by:

1. partitioning extensions by the depth-d initial strings,
2. counting each residual poset,
3. summing residual counts by forced orientation.
```

The command

```text
python tools/poset_balance.py recurrence-forced-block-obligations <trace.json>
```

turns such a recurrence into the terminal count obligations needed for a
human-checkable lemma.

## Current Mechanism Table

| Class | Form | Depth Needed | Mechanism | Lower Probability | Evidence |
|-------|------|--------------|-----------|-------------------|----------|
| U6 | `u6-form-1` | 5 | `forced-block` | `30/70 = 3/7` | `vector-forced-block-check/u6-form-1-forced-block-obligations-depth5.json` |
| P1 | `p1-form-1` | 3 | `forced-block` | `14/39` | `vector-early/p1-form-1-mechanism-depth3.json` |
| P2 | `p2-form-5` | 3 | `forced-block` | `14/35 = 2/5` | `vector-early/p2-form-5-mechanism-depth3.json` |
| P3 | `p3-form-3` | 3 | `forced-block` | `14/35 = 2/5` | `vector-early/p3-form-3-mechanism-depth3.json` |
| P4 | `p4-form-1` | 3 | `forced-block` | `12/30 = 2/5` | `vector-forced-block-check/p4-form-1-forced-block-obligations-depth3.json` |
| P5 | `p5-form-1` | 4 | `forced-block` | `14/35 = 2/5` | `vector-forced-block-check/p5-form-1-forced-block-obligations-depth4.json` |
| P6 | `p6-form-1` | 3 | `balanced-core-plus-forced-first` | `12/30 = 2/5` | `vector-forced-block-check/p6-form-1-mechanism-depth3.json` |
| P7 | `p7-form-2` | 3 | `forced-block` | `13/32` | `vector-boundary/p7-form-2-mechanism-depth3.json` |
| P8 | `p8-form-1` | 3 | `balanced-core-plus-forced-first` | `13/32` | `vector-boundary/p8-form-1-mechanism-depth3.json` |

## Pattern

The processed dangerous classes now split into two reusable mechanisms:

- `forced-block`: U6, P1, P2, P3, P4, P5, P7.
- `balanced-core-plus-forced-first`: P6, P8.

This is exactly the kind of generalization pressure dianoia needs. The proof
search is no longer "check eight named buckets"; it is "prove two local
recurrence schemas and show the vector classes reduce to them."

## Remaining Gap

This still does not prove the restricted rank-shape subcase. Missing pieces:

1. A compact human proof that every generated terminal residual count is
   correct without trusting JSON alone.
2. A reduction from all 22 U6/P1-P8 rank-normal forms to the two mechanism
   schemas, not just the minimum forms.
3. A dominance or exclusion argument for the 51 unprocessed vector classes.

## Claim Discipline

No `CLAIMS.md` row. This is a reusable proof-support schema for a restricted
finite subcase, not a verified contribution to the published open problem.
