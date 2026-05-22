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

`Any` is banned. Not "banned unless justified." Banned.

If a type is complex, use `Union[A, B]`, `TypeVar`, `overload`, or `object`. There is always a more precise type than `Any`.

Variadic signatures are not an exception. Use `*args: object` / `**kwargs: object` when the forwarded values are genuinely opaque at the call site.

`object` is honest opacity, not an escape hatch. It is acceptable only when the source accepts arbitrary Python objects, forwards genuinely opaque callback values, or exposes foreign runtime values whose type is not represented by existing Sage stubs. Named domain parameters must still be resolved.

**Named parameters must be resolved to domain types:**
- `precision` — is a number. Use `int` or the appropriate Sage numeric type.
- `degree` — is an integer. Use `int`.
- `prec` — is an integer. Use `int`.
- `n`, `p`, `k`, `m` — are integers unless the source says otherwise. Use `int`.
- `ring`, `base_ring` — use the actual base class (`Ring`, `CommutativeRing`, etc.).
- `other` on arithmetic methods — use `Self` or the operand type, not `Any`.
- `variable` — if the docstring says "a variable or integer", write `int | Variable`, not `Any`.
- `names` — if used for polynomial variable names, write `str | tuple[str, ...]`, not `Any`.

**Return types must be resolved:**
- If the source returns `P.element_class(P, ...)` where `P = self.parent()`, the return type is `Self` or the class itself.
- If the source returns `self`, the return type is `Self`.
- If the return type depends on the input type, use `@overload` to express the distinct signatures.

**The following rationalizations are not acceptable and will be rejected:**
- *"The library allows coercion from other types."* — Coercion is runtime behaviour. Annotate the intended type.
- *"I don't have that type imported."* — Add the import or use a string forward reference. Missing imports are not a license for `Any`.
- *"The parameter is polymorphic."* — If you can describe the types in words, write them as a `Union`. If you wrote a plain-English description and then typed `Any`, that is dishonesty, not uncertainty.
- *"The return type depends on runtime input."* — Use `@overload`.
- *"I described the type correctly but wrote `Any` anyway."* — Not acceptable under any circumstance.

**Only stub public methods defined directly on the class.** Nested helper functions (e.g. `def coefficient(n)` defined inside `__call__`) are not class methods. Inherited aliases are not direct definitions. Check `cls.body` in the AST, not the full `ast.walk` output.

## Banned output patterns

These patterns were observed in failed agent sessions and must be rejected by review, hooks, or tests.

**No `TYPE_CHECKING` blocks in stubs.** A `.pyi` file is already an annotation surface. Import annotation types directly at top level. If that import exposes a missing dependency, add the minimal source-grounded stub for the dependency or use a quoted forward reference only for genuinely recursive definitions.

**No local suppressions.** `# type: ignore`, `# noqa`, `cast(...)`, and similar lint or type-checking suppressions are banned in stub files. Fix the signature, import, or supporting stub instead.

**No lint or type-check relaxation.** Stub tasks must not edit `pyproject.toml` to weaken Ruff, mypy, hook, or validation settings. The only permitted `pyproject.toml` change for ordinary stub work is adding a real package path under `[tool.setuptools] packages`.

**No scratch artifacts in the repo.** Do not commit helper scripts, extraction scripts, inventories, plans, temporary tests, or generated notes such as `plan.md`, `test_*.py`, `generate_*.py`, `fix_*.py`, or one-off method-list files. Put throwaway work in `/tmp`.

**No nested `sage-stubs/sage/...` layout.** `sage-src/src/sage/structure/foo.py` maps to `sage-stubs/structure/foo.pyi`, not `sage-stubs/sage/structure/foo.pyi`.

**No destructive narrowing.** Existing stubs are part of the sidecar surface. Do not replace an existing file with a smaller partial stub, delete existing public definitions, or narrow existing signatures unless source review proves the existing stub is wrong. Corrections must be minimal and source-cited.

**No inherited-method inflation.** If a requested method is inherited rather than defined directly on the target class, report that fact. Do not add inherited methods as direct methods.

**No prompt-driven invention.** A method name appearing in a prompt is not evidence that the method belongs in the stub. Every method and signature must be justified by the direct Sage source body or by a documented alias in the source.

**No verbose builtins.** Use `object`, `type`, `list[T]`, and `dict[K, V]`, not `builtins.object`, `builtins.type`, `typing.List`, or `typing.Dict`.

## Class hierarchy

Preserve the class hierarchy exactly as in the source. Do not flatten inheritance.

## Package registration

When adding a stub for a new module path, add the corresponding package to `pyproject.toml` under `[tool.setuptools] packages` if not already present.

Do not modify validation, lint, mypy, build, or hook configuration as part of a stub task. Such changes are process changes, not stub work.

## Verification

```bash
python -m mypy --strict sage-stubs/
```

All stubs must pass `mypy --strict` with no errors before the PR is ready.

Before completion, also run `git diff --check`. For changed `.pyi` files, run the repo's stub checker if available:

```bash
python3 scripts/check_stubs.py <changed .pyi files>
```

Reviewers and hooks should reject `TYPE_CHECKING`, `Any`, local suppressions, root scratch artifacts, nested `sage-stubs/sage/` paths, and non-package-registration edits to validation config.
