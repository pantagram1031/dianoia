# R013 Width-3 Extremal Profile Notes

date: 2026-05-20
status: OBSERVATION-NOT-CLAIM

## Artifact

`width3-extremals-n7.json` records the 12 width-3 unlabeled posets through
seven elements with smallest best-pair lower-orientation probabilities.

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

## Next Proof Attempt

Try to formalize a restricted lemma for width-3, height-4, rank-layer-shape
`2,2,2,1` posets:

> If a seven-element width-3 poset has rank layer sizes `2,2,2,1`, then either
> it has a pair with orientation probability at least `4/11` and at most
> `7/11`, or it is isomorphic to one of a small extremal-profile family whose
> best lower probability is `14/39`.

This is not yet a theorem. The next required work is to generate the restricted
family, classify the profile variants, and compare against known width/thin
poset literature before any novelty claim.

## Claim Discipline

No `CLAIMS.md` row. This is a finite exact-search observation and a proof
target, not a new mathematical result.
