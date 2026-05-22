# Feature: Full Stub Parity for sage-stubs

## Goal

Bring `sage-stubs` to **complete PEP 561 parity** with the Sage 10.7 Python
surface tracked under `sage-src/src/sage/`. Every `.py` and `.pyx` source file
that defines a public Python-facing symbol must have a corresponding `.pyi`
file in `sage-stubs/` that exports the public class, function, and constant
surface, and that passes the repo's quality contract.

This is a sweeping multi-month effort. The plan is staged as phases so that
multiple contributors (or agent sessions) can land work in parallel without
stepping on dependency cycles.

## Why this is needed

The existing scope (see `README.md`) is narrowly focused on the category /
structure / coercion infrastructure required for the
`sage-mypy-category-plugin`. Downstream consumers that import broader Sage
APIs (`sage.rings.polynomial.*`, `sage.combinat.*`, `sage.schemes.*`,
`sage.modular.*`, …) currently get `Untyped` shrugs from mypy or fall back to
runtime introspection. Full stub parity unblocks strict-mode mypy across the
entire Sage user surface.

## Scope

**In-scope source.** All modules under `sage-src/src/sage/**` that satisfy
all of:

- File suffix `.py` or `.pyx`.
- Not `all.py`, `all_cmdline.py`, `all_test.py`, or `__init__.py` (these are
  pure re-export shells; they get matching empty `__init__.pyi` files when
  needed for package registration, not surface stubs).
- Not a `*_test.py` / `tests.py` / `test_*.py` doctest harness — these
  exercise behaviour, not API.
- Not a `.pxd`, `.pxi`, `.h`, or other Cython internal header.

That filter currently selects **~2700 source modules**. The existing 402
stubs cover ~15 % of that surface, heavily concentrated in
`sage.categories.*`, `sage.structure.*`, and a thin slice of `sage.rings.*`,
`sage.combinat.*`, and `sage.modular.*`.

**Out-of-scope.**

- Cython `.pxd` / `.pxi` headers (not Python-facing).
- Internal demo / timing modules (`*_demo.pyx`, `*_timings.py`,
  `*_timings_cy.pyx`).
- Doctest harnesses (`*_test.py`, `tests.py`, `test_*.py`).
- Anything under `sage-src/src/sage/ext_data/`, `sage-src/src/sage/cli/`'s
  setup glue, and other directories that contain no public Python API.
- Edits to the Sage source. `sage-src/` is read-only context for stub
  authoring.

A `.py` / `.pyx` module is **stub-exempt** (no `.pyi` needed) if its public
surface is empty after the AGENTS.md "only public methods defined directly"
filter, OR if its only role is to re-export symbols defined elsewhere
(`all.py`). The Phase-1 task for each subtree audits and lists exempt
modules explicitly.

## Quality contract

Every stub written under this feature MUST satisfy the constraints in
`CLAUDE.md` / `AGENTS.md`. The non-negotiables, restated for emphasis:

- `Any` is banned in stubs. No exceptions.
- No `TYPE_CHECKING` blocks.
- No `# type: ignore`, no `cast(...)`, no `# noqa`.
- No edits to `pyproject.toml` lint / mypy / hook config (only adding new
  `[tool.setuptools] packages` entries).
- No scratch artifacts in the repo (plans, inventories, helper scripts go
  to `/tmp`, except the cards in `.agents/`).
- Source review first, stub writing second. The AGENTS.md three-phase
  procedure (enumerate → resolve → write) applies to every task.
- Preserve the class hierarchy from the source. No flattening.
- Stubs map `sage-src/src/sage/<module>/<file>.py` →
  `sage-stubs/<module>/<file>.pyi`. **No nested `sage-stubs/sage/...`.**

## Definition of done (for the feature as a whole)

- For every in-scope source module, either a matching `.pyi` exists in
  `sage-stubs/` OR the module is listed as exempt in the relevant phase
  card with a one-line justification.
- `python -m mypy --strict sage-stubs/` passes with zero errors.
- `ruff check sage-stubs/` passes with zero errors.
- `python3 scripts/check_stubs.py $(find sage-stubs -name "*.pyi")` passes.
- All new package paths are registered in `pyproject.toml` under
  `[tool.setuptools] packages`.
- `README.md` "Scope" section is rewritten to describe full parity rather
  than the narrow category-infrastructure carve-out.

## Tracking

The umbrella plan and current phase status live in
[`.agents/plan.md`](plan.md). Phase-level breakdowns and task tables live
under [`.agents/phases/`](phases/). Each phase card embeds its own
parallelisable task list and explicit dependency notes.

When picking up work: read `.agents/plan.md`, find the next phase with
**Status: Ready** that has no unmet dependencies, open its phase card, pick
a task marked `⬜ Pending` whose `Depends` column is satisfied, and update
the task status to `🟡 In Progress` (with your handle / agent id) before
starting. Mark `✅ Done` on the same line when the commit lands.

## Risks and known blockers

- **`STUB_GAPS.md` blockers.** Three direct-method patches
  (`Posets.ParentMethods`, `InfiniteEnumeratedSets.ParentMethods.random_element`,
  `CategoryWithParameters._make_named_class_key`) currently regress the real
  consumer capture. Phase 1 must keep those changes out unless the consumer
  side is fixed first.
- **Cython forwarders.** Many `.pyx` modules export Python classes whose
  `__cinit__` and `__init__` signatures live in C-level docstrings. Where
  the runtime accepts arbitrary Python coercion, the rule is **still no
  `Any`** — use `object` for genuinely opaque incoming values, `Self` for
  arithmetic forwards, and `Union` for documented coercion sets.
- **Forward references and import cycles.** Sage's runtime relies heavily
  on `LazyImport` to break import cycles. Stubs cannot use `LazyImport` and
  must use string forward references for genuinely recursive types.
- **Surface drift.** Sage 10.7 is the pinned version; do not pull surface
  from `sage-src` until the submodule has been confirmed at the
  appropriate tag/commit.
- **Inheritance vs direct definition.** AGENTS.md forbids treating
  inherited methods as direct. Auditing tasks must use AST `cls.body`
  inspection, not `ast.walk`.
