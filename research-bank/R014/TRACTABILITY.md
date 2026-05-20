# Tractability Assessment

candidate_id: R014
rank: C

## Why This Might Be Tractable

- local structure: primitive-root status modulo a prime is exactly checkable by
  factoring `p-1`.
- small cases/computation available: density experiments for fixed `a` are
  easy to reproduce for bounded prime ranges.
- known partial results: GRH-conditional proof, Heath-Brown alternatives, and
  recent refinement conjectures give bounded subtargets.
- likely proof methods: computational density checks, finite Chebotarev
  inclusion-exclusion, order-distribution lemmas, and exact modular arithmetic.

## Why Dianoia Might Add Value

- decomposition advantage: factorization checks, density experiments,
  literature status, and conditional-proof separation are independent.
- subagent specialization: Researcher guards GRH/variant status;
  sanity-checker verifies primitive-root data; Prover packages elementary
  order lemmas; Reviewer D attacks conditional-to-unconditional slippage.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py`.
- expected honesty advantage over raw attempt: dianoia should report bounded
  data or conditional lemmas without pretending GRH has been removed.

## Risks

- literature risk: Artin-type variants in number fields, function fields, and
  matrices can be mistaken for the integer conjecture.
- proof-depth risk: very high for unconditional full density.
- computation/formalization risk: density experiments are only evidence unless
  tied to exact finite claims.
- ambiguity risk: primitive root, near-primitive root, order comparison, and
  truncated-order variants must remain distinct.

## Attempt Plan

1. First attack: implement exact primitive-root tests for fixed `a` over a
   bounded prime range and reproduce Artin-constant convergence plots.
2. Sanity-check/computation: verify factorization and order calculations with
   independent routines.
3. Literature refresh: separate Hooley/GRH, Heath-Brown, function-field, and
   refinement statements.
4. Adversarial review target: attack any proposed theorem for hidden GRH,
   ineffective constants, or exceptional `a` values.
