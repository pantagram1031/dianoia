# Tractability Assessment

candidate_id: R010
rank: C

## Why This Might Be Tractable

- local structure: finite matrices provide explicit instances for exact
  discrepancy search and certificate replay.
- small cases/computation available: brute-force and MILP checks can certify
  exact discrepancies for small matrices.
- known partial results: polylogarithmic bounds, smoothed-analysis results, and
  Beck-Fiala progress define measurable gaps.
- likely proof methods: vector balancing, randomized rounding, entropy method,
  matrix discrepancy lower bounds, and exact finite countersearch.

## Why Dianoia Might Add Value

- decomposition advantage: theory survey, exact instance search,
  computational certificates, and adversarial gap analysis can run separately.
- subagent specialization: Researcher tracks variants; sanity-checker computes
  exact small discrepancies; Prover packages restricted lemmas; Reviewer D
  attacks hidden dependence on `n` or dimension.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py` for finite matrix lemmas.
- expected honesty advantage over raw attempt: dianoia should keep conditional,
  smoothed, and worst-case claims separate.

## Risks

- literature risk: several adjacent discrepancy conjectures have similar names
  and different constants.
- proof-depth risk: high for the full constant bound; moderate for exact
  finite hard instances or restricted classes.
- computation/formalization risk: exact discrepancy certificates require
  exhaustive sign checks or independently checkable optimization certificates.
- ambiguity risk: Beck-Fiala, Steinitz, signed-series, and Komlos variants must
  be separated.

## Attempt Plan

1. First attack: build a tiny exact-discrepancy checker for rational matrices
   and reproduce known small examples.
2. Sanity-check/computation: enumerate structured small matrices and identify
   candidate hard instances.
3. Literature refresh: compare any bound or instance against Bansal-style
   current records and smoothed-analysis exceptions.
4. Adversarial review target: attack whether a claimed constant secretly
   depends on matrix size, dimension, or rounding precision.
