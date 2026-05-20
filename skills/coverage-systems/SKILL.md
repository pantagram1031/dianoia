# coverage-systems

description: Use finite congruence or residue-class coverage searches to prove
that every remaining candidate is eliminated, or to find the precise uncovered
classes that block completeness.

## When To Use

- A proof or computation claims a finite list is complete.
- A problem reduces to showing every integer in a range or residue class family
  hits at least one obstruction.
- A small-case sanity check needs to distinguish "no counterexample found" from
  "all cases covered by a certificate."
- A benchmark failure involved incomplete finite enumeration, uncovered residue
  classes, or missing exact small-a lists.

## When Not To Use

- The target is only existential finiteness and no explicit finite list or
  effective bound is being claimed.
- The modulus product or search space is not justified by a proof.
- Coverage is probabilistic or heuristic and cannot produce a checkable
  certificate.
- A simpler direct lemma closes the case without enumeration.

## Procedure

1. State the universe being covered: interval, congruence classes, or parameter
   family.
2. State each obstruction as a checkable predicate.
3. Record the modulus or finite domain that makes coverage finite.
4. Produce either a certificate listing covered classes or an explicit list of
   uncovered classes.
5. Verify the certificate with an independent small script or hand-checkable
   table.
6. If uncovered classes remain, return `GAP` with the smallest representative
   and the obstruction that would close it.

## Examples

Example trigger:

```text
Show the displayed S_2 list is complete.
```

Expected use:

```text
Build congruence obstructions for n-a*k^2 composite, choose a finite modulus
only after proving periodicity, then emit covered and uncovered residue classes.
If classes remain, do not claim completeness.
```

Example output:

```text
status: GAP
uncovered_classes_mod_M: [17, 113, 401]
suffices: find a new prime obstruction or prove no candidates in these classes.
```
