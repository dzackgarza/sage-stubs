#!/usr/bin/env python3
"""Audit semantic quality debt in the Sage stub corpus.

This deliberately complements type checkers. Mypy and basedpyright can prove
that a stub file is internally well-formed while the public API is still
erased behind ``object`` or a fabricated placeholder. This audit records those
patterns explicitly and emits machine-readable JSON/SARIF reports.

The default is report-only. CI passes ``--fail-on warning`` so every known
quality weakness remains visible until it is removed.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Literal

Severity = Literal["error", "warning", "info"]

GENERATED_MARKER = "# Generated from the pinned Sage 10.7 source tree."
SEVERITY_RANK: dict[Severity, int] = {"info": 0, "warning": 1, "error": 2}
DOMAIN_PARAMETER_NAMES = {
    "R",
    "S",
    "K",
    "F",
    "ring",
    "base_ring",
    "field",
    "base_field",
    "parent",
    "category",
    "domain",
    "codomain",
}
AMBIGUOUS_INTEGER_NAMES = {"p", "q", "r"}
SCALAR_TYPES = {"int", "bool", "str", "float", "complex"}
ERASURE_TYPES = {"Any", "object", "_SageObject"}
ARITHMETIC_DUNDERS = {
    "__add__",
    "__radd__",
    "__sub__",
    "__rsub__",
    "__mul__",
    "__rmul__",
    "__matmul__",
    "__rmatmul__",
    "__truediv__",
    "__rtruediv__",
    "__floordiv__",
    "__rfloordiv__",
    "__mod__",
    "__rmod__",
    "__pow__",
    "__rpow__",
    "__and__",
    "__rand__",
    "__or__",
    "__ror__",
    "__xor__",
    "__rxor__",
    "__lshift__",
    "__rlshift__",
    "__rshift__",
    "__rrshift__",
}
KNOWN_BOILERPLATE_IMPORTS = {"_AsyncIterator", "_Iterable", "_Iterator", "Self"}
SUPPRESSION_PATTERNS = {
    "type-ignore": re.compile(r"#\s*type:\s*ignore"),
    "pyright-ignore": re.compile(r"#\s*pyright:\s*ignore"),
    "mypy-disable": re.compile(r"#\s*mypy:"),
    "noqa": re.compile(r"#\s*noqa"),
}


@dataclass(frozen=True, slots=True)
class Finding:
    rule_id: str
    severity: Severity
    path: str
    line: int
    column: int
    message: str


def dotted_name(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return None


def annotation_names(node: ast.expr | None) -> set[str]:
    if node is None:
        return set()
    names: set[str] = set()
    for child in ast.walk(node):
        name = dotted_name(child) if isinstance(child, (ast.Name, ast.Attribute)) else None
        if name:
            names.add(name)
            names.add(name.rsplit(".", 1)[-1])
    return names


def sentence_case(text: str) -> str:
    return text[:1].upper() + text[1:]


def annotation_text(node: ast.expr | None) -> str:
    if node is None:
        return "<missing>"
    try:
        return ast.unparse(node)
    except Exception:
        return "<unparseable>"


def is_ellipsis_statement(node: ast.stmt) -> bool:
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and node.value.value is Ellipsis
    )


def public_top_level_nodes(tree: ast.Module) -> list[ast.AST]:
    return [
        node
        for node in tree.body
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    ]


class StubAuditor:
    def __init__(self, path: Path, root: Path, text: str, tree: ast.Module) -> None:
        self.path = path
        self.root = root
        self.text = text
        self.tree = tree
        self.rel = str(path.relative_to(root.parent))
        self.generated = GENERATED_MARKER in text
        self.findings: list[Finding] = []
        self.imported_names: dict[str, int] = {}
        self.used_names: set[str] = set()

    def add(
        self,
        rule_id: str,
        severity: Severity,
        node: ast.AST | None,
        message: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> None:
        self.findings.append(
            Finding(
                rule_id=rule_id,
                severity=severity,
                path=self.rel,
                line=line if line is not None else getattr(node, "lineno", 1),
                column=column if column is not None else getattr(node, "col_offset", 0) + 1,
                message=message,
            )
        )

    def audit(self) -> list[Finding]:
        if self.generated:
            self.add(
                "generated-scaffold",
                "warning",
                None,
                "Module is still marked as an automatically generated scaffold; "
                "source-grounded review has not replaced it.",
                line=1,
                column=1,
            )

        for lineno, line in enumerate(self.text.splitlines(), start=1):
            for label, pattern in SUPPRESSION_PATTERNS.items():
                if pattern.search(line):
                    self.add(
                        f"local-suppression-{label}",
                        "error",
                        None,
                        "Local lint/type suppression hides a diagnostic instead of "
                        "resolving the stub.",
                        line=lineno,
                        column=1,
                    )

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.imported_names[alias.asname or alias.name] = node.lineno
                    if node.module == "typing" and alias.name == "Any":
                        self.add(
                            "explicit-any-import",
                            "error",
                            node,
                            "typing.Any is prohibited in the public stub surface.",
                        )
                    if node.module == "typing" and alias.name == "cast":
                        self.add(
                            "cast-suppression",
                            "error",
                            node,
                            "typing.cast in a stub conceals an unresolved annotation.",
                        )
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    self.imported_names[alias.asname or alias.name.split(".", 1)[0]] = node.lineno
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                self.used_names.add(node.id)

        for node in self.tree.body:
            if isinstance(node, ast.ClassDef):
                self.audit_class(node)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.audit_function(node)
            elif isinstance(node, ast.AnnAssign):
                self.audit_annotation(node.annotation, node, context="module variable")

        public_nodes = public_top_level_nodes(self.tree)
        if not public_nodes and self.path.name != "__init__.pyi":
            self.add(
                "empty-public-surface",
                "error" if self.generated else "warning",
                None,
                "Stub exposes no public class or function; module presence alone is "
                "not API coverage.",
                line=1,
                column=1,
            )

        if self.generated:
            for name in sorted(KNOWN_BOILERPLATE_IMPORTS):
                if name in self.imported_names and name not in self.used_names:
                    self.add(
                        "unused-generated-boilerplate",
                        "warning",
                        None,
                        f"Generated boilerplate import `{name}` is unused.",
                        line=self.imported_names[name],
                        column=1,
                    )

        return self.findings

    def audit_class(self, node: ast.ClassDef) -> None:
        if node.name == "_SageObject":
            self.add(
                "fabricated-sage-object",
                "error",
                node,
                "Local `_SageObject` is a fabricated nominal type unrelated to "
                "Sage's actual Parent/Element hierarchy.",
            )
        elif self.generated and not node.bases:
            self.add(
                "generated-class-without-bases",
                "warning",
                node,
                f"Generated class `{node.name}` drops the source inheritance graph.",
            )

        if node.name != "_SageObject" and all(
            isinstance(child, (ast.Pass, ast.Expr)) and
            (isinstance(child, ast.Pass) or is_ellipsis_statement(child))
            for child in node.body
        ):
            self.add(
                "empty-class-surface",
                "warning",
                node,
                f"Class `{node.name}` contains no typed public surface.",
            )

        for child in node.body:
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.audit_function(child)
            elif isinstance(child, ast.AnnAssign):
                self.audit_annotation(child.annotation, child, context="class attribute")

    def audit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        self.audit_annotation(
            node.returns,
            node,
            context=f"return type of `{node.name}`",
            allow_object=node.name == "__new__",
        )

        positional = [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
        for arg in positional:
            if arg.arg in {"self", "cls"}:
                continue
            self.audit_parameter(node, arg, variadic=False)

        if node.args.vararg is not None:
            self.audit_parameter(node, node.args.vararg, variadic=True)
        if node.args.kwarg is not None:
            self.audit_parameter(node, node.args.kwarg, variadic=True)

        if self.generated and node.name in ARITHMETIC_DUNDERS:
            if annotation_text(node.returns) == "Self":
                self.add(
                    "generated-arithmetic-self",
                    "warning",
                    node,
                    f"`{node.name}` was blanket-inferred as returning Self; arithmetic "
                    "in Sage frequently changes parent or result type and requires "
                    "source-grounded overloads.",
                )

    def audit_parameter(
        self,
        function: ast.FunctionDef | ast.AsyncFunctionDef,
        arg: ast.arg,
        *,
        variadic: bool,
    ) -> None:
        annotation = arg.annotation
        self.audit_annotation(
            annotation,
            arg,
            context=f"parameter `{arg.arg}` of `{function.name}`",
            allow_object=variadic,
        )
        names = annotation_names(annotation)
        scalar = names & SCALAR_TYPES
        if arg.arg in DOMAIN_PARAMETER_NAMES and scalar:
            self.add(
                "domain-parameter-as-scalar",
                "error",
                arg,
                f"Domain parameter `{arg.arg}` is typed as "
                f"`{annotation_text(annotation)}`; use the actual Sage domain type.",
            )
        elif (
            self.generated
            and arg.arg.lower() in AMBIGUOUS_INTEGER_NAMES
            and "int" in names
        ):
            self.add(
                "name-inferred-integer",
                "warning",
                arg,
                f"Generated parameter `{arg.arg}` was inferred as int from its name; "
                "verify it against the source rather than accepting the heuristic.",
            )

    def audit_annotation(
        self,
        annotation: ast.expr | None,
        node: ast.AST,
        *,
        context: str,
        allow_object: bool = False,
    ) -> None:
        if annotation is None:
            self.add(
                "missing-annotation",
                "error",
                node,
                f"Missing {context}.",
            )
            return

        names = annotation_names(annotation)
        text = annotation_text(annotation)

        if "Any" in names:
            self.add(
                "explicit-any",
                "error",
                node,
                f"{sentence_case(context)} contains Any: `{text}`.",
            )

        if "_SageObject" in names:
            self.add(
                "placeholder-sage-object-annotation",
                "error",
                node,
                f"{sentence_case(context)} uses fabricated `_SageObject`: `{text}`.",
            )

        object_names = {"object", "builtins.object"} & names
        if object_names and not allow_object:
            self.add(
                "opaque-object-annotation",
                "warning",
                node,
                f"{sentence_case(context)} is erased behind object: `{text}`.",
            )

        builtins_names = sorted(name for name in names if name.startswith("builtins."))
        if builtins_names:
            self.add(
                "verbose-builtins-annotation",
                "warning",
                node,
                f"{sentence_case(context)} uses generated `builtins.*` spellings "
                f"({', '.join(builtins_names)}), contrary to the repository contract.",
            )

        if isinstance(annotation, ast.Subscript):
            erased = names & ERASURE_TYPES
            if erased:
                self.add(
                    "erased-generic-argument",
                    "error",
                    node,
                    f"{sentence_case(context)} has an erased generic argument: `{text}`.",
                )


def audit_file(path: Path, root: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        return [
            Finding(
                rule_id="syntax-error",
                severity="error",
                path=str(path.relative_to(root.parent)),
                line=exc.lineno or 1,
                column=exc.offset or 1,
                message=exc.msg,
            )
        ]
    return StubAuditor(path, root, text, tree).audit()


def sarif_document(findings: list[Finding]) -> dict[str, object]:
    rules: dict[str, dict[str, object]] = {}
    for finding in findings:
        rules.setdefault(
            finding.rule_id,
            {
                "id": finding.rule_id,
                "name": finding.rule_id,
                "shortDescription": {"text": finding.message.split(".", 1)[0]},
                "defaultConfiguration": {
                    "level": {
                        "error": "error",
                        "warning": "warning",
                        "info": "note",
                    }[finding.severity]
                },
            },
        )

    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "sage-stubs-quality-audit",
                        "informationUri": "https://github.com/dzackgarza/sage-stubs",
                        "rules": list(rules.values()),
                    }
                },
                "results": [
                    {
                        "ruleId": finding.rule_id,
                        "level": {
                            "error": "error",
                            "warning": "warning",
                            "info": "note",
                        }[finding.severity],
                        "message": {"text": finding.message},
                        "locations": [
                            {
                                "physicalLocation": {
                                    "artifactLocation": {"uri": finding.path},
                                    "region": {
                                        "startLine": finding.line,
                                        "startColumn": max(1, finding.column),
                                    },
                                }
                            }
                        ],
                    }
                    for finding in findings
                ],
            }
        ],
    }


def write_json(path: Path, findings: list[Finding]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    summary = {
        "total": len(findings),
        "by_severity": dict(Counter(f.severity for f in findings)),
        "by_rule": dict(Counter(f.rule_id for f in findings)),
        "findings": [asdict(f) for f in findings],
    }
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def print_summary(findings: list[Finding], max_console: int) -> None:
    by_severity = Counter(f.severity for f in findings)
    by_rule = Counter(f.rule_id for f in findings)

    print(
        "stub-quality: "
        f"{len(findings)} finding(s) "
        f"({by_severity['error']} error, "
        f"{by_severity['warning']} warning, "
        f"{by_severity['info']} info)"
    )
    for rule_id, count in by_rule.most_common():
        print(f"  {rule_id}: {count}")

    if findings:
        print(f"\nFirst {min(max_console, len(findings))} finding(s):")
    for finding in findings[:max_console]:
        print(
            f"{finding.path}:{finding.line}:{finding.column}: "
            f"{finding.severity.upper()} {finding.rule_id}: {finding.message}"
        )
    if len(findings) > max_console:
        print(
            f"... {len(findings) - max_console} additional finding(s) omitted "
            "from console; see the JSON/SARIF artifacts."
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("sage-stubs"))
    parser.add_argument("--json", dest="json_path", type=Path)
    parser.add_argument("--sarif", dest="sarif_path", type=Path)
    parser.add_argument(
        "--fail-on",
        choices=("none", "info", "warning", "error"),
        default="none",
        help="lowest severity that makes the command fail",
    )
    parser.add_argument("--max-console", type=int, default=200)
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"stub root does not exist: {root}", file=sys.stderr)
        return 2

    findings = [
        finding
        for path in sorted(root.rglob("*.pyi"))
        for finding in audit_file(path, root)
    ]
    findings.sort(
        key=lambda finding: (
            -SEVERITY_RANK[finding.severity],
            finding.path,
            finding.line,
            finding.column,
            finding.rule_id,
        )
    )

    print_summary(findings, max(0, args.max_console))

    if args.json_path:
        write_json(args.json_path, findings)
    if args.sarif_path:
        args.sarif_path.parent.mkdir(parents=True, exist_ok=True)
        args.sarif_path.write_text(
            json.dumps(sarif_document(findings), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    if args.fail_on == "none":
        return 0
    threshold = {"info": 0, "warning": 1, "error": 2}[args.fail_on]
    return int(any(SEVERITY_RANK[finding.severity] >= threshold for finding in findings))


if __name__ == "__main__":
    raise SystemExit(main())
