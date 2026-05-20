# arxiv-fetch

description: Use arXiv metadata and abstract-page fetching when a benchmark,
claim, or literature survey depends on an arXiv paper, arXiv id, or source
whose exact statement reference must be verified before use.

## When To Use

- A task mentions an arXiv id, arXiv URL, or paper title likely hosted on arXiv.
- A benchmark source needs the four citation fields: author, year, title, and
  exact statement reference.
- A subagent must distinguish metadata/abstract evidence from a verified
  theorem, proposition, lemma, section, or page reference.
- The arXiv Atom API rate-limits and the fallback abstract page must be used
  without pretending it proves more than it does.

## When Not To Use

- The source is a journal-only paper with no arXiv copy and no arXiv id.
- The task needs proof content that is absent from metadata and abstract text.
- The claim requires the latest paper version but the connector output does not
  show enough version information to decide that safely.
- A complete local PDF/source excerpt has already been verified and cited.

## Procedure

1. Normalize the input into either an arXiv id such as `2604.06609` or an arXiv
   abstract URL.
2. Invoke `connectors/arxiv/server.py fetch <id-or-url>` from the repo root and
   save the compact result in the subagent drop zone.
3. Extract author, year, title, arXiv id, version/date when present, and abstract
   summary.
4. Separately verify the exact statement reference. Metadata can identify a
   paper, but it cannot by itself certify "Theorem 2.1" unless the abstract or a
   fetched source explicitly names that statement.
5. If the connector falls back from Atom to the abstract page, record the
   fallback in the artifact and mark missing version/theorem fields as
   `UNVERIFIED`.
6. Use arXiv metadata as citation support only after all four citation fields
   are present. Use it as search lead otherwise.
7. For benchmark-bank sources, copy the citation fields and modification note
   into `benchmark-bank/B<N>/SOURCE.md`.

## Examples

Example trigger:

```text
Use arXiv:2604.06609 as the source for a number-theory benchmark.
```

Expected use:

```text
python connectors/arxiv/server.py fetch 2604.06609
```

Then record:

```text
authors: Boris Alexeev; Moe Putterman; Mehtaab Sawhney; Mark Sellke; Gregory Valiant
year: 2026
title: Short proofs in combinatorics, probability and number theory II
exact_statement_reference: Section 6 Theorem 6.1
```

Example non-use:

```text
The PDF has already been checked and the task is to verify a local algebraic
calculation inside Lemma 4.
```

Reason not to use:

```text
The arXiv connector is useful for source identity, not for replacing local
proof verification once the exact source is already in hand.
```
