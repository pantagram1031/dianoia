# arxiv connector example

Command:

```powershell
python connectors/arxiv/server.py fetch 2604.06609
```

Expected use by researcher subagent:

1. Fetch metadata for `2604.06609`.
2. Copy title, authors, year, arXiv id, DOI if present, and abstract summary
   into the subagent drop zone.
3. If the proof needs Theorem 6.1 specifically, inspect the paper text or PDF
   separately and record the exact theorem reference. The connector metadata
   alone is not sufficient for a ledger `CITED` row that depends on a theorem.

Observed smoke output may include `"source": "arxiv_abs_fallback"` if the Atom
API rate-limits.
