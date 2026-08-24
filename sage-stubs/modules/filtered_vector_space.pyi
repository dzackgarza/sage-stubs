from collections.abc import Iterable, Mapping, Sequence
from typing import Generic, TypeVar, overload

from sage.modules.free_module import (
    FreeModule_ambient_field,
    FreeModule_generic,
    FreeModule_generic_domain,
    FreeModule_submodule_field,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.quotient_module import FreeModule_ambient_field_quotient
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import FieldElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)
_NewScalar = TypeVar("_NewScalar", bound=FieldElement)

type FiltrationDegree = int | Integer | PlusInfinity | MinusInfinity
type FiltrationGenerator[_Scalar: FieldElement] = (
    Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar]
)
type GeneratorFiltration[_Scalar: FieldElement] = Mapping[
    FiltrationDegree,
    Iterable[FiltrationGenerator[_Scalar]],
]
type IndexedFiltration = Mapping[FiltrationDegree, Iterable[int | Integer]]
type FilteredVectorSpaceInput[_Scalar: FieldElement] = (
    int
    | Integer
    | GeneratorFiltration[_Scalar]
    | Iterable[FiltrationGenerator[_Scalar]]
)


def FilteredVectorSpace(
    arg1: FilteredVectorSpaceInput[_Scalar],
    arg2: FiltrationDegree | IndexedFiltration | None = ...,
    base_ring: Parent[_Scalar] = ...,
    check: bool = ...,
) -> FilteredVectorSpace_class[_Scalar]: ...
def normalize_degree(
    deg: FiltrationDegree,
) -> Integer | PlusInfinity | MinusInfinity: ...
def construct_from_dim_degree(
    dim: int | Integer,
    max_degree: FiltrationDegree | None,
    base_ring: Parent[_Scalar],
    check: bool,
) -> FilteredVectorSpace_class[_Scalar]: ...
def construct_from_generators(
    filtration: GeneratorFiltration[_Scalar],
    base_ring: Parent[_Scalar],
    check: bool,
) -> FilteredVectorSpace_class[_Scalar]: ...
def construct_from_generators_indices(
    generators: Iterable[FiltrationGenerator[_Scalar]],
    filtration: IndexedFiltration,
    base_ring: Parent[_Scalar],
    check: bool,
) -> FilteredVectorSpace_class[_Scalar]: ...


class FilteredVectorSpace_class(
    FreeModule_ambient_field[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        dim: int | Integer,
        generators: Sequence[FreeModuleElement[_Scalar]],
        filtration: Mapping[FiltrationDegree, Iterable[int | Integer]],
        check: bool = ...,
    ) -> None: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FilteredVectorSpace_class[_NewScalar]: ...
    def ambient_vector_space(self) -> FreeModule_ambient_field[_Scalar]: ...
    def is_constant(self) -> bool: ...
    def is_exhaustive(self) -> bool: ...
    def is_separating(self) -> bool: ...
    def support(self) -> tuple[Integer | PlusInfinity, ...]: ...
    def min_degree(self) -> Integer | PlusInfinity: ...
    def max_degree(self) -> Integer | MinusInfinity: ...
    def get_degree(
        self,
        d: FiltrationDegree,
    ) -> FreeModule_submodule_field[_Scalar]: ...
    def graded(
        self,
        d: FiltrationDegree,
    ) -> FreeModule_ambient_field_quotient[_Scalar]: ...
    def presentation(
        self,
    ) -> tuple[
        tuple[FreeModuleElement[_Scalar], ...],
        dict[Integer | PlusInfinity, tuple[Integer, ...]],
    ]: ...
    def _repr_field_name(self) -> str: ...
    def _repr_vector_space(self, dim: int | Integer) -> str: ...
    def _repr_degrees(
        self,
        min_deg: int | Integer,
        max_deg: int | Integer,
    ) -> list[str]: ...
    def _repr_(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def direct_sum(
        self,
        other: FilteredVectorSpace_class[_Scalar],
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    @overload
    def direct_sum(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    @overload
    def __add__(
        self,
        other: FilteredVectorSpace_class[_Scalar],
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    @overload
    def __add__(
        self,
        other: FreeModule_generic_domain[_Scalar],
    ) -> FreeModule_generic_domain[_Scalar]: ...
    def tensor_product(
        self,
        other: FilteredVectorSpace_class[_Scalar],
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def __mul__(
        self,
        other: FilteredVectorSpace_class[_Scalar],
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def _power_operation(
        self,
        n: int | Integer,
        operation: str,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def exterior_power(
        self,
        n: int | Integer,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def wedge(
        self,
        n: int | Integer,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def symmetric_power(
        self,
        n: int | Integer,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def dual(self) -> FilteredVectorSpace_class[_Scalar]: ...
    def shift(
        self,
        deg: int | Integer,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def random_deformation(
        self,
        epsilon: _Scalar | None = ...,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
