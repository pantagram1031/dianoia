# Openness Verification

candidate_id: R012
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Caccetta-Haggkvist conjecture for all finite directed graphs.

## Source Angles

1. Recent journal source:
   - citation: He Guo, 2026, "Short rainbow cycles for families of small edge
     sets", Discrete Mathematics 349.
   - exact location: introduction.
   - evidence quote: "conjecture is still open"
   - relationship: current source states the base conjecture and proves
     related rainbow-cycle progress.

2. Recent arXiv source:
   - citation: Raphael Steiner, 2026, "Openly disjoint cycles and directed
     tree-width of regular digraphs", arXiv:2604.13700.
   - exact location: abstract.
   - evidence quote: "famous Caccetta-Haggkvist conjecture"
   - relationship: active 2026 digraph-cycle work motivated by the conjecture,
     not a proof of it.

3. Independent problem page:
   - citation: Doug West, 2026, "The Caccetta-Haggkvist Conjecture".
   - exact location: reference/problem page.
   - evidence quote: "main problem"
   - relationship: independent problem page and reference trail for the
     classical statement.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Caccetta Haggkvist conjecture' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent narrow arXiv closure was found; openness verdict
     relies on the current source angles above.

## Alias And Closure Search

- aliases checked: Caccetta-Haggkvist; directed girth conjecture; short cycles
  in digraphs; minimum outdegree directed cycle problem.
- stronger theorems checked: regular variants, Behzad-Chartrand-Wall variant,
  rainbow-cycle generalizations, nonuniform degree versions.
- special cases checked: triangle case, regular digraph cases, rainbow `r=2`
  and `r=3` variants, dense digraph partial results.
- counterexamples checked: no accepted counterexample to the base conjecture
  found; counterexamples to stronger regular/openly-disjoint variants are
  tracked separately.
- recent author/citation trails checked: Guo 2026, Steiner 2026, Aharoni
  rainbow-generalization work, and West's reference page.

## Verdict

`OPEN-VERIFIED`. This is a good P11 candidate for finite exact search and
restricted-class progress, with high risk of variant confusion requiring
Reviewer D attention.
