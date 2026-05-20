# arxiv connector

Purpose: bounded arXiv lookup for dianoia researcher subagents.

## Capabilities

- Search arXiv through the public Atom API.
- Fetch a single arXiv record by identifier.
- Fall back to the arXiv abstract page when the Atom API rate-limits fetch.
- Emit compact JSON with title, authors, year, arXiv id, abstract, DOI, and
  links.

## Usage

```powershell
python connectors/arxiv/server.py search "short proofs combinatorics probability number theory II" --max-results 3
python connectors/arxiv/server.py fetch 2604.06609
```

## Contract

This connector is read-only. It does not certify theorem numbers by itself.
Researcher subagents must still record the exact statement reference needed for
claim-ledger use, and must mark missing theorem/section references as
UNVERIFIED.

Smoke evidence: `capability-test/CONNECTOR-arxiv-smoke.md`.
