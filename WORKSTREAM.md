# Workstream Plan for issue #5

This document turns `dzackgarza/sage-stubs#5` into parallel, source-backed
workstreams. The goal is not to classify the research ledger. The goal is to
remove the stubs-owned `category_specs` failures by implementing real Sage 10.7
stub surfaces, or by rejecting a listed surface with source/runtime evidence.

Current baseline:

- Issue scope: 370 stubs-owned `category_specs` rows.
- Validated committed progress: 41 ordinary rows removed from the refreshed
  downstream ledger after the accepted category, integer, combinatorial free
  module, finite-poset, matrix/module, and real-field stub batches.
- Current downstream ledger after reinstalling committed stubs:
  `ordinary_error_count = 1759`, with owner counts:
  `mathematical/category-interface question = 389`,
  `missing sidecar ordinary signature = 99`,
  `research typing/design = 1271`.
- Current local state after the latest accepted commits: no tracked file diff;
  untracked `.serena/` metadata may exist and must not be committed.

The main throughput problem is serial row-picking. Use this plan to split the
remaining work by stub ownership, run agents in parallel in isolated worktrees
or branches, and merge only source-cited, downstream-validated deltas.

## Orchestrator operating model

The active coordinator is the orchestrator for issue #5. The orchestrator should
primarily assign, monitor, review, and integrate subagent work. The coordinator
should do direct stub editing only when the edit is trivial, already fully in
context, and clearly within an unclaimed lane. The default coordinator action is
to turn a row family into a bounded subagent prompt, not to start implementing
the row family directly.

Subagent preference order:

- Use Spark subagents first while suitable Spark capacity remains.
- After Spark capacity is exhausted, use GPT-5.5 subagents with low
  reasoning/effort when the runtime offers that model and setting.
- Escalate model strength or reasoning effort only when transcript evidence
  shows the worker is stalling, drifting, or making source/type-surface mistakes.
- Keep small, already-contextual edits in the coordinator thread when subagent
  startup cost would exceed the value of delegation.

The orchestrator owns process integrity:

- assign exactly one primary workstream per subagent;
- give each subagent explicit owned files, target diagnostics, non-goals, and
  validation commands;
- prevent workers from touching another stream's owned files;
- reject summaries that are not backed by diffs, source citations, and downstream
  ledger deltas;
- keep commits organized by workstream, with one coherent downstream delta per
  commit or small commit group;
- track which worktrees, branches, task ids, and ledger baselines belong to each
  active workstream;
- split a workstream into substreams when it runs beyond the user-set 2-3 hour
  monitoring trigger or when transcript evidence shows multiple independent row
  families inside one stream.

Use git worktrees only when the coordinator can keep them organized. Every
worktree must have a named stream owner, branch, base commit, assigned files,
task id, status, and cleanup condition. Clean stale worktrees immediately after
merge, rejection, or abandonment.

## Non-negotiable constraints

Every worker must follow the repo contract in `AGENTS.md`:

- Read docs first: `AGENTS.md`, `README.md`, `justfile`, issue #5, and the
  relevant Sage source file under `sage-src/src/sage/...`.
- For each touched class, enumerate direct public methods from the direct source
  body before writing stubs.
- Resolve every changed type from Sage 10.7 source, docstring, or runtime
  evidence. Cite exact source lines in the commit message or worker report.
- Run type-surface review before staging changed `.pyi` files.
- Never use `Any`, `object`, quoted annotations, `TYPE_CHECKING`, local ignores,
  casts, broad superclass placeholders, or generic TypeVars as opacity markers.
- Never add fake Sage surfaces: no `sage.rings.infinity.oo`, no base
  `Morphism.is_invertible`, no generic dynamic `Category.FinitelyPresented`,
  `Category.OverPID`, `Category.Quotients`, `Category.Subobjects`, or local
  `category_specs` wrapper concepts.
- Never add inherited methods as direct methods unless the Sage source exposes
  them on that target surface.
- Never weaken a precise existing annotation to make a local check pass. Add the
  missing source-backed sidecar or stop with evidence.
- Never edit protected config except the permitted package registration case in
  `pyproject.toml`.

Negative findings must use the five-field evidence format:

```text
- Searched: ...
- Found: ...
- Conclusion: I believe ... based on ...
- Confidence: High / Medium / Low
- Gaps: ...
```

## Shared validation contract

Each workstream must validate at three levels.

Local file gates:

```bash
python scripts/check_stubs.py <changed .pyi files>
ruff check <changed files>
python scripts/check_guardrails.py --files <changed files>
python -m mypy --strict --follow-imports=silent <changed .pyi files>
just type-surface-review --files <changed .pyi files>
```

Staged repo gate:

```bash
just check
```

Downstream `category_specs` gate:

