from collections.abc import Iterable
from typing import Generic, TypeVar, overload

from sage.homology.chain_complex import ChainComplex_class
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class KoszulComplex(
    ChainComplex_class[Integer, _Scalar],
    UniqueRepresentation,
    Generic[_Scalar],
):
    @overload
    @staticmethod
    def __classcall_private__(
        cls: type[KoszulComplex[_Scalar]],
        R: Parent[_Scalar],
        elements: Iterable[_Scalar] | None = ...,
    ) -> KoszulComplex[_Scalar]: ...
    @overload
    @staticmethod
    def __classcall_private__(
        cls: type[KoszulComplex[_Scalar]],
        R: Iterable[_Scalar] | None = ...,
        elements: None = ...,
    ) -> KoszulComplex[_Scalar]: ...

    def __init__(
        self,
        R: Parent[_Scalar],
        elements: tuple[_Scalar, ...],
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def _repr_(self) -> str: ...
