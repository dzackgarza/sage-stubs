# Plan: sage-stubs Full Parity Rollout

Master tracking card for the [Full Stub Parity feature](feature.md).

The plan is a tree. The eighteen entries in the phase table below are the
**first-level children of the plan**. They are domain-scale bodies of work,
not names for individual pull requests or small file batches.

## Planning hierarchy

```text
Full Stub Parity Plan
├── Phase 01: Foundation completion
│   ├── task/workstream
│   │   ├── commit
│   │   └── commit
│   └── task/workstream
│       └── commit
├── Phase 02: Core rings & arithmetic
│   └── ...
└── Phase 18: Infrastructure
    └── ...
```

The node types have fixed meanings:

- **Plan** — the full Sage 10.7 parity objective.
- **Phase** — a first-level, domain-scale component of the plan, normally
  covering roughly 50–330 source modules and completed only when every task
  and phase-wide acceptance criterion is complete.
- **Task/workstream** — a coherent mathematical or package-level component
  inside one phase, normally covering 5–30 files. A task may require several
  commits.
- **Commit** — a terminal leaf containing one reviewable source-grounded
  increment. Commits do not become phases merely because they are delivered
  through separate branches or pull requests.
- **Pull request** — a delivery envelope around one or more adjacent commit
  leaves; it is not an additional planning level.

Every commit must belong to exactly one task. A necessary cross-phase
foundation repair must be recorded in both affected task cards, but it does
not complete either phase. Numeric labels `Phase NN` are reserved exclusively
for the eighteen first-level nodes below.

## Status semantics

- `⬜ Not Started` — no accepted task work.
- `🟡 In Progress` — at least one task has accepted or partial work, but the
  phase acceptance criteria are not complete.
- `✅ Complete` — every task and phase-wide gate is complete.
- `🔵 Blocked` — no further valid work can proceed until the stated blocker is
  resolved.
- `⚪ N/A` — excluded by a documented scope decision.

A phase cannot be declared complete from coverage, violation-count reduction,
or the landing of a small batch. Completion is a statement about the entire
first-level subtree.

## Phase tracking table

| ID | Phase | Tier | Depends on | Source files | Status |
|----|-------|------|------------|--------------|--------|
| 01 | [Foundation completion](phases/phase-01-foundation.md) | 0 | — | ~145 | ✅ Complete |
| 02 | [Core rings & arithmetic](phases/phase-02-core-rings.md) | 1 | 01 | ~80 | ✅ Complete |
| 03 | [Polynomial rings](phases/phase-03-polynomial-rings.md) | 1 | 01 | ~95 | ✅ Complete |
| 04 | [Number-theoretic rings](phases/phase-04-number-theory-rings.md) | 1 | 01 | ~130 | 🟡 In Progress |
| 05 | [Linear algebra: matrices & modules](phases/phase-05-linear-algebra.md) | 1 | 01 | ~120 | ⬜ Not Started |
| 06 | [Algebras: associative & non-Lie](phases/phase-06-algebras-core.md) | 2 | 02, 05 | ~70 | 🟡 In Progress |
| 07 | [Lie algebras & quantum groups](phases/phase-07-lie-quantum.md) | 2 | 02, 05 | ~50 | ⬜ Not Started |
| 08 | [Groups](phases/phase-08-groups.md) | 2 | 02, 05 | ~92 | ⬜ Not Started |
| 09 | [Combinatorics: leaves & foundations](phases/phase-09-combinat-leaves.md) | 2 | 02 | ~135 | ⬜ Not Started |
| 10 | [Combinatorics: symmetric functions & root systems](phases/phase-10-combinat-sf-roots.md) | 3 | 09 | ~95 | ⬜ Not Started |
| 11 | [Combinatorics: crystals, posets, words, tableaux](phases/phase-11-combinat-crystals-posets.md) | 3 | 09 | ~115 | ⬜ Not Started |
| 12 | [Geometry & polyhedra](phases/phase-12-geometry.md) | 3 | 05 | ~88 | ⬜ Not Started |
| 13 | [Schemes & dynamics](phases/phase-13-schemes-dynamics.md) | 4 | 04, 12 | ~170 | ⬜ Not Started |
| 14 | [Modular forms & Hecke modules](phases/phase-14-modular.md) | 4 | 04, 05 | ~130 | ⬜ Not Started |
| 15 | [Topology, manifolds, graphs, homology](phases/phase-15-topology-manifolds-graphs.md) | 3 | 05 | ~195 | ⬜ Not Started |
| 16 | [Symbolic, calculus, functions](phases/phase-16-symbolic.md) | 3 | 02 | 56 + 6 support | ✅ Complete |
| 17 | [Applied domains](phases/phase-17-applied-domains.md) | 3 | 02, 05 | ~155 | ⬜ Not Started |
| 18 | [Infrastructure: numerical, plot, interfaces, dev](phases/phase-18-infrastructure.md) | 5 | 02 | ~330 | ⬜ Not Started |

At kickoff, approximately 2,160 in-scope source modules remained after
exemptions and deduplication. They are grouped into roughly 140–160 tasks
across these eighteen phases. This is a module count, **not a prediction of
2,160 phases or 2,160 commits**.

## Dependency graph

```text
                 ┌─ 02 ─┐
                 │      ├─ 06, 07, 08 ──┐
        01 ─────┼─ 03 ─┤                │
                 │      ├─ 09 ── 10, 11 │
                 ├─ 04 ─┤                │
                 │      └─ 14            ├─ 13
                 ├─ 05 ─┤                │
                 │      └─ 12 ───────────┤
                 │      └─ 15            │
                 │      └─ 17            │
                 ├─ 16
                 └─ 18
```

The graph constrains phase completion and interface stabilization. Partial
source-grounded work may expose a dependency earlier, but that work must be
recorded as partial and cannot be used to claim the dependent phase complete.

## Commit and task rules

- Commits are leaf nodes. Name them for the mathematical interface changed,
  not `Phase NN`.
- A task is normally 5–30 files, but semantic coherence outranks file count.
  A one-file commit is valid when the file is a substantial mathematical API;
  it remains a commit inside a task, not a phase.
- A pull request may contain one task or several adjacent commits from one
  task. It must not invent a new phase number.
- A task is `✅` only when all files named by the task are source-grounded and
  its task-level checks pass.
- A phase is `✅` only when all task rows are `✅`, its dependency contracts
  are reconciled, and the phase-wide source-parity and quality gates pass.

## Quality gate for every commit leaf

```bash
just check
```

This runs the repository's structural, semantic, lint, and strict typing
checks. A green local leaf does not imply that its parent task or phase is
complete.

## Measuring progress

```bash
just coverage
just coverage -- --subpackage rings --missing
just coverage -- --threshold 0.95
```

Coverage and diagnostic counts locate weak or absent typing. They are evidence
for task selection, not substitutes for mathematically meaningful signatures.
See [feature.md](feature.md#measuring-progress) for the full workflow.

## Current work frontier

> **Completed first-level subtree:** Phase 16 (symbolic, calculus, and
> functions) is complete: 56 in-scope Sage modules, six Cython-fragment support
> stubs, five package initializers, and two documented harness exemptions.
>
> **Active first-level phases:** Phase 04 (number-theoretic rings) and Phase 06
> (associative and non-Lie algebras). Phase 05 (linear algebra) remains an
> unstarted dependency frontier for Phases 06–08, 12, 14, 15, and 17.
>
> **Next valid work:** continue a named task under Phase 04 or Phase 06, or
> start Phase 05. Commits remain leaves beneath those task cards and must not
> invent new phase numbers.

Update the frontier whenever a first-level phase or task status changes.
