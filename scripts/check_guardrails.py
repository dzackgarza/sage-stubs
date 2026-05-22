#!/usr/bin/env python3
"""
Repo-wide guardrails. Enforces the AGENTS.md "Banned output patterns"
section against staged files (or, with --all, against the whole repo).

Checks:
  1. No scratch artifacts at repo root or anywhere outside /tmp:
       plan.md (only `.agents/plan.md` is allowed)
       test_*.py / generate_*.py / fix_*.py / extract_*.py
       *_inventory.* / *_methods.* / scratch_*.* in the repo
  2. No `TYPE_CHECKING` blocks in any `.pyi`.
  3. No `# type: ignore`, `# noqa`, or `cast(` in any `.pyi`.
  4. No `sage-stubs/sage/...` paths (nested layout is banned).
  5. No `typing.Any` / `typing.List` / `typing.Dict` / `typing.Optional`
     /`typing.Union` / `builtins.object` / `builtins.type` imports in
     `.pyi` (use modern PEP 604/585 form).
  6. No edits to lint, mypy, ruff, hook, or validation configuration
     (only `[tool.setuptools] packages` may be edited in `pyproject.toml`).
  7. No destructive narrowing: a staged `.pyi` may not REMOVE existing
     top-level `class` / `def` definitions that were present in the
     previous version (warning unless `--allow-narrow` is set, since
     legitimate corrections do exist).

Modes:
  default       — checks files staged for commit (git diff --cached)
  --all         — checks every file in the working tree
  --files A B…  — checks the given paths

Exit:
  0 = clean
  1 = at least one hard violation
  2 = staged-diff inspection requested but git is unavailable
"""

from __future__ import annotations

import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# ---- 1. scratch artefact filenames ---------------------------------------

SCRATCH_PATTERNS = [
    re.compile(r"^plan\.md$"),
    re.compile(r"^test_.*\.py$"),
    re.compile(r"^generate_.*\.py$"),
    re.compile(r"^fix_.*\.py$"),
    re.compile(r"^extract_.*\.py$"),
    re.compile(r".*_inventory\.(md|txt|json)$"),
    re.compile(r".*_methods\.(md|txt|json)$"),
    re.compile(r"^scratch_.*"),
]

# Top-level directories where scratch artefacts at any depth are forbidden.
# (We never block files under `sage-src/` or `sage-stubs/` legitimate paths.)
SCRATCH_BLOCK_DIRS = (".", "scripts", "sage-stubs")

# ---- 2 + 3 + 5. patterns in .pyi -----------------------------------------

PYI_FORBIDDEN_LINE_PATTERNS = {
    "TYPE_CHECKING": re.compile(r"\bTYPE_CHECKING\b"),
    "# type: ignore": re.compile(r"#\s*type:\s*ignore"),
    "# noqa": re.compile(r"#\s*noqa"),
    "cast(": re.compile(r"\bcast\s*\("),
    "from typing import Any": re.compile(
        r"^from\s+typing\s+import\s+.*\bAny\b", re.MULTILINE
    ),
    "typing.List/Dict/Optional/Union": re.compile(
        r"\btyping\.(List|Dict|Optional|Union|Tuple|Set|FrozenSet)\b"
    ),
    "builtins.object/type": re.compile(r"\bbuiltins\.(object|type)\b"),
}

# ---- 4. nested layout ----------------------------------------------------

NESTED_LAYOUT = re.compile(r"sage-stubs/sage/")

# ---- 6. config files we won't let agents edit ----------------------------

PROTECTED_CONFIG = {
    ".ruff.toml",
    "ruff.toml",
    "mypy.ini",
    ".mypy.ini",
    ".pre-commit-config.yaml",
    "scripts/check_stubs.py",
    "scripts/check_guardrails.py",
    "scripts/stub_coverage.py",
    ".githooks/pre-commit",
    ".githooks/post-commit",
    "justfile",
}

PYPROJECT_PROTECTED_KEYS = ("[tool.ruff", "[tool.mypy", "[build-system")


# --------------------------------------------------------------------------


def staged_files() -> list[Path] | None:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            cwd=REPO_ROOT,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return [REPO_ROOT / p for p in out.splitlines() if p]


def all_files() -> list[Path]:
    return [
        p for p in REPO_ROOT.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and "sage-src" not in p.parts
        and ".agents" not in p.parts
    ]


def check_scratch(path: Path, errors: list[str]) -> None:
    rel = path.relative_to(REPO_ROOT) if path.is_absolute() else path
    parts = rel.parts
    if not parts:
        return
    # Exempt: any file under sage-src/ or .agents/ or sage-stubs/ that's a legitimate stub.
    if parts[0] in {"sage-src", ".agents", ".git"}:
        return
    # The Phase-1 inventory output is allowed under .agents/phases/.
    name = rel.name
    if str(rel) == ".agents/plan.md":
        return
    for pat in SCRATCH_PATTERNS:
        if pat.match(name):
            errors.append(
                f"{rel}: scratch artefact filename. "
                f"Plans, inventories, and helper scripts belong under /tmp, "
                f"not in the repo."
            )
            return


