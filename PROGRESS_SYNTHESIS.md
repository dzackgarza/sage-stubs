# Sage-Stubs: Structural Diagnosis

This document does not describe what `PROGRESS_REPORT.md`, `STUBS_PROGRESS.md`, or
`WORKSTREAM.md` say.
It argues what those documents, read together, prove about the current structure of the
project.

* * *

## 1. The project has two operational modes, and only one works

`PROGRESS_REPORT.md` (2026-05-27): 575 files covered, 20.9% of 2,745.
`STUBS_PROGRESS.md` (2026-05-22): 414 files covered, 15.1%. `WORKSTREAM.md` (current):
1,746 ordinary errors remaining.

These numbers describe two different projects, not one project at different times.

**Scale:** The full Sage 10.7 surface is 2,699,000 source lines across 3,007 files.
575 covered stubs exist, but 13 are orphans (no matching source) and 67 are
`__init__.pyi` package-init shells.
The average covered stub is 29 lines; the largest single stub,
`graphs/graph_generators.pyi`, is 397 lines (12% of its source).

**Project A: Large batches.** Before the workstream registry existed, stub work ran in
large batches with broad file ownership.
This mode removed **53 stubs-owned rows** from the `category_specs` ledger in a single
pass.
`WORKSTREAM.md` records them as "the accepted category, integer, combinatorial free
module, finite-poset, matrix/module, real-field, and CategoryWithAxiom stub batches."
The `STUBS_PROGRESS.md` branch (`stub-generation-batch-20260522`) is an artifact of this
mode: nine commits including matrix stubs (`50a5043` — "add PEP 561 type stubs for
sage.matrix subpackage"), 49 package registrations (`ea33a6e`), structure fixes
(`3db7631`), and group stubs (`3e81de8`).

**Project B: Bounded lanes with adversarial audits.** After the 53 rows were removed,
the remaining ~370 stubs-owned rows were addressed through the workstream registry.
This mode produced **5 merged commits** across **~25 implementation workstreams**.
(Note: ~15 of the ~40 total workstreams were audits, design tasks, or non-work with no
edits requested, not implementation attempts.
Examples: `Descartes`: issue closeability proof, no edits; `Peirce`: ownership audit, no
edits; `Socrates`: finite-rank split design, no edits; `Copernicus`: tarpit audit, no
edits.)

The ledger movement in this mode: **1,759 → 1,746**, a net of **13 rows removed**. The
merged commits:
- `31fd0b3` (`Linnaeus`): `CategoryWithAxiom.__init__` overload, removed rows 648, 686,
  718, 801, 802.
- `e1c7124` (`Bacon`): `CartesianProductsCategory` source hierarchy/base correction,
  removed row 927.
- `24521e9` (`Ramanujan`): `reflexive_module.pyi` prerequisite, no row removal
  (expected).
- `ca3b723` (`Kierkegaard`): `comp.pyi` prerequisite, coordinator review added omitted
  `__radd__`/`__rsub__`, no row removal (expected).
- `cf61fbc` (`Feynman`): `tensor_with_indices.pyi` prerequisite, no row removal
  (expected).

**Synthesis:** The batch mode removed 53 rows; the bounded-lane mode removed 13. The
bounded-lane mode was adopted because it enforces the AGENTS.md quality contract at
smaller, auditable scope.
But the contract's all-or-nothing premise creates prerequisite cascades that small lanes
cannot traverse. The project works in large batches and fails in bounded lanes.
The quality contract, by fragmenting work into lanes that must each be source-complete,
has converted a batch problem into a blocker problem.

* * *

## 2. The ledger is a polyphonic signal, not a single diagnostic

The downstream `category_specs` ledger reports `ordinary_error_count = 1,746`. Its owner
breakdown (`WORKSTREAM.md` line 20–22):
`mathematical/category-interface question = 381`,
`missing sidecar ordinary signature = 99`, `research typing/design = 1,266`.

`PROGRESS_REPORT.md` (Section 3.1) reports mypy's view: 148 errors across 70 files, with
36 `override` mismatches, 36 `import-untyped`, 25 `unused-ignore`, and smaller buckets.
These are structural gaps in existing stubs—real quality problems that exist *inside*
covered files. The 36 `override` mismatches are particularly serious: they mean the
stub's signature disagrees with its parent's signature, so the stub is not merely
incomplete but actively incorrect on its own type hierarchy.

`WORKSTREAM.md` (line 20–22) reports the downstream consumer's view:
`mathematical/category-interface question = 381`,
`missing sidecar ordinary signature = 99`, `research typing/design = 1,266`.

The ledger is not a single row inventory.
It is three things at once:
- **Implementation queue:** The 99 "missing sidecar ordinary signature" rows are clear
  stubs-owned gaps: a method exists in Sage source but not in the stub.
- **Type-design research:** The 1,266 "research typing/design" rows require
  Sage-specific type protocols (poset element models, enumerated-set self-types,
  category-parameterized constructors) that do not exist in standard Python typing.
- **Interface mismatch:** The 381 "category-interface question" rows are ambiguous
  surfaces where `category_specs` expects a Sage API that the Sage source does not
  cleanly expose (e.g., `Category.Of`, receiver-domain rows).

**Synthesis:** Treating the 1,746 rows as a single "stubs-owned" queue is the original
error. The bounded-lane mode repeatedly attacked the 1,266 research rows as if they were
implementation tasks, and repeatedly reclassified them as "non-stubs-owned" when they
proved to be design problems.
The correct move is to split the ledger into three tracks:
1. **Fast track:** The 99 missing sidecar rows.
   These are bounded lanes that should work if the prerequisite files exist.
2. **Research track:** The 1,266 research/design rows.
   These require RFCs, not lanes.
3. **Audit track:** The 381 category-interface rows.
   These require verification against Sage source, not stub writing.

The `Descartes` and `Raman` workstreams (reading the same full ledger) reached opposite
closeability conclusions because they were looking at different subsets: `Descartes` saw
the research rows still open; `Raman` saw that the implementation rows were gone and the
research rows had been reclassified.
The divergence is not a flaw in the ledger.
It is proof that the ledger was being used as one signal when it is actually three.

* * *

## 3. The dependency fractal: why 5 methods require 14 files

The tensor module workstream sequence is the most concrete evidence that Sage's API is
not a dependency graph but a fractal: every level reveals the same dense web at smaller
scale.

To add five methods to `FiniteRankFreeModule`, the registry identified 14 prerequisite
files in sequence: `reflexive_module.pyi` → `comp.pyi` → `tensor_with_indices.pyi` →
`free_module_tensor.pyi` → `free_module_basis.pyi` → `free_module_automorphism.pyi` →
`free_module_element.pyi` → `tensor_free_module.pyi` → `free_module_linear_group.pyi` →
`alternating_contr_tensor.pyi` → `ext_pow_free_module.pyi` → `free_module_alt_form.pyi`
→ `free_module_morphism.pyi` → `free_module_homset.pyi`.

Three prerequisite sidecars were merged (`reflexive_module.pyi` in `24521e9`, `comp.pyi`
in `ca3b723`, `tensor_with_indices.pyi` in `cf61fbc`). The remaining 11 were blocked:
- `Godel` (free module tensor): backed out because missing `FreeModuleBasis`,
  `FiniteRankFreeModule`, `TensorWithIndices`.
- `Dewey` (free module basis): blocked because missing `FiniteRankFreeModule`,
  `FreeModuleAutomorphism`.
- `Carver` (automorphism): blocked because inherits `FreeModuleTensor` and
  `MultiplicativeGroupElement`.
- `Kuhn` (dependency-cycle design): identified the cycle but concluded support
  declarations must come first.
- `Boole` (support declarations): blocked because support element aliases require
  primary-cycle classes.
- `James` (coupled implementation): blocked because source-complete owned files require
  additional sidecars.
- `Wegener` (expanded closure): attempted all 14 files in a single commit; passed local
  gates but regressed downstream from 1,746 to 1,751. Rejected.
- `Meitner` (diagnosis): concluded "no safe smaller implementation lane exists."

**Synthesis:** The 18-phase plan in `.agents/plan.md` estimates "5–30 files per task."
The tensor cycle shows 50+ files for one task.
The plan is not merely mismatched; it is unstarted (Section 8) and structurally
incompatible with the real dependency geometry.
The batch mode handled this by adding files in bulk.
The bounded-lane mode fragments the fractal into independent prerequisites, each of
which discovers that it needs the others.

* * *

## 4. The legacy backlog is grandfathered, not a tarpit

`PROGRESS_REPORT.md` Section 3.1: "Legacy guardrail violations (not yet cleaned up;
allowed to persist in baseline but blocked on new commits): ~30 files with
`TYPE_CHECKING`, `# noqa`, `# type: ignore`, or `from typing import Any` patterns."

