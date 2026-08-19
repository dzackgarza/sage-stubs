
from collections.abc import Iterable, Iterator, Sequence
from typing import Generic, Protocol, Self, TypeVar, overload

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.combinat.root_system.coxeter_type import (
    CoxeterIndex,
    CoxeterType,
    CoxeterTypeData,
)
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

type HeckeParameter = RingElement | Integer | int
type CoxeterWord = Sequence[CoxeterIndex]

class _CoxeterGroupElement(Protocol):
    def reduced_word(self) -> list[CoxeterIndex]: ...
    def length(self) -> int: ...
    def bruhat_le(self, other: Self) -> bool: ...
    def has_descent(
        self,
        i: CoxeterIndex,
        side: str = "right",
        positive: bool = False,
    ) -> bool: ...
    def descents(
        self,
        side: str = "right",
        index_set: Iterable[CoxeterIndex] | None = None,
        positive: bool = False,
    ) -> list[CoxeterIndex]: ...
    def first_descent(
        self,
        side: str = "right",
        index_set: Iterable[CoxeterIndex] | None = None,
        positive: bool = False,
    ) -> CoxeterIndex | None: ...
    def apply_simple_reflection(
        self,
        i: CoxeterIndex,
        side: str = "right",
    ) -> Self: ...
    def __mul__(self, other: Self) -> Self: ...
    def __hash__(self) -> int: ...

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_NewCoefficient = TypeVar("_NewCoefficient", bound=RingElement)
_WElement = TypeVar(
    "_WElement",
    bound=_CoxeterGroupElement,
    default=_CoxeterGroupElement,
)

class _CoefficientRing(Protocol[_Coefficient]):
    def __call__(self, value: HeckeParameter) -> _Coefficient: ...
    def one(self) -> _Coefficient: ...
    def is_commutative(self) -> bool: ...
    def variable_names(self) -> tuple[str, ...]: ...

class _CoxeterElementFamily(Protocol[_WElement]):
    def __getitem__(self, i: CoxeterIndex) -> _WElement: ...
    def __iter__(self) -> Iterator[_WElement]: ...
    def keys(self) -> Iterable[CoxeterIndex]: ...
    def values(self) -> Iterable[_WElement]: ...

class _CoxeterGroup(Protocol[_WElement]):
    n: int
    def coxeter_type(self) -> CoxeterType: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[CoxeterIndex, ...]: ...
    def one(self) -> _WElement: ...
    def simple_reflection(self, i: CoxeterIndex) -> _WElement: ...
    def simple_reflections(self) -> _CoxeterElementFamily[_WElement]: ...
    def from_reduced_word(self, word: CoxeterWord) -> _WElement: ...
    def pieri_factors(self) -> Iterable[_WElement]: ...
    def is_finite(self) -> bool: ...
    def is_commutative(self) -> bool: ...
    def __contains__(self, value: object) -> bool: ...

type CoxeterGroupInput[_WElement: _CoxeterGroupElement] = (
    _CoxeterGroup[_WElement] | CoxeterTypeData
)

class _HeckeGeneratorFamily(Protocol[_Coefficient, _WElement]):
    def __getitem__(
        self,
        i: CoxeterIndex,
    ) -> _HeckeElement[_Coefficient, _WElement]: ...
    def __iter__(
        self,
    ) -> Iterator[_HeckeElement[_Coefficient, _WElement]]: ...
    def keys(self) -> Iterable[CoxeterIndex]: ...

class _HeckeElement(
    CombinatorialFreeModule.Element,
    Generic[_Coefficient, _WElement],
):
    def parent(self) -> IwahoriHeckeAlgebra._Basis[_Coefficient, _WElement]: ...
    def monomial_coefficients(
        self,
        copy: bool = True,
    ) -> dict[_WElement, _Coefficient]: ...
    def bar(self) -> Self: ...
    def hash_involution(self) -> Self: ...
    def goldman_involution(self) -> Self: ...
    def specialize_to(
        self,
        new_hecke: IwahoriHeckeAlgebra[_NewCoefficient, _WElement],
        num_vars: int = 2,
    ) -> _HeckeElement[_NewCoefficient, _WElement]: ...

def normalized_laurent_polynomial(
    R: _CoefficientRing[_Coefficient],
    p: HeckeParameter,
) -> _Coefficient: ...

def index_cmp(
    x: _WElement,
    y: _WElement,
) -> int: ...

