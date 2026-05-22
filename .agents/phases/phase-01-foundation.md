# Phase 01 — Foundation Completion

**Tier:** 0 (must complete before anything else)
**Status:** 🟡 In Progress
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
| T01.0 | **Tooling validation** — confirm `scripts/stub_coverage.py` runs cleanly, confirm `mypy.stubgen` is installed (`python3 -m mypy.stubgen --help`), confirm `just coverage` and `just scaffold sage.structure.element` both succeed. Record the baseline `just coverage --json` to `/tmp/baseline-cov.json` (not committed) for later regression checks. | 0 | — | ✅ Done | Baseline at `/tmp/baseline-cov.json`; use `.venv/bin/stubgen` (mypy 2.1 module entry broken on Py3.14). |
| T01.1 | **Audit** — full source inventory of the six subtrees; mark Cython internals, demos, and re-export shells as Exempt. Output: `.agents/phases/phase-01-exempt.md`. Use `scripts/stub_coverage.py --missing --subpackage <name>` to enumerate candidates. | 0 stubs (audit only) | T01.0 | ✅ Done | 70 exempt modules documented; 151 in-scope missing listed. |
| T01.2 | `sage.structure` — gap fill: `coerce`, `coerce_actions`, `coerce_dict` already present; add `dynamic_class`, `formal_sum`, `factory`, `factorization_integer`, `gens_py`, `set_factories`, `support_view`, `nonexact`, `mutability`, `parent_base`, `parent_gens`, `element_wrapper`, `richcmp`, `coerce_exceptions`. | ~15 | T01.1 | ✅ Done | Added 8 stubs + minimal `parent_old.pyi` for hierarchy; structure subtree 100% in-scope. |
| T01.3 | `sage.misc` — high-traffic utilities: `bindable_class`, `call`, `callable_dict`, `c3_controlled`, `classcall_metaclass`, `cython`, `decorators`, `fast_methods`, `function_mangling`, `lazy_attribute`, `lazy_list`, `lazy_string`, `lazy_format`, `nested_class`. | ~14 | T01.1 | ✅ Done | Commits 573d0bf (+ sets mis-commit 7d2a218 superseded by a832253). `function_mangling` absent from Sage 10.7 source. |
| T01.4 | `sage.misc` — pickling, persistence, randomness: `persist`, `fpickle`, `pickle_old`, `prandom`, `randstate`, `weak_dict`, `inherit_comparison`, `instancedoc`, `parser`, `search`, `superseded`, `unknown`, `verbose`. | ~13 | T01.1 | ✅ Done | Completed in prior session. |
| T01.5 | `sage.misc` — formatting / dev tools: `latex`, `latex_macros`, `latex_standalone`, `html`, `mathml`, `repr`, `table`, `viewer`, `sage_input`, `sage_eval`, `sageinspect`, `sagedoc`, `temporary_file`, `messaging`. | ~14 | T01.1 | ✅ Done | html, latex_macros, latex_standalone, mathml, repr, table, viewer, messaging, temporary_file, timing, sage_timeit, sage_timeit_class, sage_unittest, sagedoc_conf. |
| T01.6 | `sage.misc` — remaining leaves: `proof`, `profiler`, `func_persist`, `defaults`, `flatten`, `functional`, `map_threaded`, `multireplace`, `mrange`, `object_multiplexer`, `converting_dict`, `element_with_label`, `constant_function`, `derivative`, `misc`, `misc_c`. | ~16 | T01.1 | ✅ Done | All remaining misc modules; misc 100% covered. |
| T01.7 | `sage.sets` — full subtree: `cartesian_product`, `disjoint_set`, `disjoint_union_enumerated_sets`, `family`, `finite_enumerated_set`, `finite_set_map_cy`, `finite_set_maps`, `image_set`, `integer_range`, `non_negative_integers`, `positive_integers`, `primes`, `pythonclass`, `real_set`, `recursively_enumerated_set`, `set`, `set_from_iterator`, `totally_ordered_finite_set`. | ~18 | T01.1 | ✅ Done | 7d2a218 + a832253; 100% in-scope. |
| T01.8 | `sage.categories` gap fill — verify every Sage 10.7 category module that is missing from `sage-stubs/categories/`. Cross-reference against existing 144 stubs; complete the residue. | ~10–20 | T01.1 | 🟡 In Progress | Subagent: 5 modules (super_*, vector_bundles). |
| T01.9 | `sage.cpython` — public surface: `getattr`, `string`, `type`, `debug`, `atexit`, `builtin_types`. | ~6 | T01.1 | ✅ Done | 3803048; 100% in-scope. |
| T01.10 | `sage.data_structures` — `blas_dict`, `bounded_integer_sequences`, `mutable_poset`, `stream`, `binary_search`, `bitset`, `list_of_pairs`, `sparse_bitset` (Python-facing only). | ~8 | T01.1 | ✅ Done | 51252e9; `binary_search` is cdef-only (no stub). |
| T01.11 | `STUB_GAPS.md` re-baseline — re-run the real-consumer regression capture against the new foundation; refresh the three blocked entries (`Posets.ParentMethods`, `random_element`, `_make_named_class_key`) with current data. | 0 stubs | T01.2–T01.10 | ⬜ | If any blocker is now resolvable, file a follow-up task; if still blocked, leave a fresh annotation. |
| T01.12 | `pyproject.toml` package registration — add `sage-stubs.cpython`, `sage-stubs.data_structures`, and any newly-introduced subdirs to `[tool.setuptools] packages`. | 1 (pyproject) | T01.2–T01.10 | ⬜ | This is the **only** permitted pyproject edit. |

## Bootstrap with stubgen

Tasks T01.2 – T01.10 should each begin with a stubgen scaffold of the
target module(s) (see [feature.md tooling section](../feature.md#tooling-auto-scaffolding-from-source)).
Stubgen's enumeration is the cheapest way to satisfy AGENTS.md Phase 1
(list every public method) — but every `Any` in the scaffold must be
resolved by hand before commit, and inherited methods stubgen emits must
be filtered out by checking `cls.body` in the source AST.

## Parallel work guidance

- T01.0 first, then T01.1 — both are hard prerequisites.
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