```bash
cd /home/dzack/research
sage -python -m pip install --force-reinstall /home/dzack/sage-mypy-plugin/sage-stubs
just category-specs-mypy-structural-report-full
just category-specs-mypy-ledger
jq '{ordinary_error_count, counts_by_owner}' reports/workstreams/category-specs-mypy-ledger/latest.json
```

For targeted row proof, filter the ledger by the surface being changed:

```bash
jq -r '.errors[]
  | select(.message | test("<surface regex>"))
  | [.owner,.path,.line,.message] | @tsv' \
  reports/workstreams/category-specs-mypy-ledger/latest.json
```

A workstream is merge-ready only when its report names:

- changed files;
- exact Sage source/runtime evidence;
- type-surface review classification for every changed annotation, base, alias,
  overload, import, protocol, and generic argument;
- local gate results;
- downstream `ordinary_error_count` before and after;
- targeted rows removed, unchanged, or reclassified;
- any new errors introduced, with explanation or rollback.

## Coordinator stream

Owner role: orchestrator and integration reviewer, not a broad implementation
worker.

Owned files:

- `WORKSTREAM.md`
- integration commits
- issue #5 comments and closing proof
- baseline snapshots under `/home/dzack/research/reports/...` only as external
  validation artifacts, not repo commits

Immediate action:

- Commit the validated `Category.__classcall__` `Integer` domain edit if it
  still passes hooks and downstream validation.

Responsibilities:

- Prefer subagent delegation over direct implementation. Direct edits are allowed
  only for trivial, already-contextual changes that do not cross workstream
  boundaries.
- Prefer Spark subagents until their useful capacity is exhausted, then use
  GPT-5.5 low-reasoning/low-effort subagents when available.
- Keep one authoritative baseline: latest committed `sage-stubs` revision plus
  latest full `category_specs` ledger.
- Assign workers to disjoint files. If two workers need the same file, serialize
  those workers or split by commit order with an explicit dependency.
- Maintain the active workstream registry with worker identity, branch/worktree,
  task id, owned files, target ledger regex, baseline count, current status, and
  next coordinator action.
- Monitor active workers. If a workstream exceeds the user-set 2-3 hour
  monitoring trigger, inspect the transcript and split the stream when it
  contains independent row families or separable file ownership.
- Review worker diffs before merging. Hook passage is not approval.
- Reject any worker output that broadens type surfaces without source proof.
- Reinstall stubs and rerun the full downstream ledger after each merge.
- Maintain a row reconciliation table outside commits or in issue comments:
  implemented, rejected with evidence, reclassified, still open.

Stop rules:

- Stop merging if a workstream introduces new ordinary errors outside its target
  family.
- Stop merging if type-surface review shows a high-risk broadening.
- Stop and ask for user direction if closing #5 requires changing
  `category_specs` or `sagemath-mypy-plugin` ownership rather than stubs.
- Stop and reassign if a worker repeatedly touches files outside its lane,
  rewrites unrelated stubs, or reports progress without source and ledger
  evidence.

Active workstream registry template:

| Stream | Worker | Branch/worktree | Task id | Owned files | Target rows | Baseline | Status | Cleanup |
|--------|--------|-----------------|---------|-------------|-------------|----------|--------|---------|
| _example_ | _Spark/GPT worker_ | `.worktrees/<name>` | `<id>` | `<paths>` | `<regex>` | `<count>` | active/review/merged | remove after merge |

Current active registry:

