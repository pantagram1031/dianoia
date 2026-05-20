# R013 Branch Enumeration Ledger

date: 2026-05-21
status: OBSERVATION-NOT-CLAIM

## Scope

This ledger hand-enumerates the residual branch counts left by
`RECURRENCE_LEDGER.md` for the three rank-normal cases in the common cover
matrix subcase.

Notation: after a listed prefix is fixed, only the remaining cover constraints
are shown. A chain/shuffle count such as `e < g with f free` is a direct count
of the listed residual linear extensions.

## Case A

Case A covers:

```text
a<c, a<d, b<e, b<f, c<e, c<f, d<g, e<g
```

Checked pair: `(c,b)`.

### Prefix `a,b`

Residual constraints: `c<e,f`, `d<g`, `e<g`.

```text
choose c:
  residual d,e,f,g with d<g and e<g
  choose d: e<g with f free -> 3
  choose e: d<g with f free -> 3
  choose f: d<g and e<g -> 2
  subtotal 8

choose d:
  residual c,e,f,g with c<e,f and e<g
  choose c: e<g with f free -> 3
  subtotal 3

total 11
```

Since `b` has already appeared before `c`, this contributes
`(N_c,N_b)=(0,11)`.

### Prefix `a,c`

Residual constraints: `b<e,f`, `d<g`, `e<g`. This is isomorphic to the
previous residual by swapping `b` with `c`, so the total is `11`.

Since `c` has already appeared before `b`, this contributes
`(N_c,N_b)=(11,0)`.

### Prefix `a,d`

Residual constraints: `b<e,f`, `c<e,f`, `e<g`.

If `c` appears before `b`, then after choosing `c`, `b` is forced next before
`e` and `f` become available. The residual `e<g` with `f` free has `3`
extensions. By symmetry, the same count holds for `b` before `c`.

Thus this contributes `(N_c,N_b)=(3,3)`.

Combining the depth-2 branches:

```text
after a: (0,11) + (11,0) + (3,3) = (14,14)
after b: (0,11)
total:   (14,25)
```

## Case B

Case B covers:

```text
a<c, a<e, a<f, b<d, c<g, d<e, d<f, e<g
```

Checked pair: `(a,b)`.

### Prefix `a,b`

Residual constraints: `c<g`, `d<e,f`, `e<g`.

```text
choose c:
  residual d,e,f,g with d<e,f and e<g
  choose d: e<g with f free -> 3
  subtotal 3

choose d:
  residual c,e,f,g with c<g and e<g
  two prerequisites c,e must precede g, with f free -> 8
  subtotal 8

total 11
```

Since `a` has already appeared before `b`, this contributes
`(N_a,N_b)=(11,0)`.

### Prefix `a,c`

Residual constraints: `b<d`, `d<e,f`, `e<g`.

The prefix forces `b,d`; the remaining residual is `e<g` with `f` free, which
has `3` extensions. This contributes `(N_a,N_b)=(3,0)`.

### Prefix `b,a`

The residual constraints match the `a,b` residual above, so the total is `11`.
Since `b` has already appeared before `a`, this contributes
`(N_a,N_b)=(0,11)`.

### Prefix `b,d`

Residual constraints: `a<c,e,f`, `c<g`, `e<g`.

The prefix forces `a`; the remaining residual is `c<g` and `e<g` with `f`
free, which has `8` extensions. This contributes `(N_a,N_b)=(0,8)`.

Combining the depth-2 branches:

```text
after a: (11,0) + (3,0) = (14,0)
after b: (0,11) + (0,8) = (0,19)
total:   (14,19)
```

## Case C

Case C covers:

```text
a<c, a<d, b<e, b<f, c<e, c<g, d<f, f<g
```

Checked pair: `(c,d)`.

### Prefix `a,b`

Residual constraints: `c<e,g`, `d<f`, `f<g`.

For `c` before `d`, choose `c` first. The remaining residual is `d<f<g` with
`e` free, giving `4` extensions.

For `d` before `c`, choose `d` first:

```text
choose c next: f<g with e free -> 3
choose f next: c<e,g -> 2
subtotal 5
```

Thus this contributes `(N_c,N_d)=(4,5)`.

### Prefix `a,c`

Residual constraints: `b<e,f`, `d<f`, `f<g`.

```text
choose b:
  residual d,e,f,g with d<f<g and e free -> 4
choose d:
  residual b,e,f,g with b<e,f and f<g
  choose b: f<g with e free -> 3
total 7
```

Since `c` has already appeared before `d`, this contributes
`(N_c,N_d)=(7,0)`.

### Prefix `a,d`

Residual constraints: `b<e,f`, `c<e,g`, `f<g`.

```text
choose b:
  residual c,e,f,g with c<e,g and f<g
  choose c: f<g with e free -> 3
  choose f: c<e,g -> 2
  subtotal 5

choose c:
  residual b,e,f,g with b<e,f and f<g
  choose b: f<g with e free -> 3
  subtotal 3

total 8
```

Since `d` has already appeared before `c`, this contributes
`(N_c,N_d)=(0,8)`.

### Prefix `b,a`

The residual constraints match the `a,b` residual above, so this contributes
`(N_c,N_d)=(4,5)`.

Combining the depth-2 branches:

```text
after a: (4,5) + (7,0) + (0,8) = (11,13)
after b: (4,5)
total:   (15,18)
```

## Subcase Conclusion

The hand enumeration agrees with the generated recurrence artifacts:

| Case | Pair | Orientation counts | Lower probability |
|------|------|--------------------|-------------------|
| A | `(c,b)` | `(14,25)` | `14/39` |
| B | `(a,b)` | `(14,19)` | `14/33` |
| C | `(c,d)` | `(15,18)` | `5/11` |

Therefore, inside the already-derived common cover-matrix subcase, the three
rank-normal forms have lower orientation probability at least `14/39`, with
equality only in Case A.

## Claim Discipline

No `CLAIMS.md` row. This is a finite restricted subcase of R013, not a proof of
the published open problem.
