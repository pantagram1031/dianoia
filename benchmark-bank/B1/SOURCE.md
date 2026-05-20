# B1 Source

## Metadata

- Authors: Boris Alexeev; Moe Putterman; Mehtaab Sawhney; Mark Sellke; Gregory Valiant
- Year: 2026
- Title: "Short proofs in combinatorics, probability and number theory II"
- Exact statement reference: Section 6 Theorem 6.1 / arXiv abstract finiteness theorem for integers `n` such that `n-a k^2` is prime for all `k <= sqrt(n/a)` coprime to `n`, for fixed `a in Z_+`

## Source

arXiv:2604.06609, DOI-style URL: `https://arxiv.org/abs/2604.06609`.

## Modification

The benchmark asks dianoia and the raw baseline to handle the set

`S_a = { n > 0 : for every integer k with 1 <= k <= sqrt(n/a) and gcd(k,n)=1, n-a k^2 is prime }`

and to state honestly whether explicit bounds or complete small-a lists are
proved. This is a direct modification of the APSSV finiteness statement by
adding the explicit endpoint convention and the honesty check about bounds and
lists.

## Area

number theory

## Artifacts

- Raw baseline: `C:\Users\SAMSUNG\Downloads\raw-attempt-2`
- Dianoia run: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\p3-sa-finiteness-apssv-2026`
- Retest report: `capability-test/RETEST.md`
