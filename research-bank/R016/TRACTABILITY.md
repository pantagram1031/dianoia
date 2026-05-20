# Tractability Assessment

candidate_id: R016
rank: B

## Why This Might Be Tractable

- local structure: planar, cubic, bipartite, and 3-connected constraints are
  exact and generate finite search spaces by vertex count.
- small cases/computation available: published verification below 66 vertices
  gives a replay baseline.
- known partial results: face-size, facial 2-factor, and sufficient-condition
  subclasses.
- likely proof methods: planar duality, reducible configurations,
  Hamiltonian-cycle SAT/search certificates, and discharging-style case splits.

## Why Dianoia Might Add Value

- decomposition advantage: Researcher can separate equivalent formulations,
  sanity-checker can replay finite generation, Prover can isolate a subclass,
  and Reviewer D can attack hidden connectivity assumptions.
- subagent specialization: graph generator, Hamiltonicity verifier, literature
  mapper, and adversarial reviewer can work independently.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-check-small-cases/SKILL.md`, `connectors/arxiv/server.py`,
  and `connectors/lean/server.py` for small formal lemmas.
- expected honesty advantage over raw attempt: dianoia should return a
  certified subclass or explicit obstruction search, not a handwavy global
  proof.

## Risks

- literature risk: many papers claim algorithmic or partial proofs; novelty
  checks must distinguish accepted results from unreviewed claims.
- proof-depth risk: full Hamiltonicity is likely too deep.
- computation/formalization risk: planar cubic graph generation must avoid
  duplicates and preserve 3-connectivity.
- ambiguity risk: Barnette's bipartite conjecture and face-size-at-most-six
  variant must remain separated.

## Attempt Plan

1. First attack: replay known finite verification on a small generated slice,
   then identify the first unreplayed family boundary.
2. Sanity-check/computation: generate cubic bipartite planar candidates and
   independently verify Hamiltonian cycles.
3. Literature refresh: map face-size and facial 2-factor partial results.
4. Adversarial review target: attack any claimed reduction for lost
   3-connectivity, planarity, bipartiteness, or Hamiltonian-cycle lift.
