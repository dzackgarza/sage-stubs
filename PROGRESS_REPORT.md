# Sage-Stubs Comprehensive Progress Report

Generated: 2026-05-27

## Executive Summary

**Overall stub coverage: 20.9% of in-scope source modules (575 / 2745).**

Stub quality when measured by symbolic API surface is much lower: existing stubs capture
only ~17% of the ~55,000 named public symbols in the Sage source.
Coverage is concentrated in `categories` (60% of files), `structure` (66%), and `tensor`
(94%), with the remaining ~2,170 source modules having zero or minimal stub coverage.

**Estimated effort to full parity: 1,800–2,200 stub files remaining, each requiring
source review, type resolution, and writing per AGENTS.md.**

* * *

## 1. Scope of the Sage 10.7 Source Surface

| Metric | Value |
| --- | --- |
| Total source files (`.py` + `.pyx`) | 3,007 |
| Total source lines | 2,699,000 |
| Python source lines | 2,057,000 |
| Cython source lines | 642,000 |
| `all.py`/`all_cmdline.py`/`all_test.py` re-export shells | 173 |
| `__init__.py` files | 49 |
| Test/doctest harnesses excluded from scope | 59 |
| `.pxd`/`.pxi`/`.h` Cython internals (not stub-target) | 821 |
| Timing/demo modules | 3 |
| **In-scope source modules requiring stubs** | **2,745** |
| Public classes (regex-based; .py + .pyx) | ~5,100 |
| Public methods (regex-based; .py + .pyx) | ~46,400 |
| Public module-level functions (regex-based; .py + .pyx) | ~8,200 |
| **Estimated total named public symbols** | **~55,000** |

The 2,745 in-scope modules represent 2,442 `.py` files and 565 `.pyx` files (after
removing excluded basenames and test/doc patterns).

The 18-phase plan in `.agents/plan.md` groups modules into dependency-ordered tiers.
The plan estimate of ~2,160 stub commits across ~140–160 tasks is conservative but
roughly accurate.

* * *

## 2. Existing Stub Coverage

### 2.1 By subpackage (module-file count)

`scripts/stub_coverage.py` reports 575 covered, 0 exempt, 2,170 missing out of 2,745
in-scope.

| Subpackage | Source | Covered | Missing | % Files |
| --- | --- | --- | --- | --- |
| algebras | 113 | 14 | 99 | 12.4 |
| arith | 7 | 1 | 6 | 14.3 |
| calculus | 16 | 0 | 16 | 0.0 |
| **categories** | 232 | 139 | 93 | 59.9 |
| cli | 7 | 0 | 7 | 0.0 |
| coding | 42 | 3 | 39 | 7.1 |
| **combinat** | 380 | 68 | 312 | 17.9 |
| cpython | 8 | 0 | 8 | 0.0 |
| crypto | 25 | 0 | 25 | 0.0 |
| data_structures | 9 | 0 | 9 | 0.0 |
| databases | 15 | 0 | 15 | 0.0 |
| doctest | 13 | 0 | 13 | 0.0 |
| dynamics | 18 | 3 | 15 | 16.7 |
| ext | 3 | 0 | 3 | 0.0 |
| ext_data | 1 | 0 | 1 | 0.0 |
| features | 60 | 0 | 60 | 0.0 |
| functions | 20 | 0 | 20 | 0.0 |
| game_theory | 6 | 0 | 6 | 0.0 |
| games | 4 | 0 | 4 | 0.0 |
| geometry | 88 | 16 | 72 | 18.2 |
| graphs | 89 | 6 | 83 | 6.7 |
| groups | 92 | 28 | 64 | 30.4 |
| homology | 14 | 0 | 14 | 0.0 |
| interacts | 7 | 0 | 7 | 0.0 |
| interfaces | 57 | 5 | 52 | 8.8 |
| knots | 6 | 0 | 6 | 0.0 |
| lfunctions | 5 | 4 | 1 | 80.0 |
| libs | 81 | 1 | 80 | 1.2 |
| logic | 6 | 0 | 6 | 0.0 |
| **manifolds** | 68 | 28 | 40 | 41.2 |
| matrix | 53 | 13 | 40 | 24.5 |
| matroids | 28 | 0 | 28 | 0.0 |
| misc | 96 | 18 | 78 | 18.8 |
| modular | 127 | 30 | 97 | 23.6 |
| modules | 68 | 20 | 48 | 29.4 |
| monoids | 12 | 0 | 12 | 0.0 |
| numerical | 24 | 1 | 23 | 4.2 |
| parallel | 7 | 0 | 7 | 0.0 |
| plot | 48 | 2 | 46 | 4.2 |
| probability | 2 | 0 | 2 | 0.0 |
| quadratic_forms | 34 | 12 | 22 | 35.3 |
| quivers | 8 | 1 | 7 | 12.5 |
| repl | 38 | 0 | 38 | 0.0 |
| **rings** | 337 | 82 | 255 | 24.3 |
| sandpiles | 2 | 0 | 2 | 0.0 |
| sat | 8 | 0 | 8 | 0.0 |
| schemes | 151 | 27 | 124 | 17.9 |
| sets | 19 | 7 | 12 | 36.8 |
| stats | 12 | 0 | 12 | 0.0 |
| **structure** | 35 | 23 | 12 | 65.7 |
| symbolic | 22 | 1 | 21 | 4.5 |
| **tensor** | 18 | 17 | 1 | 94.4 |
| tests | 81 | 0 | 81 | 0.0 |
| topology | 15 | 2 | 13 | 13.3 |
| typeset | 6 | 3 | 3 | 50.0 |
| **TOTAL** | **2,745** | **575** | **2,170** | **20.9** |

