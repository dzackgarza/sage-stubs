# Plan: sage-stubs Full Parity Rollout

Master tracking card for the [Full Stub Parity feature](feature.md). Eighteen
phases, each delivered as a series of task commits. Phases are ordered by
dependency tier — phases in the **same tier** can run **in parallel** once
their tier-blocker dependency completes.

## How to read this card

- **Status column:** `⬜ Not Started`, `🟡 In Progress`, `✅ Complete`,
  `🔵 Blocked`, `⚪ N/A`.
- **Depends on:** lists phase IDs that MUST be `✅ Complete` before this
  phase can start. An empty cell means no blocker. Phases without a shared
  dependency can be worked on simultaneously.
- **Source files:** approximate count of in-scope `.py`/`.pyx` modules in
  the phase, derived from the Phase-0 survey. Each phase card itself owns
  the precise per-task file list.
- The **At-a-glance next step** banner at the bottom of this file is the
  single source of truth for "what to pick up next". Update it whenever a
  phase status changes.

## Phase tracking table

| ID | Phase | Tier | Depends on | Source files | Status |
|----|-------|------|------------|--------------|--------|
| 01 | [Foundation completion](phases/phase-01-foundation.md) | 0 | — | ~145 | ⬜ Not Started |
| 02 | [Core rings & arithmetic](phases/phase-02-core-rings.md) | 1 | 01 | ~80 | ⬜ Not Started |
| 03 | [Polynomial rings](phases/phase-03-polynomial-rings.md) | 1 | 01 | ~95 | ⬜ Not Started |
| 04 | [Number-theoretic rings](phases/phase-04-number-theory-rings.md) | 1 | 01 | ~130 | ⬜ Not Started |
| 05 | [Linear algebra: matrices & modules](phases/phase-05-linear-algebra.md) | 1 | 01 | ~120 | ⬜ Not Started |
| 06 | [Algebras: associative & non-Lie](phases/phase-06-algebras-core.md) | 2 | 02, 05 | ~70 | ⬜ Not Started |
| 07 | [Lie algebras & quantum groups](phases/phase-07-lie-quantum.md) | 2 | 02, 05 | ~50 | ⬜ Not Started |
| 08 | [Groups](phases/phase-08-groups.md) | 2 | 02, 05 | ~92 | ⬜ Not Started |
| 09 | [Combinatorics: leaves & foundations](phases/phase-09-combinat-leaves.md) | 2 | 02 | ~135 | ⬜ Not Started |
| 10 | [Combinatorics: symmetric functions & root systems](phases/phase-10-combinat-sf-roots.md) | 3 | 09 | ~95 | ⬜ Not Started |
| 11 | [Combinatorics: crystals, posets, words, tableaux](phases/phase-11-combinat-crystals-posets.md) | 3 | 09 | ~115 | ⬜ Not Started |
| 12 | [Geometry & polyhedra](phases/phase-12-geometry.md) | 3 | 05 | ~88 | ⬜ Not Started |
| 13 | [Schemes & dynamics](phases/phase-13-schemes-dynamics.md) | 4 | 04, 12 | ~170 | ⬜ Not Started |
| 14 | [Modular forms & Hecke modules](phases/phase-14-modular.md) | 4 | 04, 05 | ~130 | ⬜ Not Started |
| 15 | [Topology, manifolds, graphs, homology](phases/phase-15-topology-manifolds-graphs.md) | 3 | 05 | ~195 | ⬜ Not Started |
| 16 | [Symbolic, calculus, functions](phases/phase-16-symbolic.md) | 3 | 02 | ~65 | ⬜ Not Started |
| 17 | [Applied domains](phases/phase-17-applied-domains.md) | 3 | 02, 05 | ~155 | ⬜ Not Started |
| 18 | [Infrastructure: numerical, plot, interfaces, dev](phases/phase-18-infrastructure.md) | 5 | 02 | ~330 | ⬜ Not Started |

**Totals.** ~2160 stub commits expected after Phase 0 deduplication / exempt
listings; spread across ~140–160 tasks; ~18 phase cards. Phase 0 itself —
the survey, exempt list, and initial CI wiring — is not a phase here, it's
part of Phase 1 setup.

## Dependency graph (textual)

```
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

- Phase 01 unblocks **everything**.
- Within Tier 1 (Phases 02–05), all four are independent of each other and
  can run truly in parallel by separate contributors.
- Tier 2 (Phases 06–09) needs at least Phase 02; Phases 06–08 also need
  matrix/module surface from Phase 05.
- Tier 3 (Phases 10–17) opens up as the relevant Tier 2 phase lands.
- Tier 4 (Phases 13, 14) needs number-theoretic rings (04) and the
  relevant geometric / linear-algebra dependency.
- Tier 5 (Phase 18) is the infrastructure cleanup; it can technically run
  any time after Phase 02 but it is intentionally last because consumers
  of these modules are rare and the surface is huge.

## Parallelism guidance

- **Within a phase:** every phase card lists tasks with an explicit
  `Depends` column. Tasks with `Depends: —` can run in parallel from the
  moment the phase starts.
- **Across phases:** phases in the same tier whose dependencies are all
  satisfied can run in parallel. Coordinate on the [Slack channel TBD] to
  avoid two agents claiming the same phase card simultaneously.
- **Commit scope rule.** Each task is a commit (or a small batch of tightly
  related commits). Tasks are sized at **5–30 files** per AGENTS.md. Smaller
  than 5 files = bundle with a neighbour. Larger than 30 = split along an
  obvious subtree boundary.

## Quality gate (every commit)

Before pushing a task's commit:

```bash
just check
```

which runs `ruff`, `scripts/check_stubs.py`, and `mypy --strict`. A green
result is the only acceptable signal of done.

## At-a-glance next step

> **Pick up:** Phase 01 — Foundation completion.
> **Why:** All downstream phases block on it.
> **First task to claim:** see [phase-01-foundation.md](phases/phase-01-foundation.md)
> task table; tasks T01.1, T01.2 have no internal dependencies.

Update this banner whenever a phase transitions between `Not Started`,
`In Progress`, and `Complete`.
