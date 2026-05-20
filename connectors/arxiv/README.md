# arxiv connector

Purpose: bounded arXiv lookup for dianoia researcher subagents.

## Capabilities

- Search arXiv through the public Atom API.
- Search by submitted-date window and category for recent-source curation.
- Search for open-problem leads using an openness-focused query wrapper.
- Fetch a single arXiv record by identifier.
- Fall back to the arXiv abstract page when the Atom API rate-limits fetch.
- Emit compact JSON with title, authors, year, arXiv id, abstract, DOI, and
  links.

## Usage

```powershell
python connectors/arxiv/server.py search "short proofs combinatorics probability number theory II" --max-results 3
python connectors/arxiv/server.py search "induced saturation" --category math.CO --from-date 2025-11-01 --to-date 2026-05-20 --sort-by submittedDate
python connectors/arxiv/server.py openness "chromatic threshold" --category math.CO --from-date 2025-11-20 --max-results 5
python connectors/arxiv/server.py fetch 2604.06609
```

## Contract

This connector is read-only. It does not certify theorem numbers, openness, or
novelty by itself. The `openness` command is a search lead that returns
`query_meta` plus records; researcher subagents must still gather three
independent source angles, record the exact statement reference needed for
claim-ledger use, and mark missing theorem/section/openness fields as
UNVERIFIED.

Smoke evidence: `capability-test/CONNECTOR-arxiv-smoke.md`.