def check_pyi(path: Path, errors: list[str]) -> None:
    if path.suffix != ".pyi":
        return
    try:
        text = path.read_text(encoding="utf-8")
    except (FileNotFoundError, UnicodeDecodeError):
        return
    rel = path.relative_to(REPO_ROOT) if path.is_absolute() else path
    for label, pat in PYI_FORBIDDEN_LINE_PATTERNS.items():
        if pat.search(text):
            errors.append(
                f"{rel}: contains forbidden pattern `{label}` — see AGENTS.md "
                f"Banned output patterns."
            )


def check_layout(path: Path, errors: list[str]) -> None:
    rel = str(path.relative_to(REPO_ROOT) if path.is_absolute() else path)
    if NESTED_LAYOUT.search(rel):
        errors.append(
            f"{rel}: nested `sage-stubs/sage/...` layout — stubs map "
            f"`sage-src/src/sage/X/Y.py` → `sage-stubs/X/Y.pyi`."
        )


def check_pyproject(staged: set[Path], errors: list[str]) -> None:
    pp = REPO_ROOT / "pyproject.toml"
    if pp not in staged or not pp.exists():
        return
    # Compare staged vs HEAD; reject any change in protected sections.
    try:
        head = subprocess.check_output(
            ["git", "show", "HEAD:pyproject.toml"],
            cwd=REPO_ROOT,
            text=True,
        )
    except subprocess.CalledProcessError:
        return  # initial commit; no HEAD to diff against
    current = pp.read_text(encoding="utf-8")
    for marker in PYPROJECT_PROTECTED_KEYS:
        if extract_section(head, marker) != extract_section(current, marker):
            errors.append(
                f"pyproject.toml: section starting with `{marker}` was "
                f"modified. Only `[tool.setuptools] packages` may be edited "
                f"by stub tasks."
            )


def extract_section(text: str, marker: str) -> str:
    """Return the slice of `text` from `marker` until the next `[` heading."""
    i = text.find(marker)
    if i == -1:
        return ""
    end = text.find("\n[", i + len(marker))
    return text[i:end] if end != -1 else text[i:]


def check_protected(staged: set[Path], errors: list[str]) -> None:
    for rel in PROTECTED_CONFIG:
        path = REPO_ROOT / rel
        if path in staged:
            errors.append(
                f"{rel}: protected configuration / tooling file. Stub work "
                f"must not edit lint, mypy, hook, or validation settings."
            )


def staged_pyi_diffs() -> dict[Path, str]:
    """Map staged .pyi path → previous (HEAD) content."""
    files = staged_files() or []
    out: dict[Path, str] = {}
    for path in files:
        if path.suffix != ".pyi" or not path.exists():
            continue
        try:
            head = subprocess.check_output(
                ["git", "show", f"HEAD:{path.relative_to(REPO_ROOT)}"],
                cwd=REPO_ROOT,
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            continue  # newly added
        out[path] = head
    return out


def top_level_names(text: str) -> set[str]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set()
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
    return names


def check_narrowing(allow: bool, errors: list[str], warnings: list[str]) -> None:
    if allow:
        return
    for path, head_text in staged_pyi_diffs().items():
        head_names = top_level_names(head_text)
        cur_names = top_level_names(path.read_text(encoding="utf-8"))
        removed = head_names - cur_names
        if removed:
            rel = path.relative_to(REPO_ROOT)
            warnings.append(
                f"{rel}: removes existing top-level definitions "
                f"{sorted(removed)}. Existing stubs must not be narrowed "
                f"unless source review proves the existing stub was wrong. "
                f"If this is intentional, re-run with --allow-narrow."
            )


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all", action="store_true",
                    help="check every file in the working tree, not just staged")
    ap.add_argument("--files", nargs="*",
                    help="explicit file list to check")
    ap.add_argument("--allow-narrow", action="store_true",
                    help="allow destructive narrowing of existing .pyi files")
    args = ap.parse_args()

    if args.files:
        files = [Path(p).resolve() for p in args.files]
    elif args.all:
        files = all_files()
    else:
        s = staged_files()
        if s is None:
            print("git unavailable; pass --all or --files", file=sys.stderr)
            return 2
        files = s

    errors: list[str] = []
    warnings: list[str] = []
    staged_set = set(files)

    for path in files:
        check_scratch(path, errors)
        check_pyi(path, errors)
        check_layout(path, errors)

    check_pyproject(staged_set, errors)
    check_protected(staged_set, errors)
    if not args.all and not args.files:
        check_narrowing(args.allow_narrow, errors, warnings)

    for w in warnings:
        print(f"WARN  {w}", file=sys.stderr)
    for e in errors:
        print(f"FAIL  {e}", file=sys.stderr)

    if errors:
        print(f"\n{len(errors)} guardrail violation(s).", file=sys.stderr)
        return 1
    if warnings:
        print(f"\n{len(warnings)} warning(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
