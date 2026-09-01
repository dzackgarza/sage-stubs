#!/usr/bin/env python3
"""Print the outstanding stub-work queue from .agents/plan.md and phase cards.

This is the live worklist. Coverage (`just coverage`) locates missing files;
it is not the queue. Method gaps and consumer mismatches are derived from
source vs stubs and from running mypy — do not keep a sidecar gaps ledger.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLAN = REPO_ROOT / ".agents" / "plan.md"
PHASES = REPO_ROOT / ".agents" / "phases"

PHASE_ROW = re.compile(
    r"^\|\s*(\d{2})\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|"
    r"[^|]*\|[^|]*\|[^|]*\|\s*([^|]+)\|"
)
TASK_ROW = re.compile(
    r"^\|\s*(T\d{2}\.\S+)\s*\|\s*(.*?)\s*\|"
    r"[^|]*\|\s*([^|]*)\|\s*([^|]+)\|"
)


def status_kind(cell: str) -> str:
    text = cell.strip()
    if "✅" in text:
        return "done"
    if "🔵" in text:
        return "blocked"
    if "⚪" in text:
        return "na"
    if "🟡" in text:
        return "partial"
    if "⬜" in text:
        return "pending"
    return "unknown"


def task_title(raw: str) -> str:
    text = re.sub(r"\*+", "", raw).strip()
    text = re.sub(r"\s+", " ", text)
    if "—" in text:
        text = text.split("—", 1)[0].strip()
    return text


EN_DASH = "\u2013"
EM_DASH = "\u2014"


def parse_depends(cell: str) -> list[str]:
    text = cell.strip()
    if text in {"", EM_DASH, "-"}:
        return []
    if EN_DASH in text or text.count("T") > 1:
        # Range like T06.1<en dash>T06.11: not claimable until those rows are done.
        return [text]
    return [part.strip() for part in text.split(",") if part.strip()]


def load_plan_phases() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in PLAN.read_text().splitlines():
        match = PHASE_ROW.match(line)
        if match is None:
            continue
        number, name, rel, status = match.groups()
        rows.append(
            {
                "id": number,
                "name": name,
                "path": (PHASES.parent / rel).resolve(),
                "status": status.strip(),
                "kind": status_kind(status),
            }
        )
    return rows


def load_tasks(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if not path.is_file():
        return rows
    for line in path.read_text().splitlines():
        match = TASK_ROW.match(line)
        if match is None:
            continue
        ident, title, depends, status = match.groups()
        rows.append(
            {
                "id": ident,
                "title": task_title(title),
                "depends": depends.strip(),
                "status": status.strip(),
                "kind": status_kind(status),
            }
        )
    return rows


def deps_satisfied(depends: str, tasks: list[dict[str, str]]) -> bool:
    needed = parse_depends(depends)
    if not needed:
        return True
    done = {task["id"] for task in tasks if task["kind"] == "done"}
    for item in needed:
        if EN_DASH in item or item.count("T") > 1:
            return False
        if item not in done:
            return False
    return True


def print_queue(*, all_open: bool) -> int:
    if not PLAN.is_file():
        print(f"missing plan: {PLAN}", file=sys.stderr)
        return 1
    phases = load_plan_phases()
    if not phases:
        print("no phase rows found in .agents/plan.md", file=sys.stderr)
        return 1

    frontier = [p for p in phases if p["kind"] == "partial"]
    print("sage-stubs work queue")
    print("source: .agents/plan.md + .agents/phases/")
    if frontier:
        names = ", ".join(f"Phase {p['id']} ({p['name']})" for p in frontier)
        print(f"frontier: {names}")
    else:
        nxt = next((p for p in phases if p["kind"] == "pending"), None)
        if nxt is None:
            print("frontier: no open phases")
        else:
            print(f"frontier: Phase {nxt['id']} ({nxt['name']})")

    targets = phases if all_open else frontier or phases
    if not all_open:
        targets = frontier

    claimable: list[str] = []
    waiting: list[str] = []
    for phase in targets:
        tasks = load_tasks(phase["path"])
        open_tasks = [t for t in tasks if t["kind"] in {"pending", "partial"}]
        if not open_tasks:
            continue
        print()
        print(f"Phase {phase['id']} — {phase['name']}  [{phase['status']}]")
        for task in open_tasks:
            line = f"  {task['id']:<8} {task['title']}  [{task['status']}]"
            if deps_satisfied(task["depends"], tasks):
                claimable.append(f"{phase['id']}/{task['id']}")
                print(line)
            else:
                waiting.append(f"{task['id']} waits on {task['depends']}")
                print(f"{line}  (waits on {task['depends']})")

    print()
    if claimable:
        print(f"claimable now: {len(claimable)} task(s)")
        print("pick one row, mark it 🟡 In Progress on the phase card, then stub.")
    else:
        print("no claimable tasks in the current frontier.")
    if waiting and not all_open:
        print(f"blocked on earlier rows: {len(waiting)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="include every incomplete phase, not only the in-progress frontier",
    )
    args = parser.parse_args()
    return print_queue(all_open=args.all)


if __name__ == "__main__":
    sys.exit(main())
