# citation-discipline

description: Use strict citation checks when a mathematical claim depends on a
paper, theorem, database entry, survey node, corpus row, or benchmark source and
the support must be traceable without overclaiming.

## When To Use

- A proof, survey, review, or benchmark cites external work.
- A claim is supported by a paper title or abstract but lacks an exact theorem,
  proposition, lemma, section, page, or equation reference.
- A subagent needs to decide whether a citation is complete enough to enter the
  ledger as `CITED`.
- A reviewer must check novelty, duplication, state-of-the-art relationship, or
  dependency traceability.

## When Not To Use

- The artifact contains only internal algebra whose dependencies are already
  ledgered and no external reference is invoked.
- The task is exploratory brainstorming and no claim will be promoted,
  benchmarked, or used downstream.
- The citation is purely bibliographic background and not used as evidence for
  a mathematical assertion.

## Procedure

1. For every citation-like dependency, require four fields: author, year, title,
   and exact statement reference.
2. Separate `verified` references from `unverified` references before reasoning
   with them.
3. Do not let abstracts, titles, OEIS comments, or vague survey mentions support
   theorem-level claims unless they contain the exact statement needed.
4. Record how the cited statement matches the local claim: identical,
   specialization, weakening, strengthening, analogy, or search lead.
5. If the local claim is only a specialization or weakening of prior work,
   require the result headline to say so plainly.
6. Mark missing fields as `[REFERENCE NEEDS VERIFICATION]` or `UNVERIFIED`
   rather than filling them from memory.
7. Before a claim enters `claim_ledger.md` as `CITED`, confirm the dependency is
   complete and the local use does not require extra hypotheses.

## Examples

Example complete citation:

```text
authors: Boris Alexeev; Moe Putterman; Mehtaab Sawhney; Mark Sellke; Gregory Valiant
year: 2026
title: Short proofs in combinatorics, probability and number theory II
exact_statement_reference: Section 6, Theorem 6.1
relationship: local statement specializes the APSSV admissible-set finiteness theorem
```

Example incomplete citation:

```text
APSSV proves this somewhere on arXiv.
```

Expected response:

```text
status: UNVERIFIED
missing: exact statement reference and relationship to local hypotheses
do_not_use_downstream: true
```

Example review use:

```text
The result headline says "new proof of finiteness" but the proof is a direct
specialization of a 2026 theorem.
```

Expected response:

```text
defect: headline hides relationship to state of the art
severity: MAJOR
suggested_fix: state "This is a specialization of [Author Year, exact statement]"
```
