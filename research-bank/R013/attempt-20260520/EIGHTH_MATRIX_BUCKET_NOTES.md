# R013 Eighth Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the eighth-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=8|mins=2|maxs=2|cover_matrix=[[0,3,1,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-eighth-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-eighth-cover-matrix-forms-n7.json`: direct derivation
  from rank shape plus cover matrix.
- `normal-form-cases/case-eighth-bucket-0.json` and
  `normal-form-cases/case-eighth-bucket-1.json`: named normal-form inputs.
- `normal-form-cases/case-eighth-bucket-*-report.json`: replayed count
  reports.
- `normal-form-cases/case-eighth-bucket-*-recurrence-depth2.json`: depth-2
  recurrence traces.

## Derived Forms

The cover matrix derives exactly two rank-normal forms.

Form 0:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, b<c, b<e, c<g, d<e, d<f, e<g
```

For the checked pair `(c,e)`, exact replay gives:

```text
N(c<e) = 19
N(e<c) = 13
lower orientation probability = 13/32
```

Form 1:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, b<c, b<e, c<g, d<e, d<f, f<g
```

For the checked pair `(c,f)`, exact replay gives:

```text
N(c<f) = 18
N(f<c) = 15
lower orientation probability = 15/33 = 5/11
```

Thus the bucket minimum is attained by Form 0.

## Form 0 Root Recurrence

The recurrence trace for Form 0 gives:

```text
choose a: (N_c, N_e) = (12, 9)
choose b: (N_c, N_e) = (7, 4)
total:    (N_c, N_e) = (19, 13)
```

Here `N_c` abbreviates `N(c<e)` and `N_e` abbreviates `N(e<c)`.

## Form 0 Hand Count

### Shared Residual

The prefix `b,a` leaves:

```text
c<g ; d<e,f ; e<g
```

with pair `(c,e)` still unseen.

Counting by first choice:

```text
choose c:
  residual d,e,f,g with d<e,f and e<g
  choose d, then e/f/g with e<g -> 3
  subtotal 3 contributes c<e

choose d:
  residual c,e,f,g with c<g and e<g
  choose c: e,f,g with e<g -> 3 contributes c<e
  choose e: c,f,g with c<g -> 3 contributes e<c
  choose f: c,e,g with c<g and e<g -> 1 each orientation
  subtotal (N_c,N_e) = (4,4)
```

Thus the shared residual contributes:

```text
(N_c,N_e) = (7,4)
```

### Prefix `b`

After choosing `b`, only `a` is available next, so the `b` root branch is the
shared residual:

```text
choose b: (N_c,N_e) = (7,4)
```

### Prefix `a`

After choosing `a`, the second-level choices are `b` and `d`.

The `a,b` branch is the shared residual, contributing `(7,4)`.

For `a,d`, the residual constraints are:

```text
b<c,e ; c<g ; e<g
```

and `f` is free. Counting by first choice:

```text
choose b:
  residual c,e,f,g with c<g and e<g -> (4,4)

choose f:
  residual b,c,e,g with b<c,e and c,e<g
  only the two orders b,c,e,g and b,e,c,g are possible
  subtotal (N_c,N_e) = (1,1)
```

So `a,d` contributes `(5,5)`. Therefore:

```text
choose a: (N_c,N_e) = (7,4) + (5,5) = (12,9)
```

Combining both root branches:

```text
N(c<e) = 12 + 7 = 19
N(e<c) = 9 + 4 = 13
lower orientation probability = 13/32
```

## Subcase Conclusion

The eighth matrix bucket has two rank-normal forms. The weaker form has a
balanced pair with lower orientation probability `13/32`, still separated from
the current restricted extremal `14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a proof of the published open problem.
