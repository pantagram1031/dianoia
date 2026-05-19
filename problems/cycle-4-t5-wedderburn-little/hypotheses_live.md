# Hypotheses Live

## H1 Direct Attack
For every finite division ring D, D is commutative.
Route: use the center F, maximal subfields K/F, cyclicity of K^*, centralizer control for noncentral elements, and conjugation/normalizer counts.
Refutation condition: the class-equation route cannot force D=K without a justified divisibility contradiction for the remaining normalizer action.
Sanity check: all finite subfields are finite fields; multiplicative groups of subfields are cyclic; cycle 2's centralizer/intersection obstruction is attacked directly.
Status: survives but blocked at a sharper obstruction.

## Progress from cycle 2 obstruction
The centralizer/intersection line now isolates a tractable condition: if a noncentral element x generates a maximal subfield K over F, then C_D(x)=K and distinct conjugates of K cannot share x. This controls the no-double-counting shape enough to reduce the proof to a normalizer quotient/divisibility contradiction.

## New obstruction
Need to prove the normalizer quotient action yields an integer divisibility contradiction between |D^*|, |K^*|, |F^*|, and the automorphism group of K/F. The current artifact has not closed the cyclotomic/divisibility step without citing a standard Wedderburn proof package.