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

class QuotientModule_free_ambient:
    def __init__(self, module: builtins.object, sub: builtins.object) -> None: ...
    def __hash__(self) -> builtins.int: ...
    def gens(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def gen(self, i: builtins.int = ...) -> FreeModuleElement[_Scalar]: ...
    def ambient_module(self) -> FreeModule_ambient_field_quotient: ...
    def cover(self) -> FreeModule_ambient_field_quotient: ...
    V: _SageObject

    def relations(self) -> FreeModule_ambient_field_quotient: ...
    W: _SageObject

    def free_cover(self) -> FreeModule_ambient_field_quotient: ...
    def free_relations(self) -> FreeModule_ambient_field_quotient: ...

class FreeModule_ambient_field_quotient:
    def __init__(
        self,
        domain: builtins.object,
        sub: builtins.object,
        quotient_matrix: builtins.object,
        lift_matrix: builtins.object,
        inner_product_matrix: builtins.object = ...,
    ) -> None: ...
    def __hash__(self) -> builtins.int: ...
    def quotient_map(self) -> FreeModule_ambient_field_quotient: ...
    def lift_map(self) -> FreeModule_ambient_field_quotient: ...
    def lift(self, x: builtins.object) -> FreeModule_ambient_field_quotient: ...
    def cover(self) -> FreeModule_ambient_field_quotient: ...
    V: _SageObject

    def relations(self) -> FreeModule_ambient_field_quotient: ...
    W: _SageObject