| Stream | Worker | Branch/worktree | Task id | Owned files | Target rows | Baseline | Status | Cleanup |
|--------|--------|-----------------|---------|-------------|-------------|----------|--------|---------|
| Sets leaf surfaces | Hegel / GPT-5.5 low | agent fork workspace | `019e575d-ff11-7551-ad27-ba2dbf822f34` | `sets/recursively_enumerated_set.pyi`, `sets/family.pyi`, `sets/condition_set.pyi` | recursively enumerated exports, `AbstractFamily.keys`, `ConditionSet` constructor | `ordinary_error_count=1759` | closed: no merge; remaining `ConditionSet` row reclassified as research method-container typing | cleaned by agent close |
| Finite-rank free module surfaces | Averroes / GPT-5.5 low | agent fork workspace | `019e575e-479d-76a3-9365-105ad3bb329e` | `tensor/modules/finite_rank_free_module.pyi`, optional `modules/free_module.pyi` only if source forces it | `bases`, `default_basis`, `set_default_basis`, `dimension`, `exterior_power`, `alternating_form` override rows | `ordinary_error_count=1759` | closed: no merge; split needed for return sidecars | cleaned by agent close |
| Commutative ring polynomial leaf | Goodall / GPT-5.5 low | agent fork workspace | `019e575e-84fb-7411-94e6-5eeb26f66a7d` | `rings/ring.pyi`, `rings/polynomial/polynomial_ring.pyi` | `CommutativeRing.extension`, `PolynomialRing_generic.completion`; excluding `sage.rings.infinity.oo` | `ordinary_error_count=1759` | closed: reverted after downstream regression to `ordinary_error_count=1760`; rows reclassified as receiver-typing issue, not generic `Ring.extension` | cleaned by agent close |
| Finite-rank return sidecars | Hypatia / GPT-5.5 low | agent fork workspace | `019e5763-6d92-7a91-9fce-3398ec3a45e3` | `tensor/modules/finite_rank_free_module.pyi`, `ext_pow_free_module.pyi`, `free_module_alt_form.pyi`, `free_module_basis.pyi` | precise return sidecars for finite-rank methods | `ordinary_error_count=1759` | closed: no merge; needs expanded `tensor/modules/reflexive_module.pyi` sidecar lane | cleaned by agent close |
| Reflexive finite-rank sidecars | Pascal / GPT-5.5 low | agent fork workspace | `019e576d-e684-72e2-a1f1-3a4d66b2cc39` | `tensor/modules/reflexive_module.pyi`, finite-rank return sidecars | finite-rank free-module method return sidecars | `ordinary_error_count=1759` | closed: no merge; `dimension` not direct on `FiniteRankFreeModule`, and precise sidecars need expanded `free_module_tensor`/basis-abstraction ownership | cleaned by agent close |
| Sets provider missing signatures | Carson / GPT-5.5 low | agent fork workspace | `019e576e-6a1f-7611-acde-45964a734f09` | `categories/sets_cat.pyi`, enumerated/finite/facade set category stubs | `is_facade`, `is_countable`, `is_uncountable`, `__len__`, `random_element`, maybe `_coerce_map_from_` | `ordinary_error_count=1759` | closed: no merge; rows reclassified as category_specs wrapper/projection or concrete-parent, not provider-stub gaps | cleaned by agent close |
| Forms provider missing signatures | Popper / GPT-5.5 low | agent fork workspace | `019e5774-2321-76e0-b6f3-80f287c82830` | source-backed `categories/*form*.pyi` only | `has_form`, form predicate methods, free bilinear form methods | `ordinary_error_count=1759` | closed: no merge; methods are concrete module/matrix/quadratic-form surfaces or category_specs taxonomy, not Sage category providers | cleaned by agent close |
| Homsets and morphisms audit | Anscombe / GPT-5.5 low | agent fork workspace | `019e5774-6162-7983-8808-05ccaacc3a91` | `categories/homsets.pyi`, `homset.pyi`, `morphism.pyi` | `default_super_categories`, base `Morphism.is_invertible` non-goal audit | `ordinary_error_count=1759` | closed: no merge; `default_super_categories` already on source-backed homsets/covariant classes, base `Morphism.is_invertible` remains explicit non-goal | cleaned by agent close |
| Module construction missing signatures | Epicurus / GPT-5.5 low | agent fork workspace | `019e5774-a614-7ba1-8462-bf5ee9cb9956` | `categories/modules*.pyi`, graded/bimodule sidecars | module quotient/cartesian/graded predicate provider rows | `ordinary_error_count=1759` | closed: no merge; source-backed methods are already present or live on with-basis classes, remaining predicates/hooks are category_specs-local | cleaned by agent close |
| Rational-field public methods audit | Halley / GPT-5.5 low | agent fork workspace | `019e5779-9b45-7851-a05e-4e77d3350a2d` | `rings/rational_field.pyi`, narrow number-field sidecars if source-backed | 40 rational-field missing sidecar rows | `ordinary_error_count=1759` | closed: no merge; attempted source-backed number-field patch did not move rows, remaining failures are category_specs receiver/projection mismatch or unsupported names | cleaned by agent close |
| Ring/field provider predicates | Singer / GPT-5.5 low | agent fork workspace | `019e5779-dd2d-7c13-8d13-f1baabe8a289` | ring, polynomial, real-field stubs excluding rational-field ownership | `change_precision`, extension/completion, local-field predicates, infinity non-goal | `ordinary_error_count=1759` | closed: no merge; `to_prec`/extension/completion already covered, predicate names absent from Sage source | cleaned by agent close |
| Concrete set/topological methods | Kant / GPT-5.5 low | agent fork workspace | `019e577a-2090-7463-a763-65ca322501f4` | real/image set stubs and topological category stubs | `_an_element_` real/image rows, `is_metric` | `ordinary_error_count=1759` | closed: no merge; `_an_element_` methods already covered, `is_metric` absent from Sage metric source | cleaned by agent close |
| Combinatorics constructor recheck | McClintock / GPT-5.5 low | agent fork workspace | `019e5782-5c31-7c00-b229-3660d2dd10f1` | `combinat/subset.pyi`, `combinat/set_partition.pyi` | `Subsets(..., Integer(k))`, direct `SetPartition(blocks, check=...)` | `ordinary_error_count=1759` | closed: no merge; both rows are source-backed, but touched files fail existing legacy `object` and override gates, so they require a cleanup-aware combinatorics tarpit lane rather than one-line constructor edits | cleaned by agent close |
| Category receiver-domain audit | Noether / GPT-5.5 low | agent fork workspace | `019e5782-9dcb-79b0-961b-4d59f1347a0c` | `categories/category.pyi`, `category_types.pyi`, `category_with_axiom.pyi` | `Category.Of` and `Category.__classcall__` receiver-domain rows | `ordinary_error_count=1759` | closed: no merge; latest rows are already `research typing/design`, no Sage `def Of` exists, and broadening category arguments to `Parent` or method-container types would model category_specs receiver erasure rather than a Sage API | cleaned by agent close |
| Lazy callable stream | Hubble / GPT-5.5 low | agent fork workspace | `019e5788-4897-7181-a11b-c4737a9ba885` | `misc/lazy_import.pyi`, `categories/covariant_functorial_construction.pyi` | `LazyImport` callability, lazy category factories, `TensorProductFunctor` callable rows | `ordinary_error_count=1759` | closed: no merge; callable surfaces already exist in owned stubs and latest ledger has no direct `LazyImport` or `TensorProductFunctor` callable diagnostics | cleaned by agent close |
| Posets provider-method audit | Pasteur / GPT-5.5 low | agent fork workspace | `019e5788-86ea-7ff3-bf3d-9e1cf3f979ed` | `categories/posets.pyi`, `categories/finite_posets.pyi`, `categories/finite_lattice_posets.pyi`, `combinat/posets/posets.pyi` | poset order operations, finite poset/lattice morphism callable domains | `ordinary_error_count=1759` | closed: no merge; provider methods already exist, and current poset rows are research typing/design variance or receiver-container conflicts | cleaned by agent close |
| Integer/numeric protocol audit | Mendel / GPT-5.5 low | agent fork workspace | `019e5789-89dc-75a3-9f9f-d284269806d5` | `rings/integer.pyi` | `Integer` constructor/protocol/arithmetic/comparison rows, excluding combinatorics k-domain | `ordinary_error_count=1759` | closed: no merge; current integer stub already has source-backed constructor/index/arithmetic surfaces, and remaining rows are research-local containers, Infinity unions, or other-lane ownership | cleaned by agent close |
| Combinatorics tarpit cleanup | Avicenna / GPT-5.5 low | agent fork workspace | `019e578d-ce29-7dc2-ae0d-c497be7b661f` | `combinat/subset.pyi`, `combinat/set_partition.pyi` | source-backed `Subsets(..., Integer(k))` and `SetPartition(blocks, check=...)` with touched-file gate cleanup | `ordinary_error_count=1759` | active after Spark capacity exhaustion | close after merge/rejection and registry update |
| Matrix/module constructors | Hilbert / GPT-5.5 low | agent fork workspace | `019e578e-12c1-7c13-a694-fdb8ec7a69ef` | `matrix/constructor.pyi`, `matrix/matrix_space.pyi`, `matrix/matrix.pyi`, `matrix/matrix2.pyi`, `modules/free_module.pyi` | matrix, MatrixSpace, FreeModule, VectorSpace, FreeQuadraticModule constructor rows | `ordinary_error_count=1759` | closed: no merge; current rows are category_specs receiver/protocol mismatches while source-backed constructor and Parent surfaces are already represented | cleaned by agent close |
| CFM and with-basis surfaces | Ptolemy / GPT-5.5 low | agent fork workspace | `019e578e-516f-7d92-9709-763638a70f7c` | `combinat/free_module.pyi`, `sets/family.pyi`, with-basis category stubs | CombinatorialFreeModule rows, `_refine_constructed_module`, `AbstractFamily.keys`, with-basis provider rows | `ordinary_error_count=1759` | closed: no merge; tested CFM broadening failed type-surface review, `AbstractFamily.keys` already exists, and finite-rank methods live on tensor module sources | cleaned by agent close |

