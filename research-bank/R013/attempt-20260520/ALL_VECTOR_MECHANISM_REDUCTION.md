# R013 All Vector Mechanism Reduction

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note extends the mechanism search from the dangerous classes and weakest
unprocessed classes to every adjacent/skip vector class in the width-3,
height-4, rank-layer-shape `2,2,2,1` finite-poset subproblem.

Generated evidence:

```text
width3-rank2221-all-vector-form-ledger.json
normal-form-cases/vector-all/summary.json
normal-form-cases/vector-all/mechanism-batch-depth5.json
```

Commands:

```text
python tools/poset_balance.py matrix-vector-form-ledger \
  research-bank/R013/attempt-20260520/width3-rank2221-vector-frontier.json \
  --ids P1,P2,P3,P4,P5,P6,P7,P8,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30,U31,U32,U33,U34,U35,U36,U37,U38,U39,U40,U41,U42,U43,U44,U45,U46,U47,U48,U49,U50,U51 \
  --rank-shape 2,2,2,1 \
  --width 3 \
  --height 4 \
  --output research-bank/R013/attempt-20260520/width3-rank2221-all-vector-form-ledger.json

python tools/poset_balance.py matrix-vector-named-cases \
  research-bank/R013/attempt-20260520/width3-rank2221-all-vector-form-ledger.json \
  --ids P1,P2,P3,P4,P5,P6,P7,P8,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30,U31,U32,U33,U34,U35,U36,U37,U38,U39,U40,U41,U42,U43,U44,U45,U46,U47,U48,U49,U50,U51 \
  --output-dir research-bank/R013/attempt-20260520/normal-form-cases/vector-all \
  --summary research-bank/R013/attempt-20260520/normal-form-cases/vector-all/summary.json

python tools/poset_balance.py named-case-mechanism-batch \
  research-bank/R013/attempt-20260520/normal-form-cases/vector-all \
  --max-depth 5 \
  --output research-bank/R013/attempt-20260520/normal-form-cases/vector-all/mechanism-batch-depth5.json
```

## Result

All 59 vector classes expand to 103 rank-normal forms. Every one of those 103
forms resolves by depth at most 5 in the current recurrence mechanism search.

| Mechanism | Count |
|-----------|-------|
| `forced-block` | 55 |
| `balanced-core-plus-forced-first` | 31 |
| `balanced-core-plus-forced-second` | 1 |
| `balanced-core-with-forced-blocks` | 16 |
| unresolved | 0 |

The one `balanced-core-plus-forced-second` case is `u17-form-2`, with pair
`e,f`, lower probability `12/26`, and depth 3. It is best understood as the
orientation-reversed version of the plus-forced-first schema, not as a new
unrelated phenomenon.

## Why This Matters

This is stronger than the previous U6/P1-P8 and U1-U5 checks. It says that, at
the vector-class normal-form level, the whole restricted rank-2221 universe is
covered by bounded-depth recurrence certificates.

The useful mathematical target is now sharper:

> Prove a mechanism theorem for rank-2221 width-3 posets: every normal form in
> the vector-class decomposition admits a bounded-depth partition of linear
> extensions into forced orientation blocks plus, where needed, balanced
> residual cores. The lower orientation count in that partition is at least
> `13/32` of all linear extensions.

This should not be promoted as a contribution yet. The current evidence is
generated recurrence certification, not a human-readable proof that the
mechanism hypotheses cover the class. It is, however, a real proof-search
compression: 103 normal forms collapse to a small family of recurrence
obligations.

## Next Proof Obligations

1. Extract the local trigger conditions for the four listed mechanism labels.
2. Fold `balanced-core-plus-forced-first` and
   `balanced-core-plus-forced-second` into one orientation-symmetric schema.
3. Write a human-checkable lemma that derives the recurrence partition from
   those trigger conditions.
4. Independently verify that the vector-class decomposition covers every
   width-3, height-4, rank-layer-shape `2,2,2,1` poset.

Only after those steps should this become a restricted-subcase draft note or a
`CLAIMS.md` candidate.