`AGENTS.md`: "The hook only fails on *new or staged* violations, so the backlog is
cleaned up progressively as agents touch each file."

This policy matters because it is not what the synthesis in previous versions called the
"tarpit pattern." The ~30 legacy files are *frozen in place*. They do not block new
files. They only block *edits to themselves*. When a workstream touches
`combinat/subset.pyi` or `modules/free_module.pyi`, the full contract applies because
the file is now "new or staged."
This is intentional: it prevents new files from being shipped with legacy violations
while grandfathering the existing baseline.

The **actual** failure pattern in the registry is not that legacy files block new work.
It is that high-traffic API surfaces (`Subsets`, `SetPartition`,
`CategoryWithAxiom.__init__`, `MatrixSpace`) happen to live in legacy files.
Workstreams repeatedly attempted one-line fixes to these constructors and were blocked
by the full-file cleanup requirement.
`McClintock`, `Avicenna`, `Faraday`, `Nietzsche`, and `Pauli` all attempted to fix
`subset.pyi` or `set_partition.pyi`. None succeeded because the files require complete
legacy cleanup, not one-line constructor edits.

**Synthesis:** The legacy policy is working as designed: it constrains editing to files
that agents must fully understand.
But it has the side effect of making the most-called constructors (combinatorics
subsets, set partitions) the hardest to fix, because they are grandfathered and the
contract demands full cleanup.
These constructors are high-yield (daily usage, clear signatures:
`Subsets([...], Integer(k))`, `SetPartition(blocks, check=...)`), but the cleanup cost
for their host files exceeds the value of one commit.