## Lazy callable stream

Purpose:

The issue lists `LazyImport` callability as the highest row-count blocker. This
stream should handle it separately because the surface is high-impact and easy
to over-broaden.

Owned files:

- `sage-stubs/misc/lazy_import.pyi`
- `sage-stubs/categories/covariant_functorial_construction.pyi`
- direct callable/functor sidecars needed for `TensorProductFunctor`

Target diagnostics:

- `LazyImport` not callable rows.
- assignment rows caused by lazy category factories being treated as non-callable.
- `TensorProductFunctor` callable rows, if still present after current baselines.

Required source evidence:

- Sage `LazyImport.__call__` implementation and runtime examples where a
  resolved callable object is callable.
- Sage functorial construction source showing inherited `__call__` behavior for
  tensor product functors.

Implementation guidance:

- Do not make every `LazyImport` an untyped callable escape.
- Prefer a source-backed generic or overload that preserves the distinction
  between lazy objects that are callable factories and lazy objects that are
  plain values.
- If Python typing cannot express the precise dependent behavior, implement the
  narrowest accepted callable surface that removes observed Sage factory rows
  without masking arbitrary calls.

Acceptance:

- The targeted callable rows fall substantially.
- No new `Any`, `object`, or `Callable[..., ...]` opacity appears.
- Existing non-callable lazy import surfaces are not weakened.

