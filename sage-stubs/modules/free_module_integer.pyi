from collections.abc import Iterator, Sequence
from typing import Self, TypeVar
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_double import RealDoubleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

import builtins

class _SageObject: ...

def IntegerLattice(
    basis: builtins.object, lll_reduce: builtins.bool = ...
) -> ElementConstructorInput: ...

class FreeModule_submodule_with_basis_integer:
    def __init__(
        self,
        ambient: builtins.object,
        basis: builtins.object,
        check: builtins.bool = ...,
        echelonize: builtins.bool = ...,
        echelonized_basis: builtins.object = ...,
        already_echelonized: builtins.bool = ...,
        lll_reduce: builtins.bool = ...,
    ) -> None: ...
    @property
    def reduced_basis(self) -> FreeModule_submodule_with_basis_integer: ...
    def LLL(
        self, *args: builtins.object, **kwds: builtins.object
    ) -> FreeModule_submodule_with_basis_integer: ...
    def BKZ(
        self, *args: builtins.object, **kwds: builtins.object
    ) -> FreeModule_submodule_with_basis_integer: ...
    def HKZ(
        self, *args: builtins.object, **kwds: builtins.object
    ) -> FreeModule_submodule_with_basis_integer: ...
    def volume(self) -> FreeModule_submodule_with_basis_integer: ...
    def discriminant(self) -> FreeModule_submodule_with_basis_integer: ...
    def is_unimodular(self) -> builtins.bool: ...
    def shortest_vector(
        self,
        update_reduced_basis: builtins.bool = ...,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwds: builtins.object,
    ) -> FreeModule_submodule_with_basis_integer: ...
    def update_reduced_basis(
        self, w: builtins.object
    ) -> FreeModule_submodule_with_basis_integer: ...
    def voronoi_cell(
        self, radius: builtins.object = ...
    ) -> FreeModule_submodule_with_basis_integer: ...
    def voronoi_relevant_vectors(self) -> FreeModule_submodule_with_basis_integer: ...
    def closest_vector(
        self, t: builtins.object
    ) -> FreeModule_submodule_with_basis_integer: ...
    def approximate_closest_vector(
        self,
        t: builtins.object,
        delta: builtins.object = ...,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> FreeModule_submodule_with_basis_integer: ...
    def babai(
        self, *args: builtins.object, **kwargs: builtins.object
    ) -> FreeModule_submodule_with_basis_integer: ...
    def hadamard_ratio(
        self, use_reduced_basis: builtins.bool = ...
    ) -> FreeModule_submodule_with_basis_integer: ...
    def gaussian_heuristic(
        self, exact_form: builtins.bool = ...
    ) -> FreeModule_submodule_with_basis_integer: ...
