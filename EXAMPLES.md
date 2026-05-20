# Examples

## B1: S_a Finiteness Retest

The current complete walkthrough is benchmark B1, derived from the Phase 3
retest of the S_a problem.

## Source

`benchmark-bank/B1/SOURCE.md` records the source as:

- Authors: Boris Alexeev; Moe Putterman; Mehtaab Sawhney; Mark Sellke; Gregory
  Valiant
- Year: 2026
- Title: "Short proofs in combinatorics, probability and number theory II"
- Exact statement reference: Section 6 Theorem 6.1 / arXiv:2604.06609
- Area: number theory

The benchmark asks for finiteness of the set

```text
S_a = { n > 0 : for every integer k with 1 <= k <= sqrt(n/a)
      and gcd(k,n)=1, n-a k^2 is prime }
```

and requires honesty about whether explicit bounds or complete small-a lists are
proved.

## Raw Attempt

The raw baseline lives outside this repo at
`C:\Users\SAMSUNG\Downloads\raw-attempt-2`. Its recorded outcome was:

```text
Finiteness: proved by citation to APSSV 2026 Theorem 6.1.
Explicit bound: not supplied.
Small-case completeness: not supplied.
```

It also recorded that it had no claim ledger, reviewer files, or adversarial
checks.

## Dianoia Attempt

The dianoia run lives at
`C:\Users\SAMSUNG\Downloads\dianoia-run\problems\p3-sa-finiteness-apssv-2026`.
It was deliberately started with stale active state to verify that the Phase 2
routing fix worked. `capability-test/RETEST.md` records:

```text
prior_active: fake-halted-p3-sa-20260520-182055
route: prompts/prove.md
new_slug: p3-sa-finiteness-apssv-2026
```

The run also ledgered the endpoint bridge:

```text
C-003: The set S_a in the user statement is the APSSV admissible set, with
endpoint k=sqrt(n/a) harmless because n-a k^2=0 is not prime.
```

## Comparison Verdict

`benchmark-bank/B1/COMPARISON.md` records VALUE_ADDED for three reasons:

1. Dianoia proved the stale-active routing fix fired; the raw attempt had no
   comparable machinery.
2. Dianoia recorded an endpoint bridge in the claim ledger; the raw attempt only
   stated that the citation applied.
3. Dianoia recorded reviewer and consolidated review artifacts; the raw attempt
   explicitly had no adversarial review files.

The B1 row is appended to `BENCHMARK.md`. It is only 1 of the 5 VALUE_ADDED rows
needed for MASTERPIECE.
