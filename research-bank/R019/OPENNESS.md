# Openness Verification

candidate_id: R019
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Ryser-Brualdi-Stein conjecture, especially the odd-order full
transversal component.

## Source Angles

1. Current survey source:
   - citation: Montgomery, 2026, "Transversals in Latin Squares".
   - exact location: Conjecture 3.2 and Section 5.
   - evidence quote: "further ideas would be needed"
   - relationship: records the conjecture and explains why large-even methods
     do not settle the odd full-transversal case.

2. Major partial-progress source:
   - citation: Montgomery, 2023, arXiv:2310.19779.
   - exact location: abstract.
   - evidence quote: "for sufficiently large n"
   - relationship: confirms important progress while leaving finite and odd
     full-transversal aspects outside the theorem.

3. Current open-problem source:
   - citation: Emergent Mind, 2026, "Ryser-Brualdi-Stein conjecture on Latin
     square transversals".
   - exact location: background statement.
   - evidence quote: "remains open in general"
   - relationship: independently records the odd full-transversal part as the
     central remaining target.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Ryser Brualdi Stein Latin square transversal' --category math.CO --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent narrow arXiv closure found in the last six
     months.

## Alias And Closure Search

- aliases checked: Ryser conjecture; Brualdi conjecture; Stein conjecture;
  Latin transversal; partial transversal; rainbow matching in properly colored
  complete bipartite graphs.
- stronger theorems checked: Hall-Paige group-table theorem, large-even
  `n-1` theorem, asymptotic partial transversal bounds, and hypergraph matching
  translations.
- special cases checked: even cyclic Latin squares without full transversals,
  odd group tables satisfying Hall-Paige conditions, large even orders, and
  tripartite matching formulations.
- counterexamples checked: even-order examples without full transversals do
  not refute the partial `n-1` or odd full-transversal claims.
- recent author/citation trails checked: Montgomery survey, Montgomery large
  even theorem, West open-problem page, and current open-problem index.

## Verdict

`OPEN-VERIFIED`. The full combined conjecture remains open, with the odd
full-transversal component especially suitable for restricted-class or
certificate-based P11 work.
