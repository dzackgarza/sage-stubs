from collections.abc import Iterable, Sequence
from typing import Generic, TypeVar, overload

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import (
    FreeModule_ambient,
    FreeModule_ambient_domain,
    FreeModule_ambient_field,
    FreeModule_ambient_pid,
    FreeModule_generic,
    FreeModule_generic_field,
    FreeModule_generic_pid,
    FreeModule_submodule_field,
    FreeModule_submodule_pid,
    FreeModule_submodule_with_basis_field,
    FreeModule_submodule_with_basis_pid,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import FieldElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)

type QuadraticModuleVector[_Scalar: RingElement] = (
    FreeModuleElement[_Scalar]
    | Sequence[ElementConstructorInput]
)
type QuadraticModuleBasis[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | Iterable[QuadraticModuleVector[_Scalar]]
)
type InnerProductMatrix[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | Iterable[ElementConstructorInput]
)

@overload
def FreeQuadraticModule(
    base_ring: Parent[_FieldScalar],
    rank: int | Integer,
    inner_product_matrix: InnerProductMatrix[_FieldScalar],
    sparse: bool = ...,
    inner_product_ring: None = ...,
) -> FreeQuadraticModule_ambient_field[_FieldScalar]: ...
@overload
def FreeQuadraticModule(
    base_ring: Parent[_Scalar],
    rank: int | Integer,
    inner_product_matrix: InnerProductMatrix[_Scalar],
    sparse: bool = ...,
    inner_product_ring: Parent | None = ...,
) -> FreeQuadraticModule_ambient[_Scalar]: ...

def QuadraticSpace(
    K: Parent[_FieldScalar],
    dimension: int | Integer,
    inner_product_matrix: InnerProductMatrix[_FieldScalar],
    sparse: bool = ...,
) -> FreeQuadraticModule_ambient_field[_FieldScalar]: ...

InnerProductSpace = QuadraticSpace

class FreeQuadraticModule_generic(
    FreeModule_generic[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        rank: int | Integer,
        degree: int | Integer,
        inner_product_matrix: Matrix[_Scalar],
        sparse: bool = ...,
    ) -> None: ...
    def ambient_module(self) -> FreeQuadraticModule_ambient[_Scalar]: ...
    def determinant(self) -> _Scalar: ...
    def discriminant(self) -> _Scalar: ...
    def gram_matrix(self) -> Matrix[_Scalar]: ...
    def inner_product_matrix(self) -> Matrix[_Scalar]: ...
    def _inner_product_is_dot_product(self) -> bool: ...
    def _inner_product_is_diagonal(self) -> bool: ...

class FreeQuadraticModule_generic_pid(
    FreeModule_generic_pid[_Scalar],
    FreeQuadraticModule_generic[_Scalar],
    Generic[_Scalar],
):
    def span(
        self,
        gens: FreeModule_generic[_Scalar] | QuadraticModuleBasis[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_pid[_Scalar]: ...
    def span_of_basis(
        self,
        basis: QuadraticModuleBasis[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_with_basis_pid[_Scalar]: ...
    def submodule(
        self,
        gens: QuadraticModuleBasis[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_pid[_Scalar]: ...
    def zero_submodule(self) -> FreeQuadraticModule_submodule_pid[_Scalar]: ...

class FreeQuadraticModule_generic_field(
    FreeModule_generic_field[_FieldScalar],
    FreeQuadraticModule_generic_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def span(
        self,
        gens: FreeModule_generic[_FieldScalar] | QuadraticModuleBasis[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_field[_FieldScalar]: ...
    def span_of_basis(
        self,
        basis: QuadraticModuleBasis[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_with_basis_field[_FieldScalar]: ...
    def submodule(
        self,
        gens: QuadraticModuleBasis[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeQuadraticModule_submodule_field[_FieldScalar]: ...

class FreeQuadraticModule_ambient(
    FreeModule_ambient[_Scalar],
    FreeQuadraticModule_generic[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        rank: int | Integer,
        inner_product_matrix: Matrix[_Scalar],
        sparse: bool = ...,
    ) -> None: ...

class FreeQuadraticModule_ambient_domain(
    FreeModule_ambient_domain[_Scalar],
    FreeQuadraticModule_ambient[_Scalar],
    Generic[_Scalar],
):
    def ambient_vector_space(
        self,
    ) -> FreeQuadraticModule_ambient_field[FieldElement]: ...

class FreeQuadraticModule_ambient_pid(
    FreeModule_ambient_pid[_Scalar],
    FreeQuadraticModule_generic_pid[_Scalar],
    FreeQuadraticModule_ambient_domain[_Scalar],
    Generic[_Scalar],
): ...

class FreeQuadraticModule_ambient_field(
    FreeModule_ambient_field[_FieldScalar],
    FreeQuadraticModule_generic_field[_FieldScalar],
    FreeQuadraticModule_ambient_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def ambient_vector_space(
        self,
    ) -> FreeQuadraticModule_ambient_field[_FieldScalar]: ...

class FreeQuadraticModule_submodule_with_basis_pid(
    FreeModule_submodule_with_basis_pid[_Scalar],
    FreeQuadraticModule_generic_pid[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic[_Scalar],
        basis: QuadraticModuleBasis[_Scalar],
        inner_product_matrix: Matrix[_Scalar],
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[_Scalar] | None = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FreeQuadraticModule_generic[_NewScalar]: ...

class FreeQuadraticModule_submodule_pid(
    FreeModule_submodule_pid[_Scalar],
    FreeQuadraticModule_submodule_with_basis_pid[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic[_Scalar],
        gens: QuadraticModuleBasis[_Scalar],
        inner_product_matrix: Matrix[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...

class FreeQuadraticModule_submodule_with_basis_field(
    FreeModule_submodule_with_basis_field[_FieldScalar],
    FreeQuadraticModule_generic_field[_FieldScalar],
    FreeQuadraticModule_submodule_with_basis_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic[_FieldScalar],
        basis: QuadraticModuleBasis[_FieldScalar],
        inner_product_matrix: Matrix[_FieldScalar],
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[_FieldScalar] | None = ...,
        already_echelonized: bool = ...,
    ) -> None: ...

class FreeQuadraticModule_submodule_field(
    FreeModule_submodule_field[_FieldScalar],
    FreeQuadraticModule_submodule_with_basis_field[_FieldScalar],
    Generic[_FieldScalar],
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic[_FieldScalar],
        gens: QuadraticModuleBasis[_FieldScalar],
        inner_product_matrix: Matrix[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
