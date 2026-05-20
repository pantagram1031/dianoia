# Openness Verification

candidate_id: R021
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The Erdos-Gyarfas conjecture for all finite graphs with minimum degree at least
3.

## Source Angles

1. Current open-problem source:
   - citation: Emergent Mind, 2026, "Erdos-Gyarfas power-of-two cycles
     problem".
   - exact location: background statement.
   - evidence quote: "general case is unresolved"
   - relationship: directly records the live open target.

2. Independent status source:
   - citation: Wikipedia contributors, 2024, "Erdos-Gyarfas conjecture".
   - exact location: article lead.
   - evidence quote: "unproven"
   - relationship: independent summary of statement, known counterexample
     searches, and special cases.

3. Recent partial-progress source:
   - citation: Emergent Mind, 2026, page for arXiv:2508.19302.
   - exact location: background and reference note.
   - evidence quote: "partial progress"
   - relationship: diameter-2 graphs are verified, leaving the general problem
     open.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Erdos Gyarfas conjecture power two cycles' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no narrow recent arXiv closure found in the last six months;
     web search instead found partial/status sources.

## Alias And Closure Search

- aliases checked: Erdos-Gyarfas conjecture; power-of-two cycle lengths;
  2-power cycle problem; minimum degree 3 cycle conjecture.
- stronger theorems checked: large minimum degree/dense settings,
  diameter-2 graphs, cubic planar graphs, claw-free planar graphs, and
  bounded-induced-star variants.
- special cases checked: cubic counterexample searches, Markstrom extremal
  graphs, 3-connected cubic planar graphs, diameter-2 graphs, and dense graphs.
- counterexamples checked: known search examples avoid short powers but still
  contain longer power-of-two cycles, so they do not refute the conjecture.
- recent author/citation trails checked: Emergent Mind status pages, West open
  problem page, Wikipedia known-results summary, and arXiv connector search.

## Verdict

`OPEN-VERIFIED`. The target is exact and graph-search-friendly, with natural
bounded certificate work before any full proof claim.
