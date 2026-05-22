#!/usr/bin/env python3
"""List staged or working-tree type-surface changes in Sage stub files.

This is a review inventory, not an approval tool. Every reported item still
needs a source-backed stricter/equivalent/weaker classification.
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


@dataclass(frozen=True, order=True)
class SurfaceItem:
    kind: str
    path: str
    name: str
    value: str

    def format(self) -> str:
        return f"{self.path}: {self.kind} {self.name}: {self.value}"


def git_output(args: list[str]) -> str:
    return subprocess.check_output(args, cwd=REPO_ROOT, text=True)


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


def report_file(path: Path, staged: bool) -> list[str]:
    before = collect(head_text(path, staged), path)
    after = collect(current_text(path, staged), path)
    removed = sorted(before - after)
    added = sorted(after - before)
    lines: list[str] = []
    for item in removed:
        lines.append(f"- {item.format()}")
    for item in added:
        lines.append(f"+ {item.format()}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true", help="review staged diff")
    parser.add_argument("--files", nargs="*", help="explicit .pyi files")
    args = parser.parse_args()

    files = selected_files(args.staged, args.files)
    if not files:
        print("type_surface_review: no changed .pyi files.")
        return 0

    had_items = False
    for path in files:
        lines = report_file(path, args.staged)
        if not lines:
            continue
        had_items = True
        print(f"\n# {path.relative_to(REPO_ROOT)}")
        for line in lines:
            print(line)

    if not had_items:
        print("type_surface_review: no type-surface changes found.")
    else:
        print(
            "\nReview required: classify every item as stricter, equivalent, "
            "or weaker against Sage 10.7 source before staging or committing."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
