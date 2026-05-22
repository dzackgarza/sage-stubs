# Phase 01 — Foundation Completion

**Tier:** 0 (must complete before anything else)
**Status:** ⬜ Not Started
**Depends on:** —
**Unblocks:** all subsequent phases

## Goal

Close the gaps in the four foundational subpackages that every downstream
phase imports from: `structure/`, `misc/`, `categories/`, `sets/`, plus the
low-level `cpython/` and `data_structures/` shells. After Phase 01, anyone
writing a new stub in any other subpackage should be able to assume the
foundation surface is complete and stable.

## Entry criteria

- `sage-src` submodule is initialised at the Sage 10.7 tag/commit.
- The repo's quality pipeline (`just check`) runs green on the existing
  402 stubs.

## Exit criteria

- Every in-scope source module in the six subtrees below either has a
  matching `.pyi` or is documented as **Exempt** in this card's task
  table with a one-line reason.
- `mypy --strict sage-stubs/` passes.
- The three known blockers tracked in `STUB_GAPS.md` are either resolved
  or explicitly re-confirmed as still blocked.

## Tasks

Sizing: every task is a single commit covering 5–30 files unless flagged
**Exempt-audit** (which produces no `.pyi` files, only a documented
exempt list appended to this card).

| Task | Subtree / Scope | Files | Depends | Status | Notes |
|------|-----------------|-------|---------|--------|-------|
| T01.1 | **Audit** — full source inventory of the six subtrees; mark Cython internals, demos, and re-export shells as Exempt. Output: `.agents/phases/phase-01-exempt.md`. | 0 stubs (audit only) | — | ⬜ | Establishes per-task scope for T01.2–T01.10. |
| T01.2 | `sage.structure` — gap fill: `coerce`, `coerce_actions`, `coerce_dict` already present; add `dynamic_class`, `formal_sum`, `factory`, `factorization_integer`, `gens_py`, `set_factories`, `support_view`, `nonexact`, `mutability`, `parent_base`, `parent_gens`, `element_wrapper`, `richcmp`, `coerce_exceptions`. | ~15 | T01.1 | ⬜ | Existing stubs in this subtree must not be narrowed. |
| T01.3 | `sage.misc` — high-traffic utilities: `bindable_class`, `call`, `callable_dict`, `c3_controlled`, `classcall_metaclass`, `cython`, `decorators`, `fast_methods`, `function_mangling`, `lazy_attribute`, `lazy_list`, `lazy_string`, `lazy_format`, `nested_class`. | ~14 | T01.1 | ⬜ | `lazy_attribute` and `lazy_list` are referenced by category stubs already. |
| T01.4 | `sage.misc` — pickling, persistence, randomness: `persist`, `fpickle`, `pickle_old`, `prandom`, `randstate`, `weak_dict`, `inherit_comparison`, `instancedoc`, `parser`, `search`, `superseded`, `unknown`, `verbose`. | ~13 | T01.1 | ⬜ | |
| T01.5 | `sage.misc` — formatting / dev tools: `latex`, `latex_macros`, `latex_standalone`, `html`, `mathml`, `repr`, `table`, `viewer`, `sage_input`, `sage_eval`, `sageinspect`, `sagedoc`, `temporary_file`, `messaging`. | ~14 | T01.1 | ⬜ | Many are tiny; bundle as one commit. |
| T01.6 | `sage.misc` — remaining leaves: `proof`, `profiler`, `func_persist`, `defaults`, `flatten`, `functional`, `map_threaded`, `multireplace`, `mrange`, `object_multiplexer`, `converting_dict`, `element_with_label`, `constant_function`, `derivative`, `misc`, `misc_c`. | ~16 | T01.1 | ⬜ | |
| T01.7 | `sage.sets` — full subtree: `cartesian_product`, `disjoint_set`, `disjoint_union_enumerated_sets`, `family`, `finite_enumerated_set`, `finite_set_map_cy`, `finite_set_maps`, `image_set`, `integer_range`, `non_negative_integers`, `positive_integers`, `primes`, `pythonclass`, `real_set`, `recursively_enumerated_set`, `set`, `set_from_iterator`, `totally_ordered_finite_set`. | ~18 | T01.1 | ⬜ | `condition_set` and `finite_set` already exist; do not narrow. |
| T01.8 | `sage.categories` gap fill — verify every Sage 10.7 category module that is missing from `sage-stubs/categories/`. Cross-reference against existing 144 stubs; complete the residue. | ~10–20 | T01.1 | ⬜ | Likely candidates: `algebra_ideals`, `bialgebras_with_basis`, `crystals_finite_type_*` (verify against source). |
| T01.9 | `sage.cpython` — public surface: `getattr`, `string`, `type`, `debug`, `atexit`, `builtin_types`. | ~6 | T01.1 | ⬜ | Several modules are pure `.pxd`/internal — mark Exempt in T01.1. |
| T01.10 | `sage.data_structures` — `blas_dict`, `bounded_integer_sequences`, `mutable_poset`, `stream`, `binary_search`, `bitset`, `list_of_pairs`, `sparse_bitset` (Python-facing only). | ~8 | T01.1 | ⬜ | Some are purely `.pxd`; defer to Exempt list. |
| T01.11 | `STUB_GAPS.md` re-baseline — re-run the real-consumer regression capture against the new foundation; refresh the three blocked entries (`Posets.ParentMethods`, `random_element`, `_make_named_class_key`) with current data. | 0 stubs | T01.2–T01.10 | ⬜ | If any blocker is now resolvable, file a follow-up task; if still blocked, leave a fresh annotation. |
| T01.12 | `pyproject.toml` package registration — add `sage-stubs.cpython`, `sage-stubs.data_structures`, and any newly-introduced subdirs to `[tool.setuptools] packages`. | 1 (pyproject) | T01.2–T01.10 | ⬜ | This is the **only** permitted pyproject edit. |

## Parallel work guidance

- T01.1 is a hard prerequisite — claim and finish it first.
- After T01.1, **T01.2, T01.3, T01.7, T01.9, T01.10** can run truly in
  parallel (different subtrees).
- T01.3–T01.6 all touch `sage.misc/`; serialise these or split by clean
  file-level boundaries to avoid merge conflicts.
- T01.11 runs *after* the other tasks finish.
- T01.12 runs *last*, after every new directory is populated.

## Risks

- The `coerce*` modules in `sage.structure` have deeply interlinked types.
  Read the entire trio (`coerce`, `coerce_actions`, `coerce_dict`,
  `coerce_maps`) before committing T01.2.
- `lazy_import`, `cached_method`, and `abstract_method` already have
  stubs; T01.3 must NOT touch those except for verified bug fixes.
- `STUB_GAPS.md` shows that any change to category MROs can regress
  consumers — T01.8 should be the most conservative task in the phase.

## Exempt list

See `.agents/phases/phase-01-exempt.md` after T01.1 completes.
