from collections.abc import Hashable, Iterable, Iterator, Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.module import Module
from sage.rings.integer import Integer
from sage.structure.element import FieldElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_CodomainScalar = TypeVar("_CodomainScalar", bound=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)
_BasisKey = TypeVar("_BasisKey", bound=Hashable)

type ModuleRank = int | Integer
type FreeModuleInput[_Scalar: RingElement] = (
    FreeModuleElement[_Scalar]
    | Sequence[ElementConstructorInput]
)
type GeneratorFamily[_Scalar: RingElement] = Iterable[FreeModuleInput[_Scalar]]
type FreeModuleWithBasis = Literal["standard"] | None

@overload
def FreeModule(
    base_ring: Parent[_Scalar],
    rank_or_basis_keys: ModuleRank,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_Scalar] | None = ...,
    *,
    with_basis: Literal["standard"] = ...,
    rank: None = ...,
    basis_keys: None = ...,
    **args: object,
) -> FreeModule_ambient[_Scalar]: ...
@overload
def FreeModule(
    base_ring: Parent[_Scalar],
    rank_or_basis_keys: Iterable[_BasisKey] | None = ...,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_Scalar] | None = ...,
    *,
    with_basis: Literal["standard"] = ...,
    rank: None = ...,
    basis_keys: Iterable[_BasisKey] | None = ...,
    **args: object,
) -> CombinatorialFreeModule: ...
@overload
def FreeModule(
    base_ring: Parent[_Scalar],
    rank_or_basis_keys: ModuleRank | None = ...,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_Scalar] | None = ...,
    *,
    with_basis: None,
    rank: ModuleRank | None = ...,
    basis_keys: None = ...,
    **args: object,
) -> FiniteRankFreeModule: ...

@overload
def VectorSpace(
    K: Parent[_FieldScalar],
    dimension_or_basis_keys: ModuleRank,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_FieldScalar] | None = ...,
    *,
    with_basis: Literal["standard"] = ...,
    dimension: None = ...,
    basis_keys: None = ...,
    **args: object,
) -> FreeModule_ambient_field[_FieldScalar]: ...
@overload
def VectorSpace(
    K: Parent[_FieldScalar],
    dimension_or_basis_keys: Iterable[_BasisKey] | None = ...,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_FieldScalar] | None = ...,
    *,
    with_basis: Literal["standard"] = ...,
    dimension: None = ...,
    basis_keys: Iterable[_BasisKey] | None = ...,
    **args: object,
) -> CombinatorialFreeModule: ...
@overload
def VectorSpace(
    K: Parent[_FieldScalar],
    dimension_or_basis_keys: ModuleRank | None = ...,
    sparse: bool = ...,
    inner_product_matrix: Matrix[_FieldScalar] | None = ...,
    *,
    with_basis: None,
    dimension: ModuleRank | None = ...,
    basis_keys: None = ...,
    **args: object,
) -> FiniteRankFreeModule: ...

def span(
    gens: GeneratorFamily[_Scalar],
    base_ring: Parent[_Scalar] | None = ...,
    check: bool = ...,
    already_echelonized: bool = ...,
) -> FreeModule_generic[_Scalar]: ...
def vector_space(
    span: GeneratorFamily[_FieldScalar],
    base_ring: Parent[_FieldScalar] | None = ...,
    check: bool = ...,
    already_echelonized: bool = ...,
) -> FreeModule_generic_field[_FieldScalar]: ...
def is_FreeModule(x: object) -> bool: ...

