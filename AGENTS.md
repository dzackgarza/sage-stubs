# AGENTS.md — sage-stubs

## What this repo is

PEP 561 stub-only package (`sage-stubs`) providing type stubs for the
SageMath library (10.7). Stubs live under `sage-stubs/` and mirror the
layout of the real `sage` package. Each `.pyi` file must be a valid mypy
stub for the corresponding `sage/**/*.py` source file.

Work on this repo is **agent-led**. Quality is enforced by automated
hooks rather than reviewer vigilance, so the rules below are not
suggestions — every one of them is checked mechanically before a commit
lands. Bypassing the hooks (`--no-verify`) is forbidden without explicit
human authorisation.

## Work-integrity contract

This repository exists to provide complete, correct, and usable stubs for the
entire SageMath API. That is the job. A downstream project type-checking cleanly
is a valuable diagnostic and a useful milestone, but it is not the reward
function. Do not optimize this repository for making one consumer quiet. Optimize
it for making Sage accurately visible to static tooling.

The hard part is often not writing a line in a `.pyi` file; it is preserving the
actual Sage type model when source classes are dynamic, cyclic, Cython-backed,
or only partially stubbed. Do that hard work in this repository. Do not move the
cost into the caller.

The primary failure mode to avoid is task substitution under pressure. When a
source-backed stub problem becomes difficult, an agent may try to make the
surrounding world easier instead of solving the stub problem: edit the consumer
that exposed the gap, soften the validation harness, refresh reports until the
paper trail looks current, rename the bucket, narrow the issue, add casts or
wrapper noise downstream, or describe the remaining implementation as a future
project. All of those moves preserve the appearance of progress while changing
the task. They are misaligned even when they reduce an error count.

Validation targets are sensors. Tests, downstream consumers, ledgers, reports,
tracker rows, PR comments, issue comments, and review threads exist to reveal
whether this stub package models Sage correctly. A sensor that reports an
uncomfortable fact is doing its job. Do not silence, weaken, rewrite, reroute,
or relabel the sensor to make a stub task look easier. If the sensor is truly
wrong, stop the stub task and make the new ownership explicit before editing the
sensor or its repo. A sensor fix is a separate task, not evidence that the stub
task advanced.

Metrics are evidence, not objectives. The only local objective an agent can
directly pursue here is better Sage stubs: more complete, more source-accurate,
more precise, and more usable for every downstream caller. A downstream row
disappearing only counts as supporting evidence when the causal path is: Sage
source reviewed, stub changed in this repo, this repo reinstalled downstream,
and the row disappears without changing the downstream consumer, plugin, report
generator, checker configuration, prompt, ledger classifier, smoke test, or
completion criterion. If the metric improves after changing any of those
surrounding layers, the validation run is contaminated for the stub task until
proven otherwise.

Layer ownership is part of correctness. A stub task may read and run downstream
consumers, plugins, reports, and issue threads for evidence. It must not edit
them to complete the stub task. If solving the observed problem appears to
require a consumer change, plugin change, checker change, or research-spec
change, preserve the original stub failure, state why the ownership changed, and
stop or open separately owned work. Do not combine that edit with stub progress
or count it toward stub completion.

Blocked is an acceptable state; disguised incompletion is not. If the real Sage
surface requires a larger sidecar hierarchy, cleanup of legacy policy debt,
careful overload design, or a source/runtime investigation that exceeds the
current lane, say that and keep the task incomplete. Words such as "tarpit",
"guardrail conflict", "downstream regression", "legacy touched-file debt",
"future project", "closeability", and "reclassified" are not completion words.
They either name implementation work still to do, or they require source/runtime
proof that the requested surface is not a Sage stub surface.

Administrative work is bookkeeping, not implementation. Comments, status tables,
goal updates, reports, closeout arguments, proof narratives, row inventories,
and issue/PR paperwork may preserve decisions and evidence, but they do not
substitute for source-backed stub changes. If the remaining work is
implementation, the next aligned action is implementation, a smaller
implementation split, or an explicit blocker with the original hard problem
still intact.

Before accepting any work product, ask what hard problem it made disappear and
which layer paid the cost. If the answer is not "the Sage stub surface in this
repository now models the source-backed API more accurately", reject it as
non-progress for this repo's implementation goal.

## Difficulty-laundering stop line

