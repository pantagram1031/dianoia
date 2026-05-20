# R013 Sixth Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the sixth-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=9|mins=2|maxs=2|cover_matrix=[[0,3,2,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-sixth-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-sixth-cover-matrix-forms-n7.json`: direct derivation from
  rank shape plus cover matrix.
- `normal-form-cases/case-sixth-bucket.json`: named normal-form input.
- `normal-form-cases/case-sixth-bucket-report.json`: replayed count report.
- `normal-form-cases/case-sixth-bucket-recurrence-depth2.json`: depth-2
  recurrence trace.

## Derived Form

The cover matrix derives exactly one rank-normal form:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, b<c, b<e, b<f, c<g, d<e, d<f, e<g
```

The checked pair is `(e,c)`. Exact replay gives:

```text
N(e<c) = 12
N(c<e) = 18
lower orientation probability = 12/30 = 2/5
```

## Root Recurrence

The recurrence trace gives:

```text
choose a: (N_e, N_c) = (8, 11)
choose b: (N_e, N_c) = (4, 7)
total:    (N_e, N_c) = (12, 18)
```

Here `N_e` abbreviates `N(e<c)` and `N_c` abbreviates `N(c<e)`.

## Hand Count

### Shared Residual

The prefix `b,a` leaves:

```text
c<g ; d<e,f ; e<g
```

with pair `(e,c)` still unseen.

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
  subtotal (N_e,N_c) = (4,4)
```

Thus the shared residual contributes `(N_e,N_c) = (4,7)`.

### Prefix `b`

After choosing `b`, only `a` is available next, so the `b` root branch is the
shared residual:

```text
choose b: (N_e,N_c) = (4,7)
```

### Prefix `a`

After choosing `a`, the available second-level choices are `b` and `d`.

The `a,b` branch is the shared residual, contributing `(4,7)`.

For `a,d`, the residual constraints are:

```text
b<c,e,f ; c<g ; e<g
```

The element `b` is forced first. After `a,d,b`, the residual is:

```text
c<g ; e<g
```

on the elements `{c,e,f,g}`. Counting by first choice:

```text
choose c: e,f,g with e<g -> 3 contributes c<e
choose e: c,f,g with c<g -> 3 contributes e<c
choose f: c,e,g with c<g and e<g -> 1 each orientation
```

So `a,d` contributes `(4,4)`. Therefore the `a` root branch contributes:

```text
choose a: (N_e,N_c) = (4,7) + (4,4) = (8,11)
```

Combining both root branches:

```text
N(e<c) = 8 + 4 = 12
N(c<e) = 11 + 7 = 18
lower orientation probability = 12/30 = 2/5
```

## Subcase Conclusion

The sixth matrix bucket is a singleton. The pair `(e,c)` is balanced with
lower orientation probability `2/5`, so this bucket is separated from the
current restricted extremal `14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a proof of the published open problem.
