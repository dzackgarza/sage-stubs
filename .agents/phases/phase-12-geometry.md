# Phase 12 — Geometry & Polyhedra

**Tier:** 3
**Status:** ⬜ Not Started
**Depends on:** Phase 05
**Unblocks:** Phase 13

## Goal

Cover `sage.geometry/`. Existing stubs are concentrated in
`polyhedron/__init__`, `polyhedron/base`, `polyhedron/constructor`.

## Tasks

| Task | Subtree / Group | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T12.1 | **Geometry root: cones & fans** — `cone`, `cone_catalog`, `cone_critical_angles`, `fan`, `fan_isomorphism`, `fan_morphism`, `convex_set`, `relative_interior`. | 8 | — | ⬜ | |
| T12.2 | **Geometry root: lattice polytopes & integral points** — `lattice_polytope`, `linear_expression`, `newton_polygon`, `palp_normal_form`, `point_collection`, `integral_points`, `integral_points_generic_dense`, `integral_points_integer_dense`, `toric_lattice`, `toric_lattice_element`, `toric_plotter`. | ~11 | — | ⬜ | |
| T12.3 | **Geometry root: hasse, complex, voronoi, pseudolines, ribbon** — `hasse_diagram`, `polyhedral_complex`, `pseudolines`, `ribbon_graph`, `voronoi_diagram`, `abc`. | 6 | — | ⬜ | |
| T12.4 | **Polyhedron: foundations** — audit `base`, `constructor`. Add `base_QQ`, `base_RDF`, `base_ZZ`, `base_mutable`, `base_number_field`, `combinatorial_polyhedron/base`, `combinatorial_polyhedron/face_iterator`, `combinatorial_polyhedron/list_of_faces`, `combinatorial_polyhedron/conversions`, `combinatorial_polyhedron/polyhedron_face_lattice`. | ~10 | — | ⬜ | |
| T12.5 | **Polyhedron: faces & vertices** — `face`, `representation`, `parent`, `library`, `lattice_euclidean_group_element`, `palp_database`, `plot`, `cdd_file_format`, `misc`, `relative_interior`. | ~10 | T12.4 | ⬜ | |
| T12.6 | **Polyhedron: backends** — `backend_cdd`, `backend_field`, `backend_normaliz`, `backend_polymake`, `backend_ppl`, `double_description`, `double_description_inhomogeneous`, `ppl_lattice_polygon`, `ppl_lattice_polytope`. | ~9 | T12.4 | ⬜ | |
| T12.7 | **Polyhedron: residue** — remaining files from the 47 in `polyhedron/`. | ~8 | T12.4 | ⬜ | |
| T12.8 | **Hyperbolic space** — `hyperbolic_space/` subpackage (8 files). | 8 | — | ⬜ | |
| T12.9 | **Hyperplane arrangements** — `hyperplane_arrangement/` subpackage (8 files). | 8 | — | ⬜ | |
| T12.10 | **Riemannian manifolds & triangulations** — `riemannian_manifolds/` (3 files), `triangulation/` (4 files). | 7 | — | ⬜ | |

## Parallelism

- T12.1, T12.2, T12.3, T12.4, T12.8, T12.9, T12.10 mutually independent.
- T12.5, T12.6, T12.7 chain after T12.4.

## Risks

- Polyhedron backends import optional dependencies (`cdd`, `normaliz`,
  `polymake`, `ppl`). Stubs must not import those — use string forward
  references for the optional types.
- `integral_points.py` and `integral_points.pxi` interact; only the
  `.py` is in scope, but its signatures depend on Cython-only helpers.
