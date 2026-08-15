# Contributing to sage-stubs

This project uses [`just`](https://just.systems/) to encapsulate all development workflows. 

## First Time Setup

If you don't have `just` or `uv` installed, run the bootstrap script first:

```bash
./bootstrap.sh
```

This automatically installs both tools if missing. Then run:

```bash
just setup
```

This configures git hooks and initializes submodules.

## Development Recipes

See the `justfile` for all available recipes. Common workflows:

| Recipe | Description |
|--------|-------------|
| `just check` | Full quality check (run before every commit) |
| `just lint` | Fast lint only (no mypy) |
| `just fix` | Auto-fix what ruff can fix |
| `just coverage` | Report stub-vs-source coverage |
| `just scaffold module=<name>` | Scaffold a fresh stub for one Sage module |
| `just guardrails` | Check banned patterns and narrowing detection |

The pre-commit hook enforces `just lint-staged` on staged `.pyi` files automatically.

## Workflow

1. Claim a phase task from `.agents/plan.md`
2. Make your changes
3. Run `just check` before committing
4. Commit (pre-commit hook will validate staged files)
