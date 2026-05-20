# Tractability Assessment

candidate_id: R017
rank: A

## Why This Might Be Tractable

- local structure: graceful labeling is a finite injective-labeling constraint
  with exact edge-difference coverage.
- small cases/computation available: all trees up to 35 vertices are reported
  checked, giving a replay target.
- known partial results: caterpillars, bounded-leaf trees, bounded diameter
  trees, and multiple spider families.
- likely proof methods: constructive labeling, transfer lemmas, grafting
  operations, SAT/CP search, and finite obstruction mining.

## Why Dianoia Might Add Value

- decomposition advantage: a solver can search examples, Prover can abstract
  a discovered pattern, Researcher can compare against known tree families,
  and Reviewer D can perform novelty and boundary attacks.
- subagent specialization: labeling search, construction synthesis, literature
  mapping, and adversarial novelty review split cleanly.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-check-small-cases/SKILL.md`, `connectors/arxiv/server.py`,
  and `connectors/lean/server.py` for finite combinatorial lemmas.
- expected honesty advantage over raw attempt: dianoia should isolate a new
  family or downgrade honestly after novelty checks, as the 2026 withdrawal
  shows the trap is real.

## Risks

- literature risk: many special tree families have overlapping names and
  composition lemmas.
- proof-depth risk: the full conjecture is likely out of reach.
- computation/formalization risk: solver-discovered labelings need a symbolic
  construction, not just examples.
- ambiguity risk: graceful, alpha, strongly graceful, and near-graceful
  variants must remain separated.

## Attempt Plan

1. First attack: build a small CP/SAT labeling search over a narrowly
   parameterized tree family not covered by the May 2026 spider papers.
2. Sanity-check/computation: verify generated labelings and edge-difference
   sets exactly.
3. Literature refresh: classify whether the family is already covered by
   caterpillar, spider, transfer, or alpha-labeling results.
4. Adversarial review target: attack novelty, hidden isomorphism to known
   families, and off-by-one edge label coverage.
