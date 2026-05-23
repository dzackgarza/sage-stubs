#!/usr/bin/env python3
"""List staged or working-tree type-surface changes in Sage stub files.

This is a review inventory, not an approval tool. Every reported item still
needs a source-backed stricter/equivalent/weaker classification.

High-risk widenings fail by default so they cannot be accepted accidentally.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

ANNOTATION_IMPORT_MODULES = {
    "typing",
    "collections.abc",
    "sage.categories",
    "sage.combinat",
    "sage.groups",
    "sage.libs",
    "sage.manifolds",
    "sage.matrix",
    "sage.misc",
    "sage.modules",
    "sage.rings",
    "sage.schemes",
    "sage.sets",
    "sage.structure",
    "sage.symbolic",
}

OPAQUE_TYPES = {"Any", "object"}
BROAD_SAGE_TYPES = {
    "Element",
    "Parent",
    "SageObject",
    "FreeModule_generic",
    "RingElement",
    "CommutativeRingElement",
}
CONTAINER_TYPES = {"list", "dict", "tuple", "set", "frozenset"}


@dataclass(frozen=True, order=True)
class SurfaceItem:
    kind: str
    path: str
    name: str
    value: str

    def format(self) -> str:
        return f"{self.path}: {self.kind} {self.name}: {self.value}"

    def key(self) -> tuple[str, str, str]:
        return (self.kind, self.path, self.name)


def git_output(args: list[str]) -> str:
    return subprocess.check_output(args, cwd=REPO_ROOT, stderr=subprocess.DEVNULL, text=True)


def selected_files(staged: bool, files: list[str] | None) -> list[Path]:
    if files:
        return [Path(p).resolve() for p in files if p.endswith(".pyi")]

    diff_args = ["git", "diff", "--name-only", "--diff-filter=ACMR"]
    if staged:
        diff_args.insert(2, "--cached")
    return [
        REPO_ROOT / line
        for line in git_output(diff_args).splitlines()
        if line.endswith(".pyi")
    ]


def head_text(path: Path, staged: bool) -> str:
    rel = path.relative_to(REPO_ROOT)
    spec = f"HEAD:{rel}"
    try:
        if staged:
            return git_output(["git", "show", spec])
        return git_output(["git", "show", spec])
    except subprocess.CalledProcessError:
        return ""


def current_text(path: Path, staged: bool) -> str:
    rel = path.relative_to(REPO_ROOT)
    if staged:
        try:
            return git_output(["git", "show", f":{rel}"])
        except subprocess.CalledProcessError:
            return ""
    return path.read_text(encoding="utf-8") if path.exists() else ""


def unparse(node: ast.AST | None) -> str:
    return ast.unparse(node) if node is not None else "<missing>"


def arg_name(prefix: str, arg: ast.arg) -> str:
    return f"{prefix}.{arg.arg}"


def iter_args(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> list[tuple[str, ast.arg]]:
    args = []
    args.extend((arg_name(fn.name, a), a) for a in fn.args.posonlyargs)
    args.extend((arg_name(fn.name, a), a) for a in fn.args.args)
    if fn.args.vararg:
        args.append((f"{fn.name}.*{fn.args.vararg.arg}", fn.args.vararg))
    args.extend((arg_name(fn.name, a), a) for a in fn.args.kwonlyargs)
    if fn.args.kwarg:
        args.append((f"{fn.name}.**{fn.args.kwarg.arg}", fn.args.kwarg))
    return args


def collect(text: str, path: Path) -> set[SurfaceItem]:
    if not text.strip():
        return set()
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        rel = str(path.relative_to(REPO_ROOT))
        return {SurfaceItem("syntax-error", rel, str(exc.lineno), exc.msg)}

    rel = str(path.relative_to(REPO_ROOT))
    items: set[SurfaceItem] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module == "typing" or any(
                node.module == mod or node.module.startswith(f"{mod}.")
                for mod in ANNOTATION_IMPORT_MODULES
            ):
                names = ", ".join(alias.asname or alias.name for alias in node.names)
                items.add(SurfaceItem("annotation-import", rel, node.module, names))
        elif isinstance(node, ast.ClassDef):
            bases = ", ".join(unparse(base) for base in node.bases) or "<none>"
            items.add(SurfaceItem("class-bases", rel, node.name, bases))
        elif isinstance(node, ast.AnnAssign):
            items.add(
                SurfaceItem(
                    "variable-annotation",
                    rel,
                    unparse(node.target),
                    unparse(node.annotation),
                )
            )
        elif isinstance(node, ast.Assign):
            if _is_type_alias(node.value):
                targets = ", ".join(unparse(target) for target in node.targets)
                items.add(SurfaceItem("type-alias", rel, targets, unparse(node.value)))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            items.add(SurfaceItem("return", rel, node.name, unparse(node.returns)))
            for name, arg in iter_args(node):
                if arg.arg in {"self", "cls"} and arg.annotation is None:
                    continue
                items.add(SurfaceItem("parameter", rel, name, unparse(arg.annotation)))

    return items


def _is_type_alias(node: ast.AST) -> bool:
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return True
    if isinstance(node, ast.Subscript):
        return True
    if isinstance(node, ast.Name):
        return node.id in {"TypeAlias", "Protocol", "Self"}
    return False


@dataclass(frozen=True)
class SurfaceReport:
    lines: list[str]
    high_risk: list[str]


def report_file(path: Path, staged: bool) -> SurfaceReport:
    before = collect(head_text(path, staged), path)
    after = collect(current_text(path, staged), path)
    removed = sorted(before - after)
    added = sorted(after - before)
    lines: list[str] = []
    for item in removed:
        lines.append(f"- {item.format()}")
    for item in added:
        lines.append(f"+ {item.format()}")

    before_by_key = {item.key(): item for item in before}
    after_by_key = {item.key(): item for item in after}
    high_risk = []
    for key in sorted(before_by_key.keys() & after_by_key.keys()):
        previous = before_by_key[key]
        proposed = after_by_key[key]
        if proposed.kind == "parameter" and proposed.name in {
            "__eq__.other",
            "__ne__.other",
        }:
            continue
        if proposed.kind == "parameter" and (".*" in proposed.name or ".**" in proposed.name):
            continue
        reason = high_risk_reason(previous.value, proposed.value)
        if reason:
            high_risk.append(
                f"{proposed.path}: {proposed.kind} {proposed.name}: "
                f"{previous.value} -> {proposed.value} ({reason})"
            )
    return SurfaceReport(lines, high_risk)


def high_risk_reason(previous: str, proposed: str) -> str | None:
    if previous == proposed:
        return None
    previous_names = names_in_type(previous)
    proposed_names = names_in_type(proposed)
    if proposed_names & OPAQUE_TYPES:
        return "new opaque type"
    previous_base = bare_container_base(previous)
    proposed_base = bare_container_base(proposed)
    if previous in {"<missing>", "<none>"}:
        return None
    if previous_names & OPAQUE_TYPES and not proposed_names & OPAQUE_TYPES:
        return None
    if (
        previous_base == proposed_base
        and previous_base in CONTAINER_TYPES
        and "[" not in previous
        and "[" in proposed
    ):
        return None
    if (
        previous_base in CONTAINER_TYPES
        and "[" not in previous
        and proposed_names & CONTAINER_TYPES
    ):
        return None
    broad_added = proposed_names & BROAD_SAGE_TYPES
    if broad_added and not broad_added <= previous_names:
        return "broader Sage base introduced"
    if (
        previous_base == proposed_base
        and previous_base in CONTAINER_TYPES
        and "[" in previous
        and "[" not in proposed
    ):
        return "parameterized container became unparameterized"
    if "|" in previous and proposed in OPAQUE_TYPES | BROAD_SAGE_TYPES:
        return "precise union replaced by broad placeholder"
    return None


def bare_container_base(value: str) -> str:
    for part in (part.strip() for part in value.split("|")):
        base = part.split("[", 1)[0].strip()
        if base in CONTAINER_TYPES:
            return base
    return value.split("[", 1)[0].strip()


def names_in_type(value: str) -> set[str]:
    try:
        tree = ast.parse(value)
    except SyntaxError:
        return {value}
    return {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true", help="review staged diff")
    parser.add_argument("--files", nargs="*", help="explicit .pyi files")
    parser.add_argument(
        "--allow-high-risk",
        action="store_true",
        help="print high-risk widenings without failing",
    )
    args = parser.parse_args()

    files = selected_files(args.staged, args.files)
    if not files:
        print("type_surface_review: no changed .pyi files.")
        return 0

    had_items = False
    high_risk: list[str] = []
    for path in files:
        report = report_file(path, args.staged)
        if not report.lines:
            continue
        had_items = True
        print(f"\n# {path.relative_to(REPO_ROOT)}")
        for line in report.lines:
            print(line)
        high_risk.extend(report.high_risk)

    if not had_items:
        print("type_surface_review: no type-surface changes found.")
    else:
        print(
            "\nReview required: classify every item as stricter, equivalent, "
            "or weaker against Sage 10.7 source before staging or committing."
        )
    if high_risk:
        print("\nHigh-risk broadening detected:")
        for line in high_risk:
            print(f"! {line}")
        print(
            "\nRejected: remove the broadening or cite source proof and rerun "
            "with --allow-high-risk for a local audit only. Pre-commit must not "
            "accept unresolved high-risk weakening."
        )
        if not args.allow_high_risk:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
