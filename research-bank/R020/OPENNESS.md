# Openness Verification

candidate_id: R020
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The exact no-three-in-line function `D(n)` for all `n`, with particular focus
on unknown large `n` and the status of the `2n` upper bound.

## Source Angles

1. Recent exact-computation source:
   - citation: Prellberg, 2026, arXiv:2602.07751.
   - exact location: abstract.
   - evidence quote: "unknown whether D(n)=2n"
   - relationship: identifies the current finite frontier rather than closing
     the general problem.

2. Current encyclopedia/status source:
   - citation: Wikipedia contributors, 2026, "No-three-in-line problem".
   - exact location: upper/lower bounds section.
   - evidence quote: "is not known"
   - relationship: independent status source for the exact-function problem.

3. Recent variant-progress source:
   - citation: Prellberg, 2026, arXiv:2605.09215.
   - exact location: abstract.
   - evidence quote: "classical no-three-in-line problem"
   - relationship: current work on a checkerboard-restricted variant, not a
     full solution of `D(n)`.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'no-three-in-line problem' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned arXiv:2602.07751, arXiv:2605.07000, arXiv:2603.00215,
     and arXiv:2605.09215 on 2026-05-20.
   - relationship: current arXiv activity is partial/variant progress, not an
     accepted closure of the exact general problem.

## Alias And Closure Search

- aliases checked: no-three-in-line problem; Dudeney grid problem;
  no-three-collinear grid points; Guy-Kelly conjecture; extensible
  no-three-in-line problem.
- stronger theorems checked: `D(n)=2n` for all `n`, eventual strict upper
  bounds below `2n`, checkerboard-restricted variants, and extensible variants.
- special cases checked: finite CSP certificates through the current frontier,
  prime-field constructions, checkerboard parity classes, and greedy/minimum
  variants.
- counterexamples checked: no accepted full resolution of the exact `D(n)`
  function found.
- recent author/citation trails checked: 2026 CSP paper, 2026 checkerboard
  paper, 2026 extensible lower-bound note, Wikipedia status, and arXiv search.

## Verdict

`OPEN-VERIFIED`. This is highly suitable for P11 because every proposed
advance can be attached to exact grid coordinates, line checks, or CSP
certificates.
