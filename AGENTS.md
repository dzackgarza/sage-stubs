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

## Stub conventions

- Every method in the source class must have a stub entry in the `.pyi` file.
- Use `Any` only as a last resort; prefer real types whenever the source makes them unambiguous.
- Preserve the class hierarchy exactly as in the source (`class Foo(Bar):` not `class Foo:`).
- Do not include docstrings, implementation bodies, or decorator logic — stubs only.
- Mark `@overload` where a method has multiple distinct call signatures.

## Package registration

When you add a stub for a new module path (e.g. `sage-stubs/rings/lazy_series.pyi`), add the
corresponding package to `pyproject.toml` under `[tool.setuptools] packages` if not already present.

## Verification

```bash
python -m mypy --strict sage-stubs/
```

All stubs must pass `mypy --strict` with no errors before the PR is ready.
