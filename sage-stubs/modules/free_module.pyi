from collections.abc import Hashable, Iterable, Iterator, Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.categories.category import Category
from sage.categories.pushout import VectorFunctor
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.module import Module
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import FieldElement, RingElement
from sage.structure.factory import FactoryVersion, UniqueFactory
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_CodomainScalar = TypeVar("_CodomainScalar", bound=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)
_BasisKey = TypeVar("_BasisKey", bound=Hashable)

type ModuleRank = int | Integer
type MatrixSide = Literal["left", "right"]
type FreeModuleInput[_Scalar: RingElement] = (
    FreeModuleElement[_Scalar]
    | Sequence[ElementConstructorInput]
)
type GeneratorFamily[_Scalar: RingElement] = Iterable[FreeModuleInput[_Scalar]]
type MatrixData[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | Sequence[ElementConstructorInput]
    | ElementConstructorInput
)
type FreeModuleFactoryKey[_Scalar: RingElement] = tuple[
    Parent[_Scalar],
    int,
    bool,
    Matrix[_Scalar] | None,
]


class FreeModuleFactory(UniqueFactory):
    def create_key(
        self,
        base_ring: Parent[_Scalar],
        rank: ModuleRank,
        sparse: bool = ...,
        inner_product_matrix: MatrixData[_Scalar] | None = ...,
    ) -> FreeModuleFactoryKey[_Scalar]: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: FreeModuleFactoryKey[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...


FreeModuleFactory_with_standard_basis: FreeModuleFactory


@overload
def FreeModule(
    base_ring: Parent[_Scalar],
    rank_or_basis_keys: ModuleRank,
    sparse: bool = ...,
    inner_product_matrix: MatrixData[_Scalar] | None = ...,
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
    inner_product_matrix: None = ...,
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
    inner_product_matrix: None = ...,
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
    inner_product_matrix: MatrixData[_FieldScalar] | None = ...,
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
    inner_product_matrix: None = ...,
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
    inner_product_matrix: None = ...,
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
) -> Module_free_ambient[_Scalar]: ...
def vector_space(
    span: GeneratorFamily[_FieldScalar],
    base_ring: Parent[_FieldScalar] | None = ...,
    check: bool = ...,
    already_echelonized: bool = ...,
) -> FreeModule_generic_field[_FieldScalar]: ...
def is_FreeModule(x: object) -> bool: ...


class Module_free_ambient(
    Module[_Scalar, FreeModuleElement[_Scalar]],
    Generic[_Scalar],
):
    Element: type[FreeModuleElement[_Scalar]]

    def __init__(
        self,
        base_ring: Parent[_Scalar],
        degree: ModuleRank,
        sparse: bool = ...,
        category: Category | None = ...,
    ) -> None: ...
    def _element_constructor_(
        self,
        x: FreeModuleInput[_Scalar] | int | Integer = ...,
        coerce: bool = ...,
        copy: bool = ...,
        check: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def _check_element_membership(self, x: FreeModuleInput[_Scalar]) -> None: ...
    def degree(self) -> int: ...
    def is_sparse(self) -> bool: ...
    def is_exact(self) -> bool: ...
    def _an_element_(self) -> FreeModuleElement[_Scalar]: ...
    def some_elements(self) -> list[FreeModuleElement[_Scalar]]: ...
    def coordinate_ring(self) -> Parent[_Scalar]: ...
    def zero_vector(self) -> FreeModuleElement[_Scalar]: ...
    def zero(self) -> FreeModuleElement[_Scalar]: ...
    def zero_submodule(self) -> Module_free_ambient[_Scalar]: ...
    def relations_matrix(self) -> Matrix[RingElement]: ...
    def __richcmp__(self, other: object, op: int) -> bool: ...
    def _eq(self, other: Module_free_ambient[_Scalar]) -> bool: ...
    def is_submodule(self, other: Module_free_ambient[_Scalar]) -> bool: ...
    def ambient_module(self) -> Module_free_ambient[_Scalar]: ...
    def span(
        self,
        gens: GeneratorFamily[_Scalar] | Module_free_ambient[_Scalar],
        base_ring: Parent[_Scalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> Module_free_ambient[_Scalar]: ...
    def submodule(
        self,
        gens: GeneratorFamily[_Scalar] | Module_free_ambient[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> Module_free_ambient[_Scalar]: ...
    def quotient_module(
        self,
        sub: Module_free_ambient[_Scalar] | GeneratorFamily[_Scalar],
        check: bool = ...,
    ) -> QuotientModule_free_ambient[_Scalar]: ...
    quotient = quotient_module
    def __truediv__(
        self,
        sub: Module_free_ambient[_Scalar] | GeneratorFamily[_Scalar],
    ) -> QuotientModule_free_ambient[_Scalar]: ...
    def free_resolution(
        self,
        *args: object,
        **kwds: object,
    ) -> FreeResolution[_Scalar]: ...
    def graded_free_resolution(
        self,
        *args: object,
        **kwds: object,
    ) -> GradedFiniteFreeResolution[_Scalar]: ...


class FreeModule_generic(
    Module_free_ambient[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        rank: ModuleRank,
        degree: ModuleRank,
        sparse: bool = ...,
        coordinate_ring: Parent | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def construction(self) -> tuple[VectorFunctor, Parent[_Scalar]]: ...
    def _Hom_(
        self,
        codomain: FreeModule_generic[_CodomainScalar],
        category: Category | None = ...,
    ) -> FreeModuleHomspace[_Scalar, _CodomainScalar]: ...
    def dense_module(self) -> FreeModule_generic[_Scalar]: ...
    def _dense_module(self) -> FreeModule_generic[_Scalar]: ...
    def sparse_module(self) -> FreeModule_generic[_Scalar]: ...
    def _sparse_module(self) -> FreeModule_generic[_Scalar]: ...
    def _element_constructor_(
        self,
        x: FreeModuleInput[_Scalar] | int | Integer = ...,
        coerce: bool = ...,
        copy: bool = ...,
        check: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    def _eq(self, other: FreeModule_generic[_Scalar]) -> bool: ...
    def rank(self) -> int: ...
    def dimension(self) -> int: ...
    def codimension(self) -> int: ...
    def is_ambient(self) -> bool: ...
    def is_dense(self) -> bool: ...
    def is_full(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def cardinality(self) -> Integer | PlusInfinity: ...
    def ngens(self) -> int: ...
    def gen(self, i: int | Integer = ...) -> FreeModuleElement[_Scalar]: ...
    def gens(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def basis(self) -> Sequence[FreeModuleElement[_Scalar]]: ...
    def basis_matrix(self, ring: Parent | None = ...) -> Matrix[RingElement]: ...
    def echelonized_basis_matrix(self) -> Matrix[RingElement]: ...
    def matrix(self) -> Matrix[RingElement]: ...
    def coordinates(
        self,
        v: FreeModuleInput[_Scalar],
        check: bool = ...,
    ) -> list[RingElement]: ...
    def coordinate_vector(
        self,
        v: FreeModuleInput[_Scalar],
        check: bool = ...,
    ) -> FreeModuleElement[RingElement]: ...
    def coordinate_module(
        self,
        V: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def linear_combination_of_basis(
        self,
        coefficients: Sequence[ElementConstructorInput],
    ) -> FreeModuleElement[_Scalar]: ...
    def ambient_vector_space(self) -> FreeModule_generic_field[FieldElement]: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    def base_extend(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    def direct_sum(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def dual_module(self) -> FreeModule_generic[_Scalar]: ...
    def discriminant(self) -> RingElement: ...
    def gram_matrix(self) -> Matrix[RingElement]: ...
    def inner_product_matrix(self) -> Matrix[_Scalar]: ...
    def _inner_product_is_dot_product(self) -> bool: ...
    def uses_ambient_inner_product(self) -> bool: ...
    def random_element(
        self,
        prob: float = ...,
        *args: object,
        **kwds: object,
    ) -> FreeModuleElement[_Scalar]: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...
    @overload
    def hom(
        self,
        images: Sequence[FreeModuleInput[_Scalar]] | Matrix[_Scalar],
        codomain: None = ...,
        side: MatrixSide = ...,
    ) -> FreeModuleMorphism[_Scalar, _Scalar]: ...
    @overload
    def hom(
        self,
        images: Sequence[FreeModuleInput[_CodomainScalar]] | Matrix[_CodomainScalar],
        codomain: FreeModule_generic[_CodomainScalar],
        side: MatrixSide = ...,
    ) -> FreeModuleMorphism[_Scalar, _CodomainScalar]: ...
    def pseudoHom(
        self,
        twist: PseudoTwist[_Scalar],
        codomain: FreeModule_generic[_Scalar] | None = ...,
    ) -> FreeModulePseudoHomspace[_Scalar]: ...
    def pseudohom(
        self,
        f: PseudoMorphismData[_Scalar],
        twist: PseudoTwist[_Scalar],
        codomain: FreeModule_generic[_Scalar] | None = ...,
        side: MatrixSide = ...,
    ) -> FreeModulePseudoMorphism[_Scalar, _Scalar]: ...
    def scale(
        self,
        other: ElementConstructorInput,
    ) -> FreeModule_generic[_Scalar]: ...
    def relations(self) -> Module_free_ambient[_Scalar]: ...


class FreeModule_generic_domain(
    FreeModule_generic[_Scalar],
    Generic[_Scalar],
):
    def __add__(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic_domain[_Scalar]: ...


class FreeModule_generic_pid(
    FreeModule_generic_domain[_Scalar],
    Generic[_Scalar],
):
    def span(
        self,
        gens: GeneratorFamily[_Scalar] | FreeModule_generic[_Scalar],
        base_ring: Parent[_Scalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_pid[_Scalar]: ...
    def submodule(
        self,
        gens: GeneratorFamily[_Scalar] | FreeModule_generic[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_pid[_Scalar]: ...
    def span_of_basis(
        self,
        basis: GeneratorFamily[_Scalar] | FreeModule_generic[_Scalar],
        base_ring: Parent[_Scalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_with_basis_pid[_Scalar]: ...
    def submodule_with_basis(
        self,
        basis: GeneratorFamily[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_with_basis_pid[_Scalar]: ...
    def zero_submodule(self) -> FreeModule_submodule_pid[_Scalar]: ...
    def index_in(self, other: FreeModule_generic[_Scalar]) -> RingElement: ...
    def intersection(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic_pid[_Scalar]: ...
    def denominator(self) -> RingElement: ...
    def saturation(self) -> FreeModule_generic_pid[_Scalar]: ...
    def index_in_saturation(self) -> RingElement: ...
    def vector_space_span(
        self,
        gens: GeneratorFamily[_Scalar],
        check: bool = ...,
    ) -> FreeModule_submodule_field[FieldElement]: ...
    def vector_space_span_of_basis(
        self,
        basis: GeneratorFamily[_Scalar],
        check: bool = ...,
    ) -> FreeModule_submodule_with_basis_field[FieldElement]: ...
    def quotient_module(
        self,
        sub: FreeModule_generic[_Scalar] | GeneratorFamily[_Scalar],
        check: bool = ...,
        **kwds: object,
    ) -> FGP_Module_class[_Scalar]: ...
    quotient = quotient_module
    def vector_space(
        self,
        base_field: Parent[_FieldScalar] | None = ...,
    ) -> FreeModule_generic_field[_FieldScalar | FieldElement]: ...


class FreeModule_generic_field(
    FreeModule_generic_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def _Hom_(
        self,
        codomain: FreeModule_generic[_CodomainScalar],
        category: Category | None = ...,
    ) -> FreeModuleHomspace[_FieldScalar, _CodomainScalar]: ...
    def span(
        self,
        gens: GeneratorFamily[_FieldScalar] | FreeModule_generic[_FieldScalar],
        base_ring: Parent[_FieldScalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_field[_FieldScalar]: ...
    def submodule(
        self,
        gens: GeneratorFamily[_FieldScalar] | FreeModule_generic[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_field[_FieldScalar]: ...
    subspace = submodule
    def span_of_basis(
        self,
        basis: GeneratorFamily[_FieldScalar] | FreeModule_generic[_FieldScalar],
        base_ring: Parent[_FieldScalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_with_basis_field[_FieldScalar]: ...
    def submodule_with_basis(
        self,
        basis: GeneratorFamily[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> FreeModule_submodule_with_basis_field[_FieldScalar]: ...
    subspace_with_basis = submodule_with_basis
    def zero_submodule(self) -> FreeModule_submodule_field[_FieldScalar]: ...
    def zero_subspace(self) -> FreeModule_submodule_field[_FieldScalar]: ...
    def intersection(
        self,
        other: FreeModule_generic[_FieldScalar],
    ) -> FreeModule_submodule_field[_FieldScalar]: ...
    def is_subspace(self, other: FreeModule_generic[_FieldScalar]) -> bool: ...
    def complement(self) -> FreeModule_submodule_field[_FieldScalar]: ...
    def vector_space(
        self,
        base_field: Parent[_NewScalar] | None = ...,
    ) -> FreeModule_generic_field[_FieldScalar | _NewScalar]: ...
    def quotient_module(
        self,
        sub: FreeModule_generic[_FieldScalar] | GeneratorFamily[_FieldScalar],
        check: bool = ...,
    ) -> FreeModule_ambient_field_quotient[_FieldScalar]: ...
    quotient = quotient_module
    def quotient_abstract(
        self,
        sub: FreeModule_generic[_FieldScalar] | GeneratorFamily[_FieldScalar],
        check: bool = ...,
        **kwds: object,
    ) -> tuple[
        FreeModule_ambient_field[_FieldScalar],
        FreeModuleMorphism[_FieldScalar, _FieldScalar],
        FreeModuleMorphism[_FieldScalar, _FieldScalar],
    ]: ...
    def linear_dependence(
        self,
        vectors: Sequence[FreeModuleElement[_FieldScalar]],
        zeros: Literal["left", "right"] = ...,
        check: bool = ...,
    ) -> list[FreeModuleElement[_FieldScalar]]: ...


class FreeModule_ambient(
    FreeModule_generic[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        rank: ModuleRank,
        sparse: bool = ...,
        coordinate_ring: Parent | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def is_ambient(self) -> bool: ...
    def ambient_module(self) -> FreeModule_ambient[_Scalar]: ...
    def basis(self) -> Sequence[FreeModuleElement[_Scalar]]: ...
    def basis_matrix(self, ring: Parent | None = ...) -> Matrix[RingElement]: ...
    def echelonized_basis_matrix(self) -> Matrix[RingElement]: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModule_ambient[_NewScalar]: ...


class FreeModule_ambient_domain(
    FreeModule_generic_domain[_Scalar],
    FreeModule_ambient[_Scalar],
    Generic[_Scalar],
):
    def ambient_vector_space(self) -> FreeModule_ambient_field[FieldElement]: ...


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
    def base_field(self) -> Parent[_FieldScalar]: ...


class RealDoubleVectorSpace_class(
    FreeModule_ambient_field[FieldElement],
):
    def __init__(self, n: ModuleRank) -> None: ...
    def coordinates(
        self,
        v: FreeModuleInput[FieldElement],
    ) -> FreeModuleInput[FieldElement]: ...


class ComplexDoubleVectorSpace_class(
    FreeModule_ambient_field[FieldElement],
):
    def __init__(self, n: ModuleRank) -> None: ...
    def coordinates(
        self,
        v: FreeModuleInput[FieldElement],
    ) -> FreeModuleInput[FieldElement]: ...


class FreeModule_submodule_with_basis_pid(
    FreeModule_generic_pid[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: FreeModule_ambient_pid[_Scalar],
        basis: Matrix[_Scalar] | GeneratorFamily[_Scalar],
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[_Scalar] | None = ...,
        already_echelonized: bool = ...,
        category: Category | None = ...,
    ) -> None: ...
    def ambient_module(self) -> FreeModule_ambient_pid[_Scalar]: ...
    def ambient(self) -> FreeModule_generic[_Scalar]: ...
    def basis(self) -> Sequence[FreeModuleElement[_Scalar]]: ...
    def basis_matrix(self, ring: Parent | None = ...) -> Matrix[RingElement]: ...
    def echelonized_basis(self) -> Sequence[FreeModuleElement[_Scalar]]: ...
    def echelonized_basis_matrix(self) -> Matrix[RingElement]: ...
    def user_to_echelon_matrix(self) -> Matrix[RingElement]: ...
    def echelon_to_user_matrix(self) -> Matrix[RingElement]: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...


class FreeModule_submodule_pid(
    FreeModule_submodule_with_basis_pid[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: FreeModule_ambient_pid[_Scalar],
        gens: GeneratorFamily[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
        category: Category | None = ...,
    ) -> None: ...


class FreeModule_submodule_with_basis_field(
    FreeModule_generic_field[_FieldScalar],
    FreeModule_submodule_with_basis_pid[_FieldScalar],
    Generic[_FieldScalar],
):
    def __init__(
        self,
        ambient: FreeModule_ambient_field[_FieldScalar],
        basis: Matrix[_FieldScalar] | GeneratorFamily[_FieldScalar],
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[_FieldScalar] | None = ...,
        already_echelonized: bool = ...,
        category: Category | None = ...,
    ) -> None: ...


class FreeModule_submodule_field(
    FreeModule_submodule_with_basis_field[_FieldScalar],
    Generic[_FieldScalar],
):
    def __init__(
        self,
        ambient: FreeModule_ambient_field[_FieldScalar],
        gens: GeneratorFamily[_FieldScalar],
        check: bool = ...,
        already_echelonized: bool = ...,
        category: Category | None = ...,
    ) -> None: ...


from sage.homology.free_resolution import FreeResolution
from sage.homology.graded_resolution import GradedFiniteFreeResolution
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.free_module_pseudohomspace import (
    FreeModulePseudoHomspace,
    PseudoMorphismData,
    PseudoTwist,
)
from sage.modules.free_module_pseudomorphism import FreeModulePseudoMorphism
from sage.modules.quotient_module import (
    FreeModule_ambient_field_quotient,
    QuotientModule_free_ambient,
)
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
