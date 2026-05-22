# Phase 01 — Exempt module list

Produced by T01.1. Modules listed here are excluded from the
stub-coverage denominator (`scripts/stub_coverage.py` loads this file
automatically when present).

Criteria: doctest-only examples, demo/timing harnesses, deprecated
shells, Cython-only internals with no Python consumer API, and modules
with no public top-level definitions after source review.

## `structure/`

- `structure/debug_options` — Cython debug flags; no Python consumer surface
- `structure/list_clone_demo` — demo / timing harness
- `structure/list_clone_timings` — demo / timing harness
- `structure/list_clone_timings_cy` — demo / timing harness
- `structure/proof/proof` — nested proof helper; no standalone public API
- `structure/set_factories_example` — illustrative example module

## `misc/`

- `misc/allocator` — no public top-level classes/functions after source scan
- `misc/banner` — dev / tooling / re-export shell
- `misc/benchmark` — demo / timing harness
- `misc/citation` — dev / tooling / re-export shell
- `misc/classgraph` — dev / tooling / re-export shell
- `misc/compat` — dev / tooling / re-export shell
- `misc/copying` — dev / tooling / re-export shell
- `misc/dev_tools` — dev / tooling / re-export shell
- `misc/edit_module` — dev / tooling / re-export shell
- `misc/explain_pickle` — dev / tooling / re-export shell
- `misc/gperftools` — dev / tooling / re-export shell
- `misc/inline_fortran` — dev / tooling / re-export shell
- `misc/lazy_import_cache` — dev / tooling / re-export shell
- `misc/method_decorator` — dev / tooling / re-export shell
- `misc/proof` — no public top-level classes/functions after source scan
- `misc/sagedoc` — dev / tooling / re-export shell
- `misc/search` — dev / tooling / re-export shell
- `misc/superseded` — dev / tooling / re-export shell

## `categories/`

- `categories/basic` — internal category machinery or empty re-export
- `categories/category_cy_helper` — internal category machinery or empty re-export
- `categories/coercion_methods` — internal category machinery or empty re-export
- `categories/examples/algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/commutative_additive_monoids` — category doctest examples; not consumer API
- `categories/examples/commutative_additive_semigroups` — category doctest examples; not consumer API
- `categories/examples/coxeter_groups` — category doctest examples; not consumer API
- `categories/examples/crystals` — category doctest examples; not consumer API
- `categories/examples/cw_complexes` — category doctest examples; not consumer API
- `categories/examples/facade_sets` — category doctest examples; not consumer API
- `categories/examples/filtered_algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/filtered_modules_with_basis` — category doctest examples; not consumer API
- `categories/examples/finite_coxeter_groups` — category doctest examples; not consumer API
- `categories/examples/finite_dimensional_algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/finite_dimensional_lie_algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/finite_enumerated_sets` — category doctest examples; not consumer API
- `categories/examples/finite_monoids` — category doctest examples; not consumer API
- `categories/examples/finite_semigroups` — category doctest examples; not consumer API
- `categories/examples/finite_weyl_groups` — category doctest examples; not consumer API
- `categories/examples/graded_connected_hopf_algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/graded_modules_with_basis` — category doctest examples; not consumer API
- `categories/examples/graphs` — category doctest examples; not consumer API
- `categories/examples/hopf_algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/infinite_enumerated_sets` — category doctest examples; not consumer API
- `categories/examples/lie_algebras` — category doctest examples; not consumer API
- `categories/examples/lie_algebras_with_basis` — category doctest examples; not consumer API
- `categories/examples/magmas` — category doctest examples; not consumer API
- `categories/examples/manifolds` — category doctest examples; not consumer API
- `categories/examples/monoids` — category doctest examples; not consumer API
- `categories/examples/posets` — category doctest examples; not consumer API
- `categories/examples/semigroups` — category doctest examples; not consumer API
- `categories/examples/semigroups_cython` — category doctest examples; not consumer API
- `categories/examples/semirings` — category doctest examples; not consumer API
- `categories/examples/sets_cat` — category doctest examples; not consumer API
- `categories/examples/sets_with_grading` — category doctest examples; not consumer API
- `categories/examples/with_realizations` — category doctest examples; not consumer API
- `categories/primer` — no public top-level classes/functions after source scan
- `categories/tutorial` — no public top-level classes/functions after source scan

## `cpython/`

- `cpython/builtin_types` — no public top-level classes/functions after source scan
- `cpython/cython_metaclass` — Cython-only helper; public API in sibling modules
- `cpython/dict_del_by_value` — Cython-only helper; public API in sibling modules
- `cpython/string` — no public top-level classes/functions after source scan

## `data_structures/`

- `data_structures/binary_search` — no public top-level classes/functions after source scan
- `data_structures/bitset_base` — Cython/.pxd implementation; no Python module file
- `data_structures/pairing_heap` — Cython/.pxd implementation; no Python module file

## In-scope missing (not exempt)

Count: **151** modules still need `.pyi` stubs in Phase 01 scope.

- `categories/algebra_ideals`
- `categories/algebra_modules`
- `categories/aperiodic_semigroups`
- `categories/bialgebras_with_basis`
- `categories/commutative_algebra_ideals`
- `categories/complex_reflection_or_generalized_coxeter_groups`
- `categories/coxeter_group_algebras`
- `categories/filtered_modules_with_basis`
- `categories/finite_complex_reflection_groups`
- `categories/finite_dimensional_bialgebras_with_basis`
- `categories/finite_dimensional_coalgebras_with_basis`
- `categories/finite_dimensional_graded_lie_algebras_with_basis`
- `categories/finite_dimensional_lie_algebras_with_basis`
- `categories/finite_dimensional_nilpotent_lie_algebras_with_basis`
- `categories/finite_dimensional_semisimple_algebras_with_basis`
- `categories/finitely_generated_lambda_bracket_algebras`
- `categories/finitely_generated_lie_conformal_algebras`
- `categories/g_sets`
- `categories/graded_hopf_algebras`
- `categories/graded_lie_algebras`
- `categories/graded_lie_algebras_with_basis`
- `categories/graded_lie_conformal_algebras`
- `categories/graded_modules_with_basis`
- `categories/graphs`
- `categories/group_algebras`
- `categories/groupoid`
- `categories/h_trivial_semigroups`
- `categories/j_trivial_semigroups`
- `categories/kac_moody_algebras`
- `categories/kahler_algebras`
- `categories/l_trivial_semigroups`
- `categories/lie_algebras_with_basis`
- `categories/lie_conformal_algebras_with_basis`
- `categories/lie_groups`
- `categories/loop_crystals`
- `categories/manifolds`
- `categories/matrix_algebras`
- `categories/monoid_algebras`
- `categories/ore_modules`
- `categories/partially_ordered_monoids`
- `categories/permutation_groups`
- `categories/pointed_sets`
- `categories/polyhedra`
- `categories/poor_man_map`
- `categories/quantum_group_representations`
- `categories/r_trivial_semigroups`
- `categories/regular_supercrystals`
- `categories/ring_ideals`
- `categories/shephard_groups`
- `categories/simplicial_sets`
- … and 101 more (run `just coverage -- --missing --subpackage <pkg>`)
