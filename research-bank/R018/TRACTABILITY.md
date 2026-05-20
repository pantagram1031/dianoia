# Tractability Assessment

candidate_id: R018
rank: C

## Why This Might Be Tractable

- local structure: polytopes reduce illumination to finitely many normal-cone
  and direction-cover constraints.
- small cases/computation available: dimension 3 subclasses can be modeled by
  integer linear programming and explicit direction sets.
- known partial results: zonoids, bodies of constant width, symmetric classes,
  1-unconditional bodies, and cap bodies.
- likely proof methods: convex duality, polytope approximation, normal fan
  covering, probabilistic rotations, and finite ILP certificates.

## Why Dianoia Might Add Value

- decomposition advantage: Researcher can map equivalent formulations, a
  computation subagent can test finite polytope instances, Prover can package a
  restricted lemma, and Reviewer D can attack compactness/limit steps.
- subagent specialization: convex-geometry literature, exact rational polytope
  computation, illumination-direction search, and adversarial review split
  naturally.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-check-small-cases/SKILL.md`, `connectors/arxiv/server.py`,
  and `connectors/lean/server.py` for finite convexity lemmas.
- expected honesty advantage over raw attempt: dianoia should confine claims
  to a verified class and preserve all compactness assumptions.

## Risks

- literature risk: many equivalent formulations use different constants and
  equality cases.
- proof-depth risk: general dimension 3 is already highly resistant.
- computation/formalization risk: numerical illumination directions must be
  converted to exact certificates.
- ambiguity risk: illumination number, covering number, translative covering,
  fractional illumination, and complex illumination variants must stay
  separated.

## Attempt Plan

1. First attack: reproduce a finite ILP illumination certificate for a simple
   3D cap-body or centrally symmetric polytope class.
2. Sanity-check/computation: verify each direction illuminates the claimed
   normal cones with rational inequalities.
3. Literature refresh: distinguish body classes already covered by 2024-2026
   partial results.
4. Adversarial review target: attack limiting arguments, equality cases, and
   hidden smoothness or symmetry assumptions.
