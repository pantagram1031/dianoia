# Benchmark Run Workspace Path Verification - 2026-05-21

Purpose: require B6+ run manifests to identify existing raw and dianoia
workspace paths, not just prose descriptions of the run.

Commands:

```powershell
python -m unittest discover -s tests -p test_verify_dianoia_state.py
python tools\verify_dianoia_state.py
```

Observed targeted test output:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 1.321s

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

- For B6+ rows, `RUN.md` `## Raw Workspace` and `## Dianoia Workspace`
  sections must contain nonblank `Path:` values.
- Each workspace path must exist. Relative paths are resolved from the repo
  root; absolute paths are checked directly.
