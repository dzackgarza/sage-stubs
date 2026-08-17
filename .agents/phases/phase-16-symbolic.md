# Phase 16 — Symbolic, Calculus, Functions

**Tier:** 3
**Status:** ✅ Complete
**Depends on:** Phase 02
**Unblocks:** Phase 17 (parts)

## Position in the plan tree

This is the first-level Phase 16 subtree of the full-parity plan. Its tasks
are the second-level workstreams below; the source-grounded stub commits are
leaves beneath those tasks. A commit touching one symbolic function or one
calculus module is not itself a phase.

## Goal

Provide mathematically meaningful public typing for `sage.symbolic`,
`sage.calculus`, and `sage.functions` at the pinned Sage 10.7 source revision.
The phase preserves the symbolic parent/element relation, symbolic function
application, assumptions, substitutions, differentiation and integration,
ODE and transform data, special-function objects, piecewise functions, and
numeric-versus-symbolic result shapes.

## Exact scope

The phase contains:

- **56 in-scope `.py`/`.pyx` modules:** 21 under `symbolic/`, 15 under
  `calculus/`, and 20 under `functions/`.
- **Six source-owned Cython declaration-fragment support stubs:**
  `comparison_impl`, `constants_c_impl`, `getitem_impl`,
  `pynac_constant_impl`, `pynac_function_impl`, and `series_impl`.
- **Five package initializers:** `symbolic`, `symbolic.integration`,
  `calculus`, `calculus.transforms`, and `functions`.
- **Two explicit exemptions:** `symbolic/benchmark` and `calculus/wester`;
  both are benchmark/regression harnesses rather than supported consumer APIs.

Pure re-export shells (`all.py`), doctest/test harnesses, `.pxd` declarations,
and C-level callback/helper definitions are governed by the global scope rules
and are not Python API omissions.

## Completed tasks

| Task | Workstream | Source-owned surface | Status |
|------|------------|----------------------|--------|
| T16.1 | **Symbolic core** | `assumptions`, `constants`, `expression`, `function`, `function_factory`, `ring`, `symbols` | ✅ Complete |
| T16.2 | **Symbolic callable, relations, and conversion** | `callable`, `expression_conversion_algebraic`, `expression_conversion_sympy`, `expression_conversions`, `operators`, `relation`, `subring`, `symengine`, `units` | ✅ Complete |
| T16.3 | **Symbolic integration, backend boundaries, and Cython fragments** | `complexity_measures`, `integration.external`, `integration.integral`, `maxima_wrapper`, `random_tests`, and the six declaration-fragment support stubs | ✅ Complete |
| T16.4 | **Calculus front end** | `calculus`, `expr`, `functional`, `functions`, `predefined`, `var` | ✅ Complete |
| T16.5 | **Numerical calculus, ODEs, interpolation, and transforms** | `desolvers`, `integration`, `interpolation`, `interpolators`, `ode`, `riemann`, `transforms.dft`, `transforms.dwt`, `transforms.fft` | ✅ Complete |
| T16.6 | **Airy, Bessel, gamma, exponential-integral, and hypergeometric families** | `airy`, `bessel`, `error`, `exp_integral`, `gamma`, `generalized`, `hyperbolic`, `hypergeometric` | ✅ Complete |
| T16.7 | **Elementary, orthogonal, piecewise, and remaining special functions** | `jacobi`, `log`, `min_max`, `orthogonal_polys`, `other`, `piecewise`, `prime_pi`, `special`, `spike_function`, `transcendental`, `trig`, `wigner` | ✅ Complete |
| T16.8 | **Phase-wide public globals, parity, and package closure** | symbolic constants and registries, derivative operator `D`, integration registry, package initializers, exemptions, and full source-surface reconciliation | ✅ Complete |

## Mathematical typing supplied

The phase-wide interfaces now expose, among other relationships:

- `SymbolicRing` as a parent whose elements are `Expression` objects.
- Arithmetic, substitutions, equations, differentiation, integration,
  limits, series, roots, polynomial conversions, and numerical approximation
  on `Expression` with their actual structured return shapes.
- `Function`, `BuiltinFunction`, `GinacFunction`, and `SymbolicFunction`,
  including symbolic/numeric argument and result domains.
- Named symbolic constants and the public registries
  `constants_table`/`constants_name_table`, together with `I` as a symbolic
  expression.
- The derivative-operator object `D` and typed higher derivative operators.
- Definite/indefinite integration and the public algorithm-to-integrator
  registry.
- Numerical integration result tuples, ODE solution data, interpolation
  functions, discrete/Fourier/wavelet transforms, and plotting returns.
- Special-function singleton objects rather than untyped callables.
- Piecewise domains, pieces, restrictions, extensions, transforms, and
  Fourier coefficients.

No public signature in this phase uses `Any`, a fabricated `_SageObject`, a
generated-scaffold marker, or `builtins.object` spelling.

## Source-surface reconciliation

The Python-source audit compares every top-level public function/class and
every directly defined class method with its corresponding stub. Apparent
leftovers were reviewed individually:

- parser lookup tables and Maxima helper aliases in `calculus.calculus` are
  implementation state, not documented public API;
- the historical `Function_sqrt` compatibility class is generated only to
  unpickle old objects, while the supported public object is `sqrt`;
- Cython functions such as GSL callbacks, `new_Expression_from_GEx`, and
  internal FFT wrapper classes are C-level implementation helpers;
- `Function.return_sympy` and analogous `cdef` methods are not Python-callable
  methods.

The support stubs corresponding to `.pxi` fragments are retained because they
supply annotation-owned types used by the public symbolic surface; they are
not orphaned generated modules.

## Completion gates

The completed subtree satisfies:

1. `stub_coverage.py` reports zero missing modules for `symbolic`, `calculus`,
   and `functions` after the two documented exemptions.
2. `scripts/check_stubs.py` accepts all 67 Phase 16 `.pyi` files.
3. Every Phase 16 stub parses under the project Python grammar, and annotation
   name resolution finds no undefined imported or declared type names.
4. The source/stub public-surface audit finds no unaccounted Python API
   definitions; all Cython-only differences are documented above.
5. The phase contains no unused imports after the source-grounded cleanup.
6. The semantic audit leaves only intentional protocol boundaries: comparison
   operands typed as `object`, arbitrary `__setattr__`/legacy pickle state,
   and the variable-only `calculus.predefined` module. These are retained
   because narrowing them would be false, not because a zero count was missed.

Repository-wide analyzers may still report debt in other first-level phases;
that does not change the completed state of this isolated Phase 16 subtree.
No analyzer rule or quality threshold was relaxed for this completion.
