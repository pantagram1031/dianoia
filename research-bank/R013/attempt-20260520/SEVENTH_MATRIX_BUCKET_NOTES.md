# R013 Seventh Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the seventh-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=8|mins=2|maxs=2|cover_matrix=[[0,2,1,0],[0,0,3,1],[0,0,0,1],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-seventh-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-seventh-cover-matrix-forms-n7.json`: direct derivation
  from rank shape plus cover matrix.
- `normal-form-cases/case-seventh-bucket-0.json` and
  `normal-form-cases/case-seventh-bucket-1.json`: named normal-form inputs.
- `normal-form-cases/case-seventh-bucket-*-report.json`: replayed count
  reports.
- `normal-form-cases/case-seventh-bucket-*-recurrence-depth2.json`: depth-2
  recurrence traces.

## Derived Forms

The cover matrix derives exactly two rank-normal forms.

Form 0:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, b<e, c<e, c<f, d<e, d<g, f<g
```

For the checked pair `(b,c)`, exact replay gives:

```text
N(b<c) = 19
N(c<b) = 22
lower orientation probability = 19/41
```

Form 1:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, b<e, c<e, c<f, d<f, d<g, e<g
```

For the checked pair `(b,c)`, exact replay gives:

```text
N(b<c) = 19
N(c<b) = 13
lower orientation probability = 13/32
```

Thus the bucket minimum is attained by Form 1.

## Form 1 Root Recurrence

The recurrence trace for Form 1 gives:

```text
choose a: (N_b, N_c) = (11, 13)
choose b: (N_b, N_c) = (8, 0)
total:    (N_b, N_c) = (19, 13)
```

Here `N_b` abbreviates `N(b<c)` and `N_c` abbreviates `N(c<b)`.

## Form 1 Hand Count

### Prefix `b`

After choosing `b`, only `a` is available next. The residual constraints after
`b,a` are:

```text
c<e,f ; d<f,g ; e<g
```

Counting total extensions:

```text
choose c:
  residual d,e,f,g with d<f,g and e<g
  choose d: e,f,g with e<g -> 3
  choose e: d,f,g with d<f,g -> 2
  subtotal 5

choose d:
  residual c,e,f,g with c<e,f and e<g
  choose c: e,f,g with e<g -> 3
  subtotal 3
```

So the root prefix `b` contributes `8` extensions, all with `b<c`:

```text
choose b: (N_b,N_c) = (8,0)
```

### Prefix `a`

After choosing `a`, the second-level choices are `b`, `c`, and `d`.

The `a,b` branch has the same residual as the `b,a` branch above, so it
contributes `(8,0)`.

For `a,c`, the pair state is already `c<b`. The residual constraints are:

```text
b<e ; d<f,g ; e<g
```

Counting by first choice:

```text
choose b:
  residual d,e,f,g with d<f,g and e<g -> 5
choose d:
  residual b,e,f,g with b<e and e<g
  choose b: e,f,g with e<g -> 3
  choose f: b<e<g -> 1
  subtotal 4
```

So `a,c` contributes `(0,9)`.

For `a,d`, the pair state is still unseen. The residual constraints are:

```text
b<e ; c<e,f ; e<g
```

Counting by first choice:

```text
choose b:
  residual c,e,f,g with c<e,f and e<g
  choose c: e,f,g with e<g -> 3
  subtotal 3 contributes b<c

choose c:
  residual b,e,f,g with b<e and e<g
  choose b: e,f,g with e<g -> 3
  choose f: b<e<g -> 1
  subtotal 4 contributes c<b
```

So `a,d` contributes `(3,4)`.

Therefore the `a` root branch contributes:

```text
choose a: (N_b,N_c) = (8,0) + (0,9) + (3,4) = (11,13)
```

Combining both root branches:

```text
N(b<c) = 11 + 8 = 19
N(c<b) = 13 + 0 = 13
lower orientation probability = 13/32
```

## Subcase Conclusion

The seventh matrix bucket has two rank-normal forms. The weaker form has a
balanced pair with lower orientation probability `13/32`, still separated from
the current restricted extremal `14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a proof of the published open problem.
