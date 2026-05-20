# Openness Verification

candidate_id: R002
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

Existence or nonexistence of a perfect cuboid with all three edges, all three
face diagonals, and the space diagonal integral.

## Source Angles

1. Recent source paper:
   - citation: Rene Peschmann, 2026, "Exponent-one blockers and a
     Mordell-Weil construction of Euler bricks", arXiv abstract.
   - exact location: arXiv:2605.00573 abstract.
   - evidence quote: "long-standing open problem"
   - relationship: recent paper declares the target open and reports partial
     obstruction evidence, not a solution.

2. Problem-list/reference source:
   - citation: Eric W. Weisstein, 2026, "Perfect Cuboid", MathWorld entry.
   - exact location: definition/problem discussion, updated 2026-05-10.
   - evidence quote: "No perfect cuboids are known"
   - relationship: independent current reference source classifies the problem
     as unsolved and gives the Diophantine formulation.

3. Independent encyclopedia/status source:
   - citation: Wikipedia contributors, 2026, "Euler brick", Perfect cuboid
     subsection.
   - exact location: Perfect cuboid subsection.
   - evidence quote: "no one has proven that none exist"
   - relationship: independent status source, weaker than MathWorld but useful
     as a live closure check.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'perfect cuboid' --category math.NT --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - query_meta: search query tokenizes `perfect` and `cuboid` with `cat:math.NT`
     and `submittedDate:[202511200000 TO 202605202359]`.
   - evidence: returned recent Peschmann partial-obstruction papers, including
     arXiv:2604.09328 and arXiv:2605.00573; none is recorded here as a closure.
   - relationship: recent arXiv sweep found partial progress and explicit open
     status, not a solved claim.

## Alias And Closure Search

- aliases checked: perfect Euler brick; perfect box; rational cuboid; brick
  problem; diagonals problem.
- stronger theorems checked: Peschmann 2026 master-tuple/fiber obstructions;
  no global nonexistence theorem found.
- special cases checked: bounded fiber exclusions and no-solution searches.
- counterexamples checked: no construction of a perfect cuboid found.
- recent author/citation trails checked: Peschmann 2026 arXiv companion papers,
  MathWorld, Wikipedia status page.

## Verdict

`OPEN-VERIFIED`. The full problem is probably too hard for immediate P11
attack, but bounded obstruction strengthening is a legitimate candidate for
partial progress or an intermediate win.
