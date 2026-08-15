#!/usr/bin/env python3
"""Populate every uncovered Sage 10.7 sidecar module from the pinned source."""
from __future__ import annotations

import sys
from pathlib import Path

from stubgen_common import HEADER, in_scope
from stubgen_cython import parse_cython
from stubgen_python import parse_python

ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / "sage-src" / "src" / "sage"
STUB_ROOT = ROOT / "sage-stubs"
GENERATED_LIST = Path("/tmp/sage-stubs-generated-files.txt")


def destination(source: Path) -> Path:
    return (STUB_ROOT / source.relative_to(SOURCE_ROOT)).with_suffix(".pyi")


def ensure_package(folder: Path, generated: list[Path]) -> None:
    while folder != STUB_ROOT and STUB_ROOT in folder.parents:
        for name in ("__init__.py", "__init__.pyi"):
            path = folder / name
            if not path.exists():
                path.write_text("", encoding="utf-8")
                generated.append(path)
        folder = folder.parent


def main() -> int:
    if not SOURCE_ROOT.is_dir() or not STUB_ROOT.is_dir():
        print(f"missing source or stub root: {SOURCE_ROOT} / {STUB_ROOT}", file=sys.stderr)
        return 2
    generated: list[Path] = []
    fallbacks: list[tuple[Path, Exception]] = []
    sources = sorted(path for path in SOURCE_ROOT.rglob("*") if path.is_file() and in_scope(path))
    for source in sources:
        target = destination(source)
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        ensure_package(target.parent, generated)
        try:
            content = parse_python(source) if source.suffix == ".py" else parse_cython(source)
        except (SyntaxError, ValueError, UnicodeError) as exc:
            content = HEADER
            fallbacks.append((source, exc))
        target.write_text(content, encoding="utf-8")
        generated.append(target)
    stubs = sorted({path for path in generated if path.suffix == ".pyi"})
    GENERATED_LIST.write_text("".join(f"{path.relative_to(ROOT)}\n" for path in stubs), encoding="utf-8")
    print(f"sources considered: {len(sources)}")
    print(f"new files: {len(set(generated))}")
    print(f"new stubs: {len(stubs)}")
    print(f"parser fallbacks: {len(fallbacks)}")
    for source, exc in fallbacks[:50]:
        print(f"  {source.relative_to(SOURCE_ROOT)}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
