# R013 Second Matrix Bucket Notes

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This note classifies the second-ranked matrix bucket from
`MATRIX_BUCKET_ROADMAP.md`.

Signature:

```text
layers=2,2,2,1|covers=7|mins=2|maxs=2|cover_matrix=[[0,2,0,0],[0,0,3,0],[0,0,0,2],[0,0,0,0]]
```

Artifacts:

- `width3-rank2221-second-matrix-bucket-n7.json`: extraction from the
  restricted matrix bucket.
- `width3-rank2221-second-cover-matrix-forms-n7.json`: direct derivation from
  rank shape plus cover matrix.
- `normal-form-cases/case-second-bucket.json`: named normal-form input.
- `normal-form-cases/case-second-bucket-report.json`: replayed count report.
- `normal-form-cases/case-second-bucket-recurrence-depth2.json`: recurrence
  trace for the checked pair.

## Derived Normal Form

The cover matrix derives exactly one rank-normal form:

```text
rank layers: {a,b}, {c,d}, {e,f}, {g}
covers:      a<c, a<d, c<e, c<f, d<e, e<g, f<g
```

The element `b` is isolated. The non-isolated part has `a` forced first, then
five remaining elements subject to:

```text
c<e, c<f, d<e, e<g, f<g
```

The checked balanced pair is `(b,d)`.

## Hand Count

After `a`, the five extensions of the remaining non-isolated core are:

```text
c d e f g
c d f e g
c f d e g
d c e f g
d c f e g
```

Since `b` is isolated, there are seven insertion slots for `b` in each full
six-element non-isolated extension, giving `5 * 7 = 35` total linear
extensions.

Count insertions with `b<d`:

```text
b first before a: 5 extensions

after prefix a:
  c d e f g: 2 insertion slots for b before d
  c d f e g: 2 insertion slots for b before d
  c f d e g: 3 insertion slots for b before d
  d c e f g: 1 insertion slot for b before d
  d c f e g: 1 insertion slot for b before d
  subtotal: 9

total b<d: 5 + 9 = 14
```

Thus:

```text
N(b<d) = 14
N(d<b) = 35 - 14 = 21
lower orientation probability = 14/35 = 2/5
```

This matches `case-second-bucket-report.json` and the depth-2 recurrence
artifact.

## Subcase Conclusion

Inside this singleton matrix bucket, the pair `(b,d)` is balanced with lower
orientation probability `2/5`. This is strictly above the current restricted
extremal value `14/39`.

## Claim Discipline

No `CLAIMS.md` row. This is one restricted finite subcase of R013, not a proof
of the published open problem.