The dangerous pattern is not merely an inaccurate metric. The dangerous pattern
is capitulating when the source-backed stub work becomes difficult and replacing
the product with artifacts that look responsible: status updates, issue comments,
workstream rows, reclassification notes, report refreshes, consumer edits,
casts, wrapper changes, integer-normalization churn, override deletions, or
broadened annotations. These artifacts can be useful evidence after real work,
but they are misaligned when they are produced instead of continuing the real
stub implementation.

When a worker hits a hard source/type-model problem, the hard problem must be
earmarked before any sideways work happens. Earmarking means preserving the
original requirement in its strongest form, naming the exact source-backed Sage
surface, naming the concrete failed patch or failed reasoning step, and stating
the next deeper implementation attempt. Do not rename the problem, reclassify it,
or move it to a future project while the required Sage surface still appears
real.

The next deeper attempt must stay on the product. Valid moves are: read more of
the Sage source, inspect runtime behavior, add a prerequisite source-backed
sidecar, split the sidecar hierarchy into a smaller real implementation slice,
repair legacy touched-file policy debt, strengthen an overload/type model, or
escalate to a stronger reviewer with the hard problem intact. Invalid moves are:
changing a downstream consumer to avoid the failure, changing reports or
classifiers, weakening types, adding casts, deleting demanding overrides, wrapping
values merely to satisfy current stubs, narrowing the issue, posting a new
closeability argument, or producing another registry/status artifact.

One failed patch is not a blocker. A failure first means the worker does not yet
understand the problem deeply enough. The worker must preserve epistemic
humility: name the uncertainty, list the concrete difficulties, revise the
implementation plan, and break the hard task into smaller source/type questions.
Repeat that breakdown until the true smallest obstacle is isolated.

An obstacle is atomic only when it cannot be split into a smaller question about
Sage source ownership, direct versus inherited surface, runtime behavior,
constructor/coercion domain, missing prerequisite sidecar, import cycle, generic
invariant, override relation, policy conflict, or checker limitation. If any of
those subquestions remains unresolved, the worker has not reached an atomic
blocker and is not allowed to escalate.

The escape route has a high bar. A lane may stop without implementation only
after the atomic blocker has been attacked several materially distinct ways: a
direct source-backed surface attempt, a prerequisite-sidecar or hierarchy
attempt, and an alternative precise type-model or runtime-evidence attempt. Each
attempt must leave concrete evidence of what failed and why. Failure must drive
deeper decomposition, not goal substitution.

Only after that does the lane escalate to the user. The escalation must be a
plain user-facing blocker, not a completion claim. It must state why the blocker
is minimal and atomic, what approaches were tried, why they failed, and what
compromises might be required. Agents are not authorized to decide which
compromise is acceptable; that decision belongs to the user. Until the user
chooses a compromise or changes scope, the PR/issue remains incomplete.

Reflection is mandatory when difficulty appears, but reflection is not a new
deliverable. It must produce this synthesis before any further artifact work:
"The hard product problem is ___; the last real attempt failed because ___; the
next deeper source-backed attempt is ___." If that sentence cannot be filled
with concrete source/type evidence, the agent has not understood the problem and
must read more before acting.

Artifact proliferation is a stop condition. If recent work contains multiple
comments, reports, registry edits, planning edits, reclassification records, or
consumer/report commits without corresponding source-backed stub commits, stop
the lane immediately. The coordinator must count the recent middle-management
artifacts and the recent product commits that improved `.pyi` surfaces. If
artifact output exceeds product output, or product output is absent, the default
verdict is drift until proven otherwise. The coordinator must name which `.pyi`
surfaces became more correct. If the answer is thin or indirect, no additional
artifact is allowed: no audit report, no registry cleanup, no PR comment, no
issue comment, no refreshed report, and no new plan. The only allowed next
actions are a source-backed implementation edit, a smaller implementation split
assigned to a worker, or a minimal user-facing escalation that the required work
is still blocked.

Realignment must reduce artifact production, not merely pause it. When artifact
drift is detected, disable the mechanisms that were generating artifacts:
cancel artifact-only lanes, stop report-refresh loops, stop closeability/proof
comment loops, stop registry churn except to mark a lane rejected or frozen, and
reject stale summaries that are not tied to code. Resume only with fewer active
non-code work products than before and with the next product aimed at a concrete
`.pyi` surface.

