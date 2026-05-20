# Tractability Assessment

candidate_id: R015
rank: B

## Why This Might Be Tractable

- local structure: finite point configurations can be encoded by order types
  and SAT constraints.
- small cases/computation available: known `g(6)=17` and related certificates
  provide replay targets.
- known partial results: exact small values, near-tight upper bounds, relaxed
  split-polygon thresholds, and SAT/ASP encodings.
- likely proof methods: oriented-matroid/order-type enumeration, SAT
  certificates, combinatorial geometry reductions, and exact convexity checks.

## Why Dianoia Might Add Value

- decomposition advantage: source mapping, SAT replay, order-type checking,
  and proof-note packaging are independent.
- subagent specialization: Researcher tracks known values; sanity-checker
  validates order-type certificates; Prover isolates relaxed-variant lemmas;
  Reviewer D attacks geometric degeneracy assumptions.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py`.
- expected honesty advantage over raw attempt: dianoia should produce
  certificate replay or a bounded relaxed result rather than claiming all `n`.

## Risks

- literature risk: many Erdos-Szekeres variants use similar names but different
  point-position constraints.
- proof-depth risk: high for the full formula beyond `n=6`.
- computation/formalization risk: SAT certificates and order-type encodings
  must be independently replayable.
- ambiguity risk: convex, empty, colored, split, and higher-dimensional
  variants must remain separated.

## Attempt Plan

1. First attack: replay a small known SAT/order-type certificate for `g(6)=17`
   or a relaxed split-polygon theorem.
2. Sanity-check/computation: implement exact orientation predicates and convex
   subset checks for finite order types.
3. Literature refresh: separate happy ending, empty polygon, colored, and
   split-polygon variants.
4. Adversarial review target: attack any proposed improvement for hidden
   general-position, realizability, or variant-assumption gaps.
