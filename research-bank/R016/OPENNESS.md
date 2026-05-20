# Openness Verification

candidate_id: R016
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

Barnette's conjecture for all 3-connected cubic bipartite planar graphs.

## Source Angles

1. Current reference source:
   - citation: Eric W. Weisstein, 2026, "Barnette's Conjecture", MathWorld.
   - exact location: statement paragraph.
   - evidence quote: "the general conjecture remains open"
   - relationship: gives the exact target and records finite verification
     below 66 vertices only.

2. Independent encyclopedia/status source:
   - citation: Wikipedia contributors, 2026, "Barnette's conjecture".
   - exact location: article lead.
   - evidence quote: "unsolved problem in graph theory"
   - relationship: independent status source for the same Hamiltonicity
     statement.

3. Recent partial-progress source:
   - citation: Ozeki et al., 2025, "Barnette Graphs with Faces up to Size 8
     are Hamiltonian", arXiv:2508.03531.
   - exact location: abstract.
   - evidence quote: "Barnette's conjecture states"
   - relationship: proves a restricted family, not the full conjecture.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Barnette conjecture Hamiltonian cubic bipartite planar' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no narrow recent arXiv closure found in the last six
     months.

## Alias And Closure Search

- aliases checked: Barnette's conjecture; cubic bipartite planar Hamiltonian
  conjecture; bicubic polyhedral Hamiltonian conjecture.
- stronger theorems checked: Tutte-style planar cubic Hamiltonicity,
  non-bipartite cubic planar counterexamples, face-size-bounded refinements.
- special cases checked: graphs below 66 vertices, face-size restricted
  classes, facial 2-factor classes.
- counterexamples checked: known non-Hamiltonian cubic planar examples are
  outside the bipartite 3-connected target.
- recent author/citation trails checked: 2025 arXiv partial, MathWorld,
  Wikipedia, and recent search results.

## Verdict

`OPEN-VERIFIED`. The full statement remains open, while finite graph
generation and Hamiltonian-cycle certificates give concrete bounded P11
targets.
