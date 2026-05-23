#!/usr/bin/env python3
"""List staged or working-tree type-surface changes in Sage stub files.

This is a review inventory, not an approval tool. Every reported item still
needs a source-backed stricter/equivalent/weaker classification.

Known type-relaxation patterns fail by default so agents cannot silently trade
mathematical precision for local checker convenience.
"""

from __future__ import annotations

import argparse
import ast
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from stub_annotation_policy import is_allowed_object_parameter_surface

REPO_ROOT = Path(__file__).resolve().parent.parent
OTP_ENV_VAR = "SAGE_STUBS_TYPE_SURFACE_REVIEW_OTP"
OTP_MARKER = REPO_ROOT / ".git" / "sage-stubs-type-surface-review-otp"

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
BROAD_MATHEMATICAL_TYPES = {
    "Algebra",
    "CommutativeAlgebra",
    "CommutativeRing",
    "CommutativeRingElement",
    "Element",
    "Field",
    "FieldElement",
    "FreeModule",
    "Parent",
    "Matrix",
    "Module",
    "ModuleElement",
    "Ring",
    "RingElement",
    "SageObject",
    "FreeModule_generic",
}
GENERIC_TYPES = {
    "Callable",
    "ChainMap",
    "Collection",
    "Container",
    "Counter",
    "DefaultDict",
    "Deque",
    "FrozenSet",
    "Iterable",
    "Iterator",
    "Mapping",
    "MutableMapping",
    "MutableSequence",
    "MutableSet",
    "Sequence",
    "Set",
    "Type",
    "defaultdict",
    "dict",
    "frozenset",
    "list",
    "set",
    "tuple",
    "type",
}

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
    args: list[tuple[str, ast.arg]] = []
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

    def visit_body(body: list[ast.stmt], scope: tuple[str, ...]) -> None:
        for node in body:
            if isinstance(node, ast.ImportFrom) and node.module:
                if node.module == "typing" or any(
                    node.module == mod or node.module.startswith(f"{mod}.")
                    for mod in ANNOTATION_IMPORT_MODULES
                ):
                    names = ", ".join(alias.asname or alias.name for alias in node.names)
                    items.add(SurfaceItem("annotation-import", rel, node.module, names))
            elif isinstance(node, ast.ClassDef):
                qualname = ".".join((*scope, node.name))
                bases = ", ".join(unparse(base) for base in node.bases) or "<none>"
                items.add(SurfaceItem("class-bases", rel, qualname, bases))
                visit_body(node.body, (*scope, node.name))
            elif isinstance(node, ast.AnnAssign):
                target = ".".join((*scope, unparse(node.target)))
                items.add(
                    SurfaceItem(
                        "variable-annotation",
                        rel,
                        target,
                        unparse(node.annotation),
                    )
                )
            elif isinstance(node, ast.Assign):
                if _is_type_alias(node.value):
                    targets = ", ".join(".".join((*scope, unparse(target))) for target in node.targets)
                    items.add(SurfaceItem("type-alias", rel, targets, unparse(node.value)))
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                qualname = ".".join((*scope, node.name))
                items.add(SurfaceItem("return", rel, qualname, unparse(node.returns)))
                for name, arg in iter_args(node):
                    if arg.arg in {"self", "cls"} and arg.annotation is None:
                        continue
                    suffix = name.removeprefix(f"{node.name}.")
                    items.add(SurfaceItem("parameter", rel, f"{qualname}.{suffix}", unparse(arg.annotation)))

    visit_body(tree.body, ())

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
    violations: list[str]


def report_file(path: Path, staged: bool) -> SurfaceReport:
    return report_texts(path, head_text(path, staged), current_text(path, staged))


