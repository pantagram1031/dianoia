# Phase 1 - Diagnosis

Date: 2026-05-20

Evidence basis: `capability-test/VERIFY_PRIOR.md`, current prompt files, and the
prior S_a run in `C:\Users\SAMSUNG\Downloads\dianoia-run`.

## Summary

The S_a comparison degraded because the new problem statement was not routed to
`prompts/prove.md`. A stale closed active problem remained in
`problems/.active`, and the S_a work was appended to that closed problem's
`work_journal.md` instead of creating a fresh slug and entering `00-intake`.

## Root Causes

| ID | severity | root cause | file:line evidence | proposed fix | success criterion |
|----|----------|------------|--------------------|--------------|-------------------|
| R1 | BLOCKING | First-message routing has no closed-active guard before active-unit fallback. A non-command new problem can be treated as input to the active unit when `.active` exists. | `AGENTS.md:14-15` routes default new problem statements to `prompts/prove.md`; `AGENTS.md:29-30` routes otherwise to active unit and says "Never free chat." No line checks `halt_flag` before the fallback. | Constitutional change required: add a routing guard that reads `session_state.halt_flag` and `halt_reason`; if active problem is closed and incoming text is not `resume`/`halt`/utility, route to `prompts/prove.md`. Because `AGENTS.md` is constitutional, request this in `APPROVED_CHANGES.md` if prompt-only fixes cannot satisfy smoke tests. | With `.active` pointing to a fake problem whose `session_state.md` has `halt_flag: true` and `halt_reason: FAILURE-AMBITION-GAP`, a first user math statement creates a new slug and writes `intake.md`. |
| R2 | BLOCKING | `prompts/prove.md` is safe only if invoked; it has no precondition requiring stale-active detection, supersession logging, or closed-active audit when replacing `.active`. | `prompts/prove.md:7-14` validates missing `$1`, creates a slug, writes `.active`, and initializes state, but does not inspect an existing `.active` or record that a closed problem was superseded. | Add `[PRECONDITIONS]` and `[STALE ACTIVE HANDLING]` to `prompts/prove.md`: if existing `.active` points to a closed problem, do not resume it; write a supersession note to the old `work_journal.md` and continue fresh. If existing `.active` points to an open problem, require explicit `resume`/`halt` or create a new problem only for clearly new statements. | Direct invocation of `prompts/prove.md` with stale closed `.active` preserves the old closed state, creates a new slug, writes new `problem.md`, writes new `intake.md`, and updates `.active` to the new slug. |
| R3 | MAJOR | `resume.md` has correct v4 closed-problem guards, but they only fire for messages routed to `resume.md`; they do not protect arbitrary new problem statements. | `prompts/resume.md:11-13` blocks `SUCCESS-MEANINGFUL` and `FAILURE-AMBITION-GAP` and refuses non-resume-eligible `halt_flag=true`; `AGENTS.md:17-18` routes only literal `resume`/`continue` to resume. | In `prompts/resume.md`, add a cross-reference warning that it is not a new-problem router. In `prompts/prove.md`, duplicate the closed-active guard so the fix does not rely entirely on `AGENTS.md`. | A `continue` message against a closed problem still blocks, while a new theorem statement is handled by `prove.md` and not by `resume.md`. |
| R4 | MAJOR | Missing/corrupted `.active` behavior is underspecified across phase prompts. `00-intake` has a precondition but its failure section only names missing `problem.md`. | `prompts/00-intake.md:6-9` requires `.active` names exactly one slug and `problem.md` exists; `prompts/00-intake.md:27-28` only defines failure for missing `problem.md`. `prompts/resume.md:23-24` handles missing `.active` or missing state, but not malformed multi-line `.active`. | Add explicit malformed `.active` failure text to `00-intake.md` and `resume.md`; add a template invariant that `.active` must be exactly one slug matching an existing directory. | Tests covering missing `.active`, multi-line `.active`, and nonexistent slug produce deterministic BLOCKED messages instead of silently reading or appending to the wrong state. |
| R5 | MINOR | The old mastery artifacts Goodharted on internal T1-T6 success and did not require an external controlled comparison row before `MASTERY.md`. | `MASTERY.md:10` declares cycles 2-4 have zero DEGRADED/FAIL across T1-T6; `BENCHMARK.md` was absent before this session. | Keep MASTERPIECE gate separate from old mastery: require `BENCHMARK.md` rows and Phase 3 retest before any new mastery claim. | `capability-test/MASTERPIECE.md` cannot be written until `BENCHMARK.md` contains the required VALUE_ADDED rows and supporting artifacts. |

