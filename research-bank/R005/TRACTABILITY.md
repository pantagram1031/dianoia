# Tractability Assessment

candidate_id: R005
rank: B

## Why This Might Be Tractable

- local structure: minimal counterexample formulations impose lattice and
  frequency constraints that can be checked exactly.
- small cases/computation available: finite families on small ground sets can
  be enumerated, reduced by isomorphism, and independently verified.
- known partial results: constant-factor lower bounds and FC-family special
  cases offer benchmarks for partial progress.
- likely proof methods: exact search, compression, entropy inequalities,
  lattice duality, and certificate extraction for small counterexample
  exclusions.

## Why Dianoia Might Add Value

- decomposition advantage: the problem naturally splits into literature
  verification, candidate generation, small-case search, and proof-certificate
  review.
- subagent specialization: Researcher tracks alias formulations;
  sanity-checker runs exact enumeration; Prover isolates checkable lemmas;
  Reviewer D attacks accidental proof of only a special case.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py` for small formal lemmas.
- expected honesty advantage over raw attempt: dianoia should report certified
  exclusions or failed generalizations instead of asserting a full proof from
  suggestive entropy heuristics.

## Risks

- literature risk: many equivalent forms make novelty checking easy to get
  wrong.
- proof-depth risk: high for the full conjecture; moderate for bounded
  classifications or strengthened necessary conditions.
- computation/formalization risk: exact enumeration can explode without
  isomorphism reductions.
- ambiguity risk: "Frankl's conjecture" appears in several neighboring
  formulations; every claim must pin down the exact dual.

## Attempt Plan

1. First attack: reproduce a small FC-family classification with canonical
   search output.
2. Sanity-check/computation: generate all union-closed families on small ground
   sets up to isomorphism and verify frequency certificates.
3. Literature refresh: map lattice, graph, and entropy formulations before any
   novelty claim.
4. Adversarial review target: test whether a proposed condition is merely
   equivalent to a known small-case theorem.