def report_texts(path: Path, before_text: str, after_text: str) -> SurfaceReport:
    before = collect(before_text, path)
    after = collect(after_text, path)
    abstraction_names = collect_local_abstraction_names(after_text)
    removed = sorted(before - after)
    added = sorted(after - before)
    lines: list[str] = []
    for item in removed:
        lines.append(f"- {item.format()}")
    for item in added:
        lines.append(f"+ {item.format()}")

    before_by_key = items_by_key(before)
    after_by_key = items_by_key(after)
    violations = []
    for key in sorted(before_by_key.keys() & after_by_key.keys()):
        previous_items = before_by_key[key]
        proposed_items = after_by_key[key]
        previous_values = {item.value for item in previous_items}
        for previous in previous_items:
            if previous.value in {item.value for item in proposed_items}:
                continue
            for proposed in proposed_items:
                if proposed.value in previous_values:
                    continue
                if is_allowed_protocol_widening(proposed, previous.value):
                    continue
                reason = relaxation_reason(
                    previous.value,
                    proposed.value,
                    proposed.kind,
                    abstraction_names,
                )
                if reason:
                    violations.append(
                        f"{proposed.path}: {proposed.kind} {proposed.name}: "
                        f"{previous.value} -> {proposed.value} ({reason})"
                    )
    return SurfaceReport(lines, violations)


def collect_local_abstraction_names(text: str) -> set[str]:
    """Return local TypeVar and Protocol symbols introduced by a stub file."""
    if not text.strip():
        return set()
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set()
    names: set[str] = set()
    for node in ast.walk(tree):
        targets: list[ast.expr]
        value: ast.AST | None
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
            value = node.value
        else:
            continue
        if not is_typevar_call(value):
            continue
        for target in targets:
            if isinstance(target, ast.Name):
                names.add(target.id)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and class_extends_protocol(node):
            names.add(node.name)
    return names


def is_typevar_call(node: ast.AST | None) -> bool:
    if not isinstance(node, ast.Call):
        return False
    func = node.func
    return (
        isinstance(func, ast.Name) and func.id == "TypeVar"
    ) or (
        isinstance(func, ast.Attribute) and func.attr == "TypeVar"
    )


def class_extends_protocol(node: ast.ClassDef) -> bool:
    return any("Protocol" in names_in_node(base) for base in node.bases)


def items_by_key(items: set[SurfaceItem]) -> dict[tuple[str, str, str], list[SurfaceItem]]:
    grouped: dict[tuple[str, str, str], list[SurfaceItem]] = {}
    for item in items:
        grouped.setdefault(item.key(), []).append(item)
    return grouped


def is_allowed_protocol_widening(item: SurfaceItem, previous: str) -> bool:
    """Permit Python-forced object parameters in named protocol slots only."""
    if item.kind != "parameter":
        return False
    if not is_allowed_object_parameter_surface(item.name):
        return False
    return proposed_is_exact_object(item.value) and previous not in {"<missing>", "<none>"}


def proposed_is_exact_object(value: str) -> bool:
    return value == "object"


def relaxation_reason(
    previous: str,
    proposed: str,
    kind: str,
    abstraction_names: set[str] | None = None,
) -> str | None:
    if kind == "annotation-import":
        return None
    if previous == proposed:
        return None
    abstraction_names = abstraction_names or set()
    previous_names = names_in_type(previous)
    proposed_names = names_in_type(proposed)
    if previous in {"<missing>", "<none>"}:
        return None
    if abstraction_laundering(previous_names, proposed_names, abstraction_names):
        return "existing type surface replaced by local generic/protocol abstraction without source proof"
    if previous_names & OPAQUE_TYPES and not proposed_names & OPAQUE_TYPES:
        return None

    if proposed_names & OPAQUE_TYPES:
        return "existing typed surface relaxed to opaque type"
    if callable_gained_ellipsis(previous, proposed):
        return "precise callable signature replaced by Callable ellipsis"
    if type_gained_parameters(previous, proposed):
        return None
    if lost_generic_parameters(previous, proposed):
        return "generic parameters removed from existing type surface"
    if union_collapsed_to_broad_type(previous, proposed):
        return "precise union replaced by broad placeholder"
    if relaxed_to_known_broad_math_type(previous_names, proposed_names):
        return "mathematical type relaxed to broader Sage/domain base"
    if class_base_relaxed(previous, proposed, kind):
        return "class base replaced with broader Sage/domain base"
    if class_base_changed_between_domain_types(previous, proposed, kind):
        return (
            "class base changed between Sage/domain types; review for "
            "local-checker reward-hacking and global hierarchy regression"
        )
    if sage_normalized_integer_spelling(previous_names, proposed_names):
        return None
    return None


