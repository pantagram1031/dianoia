# R013 Width-3 Extremal Profile Notes

date: 2026-05-20
status: OBSERVATION-NOT-CLAIM

## Artifact

`width3-extremals-n7.json` records the 12 width-3 unlabeled posets through
seven elements with smallest best-pair lower-orientation probabilities.
`width3-rank2221-n7.json` and `width3-rank2221-extremals-n7.json` restrict to
the proof-target class: width 3, height 4, rank-layer-shape `2,2,2,1`.
`width3-rank2221-shape-classes-n7.json` groups the same restricted class by
rank-layer shape, cover-edge count, number of minimal elements, and number of
maximal elements.
`width3-rank2221-matrix-shape-classes-n7.json` refines that split by the
inter-rank cover matrix. `width3-rank2221-fine-shape-classes-n7.json` refines
again by sorted per-layer vertex signatures.

The command was:

```powershell
python tools\poset_balance.py extremal-width `
  --max-n 7 `
  --width 3 `
  --limit 12 `
  --output research-bank\R013\attempt-20260520\width3-extremals-n7.json
```

## Boundary Data

The current extremal width-3 records are:

| n | best-pair lower probability | gap above 1/3 | linear extensions | rank layer sizes |
|---|-----------------------------|---------------|-------------------|------------------|
| 7 | `14/39` | `1/39` | 39 | `2,2,2,1` |
| 5 | `4/11` | `1/33` | 11 | `2,2,1` |
| 6 | `4/11` | `1/33` | 11 | `2,2,1,1` |

The first `n=7` extremal is the only recorded example in the top 12 below
`4/11`.

Inside the restricted width-3, height-4, rank-layer-shape `2,2,2,1` class:

- total unlabeled posets: 103;
- counterexamples to the base 1/3-2/3 condition: 0;
- worst best-pair lower probability: `14/39`;
- next worst lower probability: `2/5`.
- coarse signature buckets: 12.
- matrix signature buckets: 67.
- fine signature buckets: 103.

## Shape Signal

The strongest `n=7` profile has:

- width 3, height 4;
- two minimal elements and two maximal elements;
- rank layer sizes `2,2,2,1`;
- eight cover relations;
- best pair `(0,1)` with lower orientation probability `14/39`.

The cover relations are:

```text
0<3, 0<4, 1<3, 1<4, 2<5, 3<5, 6<0, 6<2
```

This looks like a coupled ladder/fork shape: two lower choices feed two middle
choices, one side continues into a top element, and the extra minimal element
links into both the balanced-pair side and the side branch.

The coarse signature bucket containing the `14/39` extremal is:

```text
layers=2,2,2,1|covers=8|mins=2|maxs=2
```

This bucket has 24 profiles, so cover/min/max counts alone are not a
human-checkable case split. The next split needs a finer invariant, likely the
inter-layer cover matrix or the sequence of vertex signatures by rank layer.

The matrix-signature refinement uses this cover-rank matrix for the `14/39`
extremal:

```text
[[0,2,2,0],
 [0,0,2,1],
 [0,0,0,1],
 [0,0,0,0]]
```

This matrix bucket has 3 profiles. The fully refined layer-vertex-signature
bucket is a singleton, so it identifies the extremal exactly but is too fine
to be the final human proof structure.

`MATRIX_BUCKET_NOTES.md` records the three profiles in this matrix bucket:
their best lower probabilities are `14/39`, `14/33`, and `5/11`. The immediate
manual subgoal is to prove this 3-case bucket split without referring to the
search labels.

## Next Proof Attempt

The exact restricted-family check suggests the sharper finite lemma:

> If a seven-element width-3 poset has rank layer sizes `2,2,2,1`, then either
> it has a pair with orientation probability at least `2/5` and at most `3/5`,
> or it is isomorphic to the unique recorded extremal profile whose best lower
> probability is `14/39`.

This is not yet a theorem. The current exact artifacts indicate a unique
`14/39` extremal in the restricted class and a next worst value `2/5`, but the
proof still needs a human-checkable case split and comparison against known
width/thin poset literature before any novelty claim.

## Claim Discipline

No `CLAIMS.md` row. This is a finite exact-search observation and a proof
target, not a new mathematical result.