## Integer and numeric protocol stream

Purpose:

Remove numeric protocol failures caused by over-narrow Sage `Integer` stubs and
integer-like parameters, while preserving the distinction between Python `int`,
Sage `Integer`, and parents such as `ZZ`.

Owned files:

- `sage-stubs/rings/integer.pyi`
- narrow supporting stubs for numeric protocols only when source requires them

Target diagnostics:

- unsupported arithmetic on `Integer`;
- invalid index use involving `Integer`;
- constructor rows such as `Integer(<set element>)` only where Sage source or
  runtime accepts that input;
- default mismatches where source uses Python `int` but a stub says `Integer`,
  or conversely where Sage requires `Integer`.

Already handled:

- `Integer.__sub__` and `Integer.__rsub__` overloads for integer and rational
  operands are committed and validated.

Required source evidence:

- `sage-src/src/sage/rings/integer.pyx` direct method bodies.
- Runtime checks with `sage -python` for protocol methods that Cython exposes
  indirectly and source search does not show clearly.

Implementation guidance:

- Add protocols such as `__int__`, `__index__`, arithmetic overloads, or
  comparison overloads only when Sage source/runtime proves them.
- Do not flip `int` to `Integer` across unrelated surfaces merely because one
  row mentions `Integer`.
- Do not annotate parent objects such as `ZZ` as `int` or `Integer`.

Acceptance:

- Numeric rows drop without causing `int`/`Integer` churn in downstream specs.
- Mypy still accepts the standalone `integer.pyi` file under strict mode.

## Category core shape stream

Purpose:

Fix real Sage category construction, membership, and base-object shapes without
inventing dynamic category methods that issue #5 explicitly excludes.

Owned files:

- `sage-stubs/categories/category.pyi`
- `sage-stubs/categories/category_with_axiom.pyi`
- `sage-stubs/categories/category_types.pyi`
- `sage-stubs/categories/category_singleton.pyi`
- narrow category sidecars required by direct Sage source

Target diagnostics:

- `Category.__init__` and `CategoryWithAxiom` argument-shape rows.
- `Category_over_base`, `Category_over_base_ring`, and `Category_in_ambient`
  initializer rows.
- category membership rows such as `ZZ in PrincipalIdealDomains()` and
  `ZZ in Rings()`.
- remaining `Category.__classcall__` argument-domain rows after the pending
  `Integer` edit.
- `additional_structure` only if a refreshed ledger still shows it.

Explicit non-goals:

- Do not add `Category.FinitelyPresented`, `Category.OverPID`,
  `Category.Quotients`, `Category.Subobjects`, `Category.Connected`,
  `Category.Infinite`, `Category.Finite`, or similar generic dynamic methods
  to base `Category`.
- Do not model local `category_specs.cat` receiver erasure in `sage-stubs`.

Required source evidence:

- direct bodies in `sage.categories.category`,
  `sage.categories.category_with_axiom`, and `sage.categories.category_types`;
- runtime membership examples only after source has been read.

Implementation guidance:

- Prefer precise constructor/classcall domains already accepted by Sage source.
- Keep dynamic-constructor failures in the reclassification queue unless a
  concrete Sage category class directly exposes the method.
- Treat `Category` vs `Parent` vs `CategoryObject` broadening as high risk.

Acceptance:

- Source-backed category shape rows drop.
- Dynamic-constructor non-goals remain absent from stubs.

## Sets core stream

Purpose:

Fix real set-construction and parent-method surfaces that category_specs uses
directly.

Owned files:

- `sage-stubs/sets/condition_set.pyi`
- `sage-stubs/sets/recursively_enumerated_set.pyi`
- `sage-stubs/sets/real_set.pyi`
- `sage-stubs/sets/image_set.pyi` or the actual ImageSubobject stub path
- `sage-stubs/structure/parent.pyi` only if source-backed parent methods are
  required and the stream commits the necessary legacy cleanup

Target diagnostics:

- `ConditionSet` ambient/universe argument shape.
- `RecursivelyEnumeratedSet` seed/successor/post-process variance.
- `RealSet` and `ImageSubobject` parent element methods.
- set parent methods such as `an_element`, `_an_element_`, or `is_facade` only
  when Sage source exposes them on the target surface.