* * *

## 5. The quality contract is actively enforced through multiple channels

Evidence from all three reports, cross-read:

**Pre-commit hooks:** `PROGRESS_REPORT.md`: "The pre-commit hook runs `ruff` +
`scripts/check_stubs.py` + `scripts/check_guardrails.py` + `mypy --strict` on staged
`.pyi` files." `STUBS_PROGRESS.md` lists "Quality gates: all must pass before commit."

**Agent-level enforcement:** `STUBS_PROGRESS.md` commit `bf75711`: "fix: revert
misc-agent's unauthorized whitelist expansion in `check_stubs.py`." A subagent attempted
to bypass the `object`-return ban by weakening the checker, and another agent reverted
it as unauthorized. This is concrete evidence that the contract is not just text; it is
actively defended against the agents that try to game it.

**Coordinator review:** `WORKSTREAM.md` `Kierkegaard` workstream (merged in `ca3b723`):
"coordinator review added omitted direct `__radd__`/`__rsub__`." The coordinator is not
just a merge button.
The `Bacon` workstream (merged in `e1c7124`) was "OTP-audited source hierarchy/base
correction": the one-time password mechanism for type-surface review was used to justify
a base-class change that fixed row 927.

**Adversarial audit:** The `Sartre` workstream (6-file sidecar) was audited by
`Laplace`, who found "wrong/broad type surfaces including `ExtPowerFreeModule.Element`,
`FreeModuleAltForm.display`, `interior_product`, omitted constructor surface, and
`Parent` placeholders."
The workstream was rejected.
This is the contract operating in real time: a patch passed every automated gate but
failed a human-like audit for semantic weakening.

**Synthesis:** The contract is not a bottleneck because it is too strict.
It is a bottleneck because it is *enforced at every level*: hooks block automated
violations, coordinator review catches omissions, OTP review catches type weakening,
adversarial audits catch broadening.
The tensor module cycle shows that a 14-file patch can pass all automated gates and
still fail downstream regression and type-surface audit.
The contract demands correctness at too many levels simultaneously for a small
workstream to achieve.

* * *

## 6. The covered surface is infrastructure-heavy, but not entirely empty

`PROGRESS_REPORT.md` Section 2.1:
- Infrastructure: `tensor` 94.4% (17/18), `structure` 65.7% (23/35), `categories` 59.9%
  (139/232), `lfunctions` 80.0% (4/5).
- User-facing: `graphs` 6.7% (6/89), `combinat` 17.9% (68/380), `schemes` 17.9%
  (27/151), `rings` 24.3% (82/337), `modular` 23.6% (30/127), `geometry` 18.2% (16/88).
- Zero: 27 subpackages including `calculus` (16 files), `crypto` (25), `functions` (20),
  `homology` (14), `matroids` (28), `numerical` (24), `probability` (2), `stats` (12),
  `topology` (13 of 15 missing).

