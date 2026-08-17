from collections.abc import Iterator
from typing import Self

from sage.categories.map import Map
from sage.matrix.matrix0 import Matrix
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
from sage.rings.integer import Integer
from sage.schemes.elliptic_curves.ell_modular_symbols import zero
from sage.structure.parent import ElementConstructorInput
from sage.structure.richcmp import richcmp
from sage.structure.unique_representation import UniqueRepresentation

class JacobianPoint(JacobianPoint_base):
    def __init__(self, parent: FunctionField, w: ElementConstructorInput) -> None: ...
    def multiple(self, n: int | Integer) -> Self: ...
    def addflip(
        self, other: FunctionFieldElement | ElementConstructorInput
    ) -> Self: ...
    def defining_matrix(self) -> Matrix: ...
    def divisor(self) -> FunctionFieldDivisor: ...
    def _repr_(self) -> str: ...
    def _richcmp_(
        self,
        other: FunctionFieldElement | ElementConstructorInput,
        op: ElementConstructorInput,
    ) -> bool | richcmp: ...

class JacobianPoint_finite_field(JacobianPoint, JacobianPoint_finite_field_base): ...

class JacobianGroupEmbedding(Map):
    def __init__(
        self,
        base_group: ElementConstructorInput,
        extension_group: ElementConstructorInput,
    ) -> None: ...
    def _call_(
        self, x: FunctionFieldElement | ElementConstructorInput
    ) -> FunctionFieldElement: ...

class JacobianGroup(UniqueRepresentation, JacobianGroup_base):
    def __init__(
        self,
        parent: FunctionField,
        function_field: ElementConstructorInput,
        base_div: ElementConstructorInput,
    ) -> None: ...
    def point(self, divisor: FunctionFieldDivisor) -> FunctionFieldElement: ...
    def zero(self) -> FunctionFieldElement: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self, x: FunctionFieldElement | ElementConstructorInput
    ) -> zero | point | FunctionFieldElement: ...

class JacobianGroup_finite_field(JacobianGroup, JacobianGroup_finite_field_base):
    def __init__(
        self,
        parent: FunctionField,
        function_field: ElementConstructorInput,
        base_div: ElementConstructorInput,
    ) -> None: ...
    def __iter__(self) -> Iterator[FunctionFieldElement]: ...

class Jacobian(UniqueRepresentation, Jacobian_base):
    def __init__(
        self,
        function_field: ElementConstructorInput,
        base_div: ElementConstructorInput,
        model: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> None: ...
    def _repr_(self) -> str: ...
