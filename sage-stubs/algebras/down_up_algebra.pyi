from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, Literal, Protocol, Self, TypeVar, overload

from sage.categories.rings import Rings
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

type DownUpExponent = int | Integer
type DownUpExponentVector = tuple[
    DownUpExponent,
    DownUpExponent,
    DownUpExponent,
]
type DownUpGeneratorName = Literal["d", "u"]
type DownUpCoefficientInput[_Coefficient: RingElement] = (
    _Coefficient | RingElement | Integer | int
)

class DownUpBasisIndex(Protocol):
    value: DownUpExponentVector
    def __iter__(self) -> Iterator[DownUpExponent]: ...
    def __getitem__(self, i: int) -> DownUpExponent: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)

class _WeightSequence(Protocol[_Coefficient]):
    @overload
    def __getitem__(self, i: int | Integer) -> _Coefficient: ...
    @overload
    def __getitem__(self, i: slice) -> _WeightSequence[_Coefficient]: ...
    def __iter__(self) -> Iterator[_Coefficient]: ...

class _DownUpGeneratorFamily(Protocol[_Coefficient]):
    def __getitem__(
        self,
        name: DownUpGeneratorName,
    ) -> _DownUpElement[_Coefficient]: ...
    def __iter__(self) -> Iterator[_DownUpElement[_Coefficient]]: ...
    def keys(self) -> tuple[DownUpGeneratorName, ...]: ...
    def values(self) -> Iterable[_DownUpElement[_Coefficient]]: ...

class _DownUpElement(Protocol[_Coefficient]):
    def parent(self) -> DownUpAlgebra[_Coefficient]: ...
    def monomial_coefficients(
        self,
        copy: bool = True,
    ) -> dict[DownUpBasisIndex, _Coefficient]: ...
    def degree(self) -> int: ...
    def __add__(self, other: Self) -> Self: ...
    def __sub__(self, other: Self) -> Self: ...
    def __neg__(self) -> Self: ...
    @overload
    def __mul__(self, other: Self) -> Self: ...
    @overload
    def __mul__(
        self,
        other: VermaModule.Element[_Coefficient],
    ) -> VermaModule.Element[_Coefficient]: ...
    @overload
    def __mul__(
        self,
        other: DownUpCoefficientInput[_Coefficient],
    ) -> Self: ...
    def __rmul__(
        self,
        other: DownUpCoefficientInput[_Coefficient],
    ) -> Self: ...
    def __pow__(self, exponent: int | Integer) -> Self: ...

class _VermaBasis(Protocol[_Coefficient]):
    def __getitem__(
        self,
        n: int | Integer,
    ) -> VermaModule.Element[_Coefficient]: ...
    def __iter__(self) -> Iterator[VermaModule.Element[_Coefficient]]: ...
    def keys(self) -> Iterable[Integer]: ...

class DownUpAlgebra(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    @staticmethod
    @overload
    def __classcall_private__(
        cls: type[DownUpAlgebra[_Coefficient]],
        alpha: _Coefficient,
        beta: _Coefficient,
        gamma: _Coefficient,
        base_ring: None = None,
    ) -> DownUpAlgebra[_Coefficient]: ...
    @staticmethod
    @overload
    def __classcall_private__(
        cls: type[DownUpAlgebra[_Coefficient]],
        alpha: DownUpCoefficientInput[_Coefficient],
        beta: DownUpCoefficientInput[_Coefficient],
        gamma: DownUpCoefficientInput[_Coefficient],
        base_ring: Rings.ParentMethods[_Coefficient],
    ) -> DownUpAlgebra[_Coefficient]: ...
    def __init__(
        self,
        alpha: _Coefficient,
        beta: _Coefficient,
        gamma: _Coefficient,
        base_ring: Rings.ParentMethods[_Coefficient],
    ) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_Coefficient]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _repr_term(self, m: DownUpBasisIndex) -> str: ...
    def _latex_term(self, m: DownUpBasisIndex) -> str: ...
    def algebra_generators(
        self,
    ) -> _DownUpGeneratorFamily[_Coefficient]: ...
    def gens(
        self,
    ) -> tuple[_DownUpElement[_Coefficient], _DownUpElement[_Coefficient]]: ...
    def one_basis(self) -> DownUpBasisIndex: ...
    def monomial(
        self,
        index: DownUpBasisIndex,
    ) -> _DownUpElement[_Coefficient]: ...
    def one(self) -> _DownUpElement[_Coefficient]: ...
    def zero(self) -> _DownUpElement[_Coefficient]: ...
    def product_on_basis(
        self,
        m1: DownUpBasisIndex,
        m2: DownUpBasisIndex,
    ) -> _DownUpElement[_Coefficient]: ...
    def degree_on_basis(self, m: DownUpBasisIndex) -> int: ...
    def verma_module(
        self,
        la: DownUpCoefficientInput[_Coefficient],
    ) -> VermaModule[_Coefficient]: ...

class VermaModule(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    @staticmethod
    def __classcall_private__(
        cls: type[VermaModule[_Coefficient]],
        DU: DownUpAlgebra[_Coefficient],
        la: DownUpCoefficientInput[_Coefficient],
    ) -> VermaModule[_Coefficient]: ...
    def __init__(
        self,
        DU: DownUpAlgebra[_Coefficient],
        la: _Coefficient,
    ) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_Coefficient]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def basis(self) -> _VermaBasis[_Coefficient]: ...
    def highest_weight_vector(self) -> VermaModule.Element[_Coefficient]: ...
    def weights(self) -> _WeightSequence[_Coefficient]: ...
    def _action_on_basis(
        self,
        m: DownUpBasisIndex,
        n: int | Integer,
    ) -> VermaModule.Element[_Coefficient]: ...
    def term(
        self,
        n: int | Integer,
        coefficient: _Coefficient,
    ) -> VermaModule.Element[_Coefficient]: ...
    def zero(self) -> VermaModule.Element[_Coefficient]: ...

    class Element(
        CombinatorialFreeModule.Element,
        Generic[_Coefficient],
    ):
        def parent(self) -> VermaModule[_Coefficient]: ...
        def monomial_coefficients(
            self,
            copy: bool = True,
        ) -> dict[int | Integer, _Coefficient]: ...
        def _acted_upon_(
            self,
            scalar: DownUpCoefficientInput[_Coefficient]
            | _DownUpElement[_Coefficient],
            self_on_left: bool,
        ) -> Self | None: ...
        def is_weight_vector(self) -> bool: ...
        def weight(self) -> FreeModuleElement[_Coefficient]: ...
