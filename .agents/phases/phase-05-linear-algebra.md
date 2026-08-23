# Phase 05 — Linear Algebra: Matrices & Modules

**Tier:** 1
**Status:** 🟡 In Progress
**Depends on:** Phase 01
**Unblocks:** Phase 06, 07, 08, 12, 13, 14, 15, 17

## Goal

Cover `sage.matrix/` and `sage.modules/`. These are leaf subpackages that
many higher-tier stubs lean on. Both have an existing thin stub footprint
that must be expanded.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T05.1 | **Matrix base & spaces** — audit & complete `matrix`, `matrix2`, `matrix_space`, `constructor`, plus root files (`berlekamp_massey`, `args`, `change_ring`, `compute_J_ideal`, `docs`, `echelon_matrix`, `matrix_misc`). | ~11 | — | ✅ Done | The shared matrix surface, constructor/argument contracts, matrix spaces, canonical-form dependent returns, cyclic-subspace APIs, and root helper modules are source-grounded against the pinned Sage revision. |
| T05.2 | **Matrix abstract bases** — `matrix0`, `matrix1`, `matrix_dense`, `matrix_sparse`, `matrix_generic_dense`, `matrix_generic_sparse`. | 6 | T05.1 | ✅ Done | All six abstract layers are source-grounded. `matrix0` owns common indexing, mutation, arithmetic, and structural hooks; `matrix1` owns conversion and construction surfaces; dense, sparse, and generic implementations retain their direct contracts. |
| T05.3 | **Matrix integer / rational dense** — `matrix_integer_dense`, `matrix_integer_dense_hnf`, `matrix_integer_dense_saturation`, `matrix_rational_dense`, `matrix_modn_dense_float`, `matrix_modn_dense_double`, `matrix_modn_sparse`. | 7 | T05.2 | ✅ Done | Integer and rational dense matrices, HNF and saturation helpers, and all three small-modulus backends are source-grounded, including transformation-dependent canonical forms, lattice APIs, template ownership, serialization, and LinBox rank and determinant contracts. |
| T05.4 | **Matrix specialised dense** — `matrix_double_dense`, `matrix_double_sparse`, `matrix_real_double_dense`, `matrix_complex_double_dense`, `matrix_complex_ball_dense`, `matrix_mpolynomial_dense`, `matrix_polynomial_dense`, `matrix_laurent_mpolynomial_dense`. | 8 | T05.2 | ✅ Done | All eight specialized backends are source-grounded: the NumPy/SciPy double hierarchy, certified complex-ball matrices, and univariate, multivariate, and Laurent polynomial matrix algorithms, including exact flag-dependent normal forms, quotient/remainder operations, approximant and interpolant bases, relation and kernel bases, and Smith-preserving completion. |
| T05.5 | **Matrix specialised sparse + symbolic + GAP** — `matrix_integer_sparse`, `matrix_rational_sparse`, `matrix_symbolic_dense`, `matrix_symbolic_sparse`, `matrix_gap`, `matrix_gfpn_dense`, `matrix_mod2_dense`, `matrix_gf2e_dense`, `matrix_cyclo_dense`. | 9 | T05.2 | ✅ Done | Exact sparse matrices, Maxima-backed symbolic matrices, GAP and MeatAxe wrappers, M4RI/M4RIE characteristic-two matrices, and cyclotomic multimodular algorithms are source-grounded. Direct ownership, aliases, serialization formats, algorithm literals, certificate returns, and coefficient-ring transitions were reconciled against the pinned sources. |
| T05.6 | **Matrix windows, action, plot, special** — `matrix_window`, `action`, `matrix_misc`, `special`, `operation_table`. | 5 | T05.1 | ✅ Done | Matrix-window mutation and exact returns, coercion-model action codomains, scheme morphism and point actions, permanental-minor helpers, special-matrix constructors, and operation-table naming, polynomial matrices, and plotting contracts are source-grounded. |
| T05.7 | **Modules: free modules & elements** — `free_module`, `free_module_element`, `free_module_integer`, `free_module_homspace`, `free_module_morphism`, `free_module_pseudohomspace`, `free_module_pseudomorphism`. | 7 | — | 🟡 In Progress | Vector construction and element APIs, standard-basis factories, generic parent operations, and ordinary and twisted morphism surfaces are source-grounded. PID/field submodule classes remain under direct-method and dependent-return reconciliation before task closure. |
| T05.8 | **Modules: quotients & finitely-generated** — `quotient_module`, `submodule`, `finite_submodule_iter`, `fg_pid` package surface (`fgp_module`, `fgp_element`, `fgp_morphism`, `fgp_congruence_module`). | ~7 | T05.7 | ⬜ | |
| T05.9 | **Modules: torsion & FP** — `torsion_quadratic_module`, `vector_space_morphism`, `vector_space_homspace`, `module`, `module_functors`, `with_basis/` subpackage surface (~12 files). | ~16 | T05.7 | ⬜ | `with_basis/` includes `cell_module`, `morphism`, `subquotient`, `representation`, `invariant`, `indexed_element`. |
| T05.10 | **Modules: vector implementations** — `vector_callable_symbolic_dense`, `vector_complex_double_dense`, `vector_double_dense`, `vector_integer_dense`, `vector_modn_dense`, `vector_modn_sparse`, `vector_numpy_dense`, `vector_numpy_integer_dense`, `vector_rational_dense`, `vector_rational_sparse`, `vector_real_double_dense`, `vector_symbolic_dense`, `vector_symbolic_sparse`. | ~13 | T05.7 | ⬜ | |
| T05.11 | **Modules: misc** — `numpy_util`, `tensor_operations`, `multi_filtered_vector_space`, `filtered_vector_space`, `module_misc`, `diamond_cutting`, `misc`, `ore_module` (and any leftovers from Phase-1 audit). | ~8 | T05.7 | ⬜ | |

## Parallelism

- T05.1 first. T05.2 chains on T05.1.
- Then T05.3, T05.4, T05.5, T05.6 in parallel (one per agent).
- T05.7 first within modules; T05.8, T05.9, T05.10, T05.11 in parallel
  thereafter.

## Risks

- Matrix arithmetic forwards (`__add__`, `__mul__`, `_act_on_`) MUST be
  `@overload`'d for the matrix × scalar × matrix × vector × number-field
  combinations. Do not collapse.
- `free_module.py` has dozens of constructor patterns; verify each is
  defined directly (AGENTS.md anti-inflation rule).
- `with_basis/` modules import from `combinat` — Phase 09 will *later*
  consume what we expose here, so we forward-reference `combinat` types as
  strings.
