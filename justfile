# sage-stubs quality pipeline

# Full repository quality check. This is intentionally a full-tree gate: the
# generated backlog remains red until its placeholder types are replaced.
check:
    @echo "--- ruff: syntax, imports, annotations, and stub rules ---"
    ruff check sage-stubs/
    ruff format --check sage-stubs/
    @echo "--- check_stubs: Any/object and suppression bans ---"
    python3 scripts/check_stubs.py
    @echo "--- check_guardrails: repository-wide banned patterns ---"
    python3 scripts/check_guardrails.py --all
    @echo "--- quality configuration cannot be weakened ---"
    python3 scripts/check_quality_config.py
    @echo "--- semantic quality debt audit ---"
    python3 scripts/audit_stub_quality.py --root sage-stubs --fail-on warning
    @echo "--- mypy: strict full-tree type checking ---"
    python3 -m mypy --strict --no-incremental --follow-imports=normal sage-stubs/
    @echo "--- basedpyright: strict full-tree type checking ---"
    basedpyright --project pyrightconfig.json
    @echo "--- semgrep: generated/erased-type rules ---"
    semgrep --validate --config .semgrep/stub-quality.yml
    semgrep scan --metrics=off --error --config .semgrep/stub-quality.yml --exclude sage-src .
    @echo "All checks passed."

# Fast lint only (no type checkers or Semgrep).
lint:
    ruff check sage-stubs/
    ruff format --check sage-stubs/
    python3 scripts/check_stubs.py
    python3 scripts/check_guardrails.py --all

# High-signal AST audit of placeholder and type-erasure debt.
audit *args:
    python3 scripts/audit_stub_quality.py --root sage-stubs {{args}}

# Both independent full-tree type checkers.
typecheck:
    python3 -m mypy --strict --no-incremental --follow-imports=normal sage-stubs/
    basedpyright --project pyrightconfig.json

# Repository-local Semgrep rules.
semgrep:
    semgrep --validate --config .semgrep/stub-quality.yml
    semgrep scan --metrics=off --error --config .semgrep/stub-quality.yml --exclude sage-src .

# Fast lint for staged stub files only, used by the pre-commit hook.
lint-staged:
    @files="$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.pyi$' || true)"; \
    if [ -n "$files" ]; then \
        ruff check $files; \
        python3 scripts/check_stubs.py $files; \
    fi

# Auto-fix what ruff can fix.
fix:
    ruff check --fix sage-stubs/

# Report stub-vs-source coverage. Pass extra flags like --missing / --orphan /
# --subpackage X / --threshold 0.95 / --json.
coverage *args:
    python3 scripts/stub_coverage.py {{args}}

# Scaffold a fresh stub for one Sage module using mypy stubgen.
# Output lands under /tmp/stubgen/ so it can be hand-refined into sage-stubs/.
# Example: just scaffold sage.rings.polynomial.polynomial_ring
scaffold module:
    @rm -rf /tmp/stubgen
    python3 -m mypy.stubgen -m {{module}} --include-private --inspect-mode -o /tmp/stubgen || \
      python3 -m mypy.stubgen -p {{module}} -o /tmp/stubgen
    @echo "Scaffold written under /tmp/stubgen/. Refine (replace every Any!) and copy into sage-stubs/."

# One-shot setup: point git at the tracked hooks under .githooks/.
# Run this once per clone. Idempotent.
setup:
    git config core.hooksPath .githooks
    @git submodule update --init --depth 1
    @echo "sage-stubs ready: hooks active, sage-src initialised."
    @echo "Next: read .agents/plan.md and claim a phase task."

# Legacy single-file installer for clones that haven't migrated to core.hooksPath.
install-hooks:
    cp .githooks/pre-commit .git/hooks/pre-commit
    cp .githooks/post-commit .git/hooks/post-commit
    chmod +x .githooks/pre-commit .githooks/post-commit
    @echo "pre-commit + post-commit hooks installed locally."

# Guardrails — banned patterns + scratch artefacts + narrowing detection.
guardrails *args:
    python3 scripts/check_guardrails.py {{args}}
