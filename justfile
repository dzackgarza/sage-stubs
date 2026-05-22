# sage-stubs quality pipeline

# Full quality check — run before every commit
check:
    @echo "--- ruff: deprecated patterns + missing annotations ---"
    ruff check sage-stubs/
    @echo "--- custom: Any/object ban (what ruff can't enforce) ---"
    python3 scripts/check_stubs.py $(find sage-stubs -name "*.pyi")
    @echo "--- mypy: strict type checking ---"
    python3 -m mypy --strict sage-stubs/
    @echo "All checks passed."

# Fast lint only (no mypy)
lint:
    ruff check sage-stubs/
    python3 scripts/check_stubs.py $(find sage-stubs -name "*.pyi")

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

# Install the pre-commit hook
install-hooks:
    cp scripts/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    @echo "pre-commit hook installed."
