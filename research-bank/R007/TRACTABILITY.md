# Tractability Assessment

candidate_id: R007
rank: D

## Why This Might Be Tractable

- local structure: recent work isolates alpha(G)=2 subclasses and
  near-complete-minor relaxations.
- small cases/computation available: finite graph searches can test proposed
  strengthenings and find obstructions to variants.
- known partial results: `t <= 6`, alpha(G)=2 special classes, dense-minor
  lower bounds, and near-`K_7` minor theorems.
- likely proof methods: graph-minor reductions, extremal edge counts,
  forbidden induced subgraphs, exact finite search, and proof-certificate
  extraction.

## Why Dianoia Might Add Value

- decomposition advantage: literature mapping, graph generation, minor testing,
  and proof review are separable and auditable.
- subagent specialization: Researcher verifies the exact variant; sanity-checker
  searches small graphs; Prover attempts restricted lemmas; Reviewer D attacks
  false promotion from special class to full conjecture.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py` for small formal graph lemmas.
- expected honesty advantage over raw attempt: dianoia should separate base
  conjecture, odd variants, topological variants, and restricted subclasses.

## Risks

- literature risk: many Hadwiger-named conjectures exist; wrong-target novelty
  claims are likely without strict alias discipline.
- proof-depth risk: extremely high for the full conjecture, especially `t >= 7`.
- computation/formalization risk: minor containment certificates are expensive
  and easy to misstate.
- ambiguity risk: the odd Hadwiger conjecture has recent counterexamples and
  must not be confused with the original graph-minor conjecture.

## Attempt Plan

1. First attack: choose one alpha(G)=2 unknown class from the 2025 arXiv paper
   and attempt a finite obstruction search.
2. Sanity-check/computation: implement small graph generation and minor
   containment checks for the selected restricted class.
3. Literature refresh: verify the selected class is not covered by known
   forbidden-subgraph or dense-minor results.
4. Adversarial review target: attack every statement for accidental reliance on
   a stronger false variant such as odd or topological Hadwiger.