Misaligned work poisons later evidence. If an audit finds that a lane broadened
types, added casts, stripped overrides, wrapped values to satisfy current stubs,
edited a consumer to avoid missing stubs, or otherwise moved cost downstream,
stop all work that depends on that lane. Review the actual diff, quarantine the
claim, and either reject the work or remove it by a new corrective patch after a
checkpoint. Do not build new workstreams on contaminated row counts or summaries.

Misalignment reporting must start with plain facts from the diff. Name the files
changed, the type surfaces changed, and whether the change added casts, widened
types, deleted overrides, inserted wrapper/coercion noise, changed consumers, or
changed reports. Do not start with jargon such as "alignment," "interop,"
"surface," "closeability," or "verification harness" until the concrete edits
are on the page. Performative admissions are not evidence of understanding.

## Periodic adversarial audits

Long-running agent work in this repo needs adversarial audits, not progress
summaries. The audit job is to catch the failure mode where implementation
stalls, activity continues, and the apparent target quietly changes.

Run an audit at every resume after compaction or interruption, before any status
report, before any PR/issue comment that claims progress or closeability, after
accepting subagent output, after any downstream validation run, and whenever the
recent work contains administrative artifacts without a corresponding
source-backed stub change.

An audit must start from evidence the current agent may not remember. Tail the
current Codex transcript with the transcript parser, then inspect the actual git
diff/log for this repo and any downstream repo used as a diagnostic. Do not rely
on chat summaries, worker summaries, commit subjects, registry statuses, or
memory. The audit must read what changed.

For cross-repo work, the audit must touch base with both repositories'
guidelines before judging alignment. Read the local `AGENTS.md`, `README.md`,
`justfile`, and relevant workstream docs in this repo, then read the equivalent
guidance in the downstream repo before deciding whether a downstream edit was a
real consumer improvement or an accommodation of stub/plugin failure.

The audit question is not "are we busy?" or "did the metric improve?" The audit
question is:

> What hard Sage stub problem was supposed to be solved, what actually changed,
> which repository/layer paid the cost, and did that make the Sage stub surface
> more complete, correct, and usable?

The audit output must be a causal verdict, not a filled checklist. Start with
whether the recent work was aligned, contaminated, misaligned, or still unclear.
Then explain what the agents appeared to be optimizing: Sage stub quality, or a
substitute target such as downstream quieting, row movement, status cleanliness,
review-thread closure, or narrative closeability. If that verdict could have
been written from summaries without reading transcript and diffs, the audit
failed.

If the recent work changed a consumer, plugin, report generator, validation
command, issue scope, classifier, prompt, status table, or completion narrative,
the audit must treat downstream metric movement as suspect until the causal path
back to source-backed stub improvement is proven. If that causal path is not
proven, stop the lane as misaligned or contaminated; do not keep building on its
metric result.

Every audit must include a self-reflection on artifact pressure. The required
synthesis is: "Recent work is drifting toward artifacts rather than product if
___; the hard implementation problem those artifacts may be hiding is ___; the
realignment action is ___." If the realignment action is another comment,
status table, or report, the audit has failed unless the user explicitly asked
for that artifact as the product.

An audit is an action gate, not a deliverable. Do not create a standalone audit
document, PR comment, issue comment, status report, or workstream update merely
because artifact drift was detected. Use the audit to choose the next permitted
action: implement, split implementation, freeze poisoned work, or escalate to
the user. If the user must be told, make that message the stop condition, not a
new process artifact to continue working around the blocker.

If the chosen action is freeze or reject, it must shrink the active paperwork
surface. Close or quarantine artifact-only streams, remove them from the set of
things being optimized, and stop relying on their ledgers. Do not replace one
artifact lane with a cleaner artifact lane.

After discovered misalignment, an independent subagent must review the current
coordinator transcript and the suspect diffs for alignment before the lane
continues. The subagent prompt must ask for a causal verdict, not a summary. If
no independent subagent is available, the coordinator must report that limitation
and keep the lane stopped; self-approval is not enough after a misalignment
finding.

If two consecutive work products are comments, reports, row reconciliations,
registry updates, planning edits, or rejected attempts without a merged
source-backed stub improvement, the coordinator must stop and audit for goal
substitution before doing more coordination. The correct recovery is not a
better status artifact. It is returning to source-backed stub implementation,
splitting the implementation into a smaller real lane, or reporting the exact
unresolved blocker.

