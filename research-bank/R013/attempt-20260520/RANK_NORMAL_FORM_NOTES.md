# R013 Rank Normal Form Notes

date: 2026-05-20
status: OBSERVATION-NOT-CLAIM

## Scope

This note rewrites the extremal matrix bucket from
`width3-rank2221-extremal-matrix-bucket-n7.json` in rank-layer normal form.
The point is to remove arbitrary search labels before trying a hand proof.

Fix rank layers of sizes `2,2,2,1`, written as:

```text
L0 = {a,b}, L1 = {c,d}, L2 = {e,f}, L3 = {g}.
```

The common cover matrix is:

```text
[[0,2,2,0],
 [0,0,2,1],
 [0,0,0,1],
 [0,0,0,0]]
```

Within the restricted finite bucket, the generated artifact records exactly the
following three rank-normal cover patterns.

## Normal Forms

### Case A

Cover relations:

```text
a<c, a<d, b<e, b<f, c<e, c<f, d<g, e<g
```

Exact count:

- linear extensions: 39
- balanced pair: `{b,c}`
- orientation counts: `c<b` in `14/39`, `b<c` in `25/39`
- lower orientation probability: `14/39`

### Case B

Cover relations:

```text
a<c, a<e, a<f, b<d, c<g, d<e, d<f, e<g
```

Exact count:

- linear extensions: 33
- balanced pair: `{a,b}`
- orientation counts: `b<a` in `19/33`, `a<b` in `14/33`
- lower orientation probability: `14/33`

### Case C

Cover relations:

```text
a<c, a<d, b<e, b<f, c<e, c<g, d<f, f<g
```

Exact count:

- linear extensions: 33
- balanced pair: `{c,d}`
- orientation counts: `d<c` in `6/11`, `c<d` in `5/11`
- lower orientation probability: `5/11`

## Sublemma Target

Finite evidence now reduces the extremal matrix bucket to:

> In the common cover-matrix bucket above, every case has a balanced pair with
> lower orientation probability at least `14/39`, and equality occurs only in
> Case A.

This sublemma is not yet a human proof. The next proof move is to derive the
three normal forms directly from the cover matrix plus width/height constraints,
then compute or bound the listed orientation counts without relying on the
search labels.

## Claim Discipline

No `CLAIMS.md` row. This is a normalized finite case split and proof target,
not a publishable claim or a contribution.
