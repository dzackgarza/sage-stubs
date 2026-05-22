#!/usr/bin/env python3
"""
Measure sage-stubs coverage against the sage-src submodule.

Walks sage-src/src/sage/ to enumerate in-scope source modules (.py / .pyx),
walks sage-stubs/ to enumerate existing .pyi stubs, and reports per-subpackage
and overall coverage. Honours an exempt list checked into
.agents/phases/phase-01-exempt.md (or any file passed via --exempt) so
modules listed there are excluded from the denominator.

In-scope source filter (mirrors .agents/feature.md):
  - Suffix .py or .pyx
  - NOT all.py / all_cmdline.py / all_test.py / __init__.py
  - NOT *_test.py / tests.py / test_*.py
  - NOT .pxd / .pxi / .h

Usage:
  scripts/stub_coverage.py                 # summary table to stdout
  scripts/stub_coverage.py --json          # machine-readable JSON
  scripts/stub_coverage.py --missing       # list missing files instead
  scripts/stub_coverage.py --subpackage rings --missing
  scripts/stub_coverage.py --exempt path/to/exempt.md
  scripts/stub_coverage.py --threshold 0.95  # exit 1 if overall < 95%

Exit code:
  0 = success (and threshold met if --threshold given)
  1 = threshold not met, or sage-src missing
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SAGE_SRC = REPO_ROOT / "sage-src" / "src" / "sage"
SAGE_STUBS = REPO_ROOT / "sage-stubs"

EXCLUDED_BASENAMES = {
    "all.py",
    "all_cmdline.py",
    "all_test.py",
    "__init__.py",
    "tests.py",
}

EXCLUDED_SUFFIXES = (".pxd", ".pxi", ".h", ".c", ".pyx.in", ".pxd.in")


def is_in_scope(path: Path) -> bool:
    """True if this source file should have a matching .pyi."""
    name = path.name
    if name in EXCLUDED_BASENAMES:
        return False
    if name.startswith("test_") and name.endswith(".py"):
        return False
    if name.endswith("_test.py"):
        return False
    if name.endswith(EXCLUDED_SUFFIXES):
        return False
    return name.endswith(".py") or name.endswith(".pyx")


def module_key(path: Path, root: Path) -> str:
    """Return a stub-relative key like 'rings/polynomial/polynomial_ring'."""
    rel = path.relative_to(root)
    stem = rel.with_suffix("")
    return str(stem)


def enumerate_sources(root: Path) -> set[str]:
    return {
        module_key(p, root)
        for p in root.rglob("*")
        if p.is_file() and is_in_scope(p)
    }


def enumerate_stubs(root: Path) -> set[str]:
    return {
        module_key(p, root)
        for p in root.rglob("*.pyi")
        if p.name != "__init__.pyi"
    }


# Match bullet lines like  `- rings/polynomial/foo`  or  `* foo/bar — reason`
EXEMPT_LINE = re.compile(r"^\s*[-*]\s+`?([\w/]+)`?")


def load_exempt(exempt_paths: list[Path]) -> set[str]:
    exempt: set[str] = set()
    for path in exempt_paths:
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            m = EXEMPT_LINE.match(raw)
            if not m:
                continue
            key = m.group(1)
            # Tolerate "sage/foo/bar" entries by stripping the leading "sage/".
            if key.startswith("sage/"):
                key = key[len("sage/"):]
            if "/" in key:
                exempt.add(key)
    return exempt


def top_subpackage(key: str) -> str:
    return key.split("/", 1)[0]


def summarise(
    sources: set[str],
    stubs: set[str],
    exempt: set[str],
) -> dict[str, dict[str, int]]:
    """Per-subpackage tally of source / stub / exempt / missing counts."""
    summary: dict[str, dict[str, int]] = {}
    in_scope = sources - exempt
    all_subs = sorted({top_subpackage(k) for k in sources | stubs})
    for sub in all_subs:
        sub_sources = {k for k in sources if top_subpackage(k) == sub}
        sub_stubs = {k for k in stubs if top_subpackage(k) == sub}
        sub_exempt = {k for k in exempt if top_subpackage(k) == sub}
        sub_in_scope = sub_sources - sub_exempt
        sub_missing = sub_in_scope - sub_stubs
        sub_orphan = sub_stubs - sub_sources
        summary[sub] = {
            "source": len(sub_sources),
            "stub": len(sub_stubs),
            "exempt": len(sub_exempt),
            "in_scope": len(sub_in_scope),
            "covered": len(sub_in_scope & sub_stubs),
            "missing": len(sub_missing),
            "orphan": len(sub_orphan),
        }
    # Totals row
    summary["__TOTAL__"] = {
        "source": len(sources),
        "stub": len(stubs),
        "exempt": len(exempt),
        "in_scope": len(in_scope),
        "covered": len(in_scope & stubs),
        "missing": len(in_scope - stubs),
        "orphan": len(stubs - sources),
    }
    return summary


def format_table(summary: dict[str, dict[str, int]]) -> str:
    rows = [("subpackage", "source", "exempt", "in_scope", "covered", "missing", "%")]
    for sub, vals in summary.items():
        pct = (
            f"{100.0 * vals['covered'] / vals['in_scope']:.1f}"
            if vals["in_scope"] else "—"
        )
        rows.append((
            sub,
            str(vals["source"]),
            str(vals["exempt"]),
            str(vals["in_scope"]),
            str(vals["covered"]),
            str(vals["missing"]),
            pct,
        ))
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    lines = []
    for i, r in enumerate(rows):
        line = "  ".join(c.ljust(w) for c, w in zip(r, widths))
        lines.append(line)
        if i == 0:
            lines.append("  ".join("-" * w for w in widths))
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit JSON summary")
    ap.add_argument(
        "--missing", action="store_true",
        help="list missing source modules (one per line) instead of summary",
    )
    ap.add_argument(
        "--orphan", action="store_true",
        help="list stub-without-source modules instead of summary",
    )
    ap.add_argument(
        "--subpackage",
        help="restrict --missing / --orphan output to this top-level subpackage",
    )
    ap.add_argument(
        "--exempt", action="append", default=[],
        help="path to an exempt-list markdown file (repeatable)",
    )
    ap.add_argument(
        "--threshold", type=float, default=None,
        help="if set, exit 1 when overall coverage is below this fraction (0–1)",
    )
    args = ap.parse_args()

    if not SAGE_SRC.exists():
        print(
            f"sage-src not initialised at {SAGE_SRC}. "
            f"Run: git submodule update --init --depth 1",
            file=sys.stderr,
        )
        return 1

    exempt_paths = [Path(p) for p in args.exempt]
    if not exempt_paths:
        default = REPO_ROOT / ".agents" / "phases" / "phase-01-exempt.md"
        if default.exists():
            exempt_paths.append(default)

    sources = enumerate_sources(SAGE_SRC)
    stubs = enumerate_stubs(SAGE_STUBS)
    exempt = load_exempt(exempt_paths) & sources
    summary = summarise(sources, stubs, exempt)

    if args.missing or args.orphan:
        in_scope = sources - exempt
        if args.missing:
            keys = sorted(in_scope - stubs)
        else:
            keys = sorted(stubs - sources)
        if args.subpackage:
            keys = [k for k in keys if top_subpackage(k) == args.subpackage]
        for k in keys:
            print(k)
    elif args.json:
        json.dump(summary, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    else:
        print(format_table(summary))

    if args.threshold is not None:
        total = summary["__TOTAL__"]
        coverage = total["covered"] / total["in_scope"] if total["in_scope"] else 0.0
        if coverage < args.threshold:
            print(
                f"coverage {coverage:.3f} below threshold {args.threshold:.3f}",
                file=sys.stderr,
            )
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
