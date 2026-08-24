from collections.abc import Iterable
from typing import Generic, Self, TypeVar

from sage.algebras.clifford_algebra import ExteriorAlgebraIdeal
from sage.data_structures.bitset import FrozenBitset
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.structure.element import RingElement

_Scalar = TypeVar(
    "_Scalar",
    bound=RingElement,
    default=RingElement,
)

class CliffordAlgebraElement(
    IndexedFreeModuleElement[FrozenBitset, _Scalar],
    Generic[_Scalar],
):
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def list(self) -> list[tuple[FrozenBitset, _Scalar]]: ...
    def support(self) -> list[FrozenBitset]: ...
    def reflection(self) -> Self: ...
    def degree_negation(self) -> Self: ...
    def transpose(self) -> Self: ...
    def conjugate(self) -> Self: ...
    def clifford_conjugate(self) -> Self: ...

class ExteriorAlgebraElement(
    CliffordAlgebraElement[_Scalar],
    Generic[_Scalar],
):
    def reduce(
        self,
        I: ExteriorAlgebraIdeal[_Scalar] | Iterable[ExteriorAlgebraElement[_Scalar]],
        left: bool = ...,
    ) -> Self: ...
    def interior_product(
        self,
        x: ExteriorAlgebraElement[_Scalar],
    ) -> Self: ...
    def antiderivation(
        self,
        x: ExteriorAlgebraElement[_Scalar],
    ) -> Self: ...
    def hodge_dual(self) -> Self: ...
    def constant_coefficient(self) -> _Scalar: ...
    def scalar(
        self,
        other: ExteriorAlgebraElement[_Scalar],
    ) -> _Scalar: ...

class CohomologyRAAGElement(
    CliffordAlgebraElement[_Scalar],
    Generic[_Scalar],
): ...
