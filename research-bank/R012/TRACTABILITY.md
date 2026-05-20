# Tractability Assessment

candidate_id: R012
rank: B

## Why This Might Be Tractable

- local structure: finite directed graphs allow exhaustive search, SAT/MILP
  encodings, and exact cycle certificates.
- small cases/computation available: minimum-outdegree and directed-girth
  constraints are easy to check on generated graphs.
- known partial results: triangle case bounds, dense digraph results, rainbow
  variants, and regular-variant obstructions.
- likely proof methods: extremal digraph analysis, cycle-shortening, finite
  obstruction search, rainbow-cycle reductions, and exact certificate replay.

## Why Dianoia Might Add Value

- decomposition advantage: subagents can independently search examples,
  verify cycle certificates, and map variants.
- subagent specialization: Researcher separates base and rainbow statements;
  sanity-checker enumerates small digraphs; Prover isolates finite-class
  lemmas; Reviewer D attacks overclaims from variants.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py`.
- expected honesty advantage over raw attempt: dianoia should preserve exact
  graph certificates and distinguish base conjecture from stronger false
  variants.

## Risks

- literature risk: many variants are close enough to invite false novelty.
- proof-depth risk: high for the full conjecture; moderate for bounded classes
  or improved constants.
- computation/formalization risk: exact graph generation must avoid isomorphic
  duplication and encode loops/multiple arcs correctly.
- ambiguity risk: directed girth, rainbow girth, regular variants, and
  openly-disjoint cycle problems must not be conflated.

## Attempt Plan

1. First attack: reproduce small extremal examples and verify the conjectured
   cycle bound by exhaustive search.
2. Sanity-check/computation: implement exact directed-girth and minimum
   outdegree checks for small graphs.
3. Literature refresh: map which rainbow/regular variants imply or do not
   imply the base statement.
4. Adversarial review target: attack any claimed proof for hidden use of
   regularity, density, or non-star color-class assumptions.
