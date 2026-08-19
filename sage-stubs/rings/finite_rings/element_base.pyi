from collections.abc import Iterator
from typing import Generic, Self, TypeVar

from sage.categories.map import Map
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Field
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject


class gen: ...


class FiniteRingElement(RingElement):
    def _nth_root_common(
        self,
        n: int | Integer,
        all: bool,
        algorithm: str | None,
        cunningham: bool,
    ) -> Self | list[Self] | None: ...
    def to_bytes(self, byteorder: str = ...) -> bytes: ...
    def canonical_associate(self) -> Self: ...
    def minpoly_over(
        self,
        F: Field,
        var: str = ...,
    ) -> Polynomial: ...


_Coefficient = TypeVar(
    "_Coefficient",
    bound=FiniteRingElement,
    default=FiniteRingElement,
)


class FinitePolyExtElement(
    FiniteRingElement,
    Generic[_Coefficient],
):
    def _im_gens_(
        self,
        codomain: Parent,
        im_gens: tuple[Element, ...],
        base_map: Map | None = ...,
    ) -> Element: ...
    def minpoly(
        self,
        var: str = ...,
        algorithm: str = ...,
    ) -> Polynomial: ...
    def minimal_polynomial(self, var: str = ...) -> Polynomial: ...
    def __getitem__(self, n: int) -> _Coefficient: ...
    def list(self) -> list[_Coefficient]: ...
    def __iter__(self) -> Iterator[_Coefficient]: ...
    def _vector_(
        self,
        reverse: bool = ...,
    ) -> FreeModuleElement[_Coefficient]: ...
    def matrix(
        self,
        reverse: bool = ...,
    ) -> Matrix[_Coefficient]: ...
    def _latex_(self) -> str: ...
    def __pari__(self, var: str | None = ...) -> gen: ...
    def _pari_init_(self, var: str | None = ...) -> str: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str = ...,
    ) -> Polynomial: ...
    def norm(self) -> _Coefficient: ...
    def trace(self) -> _Coefficient: ...
    def multiplicative_order(self) -> Integer: ...
    def additive_order(self) -> Integer: ...
    def is_square(self) -> bool: ...
    def square_root(
        self,
        extend: bool = ...,
        all: bool = ...,
    ) -> Self | list[Self] | None: ...
    def sqrt(
        self,
        extend: bool = ...,
        all: bool = ...,
    ) -> Self | list[Self] | None: ...
    def nth_root(
        self,
        n: int | Integer,
        extend: bool = ...,
        all: bool = ...,
        algorithm: str | None = ...,
        cunningham: bool = ...,
    ) -> Self | list[Self] | None: ...
    def pth_power(self, k: int | Integer = ...) -> Self: ...
    def pth_root(self, k: int | Integer = ...) -> Self: ...
    def conjugate(self) -> Self: ...
    def to_integer(self, reverse: bool = ...) -> Integer: ...
    def to_bytes(self, byteorder: str = ...) -> bytes: ...


class Cache_base(
    SageObject,
    Generic[_Coefficient],
):
    def fetch_int(self, number: int | Integer) -> FinitePolyExtElement[_Coefficient]: ...