13 orphan stubs exist (stub files with no matching source), plus 67 `__init__.pyi`
package-init stubs.

### 2.2 By symbolic surface (estimated)

| Metric | Sage Source | Stubs | % |
| --- | --- | --- | --- |
| Classes | ~5,100 | 1,168 | 22.9% |
| Methods | ~46,400 | 8,348 | 18.0% |
| Module-level functions | ~8,200 | 300 | 3.7% |
| `@overload` specializations | — | 169 | — |
| `TypeVar` declarations | — | 31 | — |
| **Total named symbols** | **~55,000** | **~9,500** | **~17%** |

These are counts, not weighted by complexity.
Many existing stubs cover only a fraction of their source modules' methods (average
method coverage: 54%).

### 2.3 By source lines of code

| Subpackage | Source KLOC | Stub Lines | Ratio |
| --- | --- | --- | --- |
| tensor | 23 | 1,168 | 5.0% |
| lfunctions | 4 | 170 | 3.9% |
| categories | 100 | 2,733 | 2.7% |
| sets | 17 | 365 | 2.1% |
| typeset | 2 | 44 | 2.0% |
| structure | 31 | 592 | 1.9% |
| manifolds | 97 | 1,760 | 1.8% |
| modules | 58 | 1,007 | 1.7% |
| quadratic_forms | 24 | 390 | 1.7% |
| modular | 116 | 1,320 | 1.1% |
| groups | 65 | 626 | 1.0% |
| **Global** | **2,699** | **19,047** | **0.71%** |

Stub files average 29 lines each.
The largest stubs:
- `graphs/graph_generators.pyi` (397 lines, 12% of source)
- `modules/free_module.pyi` (325 lines, 3.8% of source)
- `quadratic_forms/quadratic_form.pyi` (237 lines, 13.6% of source)

### 2.4 Subpackages with zero stubs (0% coverage)

27 subpackages have zero stubs: calculus, cli, cpython, crypto, data_structures,
databases, doctest, ext, ext_data, features, functions, game_theory, games, homology,
interacts, knots, logic, matroids, monoids, numerical (nearly zero), parallel,
probability, repl, sandpiles, sat, stats, tests.

Combined, these represent ~720 source files and ~350,000 lines of source code.

* * *

## 3. Stub Quality Assessment

### 3.1 Current quality state

All existing stubs pass `ruff` with zero errors.
Mypy reports:

| Error Category | Count |
| --- | --- |
| `override` (mismatched signatures) | 36 |
| `import-untyped` | 36 |
| `unused-ignore` | 25 |
| `misc` | 19 |
| `valid-type` | 11 |
| `attr-defined` | 9 |
| `type-arg` | 5 |
| `name-defined` | 5 |
| `overload-cannot-match` | 1 |
| `no-redef` | 1 |
| **Total mypy errors** | **148 across 70 files** |

Legacy guardrail violations (not yet cleaned up; allowed to persist in baseline but
blocked on new commits): ~30 files with `TYPE_CHECKING`, `# noqa`, `# type: ignore`, or
`from typing import Any` patterns.

### 3.2 Stub completeness within covered files

Of the 575 covered stub files:
- **18** are effectively empty (no class/function definitions, <5 lines)
- **94** have no methods and <10 lines (class-stub shells or import-only)
- **303** cover fewer than 50% of their source file's methods
- **177** cover fewer than 10% of their source file's methods
- Average method coverage: 54%

Many stubs in `categories/` provide the class hierarchy and key provider methods but
omit large swaths of concrete implementations.
Stubs in `combinat/`, `rings/`, and `schemes/` tend to be thin shells that list a
fraction of the public surface.

### 3.3 Type precision

Stubs are source-backed and avoid `Any` (enforced by pre-commit hooks on new commits).
The existing stubs use:

- 8,348 direct method definitions
- 169 `@overload` specializations
- 31 `TypeVar` declarations
- 1,168 class definitions with preserved source hierarchy

No `cast()` calls, `TYPE_CHECKING` blocks (in new commits), or type suppressions exist
in the canonical stub surface.
Legacy files predating the contract contain a small number of violations that are
cleaned up as files are touched.

* * *

## 4. Known Blockers

Tracked in `STUB_GAPS.md`:

- **Posets.ParentMethods**: Source methods (`le`, `lt`, `ge`, `gt`, `upper_covers`,
  `lower_covers`, `order_ideal`, `order_filter`) are unannotated over the poset element
  type. Requires a typed poset element/subset model before filling.
- **InfiniteEnumeratedSets.ParentMethods.random_element**: Adding this method caused
  self-type argument errors.
  Needs the enumerated-set provider self type aligned first.
- **CategoryWithParameters._make_named_class_key**: Adding it exposed broader
  local-wrapper Category mismatches in the downstream consumer.
- **No `Any` escape hatch**: For Cython forwarders, variadic signatures, and coercion
  paths, the ban on `Any` means overloads, finite unions, or source audits must be used.
  For deeply dynamic Sage APIs, this adds significant per-file review cost.
- **LazyImport cycles**: Sage's runtime depends on `LazyImport` to break cycles.
  Stubs cannot use `LazyImport`, and quoted string type references are banned.
  Direct imports may create cycles that require structural sidecar work.

* * *

## 5. Estimated Effort to Full Parity

### 5.1 Remaining work

| Item | Count |
| --- | --- |
| Source modules needing stubs | 2,170 |
| Stub files needing quality improvements | ~300+ (thin/incomplete) |
| Legacy guardrail violations to fix | 30 files |
| Mypy errors to resolve | 148 in 70 files |
| Known blockers requiring design work | 3–5 |
| Exempt module audit required (Phase 01) | Full tree |
| Package registration entries needed | ~15–20 subpackages |

### 5.2 Effort estimates (per the 18-phase plan)

The `.agents/plan.md` estimates ~2,160 stub commits across ~140–160 tasks, broken into
18 phases. This is a lower bound — the estimate assumes ~5–30 files per task and a
clean-enumeration-then-type-resolution workflow.

Realistic effort per source file varies enormously:

- **Simple modules** (data containers, enums, thin wrappers): 15–45 min each.
  Many source files have 1–3 classes with 5–20 method signatures.
- **Medium modules** (standard mathematical objects with clear signatures): 1–3 hours
  each. These require reading source for every method, resolving Sage type hierarchies,
  and writing correct overloads.
