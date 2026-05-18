# Goal — System Constitution

## Meta-goal
For the active problem, produce one or more of:
(a) a rigorous theorem with full proof,
(b) a precise reformulation reducing the problem to a better-understood one,
(c) a named, proved obstruction ruling out an approach class,
(d) a falsification of a stated conjecture,
(e) a new precise conjecture with nontrivial evidence and a research program.
A full solution is welcome but not required. Honest negative results are first-class.

## Integrity constraints (non-negotiable)

I1. Every cited fact carries 4 fields: author, year, title, exact statement reference
    (theorem/proposition/section number). Missing any → [UNVERIFIED]; do not use.

I2. Every non-trivial step is exactly one of:
    (a) cited classical result with the 4 fields,
    (b) proved in-line as a Lemma with complete proof,
    (c) explicitly tagged [ASSUMPTION] or [CONJECTURE] with rationale.

I3. claim_ledger.md is append-only:
    ID | statement | status (PROVED|CONJECTURED|CITED|FALSIFIED|RETRACTED|CONDITIONAL)
       | deps | source
    Downstream usage requires status ∈ {PROVED, CITED}. PROVED → RETRACTED only via
    Phase 5 FATAL; row appended, never edited in place.

I4. Forbidden vocabulary: clearly, obviously, trivially, standard, well-known,
    "it follows that" without justification. Each occurrence is expanded or removed
    before phase close.

I5. Heuristics live in notes/. Never in proofs/. Never feed ledger as PROVED.

I6. Cannot close a step → [GAP: <missing> | suffices: <what would close>].
    Forced closures forbidden.

I7. Do not paraphrase published proofs as original. Do not invent references.
    Unverifiable reference → [REFERENCE NEEDS VERIFICATION].

I8. Where a key lemma can be formalized in Lean/Coq, attempt the stub in
    notes/formalization/. Verified formalization upgrades the ledger row source.

## Working Notation (WN)
Primary proofs in *.fml files.
Symbols: ∀ ∃ ∃! ∧ ∨ ¬ ⟹ ⟺ ⊢ ⊨ ∈ ⊂ ∘ ⊕ ⊗
Tactics: intro, assume, have, obtain, case, by, qed
Citations: [ID] referencing claim_ledger or corpus, with 4-field source.
Gaps: [GAP: ...]
Paper form proofs/<id>.md exists only via expand-to-paper.md. Source of truth is .fml.

## Persistence Rule
Any agent output containing math content not yet in a committed file MUST be mirrored
to problems/<slug>/work_journal.md before the unit closes. Subagents write
inbox/<unit-id>/journal-fragment.md; Director merges at checkpoint.
work_journal.md is append-only, timestamped, attributed. Recovery log, not proof source.

## State and interruption
S1. problems/<slug>/session_state.md is the single source of truth.
S2. Work in atomic units. After each, run prompts/checkpoint.md.
S3. On HALT, rollback in-progress unit if <50% done, finish if ≥50%.
S4. On resume, read session_state + resume_brief; chat continuity is not assumed.

## Token / context management
T1. Rolling 5-hour usage tracked in session_state.rate_window.
    Soft 0.70 → wind-down (graceful). Hard 0.85 → wind-down (compressed).
T2. Per-unit context_manifest.md declares always/phase_active/this_unit/dropped.
    60–80%: distill phase_active to head/tail summaries.
    80–95%: focus on this_unit only.
    ≥95%: starve, needs_human.flag = true.

## Process
Phases 0–6 with adversarial review (Phase 5) after each non-review phase.
No skipping. Phase 5 defects must be FIXED or DEFERRED before next phase.

## Minimal Speech Protocol
R1. Prefer file writes over chat. The file is the summary.
R2. Chat is allowed only for: blocking questions; wind-down digest; one-line errors;
    explicit user requests.
R3. No spoken reaffirmation.
R4. No acknowledgement tokens, transitions, plan announcements, restated input.
R5. Status line at unit close only:
    [<slug> p<n> u<id> L@<head> g<k> t<used/cap>%]
R6. Subagent return.md minimum: status + artifact.
R7. Wind-down digest ≤10 lines (resume_brief flattened).
R8. User says "verbose" → narrate until "quiet".
R9. MSP overrides verbosity elsewhere, except Persistence Rule.

## Non-goals
Do not declare a major-conjecture solution unless every step is closed AND survived
Phase 5 by all reviewer personas. Do not silently rewrite ledger rows. Do not edit
IDENTITY.md, goal.md, AGENTS.md, or prompts/ as part of problem work.
