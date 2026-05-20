# Tractability Assessment

candidate_id: R006
rank: C

## Why This Might Be Tractable

- local structure: finite unit-distance graphs provide exact witnesses for
  lower-bound work.
- small cases/computation available: graph coloring, SAT, exact distance, and
  certificate-minimization checks are automatable.
- known partial results: de Grey and Polymath16 provide graph data, reduction
  goals, and well-defined certificate standards.
- likely proof methods: SAT-backed coloring obstruction, graph minimization,
  exact algebraic-coordinate checks, and independent certificate replay.

## Why Dianoia Might Add Value

- decomposition advantage: the problem splits into graph construction,
  exact-coordinate validation, chromatic-number certification, and novelty
  checking against Polymath data.
- subagent specialization: Researcher maps existing graphs; sanity-checker
  verifies colorability certificates; Prover formalizes exact-distance lemmas;
  Reviewer D attacks hidden numerical assumptions.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py`.
- expected honesty advantage over raw attempt: dianoia can avoid broad claims
  and instead produce replayable graph certificates or obstruction reports.

## Risks

- literature risk: Polymath data and informal blog threads make novelty
  checking messy.
- proof-depth risk: full exact value may be out of reach; finite-certificate
  improvements are more realistic.
- computation/formalization risk: SAT certificates and algebraic coordinates
  must be independently reproducible.
- ambiguity risk: chromatic number of the plane, fractional variants, and
  region-coloring variants must not be conflated.

## Attempt Plan

1. First attack: reproduce a known 5-chromatic graph certificate and identify
   one minimization or certificate-simplification subgoal.
2. Sanity-check/computation: verify unit distances and non-4-colorability for
   imported finite graphs.
3. Literature refresh: compare against Polymath16 graph records before
   declaring any graph smaller or simpler.
4. Adversarial review target: attack whether a proposed witness relies on
   approximate coordinates rather than exact unit-distance relations.
