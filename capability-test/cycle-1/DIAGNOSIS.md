# Cycle 1 Diagnosis

## Gap 1: Reviewer pressure can be vacuous

- Dimension capped: D2 Verifying (score 3).
- Evidence: T1-T6 reviewer files all exist, but many are empty `defects: []` pass shells. The current source allows a review to pass without documenting what adversarial search was attempted.
- Files: `prompts/subagents/reviewer.md`, `prompts/05-review.md`.
- Missing invariant: every reviewer persona must record its attempted adversarial checks, including at least one concrete attack/search trace, even when no defect survives.
- Proposed fix: add a required `attempted_attacks` section to reviewer output; require A to include a counterexample search, B a citation/duplication check, C a definition/quantifier trace, D answers with evidence paths; make missing attempted_attacks itself a review defect.

## Gap 2: Proof compression hides gaps

- Dimension capped: D1 Proving (score 3).
- Evidence: T3 and T4 proof artifacts compress substantial textbook transitions into single WN lines, while T5 demonstrates that the system can identify a real lemma gap only when the gap is obvious.
- File: `prompts/04-develop.md`.
- Missing invariant: any nontrivial proof transition must be decomposed into named lemmas or explicitly marked `[GAP]`; imported classical results need exact ledger/corpus references and cannot cover the theorem being proved.
- Proposed fix: add a proof granularity gate requiring lemma extraction for every compressed transition and a self-citation/circularity check before a proof can close.

## Gap 3: Context/checkpoint evidence is skeletal

- Dimension capped: D7 Organizing materials (score 3).
- Evidence: Cycle artifacts include `context_manifest.md`, but the manifest can be a minimal placeholder and does not prove separate phase execution or phase-specific inputs/outputs.
- Files: `prompts/checkpoint.md`, `templates/context_manifest.md`.
- Missing invariant: every checkpoint manifest must include phase prompt, artifact path, review status when applicable, ledger delta, journal fragment sources, and dropped-context recovery pointers.
- Proposed fix: strengthen checkpoint/context manifest requirements and template fields so skeletal manifests are invalid.
