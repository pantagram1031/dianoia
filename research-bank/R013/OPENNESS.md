# Openness Verification

candidate_id: R013
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The 1/3-2/3 conjecture for all finite non-chain posets.

## Source Angles

1. Current seminar source:
   - citation: Jeff Kahn and Max Aires, 2026, "Balancing extensions in posets
     of large width", Harvard-MIT Combinatorics.
   - exact location: seminar abstract.
   - evidence quote: "far from proving either"
   - relationship: current expert source explicitly says the 1/3-2/3
     conjecture and related width conjecture remain unproved.

2. ArXiv progress paper:
   - citation: Olson and Sagan, 2018, "On the 1/3-2/3 Conjecture",
     arXiv:1706.04985.
   - exact location: abstract.
   - evidence quote: "make progress"
   - relationship: proves certain families only, leaving the general
     conjecture open.

3. Classic special-case source:
   - citation: Brightwell and Wright, 1992, "The 1/3-2/3 Conjecture for
     5-Thin Posets", SIAM Journal on Discrete Mathematics.
   - exact location: abstract.
   - evidence quote: "established in the case"
   - relationship: special-case result, not a full proof.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search '1/3 2/3 conjecture posets' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent narrow arXiv closure was found; current seminar
     evidence is the strongest live-status source.

## Alias And Closure Search

- aliases checked: 1/3-2/3 conjecture; balanced pair conjecture; balancing
  linear extensions; poset linear extension probability.
- stronger theorems checked: large-width balancing, gold-partition conjecture,
  gap conjectures, cover-graph special cases.
- special cases checked: 5-thin posets, N-free ordered sets, forest cover
  graphs, lattices, dimension-2 and width-bounded cases.
- counterexamples checked: no accepted counterexample to the base conjecture
  found; stronger gap/gold-partition variants are tracked separately.
- recent author/citation trails checked: Kahn-Aires 2026 seminar, Olson-Sagan,
  Brightwell-Wright, and current encyclopedia status.

## Verdict

`OPEN-VERIFIED`. The finite and computational nature of linear-extension
probabilities makes this a strong exact-checkable P11 candidate.
