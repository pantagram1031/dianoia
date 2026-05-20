# Research Candidate Source

id: R002
area: number theory
target_type: proof | counterexample
status: OPEN-VERIFIED

## Target Statement

Resolve the perfect cuboid problem: determine whether there exist positive
integers `a,b,c,d,e,f,g` satisfying

```text
a^2 + b^2 = d^2
a^2 + c^2 = e^2
b^2 + c^2 = f^2
a^2 + b^2 + c^2 = g^2
```

Equivalently, either construct a perfect Euler brick or prove that none exists.

## Primary Source

- Authors: Rene Peschmann
- Year: 2026
- Title: Exponent-one blockers and a Mordell-Weil construction of Euler bricks
- Exact statement reference: arXiv abstract and companion-paper note
- URL or local artifact: https://arxiv.org/abs/2605.00573
- Relationship to target: 2026 paper explicitly treats the perfect cuboid as a
  long-standing open problem and contributes computational/elliptic obstruction
  evidence without closing it.

## Background Sources

1. Authors: Eric W. Weisstein
   Year: 2026
   Title: Perfect Cuboid
   Exact statement reference: MathWorld entry, lines defining the problem and
   no-known-example statement, updated 2026-05-10
   URL or local artifact: https://mathworld.wolfram.com/PerfectCuboid.html
   Relationship to target: independent problem-list source; classifies the
   target under mathematical problems and unsolved problems.

2. Authors: Wikipedia contributors
   Year: 2026
   Title: Euler brick
   Exact statement reference: Perfect cuboid subsection
   URL or local artifact: https://en.wikipedia.org/wiki/Euler_brick
   Relationship to target: independent current encyclopedic source; states
   that no example or nonexistence proof is known.

## Candidate Transformation

Attempt a bounded obstruction or certificate-strengthening contribution rather
than the full problem first. The first useful target is to reproduce and
independently attack the exponent-one blocker phenomenon on a small, fully
factored subfamily, then seek a sharper obstruction or a verified counterfamily
to a proposed strengthening.
