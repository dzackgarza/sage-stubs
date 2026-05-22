# Phase 15 — Topology, Manifolds, Graphs, Homology

**Tier:** 3
**Status:** ⬜ Not Started
**Depends on:** Phase 05
**Unblocks:** Phase 17 (parts)

## Goal

Cover `sage.topology/`, `sage.manifolds/`, `sage.graphs/`, `sage.homology/`.
Existing stubs are thin (3+4+6+0 respectively).

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T15.1 | **Topology root** — audit existing `cubical_complex`, `simplicial_complex`. Add `cell_complex`, `delta_complex`, `filtered_simplicial_complex`, `moment_angle_complex`, `simplicial_complex_catalog`, `simplicial_complex_homology_basis_repn`, `simplicial_complex_homset`, `simplicial_complex_morphism`, `simplicial_set`, `simplicial_set_catalog`, `simplicial_set_constructions`, `simplicial_set_examples`, `simplicial_set_morphism`. | ~15 | — | ⬜ | |
| T15.2 | **Homology** — `chain_complex`, `chain_complex_morphism`, `koszul_complex`, `algebraic_topological_model`, `chains`, `hochschild_complex`, `homology_group`, `homology_morphism`, `homology_vector_space_with_basis`, `koszul`, `matrix_utils`, `simplicial_set_construction`, `simplicial_set_examples`, `tests`, `chain_homotopy`. | ~15 | — | ⬜ | |
| T15.3 | **Manifolds root** — audit existing `manifold`, `chart`, `scalarfield`. Add `manifold_homset`, `point`, `subset`, `subset_pullback`, `topological_submanifold`, `vector_bundle`, `vector_bundle_fiber`, `vector_bundle_fiber_element`, `local_frame`, `section`, `section_module`. | ~12 | — | ⬜ | |
| T15.4 | **Manifolds subsets** — `subsets/` subpackage (3 files). | 3 | T15.3 | ⬜ | |
| T15.5 | **Manifolds differentiable: foundations** — `differentiable/` subpackage core (~12 of 47): `affine_connection`, `automorphismfield`, `automorphismfield_group`, `bundle_connection`, `chart`, `curve`, `de_rham_cohomology`, `degenerate`, `degenerate_submanifold`, `diff_form`, `diff_form_module`, `diff_map`. | ~12 | T15.3 | ⬜ | |
| T15.6 | **Manifolds differentiable: tensor & metric** — `metric`, `pseudo_riemannian`, `pseudo_riemannian_submanifold`, `tensorfield`, `tensorfield_module`, `tensorfield_paral`, `mixed_form`, `mixed_form_algebra`, `multivectorfield`, `multivector_module`, `examples/`. | ~12 | T15.5 | ⬜ | |
| T15.7 | **Manifolds differentiable: maps & integration** — `diff_form_paral`, `integrated_curve`, `levi_civita_connection`, `manifold`, `manifold_homset`, `scalarfield`, `scalarfield_algebra`, `symplectic_form`, `symplectic_form_test`, `vectorfield`, `vectorfield_module`. | ~11 | T15.5 | ⬜ | |
| T15.8 | **Manifolds differentiable: residue** — remaining `differentiable/` files (47 total). | ~12 | T15.5 | ⬜ | |
| T15.9 | **Graphs root: foundations** — audit existing `bipartite_graph`, `digraph`, `generic_graph`, `graph`, `graph_generators`. Add `cycle_enumeration`, `domination`, `digraph_generators`, `graph_input`, `graph_latex`, `graph_list`, `graph_plot`, `graph_plot_js`, `graph_editor`, `dot2tex_utils`, `hypergraph_generators`, `isgci`, `line_graph`, `lovasz_theta`, `matching`, `matching_covered_graph`, `morphisms`, `orientations`, `partial_cube`, `pq_trees`, `print_graphs`, `schnyder`. | ~22 | — | ⬜ | Largest task in phase — split into two commits if it crosses 25 files. |
| T15.10 | **Graphs root: Cython algorithms** — `asteroidal_triples`, `bliss`, `centrality`, `chrompoly`, `cliquer`, `comparability`, `connectivity`, `convexity_properties`, `distances_all_pairs`, `edge_connectivity`, `genus`, `graph_coloring`, `graph_generators_pyx`, `hyperbolicity`, `independent_sets`, `isoperimetric_inequalities`, `matchpoly`, `mcqd`, `path_enumeration`, `planarity`, `spanning_tree`, `strongly_regular_db`, `traversals`, `tutte_polynomial`, `views`, `weakly_chordal`. | ~26 | — | ⬜ | Split into two commits along (a) core algorithms, (b) views/decomp. |
| T15.11 | **Graphs base & decompositions** — `base/` (10 files), `graph_decompositions/` (12 files). | ~22 | — | ⬜ | Split into two commits. |
| T15.12 | **Graphs generators & misc** — `generators/` subpackage (14 files): `basic`, `chessboard`, `classical_geometries`, `degree_sequence`, `distance_regular`, `families`, `intersection`, `luw_graphs`, `platonic_solids`, `random`, `smallgraphs`, `trees`, `world_map`. Plus root `graph_database`, `cographs`. | ~16 | — | ⬜ | |

## Bootstrap with stubgen

Topology and manifolds are pure-Python and scaffold cleanly with
`python3 -m mypy.stubgen -p sage.topology -o /tmp/stubgen` /
`-p sage.manifolds`. Graphs Cython modules need `--inspect-mode` (or fall
back to manual source-reading when stubgen errors). See
[feature.md](../feature.md#tooling-auto-scaffolding-from-source).

## Parallelism

- All four subtrees (topology, homology, manifolds, graphs) are mutually
  independent — assign one per agent.
- Within manifolds: T15.3 → T15.4 / T15.5 → T15.6, T15.7, T15.8.
- Within graphs: T15.9, T15.10, T15.11, T15.12 all independent.

## Risks

- `simplicial_complex.py` has many helper methods that look direct but
  are inherited from `CellComplex`. Use the AST `cls.body` check.
- Manifolds differentiable code has heavy `__init__` keyword-only
  signatures — capture each `*, frame_name=None, ...` precisely.
- Graph Cython modules export functions, not classes — be careful with
  the `def` vs `class` distinction in the stub.