Required source evidence:

- `sage-src/src/sage/sets/condition_set.py`.
- `sage-src/src/sage/sets/recursively_enumerated_set.pyx`.
- source for RealSet and ImageSubobject actual modules.
- `sage.structure.parent` only for direct parent methods.

Implementation guidance:

- Avoid turning recursive set element domains into broad `object`.
- If a file is a legacy tarpit, clean only the violations needed to make the
  touched file committable. Do not rewrite the whole module unless the local
  gate requires it.
- For callable predicates, distinguish concrete callable domains from symbolic
  `Expression` predicates.

Acceptance:

- Targeted set rows fall.
- No new final-method override issues are hidden by weakening stubs.

## Combinatorics constructor stream

Purpose:

Handle combinatorics files that are known legacy tarpits and therefore should
not block cleaner workstreams.

Owned files:

- `sage-stubs/combinat/subset.pyi`
- `sage-stubs/combinat/set_partition.pyi`
- supporting `sage-stubs/sets/set.pyi` changes only if required by source

Target diagnostics:

- `Subsets([..], Integer(k))` accepted by source coercion through `Integer(k)`.
- `SetPartition(blocks, check=...)` direct classcall surface.

Known local blockers:

- `subset.pyi` currently has staged-check blockers involving `object` in
  `__contains__`, `__call__`, and override mismatches.
- `set_partition.pyi` has legacy `object` violations.

Required source evidence:

- `sage-src/src/sage/combinat/subset.py`, especially `Subsets` and
  `Subsets_sk.__init__`.
- `sage-src/src/sage/combinat/set_partition.py`, especially direct classcall
  and initializer paths.

Implementation guidance:

- Treat this as cleanup-aware implementation, not a one-line k-domain edit.
- Preserve all existing public definitions unless Sage source proves them wrong.
- For `__contains__`, use concrete finite unions from source behavior.
- For `__call__`, replace opaque variadics with the narrow parent-call shape
  that Sage source supports.

Acceptance:

- The target constructor rows disappear.
- The touched files pass `check_stubs.py`, guardrails, Ruff, and strict mypy.

## Matrix and module constructor stream

Purpose:

Remove construction failures around matrices, matrix spaces, free modules, and
vector spaces. This stream is large but coherent because the errors share
constructor domains and matrix class aliases.

Owned files:

- `sage-stubs/matrix/constructor.pyi`
- `sage-stubs/matrix/matrix_space.pyi`
- `sage-stubs/matrix/matrix.pyi`
- `sage-stubs/matrix/matrix2.pyi`
- `sage-stubs/modules/free_module.pyi`
- narrow constructor support under `sage-stubs/modules/`

Target diagnostics:

- `matrix(..., nrows=Integer, ncols=Integer)`.
- `MatrixSpace(ZZ, Integer(2), Integer(2))`.
- `MatrixSpace` as a `Parent`.
- matrix dimensions returning `Integer` or `int` according to source.
- `FreeModule` and `VectorSpace` base ring/field, rank, `with_basis`, and
  `inner_product_matrix` domains.
- `FreeQuadraticModule` matrix class mismatch rows.

Known local blockers:

- `matrix_space.pyi` and `modules/free_module.pyi` contain legacy `object`
  violations. Assign this stream to a worker prepared to clean those touched
  files enough to commit.

Required source evidence:

- Sage matrix constructor source and MatrixSpace source.
- Sage free module and vector space factory source.
- Runtime checks for Cython class aliases such as `matrix.Matrix` vs
  `matrix2.Matrix` when source alone is ambiguous.

Implementation guidance:

- Do not use `object` for matrix entries. Use source-backed scalar/container
  unions or overloads.
- Preserve semantic bases: do not replace `VectorSpace` with
  `FreeModule_generic` unless Sage source proves the returned object.
- Keep matrix class aliasing explicit rather than broadening to a parent class.

Acceptance:

- Matrix/module constructor rows drop.
- No precise class base is flattened.

## Combinatorial free module and with-basis stream

Purpose:

Finish remaining combinatorial free module rows and with-basis family surfaces
that are independent of the large `modules/free_module.pyi` constructor tarpit.

Owned files:

- `sage-stubs/combinat/free_module.pyi`
- `sage-stubs/sets/family.pyi`
- `sage-stubs/categories/modules*.pyi`
- `sage-stubs/categories/modules_with_basis.pyi` or actual with-basis paths

Target diagnostics:

- remaining `CombinatorialFreeModule` base ring and basis-key argument rows;
- `_refine_constructed_module` rows caused by returned module base shape;
- `AbstractFamily.keys` union-branch rows only where the Sage family surface is
  truly missing;
- finite-rank free-module category methods if they live in category provider
  stubs rather than module constructor files.

