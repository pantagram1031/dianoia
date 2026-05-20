# Connector Smoke - arxiv

Date: 2026-05-20

Command:

```powershell
python connectors/arxiv/server.py fetch 2604.06609
```

Result: PASS.

The arXiv Atom API returned HTTP 429 during the first attempt, so the connector
used its `arxiv_abs_fallback` path and emitted compact JSON.

Key output fields:

```json
{
  "arxiv_id": "2604.06609",
  "title": "Short proofs in combinatorics, probability and number theory II",
  "authors": [
    "Alexeev, Boris",
    "Putterman, Moe",
    "Sawhney, Mehtaab",
    "Sellke, Mark",
    "Valiant, Gregory"
  ],
  "year": "2026",
  "published": "2026/04/08",
  "source": "arxiv_abs_fallback"
}
```

Connector status: working for metadata fetch of the S_a source.
