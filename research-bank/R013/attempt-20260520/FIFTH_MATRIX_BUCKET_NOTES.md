# R013 Fifth Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the fifth-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=9|mins=2|maxs=2|cover_matrix=[[0,2,2,0],[0,0,3,1],[0,0,0,1],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-fifth-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-fifth-cover-matrix-forms-n7.json`: direct derivation from
  rank shape plus cover matrix.
- `normal-form-cases/case-fifth-bucket.json`: named normal-form input.
- `normal-form-cases/case-fifth-bucket-report.json`: replayed count report.
- `normal-form-cases/case-fifth-bucket-recurrence-depth2.json`: depth-2
  recurrence trace.

## Derived Form

The cover matrix derives exactly one rank-normal form:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, b<e, b<f, c<e, c<f, d<e, d<g, f<g
```

The checked pair is `(c,d)`. Exact replay gives:

```text
N(c<d) = 18
N(d<c) = 12
lower orientation probability = 12/30 = 2/5
```

## Root Recurrence

The recurrence trace gives:

```text
choose a: (N_c, N_d) = (13, 9)
choose b: (N_c, N_d) = (5, 3)
total:    (N_c, N_d) = (18, 12)
```

## Hand Count

### Prefix `a`

After choosing `a`, the residual constraints are:

```text
b<e, b<f, c<e, c<f, d<e, d<g, f<g
```

Second-level branches:

```text
choose b: (N_c, N_d) = (5,3)
choose c: (N_c, N_d) = (8,0)
choose d: (N_c, N_d) = (0,6)
```

For `a,b`, the residual constraints are:

```text
c<e,f ; d<e,g ; f<g
```

Counting by first choice:

```text
choose c:
  residual d,e,f,g with d<e,g and f<g
  choose d: f<g with e free -> 3
  choose f: d<e,g -> 2
  subtotal 5 contributes c<d

choose d:
  residual c,e,f,g with c<e,f and f<g
  choose c: f<g with e free -> 3
  subtotal 3 contributes d<c
```

So `a,b` contributes `(5,3)`.

For `a,c`, the pair state is already `c<d`. The residual constraints are:

```text
b<e,f ; d<e,g ; f<g
```

Counting by first choice:

```text
choose b:
  residual d,e,f,g with d<e,g and f<g -> 5
choose d:
  residual b,e,f,g with b<e,f and f<g -> 3
total 8
```

So `a,c` contributes `(8,0)`.

For `a,d`, the pair state is already `d<c`. The residual constraints are:

```text
b<e,f ; c<e,f ; f<g
```

If `b` is chosen before `c`, the residual after `c` is `e` free and `f<g`,
giving `3` extensions; by symmetry, `c` before `b` also gives `3`. Thus the
total is `6`, all contributing `d<c`, so `a,d` contributes `(0,6)`.

Therefore the `a` branch contributes `(13,9)`.

### Prefix `b`

After choosing `b`, the only second-level choice is `a`, and the remaining
constraints match the `a,b` residual above:

```text
c<e,f ; d<e,g ; f<g
```

So the `b` branch contributes `(5,3)`.

Combining both root branches:

```text
N(c<d) = 13 + 5 = 18
N(d<c) = 9 + 3 = 12
lower orientation probability = 12/30 = 2/5
```

## Subcase Conclusion

The fifth matrix bucket is a singleton. The pair `(c,d)` is balanced with
lower orientation probability `2/5`, so this bucket is separated from the
current restricted extremal `14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a proof of the published open problem.
