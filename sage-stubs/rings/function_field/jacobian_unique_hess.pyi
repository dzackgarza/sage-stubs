from collections.abc import Iterator
from typing import Self

from sage.plot.point import point
from sage.rings.function_field.divisor import FunctionFieldDivisor
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.function_field import FunctionField
from sage.rings.function_field.jacobian_base import (
    Jacobian_base,
    JacobianGroup_base,
    JacobianGroup_finite_field_base,
    JacobianPoint_base,
    JacobianPoint_finite_field_base,
)
from sage.schemes.elliptic_curves.ell_modular_symbols import zero
from sage.structure.parent import ElementConstructorInput
from sage.structure.unique_representation import UniqueRepresentation

class JacobianPoint(JacobianPoint_base):
    def __init__(
        self,
        parent: FunctionField,
        finite_ideal: ElementConstructorInput,
        infinite_ideal: ElementConstructorInput,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def additive_order(self) -> Self: ...
    def effective_part(self) -> Self: ...
    def divisor(self) -> FunctionFieldDivisor: ...
    def _richcmp_(self, other: Self, op: ElementConstructorInput) -> bool: ...

class JacobianPoint_finite_field(JacobianPoint, JacobianPoint_finite_field_base): ...

class JacobianGroup(UniqueRepresentation, JacobianGroup_base):
    def __init__(
        self,
        parent: FunctionField,
        function_field: ElementConstructorInput,
        base_div: ElementConstructorInput,
    ) -> None: ...
    def point(self, divisor: FunctionFieldDivisor) -> FunctionFieldElement: ...
    def zero(self) -> FunctionFieldElement: ...
    def _element_constructor_(
        self, x: FunctionFieldElement | ElementConstructorInput
    ) -> zero | point: ...
    def _repr_(self) -> str: ...

class JacobianGroup_finite_field(JacobianGroup, JacobianGroup_finite_field_base):
    def __iter__(self) -> Iterator[FunctionFieldElement]: ...

class Jacobian(Jacobian_base, UniqueRepresentation):
    def __init__(
        self,
        function_field: ElementConstructorInput,
        base_div: ElementConstructorInput,
        cache_infinite_ideals: ElementConstructorInput = ...,
        **kwds: ElementConstructorInput,
    ) -> None: ...
    def group(self, k_ext: ElementConstructorInput = ...) -> FunctionFieldElement: ...
    def _repr_(self) -> str: ...
