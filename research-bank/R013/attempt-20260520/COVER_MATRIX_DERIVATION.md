# R013 Cover-Matrix Derivation

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the direct derivation of the three rank-normal forms from
the common cover matrix, independent of the larger unlabeled-poset bucket
search.

Input constraints:

- rank shape: `2,2,2,1`;
- width: 3;
- height: 4;
- cover matrix:

```text
[[0,2,2,0],
 [0,0,2,1],
 [0,0,0,1],
 [0,0,0,0]]
```

Replay command:

```powershell
python tools\poset_balance.py cover-matrix-forms `
  --rank-shape 2,2,2,1 `
  --cover-matrix "[[0,2,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]" `
  --width 3 `
  --height 4 `
  --output research-bank\R013\attempt-20260520\width3-rank2221-cover-matrix-forms-n7.json
```

## Result

The generated artifact `width3-rank2221-cover-matrix-forms-n7.json` records
`form_count: 3`. The three forms are exactly the cases in
`RANK_NORMAL_FORM_NOTES.md`:

1. Case A:
   `a<c, a<d, b<e, b<f, c<e, c<f, d<g, e<g`.
2. Case C:
   `a<c, a<d, b<e, b<f, c<e, c<g, d<f, f<g`.
3. Case B:
   `a<c, a<e, a<f, b<d, c<g, d<e, d<f, e<g`.

The ordering above is lexicographic by normal-form cover list, not by the case
names in `RANK_NORMAL_FORM_NOTES.md`.

## Proof Use

The exact derivation narrows the remaining hand proof to two tasks:

1. Explain without code why the cover matrix plus width/height restrictions
   leaves only these three forms up to rank-layer relabeling.
2. Replace the named-case count certificates with a hand recurrence or a small
   transparent linear-extension enumeration.

Together with `NORMAL_FORM_COUNT_LEDGER.md`, this gives a finite, replayable
subcase proof target:

> In the common cover-matrix bucket, the best lower orientation probability is
> at least `14/39`, with equality only in Case A.

## Claim Discipline

No `CLAIMS.md` row. This is a finite derivation artifact for one restricted
subcase, not a proof of the published open problem.
