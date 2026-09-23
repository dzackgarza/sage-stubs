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
| T05.1 | **Matrix base & spaces** — audit & complete `matrix`, `matrix2`, `matrix_space`, `constructor`, plus root files (`berlekamp_massey`, `args`, `change_ring`, `compute_J_ideal`, `docs`, `echelon_matrix`, `matrix_misc`). | ~11 | — | ✅ Done | Revalidated against the dense-backend consumers. Generic determinant and polynomial wrappers preserve concrete backend call shapes, rank remains at its actual owner, row/column scalar-extension contracts are distinct, and Smith-form transformation outputs retain same-scalar results when the native owner does. Strict type and native consumers pass. |
| T05.2 | **Matrix abstract bases** — `matrix0`, `matrix1`, `matrix_dense`, `matrix_sparse`, `matrix_generic_dense`, `matrix_generic_sparse`. | 6 | T05.1 | ✅ Done | Revalidated source ownership for inversion, integral powers, Singular conversion, dense pickle payloads, and comparison/arithmetic hooks. Generic inversion preserves the empty/non-domain result and fraction-field coefficient extension; source-defined external conversions and backend-overridable serialization are no longer constrained by unrelated ancestor types. |
| T05.3 | **Matrix integer / rational dense** — `matrix_integer_dense`, `matrix_integer_dense_hnf`, `matrix_integer_dense_saturation`, `matrix_rational_dense`, `matrix_modn_dense_float`, `matrix_modn_dense_double`, `matrix_modn_sparse`. | 7 | T05.2 | ✅ Done | Parser defects, direct-owner declarations, coefficient-changing inverses, backend call domains, echelon/Smith/decomposition/randomize contracts, and inherited method duplication are reconciled with pinned Sage. Rejected ancestor-only argument shapes are typed as non-returning where the runtime really rejects them. Strict type and complete native dense consumers pass. |
| T05.4 | **Matrix specialised dense** — `matrix_double_dense`, `matrix_double_sparse`, `matrix_real_double_dense`, `matrix_complex_double_dense`, `matrix_complex_ball_dense`, `matrix_mpolynomial_dense`, `matrix_polynomial_dense`, `matrix_laurent_mpolynomial_dense`. | 8 | T05.2 | ✅ Done | All eight specialized backends are source-grounded: the NumPy/SciPy double hierarchy, certified complex-ball matrices, and univariate, multivariate, and Laurent polynomial matrix algorithms, including exact flag-dependent normal forms, quotient/remainder operations, approximant and interpolant bases, relation and kernel bases, and Smith-preserving completion. |
| T05.5 | **Matrix specialised sparse + symbolic + GAP** — `matrix_integer_sparse`, `matrix_rational_sparse`, `matrix_symbolic_dense`, `matrix_symbolic_sparse`, `matrix_gap`, `matrix_gfpn_dense`, `matrix_mod2_dense`, `matrix_gf2e_dense`, `matrix_cyclo_dense`. | 9 | T05.2 | ✅ Done | The cyclotomic dense backend now preserves its native pickle payload, concrete arithmetic/comparison inputs, randomization and echelon call domains, characteristic-polynomial proof option, and tensor-product result. These contracts pass strict typing together with the integer/rational dense owners and the complete native dense consumer. |
| T05.6 | **Matrix windows, action, plot, special** — `matrix_window`, `action`, `matrix_misc`, `special`, `operation_table`. | 5 | T05.1 | ✅ Done | Matrix-window mutation and exact returns, coercion-model action codomains, scheme morphism and point actions, permanental-minor helpers, special-matrix constructors, and operation-table naming, polynomial matrices, and plotting contracts are source-grounded. |
| T05.7 | **Modules: free modules & elements** — `free_module`, `free_module_element`, `free_module_integer`, `free_module_homspace`, `free_module_morphism`, `free_module_pseudohomspace`, `free_module_pseudomorphism`. | 7 | — | ✅ Done | Free-module constructors, elements, integer lattices, ordinary and twisted morphisms, and PID/field submodule classes are source-grounded, including dependent construction, ambient, coordinate, ring-change, and lift/retract returns. |
| T05.8 | **Modules: quotients & finitely-generated** — `quotient_module`, `submodule`, `finite_submodule_iter`, `fg_pid` package surface (`fgp_module`, `fgp_element`, `fgp_morphism`, `fgp_congruence_module`). | ~7 | T05.7 | ✅ Done | Abstract quotient and submodule parents, finite iterators, and the actual `fg_pid` runtime package are source-grounded. The empty `fgp_congruence_module` stub was removed because no corresponding module exists at the pinned Sage revision. |
| T05.9 | **Modules: torsion & FP** — `torsion_quadratic_module`, `vector_space_morphism`, `vector_space_homspace`, `module`, `module_functors`, `with_basis/` subpackage surface (~12 files). | ~16 | T05.7 | ✅ Done | Module and quotient functors, vector-space homsets and morphisms, torsion quadratic forms, and the complete `with_basis` element, morphism, subquotient, invariant, cellular, and representation hierarchies are source-grounded. |
| T05.10 | **Modules: vector implementations** — `vector_callable_symbolic_dense`, `vector_complex_double_dense`, `vector_double_dense`, `vector_integer_dense`, `vector_modn_dense`, `vector_modn_sparse`, `vector_numpy_dense`, `vector_numpy_integer_dense`, `vector_rational_dense`, `vector_rational_sparse`, `vector_real_double_dense`, `vector_symbolic_dense`, `vector_symbolic_sparse`. | ~13 | T05.7 | ✅ Done | Concrete NumPy, RDF/CDF, integer, rational, modular, callable-symbolic, and symbolic vector constructors, arithmetic, transforms, statistics, rendering, and serialization contracts are reconciled with their direct runtime owners; C-only helper modules do not fabricate Python classes. |
| T05.11 | **Modules: misc** — `numpy_util`, `tensor_operations`, `multi_filtered_vector_space`, `filtered_vector_space`, `module_misc`, `diamond_cutting`, `misc`, `ore_module` (and any leftovers from Phase-1 audit). | ~8 | T05.7 | ✅ Done | NumPy conversion, tensor operations, filtered and multifiltered vector spaces, lattice utilities, Gram–Schmidt, and the complete Ore module/submodule/quotient hierarchy are source-grounded. The empty `module_misc` stub was removed because the pinned source contains no such module. |

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
