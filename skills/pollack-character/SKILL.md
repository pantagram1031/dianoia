# pollack-character

description: Use Pollack-style prime character residue/nonresidue input when a
number-theory argument needs many small primes with prescribed quadratic
character behavior.

## When To Use

- A problem reduces to finding primes `p` with a quadratic character condition
  such as `chi(p)=1` or `chi(p)=-1`.
- A proof needs many small primes in residue classes attached to a quadratic
  extension or squarefree discriminant.
- A finiteness proof for expressions like `n-a k^2` needs a small prime divisor
  forced by solvability of a congruence.
- A subagent must decide whether a cited character-result is enough, or whether
  ineffectivity blocks explicit bounds.

## When Not To Use

- The needed character is not quadratic and no reduction to a quadratic
  character has been proved.
- The problem requires explicit numerical constants and the only available
  input depends on Siegel-type ineffective bounds.
- The argument only needs elementary congruences or quadratic reciprocity.
- The target is computational enumeration rather than a proof or obstruction.

## Procedure

1. Identify the modulus, conductor, or quadratic field that defines the
   character.
2. State the exact desired sign condition and why it implies the needed
   congruence or divisibility fact.
3. Verify the source has all four citation fields: author, year, title, exact
   theorem/proposition/section.
4. Mark whether the result is effective or ineffective. If ineffective, block
   any explicit-bound claim.
5. Add a bridge lemma connecting the character conclusion to the target
   arithmetic statement.
6. Record unresolved constants or exceptional ranges as gaps, not as proved
   facts.

## Examples

Example trigger:

```text
Need primes p <= n^(3/8) such that a*x^2 == n mod p is solvable.
```

Expected use:

```text
Use the quadratic character attached to Q(sqrt(d)). Cite the Pollack/APSSV
input for many small primes with chi(p)=1. Then prove a bridge lemma from
chi(p)=1 to solvability of a*x^2 == n mod p.
```

Example non-use:

```text
Need exact maximum of S_1.
```

Reason not to use:

```text
Pollack-style input proves finiteness but does not by itself provide the exact
finite list or an explicit maximum.
```