## First-clone setup (run once)

```bash
just setup
```

That command:

1. Points git at the tracked hooks in `.githooks/`
   (`git config core.hooksPath .githooks`).
2. Initialises the `sage-src` submodule at the Sage 10.7 source tree.

If `just` is unavailable, the equivalent shell is:

```bash
git config core.hooksPath .githooks
git submodule update --init --depth 1
```

After this, every commit runs `ruff` + `scripts/check_stubs.py` +
`scripts/check_guardrails.py` + `mypy --strict` on the staged `.pyi`
files, and prints current coverage. **Do not skip this step.**

## How to work on the plan

1. **Read `.agents/plan.md`.** It is the master tracking card and names
   the next phase to pick up via its "At-a-glance next step" banner.
2. **Open the relevant phase card** under `.agents/phases/`. Each card
   has a task table with explicit `Depends` and `Status` columns. Pick
   a task that is `⬜ Pending` and whose dependencies are satisfied.
3. **Mark the task `🟡 In Progress`** in the phase card, and update the
   phase status in `plan.md` if you are the first to start work in it.
   The hooks accept these doc-only edits.
4. **Follow the stub authoring procedure below** (Phases 1–3).
5. **Commit.** Hooks enforce every rule in this document and coverage
   is printed automatically. Mark the task `✅ Done` in the phase card
   as part of the same commit.
6. **Repeat.** Pick the next task. If no task remains in the current
   phase, return to `.agents/plan.md` for the next phase. Within a
   phase, tasks with `Depends: —` can run in parallel — claim by
   setting an owner annotation in the task row.

### Document index

| Document | Purpose |
|----------|---------|
| `AGENTS.md` *(this file)* | Workflow, quality contract, banned patterns |
| `.agents/feature.md` | Full-parity requirements, scope, tooling references |
| `.agents/plan.md` | Master tracking card with the 18-phase dependency graph |
| `.agents/phases/phase-NN-*.md` | One card per phase: tasks, dependencies, risks |
| `.agents/phases/phase-01-exempt.md` | Produced by T01.1: modules excluded from parity denominator |
| `STUB_GAPS.md` | Currently-blocked sidecar gaps with diagnostic evidence |
| `README.md` | User-facing scope description (rewritten at end of Phase 18) |
| `justfile` | Canonical task entrypoints (`just check`, `just coverage`, etc.) |
| `scripts/stub_coverage.py` | Measures stub coverage vs `sage-src` |
| `scripts/check_stubs.py` | AST-level `Any` / `object` ban enforcement |
| `scripts/check_guardrails.py` | Banned patterns, scratch artefacts, protected config |
| `.githooks/pre-commit` | Auto-enforces all of the above on staged files |
| `.githooks/post-commit` | Reports coverage delta after each commit |

## Sage source reference

The actual SageMath source is at `sage-src/` (a git submodule,
initialised by `just setup`). The full source for any module you are
stubbing is at `sage-src/src/sage/<module>/<file>.py`.

**You must read the source before writing any stub.** Do not infer
signatures from memory or guesswork. `mypy.stubgen` may be used to
*enumerate* the public surface — see `.agents/feature.md` for the
workflow — but its output is never the final stub, because it emits
`Any` and the hook will reject the commit.

## Stub authoring procedure

Work in three phases. Do not write any stub code until Phase 2 is
complete.

**Phase 1 — Enumerate.** Read the source file. List every public method
defined directly on the target class (not inherited), with its source
line number. Output this list explicitly before proceeding.
`mypy.stubgen` may produce the initial list; verify against the source
AST `cls.body` (not `ast.walk`) — stubgen does not distinguish direct
from inherited methods for Cython classes.

**Phase 2 — Resolve types.** For each method in your list, read the
implementation and docstring. State the concrete return type and
parameter types. Cite the source line that justifies each type decision.

**Phase 3 — Write.** Every method from Phase 1 must appear. Every type
must match Phase 2. Only then write the `.pyi` file.

