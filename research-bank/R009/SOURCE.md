# Research Candidate Source

id: R009
area: number theory
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the Lonely Runner Conjecture in full generality: for distinct integer
speeds, each runner on a unit circle is eventually at distance at least `1/n`
from every other runner.

## Primary Source

- Authors: Tony Bohman, Ron Holzman, Dan Kleitman, and collaborators surveyed
  by Goddyn and later authors
- Year: 2024
- Title: The Lonely Runner Conjecture turns 60
- Exact statement reference: arXiv:2409.20160 abstract
- URL or local artifact: https://arxiv.org/abs/2409.20160
- Relationship to target: recent survey describes the conjecture as widely
  open while summarizing steady partial progress.

## Background Sources

1. Authors: Touch Sungkawichai and Tanupat Trakulthongchai
   Year: 2026
   Title: Eleven, twelve, and thirteen lonely runners
   Exact statement reference: arXiv:2604.23906 abstract
   URL or local artifact: https://arxiv.org/abs/2604.23906
   Relationship to target: very recent partial progress gives computer-assisted
   verification for additional finite runner counts, not the general theorem.

2. Authors: Ho Tin Fan and Alec Sun
   Year: 2026
   Title: Amending the Lonely Runner Spectrum Conjecture
   Exact statement reference: Electronic Journal of Combinatorics 33(1), intro
   URL or local artifact: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p38/pdf/
   Relationship to target: current paper calls Lonely Runner a long-standing
   number-theory problem and studies a sharper spectrum variant.

3. Authors: Wikipedia contributors
   Year: 2026
   Title: Lonely runner conjecture
   Exact statement reference: current article lead and status notes
   URL or local artifact: https://en.wikipedia.org/wiki/Lonely_runner_conjecture
   Relationship to target: independent status source records solved finite
   cases and that the general case remains unsolved.

## Candidate Transformation

Target a verified computational or structural increment: replay the recent
finite-runner proofs, isolate one certificate bottleneck, and either simplify a
finite-case certificate or find a counterexample to a shifted/generalized
variant without confusing it with the base conjecture.
