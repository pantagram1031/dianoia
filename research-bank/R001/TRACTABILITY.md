# Tractability Assessment

candidate_id: R001
rank: A

## Why This Might Be Tractable

- local structure: a transitive tournament on `Q` has a dense linear order that
  supplies witnesses between any reversed pair.
- small cases/computation available: the directed 3-cycle case can be checked
  by enumerating triples around one perturbed arc.
- known partial results: the source notes the rational-order tournament as a
  single-arc example for the directed triangle in Problem 8.3.
- likely proof methods: density of `Q`, local finiteness, and a witness
  avoiding the finite set of arcs incident to a chosen perturbed pair.

## Why Dianoia Might Add Value

- decomposition advantage: the target splits into T-free baseline, choose a
  perturbed arc, avoid finitely many incident perturbations, and orient a
  triangle.
- subagent specialization: Researcher verifies whether the special case is
  already in the literature; Prover writes the short lemma; Reviewer D attacks
  whether the proof silently assumes single-arc perturbation.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `connectors/arxiv/server.py`, and `connectors/lean/server.py` if a finite
  order lemma is formalized.
- expected honesty advantage over raw attempt: dianoia should downgrade if the
  proof is already implicit in the source or if openness evidence stays weak.

## Risks

- literature risk: the special case may be too immediate to count as novel.
- proof-depth risk: low; likely a warm-up lemma rather than a publication-grade
  contribution.
- computation/formalization risk: low for finite triples, moderate for
  encoding locally finite perturbations formally.
- ambiguity risk: the source's single-arc example may already be intended to
  cover the locally finite version for directed triangles.

## Attempt Plan

1. First attack: prove the rational-order tournament over `Q` satisfies the
   locally finite directed-triangle property.
2. Sanity-check/computation: enumerate finite approximations with one reversed
   arc and witness vertices between endpoints.
3. Literature refresh: search exact phrases from Conjecture 8.4 and directed
   triangle variants.
4. Adversarial review target: attack novelty and the step choosing a witness
   not incident to any perturbation involving the selected arc endpoints.
