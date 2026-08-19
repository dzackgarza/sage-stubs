from collections.abc import Iterator, Mapping
from typing import Literal, TypeVar, overload

from sage.matrix.matrix import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_PolynomialValue = TypeVar("_PolynomialValue", bound=RingElement)


def row_iterator(
    A: Matrix[_Scalar],
) -> Iterator[FreeModuleElement[_Scalar]]: ...


def prm_mul(
    p1: Mapping[int, _PolynomialValue],
    p2: Mapping[int, _PolynomialValue],
    mask_free: int,
    prec: int | None,
) -> dict[int, _PolynomialValue]: ...


@overload
def permanental_minor_polynomial(
    A: Matrix[_Scalar],
    permanent_only: Literal[False] = ...,
    var: str = ...,
    prec: int | None = ...,
) -> Polynomial: ...


@overload
def permanental_minor_polynomial(
    A: Matrix[_Scalar],
    permanent_only: Literal[True],
    var: str = ...,
    prec: int | None = ...,
) -> _Scalar: ...


@overload
def permanental_minor_polynomial(
    A: Matrix[_Scalar],
    permanent_only: bool,
    var: str = ...,
    prec: int | None = ...,
) -> Polynomial | _Scalar: ...
