# Research Candidate Source

id: R008
area: number theory
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the Erdos-Straus conjecture: for every integer `n >= 2`, find positive
integers `a,b,c` such that

```text
4/n = 1/a + 1/b + 1/c.
```

## Primary Source

- Authors: Marc Chamberland
- Year: 2026
- Title: The Erdos-Straus Conjecture and the Structure of Primes
- Exact statement reference: INTEGERS 26 (2026), introduction
- URL or local artifact: https://math.colgate.edu/~integers/aa42/aa42.pdf
- Relationship to target: recent paper explicitly calls Erdos-Straus an
  unsolved number-theory problem and proves a prime-structure characterization
  for one type of solution.

## Background Sources

1. Authors: Andres Ventas
   Year: 2026
   Title: A Ceiling Continued Fraction Approach to the Erdos-Straus Conjecture
   Exact statement reference: arXiv:2605.04551 abstract
   URL or local artifact: https://arxiv.org/abs/2605.04551
   Relationship to target: recent paper reports heuristic/computational
   evidence and no counterexamples, not a proof.

2. Authors: Eric W. Weisstein
   Year: 2026
   Title: Erdos-Straus Conjecture
   Exact statement reference: MathWorld entry, updated 2026-05-10
   URL or local artifact: https://mathworld.wolfram.com/Erdos-StrausConjecture.html
   Relationship to target: independent reference source classifies the problem
   under unsolved problems and records only bounded verification.

3. Authors: Wikipedia contributors
   Year: 2026
   Title: Erdos-Straus conjecture
   Exact statement reference: current article, Hasse principle discussion
   URL or local artifact: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture
   Relationship to target: independent status and method source; useful for
   aliases, modular obstructions, and partial covering families.

## Candidate Transformation

Target a bounded improvement rather than the full conjecture: reproduce and
stress-test the 2026 prime-structure characterization, then seek a verified
new residue-family cover or a counterexample to a proposed strengthening.
