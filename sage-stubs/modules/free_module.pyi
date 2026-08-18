from collections.abc import Iterable, Iterator, Sequence
from typing import Generic, Self, TypeVar, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)


def FreeModule(
    base_ring: Parent[_Scalar],
    rank: int | Integer,
    degree: int | Integer | None = ...,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_Scalar] | None = ...,
    with_basis: str | None = ...,
    **kwds: object,
) -> FreeModule_ambient[_Scalar]: ...


class FreeModule_generic(
    Parent[FreeModuleElement[_Scalar]],
    Generic[_Scalar],
):
    Element: type[FreeModuleElement[_Scalar]]
    def base_ring(self) -> Parent[_Scalar]: ...
    def rank(self) -> int: ...
    dimension = rank
    def degree(self) -> int: ...
    def is_ambient(self) -> bool: ...
    def is_submodule(self, other: FreeModule_generic[_Scalar]) -> bool: ...
    def is_full(self) -> bool: ...
    def is_sparse(self) -> bool: ...
    def ambient_module(self) -> FreeModule_ambient[_Scalar]: ...
    def zero(self) -> FreeModuleElement[_Scalar]: ...
    def an_element(self) -> FreeModuleElement[_Scalar]: ...
    def random_element(self, *args: object, **kwds: object) -> FreeModuleElement[_Scalar]: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...
    def _element_constructor_(
        self,
        x: Iterable[ElementConstructorInput] | FreeModuleElement[_Scalar] = ...,
        coerce: bool = ...,
        copy: bool = ...,
        check: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def ngens(self) -> int: ...
    def gen(self, i: int | Integer) -> FreeModuleElement[_Scalar]: ...
    def gens(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def basis(self) -> AbstractFamily: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...
    def echelonized_basis_matrix(self) -> Matrix[_Scalar]: ...
    def coordinate_vector(
        self,
        v: FreeModuleElement[_Scalar] | Iterable[ElementConstructorInput],
        check: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def linear_combination_of_basis(
        self,
        coefficients: Iterable[ElementConstructorInput],
    ) -> FreeModuleElement[_Scalar]: ...
    def matrix_space(self, ncols: int | Integer | None = ...) -> MatrixSpace[_Scalar]: ...
    def span(
        self,
        gens: Iterable[FreeModuleElement[_Scalar] | Iterable[ElementConstructorInput]],
        base_ring: Parent[_Scalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule[_Scalar]: ...
    submodule = span
    def submodule_with_basis(
        self,
        basis: Iterable[FreeModuleElement[_Scalar]],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule[_Scalar]: ...
    def quotient(
        self,
        submodule: FreeModule_generic[_Scalar],
        check: bool = ...,
    ) -> FreeModule_quotient[_Scalar]: ...
    def intersection(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_submodule[_Scalar]: ...
    def sum(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_submodule[_Scalar]: ...
    def saturation(self) -> FreeModule_submodule[_Scalar]: ...
    def index_in(self, other: FreeModule_generic[_Scalar]) -> Integer: ...
    def index_in_saturation(self) -> Integer: ...
    def dual_module(self) -> FreeModule_generic[_Scalar]: ...
    def tensor_product(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def direct_sum(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def change_ring(
        self,
        ring: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    base_extend = change_ring
    def hom(
        self,
        images: Matrix[_Scalar]
        | Sequence[FreeModuleElement[_Scalar]],
        codomain: FreeModule_generic[_Scalar] | None = ...,
        check: bool = ...,
    ) -> FreeModuleMorphism[_Scalar]: ...
    def Hom(
        self,
        codomain: FreeModule_generic[_Scalar],
    ) -> FreeModuleHomspace[_Scalar]: ...
    def identity_morphism(self) -> FreeModuleMorphism[_Scalar]: ...


class FreeModule_ambient(
    UniqueRepresentation,
    FreeModule_generic[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        rank: int | Integer,
        sparse: bool = ...,
        inner_product_matrix: Matrix[_Scalar] | None = ...,
        **kwds: object,
    ) -> None: ...
    def is_ambient(self) -> bool: ...
    def ambient_module(self) -> Self: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...


class FreeModule_submodule(FreeModule_generic[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        ambient: FreeModule_ambient[_Scalar],
        gens: Iterable[FreeModuleElement[_Scalar]],
        check: bool = ...,
        already_echelonized: bool = ...,
        **kwds: object,
    ) -> None: ...
    def ambient_module(self) -> FreeModule_ambient[_Scalar]: ...
    def is_ambient(self) -> bool: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...
    def echelonized_basis_matrix(self) -> Matrix[_Scalar]: ...


class VectorSpace(FreeModule_ambient[_Scalar], Generic[_Scalar]):
    pass


from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.quotient_module import FreeModule_quotient
