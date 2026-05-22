# Phase 07 — Lie Algebras & Quantum Groups

**Tier:** 2
**Status:** ⬜ Not Started
**Depends on:** Phase 02, Phase 05
**Unblocks:** Phase 10 (parts)

## Goal

Cover `sage.algebras.lie_algebras/`, `sage.algebras.lie_conformal_algebras/`,
and `sage.algebras.quantum_groups/`. These subtrees are interlinked but
independent of the rest of `algebras/`, so they get their own phase to
parallelise with Phase 06.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T07.1 | **Lie algebras: base** — `lie_algebra`, `lie_algebra_element`, `structure_coefficients`, `subalgebra`, `quotient`, `morphism`, `representation`. | ~7 | — | ⬜ | `lie_algebra` has existing stub. |
| T07.2 | **Lie algebras: classical** — `classical_lie_algebra`, `affine_lie_algebra`, `heisenberg`, `nilpotent_lie_algebra`, `rank_two_heisenberg_virasoro`, `virasoro`, `onsager`, `verma_module`. | ~8 | T07.1 | ⬜ | |
| T07.3 | **Lie algebras: free / poincare / examples** — `free_lie_algebra`, `poincare_birkhoff_witt`, `examples`, `bch`, `bgg_dual_module`, `bgg_resolution`. | ~6 | T07.1 | ⬜ | |
| T07.4 | **Lie algebras: cartan / category** — `cartan_type`, `cartan_matrix`, `lie_algebra_category`, `centre_uea`, plus any remaining lie_algebras leaves. | ~4 | T07.1 | ⬜ | |
| T07.5 | **Lie conformal algebras: base** — `lie_conformal_algebra`, `lie_conformal_algebra_element`, `lie_conformal_algebra_with_basis`, `lie_conformal_algebra_with_generators`, `finitely_freely_generated_lie_conformal_algebra`. | 5 | — | ⬜ | |
| T07.6 | **Lie conformal algebras: specific** — `affine_lie_conformal_algebra`, `bosonic_ghosts_lie_conformal_algebra`, `fermionic_ghosts_lie_conformal_algebra`, `free_bosons_lie_conformal_algebra`, `free_fermions_lie_conformal_algebra`, `virasoro_lie_conformal_algebra`, `neveu_schwarz_lie_conformal_algebra`, `n2_lie_conformal_algebra`, `weyl_lie_conformal_algebra`, `abelian_lie_conformal_algebra`, `examples_lie_conformal_algebras`, `lie_conformal_algebra_with_structure_coefs`, `graded_lie_conformal_algebra`, `lie_conformal_algebra_basis`. | ~14 | T07.5 | ⬜ | |
| T07.7 | **Quantum groups** — `quantum_groups/` subdir (6 files). | 6 | — | ⬜ | |

## Parallelism

- T07.1 first. Then T07.2, T07.3, T07.4 in parallel.
- T07.5 → T07.6.
- T07.7 independent of all others.

## Risks

- Lie conformal algebras have abstract method tables; `abstract_method`
  decorators must be represented as the existing `AbstractMethod`
  type, not as plain functions.
- `verma_module` and `bgg_resolution` import from `combinat.root_system`
  — forward-reference until Phase 10 lands.