class FreeModule_generic(
    Module[_Scalar, FreeModuleElement[_Scalar]],
    Generic[_Scalar],
):
    Element: type[FreeModuleElement[_Scalar]]

    def __init__(
        self,
        base_ring: Parent[_Scalar],
        rank: ModuleRank,
        degree: ModuleRank,
        sparse: bool = ...,
        category: Category | None = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def rank(self) -> int: ...
    def dimension(self) -> int: ...
    def degree(self) -> int: ...
    def is_ambient(self) -> bool: ...
    def is_sparse(self) -> bool: ...
    def ngens(self) -> int: ...
    def gen(self, i: int = ...) -> FreeModuleElement[_Scalar]: ...
    def gens(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def basis(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...
    def echelonized_basis_matrix(self) -> Matrix[_Scalar]: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    def coordinate_vector(
        self,
        v: FreeModuleInput[_Scalar],
        check: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    coordinates = coordinate_vector
    def linear_combination_of_basis(
        self,
        coefficients: Sequence[ElementConstructorInput],
    ) -> FreeModuleElement[_Scalar]: ...
    def ambient_module(self) -> FreeModule_generic[_Scalar]: ...
    def ambient_vector_space(self) -> FreeModule_generic_field[FieldElement]: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    def base_extend(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    def span(
        self,
        gens: GeneratorFamily[_Scalar] | FreeModule_generic[_Scalar],
        base_ring: Parent[_Scalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_with_basis_pid[_Scalar]: ...
    span_of_basis = span
    def submodule(
        self,
        gens: GeneratorFamily[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_pid[_Scalar]: ...
    subspace = submodule
    def zero_submodule(self) -> FreeModule_submodule_pid[_Scalar]: ...
    def quotient(
        self,
        sub: FreeModule_generic[_Scalar],
        **kwds: object,
    ) -> FGP_Module_class[_Scalar] | FreeModule_ambient_field_quotient[_Scalar]: ...
    quo = quotient
    def intersection(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def direct_sum(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def dual_module(self) -> FreeModule_generic[_Scalar]: ...
    def random_element(
        self,
        *args: object,
        **kwds: object,
    ) -> FreeModuleElement[_Scalar]: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...
    def _Hom_(
        self,
        codomain: FreeModule_generic[_CodomainScalar],
        category: Category | None = ...,
    ) -> FreeModuleHomspace[_Scalar, _CodomainScalar]: ...
    @overload
    def hom(
        self,
        images: Sequence[FreeModuleInput[_Scalar]] | Matrix[_Scalar],
        codomain: None = ...,
        side: str = ...,
    ) -> FreeModuleMorphism[_Scalar, _Scalar]: ...
    @overload
    def hom(
        self,
        images: Sequence[FreeModuleInput[_CodomainScalar]] | Matrix[_CodomainScalar],
        codomain: FreeModule_generic[_CodomainScalar],
        side: str = ...,
    ) -> FreeModuleMorphism[_Scalar, _CodomainScalar]: ...

class FreeModule_generic_domain(
    FreeModule_generic[_Scalar],
    Generic[_Scalar],
): ...

class FreeModule_generic_pid(
    FreeModule_generic_domain[_Scalar],
    Generic[_Scalar],
): ...

class FreeModule_generic_field(
    FreeModule_generic_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def quotient(
        self,
        sub: FreeModule_generic_field[_FieldScalar],
        **kwds: object,
    ) -> FreeModule_ambient_field_quotient[_FieldScalar]: ...
    quo = quotient

class FreeModule_ambient(
    UniqueRepresentation,
    FreeModule_generic[_Scalar],
    Generic[_Scalar],
):
    def ambient_module(self) -> FreeModule_ambient[_Scalar]: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...

class FreeModule_ambient_domain(
    FreeModule_generic_domain[_Scalar],
    FreeModule_ambient[_Scalar],
    Generic[_Scalar],
): ...

class FreeModule_ambient_pid(
    FreeModule_generic_pid[_Scalar],
    FreeModule_ambient_domain[_Scalar],
    Generic[_Scalar],
): ...

class FreeModule_ambient_field(
    FreeModule_generic_field[_FieldScalar],
    FreeModule_ambient_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def ambient_vector_space(self) -> FreeModule_ambient_field[_FieldScalar]: ...

class FreeModule_submodule_with_basis_pid(
    FreeModule_generic_pid[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: FreeModule_generic[_Scalar],
        basis: Matrix[_Scalar] | GeneratorFamily[_Scalar],
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[_Scalar] | None = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
    def ambient_module(self) -> FreeModule_generic[_Scalar]: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...
    def echelonized_basis_matrix(self) -> Matrix[_Scalar]: ...

class FreeModule_submodule_pid(
    FreeModule_submodule_with_basis_pid[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: FreeModule_generic[_Scalar],
        gens: GeneratorFamily[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...

class FreeModule_submodule_with_basis_field(
    FreeModule_generic_field[_FieldScalar],
    FreeModule_submodule_with_basis_pid[_FieldScalar],
    Generic[_FieldScalar],
): ...

class FreeModule_submodule_field(
    FreeModule_submodule_with_basis_field[_FieldScalar],
    Generic[_FieldScalar],
): ...

from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.quotient_module import FreeModule_ambient_field_quotient
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