def abstraction_laundering(
    previous_names: set[str],
    proposed_names: set[str],
    abstraction_names: set[str],
) -> bool:
    return bool(abstraction_names and proposed_names & abstraction_names and not previous_names & abstraction_names)


def callable_gained_ellipsis(previous: str, proposed: str) -> bool:
    return (
        "Callable" in names_in_type(previous)
        and "Callable" in names_in_type(proposed)
        and "..." not in previous
        and "..." in proposed
    )


def bare_container_base(value: str) -> str:
    for part in (part.strip() for part in value.split("|")):
        base = part.split("[", 1)[0].strip()
        if base in GENERIC_TYPES:
            return base
    return value.split("[", 1)[0].strip()


def sage_normalized_integer_spelling(previous_names: set[str], proposed_names: set[str]) -> bool:
    normalized_previous = (previous_names - {"int", "Integer"}) | (
        {"Integer"} if previous_names & {"int", "Integer"} else set()
    )
    normalized_proposed = (proposed_names - {"int", "Integer"}) | (
        {"Integer"} if proposed_names & {"int", "Integer"} else set()
    )
    return normalized_previous == normalized_proposed


def type_gained_parameters(previous: str, proposed: str) -> bool:
    return (
        bare_container_base(previous) == bare_container_base(proposed)
        and bare_container_base(previous) in GENERIC_TYPES
        and "[" not in previous
        and "[" in proposed
    )


def lost_generic_parameters(previous: str, proposed: str) -> bool:
    return (
        bare_container_base(previous) == bare_container_base(proposed)
        and bare_container_base(previous) in GENERIC_TYPES
        and "[" in previous
        and "[" not in proposed
    )


def union_collapsed_to_broad_type(previous: str, proposed: str) -> bool:
    if "|" not in previous:
        return False
    proposed_names = names_in_type(proposed)
    broad_names = OPAQUE_TYPES | BROAD_MATHEMATICAL_TYPES
    return bool(proposed_names & broad_names)


def relaxed_to_known_broad_math_type(previous_names: set[str], proposed_names: set[str]) -> bool:
    broad_added = proposed_names & BROAD_MATHEMATICAL_TYPES
    if not broad_added or broad_added <= previous_names:
        return False
    precise_removed = previous_names - proposed_names
    return bool(precise_removed)


def class_base_relaxed(previous: str, proposed: str, kind: str) -> bool:
    if kind != "class-bases":
        return False
    return relaxed_to_known_broad_math_type(names_in_type(previous), names_in_type(proposed))


def class_base_changed_between_domain_types(previous: str, proposed: str, kind: str) -> bool:
    if kind != "class-bases":
        return False
    return changed_between_sage_types(names_in_type(previous), names_in_type(proposed))


def changed_between_sage_types(previous_names: set[str], proposed_names: set[str]) -> bool:
    removed = previous_names - proposed_names
    added = proposed_names - previous_names
    if not removed or not added:
        return False
    return any(looks_like_domain_type(name) for name in removed | added)


def looks_like_domain_type(name: str) -> bool:
    if name in {"None", "Literal", "Self", "TypeVar", "Protocol"}:
        return False
    return "_" in name or name[:1].isupper()


def names_in_type(value: str) -> set[str]:
    try:
        tree = ast.parse(value)
    except SyntaxError:
        return {value}
    return {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}


