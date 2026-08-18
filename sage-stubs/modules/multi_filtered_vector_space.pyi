from collections.abc import Hashable, Mapping
from typing import Generic, TypeVar

from sage.modules.filtered_vector_space import FilteredVectorSpace_class
from sage.modules.free_module import VectorSpace
from sage.structure.element import FieldElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)
_FiltrationIndex = TypeVar(
    "_FiltrationIndex",
    bound=Hashable,
    default=Hashable,
)


def MultiFilteredVectorSpace(
    vector_space: VectorSpace[_Scalar],
    filtrations: Mapping[
        _FiltrationIndex,
        FilteredVectorSpace_class[_Scalar],
    ],
) -> MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar]: ...


class MultiFilteredVectorSpace_class(
    Generic[_FiltrationIndex, _Scalar],
):
    def __init__(
        self,
        vector_space: VectorSpace[_Scalar],
        filtrations: Mapping[
            _FiltrationIndex,
            FilteredVectorSpace_class[_Scalar],
        ],
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def vector_space(self) -> VectorSpace[_Scalar]: ...
    def dimension(self) -> int: ...
    rank = dimension
    def filtration(
        self,
        index: _FiltrationIndex,
    ) -> FilteredVectorSpace_class[_Scalar]: ...
    def filtrations(
        self,
    ) -> dict[_FiltrationIndex, FilteredVectorSpace_class[_Scalar]]: ...
    def indices(self) -> tuple[_FiltrationIndex, ...]: ...
    def dual(
        self,
    ) -> MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar]: ...
    def direct_sum(
        self,
        other: MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar],
    ) -> MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar]: ...
    def tensor_product(
        self,
        other: MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar],
    ) -> MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar]: ...
    def symmetric_power(
        self,
        degree: int,
    ) -> MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar]: ...
    def exterior_power(
        self,
        degree: int,
    ) -> MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar]: ...
