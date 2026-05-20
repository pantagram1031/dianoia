# Tractability Assessment

candidate_id: R011
rank: C

## Why This Might Be Tractable

- local structure: Hanner polytopes and shadow systems provide explicit
  geometric objects and perturbation directions.
- small cases/computation available: polytopal examples can be represented by
  rational vertices/facets and checked with exact convex-geometry routines in
  low dimension.
- known partial results: dimensions 2 and 3, unconditional bodies, zonoids, and
  local-minimality neighborhoods.
- likely proof methods: convex duality, polar-volume computation, shadow-system
  monotonicity, stability estimates, and exact polytope calculations.

## Why Dianoia Might Add Value

- decomposition advantage: source mapping, exact polytope computation, local
  lemma proving, and Reviewer D geometric counterchecks can be split cleanly.
- subagent specialization: Researcher maps known special classes;
  sanity-checker verifies rational polytope examples; Prover works on local
  inequalities; Reviewer D attacks hidden smoothness or symmetry assumptions.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py` for formalizable convex-combinatorial lemmas.
- expected honesty advantage over raw attempt: dianoia should focus on local
  lemmas or explicit counterexamples to stronger variants, not full Mahler.

## Risks

- literature risk: many special-class proofs and equivalent formulations create
  high duplication risk.
- proof-depth risk: very high for the full higher-dimensional conjecture.
- computation/formalization risk: exact polar-volume computation is delicate
  and may need specialized convex-geometry tooling.
- ambiguity risk: symmetric, non-symmetric, dimension-three, and
  higher-dimensional statements must be separated.

## Attempt Plan

1. First attack: reproduce exact Mahler volume for small Hanner polytopes and
   simple perturbations in dimension 4.
2. Sanity-check/computation: implement rational vertex/facet polar conversion
   for small polytopes.
3. Literature refresh: map dimension-three shadow-system arguments before
   claiming any local higher-dimensional extension.
4. Adversarial review target: attack whether any lemma only works for
   unconditional or dimension-three bodies.
