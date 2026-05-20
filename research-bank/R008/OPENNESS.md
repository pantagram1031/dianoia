# Openness Verification

candidate_id: R008
verified_date: 2026-05-20
status: OPEN-VERIFIED

## Exact Target Checked

The full Erdos-Straus conjecture for all integers `n >= 2`.

## Source Angles

1. Recent journal source:
   - citation: Marc Chamberland, 2026, "The Erdos-Straus Conjecture and the
     Structure of Primes", INTEGERS 26.
   - exact location: introduction.
   - evidence quote: "unsolved number theory problem"
   - relationship: current source gives a partial prime-structure theorem and
     a new auxiliary conjecture, not a closure of Erdos-Straus.

2. Recent arXiv source:
   - citation: Andres Ventas, 2026, "A Ceiling Continued Fraction Approach to
     the Erdos-Straus Conjecture", arXiv:2605.04551.
   - exact location: abstract.
   - evidence quote: "show no counterexamples"
   - relationship: computational and heuristic evidence, not a proof.

3. Independent reference source:
   - citation: Eric W. Weisstein, 2026, "Erdos-Straus Conjecture", MathWorld.
   - exact location: entry body and subject classification.
   - evidence quote: "Unsolved Problems"
   - relationship: current reference source records bounded verification, not
     a theorem.

4. Recent search:
   - tool/query: `python connectors/arxiv/server.py search 'Erdos Straus conjecture' --category math.NT --from-date 2025-11-20 --max-results 5`
   - date window: 2025-11-20 to 2026-05-20
   - evidence: returned arXiv:2605.04551; no closure paper found in this
     connector sweep.
   - relationship: recent arXiv check found heuristic/computational progress,
     not accepted resolution.

## Alias And Closure Search

- aliases checked: Erdos-Straus; Erdos-Strauss; Egyptian fraction 4/n; Schinzel
  variants; prime form of the conjecture.
- stronger theorems checked: modular covering identities, almost-all results,
  bounded computational verification, and prime-structure Type I/II solution
  characterizations.
- special cases checked: even `n`, residue classes, prime denominators, and
  high-range computational searches.
- counterexamples checked: no accepted counterexample found; recent searches
  explicitly report no counterexamples in tested ranges.
- recent author/citation trails checked: Chamberland 2026, Ventas 2026,
  MathWorld, and current encyclopedia status.

## Verdict

`OPEN-VERIFIED`. The full conjecture is not a good first proof target, but
bounded residue-family certification and exact-search counterchecks are
tractable P11 tasks.
