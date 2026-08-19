from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Generic, Self, TypeVar

from sage.categories.action import Action
from sage.categories.morphism import Morphism
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoidElement
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial
from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialRing_dense
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.ring import CommutativeRing
from sage.sets.family import AbstractFamily
from sage.structure.element import CommutativeRingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar(
    "_Scalar",
    bound=CommutativeRingElement,
    default=CommutativeRingElement,
)
_Monomial = TypeVar("_Monomial")

type ExponentTuple = tuple[int | Integer, ...]
type WeylBasisKey = tuple[ExponentTuple, ExponentTuple]
type PolynomialRingType = PolynomialRing_generic | MPolynomialRing_base
type PolynomialElement = Polynomial | MPolynomial
type InfiniteMonomial = IndexedFreeAbelianMonoidElement[int]
type InfiniteWeylBasisKey = tuple[InfiniteMonomial, InfiniteMonomial]

def repr_from_monomials(
    monomials: Iterable[tuple[_Monomial, _Scalar]],
    term_repr: Callable[[_Monomial], str],
    use_latex: bool = ...,
) -> str: ...
def repr_factored(
    w: DifferentialWeylAlgebraElement[_Scalar],
    latex_output: bool = ...,
) -> str: ...

class DifferentialWeylAlgebraElement(
    IndexedFreeModuleElement[WeylBasisKey, _Scalar],
    Generic[_Scalar],
):
    def parent(self) -> DifferentialWeylAlgebra[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _mul_(
        self,
        other: DifferentialWeylAlgebraElement[_Scalar],
    ) -> Self: ...
    def _rmul_(self, other: _Scalar) -> Self: ...
    def _lmul_(self, other: _Scalar) -> Self: ...
    def __truediv__(self, x: _Scalar) -> Self: ...
    def __iter__(self) -> Iterator[tuple[WeylBasisKey, _Scalar]]: ...
    def list(self) -> list[tuple[WeylBasisKey, _Scalar]]: ...
    def factor_differentials(
        self,
    ) -> dict[ExponentTuple, PolynomialElement]: ...
    def diff(self, p: PolynomialElement) -> PolynomialElement: ...

class DifferentialWeylAlgebra(
    UniqueRepresentation,
    Parent[DifferentialWeylAlgebraElement[_Scalar]],
    Generic[_Scalar],
):
    Element: type[DifferentialWeylAlgebraElement[_Scalar]]
    element_class: type[DifferentialWeylAlgebraElement[_Scalar]]
    diff_action: DifferentialWeylAlgebraAction[_Scalar]

    @staticmethod
    def __classcall_private__(
        cls: type[DifferentialWeylAlgebra[_Scalar]],
        R: CommutativeRing | PolynomialRingType | InfinitePolynomialRing_dense,
        names: str | Iterable[str] | None = ...,
        n: int | Integer | PlusInfinity | None = ...,
    ) -> DifferentialWeylAlgebra[_Scalar] | InfGenDifferentialWeylAlgebra[_Scalar]: ...
    def __init__(
        self,
        R: CommutativeRing,
        names: tuple[str, ...],
        n: int | Integer | None = ...,
    ) -> None: ...
    def base_ring(self) -> CommutativeRing: ...
    def variable_names(self) -> tuple[str, ...]: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: DifferentialWeylAlgebraElement[_Scalar]
        | PolynomialElement
        | _Scalar
        | object,
    ) -> DifferentialWeylAlgebraElement[_Scalar]: ...
    def _coerce_map_from_(self, R: object) -> bool | Morphism | None: ...
    def degree_on_basis(self, i: WeylBasisKey) -> int | Integer: ...
    def polynomial_ring(self) -> PolynomialRingType: ...
    def basis(self) -> AbstractFamily: ...
    def algebra_generators(self) -> AbstractFamily: ...
    gens = algebra_generators
    def variables(self) -> AbstractFamily: ...
    def differentials(self) -> AbstractFamily: ...
    def gen(
        self,
        i: int | Integer,
    ) -> DifferentialWeylAlgebraElement[_Scalar]: ...
    def ngens(self) -> int: ...
    def one(self) -> DifferentialWeylAlgebraElement[_Scalar]: ...
    def zero(self) -> DifferentialWeylAlgebraElement[_Scalar]: ...

class DifferentialWeylAlgebraAction(
    Action,
    Generic[_Scalar],
):
    def __init__(self, G: DifferentialWeylAlgebra[_Scalar]) -> None: ...
    def _act_(
        self,
        g: DifferentialWeylAlgebraElement[_Scalar],
        x: PolynomialElement,
    ) -> PolynomialElement: ...
    def actor(self) -> DifferentialWeylAlgebra[_Scalar]: ...
    def underlying_set(self) -> PolynomialRingType: ...
    def right_domain(self) -> PolynomialRingType: ...

class InfGenDifferentialWeylAlgebraElement(
    IndexedFreeModuleElement[InfiniteWeylBasisKey, _Scalar],
    Generic[_Scalar],
):
    def parent(self) -> InfGenDifferentialWeylAlgebra[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _mul_(
        self,
        other: InfGenDifferentialWeylAlgebraElement[_Scalar],
    ) -> Self: ...
    def __iter__(
        self,
    ) -> Iterator[tuple[InfiniteWeylBasisKey, _Scalar]]: ...
    def list(self) -> list[tuple[InfiniteWeylBasisKey, _Scalar]]: ...

class InfGenDifferentialWeylAlgebra(
    UniqueRepresentation,
    Parent[InfGenDifferentialWeylAlgebraElement[_Scalar]],
    Generic[_Scalar],
):
    Element: type[InfGenDifferentialWeylAlgebraElement[_Scalar]]
    element_class: type[InfGenDifferentialWeylAlgebraElement[_Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[InfGenDifferentialWeylAlgebra[_Scalar]],
        R: CommutativeRing | InfinitePolynomialRing_dense,
        names: str | Iterable[str] | None = ...,
    ) -> InfGenDifferentialWeylAlgebra[_Scalar]: ...
    def __init__(
        self,
        R: CommutativeRing,
        names: tuple[str, ...],
    ) -> None: ...
    def base_ring(self) -> CommutativeRing: ...
    def variable_names(self) -> tuple[str, str]: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: InfGenDifferentialWeylAlgebraElement[_Scalar]
        | InfinitePolynomial
        | Mapping[InfiniteWeylBasisKey, _Scalar]
        | _Scalar
        | object,
    ) -> InfGenDifferentialWeylAlgebraElement[_Scalar]: ...
    def _coerce_map_from_(self, R: object) -> bool | Morphism | None: ...
    def gen(
        self,
        i: int | Integer,
    ) -> InfGenDifferentialWeylAlgebraElement[_Scalar]: ...
    def polynomial_gens(self) -> AbstractFamily: ...
    def gens(self) -> tuple[AbstractFamily, AbstractFamily]: ...
    def differential(
        self,
        i: int | Integer,
    ) -> InfGenDifferentialWeylAlgebraElement[_Scalar]: ...
    def differentials(self) -> AbstractFamily: ...
    def zero(self) -> InfGenDifferentialWeylAlgebraElement[_Scalar]: ...
    def one_basis(self) -> InfiniteWeylBasisKey: ...
    def one(self) -> InfGenDifferentialWeylAlgebraElement[_Scalar]: ...
    def basis(self) -> AbstractFamily: ...
    def degree_on_basis(
        self,
        x: InfiniteWeylBasisKey,
    ) -> int | Integer: ...
