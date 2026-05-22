---
title: Preserve type surface and forward progress
status: active
tags: [stubs, corrections, workflow]
---

When working on stub data, lint fixes, formatter fixes, or verification cleanup,
never remove or degrade existing type information to satisfy a local goal such as
cleanliness, hook passage, smaller diffs, or faster completion.

Rules:
- Do not delete public stub surface unless source review proves the symbol is
  wrong and the removal is explicitly justified.
- Do not replace precise annotations with weaker annotations such as `object`
  merely to make a checker pass.
- Do not use `object` as an opacity marker in stub annotations. Resolve a
  concrete Sage type, protocol, type variable, or finite source-backed union;
  if that cannot be done, stop and report the blocked type evidence instead of
  editing.
- If source coerces an argument, annotate the intended domain type or concrete
  observed union instead of treating coercion as permission for `object`.
- Do not flatten or simplify source-backed inheritance if doing so loses API
  information.
- Do not revert auto-fixes just because they expand the scope of cleanup. Treat
  auto-fixes as forward progress unless inspection shows a concrete regression.
- If an auto-fix creates follow-on errors, fix those errors or checkpoint the
  forward progress; do not roll back to a less-correct state for convenience.

Verification:
- Before reporting completion, inspect `git diff` for removed definitions,
  narrowed signatures, weakened annotations, or reverted auto-fix changes.
- Before staging or accepting any `.pyi` diff from local edits, subagents, or
  auto-fixers, classify every changed annotation/import/base/alias as stricter,
  equivalent, or weaker against Sage 10.7 source. Reject weaker changes before
  they reach commit.
- If any changed type surface appears broader than the current stub or the
  source-backed semantic type, stop implementation and force a separate review.
  Use a spark subagent for that review when available; if none can be started,
  perform a separate written audit pass before staging.
- If any backwards movement is intentional, cite the exact source evidence and
  make it explicit in the commit message or status.


## Forced review banning type weakening

Trigger: Any stub edit changes an annotation, import used for annotations, base
class, alias, return type, parameter type, or inferred semantic category from its
current spelling. This especially includes changes from a named/domain-specific
type to a broader type, superclass, factory implementation base,
unparameterized container, `object`, `SageObject`, `Parent`, `Element`, or other
placeholder.

Guidance: Type weakening is banned. Pause implementation and perform a forced
review before staging or committing any changed type surface. Compare the
existing type and proposed type, cite the Sage 10.7 source lines, identify their
hierarchy relationship, and classify the proposal as strictly narrower, equal,
or broader. Do not commit broader or less domain-specific types. If the existing
annotation is source-proven wrong, replace it with the most precise
source-backed type, not a broader placeholder; record the proof in the commit
message. If mypy rejects a semantic type because a support stub models it
poorly, fix the support stub or choose the nearest precise source-backed
semantic class; never fall back to an implementation superclass or placeholder
just to make the local check pass.

Forced reviewer step: Before accepting local edits, subagent output, or
auto-fixes that touch stubs, run an explicit type-surface review over the diff.
The reviewer must look for lost specificity, not just hook passage. A diff that
contains examples like `FieldElement -> Element`, `VectorSpace ->
FreeModule_generic`, concrete class -> `Parent`/`SageObject`/`object`, subclass
-> superclass, parameterized container -> unparameterized container, or precise
union -> opaque placeholder is rejected unless it is replaced by a more precise
source-backed annotation before commit.

Forced review output: The review must name the changed type surfaces and mark
each as stricter, equivalent, or weaker. "Mypy passes", "ruff passes", "cleaner
import graph", "smaller sidecar", and "unblocks local goal" are not review
results. If a proposed change is weaker, stop the implementation path that
introduced it and repair the dependency, support stub, import, or alias instead
of accepting the weaker type.

Verification:
- Before every commit touching stubs, inspect `git diff --cached` for any
  annotation, import, alias, base class, return type, or parameter type change
  that loses domain specificity.
- Apply the same forced review to subagent output and auto-fix output before
  accepting it.
- Suspicious broadenings such as `FieldElement -> Element`, `VectorSpace ->
  FreeModule_generic`, subclass -> superclass, semantic parent ->
  implementation parent, parameterized container -> unparameterized container,
  or precise type -> `object` require an independent review path before the
  diff can be accepted. A local checker failure is not a reason to accept the
  broader type.
- The commit message must state that the forced type-surface review found no
  weakening, or cite source evidence for a source-proven correction to a more
  precise type.


## Sage-normalized element annotations

Trigger: While authoring or reviewing Sage stubs, the source immediately normalizes an element input through `Integer(...)`, `int(...)`, or an equivalent Sage preprocessor/coercion path, and the remaining question is only whether the stub should spell that element type as Python `int` or Sage `Integer`.

Guidance: Do not spend review or implementation effort churn-testing equivalent `int` vs `Integer` spellings when Sage normalizes the element value before meaningful use. Keep the existing local convention if one is present; otherwise choose one source-plausible spelling and use it consistently within that stub surface. This does not apply to parent objects such as `ZZ`: `ZZ` is not interchangeable with `int` or `Integer`. This is not permission to weaken unrelated domain types, use `object`, use `Any`, or erase distinctions that Sage does not actually normalize.

Verification: The resulting diff should avoid annotation churn whose only effect is flipping `int` and `Integer`, and it should still preserve or improve all existing non-numeric domain specificity.


## Use spark subagents when possible

Trigger: A task is broad, multi-file, exploratory, or has independent cleanup/audit slices that can run in parallel without blocking the coordinator's immediate next action.

Guidance: Prefer spawning spark subagents for bounded sidecar work when it can materially advance the main task: independent source audits, lint cleanup in disjoint files, verification sweeps, or issue-state reconciliation. Keep the coordinator on the critical path, give each subagent a precise write/read scope, and do not delegate tightly coupled or immediately blocking work just to satisfy the rule.

Verification: At planning points, explicitly identify whether there is a parallelizable helper task. If yes, spawn a spark-capable subagent or state the concrete reason delegation is not possible or would block/duplicate the coordinator.
