# Benchmark Source Metadata Verification - 2026-05-21

Purpose: require B6+ benchmark source manifests to carry the four citation
fields needed by dianoia's honesty discipline before a benchmark row can pass
local verification.

Commands:

```powershell
python -m unittest discover -s tests -p test_verify_dianoia_state.py
python tools\verify_dianoia_state.py
```

Observed targeted test output:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.337s

OK
```

Observed state verifier output:

```text
OK benchmark rows: 5 VALUE_ADDED across 5 areas
OK skills: 5 SKILL.md files
OK skill referenced: skills/arxiv-fetch/SKILL.md
OK skill referenced: skills/citation-discipline/SKILL.md
OK skill referenced: skills/coverage-systems/SKILL.md
OK skill referenced: skills/pollack-character/SKILL.md
OK skill referenced: skills/sanity-small-cases/SKILL.md
OK connector wired: connectors/arxiv
OK connector wired: connectors/oeis
OK docs/state files contain current continuous-improvement baseline
WARN B1: token accounting is UNVERIFIED
WARN B2: token accounting is UNVERIFIED
WARN B3: token accounting is UNVERIFIED
WARN B4: token accounting is UNVERIFIED
WARN B5: token accounting is UNVERIFIED
SUMMARY ok=10 warn=5 fail=0
```

Verifier behavior added:

- For B6+ rows, `benchmark-bank/B<N>/SOURCE.md` must include nonblank
  `Authors`, `Year`, `Title`, and `Exact statement reference` fields under
  `## Metadata`.
