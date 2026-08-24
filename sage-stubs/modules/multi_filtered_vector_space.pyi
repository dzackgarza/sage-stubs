from collections.abc import Hashable, Mapping
from typing import Generic, TypeVar, overload

from sage.modules.filtered_vector_space import (
    FiltrationDegree,
    FilteredVectorSpace_class,
)
from sage.modules.free_module import (
    FreeModule_ambient_field,
    FreeModule_generic,
    FreeModule_submodule_field,
)
from sage.modules.quotient_module import FreeModule_ambient_field_quotient
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.sets.set import Set_generic
from sage.structure.element import FieldElement
from sage.structure.parent import Parent

_Key = TypeVar("_Key", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)
_NewScalar = TypeVar("_NewScalar", bound=FieldElement)


def MultiFilteredVectorSpace(
    arg: int | Integer | Mapping[_Key, FilteredVectorSpace_class[_Scalar]],
    base_ring: Parent[_Scalar] | None = ...,
    check: bool = ...,
) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...


class MultiFilteredVectorSpace_class(
    FreeModule_ambient_field[_Scalar],
    Generic[_Key, _Scalar],
):
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        dim: int | Integer,
        filtrations: Mapping[_Key, FilteredVectorSpace_class[_Scalar]],
        check: bool = ...,
    ) -> None: ...
    def index_set(self) -> Set_generic[_Key]: ...
    def change_ring(
        self,
        base_ring: Parent[_NewScalar],
    ) -> MultiFilteredVectorSpace_class[_Key, _NewScalar]: ...
    def ambient_vector_space(self) -> FreeModule_ambient_field[_Scalar]: ...
    def is_constant(self) -> bool: ...
    def is_exhaustive(self) -> bool: ...
    def is_separating(self) -> bool: ...
    def support(self) -> tuple[Integer | PlusInfinity, ...]: ...
    def min_degree(self) -> Integer | PlusInfinity: ...
    def max_degree(self) -> Integer | MinusInfinity: ...
    def get_filtration(
        self,
        key: _Key,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def get_degree(
        self,
        key: _Key,
        deg: FiltrationDegree,
    ) -> FreeModule_submodule_field[_Scalar]: ...
    def graded(
        self,
        key: _Key,
        deg: FiltrationDegree,
    ) -> FreeModule_ambient_field_quotient[_Scalar]: ...
    def _repr_(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @overload
    def direct_sum(
        self,
        other: MultiFilteredVectorSpace_class[_Key, _Scalar],
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    @overload
    def direct_sum(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    @overload
    def __add__(
        self,
        other: MultiFilteredVectorSpace_class[_Key, _Scalar],
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    @overload
    def __add__(
        self,
        other: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def tensor_product(
        self,
        other: MultiFilteredVectorSpace_class[_Key, _Scalar],
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def __mul__(
        self,
        other: MultiFilteredVectorSpace_class[_Key, _Scalar],
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def exterior_power(
        self,
        n: int | Integer,
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def wedge(
        self,
        n: int | Integer,
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def symmetric_power(
        self,
        n: int | Integer,
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def dual(self) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def shift(
        self,
        deg: int | Integer,
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
    def random_deformation(
        self,
        epsilon: _Scalar | None = ...,
    ) -> MultiFilteredVectorSpace_class[_Key, _Scalar]: ...
