# AGENTS.md — sage-stubs

## What this repo is

PEP 561 stub-only package (`sage-stubs`) providing type stubs for the SageMath library.
Stubs live under `sage-stubs/` and mirror the layout of the real `sage` package.
Each `.pyi` file must be a valid mypy stub for the corresponding `sage/**/*.py` source file.

## Sage source reference

The actual SageMath source is available as a git submodule at `sage-src/`.

**Before starting any stub work, initialize it:**

```bash
git submodule update --init --depth 1
```

The full source for any module you are stubbing is then readable at `sage-src/src/sage/<module>/<file>.py`.

**You must read the source before writing any stub.** Do not infer signatures from memory or guesswork.

## Stub authoring procedure

Work in three phases. Do not write any stub code until Phase 2 is complete.

**Phase 1 — Enumerate:** Read the source file. List every public method defined directly on the target class (not inherited), with its source line number. Output this list explicitly before proceeding.

**Phase 2 — Resolve types:** For each method in your list, read the implementation and docstring. State the concrete return type and parameter types. Cite the source line that justifies each type decision.

**Phase 3 — Write:** Every method from Phase 1 must appear. Every type must match Phase 2. Only then write the `.pyi` file.

## Type annotation quality contract (non-negotiable)

### Banned unconditionally

- **`Any` as a return type** — banned. No exceptions, no justifications.
- **`Any` as a named parameter type** — banned. `*args: Any` and `**kwargs: Any` in variadic positions are the only permitted use.
- **`object` as a return type** — banned, except `__new__`. Use a concrete Sage type.
- **`builtins.object` as a return type** — banned for the same reason. Qualifying `object` via the `builtins` module does not change its meaning.
- **`# type: ignore` comments** — banned in stub files. If a type error arises, fix the underlying stub, not the error.
- **Deprecated `typing` forms** — banned. Use `X | Y` not `Union[X, Y]`, `X | None` not `Optional[X]`, `list[X]` not `List[X]`, import from `collections.abc` not `typing` for `Callable`/`Iterator`.

### Required

- **Named parameters must be resolved to domain types.** If you can name the type in words, write it as a type:
  - `precision`, `prec`, `degree`, `n`, `p`, `k`, `m` — use `int` (or the specific Sage numeric type if the source confirms it)
  - `ring`, `base_ring` — use `Ring`, `CommutativeRing`, `Field`, etc. (read the source to determine which)
  - `other` in arithmetic methods — use `Self` or the concrete operand type
  - `variable` — `int | Variable` if the source says so, not `Any`
  - `names` for polynomial variables — `str | tuple[str, ...]`
- **Return types must be resolved** from the source implementation:
  - If the source returns `self`, use `Self`
  - If the source returns `P.element_class(...)`, use the element class
  - If the return type depends on the input, use `@overload`

### Completing a task means fixing ALL violations

If you are asked to fix violations in a file, you must fix every violation reported by `python3 scripts/check_stubs.py <file>`. Fixing unrelated files or making only cosmetic changes (removing quoted annotations, updating import style) while leaving the assigned violations in place is not task completion.

Run `python3 scripts/check_stubs.py <yourfile>` and verify it reports 0 violations before marking your task complete.

### Direct methods only

Only stub public methods defined directly on the class body. Nested helper functions (e.g. `def coefficient(n)` defined *inside* `__call__`) are not class methods. Check `cls.body` in the AST, not the full `ast.walk` output — `ast.walk` descends into nested function bodies and will produce false positives.

## Class hierarchy

Preserve the class hierarchy exactly as in the source. Do not flatten inheritance.

## Package registration

When adding a stub for a new module path, add the corresponding package to `pyproject.toml` under `[tool.setuptools] packages` if not already present.

## Verification

```bash
python -m mypy --strict sage-stubs/
```

All stubs must pass `mypy --strict` with no errors before the PR is ready.
