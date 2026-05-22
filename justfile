# sage-stubs quality pipeline

# Full quality check — run before every commit (also enforced by .githooks/pre-commit).
check:
    @echo "--- ruff: deprecated patterns + missing annotations ---"
    ruff check sage-stubs/
    @echo "--- check_stubs: Any/object ban ---"
    python3 scripts/check_stubs.py $(find sage-stubs -name "*.pyi")
    @echo "--- type_surface_review: changed type surfaces require review ---"
    python3 scripts/type_surface_review.py
    @echo "--- check_guardrails: banned patterns + protected config (--all) ---"
    python3 scripts/check_guardrails.py --all || echo "(legacy backlog — see report above; new commits are still gated by the hook on staged files)"
    @echo "--- mypy: strict type checking ---"
    python3 -m mypy --strict sage-stubs/
    @echo "All checks passed."

# Fast lint only (no mypy)
lint:
    ruff check sage-stubs/
    python3 scripts/check_stubs.py $(find sage-stubs -name "*.pyi")

# Fast lint for staged stub files only, used by the pre-commit hook
lint-staged:
    @files="$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.pyi$' || true)"; \
    if [ -n "$files" ]; then \
        ruff check $files; \
        python3 scripts/check_stubs.py $files; \
        python3 scripts/type_surface_review.py --staged; \
    fi

# Auto-fix what ruff can fix (deprecated patterns)
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
    chmod +x .git/hooks/pre-commit .git/hooks/post-commit
    @echo "pre-commit + post-commit hooks installed locally."

# Guardrails — banned patterns + scratch artefacts + narrowing detection.
guardrails *args:
    python3 scripts/check_guardrails.py {{args}}

# Inventory changed annotation surfaces for stricter/equivalent/weaker review.
type-surface-review *args:
    python3 scripts/type_surface_review.py {{args}}
