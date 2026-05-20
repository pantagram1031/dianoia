# Tractability Assessment

candidate_id: R021
rank: B

## Why This Might Be Tractable

- local structure: cycles of lengths `4, 8, 16, ...` are exact finite graph
  witnesses.
- small cases/computation available: known computer searches constrain
  possible cubic counterexamples.
- known partial results: cubic planar, 3-connected cubic planar, diameter-2,
  dense minimum-degree, and claw-free planar classes.
- likely proof methods: extremal graph structure, BFS layering, cycle-space
  parity, bounded counterexample search, and discharging in planar subclasses.

## Why Dianoia Might Add Value

- decomposition advantage: graph generation, cycle detection, literature
  separation, and proof attack are independent.
- subagent specialization: computational search can verify bounded classes,
  Prover can abstract structural reductions, Researcher can map special cases,
  and Reviewer D can attack degree/minor assumptions.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-check-small-cases/SKILL.md`, `connectors/arxiv/server.py`,
  and `connectors/lean/server.py` for finite graph lemmas.
- expected honesty advantage over raw attempt: dianoia can report explicit
  graph-class certificates or counterexample-search lower bounds, avoiding a
  fake global proof.

## Risks

- literature risk: several special cases are solved and can be mistaken for
  the general conjecture.
- proof-depth risk: arbitrary minimum-degree-three graphs may require new
  structural ideas.
- computation/formalization risk: counterexample search must control
  isomorphism, minimum degree, and simple-cycle enumeration.
- ambiguity risk: average degree, minimum degree, cubic-only, planar-only, and
  induced-subgraph variants must remain separated.

## Attempt Plan

1. First attack: build a bounded graph-search harness for minimum-degree-three
   graphs and verify power-of-two cycle witnesses.
2. Sanity-check/computation: replay known small extremal examples and special
   class certificates.
3. Literature refresh: separate dense, planar, cubic, diameter, and induced
   star-free results.
4. Adversarial review target: attack any proof for accidental use of stronger
   degree, connectivity, planarity, or induced-subgraph assumptions.
