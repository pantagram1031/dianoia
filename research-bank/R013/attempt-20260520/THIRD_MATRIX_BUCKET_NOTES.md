# R013 Third Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the third-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=7|mins=2|maxs=2|cover_matrix=[[0,2,1,0],[0,0,2,1],[0,0,0,1],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-third-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-third-cover-matrix-forms-n7.json`: direct derivation from
  rank shape plus cover matrix.
- `normal-form-cases/case-third-bucket-*.json`: named normal-form inputs.
- `normal-form-cases/case-third-bucket-*-report.json`: replayed count reports.
- `normal-form-cases/case-third-bucket-*-recurrence-depth2.json`: depth-2
  recurrence traces.

## Derived Forms

The cover matrix derives exactly six rank-normal forms, matching the six
extracted bucket profiles.

| Case | Covers | Pair | Counts | Lower probability |
|------|--------|------|--------|-------------------|
| 1 | `a<c, a<d, b<e, c<e, c<f, d<g, e<g` | `(b,c)` | `(25,19)` | `19/44` |
| 2 | `a<c, a<d, b<e, c<e, c<f, d<g, f<g` | `(b,c)` | `(25,26)` | `25/51` |
| 3 | `a<c, a<d, b<e, c<e, c<g, d<f, f<g` | `(b,d)` | `(22,22)` | `1/2` |
| 4 | `a<c, a<d, b<e, c<e, d<f, d<g, e<g` | `(c,d)` | `(19,18)` | `18/37` |
| 5 | `a<c, a<e, b<d, c<g, d<e, d<f, e<g` | `(a,b)` | `(14,21)` | `2/5` |
| 6 | `a<c, a<e, b<d, c<g, d<e, d<f, f<g` | `(c,f)` | `(21,15)` | `5/12` |

Thus the generated exact evidence gives a bucket lower bound of `2/5`,
attained only by Case 5.

## Root Recurrences

The depth-2 recurrence artifacts expose the following root splits:

```text
Case 1, pair (b,c): total (25,19)
  choose a: (14,19)
  choose b: (11,0)

Case 2, pair (b,c): total (25,26)
  choose a: (14,26)
  choose b: (11,0)

Case 3, pair (b,d): total (22,22)
  choose a: (13,22)
  choose b: (9,0)

Case 4, pair (c,d): total (19,18)
  choose a: (14,14)
  choose b: (5,4)

Case 5, pair (a,b): total (14,21)
  choose a: (14,0)
  choose b: (0,21)

Case 6, pair (c,f): total (21,15)
  choose a: (10,4)
  choose b: (11,11)
```

## Hand Count for the Equality Case

Case 5 covers:

```text
a<c, a<e, b<d, c<g, d<e, d<f, e<g
```

The checked pair is `(a,b)`. Initially the minimal elements are `a` and `b`.

### Prefix `a`

After `a`, the residual constraints are:

```text
b<d, c<g, d<e, d<f, e<g
```

If the next element is `b`, then the residual constraints are
`c<g, d<e, d<f, e<g`. This has `11` extensions:

```text
choose c: d<e, d<f, e<g -> 3
choose d: c<g, e<g, f free -> 8
```

If the next element is `c`, then `b,d` are forced before `e` and `f` become
available, leaving `e<g` with `f` free, which gives `3` extensions.

Therefore the `a`-first branch has `11 + 3 = 14` extensions, all with `a<b`.

### Prefix `b`

After `b`, the residual constraints are:

```text
a<c, a<e, c<g, d<e, d<f, e<g
```

If the next element is `a`, then the residual constraints are
`c<g, d<e, d<f, e<g`, counted above as `11`.

If the next element is `d`, then the residual constraints are
`a<c, a<e, c<g, e<g` with `f` free. The four-element core has two orders,
`a,c,e,g` and `a,e,c,g`; inserting `f` into five slots gives `10`.

Therefore the `b`-first branch has `11 + 10 = 21` extensions, all with `b<a`.

So Case 5 has:

```text
N(a<b) = 14
N(b<a) = 21
lower orientation probability = 14/35 = 2/5
```

## Subcase Conclusion

The third matrix bucket has six rank-normal forms and exact generated counts
show lower orientation probability at least `2/5`. The equality form, Case 5,
has a direct hand count above.

This bucket is therefore separated from the current restricted extremal
`14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a proof of the published open problem.
