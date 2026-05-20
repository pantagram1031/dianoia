# Research Candidate Source

id: R007
area: combinatorics
target_type: proof | counterexample | bound improvement
status: OPEN-VERIFIED

## Target Statement

Resolve Hadwiger's graph-minor conjecture: every graph with chromatic number
at least `t` contains `K_t` as a minor.

## Primary Source

- Authors: Jofre Costa, Eric Luu, David R. Wood, Jung Hon Yip
- Year: 2025
- Title: Verifying Hadwiger's Conjecture for Examples of Graphs with alpha(G)=2
- Exact statement reference: arXiv:2512.17114 abstract
- URL or local artifact: https://arxiv.org/abs/2512.17114
- Relationship to target: recent paper calls Hadwiger's conjecture a major open
  problem and proves additional special classes, explicitly leaving other
  alpha(G)=2 classes unknown.

## Background Sources

1. Authors: Liana Yepremyan and collaborators
   Year: 2025
   Title: Dense minors of graphs with independence number two
   Exact statement reference: Journal of Combinatorial Theory B abstract page
   URL or local artifact: https://www.sciencedirect.com/science/article/abs/pii/S0095895625000619
   Relationship to target: recent partial-progress paper stating that the
   conjecture remains wide open for `t >= 7`.

2. Authors: Agnes Totschnig
   Year: 2026
   Title: Colouring graphs with forbidden 7-vertex minors
   Exact statement reference: University of Waterloo seminar abstract
   URL or local artifact: https://uwaterloo.ca/combinatorics-and-optimization/events/graphs-and-matroids-agnes-totschnig-colouring-graphs
   Relationship to target: current research talk states the cases `k >= 7`
   remain open and reports a near-`K_7` minor result.

3. Authors: Wikipedia contributors
   Year: 2026
   Title: Hadwiger conjecture (graph theory)
   Exact statement reference: current article lead and equivalent forms
   URL or local artifact: https://en.wikipedia.org/wiki/Hadwiger_conjecture_(graph_theory)
   Relationship to target: independent status source stating the conjecture is
   known through `t <= 6` and remains a deep unsolved graph-theory problem.

## Candidate Transformation

Do not attack the full conjecture directly. Target a restricted class with
alpha(G)=2, forbidden induced subgraphs, or near-complete minors, and aim for a
checkable strengthening, counterexample search to a proposed variant, or
formalized finite reduction.
