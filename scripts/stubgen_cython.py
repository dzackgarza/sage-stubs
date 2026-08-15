"""Line-oriented extraction of public Cython declarations."""
from __future__ import annotations

import re
from pathlib import Path

from stubgen_common import HEADER, public, return_from_name

CLASS_RE = re.compile(r"^(?P<indent>\s*)(?:(?:cdef|cpdef)\s+)?class\s+(?P<name>[A-Za-z_]\w*)")
DEF_RE = re.compile(r"^(?P<indent>\s*)(?:(?:cpdef|cdef|def)\s+|async\s+def\s+)(?P<head>[^(:=]+?)\s*\((?P<args>[^)]*)\)")
ASSIGN_RE = re.compile(r"^(?P<name>[A-Za-z_]\w*)\s*=")


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


def cy_signature(text: str, name: str) -> str:
    bits: list[str] = []
    for raw in split_args(text):
        raw = raw.strip()
        if not raw or raw in {"/", "*"}:
            continue
        star = "**" if raw.startswith("**") else "*" if raw.startswith("*") else ""
        raw = raw[len(star):]
        left, separator, _ = raw.partition("=")
        identifiers = re.findall(r"[A-Za-z_]\w*", left.split(":", 1)[0])
        if not identifiers:
            continue
        arg = identifiers[-1]
        annotation = "" if arg in {"self", "cls"} else ": object"
        bits.append(f"{star}{arg}{annotation}" + (" = ..." if separator else ""))
    return f"({', '.join(bits)}) -> {return_from_name(name)}"


def parse_cython(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="latin-1")
    lines: list[str] = []
    classes: list[tuple[int, str, list[str], set[str]]] = []
    top_seen: set[str] = set()

    def close_class() -> None:
        _, name, body, _ = classes.pop()
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
        class_match = CLASS_RE.match(line)
        if class_match:
            name = class_match.group("name")
            if public(name):
                classes.append((indent, name, [], set()))
            continue
        function_match = DEF_RE.match(line)
        if function_match:
            names = re.findall(r"[A-Za-z_]\w*", function_match.group("head"))
            if not names:
                continue
            name = names[-1]
            if classes and indent > classes[-1][0]:
                body, seen = classes[-1][2], classes[-1][3]
                if public(name, True) and name not in seen:
                    seen.add(name)
                    body.append(f"def {name}{cy_signature(function_match.group('args'), name)}: ...")
            elif indent == 0 and public(name) and name not in top_seen:
                top_seen.add(name)
                lines.append(f"def {name}{cy_signature(function_match.group('args'), name)}: ...\n")
            continue
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
