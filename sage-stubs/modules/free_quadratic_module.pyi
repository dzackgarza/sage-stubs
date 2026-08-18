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

from sage.matrix.matrix2 import Matrix

type _BasisVector = FreeModuleElement | Iterable[Element | int | Integer]
type _BasisData = Matrix | Iterable[_BasisVector]

def FreeQuadraticModule(
    base_ring: Ring,
    rank: int | Integer,
    inner_product_matrix: MatrixData,
    sparse: bool = ...,
    inner_product_ring: Ring | None = ...,
) -> FreeQuadraticModule_generic: ...
def QuadraticSpace(
    K: Ring,
    dimension: int | Integer,
    inner_product_matrix: MatrixData,
    sparse: bool = ...,
) -> FreeQuadraticModule_generic_field: ...

class FreeQuadraticModule_generic(FreeModule_generic):
    def __init__(
        self,
        base_ring: Ring,
        rank: int | Integer,
        degree: int | Integer,
        inner_product_matrix: ElementConstructorInput,
        sparse: bool = ...,
    ) -> None: ...
    def ambient_module(self) -> FreeModule_generic: ...
    def determinant(self) -> _Scalar: ...
    def discriminant(self) -> FreeQuadraticModule_generic_pid: ...
    def gram_matrix(self) -> Matrix[_Scalar]: ...
    def inner_product_matrix(self) -> Matrix[_Scalar]: ...

class FreeQuadraticModule_generic_pid(
    FreeModule_generic_pid, FreeQuadraticModule_generic
):
    def span(
        self,
        gens: FreeModule_generic | _BasisData,
        base_ring: Ring | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_with_basis_pid: ...
    def submodule(
        self, gens: _BasisData, check: bool = ..., already_echelonized: bool = ...
    ) -> FreeQuadraticModule_submodule_pid: ...
    def span_of_basis(
        self,
        basis: ElementConstructorInput,
        base_ring: Ring | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_with_basis_pid: ...
    def zero_submodule(self) -> FreeQuadraticModule_submodule_pid: ...

class FreeQuadraticModule_generic_field(
    FreeModule_generic_field, FreeQuadraticModule_generic_pid
):
    def __init__(
        self,
        base_field: Ring,
        dimension: int | Integer,
        degree: int | Integer,
        inner_product_matrix: ElementConstructorInput,
        sparse: bool = ...,
    ) -> None: ...
    def span(
        self,
        gens: FreeModule_generic | _BasisData,
        base_ring: Ring | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_field: ...
    def span_of_basis(
        self,
        basis: ElementConstructorInput,
        base_ring: Ring | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_with_basis_field: ...

class FreeQuadraticModule_ambient(FreeModule_ambient, FreeQuadraticModule_generic):
    def __init__(
        self,
        base_ring: Ring,
        rank: int | Integer,
        inner_product_matrix: ElementConstructorInput,
        sparse: bool = ...,
    ) -> None: ...

class FreeQuadraticModule_ambient_domain(
    FreeModule_ambient_domain, FreeQuadraticModule_ambient
):
    def __init__(
        self,
        base_ring: Ring,
        rank: int | Integer,
        inner_product_matrix: ElementConstructorInput,
        sparse: bool = ...,
    ) -> None: ...
    def ambient_vector_space(self) -> FreeQuadraticModule_ambient_field: ...

class FreeQuadraticModule_ambient_pid(
    FreeModule_ambient_pid,
    FreeQuadraticModule_generic_pid,
    FreeQuadraticModule_ambient_domain,
): ...

class FreeQuadraticModule_ambient_field(
    FreeModule_ambient_field,
    FreeQuadraticModule_generic_field,
    FreeQuadraticModule_ambient_pid,
):
    def ambient_vector_space(self) -> FreeQuadraticModule_ambient_field: ...

class FreeQuadraticModule_submodule_with_basis_pid(
    FreeModule_submodule_with_basis_pid, FreeQuadraticModule_generic_pid
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic,
        basis: _BasisData,
        inner_product_matrix: ElementConstructorInput,
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
    def change_ring(self, R: Ring) -> FreeQuadraticModule_generic: ...

class FreeQuadraticModule_submodule_pid(
    FreeModule_submodule_pid, FreeQuadraticModule_submodule_with_basis_pid
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic,
        gens: _BasisData,
        inner_product_matrix: ElementConstructorInput,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...

class FreeQuadraticModule_submodule_with_basis_field(
    FreeModule_submodule_with_basis_field,
    FreeQuadraticModule_generic_field,
    FreeQuadraticModule_submodule_with_basis_pid,
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic,
        basis: _BasisData,
        inner_product_matrix: ElementConstructorInput,
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...

class FreeQuadraticModule_submodule_field(
    FreeModule_submodule_field, FreeQuadraticModule_submodule_with_basis_field
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic,
        gens: _BasisData,
        inner_product_matrix: ElementConstructorInput,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
