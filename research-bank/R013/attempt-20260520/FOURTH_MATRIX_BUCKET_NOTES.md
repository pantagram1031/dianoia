# R013 Fourth Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note records the fourth-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=7|mins=2|maxs=2|cover_matrix=[[0,2,1,0],[0,0,3,0],[0,0,0,1],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-fourth-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-fourth-cover-matrix-forms-n7.json`: direct derivation from
  rank shape plus cover matrix.
- `normal-form-cases/case-fourth-bucket-*.json`: named normal-form inputs.
- `normal-form-cases/case-fourth-bucket-*-report.json`: replayed count
  reports.
- `normal-form-cases/case-fourth-bucket-*-recurrence-depth2.json`: depth-2
  recurrence traces.

## Derived Forms

The cover matrix derives exactly four rank-normal forms, matching the four
extracted bucket profiles.

| Case | Covers | Pair | Counts | Lower probability |
|------|--------|------|--------|-------------------|
| 1 | `a<c, a<d, b<e, c<e, c<f, d<e, e<g` | `(e,f)` | `(16,15)` | `15/31` |
| 2 | `a<c, a<d, b<e, c<e, c<f, d<e, f<g` | `(e,g)` | `(23,24)` | `23/47` |
| 3 | `a<c, a<d, b<e, c<e, c<f, d<f, e<g` | `(b,c)` | `(21,14)` | `2/5` |
| 4 | `a<c, a<d, b<e, c<e, c<f, d<f, f<g` | `(b,c)` | `(17,16)` | `16/33` |

Thus the generated exact evidence gives a bucket lower bound of `2/5`,
attained only by Case 3.

## Root Recurrences

The depth-2 recurrence artifacts expose the following root splits:

```text
Case 1, pair (e,f): total (16,15)
  choose a: (12,12)
  choose b: (4,3)

Case 2, pair (e,g): total (23,24)
  choose a: (18,20)
  choose b: (5,4)

Case 3, pair (b,c): total (21,14)
  choose a: (12,14)
  choose b: (9,0)

Case 4, pair (b,c): total (17,16)
  choose a: (10,16)
  choose b: (7,0)
```

## Hand Count for the Equality Case

Case 3 covers:

```text
a<c, a<d, b<e, c<e, c<f, d<f, e<g
```

The checked pair is `(b,c)`. Initially the minimal elements are `a` and `b`.

### Prefix `b`

After `b`, the pair state is already `b<c`. The residual constraints are:

```text
a<c, a<d, c<e, c<f, d<f, e<g
```

The only minimal element is `a`; then the residual constraints are
`c<e, c<f, d<f, e<g`.

```text
choose c:
  residual d,e,f,g with d<f and e<g -> 6
choose d:
  residual c,e,f,g with c<e,f and e<g -> 3
total after b: 9
```

So the `b`-first branch contributes `(9,0)`.

### Prefix `a`

After `a`, the residual constraints are:

```text
b<e, c<e, c<f, d<f, e<g
```

If `b` is chosen next, then the residual constraints are
`c<e, c<f, d<f, e<g`, counted above as `9`, all with `b<c`.

If `c` is chosen next, then the residual constraints are
`b<e, d<f, e<g`. The count is `8`, all with `c<b`:

```text
choose b: d<f and e<g -> 6
choose d: b<e<g with f free -> 2
```

If `d` is chosen next, then the residual constraints are
`b<e, c<e, c<f, e<g`. Counts by first appearance of `(b,c)`:

```text
choose b: c<e,f and e<g -> 3 contributes b<c
choose c: b<e and e<g with f free -> 6 contributes c<b
```

Thus the `a`-first branch contributes:

```text
b<c: 9 + 3 = 12
c<b: 8 + 6 = 14
```

Combining both root branches:

```text
N(b<c) = 9 + 12 = 21
N(c<b) = 14
lower orientation probability = 14/35 = 2/5
```

## Subcase Conclusion

The fourth matrix bucket has four rank-normal forms and exact generated counts
show lower orientation probability at least `2/5`. The equality form, Case 3,
has a direct hand count above.

This bucket is therefore separated from the current restricted extremal
`14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is still a restricted finite subcase inside R013, not
a proof of the published open problem.
