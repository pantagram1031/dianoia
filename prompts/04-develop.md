Develop the two most promising surviving hypotheses into formal proof attempts or precise obstructions.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/hypotheses_live.md`.
3. `problems/<slug>/survey.md`.
4. `claim_ledger.md`.

[PRECONDITIONS]
1. Phase 3 hypothesize has completed.
2. `problems/<slug>/hypotheses_live.md` exists and records surviving hypotheses plus sanity-check evidence.
3. `problems/<slug>/survey.md` and `claim_ledger.md` exist for allowed dependencies.

[PROCEDURE]
1. Select the two most promising surviving hypotheses by leverage, distance from known obstructions, and falsifiability.
2. For each selected hypothesis, state a formal claim with all quantifiers explicit and all function spaces or structures named.
3. Identify the minimal model where the claim can already be tested.
4. For each separable lemma whose proof would unblock the selected hypothesis, create a `templates/subproof_request.md`-shaped request and invoke `prompts/subagents/prover.md`.
5. Merge prover returns only after checking their allowed dependencies and gaps.
6. Attempt the minimal-model version in WN and write `problems/<slug>/proofs/<id>.fml`.
7. If the proof closes, append `PROVED` rows for every proved lemma and theorem.
8. If the proof does not close, write a `[GAP: <missing> | suffices: <what would close>]` block.
9. If the direct attack is stuck, invoke `prompts/subagents/muser.md` with the STUCK-STATE and require at least one new technique, specialist, or literature angle for the NEXT-SESSION ATTACK PLAN.
10. If the minimal model succeeds, name and prove or gap-tag the lift obstruction as a separate lemma.
11. If the minimal model fails, write the counterexample or obstruction to `problems/<slug>/failures/<id>.md` and extract any salvageable structure.
12. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/proofs/<id>.fml` for each selected hypothesis.
2. Failure artifacts under `failures/` when a hypothesis dies.
3. Prover return artifacts under `problems/<slug>/inbox/<unit-id>/prover/` when lemmas are delegated.
4. Muser return artifacts when the direct attack reaches STUCK-STATE.
5. Updated ledger rows.

[FAILURE]
1. Missing live hypotheses: print `BLOCKED: run 03-hypothesize before 04-develop.` and stop.

INVARIANTS (v4 persistence on stuck):
- A direct-attack hypothesis that does not close in Phase 4 must NOT be silently replaced with a fallback. Record a work_journal.md entry "STUCK-STATE: <precise blocker>" and a "NEXT-SESSION ATTACK PLAN: <refined approach naming new technique, specialist, or literature angle>".
- A run that produces only fallback (conditional/reformulation/obstruction/conjecture) results without recording at least one STUCK-STATE entry for the direct attack is a fatal defect at Phase 4.
- Phase 4 may end in three states: (a) direct attack closed with proof, (b) direct attack stuck with STUCK-STATE recorded plus optional fallback partial results, (c) all live hypotheses closed as obstructions ruling out the primary target. State (b) is normal and not a failure; it triggers BLOCKED-ITERATE at halt.