## Required Investigation Results

### AGENTS.md routing under stale `.active`

Observed behavior: stale `.active` was present and closed. The S_a problem was
not routed through `prove.md`; it landed in
`dianoia-run/problems/cycle-4-t6-perfect-numbers/work_journal.md`.

Relevant lines:
- `AGENTS.md:14-15`: default new problem statement routes to `prompts/prove.md`.
- `AGENTS.md:29-30`: otherwise routes to active unit or clarification.

Diagnosis: the routing document lacks a deterministic test for "active problem
is closed; this incoming message is a fresh problem statement."

### `prove.md` preconditions

`prompts/prove.md` has input handling and creation steps, but no explicit
precondition block. It overwrites `.active` at `prompts/prove.md:13` only after
it is invoked. It should become robust to stale closed active state so the
Phase 2 smoke test can be expressed inside the prompt contract.

### `resume.md` guard from v4 patches

The guard is mostly correct:
- `prompts/resume.md:11` blocks `SUCCESS-MEANINGFUL` and `FAILURE-AMBITION-GAP`.
- `prompts/resume.md:13` blocks `halt_flag=true` without resume eligibility.
- `prompts/resume.md:27-28` states only `BLOCKED-ITERATE` is resume-eligible.

Residual issue: this guard is bypassed when the message is not routed to
`resume.md`.

### Behavior when `halt_flag=true` `.active` exists

Current behavior is unsafe at the router boundary. `resume.md` would block, but
the prior S_a evidence shows a fresh problem statement can still be appended to
the closed problem journal.

### Behavior when `.active` is missing

For new problem statements, missing `.active` is acceptable because
`prompts/prove.md` can create it. For `resume`, `prompts/resume.md:23` blocks
with `BLOCKED: no active problem.` This is acceptable.

### Behavior when `.active` is corrupted

No prompt gives a complete malformed `.active` protocol. `00-intake` requires
exactly one slug, but the failure section does not define the block message.
`resume.md` handles missing files, but not multi-line, whitespace-only, or
path-traversal-like slug contents.

## Future Failure Modes Not Yet Observed

1. Multi-line `.active` causes one tool/read path to choose the first line while
   another treats the whole file as a slug.
2. `.active` points to a nonexistent directory; `resume.md` blocks, but a phase
   prompt could emit a misleading missing `problem.md` error.
3. `.active` points to an open `BLOCKED-ITERATE` problem, and a genuinely new
   user problem is incorrectly treated as a continuation.
4. `.active` points to a closed successful problem, and a new problem overwrites
   or pollutes its journal without supersession evidence.
5. Future benchmark runs produce raw artifacts but no git commit in the
   comparison window, making later audit weaker.
6. Reviewer D and subagent audit files exist from a stale prior problem and are
   mistakenly counted as having fired for a new benchmark.

## Phase 2 Patch Order

1. R1/R2 guard patch: prefer prompt-level fix in `prompts/prove.md`; if the
   required smoke test still depends on `AGENTS.md`, create
   `APPROVED_CHANGES.md` and halt BLOCKED_ON_USER for constitutional approval.
2. R3/R4 guard patch: clarify `resume.md` and malformed `.active` failures in
   `00-intake.md`.
3. R5 benchmark gate patch: keep old mastery separate from MASTERPIECE evidence
   in docs and trackers.