class IwahoriHeckeAlgebra(
    Parent[_HeckeElement[_Coefficient, _WElement]],
    UniqueRepresentation,
    Generic[_Coefficient, _WElement],
):
    @staticmethod
    def __classcall_private__(
        cls: type[Self],
        W: CoxeterGroupInput[_WElement],
        q1: _Coefficient | Integer | int,
        q2: _Coefficient | Integer | int = -1,
        base_ring: _CoefficientRing[_Coefficient] | None = None,
    ) -> Self: ...
    def __init__(
        self,
        W: _CoxeterGroup[_WElement],
        q1: _Coefficient,
        q2: _Coefficient,
        base_ring: _CoefficientRing[_Coefficient],
    ) -> None: ...
    def base_ring(self) -> _CoefficientRing[_Coefficient]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _bar_on_coefficients(self, c: _Coefficient) -> _Coefficient: ...
    def coxeter_type(self) -> CoxeterType: ...
    def cartan_type(self) -> CartanType_abstract | None: ...
    def coxeter_group(self) -> _CoxeterGroup[_WElement]: ...
    def a_realization(self) -> IwahoriHeckeAlgebra.T[_Coefficient, _WElement]: ...
    def q1(self) -> _Coefficient: ...
    def q2(self) -> _Coefficient: ...

    class _Basis(
        CombinatorialFreeModule,
        Generic[_Coefficient, _WElement],
    ):
        Element: type[_HeckeElement[_Coefficient, _WElement]]
        def __init__(
            self,
            algebra: IwahoriHeckeAlgebra[_Coefficient, _WElement],
            prefix: str | None = None,
        ) -> None: ...
        def realization_of(
            self,
        ) -> IwahoriHeckeAlgebra[_Coefficient, _WElement]: ...
        def base_ring(self) -> _CoefficientRing[_Coefficient]: ...
        @overload
        def __getitem__(
            self,
            i: _WElement,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        @overload
        def __getitem__(
            self,
            i: CoxeterIndex | CoxeterWord,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def __call__(
            self,
            value: _HeckeElement[_Coefficient, _WElement] | _WElement,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def one_basis(self) -> _WElement: ...
        def index_set(self) -> tuple[CoxeterIndex, ...]: ...
        def algebra_generators(
            self,
        ) -> _HeckeGeneratorFamily[_Coefficient, _WElement]: ...
        def algebra_generator(
            self,
            i: CoxeterIndex,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def monomial(
            self,
            index: _WElement,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def sum_of_monomials(
            self,
            indices: Iterable[_WElement],
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def zero(self) -> _HeckeElement[_Coefficient, _WElement]: ...
        def one(self) -> _HeckeElement[_Coefficient, _WElement]: ...
        def product_on_basis(
            self,
            w1: _WElement,
            w2: _WElement,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def _repr_term(self, t: _WElement) -> str: ...
        def _latex_term(self, t: _WElement) -> str: ...

    class T(_Basis[_Coefficient, _WElement]):
        def __init__(
            self,
            algebra: IwahoriHeckeAlgebra[_Coefficient, _WElement] | None = None,
            prefix: str | None = None,
        ) -> None: ...
        def inverse_generator(
            self,
            i: CoxeterIndex,
        ) -> _HeckeElement[_Coefficient, _WElement]: ...
        def inverse_generators(
            self,
        ) -> _HeckeGeneratorFamily[_Coefficient, _WElement]: ...

    class C(_Basis[_Coefficient, _WElement]):
        def __init__(
            self,
            algebra: IwahoriHeckeAlgebra[_Coefficient, _WElement] | None = None,
            prefix: str | None = None,
        ) -> None: ...

    class Cp(_Basis[_Coefficient, _WElement]):
        def __init__(
            self,
            algebra: IwahoriHeckeAlgebra[_Coefficient, _WElement] | None = None,
            prefix: str | None = None,
        ) -> None: ...

    class A(_Basis[_Coefficient, _WElement]):
        def __init__(
            self,
            algebra: IwahoriHeckeAlgebra[_Coefficient, _WElement] | None = None,
            prefix: str | None = None,
        ) -> None: ...

    class B(_Basis[_Coefficient, _WElement]):
        def __init__(
            self,
            algebra: IwahoriHeckeAlgebra[_Coefficient, _WElement] | None = None,
            prefix: str | None = None,
        ) -> None: ...

class IwahoriHeckeAlgebra_nonstandard(
    IwahoriHeckeAlgebra[_Coefficient, _WElement],
    Generic[_Coefficient, _WElement],
): ...
