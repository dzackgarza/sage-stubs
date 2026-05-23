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

### Measuring progress

`scripts/stub_coverage.py` walks both trees and prints per-subpackage
counts (`source / exempt / in_scope / covered / missing / %`). Use it for
phase-by-phase progress and for the global parity number.

```bash
just coverage                              # overall summary
just coverage -- --subpackage rings --missing   # list missing rings/ files
just coverage -- --json > /tmp/cov.json    # machine-readable
just coverage -- --threshold 0.95          # CI gate
```

The script honours an exempt list at
`.agents/phases/phase-01-exempt.md` (or any path passed via `--exempt`)
so audited Exempt modules don't drag the denominator down.

CI should fail when:
- coverage drops on `main` (regression), and/or
- coverage of a touched subpackage drops on a PR.

### Tooling: auto-scaffolding from source

`mypy.stubgen` (ships with `mypy`) generates a `.pyi` scaffold from a Python
module. The scaffold gives us **method enumeration for free** — Phase 1 of
the AGENTS.md three-phase procedure — but it produces stubs that are
unusable as-is for this repo because every parameter and return type comes
out as `Any`. **Stubgen output is a starting point, not a deliverable.**

Workflow for any task that needs to bootstrap many files:

```bash
just scaffold sage.rings.polynomial.polynomial_ring   # → /tmp/stubgen/...
# Or for a whole subpackage:
python3 -m mypy.stubgen -p sage.combinat.crystals -o /tmp/stubgen
```

Then for each scaffolded file:

1. Diff the scaffold's method list against the source's `cls.body` AST
   (AGENTS.md anti-inflation rule — stubgen does NOT distinguish direct
   from inherited methods for Cython classes).
2. Read the source per AGENTS.md Phase 2 (Resolve types). Replace EVERY
   `Any` with the resolved concrete type, `Self`, a finite union,
   `@overload`, or a source-audited argument/keyword container type that
   enumerates the accepted cases.
3. Drop the resulting `.pyi` into `sage-stubs/<path>/<file>.pyi`.
4. Run `just check`.

A scaffold that still contains `Any` will be rejected by
`scripts/check_stubs.py`, so the bootstrap step cannot be skipped on the
way to a commit. Stubgen's value is purely the enumeration — it shortens
Phase 1 from ~minutes per file to seconds, leaving the same Phase 2 / 3
work intact.

When stubgen fails (Cython modules without `.py` shims, missing optional
deps), fall back to reading the source directly per AGENTS.md.

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
  the runtime accepts several shapes, the rule is **still no `Any`**:
  enumerate the shapes with overloads, finite unions, or a source-audited
  container/option type when that is tighter than the variadic source
  spelling. If a variadic signature remains, its annotation is still part
  of the type surface and must not be broadened. Reserve `object` for
  Python protocol slots already allowed in AGENTS.md.
- **Forward references and import cycles.** Sage's runtime relies heavily
  on `LazyImport` to break import cycles. Stubs cannot use `LazyImport`,
  and quoted/string type references are banned. Add the direct import or
  minimal source-backed support stub; if the cycle cannot be resolved that
  way, leave the stub unchanged and report the blocked evidence.
- **Surface drift.** Sage 10.7 is the pinned version; do not pull surface
  from `sage-src` until the submodule has been confirmed at the
  appropriate tag/commit.
- **Inheritance vs direct definition.** AGENTS.md forbids treating
  inherited methods as direct. Auditing tasks must use AST `cls.body`
  inspection, not `ast.walk`.
