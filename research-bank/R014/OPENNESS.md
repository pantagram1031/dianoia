# Openness Verification

candidate_id: R014
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The unconditional Artin primitive root conjecture over the rational integers.

## Source Angles

1. Recent arXiv source:
   - citation: Goldmakher, Martin, and Peringuey, 2025, "Refinements of Artin's
     primitive root conjecture", arXiv:2502.19601.
   - exact location: abstract.
   - evidence quote: "remains open"
   - relationship: current work proves refinements under GRH and weaker
     unconditional versions, not the full conjecture.

2. Current reference source:
   - citation: Wikipedia contributors, 2026, "Artin's conjecture on primitive
     roots".
   - exact location: lead and partial-results section.
   - evidence quote: "still unresolved as of 2026"
   - relationship: independent current source and partial-result summary.

3. Open-problem source:
   - citation: Emergent Mind, 2026, "Artin's primitive root conjecture".
   - exact location: background/references.
   - evidence quote: "unconditional proof remains unknown"
   - relationship: current problem-bank source separating GRH-conditional work
     from unconditional openness.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Artin primitive root conjecture' --category math.NT --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned `[]` on 2026-05-20.
   - relationship: no recent narrow arXiv closure found; 2025 refinement paper
     and current sources still mark the base target open.

## Alias And Closure Search

- aliases checked: Artin primitive root conjecture; Artin's conjecture on
  primitive roots; primitive roots modulo infinitely many primes.
- stronger theorems checked: Hooley's GRH-conditional proof, Chebotarev
  density refinements, function-field analogues, Artin-type matrix variants.
- special cases checked: fixed `a=2`, Heath-Brown alternatives among `2,3,5`,
  perfect-power and `a_0 mod 4` exceptional density cases.
- counterexamples checked: no accepted counterexample found; exceptional `a`
  values are outside the conjecture's hypotheses.
- recent author/citation trails checked: Goldmakher-Martin-Peringuey 2025,
  Emergent Mind problem page, current encyclopedia status, and BWT-related
  Artin open variant.

## Verdict

`OPEN-VERIFIED`. This is a number-theory candidate with useful computational
and formal subtargets, but every claim must keep GRH-conditional and
unconditional statements separate.