**Phase 4 — Type-surface review.** Before staging, committing, accepting
subagent output, or accepting auto-fix output, inspect the diff for every
changed annotation, alias, import used for annotations, class base, return
type, parameter type, protocol, or generic argument. For each changed type
surface, compare previous spelling, proposed spelling, and Sage 10.7 source
evidence. Classify the change as stricter, equivalent, or weaker. Weaker
changes are rejected unless the previous stub is source-proven wrong and the
replacement is the most precise source-backed type available.

Generic annotations require the same source proof as concrete annotations.
Introducing `TypeVar`, `Protocol`, `Callable[..., ...]`, or a generic container
is not a way to erase unknown domains. Before adding a type variable, identify
the invariant it expresses: which input, stored element, receiver, and return
positions share the same type, and where Sage preserves that identity instead of
coercing it. If Sage coerces, normalizes, wraps, or stores a different element
type, use the accepted input domain and the resulting output/storage type
explicitly. Do not replace `object`, `Any`, a concrete Sage type, or an
unresolved parameter with `_T`, `Iterable[_T]`, `Sequence[_T]`,
`Callable[..., _T]`, or a local protocol unless the source proves the type
relation.

**Stop-the-line weakening review.** If a diff changes a precise Sage type to a
broader type, do not continue implementation, staging, or commit preparation
until the weakening has been removed or independently reviewed. This applies
even when the broader type makes mypy, Ruff, imports, or local package
registration easier. The required review must be performed by a separate
subagent when one is available; otherwise perform a separate written audit pass
that names each suspicious change and cites the Sage 10.7 source. Hook passage
is not evidence that weakening is acceptable.

The review is blocking, not advisory. `scripts/type_surface_review.py` rejects
common high-risk widenings such as precise type -> `object`, precise Sage type
-> `Element`/`Parent`/`SageObject`, `VectorSpace -> FreeModule_generic`, and
parameterized container -> unparameterized container. Do not bypass this gate to
finish a local stub task. If the previous type is source-proven wrong, replace
it with the most precise source-backed type and document that proof; do not
route through a broad placeholder first.

Class-base changes between Sage/domain types are high-risk by default. The
failure mode is local-minimum reward hacking: making one file pass mypy or an
import check by replacing a precise source hierarchy with a broader nearby base,
thereby degrading downstream mathematical meaning. If such a weakening is truly
forced, set a one-time `SAGE_STUBS_TYPE_SURFACE_REVIEW_OTP` value for the commit
attempt and include the same token in the commit message. The commit message
must contain `Type-surface relaxation review:`, `Source evidence:`, `Why
forced:`, `Global regression risk:`, and `Reward-hacking/local-minimum check:`.
The `commit-msg` hook rejects the commit unless that audit trail is present.
If a later `type_surface_review` run finds no staged `.pyi` files, it clears any
stale pending OTP marker before returning so unrelated non-stub commits are not
forced to carry an old type-surface bypass audit.
The marker path is resolved through Git, not by assuming `.git` is a directory,
so the bypass audit flow also works inside linked worktrees.
The `commit-msg` hook clears stale pending markers and skips OTP enforcement
when the current staged set has no `.pyi` files.

## Type annotation quality contract (non-negotiable)

`Any` is banned. Not "banned unless justified." Banned. The
`scripts/check_stubs.py` AST checker rejects:

- `Any` as a return type.
- `Any` as a named parameter type (except in the listed protocol
  dunders).
- `object` as a return type (except `__new__`).

When a type is complex, use `Union[A, B]`, `TypeVar`, `Protocol`,
`@overload`, or add the missing source-backed Sage stub. There is
always a more precise type than `Any`.

`object` is not an acceptable opacity marker for stub authoring in this
repo. Do not add it to parameter, return, alias, or generic positions
to get around the `Any` ban. If the concrete type is unknown, stop and
resolve it from Sage source, runtime evidence, docs, or a supporting
sidecar before editing the stub.

`TypeVar` and local `Protocol` definitions are not acceptable replacement
opacity markers. They are valid only when they state a real relationship between
type positions or a real structural contract used by the Sage source. They are
invalid when they merely say "some type" or "something with this method" for a
constructor input, mutation input, variadic argument, callback, or container
whose contents Sage coerces or normalizes. Replacing an existing type surface
with a new local abstraction is a review failure by default; isolate the change
and cite the exact Sage source if the abstraction is truly forced.

**Named parameters must be resolved to domain types:**

