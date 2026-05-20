# Phase Loop Verifier Smoke

Date: 2026-05-20

Commands:

```text
python -m unittest discover -s tests
python tools\verify_phase_loop.py
```

Unit test result:

```text
Ran 3 tests
OK
```

Phase-loop verifier result:

```text
OK prove.md contains the expected phase/review order
OK prove.md contains After each atomic unit
OK prove.md contains prompts/checkpoint.md
OK prove.md contains BATCHING PROHIBITED
OK 05-review.md invokes persona `A`
OK 05-review.md invokes persona `B`
OK 05-review.md invokes persona `C`
OK Reviewer D gated phases present
OK subagent contract present: researcher
OK subagent contract present: surveyor
OK subagent contract present: sanity-checker
OK subagent contract present: prover
OK subagent contract present: reviewer
OK subagent contract present: muser
OK subagent contract present: skill-author
OK subagent contract present: specialist-factory
OK checkpoint.md contains citation_check
OK checkpoint.md contains ledger_delta
SUMMARY ok=18 fail=0
```

Interpretation:

- The prompt loop still contains the expected phase/review order.
- Reviewer D remains wired for the ambition-gated phases.
- Required subagent prompt contracts exist.
- Checkpoint still exposes citation and ledger evidence fields.
