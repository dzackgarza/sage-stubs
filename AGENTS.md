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

**Stop-the-line weakening review.** If a diff changes a precise Sage type to a
broader type, do not continue implementation, staging, or commit preparation
until the weakening has been removed or independently reviewed. This applies
even when the broader type makes mypy, Ruff, imports, or local package
registration easier. The required review must be performed by a separate
subagent when one is available; otherwise perform a separate written audit pass
that names each suspicious change and cites the Sage 10.7 source. Hook passage
is not evidence that weakening is acceptable.

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

When a forced review is triggered, do not stage the file until the review
result is known. Hook passage is not enough; the review must explicitly look
for backwards movement in semantic type precision.

**The following rationalisations are not acceptable and will be
rejected:**

- *"The library allows coercion from other types."* — Coercion is
  runtime behaviour. Annotate the intended type.
- *"I don't have that type imported."* — Add the import or use a
  string forward reference. Missing imports are not a license for `Any`.
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

These patterns are rejected by `scripts/check_guardrails.py`, which
runs automatically in the pre-commit hook.

- **No `TYPE_CHECKING` blocks in stubs.** A `.pyi` file is already an
  annotation surface. Import annotation types directly at top level. If
  that import exposes a missing dependency, add the minimal
  source-grounded stub for the dependency or use a quoted forward
  reference only for genuinely recursive definitions.
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
- **No inherited-method inflation.** If a requested method is inherited
  rather than defined directly on the target class, report that fact.
  Do not add inherited methods as direct methods.
- **No prompt-driven invention.** A method name appearing in a prompt
  is not evidence that the method belongs in the stub. Every method and
  signature must be justified by the direct Sage source body or by a
  documented alias in the source.
- **No verbose builtins.** Use `type`, `list[T]`, and `dict[K, V]`,
  not `builtins.type`, `typing.List`, or `typing.Dict`.

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