- **Large/complex modules** (26,900-line `generic_graph.py`, 14,700-line
  `finite_state_machine.py`, 12,800-line `number_field.py`): 1–3 days each.
  These have hundreds of methods, deep inheritance, coercion paths, Cython
  intersections, and dynamic dispatch that must be modeled.
- **Cython-heavy modules** (`.pyx` files without Python shims): 2–5x longer than pure
  Python equivalents. `__cinit__` and `__init__` signatures live in C-level docstrings;
  stubgen fails; every method must be extracted from source or runtime.

The 18-phase plan is dependency-ordered, meaning Phase 01 must complete first
(Foundation — survey, exempt list, CI wiring).
After that, 4 Tier-1 phases (02–05, ~445 files) can run in parallel, followed by Tier-2,
Tier-3, Tier-4, and Tier-5 in dependency order.

### 5.3 Risk factors

- **No exempt list exists yet** (Phase 01, Task T01.1). All 2,745 modules are counted as
  "must stub." A proper audit may exempt 5–15% as re-export shells, reducing the
  denominator.
- **Cython stubs are harder**: 565 `.pyx` files require different extraction techniques.
  Many expose public Python classes through C-level API.
- **Type model complexity**: Sage's dynamic coercion, category framework, and
  `LazyImport` patterns require more than simple signature enumeration.
  Each file needs source reading, not just stubgen + cleanup.
- **Stub quality floor**: The AGENTS.md contract bans `Any`, requires source review for
  every method, and enforces hierarchy preservation.
  This guarantees quality but makes per-file costs higher than a "stubgen + skim"
  approach.

* * *

## 6. Phase Status Summary

| Phase | Source Files | Status | Notes |
| --- | --- | --- | --- |
| 01 Foundation | ~145 | ⬜ Not Started | Exempt audit, CI wiring, survey |
| 02 Core rings | ~80 | ⬜ Not Started | Blocks on 01 |
| 03 Polynomial rings | ~95 | ⬜ Not Started | Blocks on 01 |
| 04 Number-theoretic rings | ~130 | ⬜ Not Started | Blocks on 01 |
| 05 Linear algebra | ~120 | ⬜ Not Started | Blocks on 01 |
| 06 Algebras | ~70 | ⬜ Not Started | Blocks on 02, 05 |
| 07 Lie/Quantum | ~50 | ⬜ Not Started | Blocks on 02, 05 |
| 08 Groups | ~92 | ⬜ Not Started | Blocks on 02, 05 |
| 09 Combinat leaves | ~135 | ⬜ Not Started | Blocks on 02 |
| 10 Symmetric functions | ~95 | ⬜ Not Started | Blocks on 09 |
| 11 Crystals/Posets | ~115 | ⬜ Not Started | Blocks on 09 |
| 12 Geometry | ~88 | ⬜ Not Started | Blocks on 05 |
| 13 Schemes/Dynamics | ~170 | ⬜ Not Started | Blocks on 04, 12 |
| 14 Modular forms | ~130 | ⬜ Not Started | Blocks on 04, 05 |
| 15 Topology/etc | ~195 | ⬜ Not Started | Blocks on 05 |
| 16 Symbolic | ~65 | ⬜ Not Started | Blocks on 02 |
| 17 Applied domains | ~155 | ⬜ Not Started | Blocks on 02, 05 |
| 18 Infrastructure | ~330 | ⬜ Not Started | Blocks on 02 |

* * *

## 7. Current Trajectory

The project has established governance (AGENTS.md quality contract), tooling (pre-commit
hooks, stub coverage, checker scripts, plan tracking), and a dependency-ordered 18-phase
plan. Actual implementation has not yet begun: all 18 phases are "Not Started" and no
exempt audit or Phase 01 task has been completed.

**Bottom line: 20.9% stub coverage by file count, ~17% by symbol count, with stubs
heavily concentrated in the category/structure/tensor infrastructure.
Full parity requires completing ~2,170 new stub files plus quality improvement of ~300+
existing thin stubs, in dependency order across 18 phases.**
