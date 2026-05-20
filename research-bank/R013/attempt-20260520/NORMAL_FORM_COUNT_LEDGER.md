# R013 Normal Form Count Ledger

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This ledger records replayable exact counts for the three rank-normal cases in
the extremal matrix bucket. Each case has:

- a named cover-relation input file in `normal-form-cases/`;
- a generated report from `python tools\poset_balance.py named-case`;
- the pair count needed by `RANK_NORMAL_FORM_NOTES.md`.

`RECURRENCE_LEDGER.md` refines these counts into first-step minimal-element
recurrences.

## Replay Commands

```powershell
python tools\poset_balance.py named-case `
  research-bank\R013\attempt-20260520\normal-form-cases\case-a.json `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-a-report.json

python tools\poset_balance.py named-case `
  research-bank\R013\attempt-20260520\normal-form-cases\case-b.json `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-b-report.json

python tools\poset_balance.py named-case `
  research-bank\R013\attempt-20260520\normal-form-cases\case-c.json `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-c-report.json
```

## Count Ledger

| Case | Input | Report | Linear extensions | Checked pair | Orientation counts | Lower probability |
|------|-------|--------|-------------------|--------------|--------------------|-------------------|
| A | `case-a.json` | `case-a-report.json` | 39 | `{c,b}` | `c<b`: 14, `b<c`: 25 | `14/39` |
| B | `case-b.json` | `case-b-report.json` | 33 | `{a,b}` | `a<b`: 14, `b<a`: 19 | `14/33` |
| C | `case-c.json` | `case-c-report.json` | 33 | `{c,d}` | `c<d`: 15, `d<c`: 18 | `5/11` |

## Proof Use

The ledger supports the finite sublemma target:

> In the common cover-matrix bucket, every rank-normal case has a balanced pair
> with lower orientation probability at least `14/39`, with equality only in
> Case A.

This is still a computational certificate. The next mathematical task is to
derive Cases A/B/C from the cover matrix and width/height assumptions, then
replace the exact-count replay with a small hand enumeration or recurrence.

## Claim Discipline

No `CLAIMS.md` row. This ledger certifies a finite proof subcase only.
