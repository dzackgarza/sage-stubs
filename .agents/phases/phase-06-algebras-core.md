# Phase 06 — Algebras: Associative & Non-Lie

**Tier:** 2
**Status:** ⬜ Not Started
**Depends on:** Phase 02, Phase 05
**Unblocks:** Phase 10 (heavily)

## Goal

Cover `sage.algebras/` except the Lie / Lie-conformal / quantum-group
subtrees (those move to Phase 07). Includes Clifford, exterior, Hecke,
group, free, polynomial-like algebras, fusion rings, Steenrod, Iwahori,
quaternions, etc.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T06.1 | **Clifford & exterior** — audit & complete `clifford_algebra`, `clifford_algebra_element`, `exterior_algebra_groebner`. | 3 | — | ⬜ | All have existing stubs — extend. |
| T06.2 | **Free algebras & quotients** — `free_algebra`, `free_algebra_element`, `free_algebra_quotient`, `free_algebra_quotient_element`, `free_zinbiel_algebra`, `letterplace/` subpackage (~4 files). | ~8 | — | ⬜ | `free_algebra` and `free_algebra_element` have existing stubs. |
| T06.3 | **Group, Iwahori-Hecke, Hecke-algebras** — `group_algebra`, `iwahori_hecke_algebra`, `nil_coxeter_algebra`, `yokonuma_hecke_algebra`, `hecke_algebras/` subpackage (~6 files). | ~10 | — | ⬜ | Three root files have existing stubs. |
| T06.4 | **Polynomial-like algebras** — `askey_wilson`, `q_commuting_polynomials`, `q_system`, `partition_shifting_algebras`, `splitting_algebra`, `cellular_basis`, `shuffle_algebra`. | ~7 | — | ⬜ | |
| T06.5 | **Combinatorial algebras** — `affine_nil_temperley_lieb`, `blob_algebra`, `descent_algebra`, `diagram_algebras`, `partition_algebra`, `schur_algebra`, `symmetric_group_algebra` (this lives under groups), `nil_coxeter_algebra`. | ~7 | — | ⬜ | `symmetric_group_algebra` cross-references Phase 08 — forward-ref. |
| T06.6 | **Quantum (non-Lie) and Yangian** — `quantum_clifford`, `quantum_oscillator`, `quantum_matrix_coordinate_algebra`, `yangian`, `rational_cherednik_algebra`, `down_up_algebra`, `weyl_algebra`. | 7 | — | ⬜ | |
| T06.7 | **Fusion rings** — `fusion_rings/` subdir (8 files). | 8 | — | ⬜ | |
| T06.8 | **Cluster, associated, commutative DGA, finite GCA** — `cluster_algebra`, `associated_graded`, `commutative_dga`, `finite_gca`, `orlik_solomon`, `orlik_terao`, `tensor_algebra`, `hall_algebra`. | 8 | — | ⬜ | |
| T06.9 | **Quaternion algebras** — `quaternion_algebra`, `quaternion_algebra_element`, `quatalg/` subpackage (4 files), `octonion_algebra`. | ~7 | — | ⬜ | `quatalg/quaternion_algebra` has existing stub. |
| T06.10 | **Jordan & Steenrod** — `jordan_algebra`, `steenrod/` subdir (5 files). | 6 | — | ⬜ | `steenrod_algebra` has existing stub. |
| T06.11 | **Finite-dimensional algebras subpackage** — `finite_dimensional_algebras/` (5 files). | 5 | — | ⬜ | |
| T06.12 | **Catalogs & root** — `catalog`, plus any algebras-root leftovers from Phase-1 audit. | ~3 | T06.1–T06.11 | ⬜ | |

## Parallelism

- T06.1–T06.11 are all independent — assign one per agent.
- T06.12 last.

## Risks

- `weyl_algebra.py` and `clifford_algebra.py` have arithmetic with
  polynomial / exterior bases; signatures must use `@overload`.
- `letterplace/` has both Python and Cython surface; some `.pyx` files
  may not export Python classes — confirm in the Phase-1 audit.