Already handled:

- `CombinatorialFreeModule.element_class` now accepts Sage `Element` subclasses
  and is committed.

Required source evidence:

- `sage-src/src/sage/combinat/free_module.py`.
- `sage-src/src/sage/sets/family.py`.
- source for with-basis category provider modules.

Implementation guidance:

- Do not broaden `CommutativeRing` to arbitrary `Parent` unless Sage source
  accepts it.
- If category_specs receiver aliases are too broad, classify that separately
  rather than weakening Sage stubs.
- Keep basis key domains hashable unless source accepts non-hashable keys.

Acceptance:

- CFM rows drop without weakening module semantics.

## Rings, fields, and completions stream

Purpose:

Handle ring/field leaf surfaces that issue #5 lists as stubs-owned.

Owned files:

- `sage-stubs/rings/ring.pyi`
- `sage-stubs/rings/commutative_ring.pyi`
- `sage-stubs/rings/rational_field.pyi`
- `sage-stubs/rings/polynomial/polynomial_ring.pyi`
- `sage-stubs/rings/abc.pyi`
- real field stubs under `sage-stubs/rings/real_*`

Target diagnostics:

- `CommutativeRing.extension` and related override rows.
- `PolynomialRing_generic.completion`.
- RationalField public methods that Sage source/runtime provides.
- `RealField`, `RealDoubleField`, and `RealIntervalField` `to_prec` surfaces.
- precision/default rows only where source proves the accepted domain.

Required source evidence:

- Sage source for ring, commutative ring, polynomial ring, rational field, and
  real field classes.
- Runtime checks for Cython/ABC aliases when method exposure differs from Python
  source layout.

Implementation guidance:

- Do not add `extension` to an unrelated superclass merely to satisfy override
  rows. Put it on the source-backed Sage class.
- Do not add broad number-field-like methods to `RationalField` unless direct
  Sage source/runtime shows them.
- Keep `Integer`, `int`, and precision parent types separate.

Acceptance:

- Listed ring rows drop.
- No unrelated ring API is widened.

## Posets stream

Purpose:

Clean remaining poset category variance and provider-method rows after the
finite poset certificate fixes.

Owned files:

- `sage-stubs/categories/posets.pyi`
- `sage-stubs/categories/finite_posets.pyi`
- `sage-stubs/categories/finite_lattice_posets.pyi`
- `sage-stubs/combinat/posets/posets.pyi`

Target diagnostics:

- argument/return variance for `le`, `lt`, `ge`, `gt`, `upper_covers`,
  `lower_covers`, `order_ideal`, `order_filter`, and related order operations;
- finite poset morphism and lattice morphism callable domains;
- provider rows where category_specs element protocols are narrower than Sage
  `Element | Hashable`.

Already handled:

- `FinitePoset.height`, `width`, `is_meet_semilattice`, and
  `is_join_semilattice` certificate overloads are committed and validated.

Required source evidence:

- `sage-src/src/sage/categories/posets.py`.
- `sage-src/src/sage/categories/finite_posets.py`.
- `sage-src/src/sage/categories/finite_lattice_posets.py`.
- `sage-src/src/sage/combinat/posets/posets.py`.

Implementation guidance:

- Do not add inherited methods as direct methods on `FinitePoset`.
- Prefer category provider stubs when source defines methods in
  `ParentMethods`.
- Be cautious about list element variance: changing `list[Element | Hashable]`
  may be a weakening or a downstream protocol mismatch rather than a Sage stub
  defect.

Acceptance:

- Poset rows drop or are reclassified with source evidence.

## Homsets and morphisms audit stream

Purpose:

Separate real homset/morphism stub gaps from explicit non-goals such as base
`Morphism.is_invertible`.

Owned files:

- `sage-stubs/categories/homsets.pyi`
- `sage-stubs/categories/homset.pyi`
- `sage-stubs/categories/morphism.pyi`
- `sage-stubs/structure/parent.pyi` only for source-backed `Hom` or inclusion
  methods

Target diagnostics:

- `default_super_categories` missing sidecar rows if source-backed.
- `Parent.Hom` shape rows if source-backed.
- `Parent.inclusion` only if Sage source exposes it on `Parent`.
- `Morphism.is_invertible` rows should remain rejected unless new source/runtime
  evidence proves a base method.

Required source evidence:

- Sage homsets, homset, morphism, and parent source files.
- Runtime checks only after source search.

Implementation guidance:

- Keep the explicit #5 non-goal: no base `Morphism.is_invertible`.
- Do not use local wrapper concepts to satisfy homset type aliases.

Acceptance:

- Source-backed homset rows drop.
- Non-goals are documented as rejections, not hidden by broad stubs.

## Final reconciliation stream

Purpose:

