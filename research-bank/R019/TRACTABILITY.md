# Tractability Assessment

candidate_id: R019
rank: B

## Why This Might Be Tractable

- local structure: Latin transversals are exact matchings with row, column, and
  symbol constraints.
- small cases/computation available: finite Latin squares and group tables can
  be enumerated or sampled.
- known partial results: large-even `n-1` theorem, Hall-Paige group-table
  theorem, and strong asymptotic partial-transversal bounds.
- likely proof methods: rainbow matching, absorption, hypergraph matching,
  permutation-covering reformulations, and exact counterexample search.

## Why Dianoia Might Add Value

- decomposition advantage: Researcher can map equivalent variants, a
  computation subagent can verify small Latin squares, Prover can isolate a
  restricted family, and Reviewer D can attack parity and variant assumptions.
- subagent specialization: Latin-square enumeration, rainbow-matching
  translation, literature separation, and adversarial novelty review can run
  independently.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-check-small-cases/SKILL.md`, `connectors/arxiv/server.py`,
  and `connectors/lean/server.py` for finite matching lemmas.
- expected honesty advantage over raw attempt: dianoia should separate
  partial-transversal and full-transversal statements and avoid falsely using
  even-order counterexamples against the odd conjecture.

## Risks

- literature risk: modern results may solve asymptotic versions under similar
  names.
- proof-depth risk: absorption arguments are technically heavy.
- computation/formalization risk: enumerating Latin squares scales rapidly and
  requires isomorphism control.
- ambiguity risk: Latin squares, arrays, quasigroups, rainbow matchings, and
  Steiner triple systems have related but non-identical conjectures.

## Attempt Plan

1. First attack: target a restricted odd-order Latin-square family expressible
   by group or quasigroup extensions.
2. Sanity-check/computation: implement exact transversal search and verify
   small examples or candidate obstructions.
3. Literature refresh: map whether the family follows from Hall-Paige,
   Montgomery large-even methods, or known rainbow-matching theorems.
4. Adversarial review target: attack any proof for parity leakage, partial vs
   full transversal confusion, and hidden quasigroup assumptions.
