# R013 All Dangerous Form Mechanism Reduction

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note checks whether the two mechanism families from
`FORCED_BLOCK_SCHEMA_NOTES.md` cover all 22 rank-normal forms in the U6 plus
P1-P8 dangerous ledger.

Generated evidence:

```text
normal-form-cases/u6-p1-p8-mechanism-batch-depth5.json
```

Command:

```text
python tools/poset_balance.py named-case-mechanism-batch \
  research-bank/R013/attempt-20260520/normal-form-cases/vector-early \
  research-bank/R013/attempt-20260520/normal-form-cases/vector-boundary \
  research-bank/R013/attempt-20260520/normal-form-cases/vector-forced-block-check \
  --max-depth 5 \
  --output research-bank/R013/attempt-20260520/normal-form-cases/u6-p1-p8-mechanism-batch-depth5.json
```

## Result

All 22 forms resolve by depth at most 5.

| Mechanism | Count |
|-----------|-------|
| `forced-block` | 15 |
| `balanced-core-plus-forced-first` | 3 |
| `balanced-core-with-forced-blocks` | 4 |

There are no unresolved dangerous forms in this max-depth-5 batch.

## Form Table

| Form | Depth | Mechanism | Lower probability |
|------|-------|-----------|-------------------|
| `p1-form-1` | 1 | `balanced-core-plus-forced-first` | `14/39` |
| `p1-form-2` | 3 | `forced-block` | `15/33` |
| `p1-form-3` | 1 | `forced-block` | `14/33` |
| `p2-form-1` | 3 | `forced-block` | `19/44` |
| `p2-form-2` | 3 | `forced-block` | `25/51` |
| `p2-form-3` | 3 | `forced-block` | `22/44` |
| `p2-form-4` | 3 | `forced-block` | `18/37` |
| `p2-form-5` | 1 | `forced-block` | `14/35` |
| `p2-form-6` | 3 | `balanced-core-with-forced-blocks` | `15/36` |
| `p3-form-1` | 5 | `forced-block` | `15/31` |
| `p3-form-2` | 5 | `balanced-core-with-forced-blocks` | `23/47` |
| `p3-form-3` | 3 | `forced-block` | `14/35` |
| `p3-form-4` | 3 | `forced-block` | `16/33` |
| `p4-form-1` | 3 | `forced-block` | `12/30` |
| `p5-form-1` | 4 | `forced-block` | `14/35` |
| `p6-form-1` | 3 | `balanced-core-plus-forced-first` | `12/30` |
| `p7-form-1` | 3 | `forced-block` | `19/41` |
| `p7-form-2` | 3 | `forced-block` | `13/32` |
| `p8-form-1` | 3 | `balanced-core-plus-forced-first` | `13/32` |
| `p8-form-2` | 3 | `balanced-core-with-forced-blocks` | `15/33` |
| `u6-form-1` | 5 | `forced-block` | `30/70` |
| `u6-form-2` | 5 | `balanced-core-with-forced-blocks` | `31/63` |

## Interpretation

The original eight dangerous vector classes do not require eight separate
arguments at the normal-form level. They reduce to:

1. forced terminal orientation blocks;
2. balanced unseen cores with extra forced blocks.

This is a stronger generalization signal than the earlier minimum-form-only
checks. The next useful proof move is not to enumerate more of these 22 forms,
but to explain why the 51 unprocessed vector classes are excluded by a
dominance, injection, or slack argument.

## Remaining Proof Gap

This note still does not prove the restricted rank-shape subcase. The missing
bridge is:

```text
unprocessed vector class -> guaranteed lower probability at least 13/32
```

The current data suggests looking for a monotone operation from U6 to the 51
unprocessed classes that preserves a balanced pair or increases the lower
orientation probability.

## Claim Discipline

No `CLAIMS.md` row. This is proof-support for a restricted finite subcase, not
a verified contribution to the published open problem.
