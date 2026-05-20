# openness-verification

description: Use when deciding whether a problem, conjecture, bound, or
possible contribution is still open enough to enter the research bank or pass a
research-claim gate.

## When To Use

- Adding a candidate to `research-bank/`.
- Promoting an attempt to `SOLVED-CLAIM-PENDING-GATES`.
- Checking whether a conjecture, open problem, or bound has been solved,
  renamed, generalized, specialized, or superseded.
- Updating an openness trail within seven days of a research attempt.

## When Not To Use

- The task is only benchmark source scope checking and no research contribution
  is being claimed.
- The claim is explicitly internal and not positioned as novel.
- The source already says the statement is closed and the attempt is only
  expository.

## Procedure

1. Record the exact target statement before searching. Include hypotheses,
   parameter ranges, exceptions, and whether the goal is proof,
   counterexample, bound improvement, or connection.
2. Collect at least three independent source angles:
   - original paper or problem list;
   - recent survey, monograph, or problem collection;
   - recent search over arXiv/MathSciNet-like metadata, author pages, seminar
     notes, or citation trails from the last six months when available.
3. For each source, record author, year, title, exact location, URL or local
   artifact path, search date, and relationship to the target statement.
4. Search for equivalent names, dual formulations, complements, parameter
   shifts, stronger theorems, special cases, and known counterexamples.
5. Classify the result:
   - `OPEN-VERIFIED`: three independent angles support openness and no closure
     was found;
   - `OPEN-WEAK`: fewer than three angles or sources are old;
   - `LIKELY-CLOSED`: a plausible solution or stronger theorem was found;
   - `AMBIGUOUS`: wording mismatch prevents a clean decision.
6. Write `OPENNESS.md` in the relevant `research-bank/<id>/` directory.
7. If verification is older than seven days at attempt time, rerun the search
   before any P11 or P12 promotion.

## Examples

Example `OPENNESS.md` entry:

```text
status: OPEN-VERIFIED
verified_date: 2026-05-21
angle_1: original paper, Section 8 Problem 8.1, says finite classification remains open
angle_2: 2026 survey, Section 4.3, lists the same problem as open
angle_3: arXiv search 2025-11..2026-05 for exact title terms found no solution
known_aliases_checked: induced saturation number zero; isolated H-free graphs
```

Example downgrade:

```text
status: LIKELY-CLOSED
reason: a 2026 preprint proves a stronger theorem under the same hypotheses
action: do not add to research-bank as open; cite as background instead
```

