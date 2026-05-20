# Openness Verification

candidate_id: R017
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Graceful Tree Conjecture for all finite trees.

## Source Angles

1. Current reference source:
   - citation: Eric W. Weisstein, 2026, "Graceful Tree Theorem", MathWorld.
   - exact location: status paragraph.
   - evidence quote: "no proof or refutation"
   - relationship: current source directly records open status.

2. Recent partial and novelty-check source:
   - citation: Tong Niu, 2026, arXiv:2605.02303.
   - exact location: abstract.
   - evidence quote: "no general proof is known"
   - relationship: May 2026 arXiv trail confirms the full conjecture remains
     unsolved despite special-family work.

3. Recent partial-progress source:
   - citation: Shan and Zhong, 2026, arXiv:2605.14295.
   - exact location: abstract.
   - evidence quote: "known to hold for several classes"
   - relationship: proves two spider-family results, not the full conjecture.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'graceful tree conjecture' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned arXiv:2605.02303v2 and arXiv:2605.14295v2 on
     2026-05-20.
   - relationship: current arXiv evidence shows partial progress and no
     accepted closure.

## Alias And Closure Search

- aliases checked: graceful tree conjecture; Ringel-Kotzig conjecture;
  Kotzig graceful tree theorem; graceful labeling of trees.
- stronger theorems checked: universal graceful-labeling constructions,
  claimed complete proofs, and class-composition theorems.
- special cases checked: caterpillars, small-leaf trees, bounded diameter,
  spiders, trees with perfect matchings, and finite checks through 35 vertices.
- counterexamples checked: none accepted in the status sources.
- recent author/citation trails checked: May 2026 arXiv spider-family papers,
  MathWorld, Wikipedia/status search, and withdrawal novelty note.

## Verdict

`OPEN-VERIFIED`. Exact finite searches and special-family construction lemmas
make this a strong P11 candidate for partial progress.
