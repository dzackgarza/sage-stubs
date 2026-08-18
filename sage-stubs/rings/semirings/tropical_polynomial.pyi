from collections.abc import Mapping, Sequence

from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_element_generic import Polynomial_generic_sparse
from sage.rings.semirings.tropical_semiring import (
    TropicalSemiring,
    TropicalSemiringElement,
)
from sage.structure.element import Element, ModuleElement
from sage.structure.factorization import Factorization
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression

type _TropicalDegree = int | Integer | tuple[int | Integer, int | Integer]
type _TropicalPolynomialInput = (
    TropicalPolynomial
    | Polynomial
    | Sequence[ElementConstructorInput]
    | Mapping[int | Integer, ElementConstructorInput]
    | ElementConstructorInput
    | None
)
type _InterpolationPoint = tuple[ElementConstructorInput, ElementConstructorInput]

class TropicalPolynomial(Polynomial_generic_sparse):
    def parent(self) -> TropicalPolynomialSemiring: ...
    def roots(self) -> list[TropicalSemiringElement[ModuleElement]]: ...
    def split_form(self) -> TropicalPolynomial: ...
    def factor(self) -> Factorization: ...
    def piecewise_function(self) -> Expression | ModuleElement: ...
    def plot(
        self,
        xmin: ElementConstructorInput | None = ...,
        xmax: ElementConstructorInput | None = ...,
    ) -> Graphics: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

class TropicalPolynomialSemiring(
    UniqueRepresentation,
    Parent[TropicalPolynomial],
):
    Element: type[TropicalPolynomial]
    @staticmethod
    def __classcall_private__(
        class_: type[TropicalPolynomialSemiring],
        base_semiring: TropicalSemiring[ModuleElement],
        names: str | tuple[str, ...],
    ) -> TropicalPolynomialSemiring: ...
    def __init__(
        self,
        base_semiring: TropicalSemiring[ModuleElement],
        names: str | tuple[str, ...],
    ) -> None: ...
    def base(self) -> TropicalSemiring[ModuleElement]: ...
    def base_ring(self) -> TropicalSemiring[ModuleElement]: ...
    def one(self) -> TropicalPolynomial: ...
    def zero(self) -> TropicalPolynomial: ...
    def gen(self, n: int | Integer = ...) -> TropicalPolynomial: ...
    def gens(self) -> tuple[TropicalPolynomial]: ...
    def ngens(self) -> Integer: ...
    def random_element(
        self,
        degree: _TropicalDegree = ...,
        monic: bool = ...,
        *args: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> TropicalPolynomial: ...
    def is_sparse(self) -> bool: ...
    def interpolation(
        self,
        points: Sequence[_InterpolationPoint],
    ) -> TropicalPolynomial: ...
    def _element_constructor_(
        self,
        x: _TropicalPolynomialInput = ...,
        check: bool = ...,
    ) -> TropicalPolynomial: ...
    def _repr_(self) -> str: ...
    @classmethod
    def _implementation_names(
        cls,
        implementation: None,
        base_ring: TropicalSemiring[ModuleElement],
        sparse: bool,
    ) -> list[None]: ...