- `precision` — is a number. Use `int` or the appropriate Sage numeric type.
- `degree` — is an integer. Use `int`.
- `prec` — is an integer. Use `int`.
- `n`, `p`, `k`, `m` — are integers unless the source says otherwise. Use `int`.
- `ring`, `base_ring` — use the actual base class (`Ring`, `CommutativeRing`, etc.).
- `other` on arithmetic methods — use `Self` or the operand type, not `Any`.
- `variable` — if the docstring says "a variable or integer", write `int | Variable`, not `Any`.
- `names` — if used for polynomial variable names, write `str | tuple[str, ...]`, not `Any`.

Do not churn equivalent Sage-normalized element annotations. If the source
immediately normalizes an element input through `Integer(...)`, `int(...)`, or
an equivalent Sage preprocessor/coercion path, and the existing local contract
already uses one of `int` or `Integer`, keep that choice consistently across the
related stub surface. Do not spend review or implementation effort flipping
`int` ↔ `Integer` merely because Sage accepts both at runtime; either is
acceptable when the source normalizes the value. This rule does not apply to
parents such as `ZZ`: `ZZ` is not interchangeable with `int` or `Integer`.
The type-surface review gate should not treat a bare `int`/`Integer` spelling
swap as a weakening by itself; surrounding domain types still require review.

**Return types must be resolved:**

- If the source returns `P.element_class(P, ...)` where `P =
  self.parent()`, the return type is `Self` or the class itself.
- If the source returns `self`, the return type is `Self`.
- If the return type depends on the input type, use `@overload` to
  express the distinct signatures.

**Type precision must move forward:**

- Never weaken an existing or source-backed type to satisfy a local
  checker error, lint warning, import problem, or cleanup goal. Fix the
  missing sidecar, import path, package registration, or supporting stub
  instead.
- Never use a broader superclass, implementation base, or placeholder as a
  local substitute for the semantic Sage type. Examples of rejected backward
  moves include `FieldElement -> Element`, `VectorSpace ->
  FreeModule_generic`, subclass -> superclass, parameterized container ->
  unparameterized container, concrete class -> `Parent`, concrete class ->
  `SageObject`, and any precise type -> `object`.
- Coercion is not arbitrary opacity. If the source coerces an argument,
  write the intended domain type or a concrete union of observed
  accepted domains; do not write `object` merely because the runtime
  may reject bad values later.
- Never replace a precise base class or protocol with a broader one.
  Changes such as `FieldElement -> Element`, `CommutativeRingElement ->
  RingElement`, or `Parent -> object` are backwards progress unless
  source review proves the original type was wrong.
- Never flatten source-backed inheritance. Stub class bases carry API
  information and must preserve the Sage hierarchy unless the direct
  source body documents a different relationship.
- If verification fails after adding a precise type, the failure is a
  dependency-resolution problem to fix. It is not permission to degrade
  the type surface.
- Auto-fixes are forward progress until proven otherwise. Do not revert an
  auto-fix merely because it exposes more required cleanup. Review the diff,
  keep the corrected parts, and either fix the follow-on errors or checkpoint
  the forward progress with the remaining blocker clearly identified.

**Forced review triggers:**

- Running or accepting output from an auto-fixer, formatter, codemod, or
  subagent that touched `.pyi` files.
- Editing imports whose only purpose is to make annotations available.
- Replacing one Sage class, parent, element type, category, protocol, alias,
  or container parameter with another.
- Changing a return type, parameter type, class base, overload, `TypeVar`
  bound, or type alias.
- Resolving a checker failure by changing the annotation rather than adding a
  missing source-backed sidecar.
- Seeing or proposing a broader annotation such as `FieldElement -> Element`,
  `VectorSpace -> FreeModule_generic`, subclass -> superclass, semantic parent
  -> implementation parent, parameterized container -> unparameterized
  container, or precise type -> `object`.

**Forced review procedure:**

- If a spark subagent is available, delegate a bounded type-surface audit before
  accepting the diff. The audit must classify changed annotations, bases,
  aliases, and annotation imports as stricter, equivalent, or weaker against
  Sage 10.7 source.
- If no subagent can be started, do a separate self-audit pass after edits and
  before staging. This pass must not be merged into ordinary lint or mypy
  cleanup; it must explicitly search for broader types, lost generic
  parameters, deleted precise imports, and support-stub shortcuts.
