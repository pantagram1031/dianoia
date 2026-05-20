# R013 Recurrence Ledger

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This ledger replaces the named-case count reports with a more transparent
minimal-element recurrence. The recurrence is still generated, but it now
exposes the first two recurrence levels needed for a hand enumeration.

For a named case and checked pair `(x,y)`, write `N_x` for the number of
linear extensions with `x` before `y`, and `N_y` for the number with `y` before
`x`.

## Replay Commands

```powershell
python tools\poset_balance.py named-case-recurrence `
  research-bank\R013\attempt-20260520\normal-form-cases\case-a.json `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-a-recurrence.json

python tools\poset_balance.py named-case-recurrence `
  research-bank\R013\attempt-20260520\normal-form-cases\case-b.json `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-b-recurrence.json

python tools\poset_balance.py named-case-recurrence `
  research-bank\R013\attempt-20260520\normal-form-cases\case-c.json `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-c-recurrence.json

python tools\poset_balance.py named-case-recurrence `
  research-bank\R013\attempt-20260520\normal-form-cases\case-a.json `
  --depth 2 `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-a-recurrence-depth2.json

python tools\poset_balance.py named-case-recurrence `
  research-bank\R013\attempt-20260520\normal-form-cases\case-b.json `
  --depth 2 `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-b-recurrence-depth2.json

python tools\poset_balance.py named-case-recurrence `
  research-bank\R013\attempt-20260520\normal-form-cases\case-c.json `
  --depth 2 `
  --output research-bank\R013\attempt-20260520\normal-form-cases\case-c-recurrence-depth2.json
```

## Root Recurrences

### Case A

Checked pair: `(c,b)`. Initial minimal elements: `{a,b}`.

```text
choose a: (N_c, N_b) = (14, 14)
choose b: (N_c, N_b) = (0, 11)
total:    (N_c, N_b) = (14, 25)
```

Thus the lower orientation probability is `14/39`.

### Case B

Checked pair: `(a,b)`. Initial minimal elements: `{a,b}`.

```text
choose a: (N_a, N_b) = (14, 0)
choose b: (N_a, N_b) = (0, 19)
total:    (N_a, N_b) = (14, 19)
```

Thus the lower orientation probability is `14/33`.

### Case C

Checked pair: `(c,d)`. Initial minimal elements: `{a,b}`.

```text
choose a: (N_c, N_d) = (11, 13)
choose b: (N_c, N_d) = (4, 5)
total:    (N_c, N_d) = (15, 18)
```

Thus the lower orientation probability is `15/33 = 5/11`.

## Second-Level Recurrences

The depth-2 traces expose the next recurrence layer without changing the
root totals above.

### Case A after root choices

```text
after choose a:
  choose b: (N_c, N_b) = (0, 11)
  choose c: (N_c, N_b) = (11, 0)
  choose d: (N_c, N_b) = (3, 3)

after choose b:
  choose a: (N_c, N_b) = (0, 11)
```

### Case B after root choices

```text
after choose a:
  choose b: (N_a, N_b) = (11, 0)
  choose c: (N_a, N_b) = (3, 0)

after choose b:
  choose a: (N_a, N_b) = (0, 11)
  choose d: (N_a, N_b) = (0, 8)
```

### Case C after root choices

```text
after choose a:
  choose b: (N_c, N_d) = (4, 5)
  choose c: (N_c, N_d) = (7, 0)
  choose d: (N_c, N_d) = (0, 8)

after choose b:
  choose a: (N_c, N_d) = (4, 5)
```

## Proof Use

The next manual proof step is to justify each branch count without code, for
example by applying the same minimal-element recurrence recursively until the
remaining poset is a chain, a two-chain shuffle, or a previously counted small
shape.

`BRANCH_ENUMERATION_LEDGER.md` supplies this hand enumeration for the depth-2
residual branches. Together with `COVER_MATRIX_DERIVATION.md`, the common
cover-matrix subcase now has a transparent finite proof:

> Cases A/B/C have lower orientation probabilities `14/39`, `14/33`, and
> `5/11`; therefore the subcase lower bound is `14/39`, attained only by
> Case A.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a solution of the published open problem.
