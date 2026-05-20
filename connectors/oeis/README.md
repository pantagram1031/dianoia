# oeis connector

Purpose: bounded OEIS lookup for dianoia researcher and sanity-checker
subagents.

## Capabilities

- Search OEIS through its public JSON endpoint.
- Fetch by sequence id, such as `A214583`.
- Emit compact JSON with sequence id, name, data terms, comments, references,
  links, and author lines when available.

## Usage

```powershell
python connectors/oeis/server.py fetch A214583
python connectors/oeis/server.py search "n-k^2 prime gcd(k,n)=1" --max-results 3
```

## Contract

OEIS is evidence for computational data and references, not by itself a proof
source. Subagents must not promote OEIS comments to PROVED ledger rows unless a
separate proof or complete cited theorem supports them.

Smoke evidence: `capability-test/CONNECTOR-oeis-smoke.md`.