Close issue #5 only when the stubs-owned queue is proven empty or every
remaining row has a source-backed rejection/reclassification.

Owned artifacts:

- issue #5 comment and closure
- final downstream ledger proof
- commit list

Required final evidence:

- latest `sage-stubs` commit hash;
- full command transcript summary for `just check`;
- full downstream validation summary:

```bash
cd /home/dzack/research
sage -python -m pip install --force-reinstall /home/dzack/sage-mypy-plugin/sage-stubs
just category-specs-mypy-structural-report-full
just category-specs-mypy-ledger
jq '{ordinary_error_count, counts_by_owner}' reports/workstreams/category-specs-mypy-ledger/latest.json
```

- stubs-owned row reconciliation: implemented, rejected, reclassified, and zero
  unresolved stubs-owned rows;
- explicit confirmation that no fake surfaces were added;
- exact source/runtime evidence for every rejection or reclassification.

Acceptance:

- The 370 stubs-owned rows are 0, modulo source-backed reclassification.
- issue #5 has a closing comment with proof.
- issue #5 is closed.

## Parallel execution protocol

Use this protocol for all workers.

Coordinator dispatch:

- Start from `WORKSTREAM.md`, not from an ad hoc prompt.
- Assign one stream, one primary target row family, and one owned file set.
- Tell the worker which files are off-limits.
- Include the current baseline ledger count and target `jq` filter.
- Require a worker report with diff summary, source citations, type-surface
  classification, local gates, downstream delta, and blockers.
- Prefer async subagent execution for independent streams so the coordinator can
  monitor several lanes at once.

Worker startup:

- Create or switch to an isolated branch/worktree.
- Read `AGENTS.md`, `README.md`, `justfile`, issue #5, `WORKSTREAM.md`, and the
  relevant Sage source files.
- Capture the baseline ledger count before editing.
- State the exact rows or regex target for the stream.

Worker implementation:

- Touch only owned files.
- If a required change crosses into another stream's owned file, stop and report
  the dependency instead of editing across ownership boundaries.
- For every changed stub annotation, cite source/runtime evidence.
- Keep commits small enough that one downstream delta explains the result.

Worker report:

- Start with the downstream delta and targeted row result.
- Include source evidence and type-surface review classification.
- Name unresolved blockers using the five-field negative-finding format.
- Do not report a row as impossible from a narrow failed grep. Broaden first.

Coordinator merge:

- Inspect the diff, not the worker summary.
- Run local gates and downstream validation again after merge.
- Commit only the files intended for that workstream.
- Update issue #5 only with evidence that matters for closing or reclassifying
  rows.
- Remove or close the worktree/task registry entry immediately after merge,
  rejection, or reassignment.

Worktree discipline:

- Use worktrees only for streams with disjoint file ownership or high context
  isolation value.
- Create one worktree per active stream and record it in the registry before
  dispatch.
- Do not let an unregistered worktree persist.
- Do not reuse a worktree for another stream until the previous stream is merged,
  rejected, or explicitly abandoned and cleaned.
- Remove stale worktrees immediately after the coordinator records the outcome.

## Suggested merge order

Merge order should minimize conflicts and make row deltas interpretable.

- Commit validated `Category.__classcall__` `Integer` edit first.
- Merge clean single-file streams next: Integer/numeric, existing clean set
  files, and clean ring leaf files.
- Merge high-impact Lazy callable stream after a dedicated review pass.
- Merge category core shape before module/ring dynamic-constructor
  reclassification decisions.
- Merge large legacy-tarpit streams last: combinatorics constructor cleanup,
  matrix/module constructors, and `structure/parent.pyi` work.
- Run final reconciliation only after all implementation streams either merged
  or produced source-backed rejections.

## Work allocation summary

These streams can run in parallel immediately because their primary file
ownership is disjoint:

| Stream | Primary files | Parallel risk |
|--------|---------------|---------------|
| Lazy callable | `misc/lazy_import.pyi`, functor stubs | medium |
| Integer/numeric | `rings/integer.pyi` | low |
| Sets core | `sets/condition_set.pyi`, `sets/recursively_enumerated_set.pyi` | medium |
| Combinatorics | `combinat/subset.pyi`, `combinat/set_partition.pyi` | high |
| Matrix/module constructors | `matrix/*`, `modules/free_module.pyi` | high |
| CFM/with-basis | `combinat/free_module.pyi`, `sets/family.pyi` | medium |
| Rings/fields | `rings/*`, polynomial stubs | medium |
| Posets | `categories/*posets*.pyi`, `combinat/posets/posets.pyi` | medium |
| Homsets/morphisms | `categories/*hom*.pyi`, `morphism.pyi` | medium |

The category core stream conflicts with many downstream interpretations. Run it
as a coordinator-supervised stream and merge it before treating dynamic
constructor rows as stubs-owned.
