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

# Install the pre-commit hook
install-hooks:
    cp scripts/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    @echo "pre-commit hook installed."
