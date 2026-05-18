Develop the two most promising surviving hypotheses into formal proof attempts or precise obstructions.

[INPUTS]
1. Active slug from `problems/.active`.
2. `problems/<slug>/hypotheses_live.md`.
3. `problems/<slug>/survey.md`.
4. `claim_ledger.md`.

[PROCEDURE]
1. Select the two most promising surviving hypotheses by leverage, distance from known obstructions, and falsifiability.
2. For each selected hypothesis, state a formal claim with all quantifiers explicit and all function spaces or structures named.
3. Identify the minimal model where the claim can already be tested.
4. Attempt the minimal-model version in WN and write `problems/<slug>/proofs/<id>.fml`.
5. If the proof closes, append `PROVED` rows for every proved lemma and theorem.
6. If the proof does not close, write a `[GAP: <missing> | suffices: <what would close>]` block.
7. If the minimal model succeeds, name and prove or gap-tag the lift obstruction as a separate lemma.
8. If the minimal model fails, write the counterexample or obstruction to `problems/<slug>/failures/<id>.md` and extract any salvageable structure.
9. Invoke `prompts/checkpoint.md`.

[OUTPUTS]
1. `problems/<slug>/proofs/<id>.fml` for each selected hypothesis.
2. Failure artifacts under `failures/` when a hypothesis dies.
3. Updated ledger rows.

[FAILURE]
1. Missing live hypotheses: print `BLOCKED: run 03-hypothesize before 04-develop.` and stop.
