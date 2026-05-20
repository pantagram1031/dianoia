# adversarial-novelty-check

description: Use before treating any result as novel or before adding a
`CLAIMS.md` row with confidence high enough for external review.

## When To Use

- An attempt appears to solve an open problem.
- A proof gives a counterexample to a published conjecture.
- A bound, construction, or reduction appears stronger than the literature.
- A reviewer asks whether the result is already known under another name.

## When Not To Use

- The work is exploratory and no novelty or priority claim is being made.
- A claim has already been downgraded to exposition or benchmark-only evidence.
- The only output is a local bug fix, connector, or skill update.

## Procedure

1. Restate the candidate contribution in one sentence and one formal version.
2. Generate at least five independent attacks:
   - renamed theorem or folklore result;
   - stronger known theorem implies it;
   - local claim is only a specialization of a source theorem;
   - hidden hypothesis mismatch makes it false or already trivial;
   - counterexample exists in small cases or databases;
   - dual/complement/category-equivalent formulation is known;
   - proof depends on an unverified source or circular lemma.
3. For each attack, search or compute enough to either refute it or downgrade
   the claim. Record artifact paths and exact citations.
4. Reviewer D must write `novelty-review.md` with at least five attacks,
   status for each (`REFUTED`, `SURVIVES`, `DOWNGRADES`, `FATAL`), and file
   evidence.
5. If any attack is `FATAL`, mark the claim `DOWNGRADED`.
6. If any attack `SURVIVES` without refutation, keep confidence below 8 and do
   not halt for external review.
7. Only if all attacks are refuted and openness verification is current may the
   claim proceed to the P12 gate.

## Examples

Example attack row:

```text
attack: stronger known theorem may imply the bound
search: arXiv last six months for exact invariant + "improved bound"
evidence: research-bank/R012/novelty/attack-2.md
status: REFUTED
reason: found papers concern dense regime; candidate is sparse planar regime
```

Example downgrade:

```text
attack: local theorem is specialization of Theorem 3.4 in 2024 survey
status: FATAL
action: CLAIMS.md status DOWNGRADED; write correction note
```

