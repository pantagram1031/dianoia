# Tractability Assessment

candidate_id: R002
rank: C

## Why This Might Be Tractable

- local structure: recent papers reduce parts of the problem to explicit
  parametric families, genus-three curves, elliptic quotients, and finite
  factorization checks.
- small cases/computation available: connector and local Python can reproduce
  bounded modular, parity, and square checks before any proof claim.
- known partial results: 2026 arXiv papers report large verified obstruction
  families and failed strengthening variants.
- likely proof methods: exact integer arithmetic, modular obstructions,
  elliptic-curve rank-zero certificates, and adversarial search for false
  generalizations.

## Why Dianoia Might Add Value

- decomposition advantage: the target breaks into many independently checkable
  obstruction families and failed-strengthening tests.
- subagent specialization: Researcher verifies literature and closure claims;
  sanity-checker reproduces small searches; Prover isolates lemmas; Reviewer D
  attacks overgeneralized computational claims.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py` for formalizable modular lemmas.
- expected honesty advantage over raw attempt: dianoia should avoid claiming
  the full perfect cuboid problem and instead report bounded verified
  obstructions.

## Risks

- literature risk: recent 2026 preprints may contain unverified strong claims;
  any improvement must be novelty-checked with care.
- proof-depth risk: high for global nonexistence; moderate for bounded or
  parameter-family obstruction lemmas.
- computation/formalization risk: computations require exact arithmetic and
  reproducible factorization trails.
- ambiguity risk: "perfect cuboid conjecture" may refer to existence,
  nonexistence, or equivalent parameterized forms.

## Attempt Plan

1. First attack: reproduce the quartic-pair equivalence on a small parametric
   slice using exact arithmetic.
2. Sanity-check/computation: enumerate small `a,b,m,n` and compare with
   Peschmann obstruction claims.
3. Literature refresh: inspect all 2026 companion papers and claimed proof
   preprints before any novelty claim.
4. Adversarial review target: attack whether a bounded obstruction has been
   silently promoted to global nonexistence.
