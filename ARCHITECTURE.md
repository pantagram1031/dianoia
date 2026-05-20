# Architecture

dianoia is a file-first mathematical investigation loop. The core object is a
problem directory under `problems/<slug>/`; the chat thread is only a launcher
and wind-down surface.

## First-Message Routing

`AGENTS.md` routes ordinary input without slash commands:

- Fresh mathematical statements go to `prompts/prove.md`.
- `resume` and `continue` go to `prompts/resume.md`.
- `halt` and `stop` go to `prompts/halt.md`.
- `muse`, `consult`, `audit`, `verbose`, and `quiet` route to their named
  prompt behaviors.

The Phase 2 fix made this routing stale-active-safe. A closed, malformed, or
missing active pointer cannot silently swallow a fresh problem statement.

## Phase Loop

`prompts/prove.md` creates a fresh slug, writes the statement, initializes
state, and then enters the sequential phase loop:

| Phase | Prompt | Purpose |
|-------|--------|---------|
| 0 | `00-intake.md` | Formal restatement, classification, success criteria, risk register |
| review | `05-review.md` | Adversarial review of the just-written phase artifact |
| 1 | `01-survey.md` | Literature terrain map and state-of-the-art citations |
| review | `05-review.md` | A/B/C review |
| 2 | `02-perspective.md` | Specialist perspectives and possible attack frames |
| review | `05-review.md` | A/B/C review |
| 3 | `03-hypothesize.md` | Generate and sanity-check live hypotheses |
| review | `05-review.md` | A/B/C/D review |
| 4 | `04-develop.md` | Proof attempts, obstructions, failures, formalization notes |
| review | `05-review.md` | A/B/C/D review |
| 6 | `06-consolidate.md` | Honest final result, formal source, summary, corpus promotion |
| review | `05-review.md` | A/B/C/D review |

After each atomic phase or review, `prompts/checkpoint.md` records state and
performs ledger/citation checks.

## Minimal Speech Protocol

The workflow is quiet by default. Phase artifacts are the deliverable; chat
output is limited to route-appropriate wind-down digests or file pointers. The
goal is to prevent persuasive narration from substituting for written evidence.

## v4 Invariants

The v4 rules prevent Goodhart-style success:

- Intake must restate the user's original target without premature weakening.
- The survey must record state-of-the-art results with four-field citations.
- Hypotheses must include direct attacks on the primary target.
- Develop must record STUCK-STATE evidence before retreating to fallbacks.
- Review persona D checks ambition at intake, hypothesize, develop, and
  consolidate.
- Consolidation must state whether the result is new, a specialization, a
  weakening, an obstruction, or not meaningful.

## Meaningfulness Gate

Before corpus promotion, a result must be meaningful in one of these ways:

- A direct attack closes with proof.
- A direct attack gets stuck at a named new obstruction or technique-class
  failure.
- The result is strictly stronger than the strongest surveyed prior result.

Equivalent or weaker re-derivations are blocked from promotion and must be
reported honestly.

## Subagent Flow

Subagents are contract files under `prompts/subagents/`. They write only to
their drop zones under `problems/<slug>/inbox/<unit-id>/...`.

- `researcher.md` verifies references and invokes arXiv/OEIS connectors.
- `surveyor.md` maps bounded literature areas.
- `sanity-checker.md` runs bounded refutation probes.
- `prover.md` proves assigned lemmas or records gaps.
- `reviewer.md` performs persona A/B/C/D adversarial review.
- `muser.md` proposes new angles after a STUCK-STATE.
- `skill-author.md` and `specialist-factory.md` create reusable process assets.

Skills in `skills/*/SKILL.md` are explicit procedures that subagents consult.
Connectors in `connectors/*/server.py` provide compact reference lookup.

## Persistent State

- `ROADMAP.md`: phase tracker.
- `DEVLOG.md`: newest-first session log and self-audit.
- `BENCHMARK.md`: controlled comparison table.
- `DECISIONS.md`: architectural decision log.
- `NEXT_SESSION.md`: resume point.
- `QUESTIONS.md`: only for BLOCKED_ON_USER halts.
