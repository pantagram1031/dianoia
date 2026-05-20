# B2 Source

## Metadata

- Authors: Yuhang Bai; Kristof Berczi
- Year: 2026
- Title: "Above-Guarantee Algorithm for Properly Colored Spanning Trees"
- Exact statement reference: arXiv:2604.11326v1, Section 4.2, Theorem 4.11

## Source

arXiv:2604.11326, DOI-style URL: `https://arxiv.org/abs/2604.11326`.

## Modification

The benchmark asks whether the paper proves the unconditional statement that
every connected edge-colored graph `G` contains a properly colored tree of order
at least `min{|V(G)|, 2 delta^c(G)+1}`.

This is a controlled modification of the paper's above-guarantee theorem: it
removes the paper's condition "if one exists" / "whenever such a tree exists" to
test whether the system catches the overclaim.

## Area

combinatorics

## Artifacts

- Raw baseline: `C:\Users\SAMSUNG\Downloads\raw-attempt-3`
- Dianoia run: `C:\Users\SAMSUNG\Downloads\dianoia-run\problems\b2-properly-colored-spanning-trees`
- Source checks: arXiv abstract page and HTML version for Theorem 4.11.
