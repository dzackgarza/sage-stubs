"""Line-oriented extraction of public Cython declarations."""
from __future__ import annotations

import re
from pathlib import Path

from stubgen_common import COMPARE, HEADER, public, return_from_name

CLASS_RE = re.compile(r"^(?P<indent>\s*)(?:(?:cdef|cpdef)\s+)?class\s+(?P<name>[A-Za-z_]\w*)")
DEF_RE = re.compile(r"^(?P<indent>\s*)(?:(?:cpdef|cdef|def)\s+|async\s+def\s+)(?P<head>[^(:=]+?)\s*\((?P<args>[^)]*)\)")
ASSIGN_RE = re.compile(r"^(?P<name>[A-Za-z_]\w*)\s*=")
DECORATOR_RE = re.compile(r"^(?P<indent>\s*)@(?P<name>staticmethod|classmethod|property)\b")


def split_args(text: str) -> list[str]:
    out: list[str] = []
    buffer: list[str] = []
    level = 0
    for char in text:
        if char in "([{": level += 1
        elif char in ")]}": level = max(0, level - 1)
        if char == "," and level == 0:
            out.append("".join(buffer)); buffer = []
        else:
            buffer.append(char)
    if buffer:
        out.append("".join(buffer))
    return out


def cy_signature(text: str, name: str, *, kind: str | None = None, class_name: str | None = None) -> str:
    parsed: list[tuple[str, bool, str]] = []
    for raw in split_args(text):
        raw = raw.strip()
        if not raw or raw in {"/", "*"}:
            continue
        star = "**" if raw.startswith("**") else "*" if raw.startswith("*") else ""
        raw = raw[len(star):]
        left, separator, _ = raw.partition("=")
        identifiers = re.findall(r"[A-Za-z_]\w*", left.split(":", 1)[0])
        if identifiers:
            parsed.append((identifiers[-1], bool(separator), star))
    bits: list[str] = []
    receiver_index = 0 if kind in {"instance", "class"} and parsed else -1
    for index, (arg, has_default, star) in enumerate(parsed):
        if index == receiver_index and kind == "instance" and arg == "self":
            rendered = "self"
        elif index == receiver_index and kind == "class" and arg in {"cls", "self"}:
            rendered = arg
        else:
            first_value = index == receiver_index + 1 if receiver_index >= 0 else index == 0
            annotation = "builtins.object" if first_value and (name in COMPARE or name == "__contains__") else "builtins.object"
            rendered = f"{star}{arg}: {annotation}"
        if has_default:
            rendered += " = ..."
        bits.append(rendered)
    if kind == "instance" and not parsed:
        bits.insert(0, "self")
    elif kind == "class" and not parsed:
        bits.insert(0, "cls")
    result = return_from_name(name)
    if kind == "static" and result == "Self":
        result = class_name or "_SageObject"
    return f"({', '.join(bits)}) -> {result}"


def parse_cython(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="latin-1")
    lines: list[str] = []
    classes: list[tuple[int, str, list[str], set[str]]] = []
    top_seen: set[str] = set()
    pending_decorators: dict[int, list[str]] = {}

    def close_class() -> None:
        _, name, body, _ = classes.pop()
        if not name:
            return
        block = [f"class {name}:", *(["    " + item for item in body] or ["    ..."]), ""]
        if classes:
            classes[-1][2].extend(block)
        else:
            lines.extend(block)

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line:
            continue
        indent = len(line) - len(line.lstrip())
        while classes and indent <= classes[-1][0]:
            close_class()
        decorator_match = DECORATOR_RE.match(line)
        if decorator_match:
            pending_decorators.setdefault(indent, []).append(decorator_match.group("name"))
            continue
        class_match = CLASS_RE.match(line)
        if class_match:
            name = class_match.group("name")
            if public(name):
                seen = classes[-1][3] if classes and indent > classes[-1][0] else top_seen
                if name in seen:
                    classes.append((indent, "", [], set()))
                else:
                    seen.add(name)
                    classes.append((indent, name, [], set()))
            pending_decorators.pop(indent, None)
            continue
        function_match = DEF_RE.match(line)
        if function_match:
            names = re.findall(r"[A-Za-z_]\w*", function_match.group("head"))
            if not names:
                pending_decorators.pop(indent, None)
                continue
            name = names[-1]
            decorator_names = pending_decorators.pop(indent, [])
            kind = "static" if "staticmethod" in decorator_names else "class" if "classmethod" in decorator_names or name == "__new__" else "instance"
            if classes and indent > classes[-1][0]:
                class_name, body, seen = classes[-1][1], classes[-1][2], classes[-1][3]
                if class_name and public(name, True) and name not in seen:
                    seen.add(name)
                    body.extend(f"@{decorator}" for decorator in decorator_names)
                    body.append(f"def {name}{cy_signature(function_match.group('args'), name, kind=kind, class_name=class_name)}: ...")
            elif indent == 0 and public(name) and name not in top_seen:
                top_seen.add(name)
                lines.extend(f"@{decorator}" for decorator in decorator_names)
                lines.append(f"def {name}{cy_signature(function_match.group('args'), name)}: ...\n")
            continue
        pending_decorators.pop(indent, None)
        if indent == 0:
            assignment = ASSIGN_RE.match(line)
            if assignment:
                name = assignment.group("name")
                if public(name) and name != "__all__" and name not in top_seen:
                    top_seen.add(name)
                    lines.append(f"{name}: _SageObject")
    while classes:
        close_class()
    return HEADER + ("\n".join(lines).rstrip() + "\n" if lines else "")
