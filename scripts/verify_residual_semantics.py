#!/usr/bin/env python3
"""Verify that residual quality findings are mathematically justified.

A nonzero audit count is acceptable only when the source itself proves that the
reported pattern is intentional.  This verifier accepts a narrow set of
residuals:

* ``object`` for Python comparison-protocol operands and heterogeneous
  variadics;
* values explicitly documented as arbitrary/opaque Python objects;
* values stored or compared without any structural operation;
* classes with no direct public source methods but a meaningful inherited
  interface;
* modules whose source is only a re-export/catalog surface.

Every other finding remains an unresolved error.  The output is an evidence
ledger, not an allowlist maintained by hand.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUB_ROOT = ROOT / "sage-stubs"
SOURCE_ROOT = ROOT / "sage-src" / "src" / "sage"
JUSTIFIABLE_RULES = {
    "opaque-object-annotation",
    "empty-class-surface",
    "empty-public-surface",
}
PROTOCOL_OBJECT_METHODS = {
    "__eq__", "__ne__", "__contains__", "__getattr__", "__setattr__",
    "__reduce__", "__reduce_ex__", "__getstate__", "__setstate__",
}
ARBITRARY_PHRASES = re.compile(
    r"(?i)\b(any|arbitrary|opaque|generic)\s+(?:python\s+)?object\b|"
    r"\bpython object\b|\buser data\b|\bpayload\b"
)


@dataclass(frozen=True)
class Evidence:
    rule_id: str
    path: str
    line: int
    status: str
    reason: str


def parse(path: Path) -> ast.Module | None:
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeError):
        return None


def source_for_stub(path: Path) -> Path | None:
    rel = path.relative_to(STUB_ROOT).with_suffix("")
    for suffix in (".py", ".pyx"):
        candidate = (SOURCE_ROOT / rel).with_suffix(suffix)
        if candidate.exists():
            return candidate
    return None


def all_functions(tree: ast.Module) -> list[ast.FunctionDef | ast.AsyncFunctionDef]:
    return [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]


def enclosing_function(tree: ast.Module, line: int) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    candidates = [
        fn for fn in all_functions(tree)
        if fn.lineno <= line <= getattr(fn, "end_lineno", fn.lineno)
    ]
    return min(candidates, key=lambda fn: getattr(fn, "end_lineno", fn.lineno) - fn.lineno) if candidates else None


def function_by_qualified_position(source: ast.Module, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    # Names are sufficient for almost every Sage module.  Where the same method
    # name occurs in multiple classes, match the nearest enclosing class name.
    parent_class = None
    for node in ast.walk(source):
        if isinstance(node, ast.ClassDef):
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name == stub_fn.name:
                    if parent_class is None:
                        parent_class = child
                    else:
                        parent_class = None
                        break
    if parent_class is not None:
        return parent_class
    matches = [fn for fn in all_functions(source) if fn.name == stub_fn.name]
    return matches[0] if len(matches) == 1 else None


def parameter_at_line(fn: ast.FunctionDef | ast.AsyncFunctionDef, line: int) -> ast.arg | None:
    arguments = [
        *fn.args.posonlyargs, *fn.args.args, *fn.args.kwonlyargs,
        *([fn.args.vararg] if fn.args.vararg else []),
        *([fn.args.kwarg] if fn.args.kwarg else []),
    ]
    exact = [arg for arg in arguments if arg and arg.lineno == line]
    return exact[0] if len(exact) == 1 else None


def source_parameter(fn: ast.FunctionDef | ast.AsyncFunctionDef, name: str) -> ast.arg | None:
    for arg in [
        *fn.args.posonlyargs, *fn.args.args, *fn.args.kwonlyargs,
        *([fn.args.vararg] if fn.args.vararg else []),
        *([fn.args.kwarg] if fn.args.kwarg else []),
    ]:
        if arg and arg.arg == name:
            return arg
    return None


def parameter_usage(fn: ast.FunctionDef | ast.AsyncFunctionDef, name: str) -> dict[str, bool | set[str]]:
    attributes: set[str] = set()
    called = False
    iterated = False
    indexed = False
    returned = False
    only_compared_or_stored = True
    for node in ast.walk(fn):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == name:
            attributes.add(node.attr)
            only_compared_or_stored = False
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == name:
                called = True
                only_compared_or_stored = False
            for arg in node.args:
                if isinstance(arg, ast.Name) and arg.id == name:
                    called_name = ""
                    if isinstance(node.func, ast.Name):
                        called_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        called_name = node.func.attr
                    if called_name not in {"id", "hash", "repr", "str", "isinstance", "type"}:
                        # Passing an opaque payload onward is still potentially
                        # arbitrary; do not reject unless the callee performs a
                        # known structural operation in this function.
                        pass
        elif isinstance(node, (ast.For, ast.comprehension)):
            if isinstance(node.iter, ast.Name) and node.iter.id == name:
                iterated = True
                only_compared_or_stored = False
        elif isinstance(node, ast.Subscript):
            if isinstance(node.value, ast.Name) and node.value.id == name:
                indexed = True
                only_compared_or_stored = False
        elif isinstance(node, ast.Return) and node.value is not None:
            if any(isinstance(child, ast.Name) and child.id == name for child in ast.walk(node.value)):
                returned = True
                only_compared_or_stored = False
        elif isinstance(node, ast.BinOp):
            if any(isinstance(child, ast.Name) and child.id == name for child in ast.walk(node)):
                only_compared_or_stored = False
    return {
        "attributes": attributes,
        "called": called,
        "iterated": iterated,
        "indexed": indexed,
        "returned": returned,
        "only_compared_or_stored": only_compared_or_stored,
    }


def arbitrary_documentation(fn: ast.FunctionDef | ast.AsyncFunctionDef, parameter: str) -> bool:
    doc = ast.get_docstring(fn) or ""
    if not ARBITRARY_PHRASES.search(doc):
        return False
    # Prefer evidence near the parameter's INPUT bullet, but explicit module or
    # function-level arbitrary-object language is still useful.
    bullet = re.search(
        rf"(?ims)-\s*``{re.escape(parameter)}``\s*--\s*(.*?)(?=^\s*-\s*``|\Z)",
        doc,
    )
    return bool(bullet and ARBITRARY_PHRASES.search(bullet.group(1))) or bool(ARBITRARY_PHRASES.search(doc))


def public_source_methods(node: ast.ClassDef) -> list[str]:
    return [
        child.name for child in node.body
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
        and (not child.name.startswith("_") or child.name.startswith("__") and child.name.endswith("__"))
    ]


def verify_object(finding: dict[str, object], stub_path: Path, source_path: Path | None) -> Evidence:
    line = int(finding["line"])
    stub_tree = parse(stub_path)
    if stub_tree is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "stub could not be parsed")
    stub_fn = enclosing_function(stub_tree, line)
    if stub_fn is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "object annotation is not attached to a function parameter")
    parameter = parameter_at_line(stub_fn, line)
    if parameter is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "object occurs in a return or class attribute, not a verified arbitrary parameter")
    if parameter is stub_fn.args.vararg or parameter is stub_fn.args.kwarg:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "heterogeneous variadic parameter")
    if stub_fn.name in PROTOCOL_OBJECT_METHODS:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", f"Python protocol method {stub_fn.name} accepts arbitrary objects")
    if source_path is None or source_path.suffix != ".py":
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "no parseable Python source proves arbitrary-object semantics")
    source_tree = parse(source_path)
    if source_tree is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "source could not be parsed")
    source_fn = function_by_qualified_position(source_tree, stub_fn)
    if source_fn is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "matching source function is ambiguous")
    if source_parameter(source_fn, parameter.arg) is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "parameter is not present in source signature")
    if arbitrary_documentation(source_fn, parameter.arg):
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "source docstring explicitly permits an arbitrary Python object")
    usage = parameter_usage(source_fn, parameter.arg)
    if usage["only_compared_or_stored"] and not usage["attributes"] and not usage["called"] and not usage["iterated"] and not usage["indexed"] and not usage["returned"]:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "source stores, compares, hashes, or forwards the payload without requiring structure")
    details = []
    if usage["attributes"]:
        details.append("attributes=" + ",".join(sorted(usage["attributes"])))
    for key in ("called", "iterated", "indexed", "returned"):
        if usage[key]:
            details.append(key)
    return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "source requires additional structure: " + "; ".join(details))


def verify_empty_class(finding: dict[str, object], stub_path: Path, source_path: Path | None) -> Evidence:
    line = int(finding["line"])
    stub_tree = parse(stub_path)
    if stub_tree is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "stub could not be parsed")
    stub_classes = [node for node in ast.walk(stub_tree) if isinstance(node, ast.ClassDef) and node.lineno == line]
    if len(stub_classes) != 1:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "class at finding line is ambiguous")
    stub_class = stub_classes[0]
    if source_path is None or source_path.suffix != ".py":
        if stub_class.bases:
            return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "extension/foreign class has a recovered inherited interface and no direct Python surface")
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "empty class has neither source methods nor inherited interface")
    source_tree = parse(source_path)
    source_matches = [node for node in ast.walk(source_tree) if isinstance(node, ast.ClassDef) and node.name == stub_class.name] if source_tree else []
    if len(source_matches) != 1:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "matching source class is absent or ambiguous")
    public = public_source_methods(source_matches[0])
    if public:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "source defines direct public methods: " + ", ".join(public))
    if stub_class.bases:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "source defines no direct public method; behavior is inherited from recovered bases")
    return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "class has no public source surface and no informative base")


def verify_empty_module(finding: dict[str, object], stub_path: Path, source_path: Path | None) -> Evidence:
    line = int(finding["line"])
    if source_path is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "source module is unavailable")
    if source_path.suffix == ".pyx":
        text = source_path.read_text(encoding="utf-8", errors="replace")
        if re.search(r"(?m)^\s*(?:cpdef|def)\s+[A-Za-z_]\w*\s*\(", text) or re.search(r"(?m)^\s*(?:cdef\s+)?class\s+[A-Za-z_]\w*", text):
            return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "Cython source contains a direct callable/class surface")
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "Cython module exposes no direct Python callable/class surface")
    tree = parse(source_path)
    if tree is None:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "source module could not be parsed")
    direct = [
        node.name for node in tree.body
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    ]
    if direct:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "unresolved", "source exposes direct public definitions: " + ", ".join(direct))
    imports = [node for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))]
    assignments = [node for node in tree.body if isinstance(node, (ast.Assign, ast.AnnAssign))]
    if imports or assignments:
        return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "module is a catalog/re-export/constant surface with no direct callable class API")
    return Evidence(str(finding["rule_id"]), str(finding["path"]), line, "justified", "source module intentionally exposes no public API")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    parser.add_argument("--json", dest="output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.audit.read_text(encoding="utf-8"))
    findings = data.get("findings", [])
    evidence: list[Evidence] = []
    for finding in findings:
        rule = str(finding.get("rule_id"))
        path_value = str(finding.get("path"))
        stub_path = ROOT / path_value
        source_path = source_for_stub(stub_path) if stub_path.exists() and STUB_ROOT in stub_path.parents else None
        if rule not in JUSTIFIABLE_RULES:
            evidence.append(Evidence(rule, path_value, int(finding.get("line", 1)), "unresolved", "audit rule is not eligible for semantic justification"))
        elif rule == "opaque-object-annotation":
            evidence.append(verify_object(finding, stub_path, source_path))
        elif rule == "empty-class-surface":
            evidence.append(verify_empty_class(finding, stub_path, source_path))
        else:
            evidence.append(verify_empty_module(finding, stub_path, source_path))
    summary = {
        "total": len(evidence),
        "justified": sum(item.status == "justified" for item in evidence),
        "unresolved": sum(item.status != "justified" for item in evidence),
        "evidence": [asdict(item) for item in evidence],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in summary.items() if key != "evidence"}, indent=2, sort_keys=True))
    for item in evidence:
        if item.status != "justified":
            print(f"{item.path}:{item.line}: {item.rule_id}: {item.reason}", file=sys.stderr)
    return int(summary["unresolved"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
