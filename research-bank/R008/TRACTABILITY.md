# Tractability Assessment

candidate_id: R008
rank: B

## Why This Might Be Tractable

- local structure: many residue classes have explicit parametric Egyptian
  fraction identities.
- small cases/computation available: exact modular and prime-range checks are
  cheap and independently reproducible.
- known partial results: recent 2026 papers give prime-structure targets and
  heuristic finite-counterexample frameworks.
- likely proof methods: modular covers, divisor searches, CRT gluing attempts,
  exact rational identity verification, and certificate generation.

## Why Dianoia Might Add Value

- decomposition advantage: identity discovery, exact verification, literature
  alias checks, and adversarial search for missed residue classes can be split.
- subagent specialization: Researcher checks old identities; sanity-checker
  verifies covers; Prover packages modular lemmas; Reviewer D attacks whether
  a finite search was promoted too far.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py` for modular arithmetic lemmas.
- expected honesty advantage over raw attempt: dianoia should report certified
  subfamilies or failed heuristics without claiming the full conjecture.

## Risks

- literature risk: many residue identities are old and easy to rediscover.
- proof-depth risk: high for the global conjecture; moderate for a new bounded
  cover or structural obstruction.
- computation/formalization risk: searches must emit replayable identities, not
  only numeric success counts.
- ambiguity risk: distinct-denominator variants and `m/n` generalizations must
  not be conflated with the base `4/n` statement.

## Attempt Plan

1. First attack: reproduce Chamberland's Type II prime characterization on a
   bounded prime range with exact identities.
2. Sanity-check/computation: generate residue-cover candidates and verify every
   identity symbolically.
3. Literature refresh: compare each identity against classic Mordell/Schinzel
   and modern computational covers.
4. Adversarial review target: test whether the proposed cover silently excludes
   difficult primes congruent to `1 mod 4`.
