# Research Candidate Source

id: R012
area: combinatorics
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve the Caccetta-Haggkvist conjecture: every `n`-vertex directed graph with
minimum outdegree `r` contains a directed cycle of length at most `ceil(n/r)`.

## Primary Source

- Authors: He Guo
- Year: 2026
- Title: Short rainbow cycles for families of small edge sets
- Exact statement reference: Discrete Mathematics 349 (2026), introduction
- URL or local artifact: https://umu.diva-portal.org/smash/get/diva2%3A2016769/FULLTEXT01.pdf
- Relationship to target: recent paper states the Caccetta-Haggkvist
  conjecture and explicitly says it is still open while proving related
  rainbow-cycle progress.

## Background Sources

1. Authors: Doug West
   Year: 2026
   Title: The Caccetta-Haggkvist Conjecture
   Exact statement reference: open problem page crawled 2026-05
   URL or local artifact: https://dwest.web.illinois.edu/regs/cacchagg.html
   Relationship to target: independent graph-theory problem page collecting
   formulations and references.

2. Authors: Raphael Steiner
   Year: 2026
   Title: Openly disjoint cycles and directed tree-width of regular digraphs
   Exact statement reference: arXiv:2604.13700 abstract
   URL or local artifact: https://arxiv.org/abs/2604.13700
   Relationship to target: recent digraph-cycle paper uses the conjecture and
   regular variants as motivation while proving adjacent degree-condition
   results.

3. Authors: Ron Aharoni, Eli Berger, Maria Chudnovsky, He Guo, Shira Zerbib
   Year: 2023
   Title: Nonuniform Degrees and Rainbow Versions of the Caccetta-Haggkvist
   Conjecture
   Exact statement reference: SIAM Journal on Discrete Mathematics abstract
   URL or local artifact: https://epubs.siam.org/doi/10.1137/22M1529658
   Relationship to target: partial rainbow/nonuniform degree progress and
   variant mapping for novelty checks.

## Candidate Transformation

Target restricted digraph or rainbow-cycle variants first: verify small
minimum-outdegree instances, search for exact extremal examples, and attempt a
new finite-class proof or improved constant in a rainbow generalization.