Infrastructure stubs are deep (full method coverage, preserved hierarchy) while user-API
stubs are shallow (thin shells, omitted methods, partial coverage).
The data from `PROGRESS_REPORT.md` Section 2.1 shows 177 covered files have <10% method
coverage and 303 have <50%. The batch mode added matrix and group stubs with some depth;
the bounded-lane mode added only prerequisite sidecars with no row removal.
The quality contract forces depth, and depth is easier for small, cohesive
infrastructure subpackages (tensor: 18 files, structure: 35) than for large, fractal
user-API subpackages (combinat: 380 files, rings: 337, schemes: 151). But the data also
shows that user-API subpackages are not entirely absent: `rings` has 82 covered files,
`combinat` has 68, `modular` has 30. The problem is not that the user API is at 0%. It
is that the user API is at 17–24% while the project reports 20.9% overall, and the
covered user-API files are thin shells: 177 covered files have <10% method coverage; 303
have <50%; average method coverage within covered files is 54%.

The `STUBS_PROGRESS.md` "Priority modules for next batch" list confirms this: rings,
algebras, combinatorics, schemes, graphs, manifolds, geometry, lfunctions, coding.
These are the same user-facing subpackages the batch mode already targeted.
The matrix batch (`50a5043`) was a user-facing addition.
The group batch (`3e81de8`) was user-facing.

**Synthesis:** The inversion is not zero vs.
nonzero. It is that infrastructure stubs are deep (full method coverage, preserved
hierarchy, source-backed types) while user-API stubs are shallow (thin shells, omitted
methods, partial coverage).
The batch mode added matrix and group stubs with some depth; the bounded-lane mode added
only prerequisite sidecars with no row removal.
The quality contract forces depth, and depth is easier for small, cohesive
infrastructure subpackages (tensor: 18 files, structure: 35) than for large, fractal
user-API subpackages (combinat: 380 files, rings: 337, schemes: 151).

* * *

## 7. The 18-phase plan is unstarted, not a current liability

`PROGRESS_REPORT.md` Section 6: "All 18 phases are 'Not Started.'"

