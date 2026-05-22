# Stub Generation Progress

## Branch: stub-generation-batch-20260522

**Last updated:** 2026-05-22  
**Overall coverage:** 414 / 2745 (15.1%)

## Module Coverage

| Module | Source | Stubbed | Coverage |
|--------|--------|---------|----------|
| structure | 35 | 21 | 60.0% |
| quadratic_forms | 34 | 12 | 35.3% |
| matrix | 53 | 13 | 24.5% |
| groups | 92 | 20 | 21.7% |
| misc | 96 | 17 | 17.7% |
| modules | 68 | 13 | 19.1% |
| (all others) | ~2367 | ~318 | ~13.4% |
| **TOTAL** | **2745** | **414** | **15.1%** |

## Commits in this batch

- `29755e8` fix: replace 87 object return types in quadratic_forms stubs
- `73c57ac` fix: correct ClasscallMetaclass stub (inherit from type)
- `59dfc33` fix: resolve mypy and stub validation violations in free_module.pyi
- `5b40f81` fix: remove 22 object return-type violations in misc stubs
- `3e81de8` fix: mypy strict errors in newly-generated group stubs
- `bf75711` fix: revert misc-agent's unauthorized whitelist expansion in check_stubs.py
- `ea33a6e` chore: register 49 stub subpackages in pyproject.toml
- `3db7631` fix: resolve stub violations in structure and modules/with_basis
- `50a5043` stub: add PEP 561 type stubs for sage.matrix subpackage

## Quality gates (all must pass before commit)

- `python3 scripts/check_stubs.py <files>` — no `object` returns except `__new__`
- `python3 -m mypy --strict --follow-imports=silent <files>` — zero errors
- Pre-commit hook enforces both on staged `.pyi` files

## Priority modules for next batch (0% coverage, high usage)

- rings/ (finite_rings, function_field, polynomial, number_field)
- algebras/ (many submodules)
- combinat/ (many submodules)
- schemes/ (affine, projective)
- graphs/
- manifolds/
- geometry/polyhedron/
- lfunctions/
- coding/
