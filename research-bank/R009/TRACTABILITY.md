# Tractability Assessment

candidate_id: R009
rank: B

## Why This Might Be Tractable

- local structure: recent proofs reduce fixed-runner cases to finite
  computational certificates.
- small cases/computation available: speed tuples, modular reductions, and
  zonotope formulations can be checked exactly.
- known partial results: 2025-2026 papers rapidly extend finite-case coverage
  and identify shifted-variant counterexamples.
- likely proof methods: finite reduction replay, integer programming,
  polyhedral certificates, modular sieving, and exact rational interval checks.

## Why Dianoia Might Add Value

- decomposition advantage: literature aliases, certificate extraction,
  computational replay, and proof packaging are naturally separable.
- subagent specialization: Researcher maps variants; sanity-checker replays
  finite certificates; Prover isolates exact lemmas; Reviewer D attacks
  confusion between original and shifted variants.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py`.
- expected honesty advantage over raw attempt: dianoia should produce a
  replayable certificate or obstruction report instead of an informal global
  proof.

## Risks

- literature risk: finite-case claims are moving quickly in 2025-2026.
- proof-depth risk: high for arbitrary `n`; moderate for certificate
  simplification or a fixed-runner extension.
- computation/formalization risk: computer-assisted proofs must be reproduced
  from exact artifacts, not trusted from prose.
- ambiguity risk: shifted Lonely Runner and spectrum conjectures have different
  truth status from the original.

## Attempt Plan

1. First attack: replay one recent fixed-runner verification using independent
   exact arithmetic.
2. Sanity-check/computation: verify the certificate format on smaller known
   cases before touching the newest case.
3. Literature refresh: distinguish original, shifted, spectrum, and zonotope
   formulations in the attempt log.
4. Adversarial review target: attack every claim for variant confusion and
   unreplayed computer assistance.
