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

The only structural exception is `*args: Any` / `**kwargs: Any` in variadic signatures where the forwarded types are genuinely unspecified at the call site. This does not apply to named parameters.

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

## Class hierarchy

Preserve the class hierarchy exactly as in the source. Do not flatten inheritance.

## Package registration

When adding a stub for a new module path, add the corresponding package to `pyproject.toml` under `[tool.setuptools] packages` if not already present.

## Verification

```bash
python -m mypy --strict sage-stubs/
```

All stubs must pass `mypy --strict` with no errors before the PR is ready.