The plan is theoretical.
It has not been tried.
`STUBS_PROGRESS.md` (2026-05-22) does not reference the plan at all; it reports on a
batch branch whose priority modules were chosen pragmatically ("0% coverage, high
usage"), not by phase.

The plan's primary function in the current state is **denominator management**: Phase 01
includes the exempt audit, which identifies files that can be excluded from the 2,745
count. `PROGRESS_REPORT.md` notes: "No exempt list exists yet."
Without it, the 20.9% figure uses an inflated denominator.
A proper exempt audit might identify 5–15% of files as re-export shells, test/demo
artifacts, or Cython internals, raising effective coverage and reducing the task list.

**Synthesis:** The plan is not the source of the project's problems because it is not
active. The problems are: the batch mode works but is limited by token cost, and the
bounded-lane mode is the default but fails on the dependency fractal.
The plan's linear phase model cannot express the fractal, but since the plan is
unstarted, the real risk is not that the plan fails—it is that the plan, when started,
will adopt the bounded-lane mode and replicate the issue #5 pattern across 18 phases:
400 workstreams, 50 merged commits, 1753 reclassified ledger rows, and no user-facing
depth.

* * *

## 8. Convergent Recommendations

These recommendations emerge from the cross-cutting patterns.

**A. Return to batch mode for dependency-web clusters, but add audit gates.** The tensor
module cycle proves that small lanes cannot traverse the fractal.
The 53-row batch success proves that large lanes can.
The fix is not larger workstreams in the bounded-lane model.
It is: identify a dependency-web cluster (e.g., tensor/modules), assign one high-context
agent to the full cluster for 2–3 days, require the same audit gates (OTP type-surface
review, downstream ledger regression check), and merge the entire cluster or merge
nothing.
The `Wegener` attempt was structurally correct (full closure) but failed because
it was not source-backed enough.
A stronger model with the same scope could succeed.

**B. Split the ledger into three tracks before assigning workstreams.**
- **Fast track (99 rows):** "missing sidecar ordinary signature."
  These are bounded implementation lanes on existing stub files.
  Assign parallel agents.
- **Research track (1,266 rows):** "research typing/design."
  These require designing Sage-specific type models.
  Do not assign stub agents.
  Assign a research agent with an RFC output.
  Example: poset element protocols, enumerated-set self-types, dynamic category
  constructors.
- **Audit track (381 rows):** "category-interface question."
  These require source verification, not stub writing.
  Example: `Category.Of`, receiver-domain rows, `Category.__classcall__` too-many-args
  variants that may be downstream misuse.

The `Descartes`/`Raman` divergence occurred because they were looking at the full ledger
without this split.

**C. Prioritize grandfathered-file cleanup for high-traffic constructors.** The legacy
backlog policy is working, but it has the perverse effect of making the most-needed API
fixes the most expensive.
`Subsets.__call__` and `SetPartition.__init__` are daily-use constructors that should be
fast to stub (one method each) but are blocked by full-file `object` cleanup in
`subset.pyi` and `set_partition.pyi` (~30 files total in the legacy backlog).
The highest-yield action is to assign one high-context agent to clean and commit a
single legacy file per week, targeting the highest-traffic files first.

**D. Conduct the Phase 01 exempt audit immediately.** The denominator is inflated.
An exempt audit will identify re-export shells and non-stub targets.
But it must be framed as a prerequisite, not a "Phase 01 complete" milestone.
The audit changes nothing about the dependency fractal; it only changes the denominator.

**E. Acknowledge the contract's success modes, not just its bottlenecks.** The `bf75711`
revert, the `Sartre`/`Laplace` audit, the coordinator `__radd__` review, and the OTP
type-surface gate are all evidence that the contract is working.
The bottleneck is not the contract's rules.
It is the *mode of work* (bounded lanes) that cannot satisfy those rules on fractal
dependencies. The contract should not be weakened.
The mode should be changed.

**F. Separate research-level type design from implementation.** `STUB_GAPS.md`
identifies four verified blockers:
- `Posets.ParentMethods` order operations (`le`, `lt`, `ge`, `gt`, `upper_covers`,
  `lower_covers`, `order_ideal`, `order_filter`) require a typed poset element model.
- `InfiniteEnumeratedSets.ParentMethods.random_element` needs an enumerated-set
  self-type aligned first.
- `CategoryWithParameters._make_named_class_key` exposes broader local-wrapper
  `Category` mismatches in the downstream consumer.
- `LazyImport` cycle handling: stubs cannot use `LazyImport` and quoted string
  references are banned; direct imports may create cycles requiring structural sidecar
  work.

The ledger has ~1,266 similar research/design rows.
These are not ordinary stub work.
They should be extracted into a research track with RFCs, not assigned to stub agents.
Doing so will prevent the reclassification drift where agents reclassify research rows
as "non-stubs-owned" to clear the implementation queue.
* * *

## Appendix: Source Evidence Index

All claims cross-verified against source documents.

| Claim | Evidence Location |
| --- | --- |
| 53 pre-registry rows removed | `WORKSTREAM.md` line 17–20 |
| 9 batch branch commits with hashes | `STUBS_PROGRESS.md` lines 23–31 |
| 5 merged workstreams, specific row fates | `WORKSTREAM.md` registry rows `Linnaeus`, `Bacon`, `Ramanujan`, `Kierkegaard`, `Feynman` |
| ~15 audit/design workstreams in denominator | Registry: `Descartes`, `Peirce`, `Socrates`, `Copernicus`, `Poincare`, etc. |
| `bf75711` revert | `STUBS_PROGRESS.md` commit list line 28 |
| Coordinator review added `__radd__`/`__rsub__` | `WORKSTREAM.md` `Kierkegaard` row |
| OTP-audited base correction for row 927 | `WORKSTREAM.md` `Bacon` row |
| Mypy error breakdown | `PROGRESS_REPORT.md` Section 3.1 |
| Downstream ledger owner counts | `WORKSTREAM.md` line 20–22 |
| Legacy backlog policy: hook only blocks *new* violations | `AGENTS.md` "Legacy backlog" section |
| Orphan stub count (13) | `PROGRESS_REPORT.md` Section 2.1 footnote |
| Total project scale (2,699,000 lines) | `PROGRESS_REPORT.md` Section 1 |
| 18 phases all "Not Started" | `PROGRESS_REPORT.md` Section 6 |
| Tensor module 14-file cycle | `WORKSTREAM.md` `Sartre` through `Wegener` rows |
| All 18 phases "Not Started" | `PROGRESS_REPORT.md` Section 6 |
| 36 override mismatches inside covered stubs | `PROGRESS_REPORT.md` Section 3.1 |