- Any weaker change blocks the commit. Fix the missing sidecar, import,
  hierarchy stub, package registration, or alias so the precise type survives.
  Do not trade semantic precision for a local green check.
- Run `just type-surface-review` before staging any changed `.pyi` file and
  after accepting any auto-fix, formatter, codemod, or subagent output. Treat
  every reported annotation, base-class, type-alias, protocol, overload,
  `TypeVar`, and annotation import change as a required review item. The
  command is an inventory, not approval: each item still needs source-backed
  classification as stricter, equivalent, or weaker.
- Treat a `type_surface_review` high-risk broadening failure as a blocked
  commit until the broadening is removed. The `--allow-high-risk` flag is only
  for local investigation after a written/source-cited review; it is not
  permitted in hooks and is not permission to commit weaker stubs.
- Use the review inventory to force a second pass over the diff. For every
  reported item, cite the Sage 10.7 source line that justifies the proposed
  type. If there is no citation, the type is not ready to stage.
- Do not stage a file while its review inventory contains a suspicious broader
  type, a lost generic parameter, a deleted precise import, or a helper sidecar
  introduced only to make a weakened annotation type-check.

When a forced review is triggered, do not stage the file until the review
result is known. Hook passage is not enough; the review must explicitly look
for backwards movement in semantic type precision.

**The following rationalisations are not acceptable and will be
rejected:**

- *"The library allows coercion from other types."* — Coercion is
  runtime behaviour. Annotate the intended type.
- *"I don't have that type imported."* — Add the import or the minimal
  source-backed support stub. Missing imports are not a license for `Any`,
  `object`, or a quoted annotation.
- *"The parameter is polymorphic."* — If you can describe the types in
  words, write them as a `Union`. If you wrote a plain-English
  description and then typed `Any`, that is dishonesty, not uncertainty.
- *"The return type depends on runtime input."* — Use `@overload`.
- *"I described the type correctly but wrote `Any` anyway."* — Not
  acceptable under any circumstance.

**Only stub public methods defined directly on the class.** Nested
helper functions (e.g. `def coefficient(n)` defined inside `__call__`)
are not class methods. Inherited aliases are not direct definitions.
Check `cls.body` in the AST, not the full `ast.walk` output.

## Banned output patterns

These patterns are rejected by `scripts/check_guardrails.py` and
`scripts/check_stubs.py`, both of which run automatically in the
pre-commit hook.

- **No `TYPE_CHECKING` blocks or quoted annotations in stubs.** A `.pyi`
  file is already an annotation surface. Import annotation types directly
  at top level. If that import exposes a missing dependency or cycle, add
  the minimal source-grounded support stub or stop and report the blocked
  evidence. Quoted/string type references are banned; they hide
  type-surface changes from review. String values inside `Literal[...]`
  remain allowed.
- **No relaxed or opaque variadics.** Variadic parameters are
  type-surface positions. If `*args` or `**kwds` is the precise
  source-backed surface, keep it annotated with the tightest known type;
  do not relax that annotation to `Any`, `object`, or a broader domain
  type. If the source paths can be exhausted more explicitly, replace
  the variadic spelling with overloads, finite unions, or a source-audited
  argument container type such as a `TypedDict` or protocol that
  enumerates the possible keyword/argument variables. If the cases cannot
  be exhausted, leave the stub unchanged and report the blocked evidence.
- **No `object` outside known forced slots.** `object` is banned in
  annotations except for the finite source-forced slots centralized in
  `scripts/stub_annotation_policy.py`: currently `__new__` returns,
  `__contains__.x`, `__eq__.other`, `__ne__.other`, and the module-level
  Sage persistence helpers `dumps.obj` / `save.obj`, which mirror
  `sage.misc.persist` accepting arbitrary pickleable payloads. Path-specific
  exceptions must stay path-specific in `scripts/stub_annotation_policy.py`; do
  not allow every function with the same name. Add to that list only with
  source-backed justification.
- **No local suppressions.** `# type: ignore`, `# noqa`, `cast(...)`,
  and similar lint or type-checking suppressions are banned in stub
  files. Fix the signature, import, or supporting stub instead.
