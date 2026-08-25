from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Generic, TypeVar

from sage.algebras.letterplace.free_algebra_element_letterplace import (
    FreeAlgebraElement_letterplace,
)
from sage.algebras.letterplace.letterplace_ideal import LetterplaceIdeal
from sage.rings.integer import Integer
from sage.rings.noncommutative_ideals import IdealMonoid_nc
from sage.rings.polynomial.multi_polynomial_ideal import MPolynomialIdeal
from sage.rings.polynomial.multi_polynomial_libsingular import (
    MPolynomial_libsingular,
    MPolynomialRing_libsingular,
)
from sage.rings.polynomial.term_order import TermOrder
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type LetterplaceDegrees = Sequence[int | Integer] | None
type LetterplacePickleArgument = MPolynomialRing_libsingular | tuple[int, ...] | None
type LetterplaceCoefficientInput[_Scalar: RingElement] = _Scalar | int | Integer
type LetterplaceElementInput[_Scalar: RingElement] = (
    FreeAlgebraElement_letterplace[_Scalar]
    | MPolynomial_libsingular
    | ElementConstructorInput
    | str
)

class FreeAlgebra_letterplace(
    Parent[FreeAlgebraElement_letterplace[_Scalar]],
    Generic[_Scalar],
):
    def __init__(
        self,
        R: MPolynomialRing_libsingular,
        degrees: LetterplaceDegrees = ...,
    ) -> None: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., FreeAlgebra_letterplace[_Scalar]],
        tuple[LetterplacePickleArgument, ...],
    ]: ...
    def ngens(self) -> int: ...
    def gen(
        self,
        i: int | Integer,
    ) -> FreeAlgebraElement_letterplace[_Scalar]: ...
    def gens(self) -> tuple[FreeAlgebraElement_letterplace[_Scalar], ...]: ...
    def current_ring(self) -> MPolynomialRing_libsingular: ...
    def commutative_ring(self) -> MPolynomialRing_libsingular: ...
    def term_order_of_block(self) -> TermOrder: ...
    def generator_degrees(self) -> tuple[int, ...]: ...
    def is_field(self, proof: bool = ...) -> bool: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def degbound(self) -> int: ...
    def set_degbound(self, d: int | Integer) -> None: ...
    def _ideal_class_(
        self,
        n: int | Integer = ...,
    ) -> type[LetterplaceIdeal[_Scalar]]: ...
    def ideal_monoid(self) -> IdealMonoid_nc: ...
    def _reductor_(
        self,
        g: Iterable[FreeAlgebraElement_letterplace[_Scalar]],
        d: int | Integer,
    ) -> MPolynomialIdeal: ...
    def _coerce_map_from_(self, S: Parent | type) -> bool: ...
    def _an_element_(self) -> FreeAlgebraElement_letterplace[_Scalar]: ...
    def _from_dict_(
        self,
        D: Mapping[tuple[int, ...], LetterplaceCoefficientInput[_Scalar]],
        check: bool = ...,
    ) -> FreeAlgebraElement_letterplace[_Scalar]: ...
    def _element_constructor_(
        self,
        x: LetterplaceElementInput[_Scalar],
    ) -> FreeAlgebraElement_letterplace[_Scalar]: ...

class FreeAlgebra_letterplace_libsingular:
    def __init__(
        self,
        commutative_ring: MPolynomialRing_libsingular,
        degbound: int | Integer,
    ) -> None: ...
