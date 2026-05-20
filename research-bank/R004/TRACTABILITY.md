# Tractability Assessment

candidate_id: R004
rank: D

## Why This Might Be Tractable

- local structure: equivalent formulations allow small, bounded algebraic
  searches and formal comparison of statements.
- small cases/computation available: finite-dimensional algebras over small
  finite fields can be searched for false strengthenings, though not for a
  general proof.
- known partial results: many positive special classes are known.
- likely proof methods: radical theory, polynomial-ring formulations, finite
  algebra search, and careful special-class reductions.

## Why Dianoia Might Add Value

- decomposition advantage: dianoia can maintain an explicit map of equivalent
  statements and prevent using a special-case theorem as if it were general.
- subagent specialization: Researcher verifies special-case boundaries; prover
  formalizes equivalences; sanity-checker searches small finite algebras;
  Reviewer D attacks hidden unitality/associativity assumptions.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, and `connectors/arxiv/server.py`.
- expected honesty advantage over raw attempt: dianoia should produce a
  boundary map or obstruction rather than claiming a general proof.

## Risks

- literature risk: many equivalent formulations and special cases make it easy
  to overclaim.
- proof-depth risk: extremely high for the full conjecture.
- computation/formalization risk: finite searches can miss infinite-ring
  phenomena.
- ambiguity risk: unital vs nonunital and left/right/two-sided ideal language
  must be pinned down.

## Attempt Plan

1. First attack: write a claim map of the equivalent formulations used in
   Ferrero's survey and current references.
2. Sanity-check/computation: search small finite-dimensional algebras for
   counterexamples to tempting but stronger finite analogues.
3. Literature refresh: inspect the 2025 partial-result page and cited paper
   before any attempt.
4. Adversarial review target: attack every use of a special-class theorem as
   if it solved the general case.
