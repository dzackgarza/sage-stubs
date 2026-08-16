# Source-grounded mathematical typing phases

The purpose of this work is to make the Sage public API express its mathematical structure. Lint and type-checker counts are diagnostics, not the specification. A phase is complete only when its signatures are justified by the pinned Sage source and are useful to a reader or consumer for understanding domains, codomains, element types, parent types, variance, coercions, and constructions.

Each phase is committed separately. A phase may leave analyzer findings when eliminating them would require a false or less informative type.

## Phase 1 — Categorical kernel

Reconstruct `SageObject`, `CategoryObject`, `Category`, `Parent`, `Element`, `Map`, `Morphism`, `Homset`, and coercion interfaces as one compatible generic graph. In particular, distinguish objects of a category from their elements, make homset domain and codomain parents explicit, and preserve the element type constructed by each parent.

## Phase 2 — Algebraic domains and morphisms

Type rings, semirings, fields, ideals, quotients, algebras, modules, and their homsets. Preserve base-ring and coefficient-element parameters, scalar extension/restriction, quotient maps, embeddings, and coercion results.

## Phase 3 — Linear and multilinear algebra

Type free modules, vectors, matrices, tensors, bilinear and quadratic forms, kernels, images, duals, and change-of-base-ring operations. Encode dimensions and shapes where Python's type system can do so without pretending that runtime integers are static literals.

## Phase 4 — Polynomial, series, and arithmetic towers

Type polynomial and power-series parents/elements, fraction fields, finite fields, p-adics, number fields, orders, places, valuations, and ideals. Preserve coefficient rings, residue fields, completions, embeddings, and exact-versus-approximate result types.

## Phase 5 — Groups, actions, and representations

Type abstract and concrete groups, elements, homomorphisms, actions, permutation and matrix groups, characters, representations, and invariant/coinvariant constructions.

## Phase 6 — Combinatorics and root-theoretic structures

Type enumerated sets, finite families, permutations, tableaux, partitions, posets, root systems, Weyl groups, crystals, and combinatorial free modules using their actual index and element types rather than a universal `Element` substitute.

## Phase 7 — Geometry, topology, and schemes

Type schemes, points, morphisms, varieties, divisors, sheaves, complexes, graphs, manifolds, and polyhedral objects. Keep base schemes/fields, coordinate rings, point residue data, and functorial constructions visible.

## Phase 8 — Symbolic, numerical, and external interfaces

Type symbolic expressions, numerical fields, solvers, plotting objects, probability/statistics, and library interfaces. Explicitly distinguish exact mathematical values from machine or interval approximations.

## Phase 9 — Native/Cython surface and residual review

Reconstruct Cython declarations from `.pxd`/`.pyx` evidence, then review every residual `object`, `Any`, placeholder, empty surface, and suppression. Retain `object` only where the public contract genuinely accepts an arbitrary Python object, such as equality or membership protocols.

## Per-phase acceptance standard

For every changed public signature:

1. The class/function and inheritance must agree with the pinned Sage source.
2. Parameters must name their mathematical domains, not merely a common superclass chosen to silence an analyzer.
3. Results must expose the strongest stable mathematical relationship supported by the source: `Self`, a parent/element parameter, a concrete construction, an overload, a protocol, or a justified union.
4. Container and iterator parameters must preserve their element/index/coefficient types.
5. Consumer examples must demonstrate the intended inference where the relationship is not evident from the declaration alone.
6. Analyzer findings are fixed only by improving the contract; suppressions and diagnostic-driven type widening do not complete a phase.
