# Tractability Assessment

candidate_id: R013
rank: A

## Why This Might Be Tractable

- local structure: finite posets can be represented exactly by cover relations.
- small cases/computation available: linear extensions can be counted exactly
  by dynamic programming for modest sizes.
- known partial results: several structural classes and computer-assisted
  searches provide replay targets.
- likely proof methods: exact enumeration, balanced-pair search,
  decomposition by width/height, automorphism arguments, and certificate
  extraction.

## Why Dianoia Might Add Value

- decomposition advantage: generation, exact counting, literature comparison,
  and proof packaging are separable.
- subagent specialization: Researcher maps variants; sanity-checker counts
  linear extensions; Prover isolates structural lemmas; Reviewer D attacks
  false promotion from special classes to all posets.
- skill or connector to invoke: `skills/openness-verification/SKILL.md`,
  `skills/adversarial-novelty-check/SKILL.md`,
  `skills/sanity-small-cases/SKILL.md`, `connectors/arxiv/server.py`, and
  `connectors/lean/server.py`.
- expected honesty advantage over raw attempt: dianoia can produce replayable
  poset certificates and avoid vague probabilistic handwaving.

## Risks

- literature risk: many special classes have already been settled.
- proof-depth risk: moderate-high for the full conjecture, but lower for new
  finite-class certificates.
- computation/formalization risk: exact extension counts grow exponentially and
  require canonicalization.
- ambiguity risk: base 1/3-2/3, large-width, gap, and gold-partition variants
  must remain separated.

## Attempt Plan

1. First attack: implement exact linear-extension counting for small posets and
   reproduce a known special-case example.
2. Sanity-check/computation: enumerate non-isomorphic small posets by size and
   compute their best balanced pairs.
3. Literature refresh: check against known width-2, width-3, thin, and forest
   cover-graph results.
4. Adversarial review target: attack any claimed improvement for dependence on
   unlabeled/isomorphic duplication or sampled rather than exact counts.
