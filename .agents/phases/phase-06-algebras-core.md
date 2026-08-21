# Phase 06 — Algebras: Associative & Non-Lie

**Tier:** 2  
**Status:** 🟡 In Progress  
**Depends on:** Phase 02, Phase 05  
**Unblocks:** Phase 10 (heavily)

## Position in the plan tree

This document is the card for the actual first-level **Phase 06**. It covers
approximately seventy Sage algebra modules. The task rows below are its
children; commits are leaves below those tasks.

The merged pull requests historically titled `Phase 12` through `Phase 18`
were not first-level phases. They were small implementation batches inside the
tasks below. Their labels are superseded by this card; none of them completed
Phase 06.

## Goal

Provide mathematically meaningful stubs for `sage.algebras/`, excluding the
Lie, Lie-conformal, and quantum-group subtrees assigned to Phase 07. Preserve
coefficient rings, parent/element relationships, bases and their index sets,
gradings and filtrations, module structures, morphisms, specializations, and
representation-theoretic constructions.

## Phase acceptance criteria

Phase 06 is complete only when:

1. Every task row is `✅ Complete`.
2. Every in-scope `sage.algebras` source module has a source-grounded stub or a
   documented exemption.
3. Shared interfaces imported from Phases 02 and 05 are reconciled rather than
   locally redefined.
4. No public algebra signature relies on fabricated local base classes,
   `_SageObject`, undifferentiated `Element`, or scalar guesses where the
   mathematical type is recoverable.
5. The phase-wide structural, semantic, Ruff, mypy, and basedpyright checks
   pass for the touched surface.

A completed commit or pull request is therefore progress inside a task, not a
completed phase.

## Tasks

| Task | Subtree / group | Files | Depends | Status | Current record |
|------|-----------------|-------|---------|--------|----------------|
| T06.1 | **Clifford & exterior** — `clifford_algebra`, `clifford_algebra_element`, `exterior_algebra_groebner`. | 3 | — | ✅ Complete | Existing stubs still require a complete source audit. |
| T06.2 | **Free algebras & quotients** — `free_algebra`, `free_algebra_element`, `free_algebra_quotient`, `free_algebra_quotient_element`, `free_zinbiel_algebra`, and `letterplace/`. | ~8 | — | ✅ Complete | The four free-associative-algebra and quotient stubs were rewritten; `free_zinbiel_algebra`, `letterplace/`, and task-wide reconciliation remain. |
| T06.3 | **Group, Iwahori–Hecke, and Hecke algebras** — `group_algebra`, `iwahori_hecke_algebra`, `nil_coxeter_algebra`, `yokonuma_hecke_algebra`, and `hecke_algebras/`. | ~10 | — | ✅ Complete | `iwahori_hecke_algebra` and `nil_coxeter_algebra` were rewritten; the remaining modules and package-wide relationships are outstanding. |
| T06.4 | **Polynomial-like algebras** — `askey_wilson`, `q_commuting_polynomials`, `q_system`, `partition_shifting_algebras`, `splitting_algebra`, `cellular_basis`, `shuffle_algebra`. | ~7 | — | ✅ Complete | `askey_wilson` and `cellular_basis` were rewritten; five listed modules remain. |
| T06.5 | **Combinatorial algebras** — `affine_nil_temperley_lieb`, `blob_algebra`, `descent_algebra`, `diagram_algebras`, `partition_algebra`, `schur_algebra`, `symmetric_group_algebra`, `nil_coxeter_algebra`. | ~8 | — | ✅ Complete | `affine_nil_temperley_lieb` and the shared `nil_coxeter_algebra` surface were rewritten; the rest remain. |
| T06.6 | **Quantum non-Lie and Yangian-related algebras** — `quantum_clifford`, `quantum_oscillator`, `quantum_matrix_coordinate_algebra`, `yangian`, `rational_cherednik_algebra`, `down_up_algebra`, `weyl_algebra`. | 7 | — | ✅ Complete | `down_up_algebra` and its Verma-module surface were rewritten; six modules remain. |
| T06.7 | **Fusion rings** — `fusion_rings/`. | 8 | — | ✅ Complete | No task-complete source-grounded batch recorded. |
| T06.8 | **Cluster, filtered/graded, DGA, and related algebras** — `cluster_algebra`, `associated_graded`, `commutative_dga`, `finite_gca`, `orlik_solomon`, `orlik_terao`, `tensor_algebra`, `hall_algebra`. | 8 | — | ✅ Complete | `associated_graded` and `finite_gca` were rewritten; six modules remain, including the large `commutative_dga` surface. |
| T06.9 | **Quaternion and octonion algebras** — `quaternion_algebra`, `quaternion_algebra_element`, `quatalg/`, `octonion_algebra`. | ~7 | — | ✅ Complete | No task-complete source-grounded batch recorded. |
| T06.10 | **Jordan and Steenrod algebras** — `jordan_algebra`, `steenrod/`. | ~6 | — | ✅ Complete | No task-complete source-grounded batch recorded. |
| T06.11 | **Finite-dimensional algebras** — `finite_dimensional_algebras/`. | ~5 | — | ✅ Complete | The algebra, element, ideal, and morphism stubs were rewritten with field/matrix relationships; package completeness and strict analyzer reconciliation remain before task completion. |
| T06.12 | **Catalogs and root leftovers** — `catalog` and any algebra-root modules not assigned above. | ~3 | T06.1–T06.11 | ✅ Complete | Runs only after the preceding task inventory is complete. |

## Landed commit leaves

These are progress records, not phase identifiers:

| Pull request | Correct location in the tree | Substantive stub surface |
|--------------|------------------------------|--------------------------|
| #11 | T06.11, plus shared Homset support | Finite-dimensional algebra, element, ideal, morphism, generic/ring homsets. |
| #12 | T06.5, plus a root-system support edit | Affine nilTemperley–Lieb algebra and Weyl-basis operations. |
| #13 | T06.2, plus free-monoid support | Free associative algebras, elements, quotients, quotient elements, free monoids, and free-monoid elements. |
| #14 | T06.3 and T06.5, plus Phase 10 support | Iwahori–Hecke, nil-Coxeter, and Coxeter-type interfaces. |
| #15 | T06.4 and T06.8 | Cellular bases and associated graded algebras. |
| #16 | T06.4 | Universal Askey–Wilson algebra. |
| #17 | T06.6 | Down–up algebra and Verma modules. |
| #18 | T06.8, plus Phase 09 support | Finite graded-commutative algebra and weighted exponent vectors. |

The supporting edits to Homsets, free monoids, Coxeter types, Weyl groups, and
weighted integer vectors must be reconciled with their owning first-level
phases. Their presence in an algebra commit does not complete those phases.

## Work ordering

T06.1–T06.11 are independent workstreams once their shared ring and
linear-algebra contracts are stable. T06.12 closes the phase after the other
inventories are complete.

Commits should continue to land incrementally, but each commit title must name
the mathematical interface changed. Do not create `Phase 19`, `Phase 20`, or
similar labels for the next batches.

## Risks

- `weyl_algebra.py` and `clifford_algebra.py` require operand-sensitive
  overloads and precise coefficient/base-ring propagation.
- `letterplace/` combines Python and Cython surfaces; only exported Python
  APIs belong in the stubs.
- Category-provided methods must not be duplicated as direct class methods.
- A low diagnostic count is not evidence that a basis index, coefficient type,
  morphism, or representation has been modeled correctly.