def names_in_node(node: ast.AST) -> set[str]:
    names = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
    names.update(child.attr for child in ast.walk(node) if isinstance(child, ast.Attribute))
    return names


def demo_relaxation_cases() -> int:
    """Run one-off examples for the agent-hacking patterns this gate owns."""
    cases = [
        ("return", "VectorSpace", "FreeModule", True),
        ("return", "Matrix_integer_dense", "Matrix", True),
        ("return", "FiniteField", "Field", True),
        ("return", "Sequence[int]", "Sequence", True),
        ("return", "Callable[[int], str]", "Callable", True),
        ("return", "<missing>", "FiniteField", False),
        ("return", "Any", "FiniteField", False),
        ("parameter", "FiniteField", "object", True),
        ("parameter", "object", "Iterable[_T]", True),
        ("parameter", "Word_class", "_T", True),
        ("parameter", "object", "_SupportsWord", True),
        ("return", "Any", "Sequence[_T]", True),
        ("return", "Callable[[Integer], FiniteField]", "Callable[..., FiniteField]", True),
        (
            "class-bases",
            "ExactSubcategorySurface, SourceBackedSpecializedBase",
            "ExactSubcategorySurface, BroaderNearbyBase",
            True,
        ),
        ("parameter", "Word_class", "Word_class", False),
    ]
    failed = 0
    for kind, previous, proposed, should_flag in cases:
        reason = relaxation_reason(previous, proposed, kind, {"_T", "_SupportsWord"})
        flagged = reason is not None
        status = "ok" if flagged == should_flag else "FAIL"
        print(f"{status}: {kind} {previous} -> {proposed}: {reason or 'allowed'}")
        failed += int(flagged != should_flag)

    allowed_eq = SurfaceItem("parameter", "demo.pyi", "__eq__.other", "object")
    if is_allowed_protocol_widening(allowed_eq, "Self"):
        print("ok: parameter Self -> object allowed for __eq__.other")
    else:
        print("FAIL: parameter Self -> object should be allowed for __eq__.other")
        failed += 1

    before_text = """
from collections.abc import Callable, Iterable, Sequence

class Demo:
    def vector_space(self) -> VectorSpace: ...
    def matrix(self) -> Matrix_integer_dense: ...
    def finite_field(self) -> FiniteField: ...
    def words(self) -> Sequence[Word_class]: ...
    def callback(self) -> Callable[[Integer], FiniteField]: ...
    def variadic(self, *items: VectorSpace) -> None: ...
    def erased(self, x: object) -> None: ...
    def structural(self, x: Word_class) -> None: ...
    def newly_typed(self): ...
    def __contains__(self, x: FiniteField) -> bool: ...
    def __eq__(self, other: Self) -> bool: ...
"""
    after_text = """
from collections.abc import Callable, Iterable, Sequence
from typing import Protocol, TypeVar

_T = TypeVar("_T")

class _SupportsWord(Protocol):
    def string_rep(self) -> str: ...

class Demo:
    def vector_space(self) -> FreeModule: ...
    def matrix(self) -> Matrix: ...
    def finite_field(self) -> Field: ...
    def words(self) -> Sequence: ...
    def callback(self) -> Callable: ...
    def variadic(self, *items: FreeModule) -> None: ...
    def erased(self, x: Iterable[_T]) -> None: ...
    def structural(self, x: _SupportsWord) -> None: ...
    def newly_typed(self) -> FiniteField: ...
    def __contains__(self, x: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
"""
    report = report_texts(REPO_ROOT / "sage-stubs/demo_relaxation.pyi", before_text, after_text)
    expected_fragments = {
        "vector_space",
        "Matrix_integer_dense -> Matrix",
        "FiniteField -> Field",
        "words",
        "callback",
        "variadic.*items",
        "erased.x",
        "structural.x",
    }
    missing_fragments = {
        fragment
        for fragment in expected_fragments
        if not any(fragment in violation for violation in report.violations)
    }
    unexpected_fragments = {
        fragment
        for fragment in {"newly_typed", "__contains__.x", "__eq__.other"}
        if any(fragment in violation for violation in report.violations)
    }
    if missing_fragments or unexpected_fragments:
        print("FAIL: parsed diff demo did not match expected relaxation candidates")
        if missing_fragments:
            print(f"missing: {sorted(missing_fragments)}")
        if unexpected_fragments:
            print(f"unexpected: {sorted(unexpected_fragments)}")
        failed += 1
    else:
        print("ok: parsed diff demo flags relaxations and ignores new typing/protocol widening")
    return 1 if failed else 0