- **No lint or type-check relaxation.** Stub tasks must not edit
  `pyproject.toml` to weaken Ruff, mypy, hook, or validation settings.
  The only permitted `pyproject.toml` change for ordinary stub work is
  adding a real package path under `[tool.setuptools] packages`. The
  hook checks the protected sections (`[tool.ruff`, `[tool.mypy`,
  `[build-system`) against `HEAD` and rejects any edit.
- **No scratch artefacts in the repo.** Do not commit helper scripts,
  extraction scripts, inventories, plans, temporary tests, or generated
  notes such as `plan.md` (at repo root), `test_*.py`, `generate_*.py`,
  `fix_*.py`, or one-off method-list files. Put throwaway work in
  `/tmp`. The hook rejects these by filename pattern.
- **No nested `sage-stubs/sage/...` layout.**
  `sage-src/src/sage/structure/foo.py` maps to
  `sage-stubs/structure/foo.pyi`, not
  `sage-stubs/sage/structure/foo.pyi`.
- **No destructive narrowing.** Existing stubs are part of the sidecar
  surface. Do not replace an existing file with a smaller partial stub,
  delete existing public definitions, or narrow existing signatures
  unless source review proves the existing stub is wrong. The hook
  warns on top-level definitions removed vs `HEAD`; override with
  `--allow-narrow` only after explicit source citation in the commit
  message.
- **No type weakening.** Do not make signatures, return types, class
  bases, protocols, aliases, or imports less precise for local
  convenience. If a precise type exposes a missing dependency or mypy
  import failure, add the missing source-grounded sidecar instead of
  broadening the type.
- **No `object` escape hatch.** Do not replace `Any` or an unresolved
  annotation with `object` to satisfy `check_stubs.py`. Resolve the
  domain type, add the missing sidecar, or write a concrete union from
  source evidence. If no source-backed type can be resolved, leave the
  stub unchanged and report the blocked type evidence.
- **No private aliases for basic containers.** Do not hide ordinary
  builtin container types behind aliases such as `_IntList` or
  `_ElementList` merely to route around a local type-checker problem.
  If a class method shadows a builtin name such as `list`, qualify the
  builtin exactly at that collision site, e.g. `builtins.list[int]`, and
  nowhere else.
- **No inherited-method inflation.** If a requested method is inherited
  rather than defined directly on the target class, report that fact.
  Do not add inherited methods as direct methods.
- **No prompt-driven invention.** A method name appearing in a prompt
  is not evidence that the method belongs in the stub. Every method and
  signature must be justified by the direct Sage source body or by a
  documented alias in the source.
- **No verbose builtins.** Use `type`, `list[T]`, and `dict[K, V]`,
  not `builtins.type`, `typing.List`, or `typing.Dict`. The only
  exception is a same-class name collision such as a `list` method,
  where `builtins.list[T]` is permitted at the affected annotation
  site to preserve the real type without aliasing.

## Class hierarchy

Preserve the class hierarchy exactly as in the source. Do not flatten
inheritance.

## Package registration

When adding a stub for a new module path, add the corresponding package
to `pyproject.toml` under `[tool.setuptools] packages` if not already
present. This is the **only** permitted edit to `pyproject.toml` for
stub tasks.

## Measuring progress

Coverage is reported by `scripts/stub_coverage.py` and printed at the
end of every successful pre-commit run. To query it yourself:

```bash
just coverage                                      # summary table
just coverage -- --subpackage rings --missing      # list missing rings/ files
just coverage -- --threshold 0.95                  # CI gate
```

Baseline at plan kickoff: ~12.7 % (349 / 2745 in-scope modules).

## Verification

The pre-commit hook runs all of the following on staged files. They can
also be invoked manually:

```bash
just check       # ruff + check_stubs + check_guardrails + mypy --strict
just lint        # ruff + check_stubs only (no mypy)
just guardrails  # check_guardrails on staged set
just coverage    # current parity report
```

If you ever bypass the hook (`--no-verify`), the next contributor's
hook will catch the violation on their next commit and your file will
block their work. Don't.

## Legacy backlog

A subset of existing `.pyi` files in `sage-stubs/` predate this
contract and contain `TYPE_CHECKING`, `# noqa`, or `Any` patterns. They
were captured in the initial 402-stub baseline. `just check` will print
these under the `check_guardrails --all` section but will not block.
The hook only fails on *new or staged* violations, so the backlog is
cleaned up progressively as agents touch each file.
