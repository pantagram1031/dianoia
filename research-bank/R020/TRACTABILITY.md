# Tractability Assessment

candidate_id: R020
rank: A

## Why This Might Be Tractable

- local structure: a candidate solution is a finite grid-point set with exact
  integer collinearity checks.
- small cases/computation available: CSP certificates exist through a current
  finite frontier.
- known partial results: prime-field constructions, CSP exact cases,
  checkerboard variants, and extensible lower bounds.
- likely proof methods: SAT/CSP encoding, exact determinant checks,
  symmetry-breaking, finite certificate replay, and modular constructions.

## Why Dianoia Might Add Value

- decomposition advantage: one subagent can search configurations, another can
  verify certificates, Researcher can separate variants, and Reviewer D can
  attack hidden use of torus/checkerboard assumptions.
- subagent specialization: CSP modeling, exact line-check verification,
  literature/variant mapping, and proof-note packaging split cleanly.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-check-small-cases/SKILL.md`, `connectors/arxiv/server.py`,
  and `connectors/oeis/server.py` for sequence/status checks.
- expected honesty advantage over raw attempt: dianoia can emit exact
  certificate files and downgrade to partial progress without pretending a
  finite range solves the asymptotic problem.

## Risks

- literature risk: many variants share the same name but change grid, torus,
  parity, or extensibility constraints.
- proof-depth risk: global asymptotic upper bounds may be hard.
- computation/formalization risk: CSP certificates must be replayable from
  coordinates and line constraints.
- ambiguity risk: `D(n)=2n` exact finite cases and Guy-Kelly asymptotic
  conjectures must remain separate.

## Attempt Plan

1. First attack: replay one current CSP certificate and build a deterministic
   verifier for `D(n)=2n` coordinate files.
2. Sanity-check/computation: implement exact determinant line checks and
   symmetry normalization.
3. Literature refresh: distinguish ordinary grid, checkerboard, torus, greedy,
   and extensible variants.
4. Adversarial review target: attack any claimed improvement for variant
   leakage, incomplete line families, and non-replayable search output.
