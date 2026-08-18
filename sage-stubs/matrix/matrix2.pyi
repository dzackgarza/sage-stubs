from collections.abc import Iterator, Sequence
from typing import Self, TypeVar
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_double import RealDoubleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type MatrixIndex = (
    int | Integer | slice | tuple[int | Integer | slice, int | Integer | slice]
)

class Matrix(MatrixElement):
    def __getitem__(self, key: MatrixIndex) -> FreeModuleElement[_Scalar] | _Scalar: ...
    def base_ring(self) -> Ring: ...
    def determinant(self, algorithm: str | None = None) -> _Scalar: ...
    def det(self, *args: str | None, **kwds: str | bool | None) -> _Scalar: ...
    def elementary_divisors(
        self, algorithm: str | None = None
    ) -> ElementConstructorInput: ...
    def ncols(self) -> int: ...
    def nrows(self) -> int: ...
    def subdivisions(self) -> tuple[list[int], list[int]]: ...
