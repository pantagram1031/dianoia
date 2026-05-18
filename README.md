# dianoia

Plato's word for the cognitive mode of mathematicians (Republic VI, 511d): the
discursive reasoning from hypotheses down to conclusions. This repo is dianoia
made operational — a Codex CLI workflow that attempts open mathematical problems
with rigor, append-only ledgers, phase-gated adversarial self-review, and
specialist personas.

## What this is
- A set of prompts, templates, and conventions for Codex CLI.
- Not a library. Not an autonomous agent. A workflow.

## What this is not
- A solver. It does not promise solutions.
- A chatbot. Outputs are mathematics.

## Quick start
1. Clone.
2. `cd dianoia && codex`
3. Type your problem. Example: `prove the riemann hypothesis`
4. Stop with `halt`. Continue with `resume`.

## Output discipline
- Every claim lives in `problems/<slug>/claim_ledger.md` (append-only).
- Every phase closes with adversarial review (Phase 5).
- All recovery state on disk; no chat-memory dependence.
- Minimal Speech Protocol: silent by default.

## License
MIT