def use_otp_bypass(violations: list[str]) -> bool:
    token = os.environ.get(OTP_ENV_VAR, "").strip()
    if not token:
        return False
    if len(token) < 16 or any(ch.isspace() for ch in token):
        print(
            f"\n{OTP_ENV_VAR} is present but invalid. Use a one-time token with "
            "at least 16 non-whitespace characters.",
            file=sys.stderr,
        )
        return False
    OTP_MARKER.write_text(
        "\n".join([token, *violations, ""]),
        encoding="utf-8",
    )
    print(
        f"\nOTP bypass recorded for this commit attempt. The commit message must "
        f"include {OTP_ENV_VAR}={token} and a source-backed audit with these "
        "headings: Type-surface relaxation review, Source evidence, Why forced, "
        "Global regression risk, Reward-hacking/local-minimum check.\n"
        "The commit-msg hook will reject the commit if the token or audit headings "
        "are missing."
    )
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true", help="review staged diff")
    parser.add_argument("--files", nargs="*", help="explicit .pyi files")
    parser.add_argument(
        "--allow-high-risk",
        action="store_true",
        help="print high-risk widenings without failing",
    )
    parser.add_argument(
        "--demo-relaxation-cases",
        action="store_true",
        help="run contrived relaxation examples and exit",
    )
    args = parser.parse_args()

    if args.demo_relaxation_cases:
        return demo_relaxation_cases()

    files = selected_files(args.staged, args.files)
    if not files:
        print("type_surface_review: no changed .pyi files.")
        return 0

    had_items = False
    violations: list[str] = []
    for path in files:
        report = report_file(path, args.staged)
        if not report.lines:
            continue
        had_items = True
        print(f"\n# {path.relative_to(REPO_ROOT)}")
        for line in report.lines:
            print(line)
        violations.extend(report.violations)

    if not had_items:
        print("type_surface_review: no type-surface changes found.")
    else:
        print(
            "\nReview required: classify every item as stricter, equivalent, "
            "or weaker against Sage 10.7 source before staging or committing."
        )
    if violations:
        print("\nType-relaxation violation candidates detected:")
        for line in violations:
            print(f"! {line}")
        print(
            "\nRejected for agent review: this repo requires the most mathematically "
            "precise, tight type that remains correct, coherent, and consistent with "
            "the surrounding Sage stubs. Do not relax a type merely to pass tests, "
            "lint, mypy, imports, package registration, or another local checker.\n\n"
            "Stop and re-evaluate whether repo rules permit every listed relaxation. "
            "Do NOT modify this script to permit fewer violations; changes to this "
            "guardrail may only flag or detect more possible relaxations. If a "
            "widening is truly forced by Sage source, isolate that widening in a "
            "single commit with a detailed source-backed audit trail explaining why "
            "the previous type was wrong and why the replacement is the tightest "
            "coherent type available."
        )
        if not args.allow_high_risk:
            if use_otp_bypass(violations):
                return 0
            print(
                f"\nEmergency bypass: set a one-time {OTP_ENV_VAR} value and commit "
                "with the same token plus a source-backed review in the commit "
                "message. This is for forced widenings only, not checker convenience."
            )
            return 1
    elif OTP_MARKER.exists():
        OTP_MARKER.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
